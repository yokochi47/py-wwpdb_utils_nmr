##
# File: BasePKCSParserListenerTests.py
# Date:  09-Oct-2026  M. Yokochi
#
# Updates:
# 09-Oct-2026  M. Yokochi - add a test for a None chain id (DAOTHER-7829)
# 09-Oct-2026  M. Yokochi - add a test for the base peak list listener of XEASY PROT (DAOTHER-7829)
##
"""Regression tests for assignCoordPolymerSequence{WithChainId,}WithoutCompId() of BasePKParserListener and
BaseCSParserListener.

In-loop sequence remap lookups overwrote the chain id (the restraint's one, or the one fixed by chain_id_remap),
so the assignment was recorded under chain None, or spread to every chain carrying that residue number
(DAOTHER-7829).
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

from wwpdb.utils.nmr.pk.BasePKParserListener import BasePKParserListener
from wwpdb.utils.nmr.cs.BaseCSParserListener import BaseCSParserListener
import wwpdb.utils.nmr.pk.XeasyPROTParserListener as xeasyProtListener


class _NefTranslatorStub:
    """ Every atom name is valid for every residue. """

    def get_valid_star_atom(self, compId, atomId, **kwargs):  # pylint: disable=unused-argument
        return [atomId], None, None


def _chain(chainId):
    return {'chain_id': chainId, 'auth_chain_id': chainId, 'seq_id': list(range(1, 11)),
            'auth_seq_id': list(range(1, 11)), 'comp_id': ['ALA'] * 10}


def _init_stub(listener, base, rstName, private):
    """ Set only the state the methods read, without coordinates. """

    listener.polySeq = None
    listener.reasons = None
    listener.f = []
    listener.nefT = _NefTranslatorStub()
    listener.no_extra_comment = True
    for name in (rstName, rstName + 'Failed', rstName + 'FailedAmbig'):
        setattr(listener, name, [])
    prefix = f'_{base.__name__}__'
    for name, value in {'allow_ext_seq': False, 'authSeqId': 'auth_seq_id',
                        'preferAuthSeqCount': 0, 'preferLabelSeqCount': 0, **private}.items():
        setattr(listener, prefix + name, value)


class _PK(BasePKParserListener):  # pylint: disable=abstract-method

    def __init__(self, polySeq, reasons):  # pylint: disable=super-init-not-called
        _init_stub(self, BasePKParserListener, 'polySeqRst',
                   {'altPolySeq': None, 'authToLabelSeq': {}, 'labelToAuthSeq': {}, 'coordUnobsRes': {}})
        self.polySeq, self.reasons = polySeq, reasons
        self.hasNonPolySeq = False

    def getRealChainSeqId(self, ps, seqId, compId=None, isPolySeq=True, isFirstTrial=True):  # pylint: disable=unused-argument
        return ps['auth_chain_id'], seqId, None

    def getCurrentSpectralPeak(self, *args, **kwargs):  # pylint: disable=unused-argument
        return ''

    def rst(self):
        return {ps['chain_id']: ps['seq_id'] for ps in self.polySeqRst}


class _CS(BaseCSParserListener):  # pylint: disable=abstract-method

    def __init__(self, polySeq, reasons):  # pylint: disable=super-init-not-called
        _init_stub(self, BaseCSParserListener, 'polySeqCs', {})
        self.polySeq, self.reasons = polySeq, reasons
        self.authToLabelSeq = self.labelToAuthSeq = {}

    def getRealChainSeqId(self, ps, seqId, compId=None, isPolySeq=True, isFirstTrial=True):  # pylint: disable=unused-argument
        return ps['auth_chain_id'], seqId, None

    def getCurrentAssignment(self, *args, **kwargs):  # pylint: disable=unused-argument
        return ''

    def rst(self):
        return {ps['chain_id']: ps['seq_id'] for ps in self.polySeqCs}


# the sequence remap knows residues 1-5 of chain B only
CHAIN_SEQ_ID_REMAP = {'chain_seq_id_remap': [{'chain_id': 'B', 'seq_id_dict': {i: i for i in range(1, 6)}}]}


class BasePKCSParserListenerTests(unittest.TestCase):

    def __listener(self, cls, chainIds, reasons):
        return cls([_chain(c) for c in chainIds], reasons)

    def test_with_chain_id_and_chain_seq_id_remap_miss(self):
        # the restraint's chain id must not be replaced by None when the remap lookup misses
        for cls in (_PK, _CS):
            for chainIds in (['A', 'B'], ['B', 'A']):
                with self.subTest(cls=cls.__name__, chainIds=chainIds):
                    listener = self.__listener(cls, chainIds, CHAIN_SEQ_ID_REMAP)
                    chainAssign = listener.assignCoordPolymerSequenceWithChainIdWithoutCompId('B', 7, 'CA', 0)
                    self.assertEqual((sorted(chainAssign), listener.rst()), ([('B', 7, 'ALA', True)], {'B': [7]}))

    def test_without_chain_id_and_chain_id_remap_hit(self):
        # the chain id fixed by chain_id_remap must survive a missed lookup of chain_seq_id_remap
        reasons = {'chain_id_remap': {7: {'chain_id': 'A', 'seq_id': 7}}}
        reasons.update(CHAIN_SEQ_ID_REMAP)
        for cls in (_PK, _CS):
            for chainIds in (['A', 'B'], ['B', 'A']):
                with self.subTest(cls=cls.__name__, chainIds=chainIds):
                    listener = self.__listener(cls, chainIds, reasons)
                    chainAssign = listener.assignCoordPolymerSequenceWithoutCompId(7, 'CA', 0)
                    self.assertEqual((sorted(chainAssign), listener.rst()), ([('A', 7, 'ALA', True)], {'A': [7]}))

    def test_with_chain_id_none(self):
        # callers fall back to assignCoordPolymerSequenceWithoutCompId() on no assignment, so a None chain must not assign:
        # that would pin the default segment id in extractPeakAssignment(), which XEASY PROT's bare base instance cannot store
        for cls in (_PK, _CS):
            with self.subTest(cls=cls.__name__):
                listener = self.__listener(cls, ['A', 'B'], None)
                self.assertEqual(listener.assignCoordPolymerSequenceWithChainIdWithoutCompId(None, 7, 'CA', 0), [])
                self.assertEqual((listener.rst(), listener.f), ({}, []))

    def test_without_reasons(self):
        # without any chain id, the restraint is ambiguous across the chains
        for cls in (_PK, _CS):
            with self.subTest(cls=cls.__name__):
                listener = self.__listener(cls, ['A', 'B'], None)
                chainAssign = listener.assignCoordPolymerSequenceWithoutCompId(7, 'CA', 0)
                self.assertEqual((sorted(chainAssign), listener.rst()),
                                 ([('A', 7, 'ALA', True), ('B', 7, 'ALA', True)], {'A': [7], 'B': [7]}))


class XeasyPROTBasePKTests(unittest.TestCase):

    def test_class_level_defaults_are_writable(self):
        # XEASY PROT drives a base peak list listener of its own; writing a class-level default outside __slots__ on a bare
        # BasePKParserListener raised AttributeError ('... object attribute ... is read-only')
        for cls, writable in ((BasePKParserListener, False), (getattr(xeasyProtListener, '_BasePKParserListener'), True)):
            with self.subTest(cls=cls.__module__):
                listener = object.__new__(cls)
                try:
                    setattr(listener, '_BasePKParserListener__defaultSegId', 'A')
                    self.assertTrue(writable)
                except AttributeError:
                    self.assertFalse(writable)


if __name__ == '__main__':
    unittest.main()
