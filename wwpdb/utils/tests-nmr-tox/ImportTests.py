##
# File: NEFImportTests.py
# Date:  06-Oct-2018  E. Peisach
#
# Updates:
# 30-Sep-2026  M. Yokochi - check that both branches of every try/except ImportError bind the same names (DAOTHER-9785)
##
"""Test cases for NefTranslator - simply import everything to ensure imports work"""
import ast
import glob
import os
import sys
import unittest

# import commonsetup first: it mocks ConfigInfo, which ChemCompUtil reads when it is imported
if __package__ is None or __package__ == "":
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from commonsetup import TESTOUTPUT  # noqa:  F401 pylint: disable=import-error,unused-import
else:
    from .commonsetup import TESTOUTPUT  # noqa: F401 pylint: disable=relative-beyond-top-level

from wwpdb.utils.nmr.BmrbChemShiftStat import BmrbChemShiftStat
from wwpdb.utils.nmr.NmrDpUtility import NmrDpUtility
from wwpdb.utils.nmr.NmrDpReport import NmrDpReport
from wwpdb.utils.nmr.nef.NefTranslator import NefTranslator
from wwpdb.utils.nmr.rci.RCI import RCI


class ImportTests(unittest.TestCase):
    def testInstantiate(self):  # pylint: disable=no-self-use
        _c = NefTranslator()  # noqa: F841
        _npu = NmrDpUtility()  # noqa: F841
        _ndp = NmrDpReport()  # noqa: F841
        # _nstc = NmrStarToCif()  # noqa: F841
        _rci = RCI()  # noqa: F841
        _bmrb = BmrbChemShiftStat()  # noqa: F841

    def testDualImportSymmetry(self):
        # Every module imports its siblings as wwpdb.utils.nmr.X in the try branch and as nmr.X in the
        # except ImportError branch (standalone mode, e.g. the Docker image). CI imports only the first, so
        # a name bound in one branch alone surfaces as a NameError only in production.
        allowed = {'ChemCompUtil.py': {'ConfigInfoAppCc', 'getSiteId'}}  # wwpdb.utils.config has no standalone twin

        pkg_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'nmr')
        asymmetric = []

        for mod_path in sorted(glob.glob(os.path.join(pkg_dir, '**', '*.py'), recursive=True)):
            if os.sep + 'obsolete' + os.sep in mod_path:
                continue
            with open(mod_path, 'r', encoding='utf-8') as ifh:
                tree = ast.parse(ifh.read(), filename=mod_path)
            for node in ast.walk(tree):
                if not isinstance(node, ast.Try):
                    continue
                handlers = [h for h in node.handlers if isinstance(h.type, ast.Name) and h.type.id == 'ImportError']
                if not handlers:
                    continue

                def bound(body):
                    return {a.asname or a.name.split('.')[0] for n in body if isinstance(n, (ast.Import, ast.ImportFrom))
                            for a in n.names}

                in_try, in_except = bound(node.body), bound(handlers[0].body)
                if not in_try or not in_except:
                    continue
                diff = (in_try ^ in_except) - allowed.get(os.path.basename(mod_path), set())
                if diff:
                    asymmetric.append(f"{os.path.relpath(mod_path, pkg_dir)}:{node.lineno} {sorted(diff)}")

        self.assertEqual(asymmetric, [], "names bound in only one branch of try/except ImportError")


if __name__ == "__main__":
    unittest.main()
