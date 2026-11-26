##
# File: PippCSParserListener.py
# Date: 11-Apr-2025
#
# Updates:
""" ParserLister class for PIPP CS files.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "1.2.0"

import copy
import sys
from typing import IO, List, Optional

from antlr4 import ParseTreeListener

try:
    from wwpdb.utils.nmr.NmrDpConstant import ASSIGNMENT_SEPARATOR_PAT
    from wwpdb.utils.nmr.nef.NefTranslator import NefTranslator
    from wwpdb.utils.nmr.cs.PippCSParser import PippCSParser
    from wwpdb.utils.nmr.cs.BaseCSParserListener import BaseCSParserListener
except ImportError:
    from nmr.NmrDpConstant import ASSIGNMENT_SEPARATOR_PAT
    from nmr.nef.NefTranslator import NefTranslator
    from nmr.cs.PippCSParser import PippCSParser
    from nmr.cs.BaseCSParserListener import BaseCSParserListener


class PippCSParserListener(ParseTreeListener, BaseCSParserListener):
    """ This class defines a complete listener for a parse tree produced by PippCSParser.
    """
    __slots__ = ()

    __chain_id = None
    __seq_id = None
    __comp_id = None

    def __init__(self, verbose: bool = True, log: IO = sys.stdout,
                 polySeq: List[dict] = None, entityAssembly: Optional[dict] = None,
                 nefT: NefTranslator = None,
                 reasons: Optional[dict] = None) -> None:
        super().__init__(verbose, log, polySeq, entityAssembly, nefT, reasons)

        self.file_type = 'nm-shi-pip'
        self.software_name = 'PIPP'

    def enterPipp_cs(self, ctx: PippCSParser.Pipp_csContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by PippCSParser#pipp_cs.
        """

    def exitPipp_cs(self, ctx: PippCSParser.Pipp_csContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by PippCSParser#pipp_cs.
        """

        self.exit()

    def enterPipp_format(self, ctx: PippCSParser.Pipp_formatContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by PippCSParser#pipp_format.
        """

        self.cur_list_id = max(self.cur_list_id, 0)
        self.cur_list_id += 1

        self.chemShifts = 0
        self.offset = {}

        self.cur_subtype = 'csp' if self.csp else 'chem_shift'

        if ctx.Integer():
            self.predictSequenceNumberOffsetByFirstResidue(None, int(str(ctx.Integer())), None)

    def exitPipp_format(self, ctx: PippCSParser.Pipp_formatContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by PippCSParser#pipp_format.
        """

    def enterExt_peak_pick_tbl(self, ctx: PippCSParser.Ext_peak_pick_tblContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by PippCSParser#ext_peak_pick_tbl.
        """

    def exitExt_peak_pick_tbl(self, ctx: PippCSParser.Ext_peak_pick_tblContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by PippCSParser#ext_peak_pick_tbl.
        """

    def enterExt_peak_pick_tbl_row(self, ctx: PippCSParser.Ext_peak_pick_tbl_rowContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by PippCSParser#ext_peak_pick_tbl_row.
        """

    def exitExt_peak_pick_tbl_row(self, ctx: PippCSParser.Ext_peak_pick_tbl_rowContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by PippCSParser#ext_peak_pick_tbl_row.
        """

    def enterResidue_list(self, ctx: PippCSParser.Residue_listContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by PippCSParser#residue_list.
        """

        self.__comp_id = '.'

    def exitResidue_list(self, ctx: PippCSParser.Residue_listContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by PippCSParser#residue_list.
        """

    def enterRes_id(self, ctx: PippCSParser.Res_idContext):
        """ Enter a parse tree produced by PippCSParser#res_id.
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

    def exitRes_id(self, ctx: PippCSParser.Res_idContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by PippCSParser#res_id.
        """

    def enterRes_type(self, ctx: PippCSParser.Res_typeContext):
        """ Enter a parse tree produced by PippCSParser#res_type.
        """

        if self.__comp_id == '.':
            if ctx.Simple_name():
                self.__comp_id = str(ctx.Simple_name())
            else:
                self.__comp_id = None

    def exitRes_type(self, ctx: PippCSParser.Res_typeContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by PippCSParser#res_type.
        """

    def enterShift_list(self, ctx: PippCSParser.Shift_listContext):  # pylint: disable=unused-argument
        """ Enter a parse tree produced by PippCSParser#shift_list.
        """

        self.cur_line_num += 1

    def exitShift_list(self, ctx: PippCSParser.Shift_listContext):
        """ Exit a parse tree produced by PippCSParser#shift_list.
        """

        try:

            if len(self.numberSelection) == 0:
                return

            dstFunc = self.validateCsValue(self.cur_line_num, self.numberSelection[0], None)

            if dstFunc is None:
                return

            dstFunc2 = None

            if len(self.numberSelection) > 1:
                dstFunc2 = self.validateCsValue(self.cur_line_num, self.numberSelection[1], None)

                if dstFunc2 is None:
                    return

            if None in (self.__seq_id, self.__comp_id) or self.__comp_id == '.':
                return

            auth_seq_id_map = {}

            seq_id = self.__seq_id
            if None in self.offset:
                seq_id += self.offset[None]
                auth_seq_id_map[seq_id] = self.__seq_id

            atom_ids = str(ctx.Simple_name())

            if atom_ids.endswith(':-1'):
                return

            atom_ids = atom_ids.split('|')
            len_atom_ids = len(atom_ids)

            if len_atom_ids == 1:

                L = f'{seq_id}:{self.__comp_id}:{atom_ids[0]}' if self.__chain_id is None\
                    else f'{self.__chain_id}:{seq_id}:{self.__comp_id}:{atom_ids[0]}'

                assignment = self.extractChemShiftAssignment(1, L, self.cur_line_num, with_segid=self.__chain_id,
                                                             with_compid=self.__comp_id, with_atomid=atom_ids[0])

                if assignment is None:
                    return

                has_assignments, has_multiple_assignments = self.checkAssignment(self.cur_line_num, assignment)

                len_atom_sel = len(self.atomSelectionSets[0][0]) if has_assignments else 0

                if dstFunc2 is None or not has_assignments and len_atom_sel == 1:
                    self.addCsRow(self.cur_line_num, dstFunc, has_assignments, has_multiple_assignments, auth_seq_id_map,
                                  f'{L} -> ')

                else:

                    ambig_code = self.csStat.getMaxAmbigCodeWoSetId(self.__comp_id, self.atomSelectionSets[0][0][0]['atom_id'])\
                        if has_assignments else None

                    atomSelectionSet1 = atomSelectionSet2 = None

                    if len_atom_sel > 0:
                        atomSelectionSet1 = copy.copy(self.atomSelectionSets[0][0][0:len_atom_sel // 2])
                        atomSelectionSet2 = copy.copy(self.atomSelectionSets[0][0][len_atom_sel // 2:])

                        self.atomSelectionSets[0][0] = atomSelectionSet1

                    self.addCsRow(self.cur_line_num, dstFunc, has_assignments, has_multiple_assignments, auth_seq_id_map,
                                  f'{L} -> ', default_ambig_code=ambig_code)

                    if has_assignments:

                        self.chemShifts += 1

                        self.atomSelectionSets[0][0] = atomSelectionSet2

                        self.addCsRow(self.cur_line_num, dstFunc2, has_assignments, has_multiple_assignments, auth_seq_id_map,
                                      f'{L} -> ', default_ambig_code=ambig_code)

                self.chemShifts += 1

            else:

                for idx, atom_id in enumerate(atom_ids):

                    L = f'{seq_id}:{self.__comp_id}:{atom_id}' if self.__chain_id is None\
                        else f'{self.__chain_id}:{seq_id}:{self.__comp_id}:{atom_id}'

                    assignment = self.extractChemShiftAssignment(1, L, self.cur_line_num,
                                                                 with_segid=self.__chain_id,
                                                                 with_compid=self.__comp_id, with_atomid=atom_id)

                    if assignment is None:
                        return

                    has_assignments, has_multiple_assignments = self.checkAssignment(self.cur_line_num, assignment)

                    if dstFunc2 is None:
                        _dstFunc = dstFunc
                    else:
                        _dstFunc = dstFunc if idx < len_atom_ids // 2 else dstFunc2

                    ambig_code = self.csStat.getMaxAmbigCodeWoSetId(self.__comp_id, self.atomSelectionSets[0][0][0]['atom_id'])\
                        if has_assignments else None

                    self.addCsRow(self.cur_line_num, _dstFunc, has_assignments, has_multiple_assignments, auth_seq_id_map,
                                  f'{L} -> ', None, ambig_code)

                    self.chemShifts += 1

                    self.atomSelectionSets.clear()

        finally:
            self.atomSelectionSets.clear()
            self.numberSelection.clear()

    def enterNumber(self, ctx: PippCSParser.NumberContext):
        """ Enter a parse tree produced by PippCSParser#number.
        """

        try:

            if ctx.Float():
                self.numberSelection.append(float(str(ctx.Float())))

            elif ctx.Integer():
                self.numberSelection.append(float(str(ctx.Integer())))

        except ValueError:
            pass

    def exitNumber(self, ctx: PippCSParser.NumberContext):  # pylint: disable=unused-argument
        """ Exit a parse tree produced by PippCSParser#number.
        """
