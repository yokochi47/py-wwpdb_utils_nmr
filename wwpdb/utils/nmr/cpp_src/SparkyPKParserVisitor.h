
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SparkyPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "SparkyPKParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by SparkyPKParser.
 */
class  SparkyPKParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by SparkyPKParser.
   */
    virtual std::any visitSparky_pk(SparkyPKParser::Sparky_pkContext *context) = 0;

    virtual std::any visitData_label(SparkyPKParser::Data_labelContext *context) = 0;

    virtual std::any visitData_label_wo_assign(SparkyPKParser::Data_label_wo_assignContext *context) = 0;

    virtual std::any visitPeak_2d(SparkyPKParser::Peak_2dContext *context) = 0;

    virtual std::any visitPeak_3d(SparkyPKParser::Peak_3dContext *context) = 0;

    virtual std::any visitPeak_4d(SparkyPKParser::Peak_4dContext *context) = 0;

    virtual std::any visitPeak_wo_assign(SparkyPKParser::Peak_wo_assignContext *context) = 0;

    virtual std::any visitPosition(SparkyPKParser::PositionContext *context) = 0;

    virtual std::any visitNumber(SparkyPKParser::NumberContext *context) = 0;

    virtual std::any visitNote(SparkyPKParser::NoteContext *context) = 0;


};

