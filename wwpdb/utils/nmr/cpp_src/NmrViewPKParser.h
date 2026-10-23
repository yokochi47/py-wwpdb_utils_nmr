
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrViewPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  NmrViewPKParser : public antlr4::Parser {
public:
  enum {
    Label = 1, Integer = 2, Float = 3, Real = 4, SHARP_COMMENT = 5, EXCLM_COMMENT = 6, 
    SMCLN_COMMENT = 7, Simple_name = 8, SPACE = 9, RETURN = 10, L_brace = 11, 
    SECTION_COMMENT = 12, LINE_COMMENT = 13, Dataset = 14, Sw = 15, Sf = 16, 
    Condition = 17, L_name = 18, P_name = 19, W_name = 20, B_name = 21, 
    E_name = 22, J_name = 23, U_name = 24, Vol = 25, Int = 26, Stat = 27, 
    Comment = 28, Flag0 = 29, Simple_name_LA = 30, Float_LA = 31, SPACE_LA = 32, 
    SINGLE_NL_LA = 33, ENCLOSE_DATA_LA = 34, Any_name = 35, SPACE_CM = 36, 
    R_brace = 37
  };

  enum {
    RuleNmrview_pk = 0, RuleData_label = 1, RuleLabels = 2, RulePeak_list_2d = 3, 
    RulePeak_2d = 4, RulePeak_list_3d = 5, RulePeak_3d = 6, RulePeak_list_4d = 7, 
    RulePeak_4d = 8, RulePeak_list_wo_eju_2d = 9, RulePeak_wo_eju_2d = 10, 
    RulePeak_list_wo_eju_3d = 11, RulePeak_wo_eju_3d = 12, RulePeak_list_wo_eju_4d = 13, 
    RulePeak_wo_eju_4d = 14, RuleLabel = 15, RuleJcoupling = 16, RuleNumber = 17, 
    RuleEnclose_data = 18
  };

  explicit NmrViewPKParser(antlr4::TokenStream *input);

  NmrViewPKParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~NmrViewPKParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Nmrview_pkContext;
  class Data_labelContext;
  class LabelsContext;
  class Peak_list_2dContext;
  class Peak_2dContext;
  class Peak_list_3dContext;
  class Peak_3dContext;
  class Peak_list_4dContext;
  class Peak_4dContext;
  class Peak_list_wo_eju_2dContext;
  class Peak_wo_eju_2dContext;
  class Peak_list_wo_eju_3dContext;
  class Peak_wo_eju_3dContext;
  class Peak_list_wo_eju_4dContext;
  class Peak_wo_eju_4dContext;
  class LabelContext;
  class JcouplingContext;
  class NumberContext;
  class Enclose_dataContext; 

  class  Nmrview_pkContext : public antlr4::ParserRuleContext {
  public:
    Nmrview_pkContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<Data_labelContext *> data_label();
    Data_labelContext* data_label(size_t i);
    std::vector<Peak_list_2dContext *> peak_list_2d();
    Peak_list_2dContext* peak_list_2d(size_t i);
    std::vector<Peak_list_3dContext *> peak_list_3d();
    Peak_list_3dContext* peak_list_3d(size_t i);
    std::vector<Peak_list_4dContext *> peak_list_4d();
    Peak_list_4dContext* peak_list_4d(size_t i);
    std::vector<Peak_list_wo_eju_2dContext *> peak_list_wo_eju_2d();
    Peak_list_wo_eju_2dContext* peak_list_wo_eju_2d(size_t i);
    std::vector<Peak_list_wo_eju_3dContext *> peak_list_wo_eju_3d();
    Peak_list_wo_eju_3dContext* peak_list_wo_eju_3d(size_t i);
    std::vector<Peak_list_wo_eju_4dContext *> peak_list_wo_eju_4d();
    Peak_list_wo_eju_4dContext* peak_list_wo_eju_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Nmrview_pkContext* nmrview_pk();

  class  Data_labelContext : public antlr4::ParserRuleContext {
  public:
    Data_labelContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Label();
    antlr4::tree::TerminalNode *Dataset();
    antlr4::tree::TerminalNode *Sw();
    antlr4::tree::TerminalNode *Sf();
    std::vector<LabelsContext *> labels();
    LabelsContext* labels(size_t i);
    antlr4::tree::TerminalNode *Condition();
    std::vector<antlr4::tree::TerminalNode *> SINGLE_NL_LA();
    antlr4::tree::TerminalNode* SINGLE_NL_LA(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LA();
    antlr4::tree::TerminalNode* Simple_name_LA(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Data_labelContext* data_label();

  class  LabelsContext : public antlr4::ParserRuleContext {
  public:
    LabelsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<LabelContext *> label();
    LabelContext* label(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  LabelsContext* labels();

  class  Peak_list_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> L_name();
    antlr4::tree::TerminalNode* L_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> P_name();
    antlr4::tree::TerminalNode* P_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> W_name();
    antlr4::tree::TerminalNode* W_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> B_name();
    antlr4::tree::TerminalNode* B_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> E_name();
    antlr4::tree::TerminalNode* E_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> J_name();
    antlr4::tree::TerminalNode* J_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> U_name();
    antlr4::tree::TerminalNode* U_name(size_t i);
    antlr4::tree::TerminalNode *Vol();
    antlr4::tree::TerminalNode *Int();
    antlr4::tree::TerminalNode *Stat();
    antlr4::tree::TerminalNode *Flag0();
    antlr4::tree::TerminalNode *Comment();
    antlr4::tree::TerminalNode *RETURN();
    std::vector<Peak_2dContext *> peak_2d();
    Peak_2dContext* peak_2d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_2dContext* peak_list_2d();

  class  Peak_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<Enclose_dataContext *> enclose_data();
    Enclose_dataContext* enclose_data(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<JcouplingContext *> jcoupling();
    JcouplingContext* jcoupling(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_2dContext* peak_2d();

  class  Peak_list_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> L_name();
    antlr4::tree::TerminalNode* L_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> P_name();
    antlr4::tree::TerminalNode* P_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> W_name();
    antlr4::tree::TerminalNode* W_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> B_name();
    antlr4::tree::TerminalNode* B_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> E_name();
    antlr4::tree::TerminalNode* E_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> J_name();
    antlr4::tree::TerminalNode* J_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> U_name();
    antlr4::tree::TerminalNode* U_name(size_t i);
    antlr4::tree::TerminalNode *Vol();
    antlr4::tree::TerminalNode *Int();
    antlr4::tree::TerminalNode *Stat();
    antlr4::tree::TerminalNode *Flag0();
    antlr4::tree::TerminalNode *Comment();
    antlr4::tree::TerminalNode *RETURN();
    std::vector<Peak_3dContext *> peak_3d();
    Peak_3dContext* peak_3d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_3dContext* peak_list_3d();

  class  Peak_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<Enclose_dataContext *> enclose_data();
    Enclose_dataContext* enclose_data(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<JcouplingContext *> jcoupling();
    JcouplingContext* jcoupling(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_3dContext* peak_3d();

  class  Peak_list_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> L_name();
    antlr4::tree::TerminalNode* L_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> P_name();
    antlr4::tree::TerminalNode* P_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> W_name();
    antlr4::tree::TerminalNode* W_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> B_name();
    antlr4::tree::TerminalNode* B_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> E_name();
    antlr4::tree::TerminalNode* E_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> J_name();
    antlr4::tree::TerminalNode* J_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> U_name();
    antlr4::tree::TerminalNode* U_name(size_t i);
    antlr4::tree::TerminalNode *Vol();
    antlr4::tree::TerminalNode *Int();
    antlr4::tree::TerminalNode *Stat();
    antlr4::tree::TerminalNode *Flag0();
    antlr4::tree::TerminalNode *Comment();
    antlr4::tree::TerminalNode *RETURN();
    std::vector<Peak_4dContext *> peak_4d();
    Peak_4dContext* peak_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_4dContext* peak_list_4d();

  class  Peak_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<Enclose_dataContext *> enclose_data();
    Enclose_dataContext* enclose_data(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<JcouplingContext *> jcoupling();
    JcouplingContext* jcoupling(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_4dContext* peak_4d();

  class  Peak_list_wo_eju_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_wo_eju_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> L_name();
    antlr4::tree::TerminalNode* L_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> P_name();
    antlr4::tree::TerminalNode* P_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> W_name();
    antlr4::tree::TerminalNode* W_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> B_name();
    antlr4::tree::TerminalNode* B_name(size_t i);
    antlr4::tree::TerminalNode *Vol();
    antlr4::tree::TerminalNode *Int();
    antlr4::tree::TerminalNode *Stat();
    antlr4::tree::TerminalNode *Flag0();
    antlr4::tree::TerminalNode *Comment();
    antlr4::tree::TerminalNode *RETURN();
    std::vector<Peak_wo_eju_2dContext *> peak_wo_eju_2d();
    Peak_wo_eju_2dContext* peak_wo_eju_2d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_wo_eju_2dContext* peak_list_wo_eju_2d();

  class  Peak_wo_eju_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_wo_eju_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<Enclose_dataContext *> enclose_data();
    Enclose_dataContext* enclose_data(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_wo_eju_2dContext* peak_wo_eju_2d();

  class  Peak_list_wo_eju_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_wo_eju_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> L_name();
    antlr4::tree::TerminalNode* L_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> P_name();
    antlr4::tree::TerminalNode* P_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> W_name();
    antlr4::tree::TerminalNode* W_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> B_name();
    antlr4::tree::TerminalNode* B_name(size_t i);
    antlr4::tree::TerminalNode *Vol();
    antlr4::tree::TerminalNode *Int();
    antlr4::tree::TerminalNode *Stat();
    antlr4::tree::TerminalNode *Flag0();
    antlr4::tree::TerminalNode *Comment();
    antlr4::tree::TerminalNode *RETURN();
    std::vector<Peak_wo_eju_3dContext *> peak_wo_eju_3d();
    Peak_wo_eju_3dContext* peak_wo_eju_3d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_wo_eju_3dContext* peak_list_wo_eju_3d();

  class  Peak_wo_eju_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_wo_eju_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<Enclose_dataContext *> enclose_data();
    Enclose_dataContext* enclose_data(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_wo_eju_3dContext* peak_wo_eju_3d();

  class  Peak_list_wo_eju_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_list_wo_eju_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> L_name();
    antlr4::tree::TerminalNode* L_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> P_name();
    antlr4::tree::TerminalNode* P_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> W_name();
    antlr4::tree::TerminalNode* W_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> B_name();
    antlr4::tree::TerminalNode* B_name(size_t i);
    antlr4::tree::TerminalNode *Vol();
    antlr4::tree::TerminalNode *Int();
    antlr4::tree::TerminalNode *Stat();
    antlr4::tree::TerminalNode *Flag0();
    antlr4::tree::TerminalNode *Comment();
    antlr4::tree::TerminalNode *RETURN();
    std::vector<Peak_wo_eju_4dContext *> peak_wo_eju_4d();
    Peak_wo_eju_4dContext* peak_wo_eju_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_list_wo_eju_4dContext* peak_list_wo_eju_4d();

  class  Peak_wo_eju_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_wo_eju_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<Enclose_dataContext *> enclose_data();
    Enclose_dataContext* enclose_data(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_wo_eju_4dContext* peak_wo_eju_4d();

  class  LabelContext : public antlr4::ParserRuleContext {
  public:
    LabelContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float_LA();
    antlr4::tree::TerminalNode *Simple_name_LA();
    antlr4::tree::TerminalNode *ENCLOSE_DATA_LA();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  LabelContext* label();

  class  JcouplingContext : public antlr4::ParserRuleContext {
  public:
    JcouplingContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Simple_name();
    Enclose_dataContext *enclose_data();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  JcouplingContext* jcoupling();

  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NumberContext* number();

  class  Enclose_dataContext : public antlr4::ParserRuleContext {
  public:
    Enclose_dataContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_brace();
    antlr4::tree::TerminalNode *R_brace();
    std::vector<antlr4::tree::TerminalNode *> Any_name();
    antlr4::tree::TerminalNode* Any_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Enclose_dataContext* enclose_data();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

