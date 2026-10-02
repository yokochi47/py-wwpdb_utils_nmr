##
# File: PseudoChemCompTests.py
# Date: 03-Oct-2026  M. Yokochi
#
# Test the pseudo CCD that is derived from the coordinates of a non-standard residue (DAOTHER-8817):
# heavy atoms are bonded by covalent radii, and ambiguity code 3 (ring flip) is guessed in reference to
# phenylalanine, using the ideal and model coordinates of the test CCD without its bond table.
##
"""Test cases for buildPseudoChemCompBond(), isFlippableRingProtonHost() and their use by NefTranslator."""
import glob
import os
import sys
import unittest

import numpy

from mmcif.io.PdbxReader import PdbxReader

# import commonsetup first: it mocks ConfigInfo, which ChemCompUtil reads when it is imported
if __package__ is None or __package__ == "":
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from commonsetup import HERE, TESTOUTPUT  # noqa: F401 pylint: disable=import-error,unused-import
else:
    from .commonsetup import HERE, TESTOUTPUT  # noqa: F401 pylint: disable=relative-beyond-top-level

from wwpdb.utils.nmr.mr.ParserListenerUtil import (buildPseudoChemCompBond,
                                                   isFlippableRingProtonHost)
from wwpdb.utils.nmr.nef.NefTranslator import NefTranslator

CCD_DIR = os.path.join(HERE, 'data', 'components', 'ligand-dict-v3')

# heavy atoms whose proton has ambiguity code 3
RING_FLIP_HOSTS = {'PHE': ['CD1', 'CD2', 'CE1', 'CE2'],
                   'TYR': ['CD1', 'CD2', 'CE1', 'CE2']}


def read_residue(compId, coordKind='pdbx_model_Cartn_{}_ideal'):
    """Return the atom_ids, type_symbols, coordinates and CCD bonds of a CCD file of the test data."""

    containerList = []
    with open(os.path.join(CCD_DIR, compId[0], compId, f'{compId}.cif'), 'r', encoding='utf-8') as ifh:
        PdbxReader(ifh).read(containerList)
    atoms = containerList[0].getObj('chem_comp_atom')
    bonds = containerList[0].getObj('chem_comp_bond')

    atomIds, typeSymbols, coords = [], [], {}
    for row in atoms.getRowList():
        try:
            xyz = numpy.array([float(row[atoms.getAttributeIndex(coordKind.format(c))]) for c in 'xyz'])
        except (ValueError, TypeError):
            continue
        atomId = row[atoms.getAttributeIndex('atom_id')]
        atomIds.append(atomId)
        typeSymbols.append(row[atoms.getAttributeIndex('type_symbol')])
        coords[atomId] = xyz

    ccdBonds = set()
    if bonds is not None:
        for row in bonds.getRowList():
            ccdBonds.add(frozenset((row[bonds.getAttributeIndex('atom_id_1')], row[bonds.getAttributeIndex('atom_id_2')])))

    return atomIds, typeSymbols, coords, ccdBonds


def ring_flip_hosts(atomIds, typeSymbols, coords):
    """Return the heavy atoms with one proton that isFlippableRingProtonHost() accepts."""

    bond, topo = buildPseudoChemCompBond(atomIds, typeSymbols, coords)
    return sorted(k for k, v in bond.items() if len(v) == 1 and k[0] == 'C' and isFlippableRingProtonHost(topo, bond, k))


class TestPseudoChemComp(unittest.TestCase):

    def test_heavy_atom_bonds_match_ccd(self):
        # a flat 2.5 A cutoff also bonded most atoms two bonds apart, e.g. CG-CE1 of PHE
        for compId in ('PHE', 'TYR', 'TRP', 'HIS'):
            with self.subTest(compId=compId):
                atomIds, typeSymbols, coords, ccdBonds = read_residue(compId)
                _, topo = buildPseudoChemCompBond(atomIds, typeSymbols, coords)
                found = {frozenset((a, b)) for a, nbrs in topo.items() for b in nbrs}
                heavy = {a for a, t in zip(atomIds, typeSymbols) if t != 'H'}
                expected = {p for p in ccdBonds if p <= heavy}
                self.assertEqual(found, expected)

    def test_ring_flip_hosts_in_reference_to_phenylalanine(self):
        for coordKind in ('pdbx_model_Cartn_{}_ideal', 'model_Cartn_{}'):
            for compId in ('PHE', 'TYR', 'TRP', 'HIS'):
                with self.subTest(compId=compId, coordKind=coordKind):
                    atomIds, typeSymbols, coords, _ = read_residue(compId, coordKind)
                    self.assertEqual(ring_flip_hosts(atomIds, typeSymbols, coords), RING_FLIP_HOSTS.get(compId, []))

    def test_no_ring_flip_hosts_elsewhere(self):
        # e.g. nucleotides, heme and the ring CH of tryptophan are not flippable rings
        for path in sorted(glob.glob(os.path.join(CCD_DIR, '*', '*', '*.cif'))):
            compId = os.path.basename(path)[:-4]
            if compId in RING_FLIP_HOSTS:
                continue
            with self.subTest(compId=compId):
                atomIds, typeSymbols, coords, _ = read_residue(compId)
                if len(atomIds) > 0:
                    self.assertEqual(ring_flip_hosts(atomIds, typeSymbols, coords), [])

    def test_nef_translator_guesses_ambiguity_code_from_pseudo_ccd(self):
        # phenylalanine under a comp_id unknown to the CCD, so that NefTranslator falls back to the pseudo CCD
        atomIds, typeSymbols, coords, _ = read_residue('PHE')
        bond, topo = buildPseudoChemCompBond(atomIds, typeSymbols, coords)
        compId = 'ZPH'
        neft = NefTranslator()
        neft.set_chem_comp_dict({compId: atomIds}, {compId: bond}, {compId: topo}, {})
        coordAtomSite = {'atom_id': atomIds, 'alt_atom_id': atomIds}
        for nefAtom, expected in (('HD%', (['HD1', 'HD2'], 3)),
                                  ('HE%', (['HE1', 'HE2'], 3)),
                                  ('HZ', (['HZ'], 1)),
                                  ('HB%', (['HB2', 'HB3'], 2))):
            with self.subTest(nefAtom=nefAtom):
                self.assertEqual(neft.get_star_atom_for_ligand_remap(compId, nefAtom, None, coordAtomSite)[:2], expected)


if __name__ == "__main__":
    unittest.main()
