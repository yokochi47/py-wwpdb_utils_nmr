
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SparkyNPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "SparkyNPKParserVisitor.h"


/**
 * This class provides an empty implementation of SparkyNPKParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  SparkyNPKParserBaseVisitor : public SparkyNPKParserVisitor {
public:

  virtual std::any visitSparky_npk(SparkyNPKParser::Sparky_npkContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitData_label(SparkyNPKParser::Data_labelContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_2d(SparkyNPKParser::Peak_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_3d(SparkyNPKParser::Peak_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_4d(SparkyNPKParser::Peak_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_2d_po(SparkyNPKParser::Peak_2d_poContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_3d_po(SparkyNPKParser::Peak_3d_poContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_4d_po(SparkyNPKParser::Peak_4d_poContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPosition(SparkyNPKParser::PositionContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(SparkyNPKParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNote(SparkyNPKParser::NoteContext *ctx) override {
    return visitChildren(ctx);
  }


};

