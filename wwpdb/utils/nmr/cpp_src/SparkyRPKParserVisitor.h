
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SparkyRPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "SparkyRPKParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by SparkyRPKParser.
 */
class  SparkyRPKParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by SparkyRPKParser.
   */
    virtual std::any visitSparky_rpk(SparkyRPKParser::Sparky_rpkContext *context) = 0;

    virtual std::any visitData_label(SparkyRPKParser::Data_labelContext *context) = 0;

    virtual std::any visitData_label_wo_assign(SparkyRPKParser::Data_label_wo_assignContext *context) = 0;

    virtual std::any visitPeak_2d(SparkyRPKParser::Peak_2dContext *context) = 0;

    virtual std::any visitPeak_3d(SparkyRPKParser::Peak_3dContext *context) = 0;

    virtual std::any visitPeak_4d(SparkyRPKParser::Peak_4dContext *context) = 0;

    virtual std::any visitPeak_wo_assign(SparkyRPKParser::Peak_wo_assignContext *context) = 0;

    virtual std::any visitPosition(SparkyRPKParser::PositionContext *context) = 0;

    virtual std::any visitNumber(SparkyRPKParser::NumberContext *context) = 0;

    virtual std::any visitNote(SparkyRPKParser::NoteContext *context) = 0;


};

