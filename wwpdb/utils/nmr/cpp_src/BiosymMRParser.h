
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BiosymMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  BiosymMRParser : public antlr4::Parser {
public:
  enum {
    Integer = 1, Float = 2, Float_DecimalComma = 3, Real = 4, SHARP_COMMENT = 5, 
    EXCLM_COMMENT = 6, SMCLN_COMMENT = 7, Chiral_code = 8, Atom_selection = 9, 
    Ordinal = 10, Or = 11, Restraint = 12, Mixing_times = 13, SPACE = 14, 
    RETURN = 15, ENCLOSE_COMMENT = 16, SECTION_COMMENT = 17, LINE_COMMENT = 18, 
    Integer_II = 19, Float_II = 20, Create = 21, Function = 22, Target = 23, 
    Distance = 24, Torsion = 25, Quadratic = 26, Flat_bottomed = 27, Relative = 28, 
    Trans = 29, Simple_name_II = 30, Double_quote_string_II = 31, CONTINUE = 32, 
    SPACE_II = 33, RETURN_II = 34, Real_MT = 35, Float_MT = 36, Integer_MT = 37, 
    And_MR = 38, SPACE_MT = 39, RETURN_MT = 40
  };

  enum {
    RuleBiosym_mr = 0, RuleDistance_restraints = 1, RuleDistance_restraint = 2, 
    RuleDistance_constraints = 3, RuleDistance_constraint = 4, RuleDistance_wo_w_constraints = 5, 
    RuleDistance_wo_w_constraint = 6, RuleDihedral_angle_restraints = 7, 
    RuleDihedral_angle_restraint = 8, RuleDihedral_angle_constraints = 9, 
    RuleDihedral_angle_constraint = 10, RuleDihedral_angle_wo_w_constraints = 11, 
    RuleDihedral_angle_wo_w_constraint = 12, RuleRdc_restraints = 13, RuleRdc_restraint = 14, 
    RuleChirality_constraints = 15, RuleChirality_constraint = 16, RuleProchirality_constraints = 17, 
    RuleProchirality_constraint = 18, RuleMixing_time = 19, RuleNumber = 20, 
    RuleIns_distance_restraints = 21, RuleIns_distance_restraint = 22, RuleIns_dihedral_angle_restraints = 23, 
    RuleIns_dihedral_angle_restraint = 24, RuleDecl_create_dist = 25, RuleDecl_create_dihed = 26, 
    RuleDecl_function = 27, RuleDecl_target = 28, RuleIns_rst_id = 29, RuleIns_atom_sel = 30, 
    RuleIns_num_sel = 31
  };

  explicit BiosymMRParser(antlr4::TokenStream *input);

  BiosymMRParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~BiosymMRParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Biosym_mrContext;
  class Distance_restraintsContext;
  class Distance_restraintContext;
  class Distance_constraintsContext;
  class Distance_constraintContext;
  class Distance_wo_w_constraintsContext;
  class Distance_wo_w_constraintContext;
  class Dihedral_angle_restraintsContext;
  class Dihedral_angle_restraintContext;
  class Dihedral_angle_constraintsContext;
  class Dihedral_angle_constraintContext;
  class Dihedral_angle_wo_w_constraintsContext;
  class Dihedral_angle_wo_w_constraintContext;
  class Rdc_restraintsContext;
  class Rdc_restraintContext;
  class Chirality_constraintsContext;
  class Chirality_constraintContext;
  class Prochirality_constraintsContext;
  class Prochirality_constraintContext;
  class Mixing_timeContext;
  class NumberContext;
  class Ins_distance_restraintsContext;
  class Ins_distance_restraintContext;
  class Ins_dihedral_angle_restraintsContext;
  class Ins_dihedral_angle_restraintContext;
  class Decl_create_distContext;
  class Decl_create_dihedContext;
  class Decl_functionContext;
  class Decl_targetContext;
  class Ins_rst_idContext;
  class Ins_atom_selContext;
  class Ins_num_selContext; 

  class  Biosym_mrContext : public antlr4::ParserRuleContext {
  public:
    Biosym_mrContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<Distance_restraintsContext *> distance_restraints();
    Distance_restraintsContext* distance_restraints(size_t i);
    std::vector<Distance_constraintsContext *> distance_constraints();
    Distance_constraintsContext* distance_constraints(size_t i);
    std::vector<Distance_wo_w_constraintsContext *> distance_wo_w_constraints();
    Distance_wo_w_constraintsContext* distance_wo_w_constraints(size_t i);
    std::vector<Dihedral_angle_restraintsContext *> dihedral_angle_restraints();
    Dihedral_angle_restraintsContext* dihedral_angle_restraints(size_t i);
    std::vector<Dihedral_angle_constraintsContext *> dihedral_angle_constraints();
    Dihedral_angle_constraintsContext* dihedral_angle_constraints(size_t i);
    std::vector<Dihedral_angle_wo_w_constraintsContext *> dihedral_angle_wo_w_constraints();
    Dihedral_angle_wo_w_constraintsContext* dihedral_angle_wo_w_constraints(size_t i);
    std::vector<Rdc_restraintsContext *> rdc_restraints();
    Rdc_restraintsContext* rdc_restraints(size_t i);
    std::vector<Chirality_constraintsContext *> chirality_constraints();
    Chirality_constraintsContext* chirality_constraints(size_t i);
    std::vector<Prochirality_constraintsContext *> prochirality_constraints();
    Prochirality_constraintsContext* prochirality_constraints(size_t i);
    std::vector<Mixing_timeContext *> mixing_time();
    Mixing_timeContext* mixing_time(size_t i);
    std::vector<Ins_distance_restraintsContext *> ins_distance_restraints();
    Ins_distance_restraintsContext* ins_distance_restraints(size_t i);
    std::vector<Ins_dihedral_angle_restraintsContext *> ins_dihedral_angle_restraints();
    Ins_dihedral_angle_restraintsContext* ins_dihedral_angle_restraints(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Biosym_mrContext* biosym_mr();

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
    std::vector<antlr4::tree::TerminalNode *> Atom_selection();
    antlr4::tree::TerminalNode* Atom_selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    antlr4::tree::TerminalNode *Ordinal();
    std::vector<antlr4::tree::TerminalNode *> Or();
    antlr4::tree::TerminalNode* Or(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_restraintContext* distance_restraint();

  class  Distance_constraintsContext : public antlr4::ParserRuleContext {
  public:
    Distance_constraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Distance_constraintContext *> distance_constraint();
    Distance_constraintContext* distance_constraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_constraintsContext* distance_constraints();

  class  Distance_constraintContext : public antlr4::ParserRuleContext {
  public:
    Distance_constraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Atom_selection();
    antlr4::tree::TerminalNode* Atom_selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    antlr4::tree::TerminalNode *Ordinal();
    std::vector<antlr4::tree::TerminalNode *> Or();
    antlr4::tree::TerminalNode* Or(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_constraintContext* distance_constraint();

  class  Distance_wo_w_constraintsContext : public antlr4::ParserRuleContext {
  public:
    Distance_wo_w_constraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Distance_wo_w_constraintContext *> distance_wo_w_constraint();
    Distance_wo_w_constraintContext* distance_wo_w_constraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_wo_w_constraintsContext* distance_wo_w_constraints();

  class  Distance_wo_w_constraintContext : public antlr4::ParserRuleContext {
  public:
    Distance_wo_w_constraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Atom_selection();
    antlr4::tree::TerminalNode* Atom_selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    antlr4::tree::TerminalNode *Ordinal();
    std::vector<antlr4::tree::TerminalNode *> Or();
    antlr4::tree::TerminalNode* Or(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_wo_w_constraintContext* distance_wo_w_constraint();

  class  Dihedral_angle_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_angle_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Dihedral_angle_restraintContext *> dihedral_angle_restraint();
    Dihedral_angle_restraintContext* dihedral_angle_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_angle_restraintsContext* dihedral_angle_restraints();

  class  Dihedral_angle_restraintContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_angle_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Atom_selection();
    antlr4::tree::TerminalNode* Atom_selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *Ordinal();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_angle_restraintContext* dihedral_angle_restraint();

  class  Dihedral_angle_constraintsContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_angle_constraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Dihedral_angle_constraintContext *> dihedral_angle_constraint();
    Dihedral_angle_constraintContext* dihedral_angle_constraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_angle_constraintsContext* dihedral_angle_constraints();

  class  Dihedral_angle_constraintContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_angle_constraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Atom_selection();
    antlr4::tree::TerminalNode* Atom_selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *Ordinal();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_angle_constraintContext* dihedral_angle_constraint();

  class  Dihedral_angle_wo_w_constraintsContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_angle_wo_w_constraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Dihedral_angle_wo_w_constraintContext *> dihedral_angle_wo_w_constraint();
    Dihedral_angle_wo_w_constraintContext* dihedral_angle_wo_w_constraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_angle_wo_w_constraintsContext* dihedral_angle_wo_w_constraints();

  class  Dihedral_angle_wo_w_constraintContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_angle_wo_w_constraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Atom_selection();
    antlr4::tree::TerminalNode* Atom_selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *Ordinal();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_angle_wo_w_constraintContext* dihedral_angle_wo_w_constraint();

  class  Rdc_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Rdc_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Rdc_restraintContext *> rdc_restraint();
    Rdc_restraintContext* rdc_restraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rdc_restraintsContext* rdc_restraints();

  class  Rdc_restraintContext : public antlr4::ParserRuleContext {
  public:
    Rdc_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Atom_selection();
    antlr4::tree::TerminalNode* Atom_selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *Ordinal();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rdc_restraintContext* rdc_restraint();

  class  Chirality_constraintsContext : public antlr4::ParserRuleContext {
  public:
    Chirality_constraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Chirality_constraintContext *> chirality_constraint();
    Chirality_constraintContext* chirality_constraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Chirality_constraintsContext* chirality_constraints();

  class  Chirality_constraintContext : public antlr4::ParserRuleContext {
  public:
    Chirality_constraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Atom_selection();
    antlr4::tree::TerminalNode *Chiral_code();
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *Ordinal();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Chirality_constraintContext* chirality_constraint();

  class  Prochirality_constraintsContext : public antlr4::ParserRuleContext {
  public:
    Prochirality_constraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Prochirality_constraintContext *> prochirality_constraint();
    Prochirality_constraintContext* prochirality_constraint(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Prochirality_constraintsContext* prochirality_constraints();

  class  Prochirality_constraintContext : public antlr4::ParserRuleContext {
  public:
    Prochirality_constraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Atom_selection();
    antlr4::tree::TerminalNode* Atom_selection(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *Ordinal();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Prochirality_constraintContext* prochirality_constraint();

  class  Mixing_timeContext : public antlr4::ParserRuleContext {
  public:
    Mixing_timeContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Mixing_times();
    antlr4::tree::TerminalNode *RETURN_MT();
    std::vector<antlr4::tree::TerminalNode *> Real_MT();
    antlr4::tree::TerminalNode* Real_MT(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Float_MT();
    antlr4::tree::TerminalNode* Float_MT(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer_MT();
    antlr4::tree::TerminalNode* Integer_MT(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Mixing_timeContext* mixing_time();

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

  class  Ins_distance_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Ins_distance_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Ins_distance_restraintContext *ins_distance_restraint();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ins_distance_restraintsContext* ins_distance_restraints();

  class  Ins_distance_restraintContext : public antlr4::ParserRuleContext {
  public:
    Ins_distance_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Decl_create_distContext *decl_create_dist();
    Decl_functionContext *decl_function();
    Decl_targetContext *decl_target();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ins_distance_restraintContext* ins_distance_restraint();

  class  Ins_dihedral_angle_restraintsContext : public antlr4::ParserRuleContext {
  public:
    Ins_dihedral_angle_restraintsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Ins_dihedral_angle_restraintContext *ins_dihedral_angle_restraint();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ins_dihedral_angle_restraintsContext* ins_dihedral_angle_restraints();

  class  Ins_dihedral_angle_restraintContext : public antlr4::ParserRuleContext {
  public:
    Ins_dihedral_angle_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Decl_create_dihedContext *decl_create_dihed();
    Decl_functionContext *decl_function();
    Decl_targetContext *decl_target();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ins_dihedral_angle_restraintContext* ins_dihedral_angle_restraint();

  class  Decl_create_distContext : public antlr4::ParserRuleContext {
  public:
    Decl_create_distContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Restraint();
    antlr4::tree::TerminalNode *Create();
    Ins_rst_idContext *ins_rst_id();
    antlr4::tree::TerminalNode *Distance();
    std::vector<Ins_atom_selContext *> ins_atom_sel();
    Ins_atom_selContext* ins_atom_sel(size_t i);
    antlr4::tree::TerminalNode *RETURN_II();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Decl_create_distContext* decl_create_dist();

  class  Decl_create_dihedContext : public antlr4::ParserRuleContext {
  public:
    Decl_create_dihedContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Restraint();
    antlr4::tree::TerminalNode *Create();
    Ins_rst_idContext *ins_rst_id();
    antlr4::tree::TerminalNode *Torsion();
    std::vector<Ins_atom_selContext *> ins_atom_sel();
    Ins_atom_selContext* ins_atom_sel(size_t i);
    antlr4::tree::TerminalNode *RETURN_II();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Decl_create_dihedContext* decl_create_dihed();

  class  Decl_functionContext : public antlr4::ParserRuleContext {
  public:
    Decl_functionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Restraint();
    antlr4::tree::TerminalNode *Function();
    Ins_rst_idContext *ins_rst_id();
    antlr4::tree::TerminalNode *RETURN_II();
    std::vector<Ins_num_selContext *> ins_num_sel();
    Ins_num_selContext* ins_num_sel(size_t i);
    antlr4::tree::TerminalNode *Trans();
    antlr4::tree::TerminalNode *Quadratic();
    antlr4::tree::TerminalNode *Flat_bottomed();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Decl_functionContext* decl_function();

  class  Decl_targetContext : public antlr4::ParserRuleContext {
  public:
    Decl_targetContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Restraint();
    antlr4::tree::TerminalNode *Target();
    Ins_rst_idContext *ins_rst_id();
    std::vector<Ins_num_selContext *> ins_num_sel();
    Ins_num_selContext* ins_num_sel(size_t i);
    antlr4::tree::TerminalNode *RETURN_II();
    antlr4::tree::TerminalNode *Relative();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Decl_targetContext* decl_target();

  class  Ins_rst_idContext : public antlr4::ParserRuleContext {
  public:
    Ins_rst_idContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Double_quote_string_II();
    antlr4::tree::TerminalNode *Simple_name_II();
    antlr4::tree::TerminalNode *Integer_II();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ins_rst_idContext* ins_rst_id();

  class  Ins_atom_selContext : public antlr4::ParserRuleContext {
  public:
    Ins_atom_selContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Double_quote_string_II();
    antlr4::tree::TerminalNode *Simple_name_II();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ins_atom_selContext* ins_atom_sel();

  class  Ins_num_selContext : public antlr4::ParserRuleContext {
  public:
    Ins_num_selContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Double_quote_string_II();
    antlr4::tree::TerminalNode *Float_II();
    antlr4::tree::TerminalNode *Integer_II();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ins_num_selContext* ins_num_sel();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

