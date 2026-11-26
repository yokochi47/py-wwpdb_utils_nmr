
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/GarretCSParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  GarretCSParser : public antlr4::Parser {
public:
  enum {
    Integer = 1, Float = 2, SHARP_COMMENT = 3, EXCLM_COMMENT = 4, SMCLN_COMMENT = 5, 
    Simple_name = 6, SPACE = 7, RETURN = 8, SECTION_COMMENT = 9, LINE_COMMENT = 10
  };

  enum {
    RuleGarret_cs = 0, RuleResidue_list = 1, RuleRes_id = 2, RuleShift_list = 3, 
    RuleNumber = 4
  };

  explicit GarretCSParser(antlr4::TokenStream *input);

  GarretCSParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~GarretCSParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Garret_csContext;
  class Residue_listContext;
  class Res_idContext;
  class Shift_listContext;
  class NumberContext; 

  class  Garret_csContext : public antlr4::ParserRuleContext {
  public:
    Garret_csContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<Residue_listContext *> residue_list();
    Residue_listContext* residue_list(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Garret_csContext* garret_cs();

  class  Residue_listContext : public antlr4::ParserRuleContext {
  public:
    Residue_listContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Res_idContext *res_id();
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *RETURN();
    std::vector<Shift_listContext *> shift_list();
    Shift_listContext* shift_list(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Residue_listContext* residue_list();

  class  Res_idContext : public antlr4::ParserRuleContext {
  public:
    Res_idContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Res_idContext* res_id();

  class  Shift_listContext : public antlr4::ParserRuleContext {
  public:
    Shift_listContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Simple_name();
    NumberContext *number();
    antlr4::tree::TerminalNode *RETURN();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Shift_listContext* shift_list();

  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NumberContext* number();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

