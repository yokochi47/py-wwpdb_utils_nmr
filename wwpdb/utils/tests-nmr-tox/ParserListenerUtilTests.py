##
# File: ParserListenerUtilTests.py
# Date:  24-Sep-2026  M. Yokochi
#
# Updates:
##
"""Test cases for the minimal-copy helpers of ParserListenerUtil and their optional C accelerator.

These run against the pure-Python bodies everywhere, and additionally assert that the compiled
implementation agrees with them wherever wwpdb/utils/nmr/mr/c_listener_util was built
(DAOTHER-10315).
"""
import random
import sys
import unittest

# import commonsetup first: it mocks ConfigInfo, which ChemCompUtil reads when it is imported
if __package__ is None or __package__ == "":
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from commonsetup import TESTOUTPUT  # noqa: F401 pylint: disable=import-error,unused-import
else:
    from .commonsetup import TESTOUTPUT  # noqa: F401 pylint: disable=relative-beyond-top-level

from wwpdb.utils.nmr.mr.ParserListenerUtil import (USE_C_IMPLEMENTATION,
                                                   atomKey, atomKeyPy,
                                                   copyFactor, copyFactorPy,
                                                   copyPolySeq, copyPolySeqPy,
                                                   factorKey, factorKeyPy)

SCALARS = ["A", "HB2", 12, -3, 0, True, False, None, 1.25, "", "*"]

ATOM_KEYS = ["chain_id", "seq_id", "comp_id", "atom_id", "auth_atom_id",
             "is_poly", "segment_id", "type_symbol", "x", "y", "z"]

FACTOR_KEYS = ["chain_id", "seq_id", "seq_ids", "comp_id", "atom_id", "atom_ids", "type_symbol",
               "atom_selection", "segment_id", "alt_chain_id", "atom_not_specified", "seq_not_specified"]


class _DictSubclass(dict):
    pass


class _ListSubclass(list):
    pass


def _randomAtom(rnd):
    keys = rnd.sample(ATOM_KEYS, rnd.randint(0, len(ATOM_KEYS)))
    return {k: rnd.choice(SCALARS) for k in keys}


def _randomValue(rnd):
    r = rnd.random()
    if r < 0.35:
        return [_randomAtom(rnd) for _ in range(rnd.randint(0, 6))]
    if r < 0.50:
        return [rnd.choice(SCALARS) for _ in range(rnd.randint(0, 6))]
    if r < 0.58:
        return _ListSubclass([_randomAtom(rnd), 1])
    if r < 0.66:
        return [_DictSubclass(a=1), {"b": 2}]
    if r < 0.72:
        return []
    return rnd.choice(SCALARS)


def _randomFactor(rnd):
    keys = rnd.sample(FACTOR_KEYS, rnd.randint(0, len(FACTOR_KEYS)))
    return {k: _randomValue(rnd) for k in keys}


class ParserListenerUtilTests(unittest.TestCase):

    def testCopyFactorDepth(self):
        """ copyFactor() copies exactly two levels: the factor, its list values, and the exact
            dictionaries inside them. Anything else is shared, as deepcopy() never was.
        """

        atom = {"chain_id": "A", "seq_id": 1, "comp_id": "ALA", "atom_id": "HB2"}
        shared = _DictSubclass(chain_id="B")
        factor = {"chain_id": ["A"], "segment_id": "PROT", "atom_selection": [atom, "*", shared]}

        copied = copyFactor(factor)

        self.assertEqual(copied, factor)
        self.assertIsNot(copied["atom_selection"], factor["atom_selection"])
        self.assertIsNot(copied["atom_selection"][0], atom)
        self.assertIs(copied["atom_selection"][1], factor["atom_selection"][1])
        self.assertIs(copied["atom_selection"][2], shared, "a dict subclass takes the borrow path")
        self.assertIs(copied["segment_id"], factor["segment_id"])

        copied["atom_selection"][0]["segment_id"] = "NOT PROT"
        del copied["chain_id"]
        copied["atom_selection"].append({})

        self.assertEqual(atom, {"chain_id": "A", "seq_id": 1, "comp_id": "ALA", "atom_id": "HB2"})
        self.assertEqual(len(factor["atom_selection"]), 3)
        self.assertIn("chain_id", factor)

    def testCopyPolySeqDepth(self):
        polySeq = [{"auth_chain_id": "A", "seq_id": [1, 2, 3], "comp_id": ["ALA", "GLY", "SER"]}]

        copied = copyPolySeq(polySeq)

        self.assertEqual(copied, polySeq)
        self.assertIsNot(copied[0], polySeq[0])
        self.assertIsNot(copied[0]["seq_id"], polySeq[0]["seq_id"])
        self.assertIs(copied[0]["auth_chain_id"], polySeq[0]["auth_chain_id"])

        copied[0]["seq_id"].append(4)
        self.assertEqual(polySeq[0]["seq_id"], [1, 2, 3])

    def testAtomKeyEquivalence(self):
        """ atomKey() compares equal exactly when the atoms do, ignoring the excluded keys. """

        a = {"chain_id": "A", "seq_id": 1, "is_poly": True}
        b = {"seq_id": 1, "chain_id": "A", "is_poly": False}

        self.assertNotEqual(atomKey(a), atomKey(b))
        self.assertEqual(atomKey(a, ("is_poly",)), atomKey(b, ("is_poly",)))
        self.assertEqual(atomKey(a), atomKey({"seq_id": 1, "is_poly": True, "chain_id": "A"}))
        self.assertEqual(atomKey({}), ())

    def testFactorKeyIsHashableAndDiscriminating(self):
        """ factorKey() is the cache key of doConsumeFactor_expressions(), so it must be hashable
            and must separate factors that str() separated.
        """

        f = {"chain_id": ["A"], "atom_selection": [{"seq_id": 1}, {"seq_id": 2}]}

        self.assertIsInstance(hash(factorKey(f)), int)
        self.assertEqual(factorKey(f), factorKey({"chain_id": ["A"],
                                                  "atom_selection": [{"seq_id": 1}, {"seq_id": 2}]}))
        self.assertNotEqual(factorKey(f), factorKey({"chain_id": ["A"],
                                                     "atom_selection": [{"seq_id": 2}, {"seq_id": 1}]}))
        self.assertNotEqual(factorKey({"seq_id": [1]}), factorKey({"seq_id": ["1"]}),
                            "str() distinguished these, so the tuple key must too")
        self.assertNotEqual(factorKey({"a": ["b"]}), factorKey({"a": "b"}))

    @unittest.skipUnless(USE_C_IMPLEMENTATION, "c_listener_util was not built")
    def testCAcceleratorMatchesPython(self):
        """ The compiled helpers are behavioral twins of the Python bodies they replace. """

        rnd = random.Random(20260924)

        for _ in range(20000):
            factor = _randomFactor(rnd)
            self.assertEqual(copyFactor(factor), copyFactorPy(factor))
            self.assertEqual(factorKey(factor), factorKeyPy(factor))

            atom = _randomAtom(rnd)
            excl = tuple(rnd.sample(("is_poly", "auth_atom_id", "segment_id", "chain_id"), rnd.randint(0, 4)))
            self.assertEqual(atomKey(atom), atomKeyPy(atom))
            self.assertEqual(atomKey(atom, excl), atomKeyPy(atom, excl))

            polySeq = [_randomAtom(rnd) for _ in range(rnd.randint(0, 4))]
            self.assertEqual(copyPolySeq(polySeq), copyPolySeqPy(polySeq))

    @unittest.skipUnless(USE_C_IMPLEMENTATION, "c_listener_util was not built")
    def testCAcceleratorRaisesTheSameErrors(self):
        for bad in ([1, 2], "abc", None, 42):
            for compiled, pure in ((copyFactor, copyFactorPy), (factorKey, factorKeyPy)):
                with self.assertRaises(AttributeError) as pureErr:
                    pure(bad)
                with self.assertRaises(AttributeError) as compiledErr:
                    compiled(bad)
                self.assertEqual(str(compiledErr.exception), str(pureErr.exception))

    @unittest.skipUnless(USE_C_IMPLEMENTATION, "c_listener_util was not built")
    def testCAcceleratorKeepsRefcountsStable(self):
        """ A reference leak or an over-decrement in the C code is a crash, not an exception,
            so hold the inputs alive across many calls and check they neither grow nor shrink.
        """

        factor = {"chain_id": ["A"],
                  "atom_selection": [{"chain_id": "A", "seq_id": i} for i in range(20)]}
        atom = factor["atom_selection"][0]
        watched = [factor, atom] + list(factor.values())

        before = [sys.getrefcount(o) for o in watched]

        for _ in range(50000):
            copyFactor(factor)
            factorKey(factor)
            atomKey(atom, ("seq_id",))
            copyPolySeq([factor])

        self.assertEqual([sys.getrefcount(o) for o in watched], before)


if __name__ == "__main__":
    unittest.main()
