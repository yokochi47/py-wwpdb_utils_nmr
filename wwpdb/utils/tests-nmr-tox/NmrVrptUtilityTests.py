##
# File: NmrVrptUtilityTests.py
# Date: 03-Oct-2026  M. Yokochi
#
# Test that an NmrVrptUtility instance is not a reference cycle (DAOTHER-7829, 9785): its workflow tasks used to be
# bound methods, so that the instance, and the coordinates, NMR data and report it holds, outlived it until a full
# garbage collection.
##
"""Test cases for the lifetime of NmrVrptUtility."""
import gc
import os
import sys
import unittest

# import commonsetup first: it mocks ConfigInfo, which ChemCompUtil reads when it is imported
if __package__ is None or __package__ == "":
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from commonsetup import TESTOUTPUT  # noqa: F401 pylint: disable=import-error,unused-import
else:
    from .commonsetup import TESTOUTPUT  # noqa: F401 pylint: disable=relative-beyond-top-level

from wwpdb.utils.nmr.NmrDpConstant import PYNMRSTAR_OBJ_KEY
from wwpdb.utils.nmr.NmrVrptUtility import NmrVrptUtility


class TestNmrVrptUtility(unittest.TestCase):

    def test_instance_is_freed_without_garbage_collection(self):
        held = ['stands in for a pynmrstar entry, the previous NMR unified data in nmr-str2str-deposit']
        enabled = gc.isenabled()
        gc.disable()
        try:
            vrpt = NmrVrptUtility()
            vrpt.addInput(name=PYNMRSTAR_OBJ_KEY, value=held, type='param')
            refs = sys.getrefcount(held)
            del vrpt
            self.assertEqual(sys.getrefcount(held), refs - 1)
        finally:
            if enabled:
                gc.enable()

    def test_tasks_keep_their_names(self):
        vrpt = NmrVrptUtility()
        tasks = getattr(vrpt, '_NmrVrptUtility__procTasksDict')['nmr-cs-validation']
        self.assertEqual([t.__name__ for t in tasks[:3]], ['__parseCoordinate', '__parseNmrData', '__parseNmrDpReport'])


if __name__ == "__main__":
    unittest.main()
