
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SparkyPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "SparkyPKParserVisitor.h"


/**
 * This class provides an empty implementation of SparkyPKParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  SparkyPKParserBaseVisitor : public SparkyPKParserVisitor {
public:

  virtual std::any visitSparky_pk(SparkyPKParser::Sparky_pkContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitData_label(SparkyPKParser::Data_labelContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitData_label_wo_assign(SparkyPKParser::Data_label_wo_assignContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_2d(SparkyPKParser::Peak_2dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_3d(SparkyPKParser::Peak_3dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_4d(SparkyPKParser::Peak_4dContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPeak_wo_assign(SparkyPKParser::Peak_wo_assignContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPosition(SparkyPKParser::PositionContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(SparkyPKParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNote(SparkyPKParser::NoteContext *ctx) override {
    return visitChildren(ctx);
  }


};

