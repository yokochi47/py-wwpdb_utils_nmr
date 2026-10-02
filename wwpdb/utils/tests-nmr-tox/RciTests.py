##
# File: RciTests.py
# Date: 17-Jun-2026  M. Yokochi
#
# Characterization (regression) test for wwpdb.utils.nmr.rci.RCI.
#
# It pins the exact numerical output of RCI.calculate() for a fixed, representative
# input so that refactoring of the (legacy) RCI module can be verified to preserve
# behavior.  The golden values below were captured from the pre-refactoring code
# (version v_1n_10_6_12_A).
##
"""Regression test cases for the Random Coil Index (RCI) calculation."""
import sys
import unittest

# import commonsetup first: it mocks ConfigInfo, which ChemCompUtil reads when it is imported
if __package__ is None or __package__ == "":
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from commonsetup import TESTOUTPUT  # noqa: F401 pylint: disable=import-error,unused-import
else:
    from .commonsetup import TESTOUTPUT  # noqa: F401 pylint: disable=relative-beyond-top-level

from wwpdb.utils.nmr.rci.RCI import RCI


def build_input():
    """Build a fixed, deterministic RCI input mirroring the format produced by
    NmrVrptUtility: an 18-residue peptide with backbone shifts (CA/CB/C/N/H/HA),
    one fully missing residue (a gap, seq_id 11) and one oxidized cysteine (seq_id 17).
    """

    seq = ["ALA", "GLY", "SER", "THR", "VAL", "LEU", "ILE", "LYS", "ARG",
           "GLU", "ASP", "ASN", "GLN", "HIS", "PHE", "TYR", "CYS", "MET"]
    bmrb_to_aa_list = [[comp_id, i + 1] for i, comp_id in enumerate(seq)]

    base = {"CA": 54.0, "CB": 30.0, "C": 176.0, "N": 120.0, "H": 8.3, "HA": 4.3}
    delta = {"CA": 0.7, "CB": 0.5, "C": 0.9, "N": 1.3, "H": 0.05, "HA": 0.08}

    assignment = []
    for comp_id, seq_id in bmrb_to_aa_list:
        if seq_id == 11:  # deliberate assignment gap
            continue
        for atom_id in ("CA", "CB", "C", "N", "H", "HA"):
            if atom_id == "CB" and comp_id == "GLY":  # glycine has no CB
                continue
            val = base[atom_id] + ((seq_id * 3 + 1) % 7) * delta[atom_id]
            assignment.append([comp_id, seq_id, atom_id, atom_id[0], round(val, 3)])

    B_Cys = [17]            # oxidized cysteine
    noshift_res = []        # no residues are flagged as shift-less
    return bmrb_to_aa_list, assignment, B_Cys, noshift_res


def build_small_input():
    """Build a short (8-residue) input, exercising the <= 10 residue branch of the
    grid search (the 18-residue case above exercises the > 10 residue branch).
    """

    seq = ["MET", "ALA", "VAL", "LEU", "SER", "GLY", "THR", "LYS"]
    bmrb_to_aa_list = [[comp_id, i + 1] for i, comp_id in enumerate(seq)]

    base = {"CA": 55.0, "CB": 31.0, "C": 175.5, "N": 121.0, "H": 8.2, "HA": 4.4}
    delta = {"CA": 0.6, "CB": 0.4, "C": 0.8, "N": 1.1, "H": 0.04, "HA": 0.07}

    assignment = []
    for comp_id, seq_id in bmrb_to_aa_list:
        for atom_id in ("CA", "CB", "C", "N", "H", "HA"):
            if atom_id == "CB" and comp_id == "GLY":
                continue
            val = base[atom_id] + ((seq_id * 2 + 3) % 5) * delta[atom_id]
            assignment.append([comp_id, seq_id, atom_id, atom_id[0], round(val, 3)])

    return bmrb_to_aa_list, assignment, [], []


# Golden output captured from RCI v_1n_10_6_12_A (pre-refactoring).
GOLDEN = {
    "seq_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    "rci": [0.008, 0.007, 0.007, 0.007, 0.009, 0.013, 0.019, 0.03, 0.037, 0.038,
            0.029, 0.022, 0.019, 0.02, 0.022, 0.025, 0.028, 0.028],
    "nmr_rmsd": [0.129, 0.115, 0.108, 0.108, 0.15, 0.212, 0.31, 0.49, 0.615, 0.624,
                 0.474, 0.354, 0.308, 0.327, 0.365, 0.414, 0.453, 0.466],
    "s2": [0.948, 0.953, 0.956, 0.956, 0.94, 0.918, 0.885, 0.831, 0.797, 0.794,
           0.835, 0.871, 0.885, 0.879, 0.867, 0.853, 0.841, 0.837],
}

GOLDEN_SMALL = {
    "seq_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "rci": [0.026, 0.023, 0.016, 0.013, 0.009, 0.007, 0.008, 0.009],
    "nmr_rmsd": [0.432, 0.379, 0.27, 0.209, 0.148, 0.119, 0.133, 0.154],
    "s2": [0.847, 0.863, 0.898, 0.919, 0.941, 0.952, 0.946, 0.939],
}


class RciTests(unittest.TestCase):
    def test_version(self):
        self.assertEqual(RCI().version, "v_1n_10_6_12_A")

    def test_calculate_matches_golden(self):
        bmrb_to_aa_list, assignment, B_Cys, noshift_res = build_input()
        result = RCI().calculate(bmrb_to_aa_list, assignment, B_Cys, noshift_res)

        self.assertEqual(set(result.keys()), set(GOLDEN.keys()))
        self.assertEqual(result["seq_id"], GOLDEN["seq_id"])
        for key in ("rci", "nmr_rmsd", "s2"):
            self.assertEqual(result[key], GOLDEN[key],
                             msg=f"'{key}' diverged from the golden RCI output")

    def test_calculate_small_matches_golden(self):
        bmrb_to_aa_list, assignment, B_Cys, noshift_res = build_small_input()
        result = RCI().calculate(bmrb_to_aa_list, assignment, B_Cys, noshift_res)

        self.assertEqual(result["seq_id"], GOLDEN_SMALL["seq_id"])
        for key in ("rci", "nmr_rmsd", "s2"):
            self.assertEqual(result[key], GOLDEN_SMALL[key],
                             msg=f"'{key}' diverged from the golden RCI output (small input)")


if __name__ == "__main__":
    unittest.main()
