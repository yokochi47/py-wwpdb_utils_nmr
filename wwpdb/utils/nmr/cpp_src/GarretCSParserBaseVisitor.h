
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/GarretCSParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "GarretCSParserVisitor.h"


/**
 * This class provides an empty implementation of GarretCSParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  GarretCSParserBaseVisitor : public GarretCSParserVisitor {
public:

  virtual std::any visitGarret_cs(GarretCSParser::Garret_csContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitResidue_list(GarretCSParser::Residue_listContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitRes_id(GarretCSParser::Res_idContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitShift_list(GarretCSParser::Shift_listContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(GarretCSParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }


};

