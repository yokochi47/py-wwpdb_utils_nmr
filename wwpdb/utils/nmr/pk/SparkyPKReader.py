##
# SparkyPKReader.py
#
# Update:
##
""" A collection of classes for parsing SPARKY PK files.
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
    from wwpdb.utils.nmr.pk import sa_sparkypk
    from wwpdb.utils.nmr.mr.LexerErrorListener import LexerErrorListener
    from wwpdb.utils.nmr.mr.ParserErrorListener import ParserErrorListener
    from wwpdb.utils.nmr.mr.ParserListenerUtil import coordAssemblyChecker
    from wwpdb.utils.nmr.pk.SparkyPKLexer import SparkyPKLexer
    from wwpdb.utils.nmr.pk.SparkyPKParser import SparkyPKParser
    from wwpdb.utils.nmr.pk.SparkyPKParserListener import SparkyPKParserListener
except ImportError:
    from nmr.NmrDpConstant import (MAX_ERROR_REPORT,
                                   REPRESENTATIVE_MODEL_ID,
                                   REPRESENTATIVE_ALT_ID)
    from nmr.ChemCompUtil import ChemCompUtil
    from nmr.BmrbChemShiftStat import BmrbChemShiftStat
    from nmr.nef.NefTranslator import NefTranslator
    from nmr.io.CifReader import CifReader
    from nmr.AntlrParseUtil import parseAntlr
    from nmr.pk import sa_sparkypk
    from nmr.mr.LexerErrorListener import LexerErrorListener
    from nmr.mr.ParserErrorListener import ParserErrorListener
    from nmr.mr.ParserListenerUtil import coordAssemblyChecker
    from nmr.pk.SparkyPKLexer import SparkyPKLexer
    from nmr.pk.SparkyPKParser import SparkyPKParser
    from nmr.pk.SparkyPKParserListener import SparkyPKParserListener


class SparkyPKReader:
    """ Accessor methods for parsing SPARKY PK files.
    """
    __slots__ = ('__class_name__',
                 '__version__',
                 '__verbose',
                 '__log',
                 '__debug',
                 '__enforcePeakRowFormat',
                 '__internal',
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
        self.__enforcePeakRowFormat = False
        self.__internal = False

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

    def enforcePeakRowFormat(self, enforcePeakRowFormat: bool) -> None:
        """ Whether to enforce peak row format or not.
        """

        self.__enforcePeakRowFormat = enforcePeakRowFormat

    def setInternalMode(self, internal: bool) -> None:
        """ Set internal mode.
        """

        self.__internal = internal

    def setLexerMaxErrorReport(self, maxErrReport: int) -> None:
        """ Set the maximum number of lexer error messages to save.
        """

        self.__maxLexerErrorReport = maxErrReport

    def setParserMaxErrorReport(self, maxErrReport: int) -> None:
        """ Set the maximum number of parser error messages to save.
        """

        self.__maxParserErrorReport = maxErrReport

    def parse(self, pkFilePath: str, cifFilePath: Optional[str] = None, isFilePath: bool = True,
              createSfDict: bool = False, originalFileName: Optional[str] = None, listIdCounter: Optional[dict] = None,
              reservedListIds: Optional[dict] = None, entryId: Optional[str] = None, csLoops: Optional[List[dict]] = None
              ) -> Tuple[Optional[SparkyPKParserListener], Optional[ParserErrorListener], Optional[LexerErrorListener]]:
        """ Parse SPARKY PK file.
            @return: SparkyPKParserListener for success or None otherwise, ParserErrorListener, LexerErrorListener.
        """

        ifh = None

        try:

            if isFilePath:
                pkString = None

                if not os.access(pkFilePath, os.R_OK):
                    if self.__verbose:
                        self.__log.write(f"+{self.__class_name__}.parse() {pkFilePath} is not accessible.\n")
                    return None, None, None

                ifh = open(pkFilePath, 'r', encoding='utf-8', errors='ignore')  # pylint: disable=consider-using-with
                pkText = ifh.read()

            else:
                pkFilePath, pkString = None, pkFilePath

                if pkString is None or len(pkString) == 0:
                    if self.__verbose:
                        self.__log.write(f"+{self.__class_name__}.parse() Empty string.\n")
                    return None, None, None

                pkText = pkString

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
                parseAntlr(SparkyPKLexer, SparkyPKParser, 'sparky_pk', pkText,
                           filePath=pkFilePath, saModule=sa_sparkypk,
                           maxLexerErrorReport=self.__maxLexerErrorReport,
                           maxParserErrorReport=self.__maxParserErrorReport,
                           ignoreCodicError=True)

            messageList = lexer_error_listener.getMessageList()

            if messageList is not None and self.__verbose:
                for description in messageList:
                    self.__log.write(f"[Syntax error] line {description['line_number']}:{description['column_position']} "
                                     f"{description['message']}\n")
                    if 'input' in description:
                        self.__log.write(f"{description['input']}\n")
                        self.__log.write(f"{description['marker']}\n")

            walker = ParseTreeWalker()
            listener = SparkyPKParserListener(self.__verbose, self.__log,
                                              self.__representativeModelId,
                                              self.__representativeAltId,
                                              self.__mrAtomNameMapping,
                                              self.__cR, self.__caC,
                                              self.__nefT,
                                              self.__reasons)
            listener.debug = self.__debug
            listener.internal = self.__internal
            listener.createSfDict = createSfDict
            listener.enforcePeakRowFormat = self.__enforcePeakRowFormat
            if createSfDict:
                if originalFileName is not None:
                    listener.originalFileName = originalFileName
                if listIdCounter is not None:
                    listener.listIdCounter = listIdCounter
                if reservedListIds is not None:
                    listener.reservedListIds = reservedListIds
                if entryId is not None:
                    listener.entryId = entryId
                if csLoops is not None:
                    listener.csLoops = csLoops
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
    reader = SparkyPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/2k1g/bmr15603/work/upload/temp-11-corrected',
                 '../../tests-nmr/mock-data-remediation/2k1g/2k1g.cif')

    reader = SparkyPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/2kzn/bmr17008/work/data/cch_noesy_final.list',
                 '../../tests-nmr/mock-data-remediation/2kzn/2kzn.cif')

    reader = SparkyPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/6kfj/bmr36268/work/data/D_1300012879_nmr-peaks-upload_P1.dat.V3',
                 '../../tests-nmr/mock-data-remediation/6kfj/6kfj.cif')

    reader = SparkyPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/7vqh/bmr36450/work/data/D_1300025198_nmr-peaks-upload_P1.dat.V2',
                 '../../tests-nmr/mock-data-remediation/7vqh/7vqh.cif')

    reader = SparkyPKReader(True)
    reader.setDebugMode(True)
    reader_listener, _, _ =\
        reader.parse('../../tests-nmr/mock-data-remediation/5z5x/bmr21081/work/upload/HVF18-NOESY.-corrected',
                     '../../tests-nmr/mock-data-remediation/5z5x/5z5x.cif')

    reasons_ = {'non_poly_remap': {'SER': {37: {'chain_id': 'A', 'seq_id': 102, 'original_chain_id': None}}}}
    mrAtomNameMapping_ = [{'auth_atom_id': 'H44', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H44', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H432', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H432', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H431', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H431', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H421', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H421', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H422', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H422', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H41', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H41', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H381', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H381', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H382', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H382', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H371', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H371', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H372', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H372', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H36', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H36', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H33', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H33', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H32', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H32', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H311', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H311', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H312', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H312', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H313', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H313', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H301', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H301', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H302', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H302', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H303', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H303', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H281', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H281', 'original_comp_id': 'PNS', 'original_seq_id': 102},
                          {'auth_atom_id': 'H282', 'auth_comp_id': 'PNS', 'auth_seq_id': 102,
                           'original_atom_id': 'H282', 'original_comp_id': 'PNS', 'original_seq_id': 102}]
    reader = SparkyPKReader(True, reasons=reasons_, mrAtomNameMapping=mrAtomNameMapping_)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/2ll8/bmr18032/work/data/holo_Nnoesy.list.str',
                 '../../tests-nmr/mock-data-remediation/2ll8/2ll8.cif')

    reader = SparkyPKReader(False)
    reader.setDebugMode(False)
    reader_listener, _, _ =\
        reader.parse('../../tests-nmr/mock-data-remediation/6nbn/bmr30550/work/data/D_1000238162_nmr-peaks-upload_P9.dat.V1',
                     '../../tests-nmr/mock-data-remediation/6nbn/6nbn.cif')
    reader = SparkyPKReader(True, reasons=reader_listener.getReasonsForReparsing())
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/6nbn/bmr30550/work/data/D_1000238162_nmr-peaks-upload_P9.dat.V1',
                 '../../tests-nmr/mock-data-remediation/6nbn/6nbn.cif')

    reader = SparkyPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/5z8f/bmr36160/work/data/D_1300006644_nmr-peaks-upload_P1.dat.V3',
                 '../../tests-nmr/mock-data-remediation/5z8f/5z8f.cif')

    reader = SparkyPKReader(False)
    reader.setDebugMode(False)
    reader_listener, _, _ =\
        reader.parse('../../tests-nmr/mock-data-remediation/6nbn/bmr30550/work/data/D_1000238162_nmr-peaks-upload_P4.dat.V1',
                     '../../tests-nmr/mock-data-remediation/6nbn/6nbn.cif')
    reader = SparkyPKReader(True, reasons=reader_listener.getReasonsForReparsing())
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/6nbn/bmr30550/work/data/D_1000238162_nmr-peaks-upload_P4.dat.V1',
                 '../../tests-nmr/mock-data-remediation/6nbn/6nbn.cif')

    reader = SparkyPKReader(False)
    reader.setDebugMode(False)
    reader_listener, _, _ =\
        reader.parse('../../tests-nmr/mock-data-remediation/6nbn/bmr30550/work/data/D_1000238162_nmr-peaks-upload_P3.dat.V2',
                     '../../tests-nmr/mock-data-remediation/6nbn/6nbn.cif')
    reader = SparkyPKReader(True, reasons=reader_listener.getReasonsForReparsing())
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/6nbn/bmr30550/work/data/D_1000238162_nmr-peaks-upload_P3.dat.V2',
                 '../../tests-nmr/mock-data-remediation/6nbn/6nbn.cif')

    reader = SparkyPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/8e1d/bmr31038/work/data/D_1000267621_nmr-peaks-upload_P6.dat.V1',
                 '../../tests-nmr/mock-data-remediation/8e1d/8e1d.cif')

    reader = SparkyPKReader(False)
    reader.setDebugMode(False)
    reader_listener, _, _ =\
        reader.parse('../../tests-nmr/mock-data-remediation/6nbn/bmr30550/work/data/D_1000238162_nmr-peaks-upload_P2.dat.V3',
                     '../../tests-nmr/mock-data-remediation/6nbn/6nbn.cif')
    reader = SparkyPKReader(True, reasons=reader_listener.getReasonsForReparsing())
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/6nbn/bmr30550/work/data/D_1000238162_nmr-peaks-upload_P2.dat.V3',
                 '../../tests-nmr/mock-data-remediation/6nbn/6nbn.cif')

    reader = SparkyPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/6nbn/bmr30550/work/data/D_1000238162_nmr-peaks-upload_P1.dat.V4',
                 '../../tests-nmr/mock-data-remediation/6nbn/6nbn.cif')

    reader = SparkyPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/6uz5/bmr30687/work/data/D_1000245462_nmr-peaks-upload_P2.dat.V1',
                 '../../tests-nmr/mock-data-remediation/6uz5/6uz5.cif')

    reader = SparkyPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/6uz5/bmr30687/work/data/D_1000245462_nmr-peaks-upload_P1.dat.V1',
                 '../../tests-nmr/mock-data-remediation/6uz5/6uz5.cif')

    reader = SparkyPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/2k5w/2k5w-corrected-div_dst.mr',
                 '../../tests-nmr/mock-data-remediation/2k5w/2k5w.cif')

    reader = SparkyPKReader(True)
    reader.setDebugMode(True)
    reader.parse('../../tests-nmr/mock-data-remediation/2js7/2js7-trimmed-div_ext.mr',
                 '../../tests-nmr/mock-data-remediation/2js7/2js7.cif')
