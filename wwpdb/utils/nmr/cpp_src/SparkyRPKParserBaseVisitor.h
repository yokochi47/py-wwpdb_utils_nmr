
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SparkyRPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "SparkyRPKParserVisitor.h"


/**
 * This class provides an empty implementation of SparkyRPKParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  SparkyRPKParserBaseVisitor : public SparkyRPKParserVisitor {
public:

  virtual std::any visitSparky_rpk(SparkyRPKParser::Sparky_rpkContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitData_label(SparkyRPKParser::Data_labelContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitData_label_wo_assign(SparkyRPKParser::Data_label_wo_assignContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_2d(SparkyRPKParser::Peak_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_3d(SparkyRPKParser::Peak_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_4d(SparkyRPKParser::Peak_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_wo_assign(SparkyRPKParser::Peak_wo_assignContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPosition(SparkyRPKParser::PositionContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(SparkyRPKParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNote(SparkyRPKParser::NoteContext *ctx) override {
    return visitChildren(ctx);
  }


};

