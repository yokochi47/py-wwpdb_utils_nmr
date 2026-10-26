
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BiosymMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  BiosymMRParser : public antlr4::Parser {
public:
  enum {
    Integer = 1, Float = 2, Float_DecimalComma = 3, Real = 4, SHARP_COMMENT = 5, 
    EXCLM_COMMENT = 6, SMCLN_COMMENT = 7, Chiral_code = 8, Atom_selection = 9, 
    Ordinal = 10, Restraint = 11, SPACE = 12, ENCLOSE_COMMENT = 13, SECTION_COMMENT = 14, 
    LINE_COMMENT = 15, Double_quote_string = 16, Create = 17, Function = 18, 
    Target = 19, Distance = 20, Quadratic = 21, Flat_bottomed = 22, Relative = 23, 
    SPACE_II = 24, RETURN_II = 25
  };

  enum {
    RuleBiosym_mr = 0, RuleDistance_restraints = 1, RuleDistance_restraint = 2, 
    RuleDistance_constraints = 3, RuleDistance_constraint = 4, RuleDistance_wo_w_constraints = 5, 
    RuleDistance_wo_w_constraint = 6, RuleDihedral_angle_restraints = 7, 
    RuleDihedral_angle_restraint = 8, RuleDihedral_angle_constraints = 9, 
    RuleDihedral_angle_constraint = 10, RuleDihedral_angle_wo_w_constraints = 11, 
    RuleDihedral_angle_wo_w_constraint = 12, RuleChirality_constraints = 13, 
    RuleChirality_constraint = 14, RuleProchirality_constraints = 15, RuleProchirality_constraint = 16, 
    RuleMixing_time = 17, RuleNumber = 18, RuleIns_distance_restraints = 19, 
    RuleIns_distance_restraint = 20, RuleDecl_create = 21, RuleDecl_function = 22, 
    RuleDecl_target = 23
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
  class Chirality_constraintsContext;
  class Chirality_constraintContext;
  class Prochirality_constraintsContext;
  class Prochirality_constraintContext;
  class Mixing_timeContext;
  class NumberContext;
  class Ins_distance_restraintsContext;
  class Ins_distance_restraintContext;
  class Decl_createContext;
  class Decl_functionContext;
  class Decl_targetContext; 

  class  Biosym_mrContext : public antlr4::ParserRuleContext {
  public:
    Biosym_mrContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
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
    std::vector<Chirality_constraintsContext *> chirality_constraints();
    Chirality_constraintsContext* chirality_constraints(size_t i);
    std::vector<Prochirality_constraintsContext *> prochirality_constraints();
    Prochirality_constraintsContext* prochirality_constraints(size_t i);
    std::vector<Mixing_timeContext *> mixing_time();
    Mixing_timeContext* mixing_time(size_t i);
    std::vector<Ins_distance_restraintsContext *> ins_distance_restraints();
    Ins_distance_restraintsContext* ins_distance_restraints(size_t i);


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
    antlr4::tree::TerminalNode *Ordinal();


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
    antlr4::tree::TerminalNode *Ordinal();


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
    antlr4::tree::TerminalNode *Ordinal();


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
    antlr4::tree::TerminalNode *Ordinal();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_angle_wo_w_constraintContext* dihedral_angle_wo_w_constraint();

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
    antlr4::tree::TerminalNode *Ordinal();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Prochirality_constraintContext* prochirality_constraint();

  class  Mixing_timeContext : public antlr4::ParserRuleContext {
  public:
    Mixing_timeContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Real();


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
    Decl_createContext *decl_create();
    Decl_functionContext *decl_function();
    Decl_targetContext *decl_target();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ins_distance_restraintContext* ins_distance_restraint();

  class  Decl_createContext : public antlr4::ParserRuleContext {
  public:
    Decl_createContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Restraint();
    antlr4::tree::TerminalNode *Create();
    std::vector<antlr4::tree::TerminalNode *> Double_quote_string();
    antlr4::tree::TerminalNode* Double_quote_string(size_t i);
    antlr4::tree::TerminalNode *Distance();
    antlr4::tree::TerminalNode *RETURN_II();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Decl_createContext* decl_create();

  class  Decl_functionContext : public antlr4::ParserRuleContext {
  public:
    Decl_functionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Restraint();
    antlr4::tree::TerminalNode *Function();
    std::vector<antlr4::tree::TerminalNode *> Double_quote_string();
    antlr4::tree::TerminalNode* Double_quote_string(size_t i);
    antlr4::tree::TerminalNode *RETURN_II();
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
    std::vector<antlr4::tree::TerminalNode *> Double_quote_string();
    antlr4::tree::TerminalNode* Double_quote_string(size_t i);
    antlr4::tree::TerminalNode *RETURN_II();
    antlr4::tree::TerminalNode *Relative();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Decl_targetContext* decl_target();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

