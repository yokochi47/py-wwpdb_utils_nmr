##
# File: AntlrParseUtilTests.py
# Date: 03-Oct-2026  M. Yokochi
#
# Test the input stream that parseAntlr() hands to the speedy-antlr C++ parsers (DAOTHER-7829, 9785): it must behave as
# antlr4.InputStream, without building the per-character list of code points that only the pure-Python lexer reads.
##
"""Test cases for LazyCodePointInputStream and its use by parseAntlr()."""
import os
import sys
import types
import unittest

from antlr4 import InputStream

# import commonsetup first: it mocks ConfigInfo, which ChemCompUtil reads when it is imported
if __package__ is None or __package__ == "":
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from commonsetup import TESTOUTPUT  # noqa: F401 pylint: disable=import-error,unused-import
else:
    from .commonsetup import TESTOUTPUT  # noqa: F401 pylint: disable=relative-beyond-top-level

from wwpdb.utils.nmr.AntlrParseUtil import LazyCodePointInputStream, parseAntlr

TEXTS = ['', 'assign (resid 1 and name HA) (resid 2 and name HN) 1.8 3.0 5.0\n', 'é中😀\r\n x']


class TestAntlrParseUtil(unittest.TestCase):

    def test_same_as_input_stream(self):
        for text in TEXTS:
            with self.subTest(text=text):
                expected, stream = InputStream(text), LazyCodePointInputStream(text)
                self.assertEqual((stream.size, stream.index, stream.strdata, str(stream)),
                                 (expected.size, expected.index, expected.strdata, str(expected)))
                for start, stop in ((0, 0), (0, 2), (1, 5), (5, 99), (99, 120)):
                    self.assertEqual(stream.getText(start, stop), expected.getText(start, stop))
                if text:
                    expected.consume()
                    stream.consume()
                    self.assertEqual((stream.index, stream.LA(1)), (expected.index, expected.LA(1)))
                self.assertEqual(stream.data, expected.data)

    def test_code_points_are_built_on_demand(self):
        stream = LazyCodePointInputStream('x' * 1000)
        self.assertIsNone(getattr(stream, '_codePoints'))
        self.assertEqual(len(stream.data), 1000)
        self.assertIs(stream.data, stream.data)

    def test_cpp_path_gets_the_lazy_stream(self):
        received = []

        def parse(stream, entryRuleName, errorListener, predictionModeSll):  # pylint: disable=unused-argument
            received.append(stream)
            return 'tree'

        saModule = types.ModuleType('sa_stub')  # a stand-in for a generated sa_<grammar> shim with its C++ accelerator
        saModule.USE_CPP_IMPLEMENTATION = True
        saModule.parse = parse
        saModule.SA_ErrorListener = type('SA_ErrorListener', (), {})
        tree, _, _ = parseAntlr(None, None, 'entry', 'assign (resid 1 and name HA) 1.0\n', saModule=saModule)
        self.assertEqual(tree, 'tree')
        self.assertIsInstance(received[0], LazyCodePointInputStream)
        self.assertIsNone(getattr(received[0], '_codePoints'))


if __name__ == "__main__":
    unittest.main()
