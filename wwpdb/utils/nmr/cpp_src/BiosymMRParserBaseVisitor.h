
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BiosymMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "BiosymMRParserVisitor.h"


/**
 * This class provides an empty implementation of BiosymMRParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  BiosymMRParserBaseVisitor : public BiosymMRParserVisitor {
public:

  virtual std::any visitBiosym_mr(BiosymMRParser::Biosym_mrContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDistance_restraints(BiosymMRParser::Distance_restraintsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDistance_restraint(BiosymMRParser::Distance_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDistance_constraints(BiosymMRParser::Distance_constraintsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDistance_constraint(BiosymMRParser::Distance_constraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDistance_wo_w_constraints(BiosymMRParser::Distance_wo_w_constraintsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDistance_wo_w_constraint(BiosymMRParser::Distance_wo_w_constraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDihedral_angle_restraints(BiosymMRParser::Dihedral_angle_restraintsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDihedral_angle_restraint(BiosymMRParser::Dihedral_angle_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDihedral_angle_constraints(BiosymMRParser::Dihedral_angle_constraintsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDihedral_angle_constraint(BiosymMRParser::Dihedral_angle_constraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDihedral_angle_wo_w_constraints(BiosymMRParser::Dihedral_angle_wo_w_constraintsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDihedral_angle_wo_w_constraint(BiosymMRParser::Dihedral_angle_wo_w_constraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitChirality_constraints(BiosymMRParser::Chirality_constraintsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitChirality_constraint(BiosymMRParser::Chirality_constraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitProchirality_constraints(BiosymMRParser::Prochirality_constraintsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitProchirality_constraint(BiosymMRParser::Prochirality_constraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitMixing_time(BiosymMRParser::Mixing_timeContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumber(BiosymMRParser::NumberContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitIns_distance_restraints(BiosymMRParser::Ins_distance_restraintsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitIns_distance_restraint(BiosymMRParser::Ins_distance_restraintContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDecl_create(BiosymMRParser::Decl_createContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDecl_function(BiosymMRParser::Decl_functionContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDecl_target(BiosymMRParser::Decl_targetContext *ctx) override {
    return visitChildren(ctx);
  }


};

