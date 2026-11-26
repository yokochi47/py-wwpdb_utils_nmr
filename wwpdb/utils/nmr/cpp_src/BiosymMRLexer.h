
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BiosymMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  BiosymMRLexer : public antlr4::Lexer {
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
    INSIGHT_II_MODE = 1, MIXING_TIME_MODE = 2
  };

  explicit BiosymMRLexer(antlr4::CharStream *input);

  ~BiosymMRLexer() override;


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

