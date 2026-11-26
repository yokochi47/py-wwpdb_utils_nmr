
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BiosymMRParser.g4 by ANTLR 4.13.2


#include "BiosymMRParserVisitor.h"

#include "BiosymMRParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct BiosymMRParserStaticData final {
  BiosymMRParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  BiosymMRParserStaticData(const BiosymMRParserStaticData&) = delete;
  BiosymMRParserStaticData(BiosymMRParserStaticData&&) = delete;
  BiosymMRParserStaticData& operator=(const BiosymMRParserStaticData&) = delete;
  BiosymMRParserStaticData& operator=(BiosymMRParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag biosymmrparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<BiosymMRParserStaticData> biosymmrparserParserStaticData = nullptr;

void biosymmrparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (biosymmrparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(biosymmrparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<BiosymMRParserStaticData>(
    std::vector<std::string>{
      "biosym_mr", "distance_restraints", "distance_restraint", "distance_constraints", 
      "distance_constraint", "distance_wo_w_constraints", "distance_wo_w_constraint", 
      "dihedral_angle_restraints", "dihedral_angle_restraint", "dihedral_angle_constraints", 
      "dihedral_angle_constraint", "dihedral_angle_wo_w_constraints", "dihedral_angle_wo_w_constraint", 
      "rdc_restraints", "rdc_restraint", "chirality_constraints", "chirality_constraint", 
      "prochirality_constraints", "prochirality_constraint", "mixing_time", 
      "number", "ins_distance_restraints", "ins_distance_restraint", "ins_dihedral_angle_restraints", 
      "ins_dihedral_angle_restraint", "decl_create_dist", "decl_create_dihed", 
      "decl_function", "decl_target", "ins_rst_id", "ins_atom_sel", "ins_num_sel"
    },
    std::vector<std::string>{
      "", "", "", "", "", "", "", "", "", "", "", "'+'", "'restraint'", 
      "", "", "", "", "", "", "", "", "'create'", "'function'", "'target'", 
      "'distance'", "'torsion'", "'quadratic'", "'flatBottomed'", "'relative'", 
      "'trans'", "", "", "", "", "", "", "", "", "'and'"
    },
    std::vector<std::string>{
      "", "Integer", "Float", "Float_DecimalComma", "Real", "SHARP_COMMENT", 
      "EXCLM_COMMENT", "SMCLN_COMMENT", "Chiral_code", "Atom_selection", 
      "Ordinal", "Or", "Restraint", "Mixing_times", "SPACE", "RETURN", "ENCLOSE_COMMENT", 
      "SECTION_COMMENT", "LINE_COMMENT", "Integer_II", "Float_II", "Create", 
      "Function", "Target", "Distance", "Torsion", "Quadratic", "Flat_bottomed", 
      "Relative", "Trans", "Simple_name_II", "Double_quote_string_II", "CONTINUE", 
      "SPACE_II", "RETURN_II", "Real_MT", "Float_MT", "Integer_MT", "And_MR", 
      "SPACE_MT", "RETURN_MT"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,40,356,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,
  	28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,3,0,66,8,0,1,0,1,0,1,0,1,0,1,0,1,
  	0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,81,8,0,10,0,12,0,84,9,0,1,0,1,0,1,1,
  	4,1,89,8,1,11,1,12,1,90,1,2,3,2,94,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
  	2,1,2,3,2,105,8,2,1,2,1,2,1,2,1,2,1,2,5,2,112,8,2,10,2,12,2,115,9,2,1,
  	3,4,3,118,8,3,11,3,12,3,119,1,4,3,4,123,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
  	4,1,4,1,4,1,4,1,4,1,4,5,4,137,8,4,10,4,12,4,140,9,4,1,5,4,5,143,8,5,11,
  	5,12,5,144,1,6,3,6,148,8,6,1,6,1,6,1,6,1,6,1,6,3,6,155,8,6,1,6,1,6,1,
  	6,1,6,1,6,5,6,162,8,6,10,6,12,6,165,9,6,1,7,4,7,168,8,7,11,7,12,7,169,
  	1,8,3,8,173,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
  	8,3,8,189,8,8,1,8,1,8,1,8,3,8,194,8,8,1,8,1,8,1,8,3,8,199,8,8,1,8,1,8,
  	1,9,4,9,204,8,9,11,9,12,9,205,1,10,3,10,209,8,10,1,10,1,10,1,10,1,10,
  	1,10,1,10,1,10,1,10,1,10,3,10,220,8,10,1,10,1,10,1,11,4,11,225,8,11,11,
  	11,12,11,226,1,12,3,12,230,8,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
  	12,1,13,4,13,241,8,13,11,13,12,13,242,1,14,3,14,246,8,14,1,14,1,14,1,
  	14,1,14,1,14,1,14,1,14,1,14,1,15,4,15,257,8,15,11,15,12,15,258,1,16,3,
  	16,262,8,16,1,16,1,16,1,16,1,16,1,17,4,17,269,8,17,11,17,12,17,270,1,
  	18,3,18,274,8,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,4,19,285,
  	8,19,11,19,12,19,286,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,22,1,22,
  	1,23,1,23,1,24,1,24,1,24,3,24,304,8,24,1,25,1,25,1,25,1,25,1,25,1,25,
  	1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,
  	1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,333,8,27,1,27,3,27,336,8,27,1,
  	27,1,27,1,28,1,28,1,28,1,28,1,28,3,28,345,8,28,1,28,1,28,1,28,1,29,1,
  	29,1,30,1,30,1,31,1,31,1,31,0,0,32,0,2,4,6,8,10,12,14,16,18,20,22,24,
  	26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,0,6,1,0,35,37,
  	1,0,1,3,1,0,26,27,2,0,19,19,30,31,1,0,30,31,2,0,19,20,31,31,369,0,65,
  	1,0,0,0,2,88,1,0,0,0,4,93,1,0,0,0,6,117,1,0,0,0,8,122,1,0,0,0,10,142,
  	1,0,0,0,12,147,1,0,0,0,14,167,1,0,0,0,16,172,1,0,0,0,18,203,1,0,0,0,20,
  	208,1,0,0,0,22,224,1,0,0,0,24,229,1,0,0,0,26,240,1,0,0,0,28,245,1,0,0,
  	0,30,256,1,0,0,0,32,261,1,0,0,0,34,268,1,0,0,0,36,273,1,0,0,0,38,282,
  	1,0,0,0,40,290,1,0,0,0,42,292,1,0,0,0,44,294,1,0,0,0,46,298,1,0,0,0,48,
  	300,1,0,0,0,50,305,1,0,0,0,52,313,1,0,0,0,54,323,1,0,0,0,56,339,1,0,0,
  	0,58,349,1,0,0,0,60,351,1,0,0,0,62,353,1,0,0,0,64,66,5,15,0,0,65,64,1,
  	0,0,0,65,66,1,0,0,0,66,82,1,0,0,0,67,81,3,2,1,0,68,81,3,6,3,0,69,81,3,
  	10,5,0,70,81,3,14,7,0,71,81,3,18,9,0,72,81,3,22,11,0,73,81,3,26,13,0,
  	74,81,3,30,15,0,75,81,3,34,17,0,76,81,3,38,19,0,77,81,3,42,21,0,78,81,
  	3,46,23,0,79,81,5,15,0,0,80,67,1,0,0,0,80,68,1,0,0,0,80,69,1,0,0,0,80,
  	70,1,0,0,0,80,71,1,0,0,0,80,72,1,0,0,0,80,73,1,0,0,0,80,74,1,0,0,0,80,
  	75,1,0,0,0,80,76,1,0,0,0,80,77,1,0,0,0,80,78,1,0,0,0,80,79,1,0,0,0,81,
  	84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,82,1,0,0,0,85,
  	86,5,0,0,1,86,1,1,0,0,0,87,89,3,4,2,0,88,87,1,0,0,0,89,90,1,0,0,0,90,
  	88,1,0,0,0,90,91,1,0,0,0,91,3,1,0,0,0,92,94,5,10,0,0,93,92,1,0,0,0,93,
  	94,1,0,0,0,94,95,1,0,0,0,95,96,5,9,0,0,96,97,5,9,0,0,97,98,3,40,20,0,
  	98,99,3,40,20,0,99,100,3,40,20,0,100,101,3,40,20,0,101,102,3,40,20,0,
  	102,104,3,40,20,0,103,105,3,40,20,0,104,103,1,0,0,0,104,105,1,0,0,0,105,
  	106,1,0,0,0,106,113,5,15,0,0,107,108,5,11,0,0,108,109,5,9,0,0,109,110,
  	5,9,0,0,110,112,5,15,0,0,111,107,1,0,0,0,112,115,1,0,0,0,113,111,1,0,
  	0,0,113,114,1,0,0,0,114,5,1,0,0,0,115,113,1,0,0,0,116,118,3,8,4,0,117,
  	116,1,0,0,0,118,119,1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,7,1,0,
  	0,0,121,123,5,10,0,0,122,121,1,0,0,0,122,123,1,0,0,0,123,124,1,0,0,0,
  	124,125,5,9,0,0,125,126,5,9,0,0,126,127,3,40,20,0,127,128,3,40,20,0,128,
  	129,3,40,20,0,129,130,3,40,20,0,130,131,3,40,20,0,131,138,5,15,0,0,132,
  	133,5,11,0,0,133,134,5,9,0,0,134,135,5,9,0,0,135,137,5,15,0,0,136,132,
  	1,0,0,0,137,140,1,0,0,0,138,136,1,0,0,0,138,139,1,0,0,0,139,9,1,0,0,0,
  	140,138,1,0,0,0,141,143,3,12,6,0,142,141,1,0,0,0,143,144,1,0,0,0,144,
  	142,1,0,0,0,144,145,1,0,0,0,145,11,1,0,0,0,146,148,5,10,0,0,147,146,1,
  	0,0,0,147,148,1,0,0,0,148,149,1,0,0,0,149,150,5,9,0,0,150,151,5,9,0,0,
  	151,152,3,40,20,0,152,154,3,40,20,0,153,155,3,40,20,0,154,153,1,0,0,0,
  	154,155,1,0,0,0,155,156,1,0,0,0,156,163,5,15,0,0,157,158,5,11,0,0,158,
  	159,5,9,0,0,159,160,5,9,0,0,160,162,5,15,0,0,161,157,1,0,0,0,162,165,
  	1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,13,1,0,0,0,165,163,1,0,0,
  	0,166,168,3,16,8,0,167,166,1,0,0,0,168,169,1,0,0,0,169,167,1,0,0,0,169,
  	170,1,0,0,0,170,15,1,0,0,0,171,173,5,10,0,0,172,171,1,0,0,0,172,173,1,
  	0,0,0,173,174,1,0,0,0,174,175,5,9,0,0,175,176,5,9,0,0,176,177,5,9,0,0,
  	177,178,5,9,0,0,178,179,3,40,20,0,179,180,3,40,20,0,180,181,3,40,20,0,
  	181,182,3,40,20,0,182,183,3,40,20,0,183,184,3,40,20,0,184,188,3,40,20,
  	0,185,186,3,40,20,0,186,187,3,40,20,0,187,189,1,0,0,0,188,185,1,0,0,0,
  	188,189,1,0,0,0,189,193,1,0,0,0,190,191,3,40,20,0,191,192,3,40,20,0,192,
  	194,1,0,0,0,193,190,1,0,0,0,193,194,1,0,0,0,194,198,1,0,0,0,195,196,3,
  	40,20,0,196,197,3,40,20,0,197,199,1,0,0,0,198,195,1,0,0,0,198,199,1,0,
  	0,0,199,200,1,0,0,0,200,201,5,15,0,0,201,17,1,0,0,0,202,204,3,20,10,0,
  	203,202,1,0,0,0,204,205,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,19,
  	1,0,0,0,207,209,5,10,0,0,208,207,1,0,0,0,208,209,1,0,0,0,209,210,1,0,
  	0,0,210,211,5,9,0,0,211,212,5,9,0,0,212,213,5,9,0,0,213,214,5,9,0,0,214,
  	215,3,40,20,0,215,216,3,40,20,0,216,217,3,40,20,0,217,219,3,40,20,0,218,
  	220,3,40,20,0,219,218,1,0,0,0,219,220,1,0,0,0,220,221,1,0,0,0,221,222,
  	5,15,0,0,222,21,1,0,0,0,223,225,3,24,12,0,224,223,1,0,0,0,225,226,1,0,
  	0,0,226,224,1,0,0,0,226,227,1,0,0,0,227,23,1,0,0,0,228,230,5,10,0,0,229,
  	228,1,0,0,0,229,230,1,0,0,0,230,231,1,0,0,0,231,232,5,9,0,0,232,233,5,
  	9,0,0,233,234,5,9,0,0,234,235,5,9,0,0,235,236,3,40,20,0,236,237,3,40,
  	20,0,237,238,5,15,0,0,238,25,1,0,0,0,239,241,3,28,14,0,240,239,1,0,0,
  	0,241,242,1,0,0,0,242,240,1,0,0,0,242,243,1,0,0,0,243,27,1,0,0,0,244,
  	246,5,10,0,0,245,244,1,0,0,0,245,246,1,0,0,0,246,247,1,0,0,0,247,248,
  	5,9,0,0,248,249,5,9,0,0,249,250,3,40,20,0,250,251,3,40,20,0,251,252,3,
  	40,20,0,252,253,3,40,20,0,253,254,5,15,0,0,254,29,1,0,0,0,255,257,3,32,
  	16,0,256,255,1,0,0,0,257,258,1,0,0,0,258,256,1,0,0,0,258,259,1,0,0,0,
  	259,31,1,0,0,0,260,262,5,10,0,0,261,260,1,0,0,0,261,262,1,0,0,0,262,263,
  	1,0,0,0,263,264,5,9,0,0,264,265,5,8,0,0,265,266,5,15,0,0,266,33,1,0,0,
  	0,267,269,3,36,18,0,268,267,1,0,0,0,269,270,1,0,0,0,270,268,1,0,0,0,270,
  	271,1,0,0,0,271,35,1,0,0,0,272,274,5,10,0,0,273,272,1,0,0,0,273,274,1,
  	0,0,0,274,275,1,0,0,0,275,276,5,9,0,0,276,277,5,9,0,0,277,278,5,9,0,0,
  	278,279,5,9,0,0,279,280,5,9,0,0,280,281,5,15,0,0,281,37,1,0,0,0,282,284,
  	5,13,0,0,283,285,7,0,0,0,284,283,1,0,0,0,285,286,1,0,0,0,286,284,1,0,
  	0,0,286,287,1,0,0,0,287,288,1,0,0,0,288,289,5,40,0,0,289,39,1,0,0,0,290,
  	291,7,1,0,0,291,41,1,0,0,0,292,293,3,44,22,0,293,43,1,0,0,0,294,295,3,
  	50,25,0,295,296,3,54,27,0,296,297,3,56,28,0,297,45,1,0,0,0,298,299,3,
  	48,24,0,299,47,1,0,0,0,300,301,3,52,26,0,301,303,3,54,27,0,302,304,3,
  	56,28,0,303,302,1,0,0,0,303,304,1,0,0,0,304,49,1,0,0,0,305,306,5,12,0,
  	0,306,307,5,21,0,0,307,308,3,58,29,0,308,309,5,24,0,0,309,310,3,60,30,
  	0,310,311,3,60,30,0,311,312,5,34,0,0,312,51,1,0,0,0,313,314,5,12,0,0,
  	314,315,5,21,0,0,315,316,3,58,29,0,316,317,5,25,0,0,317,318,3,60,30,0,
  	318,319,3,60,30,0,319,320,3,60,30,0,320,321,3,60,30,0,321,322,5,34,0,
  	0,322,53,1,0,0,0,323,324,5,12,0,0,324,325,5,22,0,0,325,332,3,58,29,0,
  	326,327,7,2,0,0,327,328,3,62,31,0,328,329,3,62,31,0,329,333,1,0,0,0,330,
  	331,5,29,0,0,331,333,3,62,31,0,332,326,1,0,0,0,332,330,1,0,0,0,333,335,
  	1,0,0,0,334,336,3,62,31,0,335,334,1,0,0,0,335,336,1,0,0,0,336,337,1,0,
  	0,0,337,338,5,34,0,0,338,55,1,0,0,0,339,340,5,12,0,0,340,341,5,23,0,0,
  	341,344,3,58,29,0,342,345,3,62,31,0,343,345,5,28,0,0,344,342,1,0,0,0,
  	344,343,1,0,0,0,345,346,1,0,0,0,346,347,3,62,31,0,347,348,5,34,0,0,348,
  	57,1,0,0,0,349,350,7,3,0,0,350,59,1,0,0,0,351,352,7,4,0,0,352,61,1,0,
  	0,0,353,354,7,5,0,0,354,63,1,0,0,0,35,65,80,82,90,93,104,113,119,122,
  	138,144,147,154,163,169,172,188,193,198,205,208,219,226,229,242,245,258,
  	261,270,273,286,303,332,335,344
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  biosymmrparserParserStaticData = std::move(staticData);
}

}

BiosymMRParser::BiosymMRParser(TokenStream *input) : BiosymMRParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

BiosymMRParser::BiosymMRParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  BiosymMRParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *biosymmrparserParserStaticData->atn, biosymmrparserParserStaticData->decisionToDFA, biosymmrparserParserStaticData->sharedContextCache, options);
}

BiosymMRParser::~BiosymMRParser() {
  delete _interpreter;
}

const atn::ATN& BiosymMRParser::getATN() const {
  return *biosymmrparserParserStaticData->atn;
}

std::string BiosymMRParser::getGrammarFileName() const {
  return "BiosymMRParser.g4";
}

const std::vector<std::string>& BiosymMRParser::getRuleNames() const {
  return biosymmrparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& BiosymMRParser::getVocabulary() const {
  return biosymmrparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView BiosymMRParser::getSerializedATN() const {
  return biosymmrparserParserStaticData->serializedATN;
}


//----------------- Biosym_mrContext ------------------------------------------------------------------

BiosymMRParser::Biosym_mrContext::Biosym_mrContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BiosymMRParser::Biosym_mrContext::EOF() {
  return getToken(BiosymMRParser::EOF, 0);
}

std::vector<tree::TerminalNode *> BiosymMRParser::Biosym_mrContext::RETURN() {
  return getTokens(BiosymMRParser::RETURN);
}

tree::TerminalNode* BiosymMRParser::Biosym_mrContext::RETURN(size_t i) {
  return getToken(BiosymMRParser::RETURN, i);
}

std::vector<BiosymMRParser::Distance_restraintsContext *> BiosymMRParser::Biosym_mrContext::distance_restraints() {
  return getRuleContexts<BiosymMRParser::Distance_restraintsContext>();
}

BiosymMRParser::Distance_restraintsContext* BiosymMRParser::Biosym_mrContext::distance_restraints(size_t i) {
  return getRuleContext<BiosymMRParser::Distance_restraintsContext>(i);
}

std::vector<BiosymMRParser::Distance_constraintsContext *> BiosymMRParser::Biosym_mrContext::distance_constraints() {
  return getRuleContexts<BiosymMRParser::Distance_constraintsContext>();
}

BiosymMRParser::Distance_constraintsContext* BiosymMRParser::Biosym_mrContext::distance_constraints(size_t i) {
  return getRuleContext<BiosymMRParser::Distance_constraintsContext>(i);
}

std::vector<BiosymMRParser::Distance_wo_w_constraintsContext *> BiosymMRParser::Biosym_mrContext::distance_wo_w_constraints() {
  return getRuleContexts<BiosymMRParser::Distance_wo_w_constraintsContext>();
}

BiosymMRParser::Distance_wo_w_constraintsContext* BiosymMRParser::Biosym_mrContext::distance_wo_w_constraints(size_t i) {
  return getRuleContext<BiosymMRParser::Distance_wo_w_constraintsContext>(i);
}

std::vector<BiosymMRParser::Dihedral_angle_restraintsContext *> BiosymMRParser::Biosym_mrContext::dihedral_angle_restraints() {
  return getRuleContexts<BiosymMRParser::Dihedral_angle_restraintsContext>();
}

BiosymMRParser::Dihedral_angle_restraintsContext* BiosymMRParser::Biosym_mrContext::dihedral_angle_restraints(size_t i) {
  return getRuleContext<BiosymMRParser::Dihedral_angle_restraintsContext>(i);
}

std::vector<BiosymMRParser::Dihedral_angle_constraintsContext *> BiosymMRParser::Biosym_mrContext::dihedral_angle_constraints() {
  return getRuleContexts<BiosymMRParser::Dihedral_angle_constraintsContext>();
}

BiosymMRParser::Dihedral_angle_constraintsContext* BiosymMRParser::Biosym_mrContext::dihedral_angle_constraints(size_t i) {
  return getRuleContext<BiosymMRParser::Dihedral_angle_constraintsContext>(i);
}

std::vector<BiosymMRParser::Dihedral_angle_wo_w_constraintsContext *> BiosymMRParser::Biosym_mrContext::dihedral_angle_wo_w_constraints() {
  return getRuleContexts<BiosymMRParser::Dihedral_angle_wo_w_constraintsContext>();
}

BiosymMRParser::Dihedral_angle_wo_w_constraintsContext* BiosymMRParser::Biosym_mrContext::dihedral_angle_wo_w_constraints(size_t i) {
  return getRuleContext<BiosymMRParser::Dihedral_angle_wo_w_constraintsContext>(i);
}

std::vector<BiosymMRParser::Rdc_restraintsContext *> BiosymMRParser::Biosym_mrContext::rdc_restraints() {
  return getRuleContexts<BiosymMRParser::Rdc_restraintsContext>();
}

BiosymMRParser::Rdc_restraintsContext* BiosymMRParser::Biosym_mrContext::rdc_restraints(size_t i) {
  return getRuleContext<BiosymMRParser::Rdc_restraintsContext>(i);
}

std::vector<BiosymMRParser::Chirality_constraintsContext *> BiosymMRParser::Biosym_mrContext::chirality_constraints() {
  return getRuleContexts<BiosymMRParser::Chirality_constraintsContext>();
}

BiosymMRParser::Chirality_constraintsContext* BiosymMRParser::Biosym_mrContext::chirality_constraints(size_t i) {
  return getRuleContext<BiosymMRParser::Chirality_constraintsContext>(i);
}

std::vector<BiosymMRParser::Prochirality_constraintsContext *> BiosymMRParser::Biosym_mrContext::prochirality_constraints() {
  return getRuleContexts<BiosymMRParser::Prochirality_constraintsContext>();
}

BiosymMRParser::Prochirality_constraintsContext* BiosymMRParser::Biosym_mrContext::prochirality_constraints(size_t i) {
  return getRuleContext<BiosymMRParser::Prochirality_constraintsContext>(i);
}

std::vector<BiosymMRParser::Mixing_timeContext *> BiosymMRParser::Biosym_mrContext::mixing_time() {
  return getRuleContexts<BiosymMRParser::Mixing_timeContext>();
}

BiosymMRParser::Mixing_timeContext* BiosymMRParser::Biosym_mrContext::mixing_time(size_t i) {
  return getRuleContext<BiosymMRParser::Mixing_timeContext>(i);
}

std::vector<BiosymMRParser::Ins_distance_restraintsContext *> BiosymMRParser::Biosym_mrContext::ins_distance_restraints() {
  return getRuleContexts<BiosymMRParser::Ins_distance_restraintsContext>();
}

BiosymMRParser::Ins_distance_restraintsContext* BiosymMRParser::Biosym_mrContext::ins_distance_restraints(size_t i) {
  return getRuleContext<BiosymMRParser::Ins_distance_restraintsContext>(i);
}

std::vector<BiosymMRParser::Ins_dihedral_angle_restraintsContext *> BiosymMRParser::Biosym_mrContext::ins_dihedral_angle_restraints() {
  return getRuleContexts<BiosymMRParser::Ins_dihedral_angle_restraintsContext>();
}

BiosymMRParser::Ins_dihedral_angle_restraintsContext* BiosymMRParser::Biosym_mrContext::ins_dihedral_angle_restraints(size_t i) {
  return getRuleContext<BiosymMRParser::Ins_dihedral_angle_restraintsContext>(i);
}


size_t BiosymMRParser::Biosym_mrContext::getRuleIndex() const {
  return BiosymMRParser::RuleBiosym_mr;
}


std::any BiosymMRParser::Biosym_mrContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitBiosym_mr(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Biosym_mrContext* BiosymMRParser::biosym_mr() {
  Biosym_mrContext *_localctx = _tracker.createInstance<Biosym_mrContext>(_ctx, getState());
  enterRule(_localctx, 0, BiosymMRParser::RuleBiosym_mr);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(65);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
    case 1: {
      setState(64);
      match(BiosymMRParser::RETURN);
      break;
    }

    default:
      break;
    }
    setState(82);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 46592) != 0)) {
      setState(80);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx)) {
      case 1: {
        setState(67);
        distance_restraints();
        break;
      }

      case 2: {
        setState(68);
        distance_constraints();
        break;
      }

      case 3: {
        setState(69);
        distance_wo_w_constraints();
        break;
      }

      case 4: {
        setState(70);
        dihedral_angle_restraints();
        break;
      }

      case 5: {
        setState(71);
        dihedral_angle_constraints();
        break;
      }

      case 6: {
        setState(72);
        dihedral_angle_wo_w_constraints();
        break;
      }

      case 7: {
        setState(73);
        rdc_restraints();
        break;
      }

      case 8: {
        setState(74);
        chirality_constraints();
        break;
      }

      case 9: {
        setState(75);
        prochirality_constraints();
        break;
      }

      case 10: {
        setState(76);
        mixing_time();
        break;
      }

      case 11: {
        setState(77);
        ins_distance_restraints();
        break;
      }

      case 12: {
        setState(78);
        ins_dihedral_angle_restraints();
        break;
      }

      case 13: {
        setState(79);
        match(BiosymMRParser::RETURN);
        break;
      }

      default:
        break;
      }
      setState(84);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(85);
    match(BiosymMRParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_restraintsContext ------------------------------------------------------------------

BiosymMRParser::Distance_restraintsContext::Distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BiosymMRParser::Distance_restraintContext *> BiosymMRParser::Distance_restraintsContext::distance_restraint() {
  return getRuleContexts<BiosymMRParser::Distance_restraintContext>();
}

BiosymMRParser::Distance_restraintContext* BiosymMRParser::Distance_restraintsContext::distance_restraint(size_t i) {
  return getRuleContext<BiosymMRParser::Distance_restraintContext>(i);
}


size_t BiosymMRParser::Distance_restraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleDistance_restraints;
}


std::any BiosymMRParser::Distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_restraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Distance_restraintsContext* BiosymMRParser::distance_restraints() {
  Distance_restraintsContext *_localctx = _tracker.createInstance<Distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 2, BiosymMRParser::RuleDistance_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(88); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(87);
              distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(90); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 3, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_restraintContext ------------------------------------------------------------------

BiosymMRParser::Distance_restraintContext::Distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BiosymMRParser::Distance_restraintContext::Atom_selection() {
  return getTokens(BiosymMRParser::Atom_selection);
}

tree::TerminalNode* BiosymMRParser::Distance_restraintContext::Atom_selection(size_t i) {
  return getToken(BiosymMRParser::Atom_selection, i);
}

std::vector<BiosymMRParser::NumberContext *> BiosymMRParser::Distance_restraintContext::number() {
  return getRuleContexts<BiosymMRParser::NumberContext>();
}

BiosymMRParser::NumberContext* BiosymMRParser::Distance_restraintContext::number(size_t i) {
  return getRuleContext<BiosymMRParser::NumberContext>(i);
}

std::vector<tree::TerminalNode *> BiosymMRParser::Distance_restraintContext::RETURN() {
  return getTokens(BiosymMRParser::RETURN);
}

tree::TerminalNode* BiosymMRParser::Distance_restraintContext::RETURN(size_t i) {
  return getToken(BiosymMRParser::RETURN, i);
}

tree::TerminalNode* BiosymMRParser::Distance_restraintContext::Ordinal() {
  return getToken(BiosymMRParser::Ordinal, 0);
}

std::vector<tree::TerminalNode *> BiosymMRParser::Distance_restraintContext::Or() {
  return getTokens(BiosymMRParser::Or);
}

tree::TerminalNode* BiosymMRParser::Distance_restraintContext::Or(size_t i) {
  return getToken(BiosymMRParser::Or, i);
}


size_t BiosymMRParser::Distance_restraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleDistance_restraint;
}


std::any BiosymMRParser::Distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_restraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Distance_restraintContext* BiosymMRParser::distance_restraint() {
  Distance_restraintContext *_localctx = _tracker.createInstance<Distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 4, BiosymMRParser::RuleDistance_restraint);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(93);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(92);
      match(BiosymMRParser::Ordinal);
    }
    setState(95);
    match(BiosymMRParser::Atom_selection);
    setState(96);
    match(BiosymMRParser::Atom_selection);
    setState(97);
    number();
    setState(98);
    number();
    setState(99);
    number();
    setState(100);
    number();
    setState(101);
    number();
    setState(102);
    number();
    setState(104);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 14) != 0)) {
      setState(103);
      number();
    }
    setState(106);
    match(BiosymMRParser::RETURN);
    setState(113);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BiosymMRParser::Or) {
      setState(107);
      match(BiosymMRParser::Or);
      setState(108);
      match(BiosymMRParser::Atom_selection);
      setState(109);
      match(BiosymMRParser::Atom_selection);
      setState(110);
      match(BiosymMRParser::RETURN);
      setState(115);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_constraintsContext ------------------------------------------------------------------

BiosymMRParser::Distance_constraintsContext::Distance_constraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BiosymMRParser::Distance_constraintContext *> BiosymMRParser::Distance_constraintsContext::distance_constraint() {
  return getRuleContexts<BiosymMRParser::Distance_constraintContext>();
}

BiosymMRParser::Distance_constraintContext* BiosymMRParser::Distance_constraintsContext::distance_constraint(size_t i) {
  return getRuleContext<BiosymMRParser::Distance_constraintContext>(i);
}


size_t BiosymMRParser::Distance_constraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleDistance_constraints;
}


std::any BiosymMRParser::Distance_constraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_constraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Distance_constraintsContext* BiosymMRParser::distance_constraints() {
  Distance_constraintsContext *_localctx = _tracker.createInstance<Distance_constraintsContext>(_ctx, getState());
  enterRule(_localctx, 6, BiosymMRParser::RuleDistance_constraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(117); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(116);
              distance_constraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(119); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 7, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_constraintContext ------------------------------------------------------------------

BiosymMRParser::Distance_constraintContext::Distance_constraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BiosymMRParser::Distance_constraintContext::Atom_selection() {
  return getTokens(BiosymMRParser::Atom_selection);
}

tree::TerminalNode* BiosymMRParser::Distance_constraintContext::Atom_selection(size_t i) {
  return getToken(BiosymMRParser::Atom_selection, i);
}

std::vector<BiosymMRParser::NumberContext *> BiosymMRParser::Distance_constraintContext::number() {
  return getRuleContexts<BiosymMRParser::NumberContext>();
}

BiosymMRParser::NumberContext* BiosymMRParser::Distance_constraintContext::number(size_t i) {
  return getRuleContext<BiosymMRParser::NumberContext>(i);
}

std::vector<tree::TerminalNode *> BiosymMRParser::Distance_constraintContext::RETURN() {
  return getTokens(BiosymMRParser::RETURN);
}

tree::TerminalNode* BiosymMRParser::Distance_constraintContext::RETURN(size_t i) {
  return getToken(BiosymMRParser::RETURN, i);
}

tree::TerminalNode* BiosymMRParser::Distance_constraintContext::Ordinal() {
  return getToken(BiosymMRParser::Ordinal, 0);
}

std::vector<tree::TerminalNode *> BiosymMRParser::Distance_constraintContext::Or() {
  return getTokens(BiosymMRParser::Or);
}

tree::TerminalNode* BiosymMRParser::Distance_constraintContext::Or(size_t i) {
  return getToken(BiosymMRParser::Or, i);
}


size_t BiosymMRParser::Distance_constraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleDistance_constraint;
}


std::any BiosymMRParser::Distance_constraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_constraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Distance_constraintContext* BiosymMRParser::distance_constraint() {
  Distance_constraintContext *_localctx = _tracker.createInstance<Distance_constraintContext>(_ctx, getState());
  enterRule(_localctx, 8, BiosymMRParser::RuleDistance_constraint);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(122);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(121);
      match(BiosymMRParser::Ordinal);
    }
    setState(124);
    match(BiosymMRParser::Atom_selection);
    setState(125);
    match(BiosymMRParser::Atom_selection);
    setState(126);
    number();
    setState(127);
    number();
    setState(128);
    number();
    setState(129);
    number();
    setState(130);
    number();
    setState(131);
    match(BiosymMRParser::RETURN);
    setState(138);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BiosymMRParser::Or) {
      setState(132);
      match(BiosymMRParser::Or);
      setState(133);
      match(BiosymMRParser::Atom_selection);
      setState(134);
      match(BiosymMRParser::Atom_selection);
      setState(135);
      match(BiosymMRParser::RETURN);
      setState(140);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_wo_w_constraintsContext ------------------------------------------------------------------

BiosymMRParser::Distance_wo_w_constraintsContext::Distance_wo_w_constraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BiosymMRParser::Distance_wo_w_constraintContext *> BiosymMRParser::Distance_wo_w_constraintsContext::distance_wo_w_constraint() {
  return getRuleContexts<BiosymMRParser::Distance_wo_w_constraintContext>();
}

BiosymMRParser::Distance_wo_w_constraintContext* BiosymMRParser::Distance_wo_w_constraintsContext::distance_wo_w_constraint(size_t i) {
  return getRuleContext<BiosymMRParser::Distance_wo_w_constraintContext>(i);
}


size_t BiosymMRParser::Distance_wo_w_constraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleDistance_wo_w_constraints;
}


std::any BiosymMRParser::Distance_wo_w_constraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_wo_w_constraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Distance_wo_w_constraintsContext* BiosymMRParser::distance_wo_w_constraints() {
  Distance_wo_w_constraintsContext *_localctx = _tracker.createInstance<Distance_wo_w_constraintsContext>(_ctx, getState());
  enterRule(_localctx, 10, BiosymMRParser::RuleDistance_wo_w_constraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(142); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(141);
              distance_wo_w_constraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(144); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 10, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_wo_w_constraintContext ------------------------------------------------------------------

BiosymMRParser::Distance_wo_w_constraintContext::Distance_wo_w_constraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BiosymMRParser::Distance_wo_w_constraintContext::Atom_selection() {
  return getTokens(BiosymMRParser::Atom_selection);
}

tree::TerminalNode* BiosymMRParser::Distance_wo_w_constraintContext::Atom_selection(size_t i) {
  return getToken(BiosymMRParser::Atom_selection, i);
}

std::vector<BiosymMRParser::NumberContext *> BiosymMRParser::Distance_wo_w_constraintContext::number() {
  return getRuleContexts<BiosymMRParser::NumberContext>();
}

BiosymMRParser::NumberContext* BiosymMRParser::Distance_wo_w_constraintContext::number(size_t i) {
  return getRuleContext<BiosymMRParser::NumberContext>(i);
}

std::vector<tree::TerminalNode *> BiosymMRParser::Distance_wo_w_constraintContext::RETURN() {
  return getTokens(BiosymMRParser::RETURN);
}

tree::TerminalNode* BiosymMRParser::Distance_wo_w_constraintContext::RETURN(size_t i) {
  return getToken(BiosymMRParser::RETURN, i);
}

tree::TerminalNode* BiosymMRParser::Distance_wo_w_constraintContext::Ordinal() {
  return getToken(BiosymMRParser::Ordinal, 0);
}

std::vector<tree::TerminalNode *> BiosymMRParser::Distance_wo_w_constraintContext::Or() {
  return getTokens(BiosymMRParser::Or);
}

tree::TerminalNode* BiosymMRParser::Distance_wo_w_constraintContext::Or(size_t i) {
  return getToken(BiosymMRParser::Or, i);
}


size_t BiosymMRParser::Distance_wo_w_constraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleDistance_wo_w_constraint;
}


std::any BiosymMRParser::Distance_wo_w_constraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_wo_w_constraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Distance_wo_w_constraintContext* BiosymMRParser::distance_wo_w_constraint() {
  Distance_wo_w_constraintContext *_localctx = _tracker.createInstance<Distance_wo_w_constraintContext>(_ctx, getState());
  enterRule(_localctx, 12, BiosymMRParser::RuleDistance_wo_w_constraint);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(147);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(146);
      match(BiosymMRParser::Ordinal);
    }
    setState(149);
    match(BiosymMRParser::Atom_selection);
    setState(150);
    match(BiosymMRParser::Atom_selection);
    setState(151);
    number();
    setState(152);
    number();
    setState(154);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 14) != 0)) {
      setState(153);
      number();
    }
    setState(156);
    match(BiosymMRParser::RETURN);
    setState(163);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BiosymMRParser::Or) {
      setState(157);
      match(BiosymMRParser::Or);
      setState(158);
      match(BiosymMRParser::Atom_selection);
      setState(159);
      match(BiosymMRParser::Atom_selection);
      setState(160);
      match(BiosymMRParser::RETURN);
      setState(165);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_angle_restraintsContext ------------------------------------------------------------------

BiosymMRParser::Dihedral_angle_restraintsContext::Dihedral_angle_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BiosymMRParser::Dihedral_angle_restraintContext *> BiosymMRParser::Dihedral_angle_restraintsContext::dihedral_angle_restraint() {
  return getRuleContexts<BiosymMRParser::Dihedral_angle_restraintContext>();
}

BiosymMRParser::Dihedral_angle_restraintContext* BiosymMRParser::Dihedral_angle_restraintsContext::dihedral_angle_restraint(size_t i) {
  return getRuleContext<BiosymMRParser::Dihedral_angle_restraintContext>(i);
}


size_t BiosymMRParser::Dihedral_angle_restraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleDihedral_angle_restraints;
}


std::any BiosymMRParser::Dihedral_angle_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_angle_restraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Dihedral_angle_restraintsContext* BiosymMRParser::dihedral_angle_restraints() {
  Dihedral_angle_restraintsContext *_localctx = _tracker.createInstance<Dihedral_angle_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 14, BiosymMRParser::RuleDihedral_angle_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(167); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(166);
              dihedral_angle_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(169); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 14, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_angle_restraintContext ------------------------------------------------------------------

BiosymMRParser::Dihedral_angle_restraintContext::Dihedral_angle_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BiosymMRParser::Dihedral_angle_restraintContext::Atom_selection() {
  return getTokens(BiosymMRParser::Atom_selection);
}

tree::TerminalNode* BiosymMRParser::Dihedral_angle_restraintContext::Atom_selection(size_t i) {
  return getToken(BiosymMRParser::Atom_selection, i);
}

std::vector<BiosymMRParser::NumberContext *> BiosymMRParser::Dihedral_angle_restraintContext::number() {
  return getRuleContexts<BiosymMRParser::NumberContext>();
}

BiosymMRParser::NumberContext* BiosymMRParser::Dihedral_angle_restraintContext::number(size_t i) {
  return getRuleContext<BiosymMRParser::NumberContext>(i);
}

tree::TerminalNode* BiosymMRParser::Dihedral_angle_restraintContext::RETURN() {
  return getToken(BiosymMRParser::RETURN, 0);
}

tree::TerminalNode* BiosymMRParser::Dihedral_angle_restraintContext::Ordinal() {
  return getToken(BiosymMRParser::Ordinal, 0);
}


size_t BiosymMRParser::Dihedral_angle_restraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleDihedral_angle_restraint;
}


std::any BiosymMRParser::Dihedral_angle_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_angle_restraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Dihedral_angle_restraintContext* BiosymMRParser::dihedral_angle_restraint() {
  Dihedral_angle_restraintContext *_localctx = _tracker.createInstance<Dihedral_angle_restraintContext>(_ctx, getState());
  enterRule(_localctx, 16, BiosymMRParser::RuleDihedral_angle_restraint);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(172);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(171);
      match(BiosymMRParser::Ordinal);
    }
    setState(174);
    match(BiosymMRParser::Atom_selection);
    setState(175);
    match(BiosymMRParser::Atom_selection);
    setState(176);
    match(BiosymMRParser::Atom_selection);
    setState(177);
    match(BiosymMRParser::Atom_selection);
    setState(178);
    number();
    setState(179);
    number();
    setState(180);
    number();
    setState(181);
    number();
    setState(182);
    number();
    setState(183);
    number();
    setState(184);
    number();
    setState(188);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 16, _ctx)) {
    case 1: {
      setState(185);
      number();
      setState(186);
      number();
      break;
    }

    default:
      break;
    }
    setState(193);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 17, _ctx)) {
    case 1: {
      setState(190);
      number();
      setState(191);
      number();
      break;
    }

    default:
      break;
    }
    setState(198);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 14) != 0)) {
      setState(195);
      number();
      setState(196);
      number();
    }
    setState(200);
    match(BiosymMRParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_angle_constraintsContext ------------------------------------------------------------------

BiosymMRParser::Dihedral_angle_constraintsContext::Dihedral_angle_constraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BiosymMRParser::Dihedral_angle_constraintContext *> BiosymMRParser::Dihedral_angle_constraintsContext::dihedral_angle_constraint() {
  return getRuleContexts<BiosymMRParser::Dihedral_angle_constraintContext>();
}

BiosymMRParser::Dihedral_angle_constraintContext* BiosymMRParser::Dihedral_angle_constraintsContext::dihedral_angle_constraint(size_t i) {
  return getRuleContext<BiosymMRParser::Dihedral_angle_constraintContext>(i);
}


size_t BiosymMRParser::Dihedral_angle_constraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleDihedral_angle_constraints;
}


std::any BiosymMRParser::Dihedral_angle_constraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_angle_constraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Dihedral_angle_constraintsContext* BiosymMRParser::dihedral_angle_constraints() {
  Dihedral_angle_constraintsContext *_localctx = _tracker.createInstance<Dihedral_angle_constraintsContext>(_ctx, getState());
  enterRule(_localctx, 18, BiosymMRParser::RuleDihedral_angle_constraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(203); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(202);
              dihedral_angle_constraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(205); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 19, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_angle_constraintContext ------------------------------------------------------------------

BiosymMRParser::Dihedral_angle_constraintContext::Dihedral_angle_constraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BiosymMRParser::Dihedral_angle_constraintContext::Atom_selection() {
  return getTokens(BiosymMRParser::Atom_selection);
}

tree::TerminalNode* BiosymMRParser::Dihedral_angle_constraintContext::Atom_selection(size_t i) {
  return getToken(BiosymMRParser::Atom_selection, i);
}

std::vector<BiosymMRParser::NumberContext *> BiosymMRParser::Dihedral_angle_constraintContext::number() {
  return getRuleContexts<BiosymMRParser::NumberContext>();
}

BiosymMRParser::NumberContext* BiosymMRParser::Dihedral_angle_constraintContext::number(size_t i) {
  return getRuleContext<BiosymMRParser::NumberContext>(i);
}

tree::TerminalNode* BiosymMRParser::Dihedral_angle_constraintContext::RETURN() {
  return getToken(BiosymMRParser::RETURN, 0);
}

tree::TerminalNode* BiosymMRParser::Dihedral_angle_constraintContext::Ordinal() {
  return getToken(BiosymMRParser::Ordinal, 0);
}


size_t BiosymMRParser::Dihedral_angle_constraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleDihedral_angle_constraint;
}


std::any BiosymMRParser::Dihedral_angle_constraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_angle_constraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Dihedral_angle_constraintContext* BiosymMRParser::dihedral_angle_constraint() {
  Dihedral_angle_constraintContext *_localctx = _tracker.createInstance<Dihedral_angle_constraintContext>(_ctx, getState());
  enterRule(_localctx, 20, BiosymMRParser::RuleDihedral_angle_constraint);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(208);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(207);
      match(BiosymMRParser::Ordinal);
    }
    setState(210);
    match(BiosymMRParser::Atom_selection);
    setState(211);
    match(BiosymMRParser::Atom_selection);
    setState(212);
    match(BiosymMRParser::Atom_selection);
    setState(213);
    match(BiosymMRParser::Atom_selection);
    setState(214);
    number();
    setState(215);
    number();
    setState(216);
    number();
    setState(217);
    number();
    setState(219);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 14) != 0)) {
      setState(218);
      number();
    }
    setState(221);
    match(BiosymMRParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_angle_wo_w_constraintsContext ------------------------------------------------------------------

BiosymMRParser::Dihedral_angle_wo_w_constraintsContext::Dihedral_angle_wo_w_constraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BiosymMRParser::Dihedral_angle_wo_w_constraintContext *> BiosymMRParser::Dihedral_angle_wo_w_constraintsContext::dihedral_angle_wo_w_constraint() {
  return getRuleContexts<BiosymMRParser::Dihedral_angle_wo_w_constraintContext>();
}

BiosymMRParser::Dihedral_angle_wo_w_constraintContext* BiosymMRParser::Dihedral_angle_wo_w_constraintsContext::dihedral_angle_wo_w_constraint(size_t i) {
  return getRuleContext<BiosymMRParser::Dihedral_angle_wo_w_constraintContext>(i);
}


size_t BiosymMRParser::Dihedral_angle_wo_w_constraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleDihedral_angle_wo_w_constraints;
}


std::any BiosymMRParser::Dihedral_angle_wo_w_constraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_angle_wo_w_constraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Dihedral_angle_wo_w_constraintsContext* BiosymMRParser::dihedral_angle_wo_w_constraints() {
  Dihedral_angle_wo_w_constraintsContext *_localctx = _tracker.createInstance<Dihedral_angle_wo_w_constraintsContext>(_ctx, getState());
  enterRule(_localctx, 22, BiosymMRParser::RuleDihedral_angle_wo_w_constraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(224); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(223);
              dihedral_angle_wo_w_constraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(226); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 22, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Dihedral_angle_wo_w_constraintContext ------------------------------------------------------------------

BiosymMRParser::Dihedral_angle_wo_w_constraintContext::Dihedral_angle_wo_w_constraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BiosymMRParser::Dihedral_angle_wo_w_constraintContext::Atom_selection() {
  return getTokens(BiosymMRParser::Atom_selection);
}

tree::TerminalNode* BiosymMRParser::Dihedral_angle_wo_w_constraintContext::Atom_selection(size_t i) {
  return getToken(BiosymMRParser::Atom_selection, i);
}

std::vector<BiosymMRParser::NumberContext *> BiosymMRParser::Dihedral_angle_wo_w_constraintContext::number() {
  return getRuleContexts<BiosymMRParser::NumberContext>();
}

BiosymMRParser::NumberContext* BiosymMRParser::Dihedral_angle_wo_w_constraintContext::number(size_t i) {
  return getRuleContext<BiosymMRParser::NumberContext>(i);
}

tree::TerminalNode* BiosymMRParser::Dihedral_angle_wo_w_constraintContext::RETURN() {
  return getToken(BiosymMRParser::RETURN, 0);
}

tree::TerminalNode* BiosymMRParser::Dihedral_angle_wo_w_constraintContext::Ordinal() {
  return getToken(BiosymMRParser::Ordinal, 0);
}


size_t BiosymMRParser::Dihedral_angle_wo_w_constraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleDihedral_angle_wo_w_constraint;
}


std::any BiosymMRParser::Dihedral_angle_wo_w_constraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDihedral_angle_wo_w_constraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Dihedral_angle_wo_w_constraintContext* BiosymMRParser::dihedral_angle_wo_w_constraint() {
  Dihedral_angle_wo_w_constraintContext *_localctx = _tracker.createInstance<Dihedral_angle_wo_w_constraintContext>(_ctx, getState());
  enterRule(_localctx, 24, BiosymMRParser::RuleDihedral_angle_wo_w_constraint);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(229);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(228);
      match(BiosymMRParser::Ordinal);
    }
    setState(231);
    match(BiosymMRParser::Atom_selection);
    setState(232);
    match(BiosymMRParser::Atom_selection);
    setState(233);
    match(BiosymMRParser::Atom_selection);
    setState(234);
    match(BiosymMRParser::Atom_selection);
    setState(235);
    number();
    setState(236);
    number();
    setState(237);
    match(BiosymMRParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Rdc_restraintsContext ------------------------------------------------------------------

BiosymMRParser::Rdc_restraintsContext::Rdc_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BiosymMRParser::Rdc_restraintContext *> BiosymMRParser::Rdc_restraintsContext::rdc_restraint() {
  return getRuleContexts<BiosymMRParser::Rdc_restraintContext>();
}

BiosymMRParser::Rdc_restraintContext* BiosymMRParser::Rdc_restraintsContext::rdc_restraint(size_t i) {
  return getRuleContext<BiosymMRParser::Rdc_restraintContext>(i);
}


size_t BiosymMRParser::Rdc_restraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleRdc_restraints;
}


std::any BiosymMRParser::Rdc_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitRdc_restraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Rdc_restraintsContext* BiosymMRParser::rdc_restraints() {
  Rdc_restraintsContext *_localctx = _tracker.createInstance<Rdc_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 26, BiosymMRParser::RuleRdc_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(240); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(239);
              rdc_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(242); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 24, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Rdc_restraintContext ------------------------------------------------------------------

BiosymMRParser::Rdc_restraintContext::Rdc_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BiosymMRParser::Rdc_restraintContext::Atom_selection() {
  return getTokens(BiosymMRParser::Atom_selection);
}

tree::TerminalNode* BiosymMRParser::Rdc_restraintContext::Atom_selection(size_t i) {
  return getToken(BiosymMRParser::Atom_selection, i);
}

std::vector<BiosymMRParser::NumberContext *> BiosymMRParser::Rdc_restraintContext::number() {
  return getRuleContexts<BiosymMRParser::NumberContext>();
}

BiosymMRParser::NumberContext* BiosymMRParser::Rdc_restraintContext::number(size_t i) {
  return getRuleContext<BiosymMRParser::NumberContext>(i);
}

tree::TerminalNode* BiosymMRParser::Rdc_restraintContext::RETURN() {
  return getToken(BiosymMRParser::RETURN, 0);
}

tree::TerminalNode* BiosymMRParser::Rdc_restraintContext::Ordinal() {
  return getToken(BiosymMRParser::Ordinal, 0);
}


size_t BiosymMRParser::Rdc_restraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleRdc_restraint;
}


std::any BiosymMRParser::Rdc_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitRdc_restraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Rdc_restraintContext* BiosymMRParser::rdc_restraint() {
  Rdc_restraintContext *_localctx = _tracker.createInstance<Rdc_restraintContext>(_ctx, getState());
  enterRule(_localctx, 28, BiosymMRParser::RuleRdc_restraint);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(245);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(244);
      match(BiosymMRParser::Ordinal);
    }
    setState(247);
    match(BiosymMRParser::Atom_selection);
    setState(248);
    match(BiosymMRParser::Atom_selection);
    setState(249);
    number();
    setState(250);
    number();
    setState(251);
    number();
    setState(252);
    number();
    setState(253);
    match(BiosymMRParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Chirality_constraintsContext ------------------------------------------------------------------

BiosymMRParser::Chirality_constraintsContext::Chirality_constraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BiosymMRParser::Chirality_constraintContext *> BiosymMRParser::Chirality_constraintsContext::chirality_constraint() {
  return getRuleContexts<BiosymMRParser::Chirality_constraintContext>();
}

BiosymMRParser::Chirality_constraintContext* BiosymMRParser::Chirality_constraintsContext::chirality_constraint(size_t i) {
  return getRuleContext<BiosymMRParser::Chirality_constraintContext>(i);
}


size_t BiosymMRParser::Chirality_constraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleChirality_constraints;
}


std::any BiosymMRParser::Chirality_constraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitChirality_constraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Chirality_constraintsContext* BiosymMRParser::chirality_constraints() {
  Chirality_constraintsContext *_localctx = _tracker.createInstance<Chirality_constraintsContext>(_ctx, getState());
  enterRule(_localctx, 30, BiosymMRParser::RuleChirality_constraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(256); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(255);
              chirality_constraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(258); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 26, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Chirality_constraintContext ------------------------------------------------------------------

BiosymMRParser::Chirality_constraintContext::Chirality_constraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BiosymMRParser::Chirality_constraintContext::Atom_selection() {
  return getToken(BiosymMRParser::Atom_selection, 0);
}

tree::TerminalNode* BiosymMRParser::Chirality_constraintContext::Chiral_code() {
  return getToken(BiosymMRParser::Chiral_code, 0);
}

tree::TerminalNode* BiosymMRParser::Chirality_constraintContext::RETURN() {
  return getToken(BiosymMRParser::RETURN, 0);
}

tree::TerminalNode* BiosymMRParser::Chirality_constraintContext::Ordinal() {
  return getToken(BiosymMRParser::Ordinal, 0);
}


size_t BiosymMRParser::Chirality_constraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleChirality_constraint;
}


std::any BiosymMRParser::Chirality_constraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitChirality_constraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Chirality_constraintContext* BiosymMRParser::chirality_constraint() {
  Chirality_constraintContext *_localctx = _tracker.createInstance<Chirality_constraintContext>(_ctx, getState());
  enterRule(_localctx, 32, BiosymMRParser::RuleChirality_constraint);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(261);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(260);
      match(BiosymMRParser::Ordinal);
    }
    setState(263);
    match(BiosymMRParser::Atom_selection);
    setState(264);
    match(BiosymMRParser::Chiral_code);
    setState(265);
    match(BiosymMRParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Prochirality_constraintsContext ------------------------------------------------------------------

BiosymMRParser::Prochirality_constraintsContext::Prochirality_constraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BiosymMRParser::Prochirality_constraintContext *> BiosymMRParser::Prochirality_constraintsContext::prochirality_constraint() {
  return getRuleContexts<BiosymMRParser::Prochirality_constraintContext>();
}

BiosymMRParser::Prochirality_constraintContext* BiosymMRParser::Prochirality_constraintsContext::prochirality_constraint(size_t i) {
  return getRuleContext<BiosymMRParser::Prochirality_constraintContext>(i);
}


size_t BiosymMRParser::Prochirality_constraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleProchirality_constraints;
}


std::any BiosymMRParser::Prochirality_constraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitProchirality_constraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Prochirality_constraintsContext* BiosymMRParser::prochirality_constraints() {
  Prochirality_constraintsContext *_localctx = _tracker.createInstance<Prochirality_constraintsContext>(_ctx, getState());
  enterRule(_localctx, 34, BiosymMRParser::RuleProchirality_constraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(268); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(267);
              prochirality_constraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(270); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 28, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Prochirality_constraintContext ------------------------------------------------------------------

BiosymMRParser::Prochirality_constraintContext::Prochirality_constraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> BiosymMRParser::Prochirality_constraintContext::Atom_selection() {
  return getTokens(BiosymMRParser::Atom_selection);
}

tree::TerminalNode* BiosymMRParser::Prochirality_constraintContext::Atom_selection(size_t i) {
  return getToken(BiosymMRParser::Atom_selection, i);
}

tree::TerminalNode* BiosymMRParser::Prochirality_constraintContext::RETURN() {
  return getToken(BiosymMRParser::RETURN, 0);
}

tree::TerminalNode* BiosymMRParser::Prochirality_constraintContext::Ordinal() {
  return getToken(BiosymMRParser::Ordinal, 0);
}


size_t BiosymMRParser::Prochirality_constraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleProchirality_constraint;
}


std::any BiosymMRParser::Prochirality_constraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitProchirality_constraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Prochirality_constraintContext* BiosymMRParser::prochirality_constraint() {
  Prochirality_constraintContext *_localctx = _tracker.createInstance<Prochirality_constraintContext>(_ctx, getState());
  enterRule(_localctx, 36, BiosymMRParser::RuleProchirality_constraint);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(273);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BiosymMRParser::Ordinal) {
      setState(272);
      match(BiosymMRParser::Ordinal);
    }
    setState(275);
    match(BiosymMRParser::Atom_selection);
    setState(276);
    match(BiosymMRParser::Atom_selection);
    setState(277);
    match(BiosymMRParser::Atom_selection);
    setState(278);
    match(BiosymMRParser::Atom_selection);
    setState(279);
    match(BiosymMRParser::Atom_selection);
    setState(280);
    match(BiosymMRParser::RETURN);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Mixing_timeContext ------------------------------------------------------------------

BiosymMRParser::Mixing_timeContext::Mixing_timeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BiosymMRParser::Mixing_timeContext::Mixing_times() {
  return getToken(BiosymMRParser::Mixing_times, 0);
}

tree::TerminalNode* BiosymMRParser::Mixing_timeContext::RETURN_MT() {
  return getToken(BiosymMRParser::RETURN_MT, 0);
}

std::vector<tree::TerminalNode *> BiosymMRParser::Mixing_timeContext::Real_MT() {
  return getTokens(BiosymMRParser::Real_MT);
}

tree::TerminalNode* BiosymMRParser::Mixing_timeContext::Real_MT(size_t i) {
  return getToken(BiosymMRParser::Real_MT, i);
}

std::vector<tree::TerminalNode *> BiosymMRParser::Mixing_timeContext::Float_MT() {
  return getTokens(BiosymMRParser::Float_MT);
}

tree::TerminalNode* BiosymMRParser::Mixing_timeContext::Float_MT(size_t i) {
  return getToken(BiosymMRParser::Float_MT, i);
}

std::vector<tree::TerminalNode *> BiosymMRParser::Mixing_timeContext::Integer_MT() {
  return getTokens(BiosymMRParser::Integer_MT);
}

tree::TerminalNode* BiosymMRParser::Mixing_timeContext::Integer_MT(size_t i) {
  return getToken(BiosymMRParser::Integer_MT, i);
}


size_t BiosymMRParser::Mixing_timeContext::getRuleIndex() const {
  return BiosymMRParser::RuleMixing_time;
}


std::any BiosymMRParser::Mixing_timeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitMixing_time(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Mixing_timeContext* BiosymMRParser::mixing_time() {
  Mixing_timeContext *_localctx = _tracker.createInstance<Mixing_timeContext>(_ctx, getState());
  enterRule(_localctx, 38, BiosymMRParser::RuleMixing_time);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(282);
    match(BiosymMRParser::Mixing_times);
    setState(284); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(283);
      _la = _input->LA(1);
      if (!((((_la & ~ 0x3fULL) == 0) &&
        ((1ULL << _la) & 240518168576) != 0))) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(286); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 240518168576) != 0));
    setState(288);
    match(BiosymMRParser::RETURN_MT);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- NumberContext ------------------------------------------------------------------

BiosymMRParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BiosymMRParser::NumberContext::Float() {
  return getToken(BiosymMRParser::Float, 0);
}

tree::TerminalNode* BiosymMRParser::NumberContext::Float_DecimalComma() {
  return getToken(BiosymMRParser::Float_DecimalComma, 0);
}

tree::TerminalNode* BiosymMRParser::NumberContext::Integer() {
  return getToken(BiosymMRParser::Integer, 0);
}


size_t BiosymMRParser::NumberContext::getRuleIndex() const {
  return BiosymMRParser::RuleNumber;
}


std::any BiosymMRParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::NumberContext* BiosymMRParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 40, BiosymMRParser::RuleNumber);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(290);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 14) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ins_distance_restraintsContext ------------------------------------------------------------------

BiosymMRParser::Ins_distance_restraintsContext::Ins_distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BiosymMRParser::Ins_distance_restraintContext* BiosymMRParser::Ins_distance_restraintsContext::ins_distance_restraint() {
  return getRuleContext<BiosymMRParser::Ins_distance_restraintContext>(0);
}


size_t BiosymMRParser::Ins_distance_restraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleIns_distance_restraints;
}


std::any BiosymMRParser::Ins_distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitIns_distance_restraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Ins_distance_restraintsContext* BiosymMRParser::ins_distance_restraints() {
  Ins_distance_restraintsContext *_localctx = _tracker.createInstance<Ins_distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 42, BiosymMRParser::RuleIns_distance_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(292);
    ins_distance_restraint();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ins_distance_restraintContext ------------------------------------------------------------------

BiosymMRParser::Ins_distance_restraintContext::Ins_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BiosymMRParser::Decl_create_distContext* BiosymMRParser::Ins_distance_restraintContext::decl_create_dist() {
  return getRuleContext<BiosymMRParser::Decl_create_distContext>(0);
}

BiosymMRParser::Decl_functionContext* BiosymMRParser::Ins_distance_restraintContext::decl_function() {
  return getRuleContext<BiosymMRParser::Decl_functionContext>(0);
}

BiosymMRParser::Decl_targetContext* BiosymMRParser::Ins_distance_restraintContext::decl_target() {
  return getRuleContext<BiosymMRParser::Decl_targetContext>(0);
}


size_t BiosymMRParser::Ins_distance_restraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleIns_distance_restraint;
}


std::any BiosymMRParser::Ins_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitIns_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Ins_distance_restraintContext* BiosymMRParser::ins_distance_restraint() {
  Ins_distance_restraintContext *_localctx = _tracker.createInstance<Ins_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 44, BiosymMRParser::RuleIns_distance_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(294);
    decl_create_dist();
    setState(295);
    decl_function();
    setState(296);
    decl_target();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ins_dihedral_angle_restraintsContext ------------------------------------------------------------------

BiosymMRParser::Ins_dihedral_angle_restraintsContext::Ins_dihedral_angle_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BiosymMRParser::Ins_dihedral_angle_restraintContext* BiosymMRParser::Ins_dihedral_angle_restraintsContext::ins_dihedral_angle_restraint() {
  return getRuleContext<BiosymMRParser::Ins_dihedral_angle_restraintContext>(0);
}


size_t BiosymMRParser::Ins_dihedral_angle_restraintsContext::getRuleIndex() const {
  return BiosymMRParser::RuleIns_dihedral_angle_restraints;
}


std::any BiosymMRParser::Ins_dihedral_angle_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitIns_dihedral_angle_restraints(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Ins_dihedral_angle_restraintsContext* BiosymMRParser::ins_dihedral_angle_restraints() {
  Ins_dihedral_angle_restraintsContext *_localctx = _tracker.createInstance<Ins_dihedral_angle_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 46, BiosymMRParser::RuleIns_dihedral_angle_restraints);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(298);
    ins_dihedral_angle_restraint();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ins_dihedral_angle_restraintContext ------------------------------------------------------------------

BiosymMRParser::Ins_dihedral_angle_restraintContext::Ins_dihedral_angle_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BiosymMRParser::Decl_create_dihedContext* BiosymMRParser::Ins_dihedral_angle_restraintContext::decl_create_dihed() {
  return getRuleContext<BiosymMRParser::Decl_create_dihedContext>(0);
}

BiosymMRParser::Decl_functionContext* BiosymMRParser::Ins_dihedral_angle_restraintContext::decl_function() {
  return getRuleContext<BiosymMRParser::Decl_functionContext>(0);
}

BiosymMRParser::Decl_targetContext* BiosymMRParser::Ins_dihedral_angle_restraintContext::decl_target() {
  return getRuleContext<BiosymMRParser::Decl_targetContext>(0);
}


size_t BiosymMRParser::Ins_dihedral_angle_restraintContext::getRuleIndex() const {
  return BiosymMRParser::RuleIns_dihedral_angle_restraint;
}


std::any BiosymMRParser::Ins_dihedral_angle_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitIns_dihedral_angle_restraint(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Ins_dihedral_angle_restraintContext* BiosymMRParser::ins_dihedral_angle_restraint() {
  Ins_dihedral_angle_restraintContext *_localctx = _tracker.createInstance<Ins_dihedral_angle_restraintContext>(_ctx, getState());
  enterRule(_localctx, 48, BiosymMRParser::RuleIns_dihedral_angle_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(300);
    decl_create_dihed();
    setState(301);
    decl_function();
    setState(303);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 31, _ctx)) {
    case 1: {
      setState(302);
      decl_target();
      break;
    }

    default:
      break;
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Decl_create_distContext ------------------------------------------------------------------

BiosymMRParser::Decl_create_distContext::Decl_create_distContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BiosymMRParser::Decl_create_distContext::Restraint() {
  return getToken(BiosymMRParser::Restraint, 0);
}

tree::TerminalNode* BiosymMRParser::Decl_create_distContext::Create() {
  return getToken(BiosymMRParser::Create, 0);
}

BiosymMRParser::Ins_rst_idContext* BiosymMRParser::Decl_create_distContext::ins_rst_id() {
  return getRuleContext<BiosymMRParser::Ins_rst_idContext>(0);
}

tree::TerminalNode* BiosymMRParser::Decl_create_distContext::Distance() {
  return getToken(BiosymMRParser::Distance, 0);
}

std::vector<BiosymMRParser::Ins_atom_selContext *> BiosymMRParser::Decl_create_distContext::ins_atom_sel() {
  return getRuleContexts<BiosymMRParser::Ins_atom_selContext>();
}

BiosymMRParser::Ins_atom_selContext* BiosymMRParser::Decl_create_distContext::ins_atom_sel(size_t i) {
  return getRuleContext<BiosymMRParser::Ins_atom_selContext>(i);
}

tree::TerminalNode* BiosymMRParser::Decl_create_distContext::RETURN_II() {
  return getToken(BiosymMRParser::RETURN_II, 0);
}


size_t BiosymMRParser::Decl_create_distContext::getRuleIndex() const {
  return BiosymMRParser::RuleDecl_create_dist;
}


std::any BiosymMRParser::Decl_create_distContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDecl_create_dist(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Decl_create_distContext* BiosymMRParser::decl_create_dist() {
  Decl_create_distContext *_localctx = _tracker.createInstance<Decl_create_distContext>(_ctx, getState());
  enterRule(_localctx, 50, BiosymMRParser::RuleDecl_create_dist);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(305);
    match(BiosymMRParser::Restraint);
    setState(306);
    match(BiosymMRParser::Create);
    setState(307);
    ins_rst_id();
    setState(308);
    match(BiosymMRParser::Distance);
    setState(309);
    ins_atom_sel();
    setState(310);
    ins_atom_sel();
    setState(311);
    match(BiosymMRParser::RETURN_II);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Decl_create_dihedContext ------------------------------------------------------------------

BiosymMRParser::Decl_create_dihedContext::Decl_create_dihedContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BiosymMRParser::Decl_create_dihedContext::Restraint() {
  return getToken(BiosymMRParser::Restraint, 0);
}

tree::TerminalNode* BiosymMRParser::Decl_create_dihedContext::Create() {
  return getToken(BiosymMRParser::Create, 0);
}

BiosymMRParser::Ins_rst_idContext* BiosymMRParser::Decl_create_dihedContext::ins_rst_id() {
  return getRuleContext<BiosymMRParser::Ins_rst_idContext>(0);
}

tree::TerminalNode* BiosymMRParser::Decl_create_dihedContext::Torsion() {
  return getToken(BiosymMRParser::Torsion, 0);
}

std::vector<BiosymMRParser::Ins_atom_selContext *> BiosymMRParser::Decl_create_dihedContext::ins_atom_sel() {
  return getRuleContexts<BiosymMRParser::Ins_atom_selContext>();
}

BiosymMRParser::Ins_atom_selContext* BiosymMRParser::Decl_create_dihedContext::ins_atom_sel(size_t i) {
  return getRuleContext<BiosymMRParser::Ins_atom_selContext>(i);
}

tree::TerminalNode* BiosymMRParser::Decl_create_dihedContext::RETURN_II() {
  return getToken(BiosymMRParser::RETURN_II, 0);
}


size_t BiosymMRParser::Decl_create_dihedContext::getRuleIndex() const {
  return BiosymMRParser::RuleDecl_create_dihed;
}


std::any BiosymMRParser::Decl_create_dihedContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDecl_create_dihed(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Decl_create_dihedContext* BiosymMRParser::decl_create_dihed() {
  Decl_create_dihedContext *_localctx = _tracker.createInstance<Decl_create_dihedContext>(_ctx, getState());
  enterRule(_localctx, 52, BiosymMRParser::RuleDecl_create_dihed);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(313);
    match(BiosymMRParser::Restraint);
    setState(314);
    match(BiosymMRParser::Create);
    setState(315);
    ins_rst_id();
    setState(316);
    match(BiosymMRParser::Torsion);
    setState(317);
    ins_atom_sel();
    setState(318);
    ins_atom_sel();
    setState(319);
    ins_atom_sel();
    setState(320);
    ins_atom_sel();
    setState(321);
    match(BiosymMRParser::RETURN_II);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Decl_functionContext ------------------------------------------------------------------

BiosymMRParser::Decl_functionContext::Decl_functionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BiosymMRParser::Decl_functionContext::Restraint() {
  return getToken(BiosymMRParser::Restraint, 0);
}

tree::TerminalNode* BiosymMRParser::Decl_functionContext::Function() {
  return getToken(BiosymMRParser::Function, 0);
}

BiosymMRParser::Ins_rst_idContext* BiosymMRParser::Decl_functionContext::ins_rst_id() {
  return getRuleContext<BiosymMRParser::Ins_rst_idContext>(0);
}

tree::TerminalNode* BiosymMRParser::Decl_functionContext::RETURN_II() {
  return getToken(BiosymMRParser::RETURN_II, 0);
}

std::vector<BiosymMRParser::Ins_num_selContext *> BiosymMRParser::Decl_functionContext::ins_num_sel() {
  return getRuleContexts<BiosymMRParser::Ins_num_selContext>();
}

BiosymMRParser::Ins_num_selContext* BiosymMRParser::Decl_functionContext::ins_num_sel(size_t i) {
  return getRuleContext<BiosymMRParser::Ins_num_selContext>(i);
}

tree::TerminalNode* BiosymMRParser::Decl_functionContext::Trans() {
  return getToken(BiosymMRParser::Trans, 0);
}

tree::TerminalNode* BiosymMRParser::Decl_functionContext::Quadratic() {
  return getToken(BiosymMRParser::Quadratic, 0);
}

tree::TerminalNode* BiosymMRParser::Decl_functionContext::Flat_bottomed() {
  return getToken(BiosymMRParser::Flat_bottomed, 0);
}


size_t BiosymMRParser::Decl_functionContext::getRuleIndex() const {
  return BiosymMRParser::RuleDecl_function;
}


std::any BiosymMRParser::Decl_functionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDecl_function(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Decl_functionContext* BiosymMRParser::decl_function() {
  Decl_functionContext *_localctx = _tracker.createInstance<Decl_functionContext>(_ctx, getState());
  enterRule(_localctx, 54, BiosymMRParser::RuleDecl_function);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(323);
    match(BiosymMRParser::Restraint);
    setState(324);
    match(BiosymMRParser::Function);
    setState(325);
    ins_rst_id();
    setState(332);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case BiosymMRParser::Quadratic:
      case BiosymMRParser::Flat_bottomed: {
        setState(326);
        _la = _input->LA(1);
        if (!(_la == BiosymMRParser::Quadratic

        || _la == BiosymMRParser::Flat_bottomed)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(327);
        ins_num_sel();
        setState(328);
        ins_num_sel();
        break;
      }

      case BiosymMRParser::Trans: {
        setState(330);
        match(BiosymMRParser::Trans);
        setState(331);
        ins_num_sel();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(335);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2149056512) != 0)) {
      setState(334);
      ins_num_sel();
    }
    setState(337);
    match(BiosymMRParser::RETURN_II);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Decl_targetContext ------------------------------------------------------------------

BiosymMRParser::Decl_targetContext::Decl_targetContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BiosymMRParser::Decl_targetContext::Restraint() {
  return getToken(BiosymMRParser::Restraint, 0);
}

tree::TerminalNode* BiosymMRParser::Decl_targetContext::Target() {
  return getToken(BiosymMRParser::Target, 0);
}

BiosymMRParser::Ins_rst_idContext* BiosymMRParser::Decl_targetContext::ins_rst_id() {
  return getRuleContext<BiosymMRParser::Ins_rst_idContext>(0);
}

std::vector<BiosymMRParser::Ins_num_selContext *> BiosymMRParser::Decl_targetContext::ins_num_sel() {
  return getRuleContexts<BiosymMRParser::Ins_num_selContext>();
}

BiosymMRParser::Ins_num_selContext* BiosymMRParser::Decl_targetContext::ins_num_sel(size_t i) {
  return getRuleContext<BiosymMRParser::Ins_num_selContext>(i);
}

tree::TerminalNode* BiosymMRParser::Decl_targetContext::RETURN_II() {
  return getToken(BiosymMRParser::RETURN_II, 0);
}

tree::TerminalNode* BiosymMRParser::Decl_targetContext::Relative() {
  return getToken(BiosymMRParser::Relative, 0);
}


size_t BiosymMRParser::Decl_targetContext::getRuleIndex() const {
  return BiosymMRParser::RuleDecl_target;
}


std::any BiosymMRParser::Decl_targetContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitDecl_target(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Decl_targetContext* BiosymMRParser::decl_target() {
  Decl_targetContext *_localctx = _tracker.createInstance<Decl_targetContext>(_ctx, getState());
  enterRule(_localctx, 56, BiosymMRParser::RuleDecl_target);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(339);
    match(BiosymMRParser::Restraint);
    setState(340);
    match(BiosymMRParser::Target);
    setState(341);
    ins_rst_id();
    setState(344);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case BiosymMRParser::Integer_II:
      case BiosymMRParser::Float_II:
      case BiosymMRParser::Double_quote_string_II: {
        setState(342);
        ins_num_sel();
        break;
      }

      case BiosymMRParser::Relative: {
        setState(343);
        match(BiosymMRParser::Relative);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(346);
    ins_num_sel();
    setState(347);
    match(BiosymMRParser::RETURN_II);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ins_rst_idContext ------------------------------------------------------------------

BiosymMRParser::Ins_rst_idContext::Ins_rst_idContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BiosymMRParser::Ins_rst_idContext::Double_quote_string_II() {
  return getToken(BiosymMRParser::Double_quote_string_II, 0);
}

tree::TerminalNode* BiosymMRParser::Ins_rst_idContext::Simple_name_II() {
  return getToken(BiosymMRParser::Simple_name_II, 0);
}

tree::TerminalNode* BiosymMRParser::Ins_rst_idContext::Integer_II() {
  return getToken(BiosymMRParser::Integer_II, 0);
}


size_t BiosymMRParser::Ins_rst_idContext::getRuleIndex() const {
  return BiosymMRParser::RuleIns_rst_id;
}


std::any BiosymMRParser::Ins_rst_idContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitIns_rst_id(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Ins_rst_idContext* BiosymMRParser::ins_rst_id() {
  Ins_rst_idContext *_localctx = _tracker.createInstance<Ins_rst_idContext>(_ctx, getState());
  enterRule(_localctx, 58, BiosymMRParser::RuleIns_rst_id);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(349);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 3221749760) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ins_atom_selContext ------------------------------------------------------------------

BiosymMRParser::Ins_atom_selContext::Ins_atom_selContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BiosymMRParser::Ins_atom_selContext::Double_quote_string_II() {
  return getToken(BiosymMRParser::Double_quote_string_II, 0);
}

tree::TerminalNode* BiosymMRParser::Ins_atom_selContext::Simple_name_II() {
  return getToken(BiosymMRParser::Simple_name_II, 0);
}


size_t BiosymMRParser::Ins_atom_selContext::getRuleIndex() const {
  return BiosymMRParser::RuleIns_atom_sel;
}


std::any BiosymMRParser::Ins_atom_selContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitIns_atom_sel(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Ins_atom_selContext* BiosymMRParser::ins_atom_sel() {
  Ins_atom_selContext *_localctx = _tracker.createInstance<Ins_atom_selContext>(_ctx, getState());
  enterRule(_localctx, 60, BiosymMRParser::RuleIns_atom_sel);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(351);
    _la = _input->LA(1);
    if (!(_la == BiosymMRParser::Simple_name_II

    || _la == BiosymMRParser::Double_quote_string_II)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ins_num_selContext ------------------------------------------------------------------

BiosymMRParser::Ins_num_selContext::Ins_num_selContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BiosymMRParser::Ins_num_selContext::Double_quote_string_II() {
  return getToken(BiosymMRParser::Double_quote_string_II, 0);
}

tree::TerminalNode* BiosymMRParser::Ins_num_selContext::Float_II() {
  return getToken(BiosymMRParser::Float_II, 0);
}

tree::TerminalNode* BiosymMRParser::Ins_num_selContext::Integer_II() {
  return getToken(BiosymMRParser::Integer_II, 0);
}


size_t BiosymMRParser::Ins_num_selContext::getRuleIndex() const {
  return BiosymMRParser::RuleIns_num_sel;
}


std::any BiosymMRParser::Ins_num_selContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BiosymMRParserVisitor*>(visitor))
    return parserVisitor->visitIns_num_sel(this);
  else
    return visitor->visitChildren(this);
}

BiosymMRParser::Ins_num_selContext* BiosymMRParser::ins_num_sel() {
  Ins_num_selContext *_localctx = _tracker.createInstance<Ins_num_selContext>(_ctx, getState());
  enterRule(_localctx, 62, BiosymMRParser::RuleIns_num_sel);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(353);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2149056512) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

void BiosymMRParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  biosymmrparserParserInitialize();
#else
  ::antlr4::internal::call_once(biosymmrparserParserOnceFlag, biosymmrparserParserInitialize);
#endif
}
