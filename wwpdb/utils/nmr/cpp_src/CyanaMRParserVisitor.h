
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CyanaMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "CyanaMRParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by CyanaMRParser.
 */
class  CyanaMRParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by CyanaMRParser.
   */
    virtual std::any visitCyana_mr(CyanaMRParser::Cyana_mrContext *context) = 0;

    virtual std::any visitComment(CyanaMRParser::CommentContext *context) = 0;

    virtual std::any visitDistance_restraints(CyanaMRParser::Distance_restraintsContext *context) = 0;

    virtual std::any visitDistance_restraint(CyanaMRParser::Distance_restraintContext *context) = 0;

    virtual std::any visitTorsion_angle_restraints(CyanaMRParser::Torsion_angle_restraintsContext *context) = 0;

    virtual std::any visitTorsion_angle_restraint(CyanaMRParser::Torsion_angle_restraintContext *context) = 0;

    virtual std::any visitRdc_restraints(CyanaMRParser::Rdc_restraintsContext *context) = 0;

    virtual std::any visitRdc_parameter(CyanaMRParser::Rdc_parameterContext *context) = 0;

    virtual std::any visitRdc_restraint(CyanaMRParser::Rdc_restraintContext *context) = 0;

    virtual std::any visitPcs_restraints(CyanaMRParser::Pcs_restraintsContext *context) = 0;

    virtual std::any visitPcs_parameter(CyanaMRParser::Pcs_parameterContext *context) = 0;

    virtual std::any visitPcs_restraint(CyanaMRParser::Pcs_restraintContext *context) = 0;

    virtual std::any visitFixres_distance_restraints(CyanaMRParser::Fixres_distance_restraintsContext *context) = 0;

    virtual std::any visitFixres_distance_restraint(CyanaMRParser::Fixres_distance_restraintContext *context) = 0;

    virtual std::any visitFixresw_distance_restraints(CyanaMRParser::Fixresw_distance_restraintsContext *context) = 0;

    virtual std::any visitFixresw_distance_restraint(CyanaMRParser::Fixresw_distance_restraintContext *context) = 0;

    virtual std::any visitFixresw2_distance_restraints(CyanaMRParser::Fixresw2_distance_restraintsContext *context) = 0;

    virtual std::any visitFixresw2_distance_restraint(CyanaMRParser::Fixresw2_distance_restraintContext *context) = 0;

    virtual std::any visitFixatm_distance_restraints(CyanaMRParser::Fixatm_distance_restraintsContext *context) = 0;

    virtual std::any visitFixatm_distance_restraint(CyanaMRParser::Fixatm_distance_restraintContext *context) = 0;

    virtual std::any visitFixatmw_distance_restraints(CyanaMRParser::Fixatmw_distance_restraintsContext *context) = 0;

    virtual std::any visitFixatmw_distance_restraint(CyanaMRParser::Fixatmw_distance_restraintContext *context) = 0;

    virtual std::any visitFixatmw2_distance_restraints(CyanaMRParser::Fixatmw2_distance_restraintsContext *context) = 0;

    virtual std::any visitFixatmw2_distance_restraint(CyanaMRParser::Fixatmw2_distance_restraintContext *context) = 0;

    virtual std::any visitDiana_distance_restraints(CyanaMRParser::Diana_distance_restraintsContext *context) = 0;

    virtual std::any visitDiana_distance_restraint(CyanaMRParser::Diana_distance_restraintContext *context) = 0;

    virtual std::any visitDiana_ssbond_restraints(CyanaMRParser::Diana_ssbond_restraintsContext *context) = 0;

    virtual std::any visitDiana_ssbond_restraint(CyanaMRParser::Diana_ssbond_restraintContext *context) = 0;

    virtual std::any visitDiana_torsion_angle_restraints(CyanaMRParser::Diana_torsion_angle_restraintsContext *context) = 0;

    virtual std::any visitDiana_torsion_angle_restraint(CyanaMRParser::Diana_torsion_angle_restraintContext *context) = 0;

    virtual std::any visitDiana_coupling_constant_restraints(CyanaMRParser::Diana_coupling_constant_restraintsContext *context) = 0;

    virtual std::any visitDiana_coupling_constant_restraint(CyanaMRParser::Diana_coupling_constant_restraintContext *context) = 0;

    virtual std::any visitDiana_stereoassign_macro(CyanaMRParser::Diana_stereoassign_macroContext *context) = 0;

    virtual std::any visitDiana_chemical_shifts(CyanaMRParser::Diana_chemical_shiftsContext *context) = 0;

    virtual std::any visitDiana_chemical_shift(CyanaMRParser::Diana_chemical_shiftContext *context) = 0;

    virtual std::any visitDistance_w_chain_restraints(CyanaMRParser::Distance_w_chain_restraintsContext *context) = 0;

    virtual std::any visitDistance_w_chain_restraint(CyanaMRParser::Distance_w_chain_restraintContext *context) = 0;

    virtual std::any visitDistance_w_chain2_restraints(CyanaMRParser::Distance_w_chain2_restraintsContext *context) = 0;

    virtual std::any visitDistance_w_chain2_restraint(CyanaMRParser::Distance_w_chain2_restraintContext *context) = 0;

    virtual std::any visitDistance_w_chain3_restraints(CyanaMRParser::Distance_w_chain3_restraintsContext *context) = 0;

    virtual std::any visitDistance_w_chain3_restraint(CyanaMRParser::Distance_w_chain3_restraintContext *context) = 0;

    virtual std::any visitTorsion_angle_w_chain_restraints(CyanaMRParser::Torsion_angle_w_chain_restraintsContext *context) = 0;

    virtual std::any visitTorsion_angle_w_chain_restraint(CyanaMRParser::Torsion_angle_w_chain_restraintContext *context) = 0;

    virtual std::any visitCco_restraints(CyanaMRParser::Cco_restraintsContext *context) = 0;

    virtual std::any visitCco_restraint(CyanaMRParser::Cco_restraintContext *context) = 0;

    virtual std::any visitSsbond_macro(CyanaMRParser::Ssbond_macroContext *context) = 0;

    virtual std::any visitHbond_macro(CyanaMRParser::Hbond_macroContext *context) = 0;

    virtual std::any visitLink_statement(CyanaMRParser::Link_statementContext *context) = 0;

    virtual std::any visitStereoassign_macro(CyanaMRParser::Stereoassign_macroContext *context) = 0;

    virtual std::any visitDeclare_variable(CyanaMRParser::Declare_variableContext *context) = 0;

    virtual std::any visitSet_variable(CyanaMRParser::Set_variableContext *context) = 0;

    virtual std::any visitUnset_variable(CyanaMRParser::Unset_variableContext *context) = 0;

    virtual std::any visitPrint_macro(CyanaMRParser::Print_macroContext *context) = 0;

    virtual std::any visitUnambig_atom_name_mapping(CyanaMRParser::Unambig_atom_name_mappingContext *context) = 0;

    virtual std::any visitMapping_list(CyanaMRParser::Mapping_listContext *context) = 0;

    virtual std::any visitAmbig_atom_name_mapping(CyanaMRParser::Ambig_atom_name_mappingContext *context) = 0;

    virtual std::any visitAmbig_list(CyanaMRParser::Ambig_listContext *context) = 0;

    virtual std::any visitNumber(CyanaMRParser::NumberContext *context) = 0;

    virtual std::any visitGen_res_num(CyanaMRParser::Gen_res_numContext *context) = 0;

    virtual std::any visitGen_simple_name(CyanaMRParser::Gen_simple_nameContext *context) = 0;

    virtual std::any visitGen_atom_name(CyanaMRParser::Gen_atom_nameContext *context) = 0;


};

