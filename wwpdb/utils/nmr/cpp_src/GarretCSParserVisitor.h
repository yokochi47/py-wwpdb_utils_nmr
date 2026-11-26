
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/GarretCSParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "GarretCSParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by GarretCSParser.
 */
class  GarretCSParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by GarretCSParser.
   */
    virtual std::any visitGarret_cs(GarretCSParser::Garret_csContext *context) = 0;

    virtual std::any visitResidue_list(GarretCSParser::Residue_listContext *context) = 0;

    virtual std::any visitRes_id(GarretCSParser::Res_idContext *context) = 0;

    virtual std::any visitShift_list(GarretCSParser::Shift_listContext *context) = 0;

    virtual std::any visitNumber(GarretCSParser::NumberContext *context) = 0;


};

