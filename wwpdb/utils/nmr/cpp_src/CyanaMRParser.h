
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CyanaMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  CyanaMRParser : public antlr4::Parser {
public:
  enum {
    Ambig_code = 1, Integer = 2, Float = 3, Float_DecimalComma = 4, Orientation_header = 5, 
    Tensor_header = 6, SMCLN_COMMENT = 7, COMMENT = 8, NoeUpp = 9, NoeLow = 10, 
    HBUpp = 11, HBLow = 12, SSUpp = 13, SSLow = 14, Jcoupl = 15, Angle = 16, 
    Stereo = 17, Shifts = 18, Type = 19, Equ_op = 20, Or = 21, Ssbond = 22, 
    Ssbond_resids = 23, Hbond = 24, Link = 25, Atom_stereo = 26, Var = 27, 
    Unset = 28, SetVar = 29, Print = 30, Residue = 31, Mapping = 32, Ambig = 33, 
    Capital_integer = 34, Integer_capital = 35, Simple_name = 36, SPACE = 37, 
    ENCLOSE_COMMENT = 38, SECTION_COMMENT = 39, LINE_COMMENT = 40, Any_name = 41, 
    SPACE_CM = 42, RETURN_CM = 43, Atom1 = 44, Atom2 = 45, Residue1 = 46, 
    Residue2 = 47, Equ_op_HB = 48, Atom1_equ = 49, Atom2_equ = 50, Residue1_equ = 51, 
    Residue2_equ = 52, Concat_atom_1 = 53, Concat_atom_2 = 54, Concat_res_1 = 55, 
    Concat_res_2 = 56, Integer_HB = 57, Simple_name_HB = 58, SPACE_HB = 59, 
    RETURN_HB = 60, LINE_COMMENT_HB = 61, Double_quote_string = 62, SPACE_PR = 63, 
    RETURN_PR = 64, LINE_COMMENT_PR = 65, Simple_name_VA = 66, SPACE_VA = 67, 
    RETURN_VA = 68, LINE_COMMENT_VA = 69, Ambig_code_MP = 70, Integer_MP = 71, 
    Simple_name_MP = 72, Equ_op_MP = 73, SPACE_MP = 74, RETURN_MP = 75, 
    LINE_COMMENT_MP = 76
  };

  enum {
    RuleCyana_mr = 0, RuleComment = 1, RuleDistance_restraints = 2, RuleDistance_restraint = 3, 
    RuleTorsion_angle_restraints = 4, RuleTorsion_angle_restraint = 5, RuleRdc_restraints = 6, 
    RuleRdc_parameter = 7, RuleRdc_restraint = 8, RulePcs_restraints = 9, 
    RulePcs_parameter = 10, RulePcs_restraint = 11, RuleFixres_distance_restraints = 12, 
    RuleFixres_distance_restraint = 13, RuleFixresw_distance_restraints = 14, 
    RuleFixresw_distance_restraint = 15, RuleFixresw2_distance_restraints = 16, 
    RuleFixresw2_distance_restraint = 17, RuleFixatm_distance_restraints = 18, 
    RuleFixatm_distance_restraint = 19, RuleFixatmw_distance_restraints = 20, 
    RuleFixatmw_distance_restraint = 21, RuleFixatmw2_distance_restraints = 22, 
    RuleFixatmw2_distance_restraint = 23, RuleDiana_distance_restraints = 24, 
    RuleDiana_distance_restraint = 25, RuleDiana_ssbond_restraints = 26, 
    RuleDiana_ssbond_restraint = 27, RuleDiana_hbond_restraints = 28, RuleDiana_hbond_restraint = 29, 
    RuleDiana_torsion_angle_restraints = 30, RuleDiana_torsion_angle_restraint = 31, 
    RuleDiana_coupling_constant_restraints = 32, RuleDiana_coupling_constant_restraint = 33, 
    RuleDiana_stereoassign_macro = 34, RuleDiana_chemical_shifts = 35, RuleDiana_chemical_shift = 36, 
    RuleDistance_w_chain_restraints = 37, RuleDistance_w_chain_restraint = 38, 
    RuleDistance_w_chain2_restraints = 39, RuleDistance_w_chain2_restraint = 40, 
    RuleDistance_w_chain3_restraints = 41, RuleDistance_w_chain3_restraint = 42, 
    RuleTorsion_angle_w_chain_restraints = 43, RuleTorsion_angle_w_chain_restraint = 44, 
    RuleCco_restraints = 45, RuleCco_restraint = 46, RuleSsbond_macro = 47, 
    RuleHbond_macro = 48, RuleLink_statement = 49, RuleStereoassign_macro = 50, 
    RuleDeclare_variable = 51, RuleSet_variable = 52, RuleUnset_variable = 53, 
    RulePrint_macro = 54, RuleUnambig_atom_name_mapping = 55, RuleMapping_list = 56, 
    RuleAmbig_atom_name_mapping = 57, RuleAmbig_list = 58, RuleNumber = 59, 
    RuleGen_res_num = 60, RuleGen_simple_name = 61, RuleGen_atom_name = 62
  };

  explicit CyanaMRParser(antlr4::TokenStream *input);

  CyanaMRParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~CyanaMRParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Cyana_mrContext;
  class CommentContext;
  class Distance_restraintsContext;
  class Distance_restraintContext;
  class Torsion_angle_restraintsContext;
  class Torsion_angle_restraintContext;
  class Rdc_restraintsContext;
  class Rdc_parameterContext;
  class Rdc_restraintContext;
  class Pcs_restraintsContext;
  class Pcs_parameterContext;
  class Pcs_restraintContext;
  class Fixres_distance_restraintsContext;
  class Fixres_distance_restraintContext;
  class Fixresw_distance_restraintsContext;
  class Fixresw_distance_restraintContext;
  class Fixresw2_distance_restraintsContext;
  class Fixresw2_distance_restraintContext;
  class Fixatm_distance_restraintsContext;
  class Fixatm_distance_restraintContext;
  class Fixatmw_distance_restraintsContext;
  class Fixatmw_distance_restraintContext;
  class Fixatmw2_distance_restraintsContext;
  class Fixatmw2_distance_restraintContext;
  class Diana_distance_restraintsContext;
  class Diana_distance_restraintContext;
  class Diana_ssbond_restraintsContext;
  class Diana_ssbond_restraintContext;
  class Diana_hbond_restraintsContext;
  class Diana_hbond_restraintContext;
  class Diana_torsion_angle_restraintsContext;
  class Diana_torsion_angle_restraintContext;
  class Diana_coupling_constant_restraintsContext;
  class Diana_coupling_constant_restraintContext;
  class Diana_stereoassign_macroContext;
  class Diana_chemical_shiftsContext;
  class Diana_chemical_shiftContext;
  class Distance_w_chain_restraintsContext;
  class Distance_w_chain_restraintContext;
  class Distance_w_chain2_restraintsContext;
  class Distance_w_chain2_restraintContext;
  class Distance_w_chain3_restraintsContext;
  class Distance_w_chain3_restraintContext;
  class Torsion_angle_w_chain_restraintsContext;
  class Torsion_angle_w_chain_restraintContext;
  class Cco_restraintsContext;
  class Cco_restraintContext;
  class Ssbond_macroContext;
  class Hbond_macroContext;
  class Link_statementContext;
  class Stereoassign_macroContext;
  class Declare_variableContext;
  class Set_variableContext;
  class Unset_variableContext;
  class Print_macroContext;
  class Unambig_atom_name_mappingContext;
  class Mapping_listContext;
  class Ambig_atom_name_mappingContext;
  class Ambig_listContext;
  class NumberContext;
  class Gen_res_numContext;
  class Gen_simple_nameContext;
  class Gen_atom_nameContext; 

  class  Cyana_mrContext : public antlr4::ParserRuleContext {
  public:
    Cyana_mrContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Orientation_header();
    antlr4::tree::TerminalNode* Orientation_header(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<Distance_restraintsContext *> distance_restraints();
    Distance_restraintsContext* distance_restraints(size_t i);
    std::vector<Fixres_distance_restraintsContext *> fixres_distance_restraints();
    Fixres_distance_restraintsContext* fixres_distance_restraints(size_t i);
    std::vector<Fixresw_distance_restraintsContext *> fixresw_distance_restraints();
    Fixresw_distance_restraintsContext* fixresw_distance_restraints(size_t i);
    std::vector<Fixresw2_distance_restraintsContext *> fixresw2_distance_restraints();
    Fixresw2_distance_restraintsContext* fixresw2_distance_restraints(size_t i);
    std::vector<Fixatm_distance_restraintsContext *> fixatm_distance_restraints();
    Fixatm_distance_restraintsContext* fixatm_distance_restraints(size_t i);
    std::vector<Fixatmw_distance_restraintsContext *> fixatmw_distance_restraints();
    Fixatmw_distance_restraintsContext* fixatmw_distance_restraints(size_t i);
    std::vector<Fixatmw2_distance_restraintsContext *> fixatmw2_distance_restraints();
    Fixatmw2_distance_restraintsContext* fixatmw2_distance_restraints(size_t i);
    std::vector<Diana_distance_restraintsContext *> diana_distance_restraints();
    Diana_distance_restraintsContext* diana_distance_restraints(size_t i);
    std::vector<Diana_ssbond_restraintsContext *> diana_ssbond_restraints();
    Diana_ssbond_restraintsContext* diana_ssbond_restraints(size_t i);
    std::vector<Diana_hbond_restraintsContext *> diana_hbond_restraints();
    Diana_hbond_restraintsContext* diana_hbond_restraints(size_t i);
    std::vector<Diana_torsion_angle_restraintsContext *> diana_torsion_angle_restraints();
    Diana_torsion_angle_restraintsContext* diana_torsion_angle_restraints(size_t i);
    std::vector<Diana_coupling_constant_restraintsContext *> diana_coupling_constant_restraints();
    Diana_coupling_constant_restraintsContext* diana_coupling_constant_restraints(size_t i);
    std::vector<Diana_stereoassign_macroContext *> diana_stereoassign_macro();
    Diana_stereoassign_macroContext* diana_stereoassign_macro(size_t i);
    std::vector<Diana_chemical_shiftsContext *> diana_chemical_shifts();
    Diana_chemical_shiftsContext* diana_chemical_shifts(size_t i);
    std::vector<Distance_w_chain_restraintsContext *> distance_w_chain_restraints();
    Distance_w_chain_restraintsContext* distance_w_chain_restraints(size_t i);
    std::vector<Distance_w_chain2_restraintsContext *> distance_w_chain2_restraints();
    Distance_w_chain2_restraintsContext* distance_w_chain2_restraints(size_t i);
    std::vector<Distance_w_chain3_restraintsContext *> distance_w_chain3_restraints();
    Distance_w_chain3_restraintsContext* distance_w_chain3_restraints(size_t i);
    std::vector<Torsion_angle_restraintsContext *> torsion_angle_restraints();
    Torsion_angle_restraintsContext* torsion_angle_restraints(size_t i);
    std::vector<Torsion_angle_w_chain_restraintsContext *> torsion_angle_w_chain_restraints();
    Torsion_angle_w_chain_restraintsContext* torsion_angle_w_chain_restraints(size_t i);
    std::vector<Rdc_restraintsContext *> rdc_restraints();
    Rdc_restraintsContext* rdc_restraints(size_t i);
    std::vector<Pcs_restraintsContext *> pcs_restraints();
    Pcs_restraintsContext* pcs_restraints(size_t i);
    std::vector<Cco_restraintsContext *> cco_restraints();
    Cco_restraintsContext* cco_restraints(size_t i);
    std::vector<Ssbond_macroContext *> ssbond_macro();
    Ssbond_macroContext* ssbond_macro(size_t i);
    std::vector<Hbond_macroContext *> hbond_macro();
    Hbond_macroContext* hbond_macro(size_t i);
    std::vector<Link_statementContext *> link_statement();
    Link_statementContext* link_statement(size_t i);
    std::vector<Stereoassign_macroContext *> stereoassign_macro();
    Stereoassign_macroContext* stereoassign_macro(size_t i);
    std::vector<Declare_variableContext *> declare_variable();
    Declare_variableContext* declare_variable(size_t i);
    std::vector<Set_variableContext *> set_variable();
    Set_variableContext* set_variable(size_t i);
    std::vector<Unset_variableContext *> unset_variable();
    Unset_variableContext* unset_variable(size_t i);
    std::vector<Print_macroContext *> print_macro();
    Print_macroContext* print_macro(size_t i);
    std::vector<Unambig_atom_name_mappingContext *> unambig_atom_name_mapping();
    Unambig_atom_name_mappingContext* unambig_atom_name_mapping(size_t i);
    std::vector<Ambig_atom_name_mappingContext *> ambig_atom_name_mapping();
    Ambig_atom_name_mappingContext* ambig_atom_name_mapping(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Tensor_header();
    antlr4::tree::TerminalNode* Tensor_header(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Cyana_mrContext* cyana_mr();

  class  CommentContext : public antlr4::ParserRuleContext {
  public:
    CommentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *COMMENT();
    antlr4::tree::TerminalNode *RETURN_CM();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Any_name();
    antlr4::tree::TerminalNode* Any_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  CommentContext* comment();

  class  Distance_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Distance_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Distance_restraintContext *> distance_restraint();
    Distance_restraintContext* distance_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_restraintsContext* distance_restraints();

  class  Distance_restraintContext : public antlr4::ParserRuleContext {
  public:
    Distance_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<Gen_atom_nameContext *> gen_atom_name();
    Gen_atom_nameContext* gen_atom_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_restraintContext* distance_restraint();

  class  Torsion_angle_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Torsion_angle_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Torsion_angle_restraintContext *> torsion_angle_restraint();
    Torsion_angle_restraintContext* torsion_angle_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Torsion_angle_restraintsContext* torsion_angle_restraints();

  class  Torsion_angle_restraintContext : public antlr4::ParserRuleContext {
  public:
    Torsion_angle_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Gen_res_numContext *gen_res_num();
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Type();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Or();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Torsion_angle_restraintContext* torsion_angle_restraint();

  class  Rdc_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Rdc_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Rdc_parameterContext *> rdc_parameter();
    Rdc_parameterContext* rdc_parameter(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Orientation_header();
    antlr4::tree::TerminalNode* Orientation_header(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<Rdc_restraintContext *> rdc_restraint();
    Rdc_restraintContext* rdc_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rdc_restraintsContext* rdc_restraints();

  class  Rdc_parameterContext : public antlr4::ParserRuleContext {
  public:
    Rdc_parameterContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Capital_integer();
    antlr4::tree::TerminalNode *Integer_capital();
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rdc_parameterContext* rdc_parameter();

  class  Rdc_restraintContext : public antlr4::ParserRuleContext {
  public:
    Rdc_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rdc_restraintContext* rdc_restraint();

  class  Pcs_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Pcs_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Pcs_parameterContext *> pcs_parameter();
    Pcs_parameterContext* pcs_parameter(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Orientation_header();
    antlr4::tree::TerminalNode* Orientation_header(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<Pcs_restraintContext *> pcs_restraint();
    Pcs_restraintContext* pcs_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pcs_restraintsContext* pcs_restraints();

  class  Pcs_parameterContext : public antlr4::ParserRuleContext {
  public:
    Pcs_parameterContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Capital_integer();
    antlr4::tree::TerminalNode *Integer_capital();
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pcs_parameterContext* pcs_parameter();

  class  Pcs_restraintContext : public antlr4::ParserRuleContext {
  public:
    Pcs_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Gen_res_numContext *gen_res_num();
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pcs_restraintContext* pcs_restraint();

  class  Fixres_distance_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Fixres_distance_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Fixres_distance_restraintContext *> fixres_distance_restraint();
    Fixres_distance_restraintContext* fixres_distance_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fixres_distance_restraintsContext* fixres_distance_restraints();

  class  Fixres_distance_restraintContext : public antlr4::ParserRuleContext {
  public:
    Fixres_distance_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fixres_distance_restraintContext* fixres_distance_restraint();

  class  Fixresw_distance_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Fixresw_distance_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Fixresw_distance_restraintContext *> fixresw_distance_restraint();
    Fixresw_distance_restraintContext* fixresw_distance_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fixresw_distance_restraintsContext* fixresw_distance_restraints();

  class  Fixresw_distance_restraintContext : public antlr4::ParserRuleContext {
  public:
    Fixresw_distance_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fixresw_distance_restraintContext* fixresw_distance_restraint();

  class  Fixresw2_distance_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Fixresw2_distance_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Fixresw2_distance_restraintContext *> fixresw2_distance_restraint();
    Fixresw2_distance_restraintContext* fixresw2_distance_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fixresw2_distance_restraintsContext* fixresw2_distance_restraints();

  class  Fixresw2_distance_restraintContext : public antlr4::ParserRuleContext {
  public:
    Fixresw2_distance_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fixresw2_distance_restraintContext* fixresw2_distance_restraint();

  class  Fixatm_distance_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Fixatm_distance_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Fixatm_distance_restraintContext *> fixatm_distance_restraint();
    Fixatm_distance_restraintContext* fixatm_distance_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fixatm_distance_restraintsContext* fixatm_distance_restraints();

  class  Fixatm_distance_restraintContext : public antlr4::ParserRuleContext {
  public:
    Fixatm_distance_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fixatm_distance_restraintContext* fixatm_distance_restraint();

  class  Fixatmw_distance_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Fixatmw_distance_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Fixatmw_distance_restraintContext *> fixatmw_distance_restraint();
    Fixatmw_distance_restraintContext* fixatmw_distance_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fixatmw_distance_restraintsContext* fixatmw_distance_restraints();

  class  Fixatmw_distance_restraintContext : public antlr4::ParserRuleContext {
  public:
    Fixatmw_distance_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fixatmw_distance_restraintContext* fixatmw_distance_restraint();

  class  Fixatmw2_distance_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Fixatmw2_distance_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Fixatmw2_distance_restraintContext *> fixatmw2_distance_restraint();
    Fixatmw2_distance_restraintContext* fixatmw2_distance_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fixatmw2_distance_restraintsContext* fixatmw2_distance_restraints();

  class  Fixatmw2_distance_restraintContext : public antlr4::ParserRuleContext {
  public:
    Fixatmw2_distance_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Fixatmw2_distance_restraintContext* fixatmw2_distance_restraint();

  class  Diana_distance_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Diana_distance_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Diana_distance_restraintContext *> diana_distance_restraint();
    Diana_distance_restraintContext* diana_distance_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Diana_distance_restraintsContext* diana_distance_restraints();

  class  Diana_distance_restraintContext : public antlr4::ParserRuleContext {
  public:
    Diana_distance_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *NoeUpp();
    antlr4::tree::TerminalNode *NoeLow();
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Diana_distance_restraintContext* diana_distance_restraint();

  class  Diana_ssbond_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Diana_ssbond_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Diana_ssbond_restraintContext *> diana_ssbond_restraint();
    Diana_ssbond_restraintContext* diana_ssbond_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Diana_ssbond_restraintsContext* diana_ssbond_restraints();

  class  Diana_ssbond_restraintContext : public antlr4::ParserRuleContext {
  public:
    Diana_ssbond_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *SSUpp();
    antlr4::tree::TerminalNode *SSLow();
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Diana_ssbond_restraintContext* diana_ssbond_restraint();

  class  Diana_hbond_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Diana_hbond_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Diana_hbond_restraintContext *> diana_hbond_restraint();
    Diana_hbond_restraintContext* diana_hbond_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Diana_hbond_restraintsContext* diana_hbond_restraints();

  class  Diana_hbond_restraintContext : public antlr4::ParserRuleContext {
  public:
    Diana_hbond_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *HBUpp();
    antlr4::tree::TerminalNode *HBLow();
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Diana_hbond_restraintContext* diana_hbond_restraint();

  class  Diana_torsion_angle_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Diana_torsion_angle_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Diana_torsion_angle_restraintContext *> diana_torsion_angle_restraint();
    Diana_torsion_angle_restraintContext* diana_torsion_angle_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Diana_torsion_angle_restraintsContext* diana_torsion_angle_restraints();

  class  Diana_torsion_angle_restraintContext : public antlr4::ParserRuleContext {
  public:
    Diana_torsion_angle_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Angle();
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    Gen_res_numContext *gen_res_num();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Diana_torsion_angle_restraintContext* diana_torsion_angle_restraint();

  class  Diana_coupling_constant_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Diana_coupling_constant_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Diana_coupling_constant_restraintContext *> diana_coupling_constant_restraint();
    Diana_coupling_constant_restraintContext* diana_coupling_constant_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Diana_coupling_constant_restraintsContext* diana_coupling_constant_restraints();

  class  Diana_coupling_constant_restraintContext : public antlr4::ParserRuleContext {
  public:
    Diana_coupling_constant_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Jcoupl();
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    Gen_res_numContext *gen_res_num();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Diana_coupling_constant_restraintContext* diana_coupling_constant_restraint();

  class  Diana_stereoassign_macroContext : public antlr4::ParserRuleContext {
  public:
    Diana_stereoassign_macroContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Stereo();
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    Gen_res_numContext *gen_res_num();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Diana_stereoassign_macroContext* diana_stereoassign_macro();

  class  Diana_chemical_shiftsContext : public antlr4::ParserRuleContext {
  public:
    Diana_chemical_shiftsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Diana_chemical_shiftContext *> diana_chemical_shift();
    Diana_chemical_shiftContext* diana_chemical_shift(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Diana_chemical_shiftsContext* diana_chemical_shifts();

  class  Diana_chemical_shiftContext : public antlr4::ParserRuleContext {
  public:
    Diana_chemical_shiftContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Shifts();
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    Gen_res_numContext *gen_res_num();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Diana_chemical_shiftContext* diana_chemical_shift();

  class  Distance_w_chain_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Distance_w_chain_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Distance_w_chain_restraintContext *> distance_w_chain_restraint();
    Distance_w_chain_restraintContext* distance_w_chain_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_w_chain_restraintsContext* distance_w_chain_restraints();

  class  Distance_w_chain_restraintContext : public antlr4::ParserRuleContext {
  public:
    Distance_w_chain_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_w_chain_restraintContext* distance_w_chain_restraint();

  class  Distance_w_chain2_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Distance_w_chain2_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Distance_w_chain2_restraintContext *> distance_w_chain2_restraint();
    Distance_w_chain2_restraintContext* distance_w_chain2_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_w_chain2_restraintsContext* distance_w_chain2_restraints();

  class  Distance_w_chain2_restraintContext : public antlr4::ParserRuleContext {
  public:
    Distance_w_chain2_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_w_chain2_restraintContext* distance_w_chain2_restraint();

  class  Distance_w_chain3_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Distance_w_chain3_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Distance_w_chain3_restraintContext *> distance_w_chain3_restraint();
    Distance_w_chain3_restraintContext* distance_w_chain3_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_w_chain3_restraintsContext* distance_w_chain3_restraints();

  class  Distance_w_chain3_restraintContext : public antlr4::ParserRuleContext {
  public:
    Distance_w_chain3_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_w_chain3_restraintContext* distance_w_chain3_restraint();

  class  Torsion_angle_w_chain_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Torsion_angle_w_chain_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Torsion_angle_w_chain_restraintContext *> torsion_angle_w_chain_restraint();
    Torsion_angle_w_chain_restraintContext* torsion_angle_w_chain_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Torsion_angle_w_chain_restraintsContext* torsion_angle_w_chain_restraints();

  class  Torsion_angle_w_chain_restraintContext : public antlr4::ParserRuleContext {
  public:
    Torsion_angle_w_chain_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Type();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Or();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Torsion_angle_w_chain_restraintContext* torsion_angle_w_chain_restraint();

  class  Cco_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Cco_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Cco_restraintContext *> cco_restraint();
    Cco_restraintContext* cco_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Cco_restraintsContext* cco_restraints();

  class  Cco_restraintContext : public antlr4::ParserRuleContext {
  public:
    Cco_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Gen_res_numContext *gen_res_num();
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Cco_restraintContext* cco_restraint();

  class  Ssbond_macroContext : public antlr4::ParserRuleContext {
  public:
    Ssbond_macroContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Ssbond();
    antlr4::tree::TerminalNode *Ssbond_resids();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ssbond_macroContext* ssbond_macro();

  class  Hbond_macroContext : public antlr4::ParserRuleContext {
  public:
    Hbond_macroContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Hbond();
    antlr4::tree::TerminalNode *RETURN_HB();
    std::vector<antlr4::tree::TerminalNode *> Simple_name_HB();
    antlr4::tree::TerminalNode* Simple_name_HB(size_t i);
    antlr4::tree::TerminalNode *Concat_atom_1();
    std::vector<antlr4::tree::TerminalNode *> Integer_HB();
    antlr4::tree::TerminalNode* Integer_HB(size_t i);
    antlr4::tree::TerminalNode *Concat_res_1();
    antlr4::tree::TerminalNode *Concat_atom_2();
    antlr4::tree::TerminalNode *Concat_res_2();
    antlr4::tree::TerminalNode *Atom1();
    std::vector<antlr4::tree::TerminalNode *> Equ_op_HB();
    antlr4::tree::TerminalNode* Equ_op_HB(size_t i);
    antlr4::tree::TerminalNode *Atom1_equ();
    antlr4::tree::TerminalNode *Residue1();
    antlr4::tree::TerminalNode *Residue1_equ();
    antlr4::tree::TerminalNode *Atom2();
    antlr4::tree::TerminalNode *Atom2_equ();
    antlr4::tree::TerminalNode *Residue2();
    antlr4::tree::TerminalNode *Residue2_equ();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Hbond_macroContext* hbond_macro();

  class  Link_statementContext : public antlr4::ParserRuleContext {
  public:
    Link_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Link();
    std::vector<Gen_simple_nameContext *> gen_simple_name();
    Gen_simple_nameContext* gen_simple_name(size_t i);
    std::vector<Gen_res_numContext *> gen_res_num();
    Gen_res_numContext* gen_res_num(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Link_statementContext* link_statement();

  class  Stereoassign_macroContext : public antlr4::ParserRuleContext {
  public:
    Stereoassign_macroContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Atom_stereo();
    antlr4::tree::TerminalNode *Double_quote_string();
    antlr4::tree::TerminalNode *RETURN_PR();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Stereoassign_macroContext* stereoassign_macro();

  class  Declare_variableContext : public antlr4::ParserRuleContext {
  public:
    Declare_variableContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Var();
    antlr4::tree::TerminalNode *RETURN_VA();
    std::vector<antlr4::tree::TerminalNode *> Simple_name_VA();
    antlr4::tree::TerminalNode* Simple_name_VA(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Declare_variableContext* declare_variable();

  class  Set_variableContext : public antlr4::ParserRuleContext {
  public:
    Set_variableContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *SetVar();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Set_variableContext* set_variable();

  class  Unset_variableContext : public antlr4::ParserRuleContext {
  public:
    Unset_variableContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Unset();
    antlr4::tree::TerminalNode *RETURN_VA();
    std::vector<antlr4::tree::TerminalNode *> Simple_name_VA();
    antlr4::tree::TerminalNode* Simple_name_VA(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Unset_variableContext* unset_variable();

  class  Print_macroContext : public antlr4::ParserRuleContext {
  public:
    Print_macroContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Double_quote_string();
    antlr4::tree::TerminalNode *RETURN_PR();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Print_macroContext* print_macro();

  class  Unambig_atom_name_mappingContext : public antlr4::ParserRuleContext {
  public:
    Unambig_atom_name_mappingContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Residue();
    Gen_simple_nameContext *gen_simple_name();
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<Mapping_listContext *> mapping_list();
    Mapping_listContext* mapping_list(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Unambig_atom_name_mappingContext* unambig_atom_name_mapping();

  class  Mapping_listContext : public antlr4::ParserRuleContext {
  public:
    Mapping_listContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Mapping();
    std::vector<antlr4::tree::TerminalNode *> Simple_name_MP();
    antlr4::tree::TerminalNode* Simple_name_MP(size_t i);
    antlr4::tree::TerminalNode *Equ_op_MP();
    antlr4::tree::TerminalNode *RETURN_MP();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Mapping_listContext* mapping_list();

  class  Ambig_atom_name_mappingContext : public antlr4::ParserRuleContext {
  public:
    Ambig_atom_name_mappingContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Residue();
    Gen_simple_nameContext *gen_simple_name();
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<Ambig_listContext *> ambig_list();
    Ambig_listContext* ambig_list(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ambig_atom_name_mappingContext* ambig_atom_name_mapping();

  class  Ambig_listContext : public antlr4::ParserRuleContext {
  public:
    Ambig_listContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Ambig();
    antlr4::tree::TerminalNode *Equ_op_MP();
    antlr4::tree::TerminalNode *RETURN_MP();
    std::vector<antlr4::tree::TerminalNode *> Simple_name_MP();
    antlr4::tree::TerminalNode* Simple_name_MP(size_t i);
    antlr4::tree::TerminalNode *Ambig_code_MP();
    std::vector<antlr4::tree::TerminalNode *> Integer_MP();
    antlr4::tree::TerminalNode* Integer_MP(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ambig_listContext* ambig_list();

  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Float_DecimalComma();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NumberContext* number();

  class  Gen_res_numContext : public antlr4::ParserRuleContext {
  public:
    Gen_res_numContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Capital_integer();
    antlr4::tree::TerminalNode *Integer_capital();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Gen_res_numContext* gen_res_num();

  class  Gen_simple_nameContext : public antlr4::ParserRuleContext {
  public:
    Gen_simple_nameContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Capital_integer();
    antlr4::tree::TerminalNode *Integer_capital();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Gen_simple_nameContext* gen_simple_name();

  class  Gen_atom_nameContext : public antlr4::ParserRuleContext {
  public:
    Gen_atom_nameContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Capital_integer();
    antlr4::tree::TerminalNode *Integer_capital();
    antlr4::tree::TerminalNode *Ambig_code();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Gen_atom_nameContext* gen_atom_name();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

