
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CyanaMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  CyanaMRLexer : public antlr4::Lexer {
public:
  enum {
    Ambig_code = 1, Integer = 2, Float = 3, Float_DecimalComma = 4, Orientation_header = 5, 
    Tensor_header = 6, SMCLN_COMMENT = 7, COMMENT = 8, NoeUpp = 9, NoeLow = 10, 
    SSUpp = 11, SSLow = 12, JCoupl = 13, Angle = 14, Shifts = 15, Type = 16, 
    Equ_op = 17, Or = 18, Ssbond = 19, Ssbond_resids = 20, Hbond = 21, Link = 22, 
    Atom_stereo = 23, Var = 24, Unset = 25, SetVar = 26, Print = 27, Residue = 28, 
    Mapping = 29, Ambig = 30, Capital_integer = 31, Integer_capital = 32, 
    Simple_name = 33, SPACE = 34, ENCLOSE_COMMENT = 35, SECTION_COMMENT = 36, 
    LINE_COMMENT = 37, Any_name = 38, SPACE_CM = 39, RETURN_CM = 40, Atom1 = 41, 
    Atom2 = 42, Residue1 = 43, Residue2 = 44, Equ_op_HB = 45, Integer_HB = 46, 
    Simple_name_HB = 47, SPACE_HB = 48, RETURN_HB = 49, LINE_COMMENT_HB = 50, 
    Double_quote_string = 51, SPACE_PR = 52, RETURN_PR = 53, LINE_COMMENT_PR = 54, 
    Simple_name_VA = 55, SPACE_VA = 56, RETURN_VA = 57, LINE_COMMENT_VA = 58, 
    Ambig_code_MP = 59, Integer_MP = 60, Simple_name_MP = 61, Equ_op_MP = 62, 
    SPACE_MP = 63, RETURN_MP = 64, LINE_COMMENT_MP = 65
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

