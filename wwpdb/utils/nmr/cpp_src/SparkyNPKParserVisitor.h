
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SparkyNPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "SparkyNPKParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by SparkyNPKParser.
 */
class  SparkyNPKParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by SparkyNPKParser.
   */
    virtual std::any visitSparky_npk(SparkyNPKParser::Sparky_npkContext *context) = 0;

    virtual std::any visitData_label(SparkyNPKParser::Data_labelContext *context) = 0;

    virtual std::any visitPeak_2d(SparkyNPKParser::Peak_2dContext *context) = 0;

    virtual std::any visitPeak_3d(SparkyNPKParser::Peak_3dContext *context) = 0;

    virtual std::any visitPeak_4d(SparkyNPKParser::Peak_4dContext *context) = 0;

    virtual std::any visitPeak_2d_po(SparkyNPKParser::Peak_2d_poContext *context) = 0;

    virtual std::any visitPeak_3d_po(SparkyNPKParser::Peak_3d_poContext *context) = 0;

    virtual std::any visitPeak_4d_po(SparkyNPKParser::Peak_4d_poContext *context) = 0;

    virtual std::any visitPosition(SparkyNPKParser::PositionContext *context) = 0;

    virtual std::any visitNumber(SparkyNPKParser::NumberContext *context) = 0;

    virtual std::any visitNote(SparkyNPKParser::NoteContext *context) = 0;


};

