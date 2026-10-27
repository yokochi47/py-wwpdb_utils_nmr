
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SparkyPKParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  SparkyPKParser : public antlr4::Parser {
public:
  enum {
    Assignment = 1, W1 = 2, Integer = 3, Float = 4, Real = 5, Real_vol = 6, 
    SHARP_COMMENT = 7, EXCLM_COMMENT = 8, SMCLN_COMMENT = 9, Assignment_2d_ex = 10, 
    Assignment_3d_ex = 11, Assignment_4d_ex = 12, Note_2d_ex = 13, Note_3d_ex = 14, 
    Note_4d_ex = 15, Note_ex = 16, Simple_name = 17, SPACE = 18, RETURN = 19, 
    ENCLOSE_COMMENT = 20, SECTION_COMMENT = 21, LINE_COMMENT = 22, W1_Hz_LA = 23, 
    W2_Hz_LA = 24, W3_Hz_LA = 25, W4_Hz_LA = 26, Lw1_Hz_LA = 27, Lw2_Hz_LA = 28, 
    Lw3_Hz_LA = 29, Lw4_Hz_LA = 30, W1_LA = 31, W2_LA = 32, W3_LA = 33, 
    W4_LA = 34, Dev_w1_LA = 35, Dev_w2_LA = 36, Dev_w3_LA = 37, Dev_w4_LA = 38, 
    Dummy_H_LA = 39, Height_LA = 40, Volume_LA = 41, Dummy_Rms_LA = 42, 
    S_N_LA = 43, Atom1_LA = 44, Atom2_LA = 45, Atom3_LA = 46, Atom4_LA = 47, 
    Distance_LA = 48, Note_LA = 49, SPACE_LA = 50, RETURN_LA = 51
  };

  enum {
    RuleSparky_pk = 0, RuleData_label = 1, RuleData_label_wo_assign = 2, 
    RulePeak_2d = 3, RulePeak_3d = 4, RulePeak_4d = 5, RulePeak_wo_assign = 6, 
    RuleNumber = 7, RuleNote = 8
  };

  explicit SparkyPKParser(antlr4::TokenStream *input);

  SparkyPKParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~SparkyPKParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Sparky_pkContext;
  class Data_labelContext;
  class Data_label_wo_assignContext;
  class Peak_2dContext;
  class Peak_3dContext;
  class Peak_4dContext;
  class Peak_wo_assignContext;
  class NumberContext;
  class NoteContext; 

  class  Sparky_pkContext : public antlr4::ParserRuleContext {
  public:
    Sparky_pkContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<Data_labelContext *> data_label();
    Data_labelContext* data_label(size_t i);
    std::vector<Data_label_wo_assignContext *> data_label_wo_assign();
    Data_label_wo_assignContext* data_label_wo_assign(size_t i);
    std::vector<Peak_2dContext *> peak_2d();
    Peak_2dContext* peak_2d(size_t i);
    std::vector<Peak_3dContext *> peak_3d();
    Peak_3dContext* peak_3d(size_t i);
    std::vector<Peak_4dContext *> peak_4d();
    Peak_4dContext* peak_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Sparky_pkContext* sparky_pk();

  class  Data_labelContext : public antlr4::ParserRuleContext {
  public:
    Data_labelContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *W1_LA();
    antlr4::tree::TerminalNode *W2_LA();
    antlr4::tree::TerminalNode *RETURN_LA();
    antlr4::tree::TerminalNode *Assignment();
    antlr4::tree::TerminalNode *Assignment_2d_ex();
    antlr4::tree::TerminalNode *Assignment_3d_ex();
    antlr4::tree::TerminalNode *Assignment_4d_ex();
    antlr4::tree::TerminalNode *W3_LA();
    antlr4::tree::TerminalNode *W4_LA();
    antlr4::tree::TerminalNode *W1_Hz_LA();
    antlr4::tree::TerminalNode *W2_Hz_LA();
    antlr4::tree::TerminalNode *W3_Hz_LA();
    antlr4::tree::TerminalNode *W4_Hz_LA();
    antlr4::tree::TerminalNode *Dev_w1_LA();
    antlr4::tree::TerminalNode *Dev_w2_LA();
    antlr4::tree::TerminalNode *Dev_w3_LA();
    antlr4::tree::TerminalNode *Dev_w4_LA();
    antlr4::tree::TerminalNode *Height_LA();
    antlr4::tree::TerminalNode *Volume_LA();
    antlr4::tree::TerminalNode *Dummy_Rms_LA();
    antlr4::tree::TerminalNode *S_N_LA();
    antlr4::tree::TerminalNode *Lw1_Hz_LA();
    antlr4::tree::TerminalNode *Lw2_Hz_LA();
    antlr4::tree::TerminalNode *Lw3_Hz_LA();
    antlr4::tree::TerminalNode *Lw4_Hz_LA();
    antlr4::tree::TerminalNode *Atom1_LA();
    antlr4::tree::TerminalNode *Atom2_LA();
    antlr4::tree::TerminalNode *Atom3_LA();
    antlr4::tree::TerminalNode *Atom4_LA();
    antlr4::tree::TerminalNode *Distance_LA();
    antlr4::tree::TerminalNode *Note_LA();
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *Dummy_H_LA();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Data_labelContext* data_label();

  class  Data_label_wo_assignContext : public antlr4::ParserRuleContext {
  public:
    Data_label_wo_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *W1();
    antlr4::tree::TerminalNode *W2_LA();
    antlr4::tree::TerminalNode *RETURN_LA();
    antlr4::tree::TerminalNode *W3_LA();
    antlr4::tree::TerminalNode *W4_LA();
    antlr4::tree::TerminalNode *W1_Hz_LA();
    antlr4::tree::TerminalNode *W2_Hz_LA();
    antlr4::tree::TerminalNode *W3_Hz_LA();
    antlr4::tree::TerminalNode *W4_Hz_LA();
    antlr4::tree::TerminalNode *Dev_w1_LA();
    antlr4::tree::TerminalNode *Dev_w2_LA();
    antlr4::tree::TerminalNode *Dev_w3_LA();
    antlr4::tree::TerminalNode *Dev_w4_LA();
    antlr4::tree::TerminalNode *Height_LA();
    antlr4::tree::TerminalNode *Volume_LA();
    antlr4::tree::TerminalNode *Dummy_Rms_LA();
    antlr4::tree::TerminalNode *S_N_LA();
    antlr4::tree::TerminalNode *Lw1_Hz_LA();
    antlr4::tree::TerminalNode *Lw2_Hz_LA();
    antlr4::tree::TerminalNode *Lw3_Hz_LA();
    antlr4::tree::TerminalNode *Lw4_Hz_LA();
    antlr4::tree::TerminalNode *Distance_LA();
    antlr4::tree::TerminalNode *Note_LA();
    antlr4::tree::TerminalNode *RETURN();
    std::vector<Peak_wo_assignContext *> peak_wo_assign();
    Peak_wo_assignContext* peak_wo_assign(size_t i);
    antlr4::tree::TerminalNode *Dummy_H_LA();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Data_label_wo_assignContext* data_label_wo_assign();

  class  Peak_2dContext : public antlr4::ParserRuleContext {
  public:
    Peak_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assignment_2d_ex();
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<NoteContext *> note();
    NoteContext* note(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_2dContext* peak_2d();

  class  Peak_3dContext : public antlr4::ParserRuleContext {
  public:
    Peak_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assignment_3d_ex();
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<NoteContext *> note();
    NoteContext* note(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_3dContext* peak_3d();

  class  Peak_4dContext : public antlr4::ParserRuleContext {
  public:
    Peak_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assignment_4d_ex();
    std::vector<antlr4::tree::TerminalNode *> Float();
    antlr4::tree::TerminalNode* Float(size_t i);
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<NoteContext *> note();
    NoteContext* note(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_4dContext* peak_4d();

  class  Peak_wo_assignContext : public antlr4::ParserRuleContext {
  public:
    Peak_wo_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN();
    antlr4::tree::TerminalNode *EOF();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    NoteContext *note();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Peak_wo_assignContext* peak_wo_assign();

  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Real_vol();
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NumberContext* number();

  class  NoteContext : public antlr4::ParserRuleContext {
  public:
    NoteContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Note_2d_ex();
    antlr4::tree::TerminalNode *Note_3d_ex();
    antlr4::tree::TerminalNode *Note_4d_ex();
    antlr4::tree::TerminalNode *Note_ex();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NoteContext* note();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

