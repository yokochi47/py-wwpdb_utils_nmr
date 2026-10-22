
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CyanaMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  CyanaMRLexer : public antlr4::Lexer {
public:
  enum {
    Ambig_code = 1, Integer = 2, Float = 3, Float_DecimalComma = 4, Orientation_header = 5, 
    Tensor_header = 6, SMCLN_COMMENT = 7, COMMENT = 8, NoeUpp = 9, NoeLow = 10, 
    SSUpp = 11, SSLow = 12, Jcoupl = 13, Angle = 14, Stereo = 15, Shifts = 16, 
    Type = 17, Equ_op = 18, Or = 19, Ssbond = 20, Ssbond_resids = 21, Hbond = 22, 
    Link = 23, Atom_stereo = 24, Var = 25, Unset = 26, SetVar = 27, Print = 28, 
    Residue = 29, Mapping = 30, Ambig = 31, Capital_integer = 32, Integer_capital = 33, 
    Simple_name = 34, SPACE = 35, ENCLOSE_COMMENT = 36, SECTION_COMMENT = 37, 
    LINE_COMMENT = 38, Any_name = 39, SPACE_CM = 40, RETURN_CM = 41, Atom1 = 42, 
    Atom2 = 43, Residue1 = 44, Residue2 = 45, Equ_op_HB = 46, Integer_HB = 47, 
    Simple_name_HB = 48, SPACE_HB = 49, RETURN_HB = 50, LINE_COMMENT_HB = 51, 
    Double_quote_string = 52, SPACE_PR = 53, RETURN_PR = 54, LINE_COMMENT_PR = 55, 
    Simple_name_VA = 56, SPACE_VA = 57, RETURN_VA = 58, LINE_COMMENT_VA = 59, 
    Ambig_code_MP = 60, Integer_MP = 61, Simple_name_MP = 62, Equ_op_MP = 63, 
    SPACE_MP = 64, RETURN_MP = 65, LINE_COMMENT_MP = 66
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

