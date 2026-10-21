##
# BiosymMRReader.py
#
# Update:
##
""" A collection of classes for parsing BIOSYM MR files.
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "1.2.0"

import os
import sys
from typing import IO, List, Optional, Tuple

from antlr4 import ParseTreeWalker

try:
    from wwpdb.utils.nmr.NmrDpConstant import (MAX_ERROR_REPORT,
                                               REPRESENTATIVE_MODEL_ID,
                                               REPRESENTATIVE_ALT_ID)
    from wwpdb.utils.nmr.ChemCompUtil import ChemCompUtil
    from wwpdb.utils.nmr.BmrbChemShiftStat import BmrbChemShiftStat
    from wwpdb.utils.nmr.nef.NefTranslator import NefTranslator
    from wwpdb.utils.nmr.io.CifReader import CifReader
    from wwpdb.utils.nmr.AntlrParseUtil import parseAntlr
    from wwpdb.utils.nmr.mr import sa_biosymmr
    from wwpdb.utils.nmr.mr.LexerErrorListener import LexerErrorListener
    from wwpdb.utils.nmr.mr.ParserErrorListener import ParserErrorListener
    from wwpdb.utils.nmr.mr.BiosymMRLexer import BiosymMRLexer
    from wwpdb.utils.nmr.mr.BiosymMRParser import BiosymMRParser
    from wwpdb.utils.nmr.mr.BiosymMRParserListener import BiosymMRParserListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (coordAssemblyChecker,
                                                       retrieveOriginalFileName)
except ImportError:
    from nmr.NmrDpConstant import (MAX_ERROR_REPORT,
                                   REPRESENTATIVE_MODEL_ID,
                                   REPRESENTATIVE_ALT_ID)
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BmrbChemShiftStat import BmrbChemShiftStat
    from nmr.nef.NefTranslator import NefTranslator
    from nmr.io.CifReader import CifReader
    from nmr.AntlrParseUtil import parseAntlr
    from nmr.mr import sa_biosymmr
    from nmr.mr.LexerErrorListener import LexerErrorListener
    from nmr.mr.ParserErrorListener import ParserErrorListener
    from nmr.mr.BiosymMRLexer import BiosymMRLexer
    from nmr.mr.BiosymMRParser import BiosymMRParser
    from nmr.mr.BiosymMRParserListener import BiosymMRParserListener
    from nmr.mr.ParserListenerUtil import (coordAssemblyChecker,
                                           retrieveOriginalFileName)


class BiosymMRReader:
    """ Accessor methods for parsing BIOSYM MR files.
    """
    __slots__ = ('__class_name__',
                 '__version__',
                 '__verbose',
                 '__log',
                 '__debug',
                 '__maxLexerErrorReport',
                 '__maxParserErrorReport',
                 '__representativeModelId',
                 '__representativeAltId',
                 '__mrAtomNameMapping',
                 '__ccU',
                 '__cR',
                 '__caC',
                 '__csStat',
                 '__nefT',
                 '__reasons')

    def __init__(self, verbose: bool = True, log: IO = sys.stdout,
                 representativeModelId: int = REPRESENTATIVE_MODEL_ID,
                 representativeAltId: str = REPRESENTATIVE_ALT_ID,
                 mrAtomNameMapping: Optional[List[dict]] = None,
                 cR: Optional[CifReader] = None, caC: Optional[dict] = None, ccU: Optional[ChemCompUtil] = None,
                 csStat: Optional[BmrbChemShiftStat] = None, nefT: Optional[NefTranslator] = None,
                 reasons: Optional[dict] = None) -> None:
        self.__class_name__ = self.__class__.__name__
        self.__version__ = __version__

        self.__verbose = verbose
        self.__log = log
        self.__debug = False

        self.__maxLexerErrorReport = MAX_ERROR_REPORT
        self.__maxParserErrorReport = MAX_ERROR_REPORT

        self.__representativeModelId = representativeModelId
        self.__representativeAltId = representativeAltId
        self.__mrAtomNameMapping = mrAtomNameMapping

        # CCD accessing utility
        self.__ccU = ChemCompUtil(verbose, log) if ccU is None else ccU

        if cR is not None and caC is None:
            caC = coordAssemblyChecker(verbose, log, representativeModelId, representativeAltId,
                                       cR, self.__ccU, None, None, fullCheck=False)

        self.__cR = cR
        self.__caC = caC

        # BMRB chemical shift statistics
        self.__csStat = BmrbChemShiftStat(verbose, log, self.__ccU) if csStat is None else csStat

        # NefTranslator
        self.__nefT = NefTranslator(verbose, log, self.__ccU, self.__csStat) if nefT is None else nefT
        if nefT is None:
            self.__nefT.set_remediation_mode(True)

        # reasons for re-parsing request from the previous trial
        self.__reasons = reasons

    def setDebugMode(self, debug: bool) -> None:
        """ Set debug mode.
        """

        self.__debug = debug

    def setLexerMaxErrorReport(self, maxErrReport: int) -> None:
        """ Set the maximum number of lexer error messages to save.
        """

        self.__maxLexerErrorReport = maxErrReport

    def setParserMaxErrorReport(self, maxErrReport: int) -> None:
        """ Set the maximum number of parser error messages to save.
        """

        self.__maxParserErrorReport = maxErrReport

    def parse(self, mrFilePath: str, cifFilePath: Optional[str] = None, isFilePath: bool = True,
              createSfDict: bool = False, originalFileName: Optional[str] = None, listIdCounter: Optional[dict] = None,
              entryId: Optional[str] = None
              ) -> Tuple[Optional[BiosymMRParserListener], Optional[ParserErrorListener], Optional[LexerErrorListener]]:
        """ Parse BIOSYM MR file.
            @return: BiosymMRParserListener for success or None otherwise, ParserErrorListener, LexerErrorListener.
        """

        ifh = None

        try:

            if isFilePath:
                mrString = None

                if not os.access(mrFilePath, os.R_OK):
                    if self.__verbose:
                        self.__log.write(f"+{self.__class_name__}.parse() {mrFilePath} is not accessible.\n")
                    return None, None, None

                ifh = open(mrFilePath, 'r', encoding='utf-8', errors='ignore')  # pylint: disable=consider-using-with
                mrText = ifh.read()

            else:
                mrFilePath, mrString = None, mrFilePath

                if mrString is None or len(mrString) == 0:
                    if self.__verbose:
                        self.__log.write(f"+{self.__class_name__}.parse() Empty string.\n")
                    return None, None, None

                mrText = mrString

            if cifFilePath is not None:
                if not os.access(cifFilePath, os.R_OK):
                    if self.__verbose:
                        self.__log.write(f"+{self.__class_name__}.parse() {cifFilePath} is not accessible.\n")
                    return None, None, None

                if self.__cR is None:
                    self.__cR = CifReader(self.__verbose, self.__log)
                    if not self.__cR.parse(cifFilePath):
                        if self.__verbose:
                            self.__log.write(f"+{self.__class_name__}.parse() {cifFilePath} is not CIF file.\n")
                        return None, None, None

            tree, parser_error_listener, lexer_error_listener =\
                parseAntlr(BiosymMRLexer, BiosymMRParser, 'biosym_mr', mrText,
                           filePath=mrFilePath, saModule=sa_biosymmr,
                           maxLexerErrorReport=self.__maxLexerErrorReport,
                           maxParserErrorReport=self.__maxParserErrorReport,
                           predictionModeSll=True)

            messageList = lexer_error_listener.getMessageList()

            if messageList is not None and self.__verbose:
                for description in messageList:
                    self.__log.write(f"[Syntax error] line {description['line_number']}:{description['column_position']} "
                                     f"{description['message']}\n")
                    if 'input' in description:
                        self.__log.write(f"{description['input']}\n")
                        self.__log.write(f"{description['marker']}\n")

            walker = ParseTreeWalker()
            listener = BiosymMRParserListener(self.__verbose, self.__log,
                                              self.__representativeModelId,
                                              self.__representativeAltId,
                                              self.__mrAtomNameMapping,
                                              self.__cR, self.__caC,
                                              self.__nefT,
                                              self.__reasons)
            listener.debug = self.__debug
            listener.createSfDict = createSfDict
            if createSfDict:
                listener.originalFileName =\
                    originalFileName if originalFileName is not None else retrieveOriginalFileName(mrFilePath)
                if listIdCounter is not None:
                    listener.listIdCounter = listIdCounter
                if entryId is not None:
                    listener.entryId = entryId
            walker.walk(listener, tree)

            messageList = parser_error_listener.getMessageList()

            if messageList is not None and self.__verbose:
                for description in messageList:
                    self.__log.write(f"[Syntax error] line {description['line_number']}:{description['column_position']} "
                                     f"{description['message']}\n")
                    if 'input' in description:
                        self.__log.write(f"{description['input']}\n")
                        self.__log.write(f"{description['marker']}\n")

            if self.__verbose and self.__debug:
                if listener.warningMessage is not None and len(listener.warningMessage) > 0:
                    self.__log.write(f"+{self.__class_name__}.parse() ++ Info  -\n" + '\n'.join(listener.warningMessage) + '\n')
                if isFilePath:
                    self.__log.write(f"+{self.__class_name__}.parse() ++ Info  - {listener.getContentSubtype()}\n")

            return listener, parser_error_listener, lexer_error_listener

        except IOError as e:
            if self.__verbose:
                self.__log.write(f"+{self.__class_name__}.parse() ++ Error  - {str(e)}\n")
            return None, None, None
        finally:
            if isFilePath and ifh is not None:
                ifh.close()


if __name__ == "__main__":
    reader = BiosymMRReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/1l1v/1l1v-corrected.mr',
                 '../../tests-nmr/mock-data-remediation/1l1v/1l1v.cif')

    reader = BiosymMRReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/1sut/1sut-trimmed.mr',
                 '../../tests-nmr/mock-data-remediation/1sut/1sut.cif')

    reader = BiosymMRReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/2l7v/2l7v-trimmed.mr',
                 '../../tests-nmr/mock-data-remediation/2l7v/2l7v.cif')

    reader = BiosymMRReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/2vb5/2vb5-corrected-div_dst-div_src.mr',
                 '../../tests-nmr/mock-data-remediation/2vb5/2vb5.cif')

    reader = BiosymMRReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/2lyw/2lyw-trimmed.mr',
                 '../../tests-nmr/mock-data-remediation/2lyw/2lyw.cif')

    reader = BiosymMRReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/6var/HBVe_SAXS.tab',
                 '../../tests-nmr/mock-data-remediation/6var/6var.cif')

    reader = BiosymMRReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/2mug/2mug-trimmed.mr',
                 '../../tests-nmr/mock-data-remediation/2mug/2mug.cif')
