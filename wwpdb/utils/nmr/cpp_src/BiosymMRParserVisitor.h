
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BiosymMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "BiosymMRParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by BiosymMRParser.
 */
class  BiosymMRParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by BiosymMRParser.
   */
    virtual std::any visitBiosym_mr(BiosymMRParser::Biosym_mrContext *context) = 0;

    virtual std::any visitDistance_restraints(BiosymMRParser::Distance_restraintsContext *context) = 0;

    virtual std::any visitDistance_restraint(BiosymMRParser::Distance_restraintContext *context) = 0;

    virtual std::any visitDistance_constraints(BiosymMRParser::Distance_constraintsContext *context) = 0;

    virtual std::any visitDistance_constraint(BiosymMRParser::Distance_constraintContext *context) = 0;

    virtual std::any visitDistance_wo_w_constraints(BiosymMRParser::Distance_wo_w_constraintsContext *context) = 0;

    virtual std::any visitDistance_wo_w_constraint(BiosymMRParser::Distance_wo_w_constraintContext *context) = 0;

    virtual std::any visitDihedral_angle_restraints(BiosymMRParser::Dihedral_angle_restraintsContext *context) = 0;

    virtual std::any visitDihedral_angle_restraint(BiosymMRParser::Dihedral_angle_restraintContext *context) = 0;

    virtual std::any visitDihedral_angle_constraints(BiosymMRParser::Dihedral_angle_constraintsContext *context) = 0;

    virtual std::any visitDihedral_angle_constraint(BiosymMRParser::Dihedral_angle_constraintContext *context) = 0;

    virtual std::any visitDihedral_angle_wo_w_constraints(BiosymMRParser::Dihedral_angle_wo_w_constraintsContext *context) = 0;

    virtual std::any visitDihedral_angle_wo_w_constraint(BiosymMRParser::Dihedral_angle_wo_w_constraintContext *context) = 0;

    virtual std::any visitChirality_constraints(BiosymMRParser::Chirality_constraintsContext *context) = 0;

    virtual std::any visitChirality_constraint(BiosymMRParser::Chirality_constraintContext *context) = 0;

    virtual std::any visitProchirality_constraints(BiosymMRParser::Prochirality_constraintsContext *context) = 0;

    virtual std::any visitProchirality_constraint(BiosymMRParser::Prochirality_constraintContext *context) = 0;

    virtual std::any visitMixing_time(BiosymMRParser::Mixing_timeContext *context) = 0;

    virtual std::any visitNumber(BiosymMRParser::NumberContext *context) = 0;

    virtual std::any visitIns_distance_restraints(BiosymMRParser::Ins_distance_restraintsContext *context) = 0;

    virtual std::any visitIns_distance_restraint(BiosymMRParser::Ins_distance_restraintContext *context) = 0;

    virtual std::any visitDecl_create(BiosymMRParser::Decl_createContext *context) = 0;

    virtual std::any visitDecl_function(BiosymMRParser::Decl_functionContext *context) = 0;

    virtual std::any visitDecl_target(BiosymMRParser::Decl_targetContext *context) = 0;


};

