
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/PippCSParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "PippCSParserVisitor.h"


/**
 * This class provides an empty implementation of PippCSParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  PippCSParserBaseVisitor : public PippCSParserVisitor {
public:

  virtual std::any visitPipp_cs(PippCSParser::Pipp_csContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitPipp_format(PippCSParser::Pipp_formatContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExt_peak_pick_tbl(PippCSParser::Ext_peak_pick_tblContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExt_peak_pick_tbl_row(PippCSParser::Ext_peak_pick_tbl_rowContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitResidue_list(PippCSParser::Residue_listContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitRes_id(PippCSParser::Res_idContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitRes_type(PippCSParser::Res_typeContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitShift_list(PippCSParser::Shift_listContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(PippCSParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }


};

