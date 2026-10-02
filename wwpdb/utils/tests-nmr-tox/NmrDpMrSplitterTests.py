##
# File: NmrDpMrSplitterTests.py
# Date: 03-Oct-2026  M. Yokochi
#
# Test the content-subtype heuristic for light-weight restraint files (DAOTHER-7829): restraint lines must not be
# taken for chemical shifts when exactly one of their atom names is chemical shift-like.
##
"""Test cases for the text scan of NmrDpMrSplitter on light-weight restraint files."""
import os
import sys
import types
import unittest

# import commonsetup first: it mocks ConfigInfo, which ChemCompUtil reads when it is imported
if __package__ is None or __package__ == "":
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from commonsetup import TESTOUTPUT  # noqa: F401 pylint: disable=import-error,unused-import
else:
    from .commonsetup import TESTOUTPUT  # noqa: F401 pylint: disable=relative-beyond-top-level

from wwpdb.utils.nmr.BmrbChemShiftStat import BmrbChemShiftStat
from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
from wwpdb.utils.nmr.NmrDpMrSplitter import MrContentFlags, NmrDpMrSplitter

# hydrogen bond restraints: O is atom-like, HN is the only chemical shift-like name, and 1.9 lies in CS_RANGE
HBOND_TEXT = """! hydrogen bonds
assign (resid 23 and name O) (resid 27 and name HN) 1.9 0.1 0.1
assign (resid 24 and name O) (resid 28 and name HN) 1.9 0.1 0.1
assign (resid 25 and name O) (resid 29 and name HN) 1.9 0.1 0.1
"""

# dihedral angle restraints, rows of a NEF dihedral restraint loop (1pqx, column padding removed): a residue name and
# the angle name make the line dihedral-like, while CA is the only chemical shift-like atom name and the angles lie in CS_RANGE
DIHED_TEXT = """1 1 . A 2 LYS C A 3 ILE N A 3 ILE CA A 3 ILE C 1.00 -40.000 0.000 -170.000 90.000 PHI
2 2 . A 3 ILE C A 4 ILE N A 4 ILE CA A 4 ILE C 1.00 -120.000 0.000 -155.000 -85.000 PHI
3 3 . A 4 ILE C A 5 SER N A 5 SER CA A 5 SER C 1.00 -35.000 0.000 180.000 110.000 PHI
"""

CS_TEXT = """1 MET HA 4.35
2 ALA HA 4.12
2 ALA CA 52.10
3 GLY N 108.50
"""


class TestNmrDpMrSplitterLightScan(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.splitter = NmrDpMrSplitter(types.SimpleNamespace(csStat=BmrbChemShiftStat(), ccU=ChemCompUtil(False)))

    def scan(self, text, name):
        path = os.path.join(TESTOUTPUT, name)
        with open(path, 'w', encoding='utf-8') as ofh:
            ofh.write(text)
        names = getattr(self.splitter, '_NmrDpMrSplitter__legacyMrAtomNames')('nm-res-oth', {})
        flags = MrContentFlags()
        getattr(self.splitter, '_NmrDpMrSplitter__scanLightMrAndAuxTop')(path, 'nm-res-oth', names, flags)
        return flags

    def test_hydrogen_bond_restraints_are_not_chemical_shifts(self):
        flags = self.scan(HBOND_TEXT, 'light_scan_hbond.txt')
        self.assertTrue(flags.has_dist_restraint)
        self.assertFalse(flags.has_chem_shift)

    def test_dihedral_angle_restraints_are_not_chemical_shifts(self):
        flags = self.scan(DIHED_TEXT, 'light_scan_dihed.txt')
        self.assertTrue(flags.has_dihed_restraint)
        self.assertFalse(flags.has_chem_shift)

    def test_chemical_shifts_are_still_detected(self):
        flags = self.scan(CS_TEXT, 'light_scan_cs.txt')
        self.assertTrue(flags.has_chem_shift)
        self.assertFalse(flags.has_dist_restraint)
        self.assertFalse(flags.has_dihed_restraint)


if __name__ == "__main__":
    unittest.main()
