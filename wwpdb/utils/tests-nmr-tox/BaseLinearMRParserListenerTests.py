##
# File: BaseLinearMRParserListenerTests.py
# Date:  07-Oct-2026  M. Yokochi
#
# Updates:
# 08-Oct-2026  M. Yokochi - add tests for assignCoordPolymerSequenceWithoutCompId() (DAOTHER-7829)
# 08-Oct-2026  M. Yokochi - add a test for a restraint without chain id (DAOTHER-7829)
##
"""Regression tests for BaseLinearMRParserListener.assignCoordPolymerSequence{WithChainId,}WithoutCompId().

A sequence remap lookup that missed returned None and overwrote the restraint's chain id, or the chain id
fixed by chain_id_remap, so the restraint was assigned to every coordinate chain carrying that residue
number and recorded in the polymer sequence of the restraint file under chain None (DAOTHER-7829).
"""
import sys
import unittest

# import commonsetup first: it mocks ConfigInfo, which ChemCompUtil reads when it is imported
if __package__ is None or __package__ == "":
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from commonsetup import TESTOUTPUT  # noqa: F401 pylint: disable=import-error,unused-import
else:
    from .commonsetup import TESTOUTPUT  # noqa: F401 pylint: disable=relative-beyond-top-level

from wwpdb.utils.nmr.mr.BaseLinearMRParserListener import BaseLinearMRParserListener

_P = '_BaseLinearMRParserListener__'


class _NefTranslatorStub:
    """ Every atom name is valid for every residue. """

    def get_valid_star_atom(self, compId, atomId):  # pylint: disable=unused-argument
        return [atomId], None, None


class _ListenerStub(BaseLinearMRParserListener):
    """ Only the state assignCoordPolymerSequence{WithChainId,}WithoutCompId() read, without coordinates. """

    __slots__ = ('allow_ext_seq', 'software_name')

    def __init__(self, polySeq, reasons):  # pylint: disable=super-init-not-called
        self.polySeq = polySeq
        self.reasons = reasons
        self.f = []
        self.hasNonPolySeq = False
        self.authToLabelSeq = {}
        self.nefT = _NefTranslatorStub()
        self.software_name = 'BARE'
        self.allow_ext_seq = False
        for name, value in {'polySeqRst': [], 'polySeqRstFailed': [], 'polySeqRstFailedAmbig': [],
                            'nonPolySeq': None, 'altPolySeq': None, 'labelToAuthSeq': {}, 'coordUnobsRes': {},
                            'preferAuthSeqCount': 0, 'preferLabelSeqCount': 0,
                            'multiPolymer': True, 'monoPolymer': False}.items():
            setattr(self, _P + name, value)

    def getRealChainSeqId(self, ps, seqId, compId=None, isPolySeq=True, isFirstTrial=True):  # pylint: disable=unused-argument
        return ps['auth_chain_id'], seqId, None

    def getCurrentRestraint(self, *args, **kwargs):  # pylint: disable=unused-argument
        return ''

    def polySeqRst(self):
        return {ps['chain_id']: ps['seq_id'] for ps in getattr(self, _P + 'polySeqRst')}


def _chain(chainId):
    return {'chain_id': chainId, 'auth_chain_id': chainId, 'seq_id': list(range(1, 11)),
            'auth_seq_id': list(range(1, 11)), 'comp_id': ['ALA'] * 10}


# the sequence remap knows residues 1-5 of chain B only
CHAIN_SEQ_ID_REMAP = {'chain_seq_id_remap': [{'chain_id': 'B', 'seq_id_dict': {i: i for i in range(1, 6)}}]}


class BaseLinearMRParserListenerTests(unittest.TestCase):

    def __assign(self, chainIds, reasons, chainId, seqId):
        listener = _ListenerStub([_chain(c) for c in chainIds], reasons)
        chainAssign = listener.assignCoordPolymerSequenceWithChainIdWithoutCompId(chainId, seqId, 'CA')
        return sorted(chainAssign), listener.polySeqRst()

    def test_without_reasons(self):
        self.assertEqual(self.__assign(['A', 'B'], None, 'B', 7),
                         ([('B', 7, 'ALA', True)], {'B': [7]}))

    def test_chain_seq_id_remap_hit(self):
        self.assertEqual(self.__assign(['B', 'A'], CHAIN_SEQ_ID_REMAP, 'B', 3),
                         ([('B', 3, 'ALA', True)], {'B': [3]}))

    def test_chain_seq_id_remap_miss(self):
        # the result must not depend on the order of the coordinate chains
        for chainIds in (['A', 'B'], ['B', 'A']):
            with self.subTest(chainIds=chainIds):
                self.assertEqual(self.__assign(chainIds, CHAIN_SEQ_ID_REMAP, 'B', 7),
                                 ([('B', 7, 'ALA', True)], {'B': [7]}))

    def test_chain_id_remap_hit(self):
        # a remapped chain id still redirects the restraint
        reasons = {'chain_id_remap': {7: {'chain_id': 'A', 'seq_id': 7}}}
        self.assertEqual(self.__assign(['A', 'B'], reasons, 'B', 7),
                         ([('A', 7, 'ALA', True)], {'A': [7]}))

    def test_chain_id_remap_miss(self):
        reasons = {'chain_id_remap': {1: {'chain_id': 'A', 'seq_id': 1}}}
        self.assertEqual(self.__assign(['A', 'B'], reasons, 'B', 7),
                         ([('B', 7, 'ALA', True)], {'B': [7]}))

    def test_without_chain_id(self):
        # callers such as BIOSYM pass None for a chain absent from the coordinates: the restraint is then ambiguous
        # across the chains, as in assignCoordPolymerSequenceWithoutCompId(), instead of being recorded under chain None
        self.assertEqual(self.__assign(['A', 'B'], None, None, 7),
                         ([('A', 7, 'ALA', True), ('B', 7, 'ALA', True)], {'A': [7], 'B': [7]}))


class BaseLinearMRParserListenerWithoutChainIdTests(unittest.TestCase):

    def __assign(self, chainIds, reasons, seqId):
        listener = _ListenerStub([_chain(c) for c in chainIds], reasons)
        chainAssign = listener.assignCoordPolymerSequenceWithoutCompId(seqId, 'CA')
        return sorted(chainAssign), listener.polySeqRst()

    def test_without_reasons(self):
        # without any chain id, the restraint is ambiguous across the chains
        self.assertEqual(self.__assign(['A', 'B'], None, 7),
                         ([('A', 7, 'ALA', True), ('B', 7, 'ALA', True)], {'A': [7], 'B': [7]}))

    def test_chain_id_remap_hit(self):
        reasons = {'chain_id_remap': {7: {'chain_id': 'A', 'seq_id': 7}}}
        self.assertEqual(self.__assign(['A', 'B'], reasons, 7),
                         ([('A', 7, 'ALA', True)], {'A': [7]}))

    def test_chain_id_remap_hit_with_chain_seq_id_remap_miss(self):
        # the chain id fixed by chain_id_remap must survive a missed lookup of chain_seq_id_remap,
        # whatever the order of the coordinate chains
        reasons = {'chain_id_remap': {7: {'chain_id': 'A', 'seq_id': 7}}}
        reasons.update(CHAIN_SEQ_ID_REMAP)
        for chainIds in (['A', 'B'], ['B', 'A']):
            with self.subTest(chainIds=chainIds):
                self.assertEqual(self.__assign(chainIds, reasons, 7),
                                 ([('A', 7, 'ALA', True)], {'A': [7]}))


if __name__ == '__main__':
    unittest.main()
