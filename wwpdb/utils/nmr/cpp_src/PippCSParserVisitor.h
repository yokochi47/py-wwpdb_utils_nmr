
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/PippCSParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "PippCSParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by PippCSParser.
 */
class  PippCSParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by PippCSParser.
   */
    virtual std::any visitPipp_cs(PippCSParser::Pipp_csContext *context) = 0;

    virtual std::any visitPipp_format(PippCSParser::Pipp_formatContext *context) = 0;

    virtual std::any visitExt_peak_pick_tbl(PippCSParser::Ext_peak_pick_tblContext *context) = 0;

    virtual std::any visitExt_peak_pick_tbl_row(PippCSParser::Ext_peak_pick_tbl_rowContext *context) = 0;

    virtual std::any visitResidue_list(PippCSParser::Residue_listContext *context) = 0;

    virtual std::any visitRes_id(PippCSParser::Res_idContext *context) = 0;

    virtual std::any visitRes_type(PippCSParser::Res_typeContext *context) = 0;

    virtual std::any visitShift_list(PippCSParser::Shift_listContext *context) = 0;

    virtual std::any visitNumber(PippCSParser::NumberContext *context) = 0;


};

