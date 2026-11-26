##
# File: GarretCSParserListener.py
# Date: 11-Apr-2025
#
# Updates:
""" ParserLister class for GARRET CS files.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "1.2.0"

import sys
from typing import IO, List, Optional

from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.nmr.NmrDpConstant import ASSIGNMENT_SEPARATOR_PAT
    from wwpdb.utils.nmr.nef.NefTranslator import NefTranslator
    from wwpdb.utils.nmr.cs.GarretCSParser import GarretCSParser
    from wwpdb.utils.nmr.cs.BaseCSParserListener import BaseCSParserListener
except ImportError:
    from nmr.NmrDpConstant import ASSIGNMENT_SEPARATOR_PAT
    from nmr.nef.NefTranslator import NefTranslator
    from nmr.cs.GarretCSParser import GarretCSParser
    from nmr.cs.BaseCSParserListener import BaseCSParserListener


class GarretCSParserListener(ParseTreeListener, BaseCSParserListener):
    """ This class defines a complete listener for a parse tree produced by GarretCSParser.
    """
    __slots__ = ()

    __chain_id = None
    __seq_id = None
    __comp_id = None
    __number = None

    def __init__(self, verbose: bool = True, log: IO = sys.stdout,
                 polySeq: List[dict] = None, entityAssembly: Optional[dict] = None,
                 nefT: NefTranslator = None,
                 reasons: Optional[dict] = None) -> None:
        super().__init__(verbose, log, polySeq, entityAssembly, nefT, reasons)

        self.file_type = 'nm-shi-gar'

    def enterGarret_cs(self, ctx: GarretCSParser.Garret_csContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by GarretCSParser#garret_cs.
        """

        self.cur_list_id = max(self.cur_list_id, 0)
        self.cur_list_id += 1

        self.cur_line_num = 0

        self.chemShifts = 0
        self.offset = {}

        self.cur_subtype = 'csp' if self.csp else 'chem_shift'

    def exitGarret_cs(self, ctx: GarretCSParser.Garret_csContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by GarretCSParser#garret_cs.
        """

        self.exit()

    def enterResidue_list(self, ctx: GarretCSParser.Residue_listContext):
        """ Enter a parse tree produced by GarretCSParser#residue_list.
        """

        if ctx.Simple_name():
            self.__comp_id = str(ctx.Simple_name())
        else:
            self.__comp_id = None

    def exitResidue_list(self, ctx: GarretCSParser.Residue_listContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by GarretCSParser#residue_list.
        """

    def enterRes_id(self, ctx: GarretCSParser.Res_idContext):
        """ Enter a parse tree produced by GarretCSParser#res_id.
        """

        try:

            if ctx.Integer():
                self.__chain_id = None
                self.__seq_id = int(str(ctx.Integer()))

            else:
                string = str(ctx.Simple_name())
                _str = ASSIGNMENT_SEPARATOR_PAT.sub(' ', string.upper()).split()

                len_str = len(_str)

                if len_str == 1 and _str[0][1:].isdigit():
                    self.__chain_id = _str[0][0]
                    self.__seq_id = int(_str[0][1:])

                elif len_str == 2 and _str[1].isdigit():
                    self.__chain_id = _str[0]
                    self.__seq_id = int(_str[1])

                else:
                    self.__chain_id = None
                    self.__seq_id = None

        except ValueError:
            self.__chain_id = None
            self.__seq_id = None

    def exitRes_id(self, ctx: GarretCSParser.Res_idContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by GarretCSParser#res_id.
        """

    def enterShift_list(self, ctx: GarretCSParser.Shift_listContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by GarretCSParser#shift_list.
        """

        self.cur_subtype = 'csp' if self.csp else 'chem_shift'
        self.cur_line_num += 1

    def exitShift_list(self, ctx: GarretCSParser.Shift_listContext):
        """ Exit a parse tree produced by GarretCSParser#shift_list.
        """

        value = self.__number

        if value is None:
            return

        self.atomSelectionSets.clear()

        dstFunc = self.validateCsValue(self.cur_line_num, value, None)

        if dstFunc is None:
            return

        if None in (self.__seq_id, self.__comp_id):
            return

        atom_id = str(ctx.Simple_name())

        L = f'{self.__seq_id}:{self.__comp_id}:{atom_id}' if self.__chain_id is None\
            else f'{self.__chain_id}:{self.__seq_id}:{self.__comp_id}:{atom_id}'

        assignment = self.extractChemShiftAssignment(1, L, self.cur_line_num,
                                                     with_segid=self.__chain_id,
                                                     with_compid=self.__comp_id,
                                                     with_atomid=atom_id)

        if assignment is None:
            return

        has_assignments, has_multiple_assignments = self.checkAssignment(self.cur_line_num, assignment)

        self.addCsRow(self.cur_line_num, dstFunc, has_assignments, has_multiple_assignments, {}, f'{L} -> ')

        self.chemShifts += 1

    def enterNumber(self, ctx: GarretCSParser.NumberContext):
        """ Enter a parse tree produced by GarretCSParser#number.
        """

        try:

            if ctx.Float():
                self.__number = float(str(ctx.Float()))

            elif ctx.Integer():
                self.__number = float(str(ctx.Integer()))

            else:
                self.__number = None

        except ValueError:
            self.__number = None

    def exitNumber(self, ctx: GarretCSParser.NumberContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by GarretCSParser#number.
        """
