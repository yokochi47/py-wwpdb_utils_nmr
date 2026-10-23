
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CyanaMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  CyanaMRLexer : public antlr4::Lexer {
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
    Residue2 = 47, Equ_op_HB = 48, Integer_HB = 49, Simple_name_HB = 50, 
    SPACE_HB = 51, RETURN_HB = 52, LINE_COMMENT_HB = 53, Double_quote_string = 54, 
    SPACE_PR = 55, RETURN_PR = 56, LINE_COMMENT_PR = 57, Simple_name_VA = 58, 
    SPACE_VA = 59, RETURN_VA = 60, LINE_COMMENT_VA = 61, Ambig_code_MP = 62, 
    Integer_MP = 63, Simple_name_MP = 64, Equ_op_MP = 65, SPACE_MP = 66, 
    RETURN_MP = 67, LINE_COMMENT_MP = 68
  };

  enum {
    COMMENT_MODE = 1, HBOND_MODE = 2, PRINT_MODE = 3, VARIABLE_MODE = 4, 
    MAP_MODE = 5
  };

  explicit CyanaMRLexer(antlr4::CharStream *input);

  ~CyanaMRLexer() override;


  std::string getGrammarFileName() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const std::vector<std::string>& getChannelNames() const override;

  const std::vector<std::string>& getModeNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;

  const antlr4::atn::ATN& getATN() const override;

  // By default the static state used to implement the lexer is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:

  // Individual action functions triggered by action() above.

  // Individual semantic predicate functions triggered by sempred() above.

};

