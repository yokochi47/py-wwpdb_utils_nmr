
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/CyanaMRParser.g4 by ANTLR 4.13.2


#include "CyanaMRParserVisitor.h"

#include "CyanaMRParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct CyanaMRParserStaticData final {
  CyanaMRParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  CyanaMRParserStaticData(const CyanaMRParserStaticData&) = delete;
  CyanaMRParserStaticData(CyanaMRParserStaticData&&) = delete;
  CyanaMRParserStaticData& operator=(const CyanaMRParserStaticData&) = delete;
  CyanaMRParserStaticData& operator=(CyanaMRParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag cyanamrparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<CyanaMRParserStaticData> cyanamrparserParserStaticData = nullptr;

void cyanamrparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (cyanamrparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(cyanamrparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<CyanaMRParserStaticData>(
    std::vector<std::string>{
      "cyana_mr", "comment", "distance_restraints", "distance_restraint", 
      "torsion_angle_restraints", "torsion_angle_restraint", "rdc_restraints", 
      "rdc_parameter", "rdc_restraint", "pcs_restraints", "pcs_parameter", 
      "pcs_restraint", "fixres_distance_restraints", "fixres_distance_restraint", 
      "fixresw_distance_restraints", "fixresw_distance_restraint", "fixresw2_distance_restraints", 
      "fixresw2_distance_restraint", "fixatm_distance_restraints", "fixatm_distance_restraint", 
      "fixatmw_distance_restraints", "fixatmw_distance_restraint", "fixatmw2_distance_restraints", 
      "fixatmw2_distance_restraint", "diana_distance_restraints", "diana_distance_restraint", 
      "diana_ssbond_restraints", "diana_ssbond_restraint", "diana_torsion_angle_restraints", 
      "diana_torsion_angle_restraint", "diana_coupling_constant_restraints", 
      "diana_coupling_constant_restraint", "diana_chemical_shifts", "diana_chemical_shift", 
      "distance_w_chain_restraints", "distance_w_chain_restraint", "distance_w_chain2_restraints", 
      "distance_w_chain2_restraint", "distance_w_chain3_restraints", "distance_w_chain3_restraint", 
      "torsion_angle_w_chain_restraints", "torsion_angle_w_chain_restraint", 
      "cco_restraints", "cco_restraint", "ssbond_macro", "hbond_macro", 
      "link_statement", "stereoassign_macro", "declare_variable", "set_variable", 
      "unset_variable", "print_macro", "unambig_atom_name_mapping", "mapping_list", 
      "ambig_atom_name_mapping", "ambig_list", "number", "gen_res_num", 
      "gen_simple_name", "gen_atom_name"
    },
    std::vector<std::string>{
      "", "", "", "", "", "", "", "", "", "'NOEUPP'", "'NOELOW'", "'SSUPP'", 
      "'SSLOW'", "'JCOUPL'", "'ANGLE'", "'SHIFTS'", "'TYPE'", "", "'OR'", 
      "'SSBOND'", "", "'HBOND'", "'LINK'", "", "'VAR'", "'UNSET'", "", "'PRINT'", 
      "'RESIDUE'", "'MAPPING'", "'AMBIG'", "", "", "", "", "", "", "", "", 
      "", "", "'ATOM1'", "'ATOM2'", "'RESIDUE1'", "'RESIDUE2'"
    },
    std::vector<std::string>{
      "", "Ambig_code", "Integer", "Float", "Float_DecimalComma", "Orientation_header", 
      "Tensor_header", "SMCLN_COMMENT", "COMMENT", "NoeUpp", "NoeLow", "SSUpp", 
      "SSLow", "JCoupl", "Angle", "Shifts", "Type", "Equ_op", "Or", "Ssbond", 
      "Ssbond_resids", "Hbond", "Link", "Atom_stereo", "Var", "Unset", "SetVar", 
      "Print", "Residue", "Mapping", "Ambig", "Capital_integer", "Integer_capital", 
      "Simple_name", "SPACE", "ENCLOSE_COMMENT", "SECTION_COMMENT", "LINE_COMMENT", 
      "Any_name", "SPACE_CM", "RETURN_CM", "Atom1", "Atom2", "Residue1", 
      "Residue2", "Equ_op_HB", "Integer_HB", "Simple_name_HB", "SPACE_HB", 
      "RETURN_HB", "LINE_COMMENT_HB", "Double_quote_string", "SPACE_PR", 
      "RETURN_PR", "LINE_COMMENT_PR", "Simple_name_VA", "SPACE_VA", "RETURN_VA", 
      "LINE_COMMENT_VA", "Ambig_code_MP", "Integer_MP", "Simple_name_MP", 
      "Equ_op_MP", "SPACE_MP", "RETURN_MP", "LINE_COMMENT_MP"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,65,756,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,
  	28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,7,33,2,34,7,34,2,35,7,
  	35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,2,40,7,40,2,41,7,41,2,42,7,
  	42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,
  	49,2,50,7,50,2,51,7,51,2,52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,
  	56,2,57,7,57,2,58,7,58,2,59,7,59,1,0,1,0,4,0,123,8,0,11,0,12,0,124,1,
  	0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
  	1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,158,8,0,10,0,
  	12,0,161,9,0,1,0,1,0,1,1,1,1,5,1,167,8,1,10,1,12,1,170,9,1,1,1,1,1,1,
  	2,4,2,175,8,2,11,2,12,2,176,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,187,8,
  	3,1,3,3,3,190,8,3,1,3,3,3,193,8,3,1,3,3,3,196,8,3,1,3,3,3,199,8,3,1,4,
  	4,4,202,8,4,11,4,12,4,203,1,5,1,5,1,5,1,5,1,5,1,5,3,5,212,8,5,1,5,1,5,
  	1,5,3,5,217,8,5,1,5,3,5,220,8,5,1,6,4,6,223,8,6,11,6,12,6,224,1,6,1,6,
  	1,6,4,6,230,8,6,11,6,12,6,231,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
  	1,8,1,8,1,8,1,8,1,8,1,8,3,8,250,8,8,1,9,4,9,253,8,9,11,9,12,9,254,1,9,
  	1,9,1,9,4,9,260,8,9,11,9,12,9,261,1,10,1,10,1,10,1,10,1,10,1,11,1,11,
  	1,11,1,11,1,11,1,11,1,11,1,11,1,12,4,12,278,8,12,11,12,12,12,279,1,13,
  	1,13,1,13,3,13,285,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,4,13,294,8,
  	13,11,13,12,13,295,1,14,4,14,299,8,14,11,14,12,14,300,1,15,1,15,1,15,
  	3,15,306,8,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,4,15,316,8,15,11,
  	15,12,15,317,1,16,4,16,321,8,16,11,16,12,16,322,1,17,1,17,1,17,3,17,328,
  	8,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,4,17,339,8,17,11,17,
  	12,17,340,1,18,4,18,344,8,18,11,18,12,18,345,1,19,1,19,1,19,1,19,3,19,
  	352,8,19,1,19,1,19,1,19,1,19,1,19,1,19,4,19,360,8,19,11,19,12,19,361,
  	1,20,4,20,365,8,20,11,20,12,20,366,1,21,1,21,1,21,1,21,3,21,373,8,21,
  	1,21,1,21,1,21,1,21,1,21,1,21,1,21,4,21,382,8,21,11,21,12,21,383,1,22,
  	4,22,387,8,22,11,22,12,22,388,1,23,1,23,1,23,1,23,3,23,395,8,23,1,23,
  	1,23,1,23,1,23,1,23,1,23,1,23,1,23,4,23,405,8,23,11,23,12,23,406,1,24,
  	4,24,410,8,24,11,24,12,24,411,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,
  	1,25,1,25,1,25,1,25,1,25,1,25,3,25,428,8,25,1,25,1,25,3,25,432,8,25,1,
  	26,4,26,435,8,26,11,26,12,26,436,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,
  	27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,453,8,27,1,27,1,27,3,27,457,8,27,
  	1,28,4,28,460,8,28,11,28,12,28,461,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
  	1,29,3,29,472,8,29,1,30,4,30,475,8,30,11,30,12,30,476,1,31,1,31,1,31,
  	1,31,1,31,1,31,1,31,1,31,3,31,487,8,31,1,32,4,32,490,8,32,11,32,12,32,
  	491,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,5,33,502,8,33,10,33,12,33,
  	505,9,33,1,33,1,33,3,33,509,8,33,1,34,4,34,512,8,34,11,34,12,34,513,1,
  	35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,3,35,526,8,35,1,35,3,
  	35,529,8,35,1,35,3,35,532,8,35,1,35,3,35,535,8,35,1,35,3,35,538,8,35,
  	1,36,4,36,541,8,36,11,36,12,36,542,1,37,1,37,1,37,1,37,1,37,1,37,1,37,
  	1,37,1,37,1,37,3,37,555,8,37,1,37,3,37,558,8,37,1,37,3,37,561,8,37,1,
  	37,3,37,564,8,37,1,37,3,37,567,8,37,1,38,4,38,570,8,38,11,38,12,38,571,
  	1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,3,39,584,8,39,1,39,
  	3,39,587,8,39,1,39,3,39,590,8,39,1,39,3,39,593,8,39,1,39,3,39,596,8,39,
  	1,40,4,40,599,8,40,11,40,12,40,600,1,41,1,41,1,41,1,41,1,41,1,41,1,41,
  	3,41,610,8,41,1,41,1,41,1,41,3,41,615,8,41,1,41,3,41,618,8,41,1,42,4,
  	42,621,8,42,11,42,12,42,622,1,43,1,43,1,43,1,43,1,43,1,43,3,43,631,8,
  	43,1,43,3,43,634,8,43,1,43,3,43,637,8,43,1,43,3,43,640,8,43,1,43,3,43,
  	643,8,43,1,44,1,44,1,44,1,45,1,45,1,45,3,45,651,8,45,1,45,1,45,1,45,3,
  	45,656,8,45,1,45,1,45,1,45,3,45,661,8,45,1,45,1,45,1,45,3,45,666,8,45,
  	1,45,1,45,1,45,1,46,1,46,1,46,1,46,1,46,1,46,1,47,1,47,1,47,1,47,1,48,
  	1,48,5,48,683,8,48,10,48,12,48,686,9,48,1,48,1,48,1,49,1,49,1,50,1,50,
  	5,50,694,8,50,10,50,12,50,697,9,50,1,50,1,50,1,51,1,51,1,51,1,51,1,52,
  	1,52,1,52,3,52,708,8,52,1,52,1,52,4,52,712,8,52,11,52,12,52,713,1,53,
  	1,53,1,53,1,53,4,53,720,8,53,11,53,12,53,721,1,53,1,53,1,54,1,54,1,54,
  	3,54,729,8,54,1,54,1,54,4,54,733,8,54,11,54,12,54,734,1,55,1,55,1,55,
  	1,55,1,55,4,55,742,8,55,11,55,12,55,743,1,55,1,55,1,56,1,56,1,57,1,57,
  	1,58,1,58,1,59,1,59,1,59,0,0,60,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
  	28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,
  	74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,
  	116,118,0,9,1,1,40,40,2,0,2,2,31,33,1,0,9,10,1,0,11,12,2,0,59,59,61,61,
  	1,0,2,4,2,0,2,2,31,32,1,0,31,33,2,0,1,1,31,33,828,0,159,1,0,0,0,2,164,
  	1,0,0,0,4,174,1,0,0,0,6,178,1,0,0,0,8,201,1,0,0,0,10,205,1,0,0,0,12,222,
  	1,0,0,0,14,233,1,0,0,0,16,238,1,0,0,0,18,252,1,0,0,0,20,263,1,0,0,0,22,
  	268,1,0,0,0,24,277,1,0,0,0,26,281,1,0,0,0,28,298,1,0,0,0,30,302,1,0,0,
  	0,32,320,1,0,0,0,34,324,1,0,0,0,36,343,1,0,0,0,38,347,1,0,0,0,40,364,
  	1,0,0,0,42,368,1,0,0,0,44,386,1,0,0,0,46,390,1,0,0,0,48,409,1,0,0,0,50,
  	413,1,0,0,0,52,434,1,0,0,0,54,438,1,0,0,0,56,459,1,0,0,0,58,463,1,0,0,
  	0,60,474,1,0,0,0,62,478,1,0,0,0,64,489,1,0,0,0,66,493,1,0,0,0,68,511,
  	1,0,0,0,70,515,1,0,0,0,72,540,1,0,0,0,74,544,1,0,0,0,76,569,1,0,0,0,78,
  	573,1,0,0,0,80,598,1,0,0,0,82,602,1,0,0,0,84,620,1,0,0,0,86,624,1,0,0,
  	0,88,644,1,0,0,0,90,647,1,0,0,0,92,670,1,0,0,0,94,676,1,0,0,0,96,680,
  	1,0,0,0,98,689,1,0,0,0,100,691,1,0,0,0,102,700,1,0,0,0,104,704,1,0,0,
  	0,106,715,1,0,0,0,108,725,1,0,0,0,110,736,1,0,0,0,112,747,1,0,0,0,114,
  	749,1,0,0,0,116,751,1,0,0,0,118,753,1,0,0,0,120,158,5,5,0,0,121,123,5,
  	6,0,0,122,121,1,0,0,0,123,124,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,
  	125,158,1,0,0,0,126,158,3,2,1,0,127,158,3,4,2,0,128,158,3,24,12,0,129,
  	158,3,28,14,0,130,158,3,32,16,0,131,158,3,36,18,0,132,158,3,40,20,0,133,
  	158,3,44,22,0,134,158,3,48,24,0,135,158,3,52,26,0,136,158,3,56,28,0,137,
  	158,3,60,30,0,138,158,3,64,32,0,139,158,3,68,34,0,140,158,3,72,36,0,141,
  	158,3,76,38,0,142,158,3,8,4,0,143,158,3,80,40,0,144,158,3,12,6,0,145,
  	158,3,18,9,0,146,158,3,84,42,0,147,158,3,88,44,0,148,158,3,90,45,0,149,
  	158,3,92,46,0,150,158,3,94,47,0,151,158,3,96,48,0,152,158,3,98,49,0,153,
  	158,3,100,50,0,154,158,3,102,51,0,155,158,3,104,52,0,156,158,3,108,54,
  	0,157,120,1,0,0,0,157,122,1,0,0,0,157,126,1,0,0,0,157,127,1,0,0,0,157,
  	128,1,0,0,0,157,129,1,0,0,0,157,130,1,0,0,0,157,131,1,0,0,0,157,132,1,
  	0,0,0,157,133,1,0,0,0,157,134,1,0,0,0,157,135,1,0,0,0,157,136,1,0,0,0,
  	157,137,1,0,0,0,157,138,1,0,0,0,157,139,1,0,0,0,157,140,1,0,0,0,157,141,
  	1,0,0,0,157,142,1,0,0,0,157,143,1,0,0,0,157,144,1,0,0,0,157,145,1,0,0,
  	0,157,146,1,0,0,0,157,147,1,0,0,0,157,148,1,0,0,0,157,149,1,0,0,0,157,
  	150,1,0,0,0,157,151,1,0,0,0,157,152,1,0,0,0,157,153,1,0,0,0,157,154,1,
  	0,0,0,157,155,1,0,0,0,157,156,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,
  	159,160,1,0,0,0,160,162,1,0,0,0,161,159,1,0,0,0,162,163,5,0,0,1,163,1,
  	1,0,0,0,164,168,5,8,0,0,165,167,5,38,0,0,166,165,1,0,0,0,167,170,1,0,
  	0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,171,1,0,0,0,170,168,1,0,0,0,171,
  	172,7,0,0,0,172,3,1,0,0,0,173,175,3,6,3,0,174,173,1,0,0,0,175,176,1,0,
  	0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,5,1,0,0,0,178,179,3,114,57,0,
  	179,180,3,116,58,0,180,181,3,118,59,0,181,182,3,114,57,0,182,183,3,116,
  	58,0,183,184,3,118,59,0,184,186,3,112,56,0,185,187,3,112,56,0,186,185,
  	1,0,0,0,186,187,1,0,0,0,187,189,1,0,0,0,188,190,3,112,56,0,189,188,1,
  	0,0,0,189,190,1,0,0,0,190,192,1,0,0,0,191,193,3,112,56,0,192,191,1,0,
  	0,0,192,193,1,0,0,0,193,195,1,0,0,0,194,196,3,112,56,0,195,194,1,0,0,
  	0,195,196,1,0,0,0,196,198,1,0,0,0,197,199,3,112,56,0,198,197,1,0,0,0,
  	198,199,1,0,0,0,199,7,1,0,0,0,200,202,3,10,5,0,201,200,1,0,0,0,202,203,
  	1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,9,1,0,0,0,205,206,3,114,57,
  	0,206,207,3,116,58,0,207,208,3,116,58,0,208,209,3,112,56,0,209,211,3,
  	112,56,0,210,212,3,112,56,0,211,210,1,0,0,0,211,212,1,0,0,0,212,216,1,
  	0,0,0,213,214,5,16,0,0,214,215,5,17,0,0,215,217,5,2,0,0,216,213,1,0,0,
  	0,216,217,1,0,0,0,217,219,1,0,0,0,218,220,5,18,0,0,219,218,1,0,0,0,219,
  	220,1,0,0,0,220,11,1,0,0,0,221,223,3,14,7,0,222,221,1,0,0,0,223,224,1,
  	0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,229,1,0,0,0,226,230,5,5,0,0,
  	227,230,3,2,1,0,228,230,3,16,8,0,229,226,1,0,0,0,229,227,1,0,0,0,229,
  	228,1,0,0,0,230,231,1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,13,1,
  	0,0,0,233,234,5,2,0,0,234,235,3,112,56,0,235,236,3,112,56,0,236,237,7,
  	1,0,0,237,15,1,0,0,0,238,239,3,114,57,0,239,240,3,116,58,0,240,241,3,
  	116,58,0,241,242,3,114,57,0,242,243,3,116,58,0,243,244,3,116,58,0,244,
  	245,3,112,56,0,245,246,3,112,56,0,246,247,3,112,56,0,247,249,5,2,0,0,
  	248,250,3,112,56,0,249,248,1,0,0,0,249,250,1,0,0,0,250,17,1,0,0,0,251,
  	253,3,20,10,0,252,251,1,0,0,0,253,254,1,0,0,0,254,252,1,0,0,0,254,255,
  	1,0,0,0,255,259,1,0,0,0,256,260,5,5,0,0,257,260,3,2,1,0,258,260,3,22,
  	11,0,259,256,1,0,0,0,259,257,1,0,0,0,259,258,1,0,0,0,260,261,1,0,0,0,
  	261,259,1,0,0,0,261,262,1,0,0,0,262,19,1,0,0,0,263,264,5,2,0,0,264,265,
  	3,112,56,0,265,266,3,112,56,0,266,267,7,1,0,0,267,21,1,0,0,0,268,269,
  	3,114,57,0,269,270,3,116,58,0,270,271,3,116,58,0,271,272,3,112,56,0,272,
  	273,3,112,56,0,273,274,3,112,56,0,274,275,5,2,0,0,275,23,1,0,0,0,276,
  	278,3,26,13,0,277,276,1,0,0,0,278,279,1,0,0,0,279,277,1,0,0,0,279,280,
  	1,0,0,0,280,25,1,0,0,0,281,282,3,114,57,0,282,284,3,116,58,0,283,285,
  	3,2,1,0,284,283,1,0,0,0,284,285,1,0,0,0,285,293,1,0,0,0,286,287,3,116,
  	58,0,287,288,3,114,57,0,288,289,3,116,58,0,289,290,3,116,58,0,290,291,
  	3,112,56,0,291,294,1,0,0,0,292,294,3,2,1,0,293,286,1,0,0,0,293,292,1,
  	0,0,0,294,295,1,0,0,0,295,293,1,0,0,0,295,296,1,0,0,0,296,27,1,0,0,0,
  	297,299,3,30,15,0,298,297,1,0,0,0,299,300,1,0,0,0,300,298,1,0,0,0,300,
  	301,1,0,0,0,301,29,1,0,0,0,302,303,3,114,57,0,303,305,3,116,58,0,304,
  	306,3,2,1,0,305,304,1,0,0,0,305,306,1,0,0,0,306,315,1,0,0,0,307,308,3,
  	116,58,0,308,309,3,114,57,0,309,310,3,116,58,0,310,311,3,116,58,0,311,
  	312,3,112,56,0,312,313,3,112,56,0,313,316,1,0,0,0,314,316,3,2,1,0,315,
  	307,1,0,0,0,315,314,1,0,0,0,316,317,1,0,0,0,317,315,1,0,0,0,317,318,1,
  	0,0,0,318,31,1,0,0,0,319,321,3,34,17,0,320,319,1,0,0,0,321,322,1,0,0,
  	0,322,320,1,0,0,0,322,323,1,0,0,0,323,33,1,0,0,0,324,325,3,114,57,0,325,
  	327,3,116,58,0,326,328,3,2,1,0,327,326,1,0,0,0,327,328,1,0,0,0,328,338,
  	1,0,0,0,329,330,3,116,58,0,330,331,3,114,57,0,331,332,3,116,58,0,332,
  	333,3,116,58,0,333,334,3,112,56,0,334,335,3,112,56,0,335,336,3,112,56,
  	0,336,339,1,0,0,0,337,339,3,2,1,0,338,329,1,0,0,0,338,337,1,0,0,0,339,
  	340,1,0,0,0,340,338,1,0,0,0,340,341,1,0,0,0,341,35,1,0,0,0,342,344,3,
  	38,19,0,343,342,1,0,0,0,344,345,1,0,0,0,345,343,1,0,0,0,345,346,1,0,0,
  	0,346,37,1,0,0,0,347,348,3,114,57,0,348,349,3,116,58,0,349,351,3,116,
  	58,0,350,352,3,2,1,0,351,350,1,0,0,0,351,352,1,0,0,0,352,359,1,0,0,0,
  	353,354,3,114,57,0,354,355,3,116,58,0,355,356,3,116,58,0,356,357,3,112,
  	56,0,357,360,1,0,0,0,358,360,3,2,1,0,359,353,1,0,0,0,359,358,1,0,0,0,
  	360,361,1,0,0,0,361,359,1,0,0,0,361,362,1,0,0,0,362,39,1,0,0,0,363,365,
  	3,42,21,0,364,363,1,0,0,0,365,366,1,0,0,0,366,364,1,0,0,0,366,367,1,0,
  	0,0,367,41,1,0,0,0,368,369,3,114,57,0,369,370,3,116,58,0,370,372,3,116,
  	58,0,371,373,3,2,1,0,372,371,1,0,0,0,372,373,1,0,0,0,373,381,1,0,0,0,
  	374,375,3,114,57,0,375,376,3,116,58,0,376,377,3,116,58,0,377,378,3,112,
  	56,0,378,379,3,112,56,0,379,382,1,0,0,0,380,382,3,2,1,0,381,374,1,0,0,
  	0,381,380,1,0,0,0,382,383,1,0,0,0,383,381,1,0,0,0,383,384,1,0,0,0,384,
  	43,1,0,0,0,385,387,3,46,23,0,386,385,1,0,0,0,387,388,1,0,0,0,388,386,
  	1,0,0,0,388,389,1,0,0,0,389,45,1,0,0,0,390,391,3,114,57,0,391,392,3,116,
  	58,0,392,394,3,116,58,0,393,395,3,2,1,0,394,393,1,0,0,0,394,395,1,0,0,
  	0,395,404,1,0,0,0,396,397,3,114,57,0,397,398,3,116,58,0,398,399,3,116,
  	58,0,399,400,3,112,56,0,400,401,3,112,56,0,401,402,3,112,56,0,402,405,
  	1,0,0,0,403,405,3,2,1,0,404,396,1,0,0,0,404,403,1,0,0,0,405,406,1,0,0,
  	0,406,404,1,0,0,0,406,407,1,0,0,0,407,47,1,0,0,0,408,410,3,50,25,0,409,
  	408,1,0,0,0,410,411,1,0,0,0,411,409,1,0,0,0,411,412,1,0,0,0,412,49,1,
  	0,0,0,413,414,7,2,0,0,414,415,3,116,58,0,415,416,3,114,57,0,416,417,3,
  	116,58,0,417,418,3,116,58,0,418,419,3,114,57,0,419,420,3,116,58,0,420,
  	427,3,112,56,0,421,422,3,116,58,0,422,423,3,116,58,0,423,424,3,114,57,
  	0,424,425,3,116,58,0,425,426,3,112,56,0,426,428,1,0,0,0,427,421,1,0,0,
  	0,427,428,1,0,0,0,428,431,1,0,0,0,429,430,5,33,0,0,430,432,5,2,0,0,431,
  	429,1,0,0,0,431,432,1,0,0,0,432,51,1,0,0,0,433,435,3,54,27,0,434,433,
  	1,0,0,0,435,436,1,0,0,0,436,434,1,0,0,0,436,437,1,0,0,0,437,53,1,0,0,
  	0,438,439,7,3,0,0,439,440,3,116,58,0,440,441,3,114,57,0,441,442,3,116,
  	58,0,442,443,3,116,58,0,443,444,3,114,57,0,444,445,3,116,58,0,445,452,
  	3,112,56,0,446,447,3,116,58,0,447,448,3,116,58,0,448,449,3,114,57,0,449,
  	450,3,116,58,0,450,451,3,112,56,0,451,453,1,0,0,0,452,446,1,0,0,0,452,
  	453,1,0,0,0,453,456,1,0,0,0,454,455,5,33,0,0,455,457,5,2,0,0,456,454,
  	1,0,0,0,456,457,1,0,0,0,457,55,1,0,0,0,458,460,3,58,29,0,459,458,1,0,
  	0,0,460,461,1,0,0,0,461,459,1,0,0,0,461,462,1,0,0,0,462,57,1,0,0,0,463,
  	464,5,14,0,0,464,465,3,116,58,0,465,466,3,114,57,0,466,467,3,116,58,0,
  	467,468,3,112,56,0,468,471,3,112,56,0,469,470,5,33,0,0,470,472,5,2,0,
  	0,471,469,1,0,0,0,471,472,1,0,0,0,472,59,1,0,0,0,473,475,3,62,31,0,474,
  	473,1,0,0,0,475,476,1,0,0,0,476,474,1,0,0,0,476,477,1,0,0,0,477,61,1,
  	0,0,0,478,479,5,13,0,0,479,480,3,116,58,0,480,481,3,114,57,0,481,482,
  	3,116,58,0,482,483,3,116,58,0,483,486,3,112,56,0,484,485,5,33,0,0,485,
  	487,5,2,0,0,486,484,1,0,0,0,486,487,1,0,0,0,487,63,1,0,0,0,488,490,3,
  	66,33,0,489,488,1,0,0,0,490,491,1,0,0,0,491,489,1,0,0,0,491,492,1,0,0,
  	0,492,65,1,0,0,0,493,494,5,15,0,0,494,495,3,116,58,0,495,496,3,114,57,
  	0,496,497,3,116,58,0,497,503,3,112,56,0,498,499,3,116,58,0,499,500,3,
  	112,56,0,500,502,1,0,0,0,501,498,1,0,0,0,502,505,1,0,0,0,503,501,1,0,
  	0,0,503,504,1,0,0,0,504,508,1,0,0,0,505,503,1,0,0,0,506,507,5,33,0,0,
  	507,509,5,2,0,0,508,506,1,0,0,0,508,509,1,0,0,0,509,67,1,0,0,0,510,512,
  	3,70,35,0,511,510,1,0,0,0,512,513,1,0,0,0,513,511,1,0,0,0,513,514,1,0,
  	0,0,514,69,1,0,0,0,515,516,5,2,0,0,516,517,3,116,58,0,517,518,3,116,58,
  	0,518,519,3,116,58,0,519,520,5,2,0,0,520,521,3,116,58,0,521,522,3,116,
  	58,0,522,523,3,116,58,0,523,525,3,112,56,0,524,526,3,112,56,0,525,524,
  	1,0,0,0,525,526,1,0,0,0,526,528,1,0,0,0,527,529,3,112,56,0,528,527,1,
  	0,0,0,528,529,1,0,0,0,529,531,1,0,0,0,530,532,3,112,56,0,531,530,1,0,
  	0,0,531,532,1,0,0,0,532,534,1,0,0,0,533,535,3,112,56,0,534,533,1,0,0,
  	0,534,535,1,0,0,0,535,537,1,0,0,0,536,538,3,112,56,0,537,536,1,0,0,0,
  	537,538,1,0,0,0,538,71,1,0,0,0,539,541,3,74,37,0,540,539,1,0,0,0,541,
  	542,1,0,0,0,542,540,1,0,0,0,542,543,1,0,0,0,543,73,1,0,0,0,544,545,3,
  	116,58,0,545,546,5,2,0,0,546,547,3,116,58,0,547,548,3,116,58,0,548,549,
  	3,116,58,0,549,550,5,2,0,0,550,551,3,116,58,0,551,552,3,116,58,0,552,
  	554,3,112,56,0,553,555,3,112,56,0,554,553,1,0,0,0,554,555,1,0,0,0,555,
  	557,1,0,0,0,556,558,3,112,56,0,557,556,1,0,0,0,557,558,1,0,0,0,558,560,
  	1,0,0,0,559,561,3,112,56,0,560,559,1,0,0,0,560,561,1,0,0,0,561,563,1,
  	0,0,0,562,564,3,112,56,0,563,562,1,0,0,0,563,564,1,0,0,0,564,566,1,0,
  	0,0,565,567,3,112,56,0,566,565,1,0,0,0,566,567,1,0,0,0,567,75,1,0,0,0,
  	568,570,3,78,39,0,569,568,1,0,0,0,570,571,1,0,0,0,571,569,1,0,0,0,571,
  	572,1,0,0,0,572,77,1,0,0,0,573,574,3,116,58,0,574,575,3,116,58,0,575,
  	576,5,2,0,0,576,577,3,116,58,0,577,578,3,116,58,0,578,579,3,116,58,0,
  	579,580,5,2,0,0,580,581,3,116,58,0,581,583,3,112,56,0,582,584,3,112,56,
  	0,583,582,1,0,0,0,583,584,1,0,0,0,584,586,1,0,0,0,585,587,3,112,56,0,
  	586,585,1,0,0,0,586,587,1,0,0,0,587,589,1,0,0,0,588,590,3,112,56,0,589,
  	588,1,0,0,0,589,590,1,0,0,0,590,592,1,0,0,0,591,593,3,112,56,0,592,591,
  	1,0,0,0,592,593,1,0,0,0,593,595,1,0,0,0,594,596,3,112,56,0,595,594,1,
  	0,0,0,595,596,1,0,0,0,596,79,1,0,0,0,597,599,3,82,41,0,598,597,1,0,0,
  	0,599,600,1,0,0,0,600,598,1,0,0,0,600,601,1,0,0,0,601,81,1,0,0,0,602,
  	603,3,116,58,0,603,604,5,2,0,0,604,605,3,116,58,0,605,606,3,116,58,0,
  	606,607,3,112,56,0,607,609,3,112,56,0,608,610,3,112,56,0,609,608,1,0,
  	0,0,609,610,1,0,0,0,610,614,1,0,0,0,611,612,5,16,0,0,612,613,5,17,0,0,
  	613,615,5,2,0,0,614,611,1,0,0,0,614,615,1,0,0,0,615,617,1,0,0,0,616,618,
  	5,18,0,0,617,616,1,0,0,0,617,618,1,0,0,0,618,83,1,0,0,0,619,621,3,86,
  	43,0,620,619,1,0,0,0,621,622,1,0,0,0,622,620,1,0,0,0,622,623,1,0,0,0,
  	623,85,1,0,0,0,624,625,3,114,57,0,625,626,3,116,58,0,626,627,3,116,58,
  	0,627,628,3,116,58,0,628,630,3,112,56,0,629,631,3,112,56,0,630,629,1,
  	0,0,0,630,631,1,0,0,0,631,633,1,0,0,0,632,634,3,112,56,0,633,632,1,0,
  	0,0,633,634,1,0,0,0,634,636,1,0,0,0,635,637,3,112,56,0,636,635,1,0,0,
  	0,636,637,1,0,0,0,637,639,1,0,0,0,638,640,3,112,56,0,639,638,1,0,0,0,
  	639,640,1,0,0,0,640,642,1,0,0,0,641,643,3,112,56,0,642,641,1,0,0,0,642,
  	643,1,0,0,0,643,87,1,0,0,0,644,645,5,19,0,0,645,646,5,20,0,0,646,89,1,
  	0,0,0,647,650,5,21,0,0,648,649,5,41,0,0,649,651,5,45,0,0,650,648,1,0,
  	0,0,650,651,1,0,0,0,651,652,1,0,0,0,652,655,5,47,0,0,653,654,5,43,0,0,
  	654,656,5,45,0,0,655,653,1,0,0,0,655,656,1,0,0,0,656,657,1,0,0,0,657,
  	660,5,46,0,0,658,659,5,42,0,0,659,661,5,45,0,0,660,658,1,0,0,0,660,661,
  	1,0,0,0,661,662,1,0,0,0,662,665,5,47,0,0,663,664,5,44,0,0,664,666,5,45,
  	0,0,665,663,1,0,0,0,665,666,1,0,0,0,666,667,1,0,0,0,667,668,5,46,0,0,
  	668,669,5,49,0,0,669,91,1,0,0,0,670,671,5,22,0,0,671,672,3,116,58,0,672,
  	673,3,114,57,0,673,674,3,116,58,0,674,675,3,114,57,0,675,93,1,0,0,0,676,
  	677,5,23,0,0,677,678,5,51,0,0,678,679,5,53,0,0,679,95,1,0,0,0,680,684,
  	5,24,0,0,681,683,5,55,0,0,682,681,1,0,0,0,683,686,1,0,0,0,684,682,1,0,
  	0,0,684,685,1,0,0,0,685,687,1,0,0,0,686,684,1,0,0,0,687,688,5,57,0,0,
  	688,97,1,0,0,0,689,690,5,26,0,0,690,99,1,0,0,0,691,695,5,25,0,0,692,694,
  	5,55,0,0,693,692,1,0,0,0,694,697,1,0,0,0,695,693,1,0,0,0,695,696,1,0,
  	0,0,696,698,1,0,0,0,697,695,1,0,0,0,698,699,5,57,0,0,699,101,1,0,0,0,
  	700,701,5,27,0,0,701,702,5,51,0,0,702,703,5,53,0,0,703,103,1,0,0,0,704,
  	705,5,28,0,0,705,707,3,116,58,0,706,708,3,2,1,0,707,706,1,0,0,0,707,708,
  	1,0,0,0,708,711,1,0,0,0,709,712,3,106,53,0,710,712,3,2,1,0,711,709,1,
  	0,0,0,711,710,1,0,0,0,712,713,1,0,0,0,713,711,1,0,0,0,713,714,1,0,0,0,
  	714,105,1,0,0,0,715,716,5,29,0,0,716,717,5,61,0,0,717,719,5,62,0,0,718,
  	720,5,61,0,0,719,718,1,0,0,0,720,721,1,0,0,0,721,719,1,0,0,0,721,722,
  	1,0,0,0,722,723,1,0,0,0,723,724,5,64,0,0,724,107,1,0,0,0,725,726,5,28,
  	0,0,726,728,3,116,58,0,727,729,3,2,1,0,728,727,1,0,0,0,728,729,1,0,0,
  	0,729,732,1,0,0,0,730,733,3,110,55,0,731,733,3,2,1,0,732,730,1,0,0,0,
  	732,731,1,0,0,0,733,734,1,0,0,0,734,732,1,0,0,0,734,735,1,0,0,0,735,109,
  	1,0,0,0,736,737,5,30,0,0,737,738,7,4,0,0,738,741,5,62,0,0,739,740,5,61,
  	0,0,740,742,5,60,0,0,741,739,1,0,0,0,742,743,1,0,0,0,743,741,1,0,0,0,
  	743,744,1,0,0,0,744,745,1,0,0,0,745,746,5,64,0,0,746,111,1,0,0,0,747,
  	748,7,5,0,0,748,113,1,0,0,0,749,750,7,6,0,0,750,115,1,0,0,0,751,752,7,
  	7,0,0,752,117,1,0,0,0,753,754,7,8,0,0,754,119,1,0,0,0,100,124,157,159,
  	168,176,186,189,192,195,198,203,211,216,219,224,229,231,249,254,259,261,
  	279,284,293,295,300,305,315,317,322,327,338,340,345,351,359,361,366,372,
  	381,383,388,394,404,406,411,427,431,436,452,456,461,471,476,486,491,503,
  	508,513,525,528,531,534,537,542,554,557,560,563,566,571,583,586,589,592,
  	595,600,609,614,617,622,630,633,636,639,642,650,655,660,665,684,695,707,
  	711,713,721,728,732,734,743
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  cyanamrparserParserStaticData = std::move(staticData);
}

}

CyanaMRParser::CyanaMRParser(TokenStream *input) : CyanaMRParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

CyanaMRParser::CyanaMRParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  CyanaMRParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *cyanamrparserParserStaticData->atn, cyanamrparserParserStaticData->decisionToDFA, cyanamrparserParserStaticData->sharedContextCache, options);
}

CyanaMRParser::~CyanaMRParser() {
  delete _interpreter;
}

const atn::ATN& CyanaMRParser::getATN() const {
  return *cyanamrparserParserStaticData->atn;
}

std::string CyanaMRParser::getGrammarFileName() const {
  return "CyanaMRParser.g4";
}

const std::vector<std::string>& CyanaMRParser::getRuleNames() const {
  return cyanamrparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& CyanaMRParser::getVocabulary() const {
  return cyanamrparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView CyanaMRParser::getSerializedATN() const {
  return cyanamrparserParserStaticData->serializedATN;
}


//----------------- Cyana_mrContext ------------------------------------------------------------------

CyanaMRParser::Cyana_mrContext::Cyana_mrContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Cyana_mrContext::EOF() {
  return getToken(CyanaMRParser::EOF, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Cyana_mrContext::Orientation_header() {
  return getTokens(CyanaMRParser::Orientation_header);
}

tree::TerminalNode* CyanaMRParser::Cyana_mrContext::Orientation_header(size_t i) {
  return getToken(CyanaMRParser::Orientation_header, i);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Cyana_mrContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Cyana_mrContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::Distance_restraintsContext *> CyanaMRParser::Cyana_mrContext::distance_restraints() {
  return getRuleContexts<CyanaMRParser::Distance_restraintsContext>();
}

CyanaMRParser::Distance_restraintsContext* CyanaMRParser::Cyana_mrContext::distance_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Distance_restraintsContext>(i);
}

std::vector<CyanaMRParser::Fixres_distance_restraintsContext *> CyanaMRParser::Cyana_mrContext::fixres_distance_restraints() {
  return getRuleContexts<CyanaMRParser::Fixres_distance_restraintsContext>();
}

CyanaMRParser::Fixres_distance_restraintsContext* CyanaMRParser::Cyana_mrContext::fixres_distance_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Fixres_distance_restraintsContext>(i);
}

std::vector<CyanaMRParser::Fixresw_distance_restraintsContext *> CyanaMRParser::Cyana_mrContext::fixresw_distance_restraints() {
  return getRuleContexts<CyanaMRParser::Fixresw_distance_restraintsContext>();
}

CyanaMRParser::Fixresw_distance_restraintsContext* CyanaMRParser::Cyana_mrContext::fixresw_distance_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Fixresw_distance_restraintsContext>(i);
}

std::vector<CyanaMRParser::Fixresw2_distance_restraintsContext *> CyanaMRParser::Cyana_mrContext::fixresw2_distance_restraints() {
  return getRuleContexts<CyanaMRParser::Fixresw2_distance_restraintsContext>();
}

CyanaMRParser::Fixresw2_distance_restraintsContext* CyanaMRParser::Cyana_mrContext::fixresw2_distance_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Fixresw2_distance_restraintsContext>(i);
}

std::vector<CyanaMRParser::Fixatm_distance_restraintsContext *> CyanaMRParser::Cyana_mrContext::fixatm_distance_restraints() {
  return getRuleContexts<CyanaMRParser::Fixatm_distance_restraintsContext>();
}

CyanaMRParser::Fixatm_distance_restraintsContext* CyanaMRParser::Cyana_mrContext::fixatm_distance_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Fixatm_distance_restraintsContext>(i);
}

std::vector<CyanaMRParser::Fixatmw_distance_restraintsContext *> CyanaMRParser::Cyana_mrContext::fixatmw_distance_restraints() {
  return getRuleContexts<CyanaMRParser::Fixatmw_distance_restraintsContext>();
}

CyanaMRParser::Fixatmw_distance_restraintsContext* CyanaMRParser::Cyana_mrContext::fixatmw_distance_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Fixatmw_distance_restraintsContext>(i);
}

std::vector<CyanaMRParser::Fixatmw2_distance_restraintsContext *> CyanaMRParser::Cyana_mrContext::fixatmw2_distance_restraints() {
  return getRuleContexts<CyanaMRParser::Fixatmw2_distance_restraintsContext>();
}

CyanaMRParser::Fixatmw2_distance_restraintsContext* CyanaMRParser::Cyana_mrContext::fixatmw2_distance_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Fixatmw2_distance_restraintsContext>(i);
}

std::vector<CyanaMRParser::Diana_distance_restraintsContext *> CyanaMRParser::Cyana_mrContext::diana_distance_restraints() {
  return getRuleContexts<CyanaMRParser::Diana_distance_restraintsContext>();
}

CyanaMRParser::Diana_distance_restraintsContext* CyanaMRParser::Cyana_mrContext::diana_distance_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_distance_restraintsContext>(i);
}

std::vector<CyanaMRParser::Diana_ssbond_restraintsContext *> CyanaMRParser::Cyana_mrContext::diana_ssbond_restraints() {
  return getRuleContexts<CyanaMRParser::Diana_ssbond_restraintsContext>();
}

CyanaMRParser::Diana_ssbond_restraintsContext* CyanaMRParser::Cyana_mrContext::diana_ssbond_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_ssbond_restraintsContext>(i);
}

std::vector<CyanaMRParser::Diana_torsion_angle_restraintsContext *> CyanaMRParser::Cyana_mrContext::diana_torsion_angle_restraints() {
  return getRuleContexts<CyanaMRParser::Diana_torsion_angle_restraintsContext>();
}

CyanaMRParser::Diana_torsion_angle_restraintsContext* CyanaMRParser::Cyana_mrContext::diana_torsion_angle_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_torsion_angle_restraintsContext>(i);
}

std::vector<CyanaMRParser::Diana_coupling_constant_restraintsContext *> CyanaMRParser::Cyana_mrContext::diana_coupling_constant_restraints() {
  return getRuleContexts<CyanaMRParser::Diana_coupling_constant_restraintsContext>();
}

CyanaMRParser::Diana_coupling_constant_restraintsContext* CyanaMRParser::Cyana_mrContext::diana_coupling_constant_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_coupling_constant_restraintsContext>(i);
}

std::vector<CyanaMRParser::Diana_chemical_shiftsContext *> CyanaMRParser::Cyana_mrContext::diana_chemical_shifts() {
  return getRuleContexts<CyanaMRParser::Diana_chemical_shiftsContext>();
}

CyanaMRParser::Diana_chemical_shiftsContext* CyanaMRParser::Cyana_mrContext::diana_chemical_shifts(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_chemical_shiftsContext>(i);
}

std::vector<CyanaMRParser::Distance_w_chain_restraintsContext *> CyanaMRParser::Cyana_mrContext::distance_w_chain_restraints() {
  return getRuleContexts<CyanaMRParser::Distance_w_chain_restraintsContext>();
}

CyanaMRParser::Distance_w_chain_restraintsContext* CyanaMRParser::Cyana_mrContext::distance_w_chain_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Distance_w_chain_restraintsContext>(i);
}

std::vector<CyanaMRParser::Distance_w_chain2_restraintsContext *> CyanaMRParser::Cyana_mrContext::distance_w_chain2_restraints() {
  return getRuleContexts<CyanaMRParser::Distance_w_chain2_restraintsContext>();
}

CyanaMRParser::Distance_w_chain2_restraintsContext* CyanaMRParser::Cyana_mrContext::distance_w_chain2_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Distance_w_chain2_restraintsContext>(i);
}

std::vector<CyanaMRParser::Distance_w_chain3_restraintsContext *> CyanaMRParser::Cyana_mrContext::distance_w_chain3_restraints() {
  return getRuleContexts<CyanaMRParser::Distance_w_chain3_restraintsContext>();
}

CyanaMRParser::Distance_w_chain3_restraintsContext* CyanaMRParser::Cyana_mrContext::distance_w_chain3_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Distance_w_chain3_restraintsContext>(i);
}

std::vector<CyanaMRParser::Torsion_angle_restraintsContext *> CyanaMRParser::Cyana_mrContext::torsion_angle_restraints() {
  return getRuleContexts<CyanaMRParser::Torsion_angle_restraintsContext>();
}

CyanaMRParser::Torsion_angle_restraintsContext* CyanaMRParser::Cyana_mrContext::torsion_angle_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Torsion_angle_restraintsContext>(i);
}

std::vector<CyanaMRParser::Torsion_angle_w_chain_restraintsContext *> CyanaMRParser::Cyana_mrContext::torsion_angle_w_chain_restraints() {
  return getRuleContexts<CyanaMRParser::Torsion_angle_w_chain_restraintsContext>();
}

CyanaMRParser::Torsion_angle_w_chain_restraintsContext* CyanaMRParser::Cyana_mrContext::torsion_angle_w_chain_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Torsion_angle_w_chain_restraintsContext>(i);
}

std::vector<CyanaMRParser::Rdc_restraintsContext *> CyanaMRParser::Cyana_mrContext::rdc_restraints() {
  return getRuleContexts<CyanaMRParser::Rdc_restraintsContext>();
}

CyanaMRParser::Rdc_restraintsContext* CyanaMRParser::Cyana_mrContext::rdc_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Rdc_restraintsContext>(i);
}

std::vector<CyanaMRParser::Pcs_restraintsContext *> CyanaMRParser::Cyana_mrContext::pcs_restraints() {
  return getRuleContexts<CyanaMRParser::Pcs_restraintsContext>();
}

CyanaMRParser::Pcs_restraintsContext* CyanaMRParser::Cyana_mrContext::pcs_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Pcs_restraintsContext>(i);
}

std::vector<CyanaMRParser::Cco_restraintsContext *> CyanaMRParser::Cyana_mrContext::cco_restraints() {
  return getRuleContexts<CyanaMRParser::Cco_restraintsContext>();
}

CyanaMRParser::Cco_restraintsContext* CyanaMRParser::Cyana_mrContext::cco_restraints(size_t i) {
  return getRuleContext<CyanaMRParser::Cco_restraintsContext>(i);
}

std::vector<CyanaMRParser::Ssbond_macroContext *> CyanaMRParser::Cyana_mrContext::ssbond_macro() {
  return getRuleContexts<CyanaMRParser::Ssbond_macroContext>();
}

CyanaMRParser::Ssbond_macroContext* CyanaMRParser::Cyana_mrContext::ssbond_macro(size_t i) {
  return getRuleContext<CyanaMRParser::Ssbond_macroContext>(i);
}

std::vector<CyanaMRParser::Hbond_macroContext *> CyanaMRParser::Cyana_mrContext::hbond_macro() {
  return getRuleContexts<CyanaMRParser::Hbond_macroContext>();
}

CyanaMRParser::Hbond_macroContext* CyanaMRParser::Cyana_mrContext::hbond_macro(size_t i) {
  return getRuleContext<CyanaMRParser::Hbond_macroContext>(i);
}

std::vector<CyanaMRParser::Link_statementContext *> CyanaMRParser::Cyana_mrContext::link_statement() {
  return getRuleContexts<CyanaMRParser::Link_statementContext>();
}

CyanaMRParser::Link_statementContext* CyanaMRParser::Cyana_mrContext::link_statement(size_t i) {
  return getRuleContext<CyanaMRParser::Link_statementContext>(i);
}

std::vector<CyanaMRParser::Stereoassign_macroContext *> CyanaMRParser::Cyana_mrContext::stereoassign_macro() {
  return getRuleContexts<CyanaMRParser::Stereoassign_macroContext>();
}

CyanaMRParser::Stereoassign_macroContext* CyanaMRParser::Cyana_mrContext::stereoassign_macro(size_t i) {
  return getRuleContext<CyanaMRParser::Stereoassign_macroContext>(i);
}

std::vector<CyanaMRParser::Declare_variableContext *> CyanaMRParser::Cyana_mrContext::declare_variable() {
  return getRuleContexts<CyanaMRParser::Declare_variableContext>();
}

CyanaMRParser::Declare_variableContext* CyanaMRParser::Cyana_mrContext::declare_variable(size_t i) {
  return getRuleContext<CyanaMRParser::Declare_variableContext>(i);
}

std::vector<CyanaMRParser::Set_variableContext *> CyanaMRParser::Cyana_mrContext::set_variable() {
  return getRuleContexts<CyanaMRParser::Set_variableContext>();
}

CyanaMRParser::Set_variableContext* CyanaMRParser::Cyana_mrContext::set_variable(size_t i) {
  return getRuleContext<CyanaMRParser::Set_variableContext>(i);
}

std::vector<CyanaMRParser::Unset_variableContext *> CyanaMRParser::Cyana_mrContext::unset_variable() {
  return getRuleContexts<CyanaMRParser::Unset_variableContext>();
}

CyanaMRParser::Unset_variableContext* CyanaMRParser::Cyana_mrContext::unset_variable(size_t i) {
  return getRuleContext<CyanaMRParser::Unset_variableContext>(i);
}

std::vector<CyanaMRParser::Print_macroContext *> CyanaMRParser::Cyana_mrContext::print_macro() {
  return getRuleContexts<CyanaMRParser::Print_macroContext>();
}

CyanaMRParser::Print_macroContext* CyanaMRParser::Cyana_mrContext::print_macro(size_t i) {
  return getRuleContext<CyanaMRParser::Print_macroContext>(i);
}

std::vector<CyanaMRParser::Unambig_atom_name_mappingContext *> CyanaMRParser::Cyana_mrContext::unambig_atom_name_mapping() {
  return getRuleContexts<CyanaMRParser::Unambig_atom_name_mappingContext>();
}

CyanaMRParser::Unambig_atom_name_mappingContext* CyanaMRParser::Cyana_mrContext::unambig_atom_name_mapping(size_t i) {
  return getRuleContext<CyanaMRParser::Unambig_atom_name_mappingContext>(i);
}

std::vector<CyanaMRParser::Ambig_atom_name_mappingContext *> CyanaMRParser::Cyana_mrContext::ambig_atom_name_mapping() {
  return getRuleContexts<CyanaMRParser::Ambig_atom_name_mappingContext>();
}

CyanaMRParser::Ambig_atom_name_mappingContext* CyanaMRParser::Cyana_mrContext::ambig_atom_name_mapping(size_t i) {
  return getRuleContext<CyanaMRParser::Ambig_atom_name_mappingContext>(i);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Cyana_mrContext::Tensor_header() {
  return getTokens(CyanaMRParser::Tensor_header);
}

tree::TerminalNode* CyanaMRParser::Cyana_mrContext::Tensor_header(size_t i) {
  return getToken(CyanaMRParser::Tensor_header, i);
}


size_t CyanaMRParser::Cyana_mrContext::getRuleIndex() const {
  return CyanaMRParser::RuleCyana_mr;
}


std::any CyanaMRParser::Cyana_mrContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitCyana_mr(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Cyana_mrContext* CyanaMRParser::cyana_mr() {
  Cyana_mrContext *_localctx = _tracker.createInstance<Cyana_mrContext>(_ctx, getState());
  enterRule(_localctx, 0, CyanaMRParser::RuleCyana_mr);
  size_t _la = 0;

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
    setState(159);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 15567748964) != 0)) {
      setState(157);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx)) {
      case 1: {
        setState(120);
        match(CyanaMRParser::Orientation_header);
        break;
      }

      case 2: {
        setState(122); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(121);
                  match(CyanaMRParser::Tensor_header);
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(124); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 3: {
        setState(126);
        comment();
        break;
      }

      case 4: {
        setState(127);
        distance_restraints();
        break;
      }

      case 5: {
        setState(128);
        fixres_distance_restraints();
        break;
      }

      case 6: {
        setState(129);
        fixresw_distance_restraints();
        break;
      }

      case 7: {
        setState(130);
        fixresw2_distance_restraints();
        break;
      }

      case 8: {
        setState(131);
        fixatm_distance_restraints();
        break;
      }

      case 9: {
        setState(132);
        fixatmw_distance_restraints();
        break;
      }

      case 10: {
        setState(133);
        fixatmw2_distance_restraints();
        break;
      }

      case 11: {
        setState(134);
        diana_distance_restraints();
        break;
      }

      case 12: {
        setState(135);
        diana_ssbond_restraints();
        break;
      }

      case 13: {
        setState(136);
        diana_torsion_angle_restraints();
        break;
      }

      case 14: {
        setState(137);
        diana_coupling_constant_restraints();
        break;
      }

      case 15: {
        setState(138);
        diana_chemical_shifts();
        break;
      }

      case 16: {
        setState(139);
        distance_w_chain_restraints();
        break;
      }

      case 17: {
        setState(140);
        distance_w_chain2_restraints();
        break;
      }

      case 18: {
        setState(141);
        distance_w_chain3_restraints();
        break;
      }

      case 19: {
        setState(142);
        torsion_angle_restraints();
        break;
      }

      case 20: {
        setState(143);
        torsion_angle_w_chain_restraints();
        break;
      }

      case 21: {
        setState(144);
        rdc_restraints();
        break;
      }

      case 22: {
        setState(145);
        pcs_restraints();
        break;
      }

      case 23: {
        setState(146);
        cco_restraints();
        break;
      }

      case 24: {
        setState(147);
        ssbond_macro();
        break;
      }

      case 25: {
        setState(148);
        hbond_macro();
        break;
      }

      case 26: {
        setState(149);
        link_statement();
        break;
      }

      case 27: {
        setState(150);
        stereoassign_macro();
        break;
      }

      case 28: {
        setState(151);
        declare_variable();
        break;
      }

      case 29: {
        setState(152);
        set_variable();
        break;
      }

      case 30: {
        setState(153);
        unset_variable();
        break;
      }

      case 31: {
        setState(154);
        print_macro();
        break;
      }

      case 32: {
        setState(155);
        unambig_atom_name_mapping();
        break;
      }

      case 33: {
        setState(156);
        ambig_atom_name_mapping();
        break;
      }

      default:
        break;
      }
      setState(161);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(162);
    match(CyanaMRParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- CommentContext ------------------------------------------------------------------

CyanaMRParser::CommentContext::CommentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::CommentContext::COMMENT() {
  return getToken(CyanaMRParser::COMMENT, 0);
}

tree::TerminalNode* CyanaMRParser::CommentContext::RETURN_CM() {
  return getToken(CyanaMRParser::RETURN_CM, 0);
}

tree::TerminalNode* CyanaMRParser::CommentContext::EOF() {
  return getToken(CyanaMRParser::EOF, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::CommentContext::Any_name() {
  return getTokens(CyanaMRParser::Any_name);
}

tree::TerminalNode* CyanaMRParser::CommentContext::Any_name(size_t i) {
  return getToken(CyanaMRParser::Any_name, i);
}


size_t CyanaMRParser::CommentContext::getRuleIndex() const {
  return CyanaMRParser::RuleComment;
}


std::any CyanaMRParser::CommentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitComment(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::CommentContext* CyanaMRParser::comment() {
  CommentContext *_localctx = _tracker.createInstance<CommentContext>(_ctx, getState());
  enterRule(_localctx, 2, CyanaMRParser::RuleComment);
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
    setState(164);
    match(CyanaMRParser::COMMENT);
    setState(168);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CyanaMRParser::Any_name) {
      setState(165);
      match(CyanaMRParser::Any_name);
      setState(170);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(171);
    _la = _input->LA(1);
    if (!(_la == CyanaMRParser::EOF

    || _la == CyanaMRParser::RETURN_CM)) {
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

//----------------- Distance_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Distance_restraintsContext::Distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Distance_restraintContext *> CyanaMRParser::Distance_restraintsContext::distance_restraint() {
  return getRuleContexts<CyanaMRParser::Distance_restraintContext>();
}

CyanaMRParser::Distance_restraintContext* CyanaMRParser::Distance_restraintsContext::distance_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Distance_restraintContext>(i);
}


size_t CyanaMRParser::Distance_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleDistance_restraints;
}


std::any CyanaMRParser::Distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Distance_restraintsContext* CyanaMRParser::distance_restraints() {
  Distance_restraintsContext *_localctx = _tracker.createInstance<Distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 4, CyanaMRParser::RuleDistance_restraints);

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
    setState(174); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(173);
              distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(176); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 4, _ctx);
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

CyanaMRParser::Distance_restraintContext::Distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Distance_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Distance_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Distance_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Distance_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::Gen_atom_nameContext *> CyanaMRParser::Distance_restraintContext::gen_atom_name() {
  return getRuleContexts<CyanaMRParser::Gen_atom_nameContext>();
}

CyanaMRParser::Gen_atom_nameContext* CyanaMRParser::Distance_restraintContext::gen_atom_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_atom_nameContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Distance_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Distance_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Distance_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleDistance_restraint;
}


std::any CyanaMRParser::Distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Distance_restraintContext* CyanaMRParser::distance_restraint() {
  Distance_restraintContext *_localctx = _tracker.createInstance<Distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 6, CyanaMRParser::RuleDistance_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(178);
    gen_res_num();
    setState(179);
    gen_simple_name();
    setState(180);
    gen_atom_name();
    setState(181);
    gen_res_num();
    setState(182);
    gen_simple_name();
    setState(183);
    gen_atom_name();
    setState(184);
    number();
    setState(186);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 5, _ctx)) {
    case 1: {
      setState(185);
      number();
      break;
    }

    default:
      break;
    }
    setState(189);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 6, _ctx)) {
    case 1: {
      setState(188);
      number();
      break;
    }

    default:
      break;
    }
    setState(192);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 7, _ctx)) {
    case 1: {
      setState(191);
      number();
      break;
    }

    default:
      break;
    }
    setState(195);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 8, _ctx)) {
    case 1: {
      setState(194);
      number();
      break;
    }

    default:
      break;
    }
    setState(198);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 9, _ctx)) {
    case 1: {
      setState(197);
      number();
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

//----------------- Torsion_angle_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Torsion_angle_restraintsContext::Torsion_angle_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Torsion_angle_restraintContext *> CyanaMRParser::Torsion_angle_restraintsContext::torsion_angle_restraint() {
  return getRuleContexts<CyanaMRParser::Torsion_angle_restraintContext>();
}

CyanaMRParser::Torsion_angle_restraintContext* CyanaMRParser::Torsion_angle_restraintsContext::torsion_angle_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Torsion_angle_restraintContext>(i);
}


size_t CyanaMRParser::Torsion_angle_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleTorsion_angle_restraints;
}


std::any CyanaMRParser::Torsion_angle_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitTorsion_angle_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Torsion_angle_restraintsContext* CyanaMRParser::torsion_angle_restraints() {
  Torsion_angle_restraintsContext *_localctx = _tracker.createInstance<Torsion_angle_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 8, CyanaMRParser::RuleTorsion_angle_restraints);

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
    setState(201); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(200);
              torsion_angle_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(203); 
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

//----------------- Torsion_angle_restraintContext ------------------------------------------------------------------

CyanaMRParser::Torsion_angle_restraintContext::Torsion_angle_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Torsion_angle_restraintContext::gen_res_num() {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(0);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Torsion_angle_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Torsion_angle_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Torsion_angle_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Torsion_angle_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Torsion_angle_restraintContext::Type() {
  return getToken(CyanaMRParser::Type, 0);
}

tree::TerminalNode* CyanaMRParser::Torsion_angle_restraintContext::Equ_op() {
  return getToken(CyanaMRParser::Equ_op, 0);
}

tree::TerminalNode* CyanaMRParser::Torsion_angle_restraintContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}

tree::TerminalNode* CyanaMRParser::Torsion_angle_restraintContext::Or() {
  return getToken(CyanaMRParser::Or, 0);
}


size_t CyanaMRParser::Torsion_angle_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleTorsion_angle_restraint;
}


std::any CyanaMRParser::Torsion_angle_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitTorsion_angle_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Torsion_angle_restraintContext* CyanaMRParser::torsion_angle_restraint() {
  Torsion_angle_restraintContext *_localctx = _tracker.createInstance<Torsion_angle_restraintContext>(_ctx, getState());
  enterRule(_localctx, 10, CyanaMRParser::RuleTorsion_angle_restraint);
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
    setState(205);
    gen_res_num();
    setState(206);
    gen_simple_name();
    setState(207);
    gen_simple_name();
    setState(208);
    number();
    setState(209);
    number();
    setState(211);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 11, _ctx)) {
    case 1: {
      setState(210);
      number();
      break;
    }

    default:
      break;
    }
    setState(216);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Type) {
      setState(213);
      match(CyanaMRParser::Type);
      setState(214);
      match(CyanaMRParser::Equ_op);
      setState(215);
      match(CyanaMRParser::Integer);
    }
    setState(219);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Or) {
      setState(218);
      match(CyanaMRParser::Or);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Rdc_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Rdc_restraintsContext::Rdc_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Rdc_parameterContext *> CyanaMRParser::Rdc_restraintsContext::rdc_parameter() {
  return getRuleContexts<CyanaMRParser::Rdc_parameterContext>();
}

CyanaMRParser::Rdc_parameterContext* CyanaMRParser::Rdc_restraintsContext::rdc_parameter(size_t i) {
  return getRuleContext<CyanaMRParser::Rdc_parameterContext>(i);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Rdc_restraintsContext::Orientation_header() {
  return getTokens(CyanaMRParser::Orientation_header);
}

tree::TerminalNode* CyanaMRParser::Rdc_restraintsContext::Orientation_header(size_t i) {
  return getToken(CyanaMRParser::Orientation_header, i);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Rdc_restraintsContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Rdc_restraintsContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::Rdc_restraintContext *> CyanaMRParser::Rdc_restraintsContext::rdc_restraint() {
  return getRuleContexts<CyanaMRParser::Rdc_restraintContext>();
}

CyanaMRParser::Rdc_restraintContext* CyanaMRParser::Rdc_restraintsContext::rdc_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Rdc_restraintContext>(i);
}


size_t CyanaMRParser::Rdc_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleRdc_restraints;
}


std::any CyanaMRParser::Rdc_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitRdc_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Rdc_restraintsContext* CyanaMRParser::rdc_restraints() {
  Rdc_restraintsContext *_localctx = _tracker.createInstance<Rdc_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 12, CyanaMRParser::RuleRdc_restraints);

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
    setState(222); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(221);
              rdc_parameter();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(224); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 14, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(229); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(229);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Orientation_header: {
                  setState(226);
                  match(CyanaMRParser::Orientation_header);
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(227);
                  comment();
                  break;
                }

                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(228);
                  rdc_restraint();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(231); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 16, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Rdc_parameterContext ------------------------------------------------------------------

CyanaMRParser::Rdc_parameterContext::Rdc_parameterContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> CyanaMRParser::Rdc_parameterContext::Integer() {
  return getTokens(CyanaMRParser::Integer);
}

tree::TerminalNode* CyanaMRParser::Rdc_parameterContext::Integer(size_t i) {
  return getToken(CyanaMRParser::Integer, i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Rdc_parameterContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Rdc_parameterContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Rdc_parameterContext::Capital_integer() {
  return getToken(CyanaMRParser::Capital_integer, 0);
}

tree::TerminalNode* CyanaMRParser::Rdc_parameterContext::Integer_capital() {
  return getToken(CyanaMRParser::Integer_capital, 0);
}

tree::TerminalNode* CyanaMRParser::Rdc_parameterContext::Simple_name() {
  return getToken(CyanaMRParser::Simple_name, 0);
}


size_t CyanaMRParser::Rdc_parameterContext::getRuleIndex() const {
  return CyanaMRParser::RuleRdc_parameter;
}


std::any CyanaMRParser::Rdc_parameterContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitRdc_parameter(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Rdc_parameterContext* CyanaMRParser::rdc_parameter() {
  Rdc_parameterContext *_localctx = _tracker.createInstance<Rdc_parameterContext>(_ctx, getState());
  enterRule(_localctx, 14, CyanaMRParser::RuleRdc_parameter);
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
    setState(233);
    match(CyanaMRParser::Integer);
    setState(234);
    number();
    setState(235);
    number();
    setState(236);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 15032385540) != 0))) {
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

//----------------- Rdc_restraintContext ------------------------------------------------------------------

CyanaMRParser::Rdc_restraintContext::Rdc_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Rdc_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Rdc_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Rdc_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Rdc_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Rdc_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Rdc_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Rdc_restraintContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}


size_t CyanaMRParser::Rdc_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleRdc_restraint;
}


std::any CyanaMRParser::Rdc_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitRdc_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Rdc_restraintContext* CyanaMRParser::rdc_restraint() {
  Rdc_restraintContext *_localctx = _tracker.createInstance<Rdc_restraintContext>(_ctx, getState());
  enterRule(_localctx, 16, CyanaMRParser::RuleRdc_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(238);
    gen_res_num();
    setState(239);
    gen_simple_name();
    setState(240);
    gen_simple_name();
    setState(241);
    gen_res_num();
    setState(242);
    gen_simple_name();
    setState(243);
    gen_simple_name();
    setState(244);
    number();
    setState(245);
    number();
    setState(246);
    number();
    setState(247);
    match(CyanaMRParser::Integer);
    setState(249);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 17, _ctx)) {
    case 1: {
      setState(248);
      number();
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

//----------------- Pcs_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Pcs_restraintsContext::Pcs_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Pcs_parameterContext *> CyanaMRParser::Pcs_restraintsContext::pcs_parameter() {
  return getRuleContexts<CyanaMRParser::Pcs_parameterContext>();
}

CyanaMRParser::Pcs_parameterContext* CyanaMRParser::Pcs_restraintsContext::pcs_parameter(size_t i) {
  return getRuleContext<CyanaMRParser::Pcs_parameterContext>(i);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Pcs_restraintsContext::Orientation_header() {
  return getTokens(CyanaMRParser::Orientation_header);
}

tree::TerminalNode* CyanaMRParser::Pcs_restraintsContext::Orientation_header(size_t i) {
  return getToken(CyanaMRParser::Orientation_header, i);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Pcs_restraintsContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Pcs_restraintsContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::Pcs_restraintContext *> CyanaMRParser::Pcs_restraintsContext::pcs_restraint() {
  return getRuleContexts<CyanaMRParser::Pcs_restraintContext>();
}

CyanaMRParser::Pcs_restraintContext* CyanaMRParser::Pcs_restraintsContext::pcs_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Pcs_restraintContext>(i);
}


size_t CyanaMRParser::Pcs_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RulePcs_restraints;
}


std::any CyanaMRParser::Pcs_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitPcs_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Pcs_restraintsContext* CyanaMRParser::pcs_restraints() {
  Pcs_restraintsContext *_localctx = _tracker.createInstance<Pcs_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 18, CyanaMRParser::RulePcs_restraints);

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
    setState(252); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(251);
              pcs_parameter();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(254); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 18, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(259); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(259);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Orientation_header: {
                  setState(256);
                  match(CyanaMRParser::Orientation_header);
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(257);
                  comment();
                  break;
                }

                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(258);
                  pcs_restraint();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(261); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 20, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Pcs_parameterContext ------------------------------------------------------------------

CyanaMRParser::Pcs_parameterContext::Pcs_parameterContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> CyanaMRParser::Pcs_parameterContext::Integer() {
  return getTokens(CyanaMRParser::Integer);
}

tree::TerminalNode* CyanaMRParser::Pcs_parameterContext::Integer(size_t i) {
  return getToken(CyanaMRParser::Integer, i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Pcs_parameterContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Pcs_parameterContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Pcs_parameterContext::Capital_integer() {
  return getToken(CyanaMRParser::Capital_integer, 0);
}

tree::TerminalNode* CyanaMRParser::Pcs_parameterContext::Integer_capital() {
  return getToken(CyanaMRParser::Integer_capital, 0);
}

tree::TerminalNode* CyanaMRParser::Pcs_parameterContext::Simple_name() {
  return getToken(CyanaMRParser::Simple_name, 0);
}


size_t CyanaMRParser::Pcs_parameterContext::getRuleIndex() const {
  return CyanaMRParser::RulePcs_parameter;
}


std::any CyanaMRParser::Pcs_parameterContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitPcs_parameter(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Pcs_parameterContext* CyanaMRParser::pcs_parameter() {
  Pcs_parameterContext *_localctx = _tracker.createInstance<Pcs_parameterContext>(_ctx, getState());
  enterRule(_localctx, 20, CyanaMRParser::RulePcs_parameter);
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
    setState(263);
    match(CyanaMRParser::Integer);
    setState(264);
    number();
    setState(265);
    number();
    setState(266);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 15032385540) != 0))) {
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

//----------------- Pcs_restraintContext ------------------------------------------------------------------

CyanaMRParser::Pcs_restraintContext::Pcs_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Pcs_restraintContext::gen_res_num() {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(0);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Pcs_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Pcs_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Pcs_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Pcs_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Pcs_restraintContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}


size_t CyanaMRParser::Pcs_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RulePcs_restraint;
}


std::any CyanaMRParser::Pcs_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitPcs_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Pcs_restraintContext* CyanaMRParser::pcs_restraint() {
  Pcs_restraintContext *_localctx = _tracker.createInstance<Pcs_restraintContext>(_ctx, getState());
  enterRule(_localctx, 22, CyanaMRParser::RulePcs_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(268);
    gen_res_num();
    setState(269);
    gen_simple_name();
    setState(270);
    gen_simple_name();
    setState(271);
    number();
    setState(272);
    number();
    setState(273);
    number();
    setState(274);
    match(CyanaMRParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixres_distance_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Fixres_distance_restraintsContext::Fixres_distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Fixres_distance_restraintContext *> CyanaMRParser::Fixres_distance_restraintsContext::fixres_distance_restraint() {
  return getRuleContexts<CyanaMRParser::Fixres_distance_restraintContext>();
}

CyanaMRParser::Fixres_distance_restraintContext* CyanaMRParser::Fixres_distance_restraintsContext::fixres_distance_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Fixres_distance_restraintContext>(i);
}


size_t CyanaMRParser::Fixres_distance_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixres_distance_restraints;
}


std::any CyanaMRParser::Fixres_distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixres_distance_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixres_distance_restraintsContext* CyanaMRParser::fixres_distance_restraints() {
  Fixres_distance_restraintsContext *_localctx = _tracker.createInstance<Fixres_distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 24, CyanaMRParser::RuleFixres_distance_restraints);

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
    setState(277); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(276);
              fixres_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(279); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 21, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixres_distance_restraintContext ------------------------------------------------------------------

CyanaMRParser::Fixres_distance_restraintContext::Fixres_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Fixres_distance_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Fixres_distance_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Fixres_distance_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Fixres_distance_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Fixres_distance_restraintContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Fixres_distance_restraintContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Fixres_distance_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Fixres_distance_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Fixres_distance_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixres_distance_restraint;
}


std::any CyanaMRParser::Fixres_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixres_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixres_distance_restraintContext* CyanaMRParser::fixres_distance_restraint() {
  Fixres_distance_restraintContext *_localctx = _tracker.createInstance<Fixres_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 26, CyanaMRParser::RuleFixres_distance_restraint);

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
    setState(281);
    gen_res_num();
    setState(282);
    gen_simple_name();
    setState(284);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 22, _ctx)) {
    case 1: {
      setState(283);
      comment();
      break;
    }

    default:
      break;
    }
    setState(293); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(293);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital:
                case CyanaMRParser::Simple_name: {
                  setState(286);
                  gen_simple_name();
                  setState(287);
                  gen_res_num();
                  setState(288);
                  gen_simple_name();
                  setState(289);
                  gen_simple_name();
                  setState(290);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(292);
                  comment();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(295); 
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

//----------------- Fixresw_distance_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Fixresw_distance_restraintsContext::Fixresw_distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Fixresw_distance_restraintContext *> CyanaMRParser::Fixresw_distance_restraintsContext::fixresw_distance_restraint() {
  return getRuleContexts<CyanaMRParser::Fixresw_distance_restraintContext>();
}

CyanaMRParser::Fixresw_distance_restraintContext* CyanaMRParser::Fixresw_distance_restraintsContext::fixresw_distance_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Fixresw_distance_restraintContext>(i);
}


size_t CyanaMRParser::Fixresw_distance_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixresw_distance_restraints;
}


std::any CyanaMRParser::Fixresw_distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixresw_distance_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixresw_distance_restraintsContext* CyanaMRParser::fixresw_distance_restraints() {
  Fixresw_distance_restraintsContext *_localctx = _tracker.createInstance<Fixresw_distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 28, CyanaMRParser::RuleFixresw_distance_restraints);

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
    setState(298); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(297);
              fixresw_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(300); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 25, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixresw_distance_restraintContext ------------------------------------------------------------------

CyanaMRParser::Fixresw_distance_restraintContext::Fixresw_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Fixresw_distance_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Fixresw_distance_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Fixresw_distance_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Fixresw_distance_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Fixresw_distance_restraintContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Fixresw_distance_restraintContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Fixresw_distance_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Fixresw_distance_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Fixresw_distance_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixresw_distance_restraint;
}


std::any CyanaMRParser::Fixresw_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixresw_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixresw_distance_restraintContext* CyanaMRParser::fixresw_distance_restraint() {
  Fixresw_distance_restraintContext *_localctx = _tracker.createInstance<Fixresw_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 30, CyanaMRParser::RuleFixresw_distance_restraint);

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
    setState(302);
    gen_res_num();
    setState(303);
    gen_simple_name();
    setState(305);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 26, _ctx)) {
    case 1: {
      setState(304);
      comment();
      break;
    }

    default:
      break;
    }
    setState(315); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(315);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital:
                case CyanaMRParser::Simple_name: {
                  setState(307);
                  gen_simple_name();
                  setState(308);
                  gen_res_num();
                  setState(309);
                  gen_simple_name();
                  setState(310);
                  gen_simple_name();
                  setState(311);
                  number();
                  setState(312);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(314);
                  comment();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(317); 
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

//----------------- Fixresw2_distance_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Fixresw2_distance_restraintsContext::Fixresw2_distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Fixresw2_distance_restraintContext *> CyanaMRParser::Fixresw2_distance_restraintsContext::fixresw2_distance_restraint() {
  return getRuleContexts<CyanaMRParser::Fixresw2_distance_restraintContext>();
}

CyanaMRParser::Fixresw2_distance_restraintContext* CyanaMRParser::Fixresw2_distance_restraintsContext::fixresw2_distance_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Fixresw2_distance_restraintContext>(i);
}


size_t CyanaMRParser::Fixresw2_distance_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixresw2_distance_restraints;
}


std::any CyanaMRParser::Fixresw2_distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixresw2_distance_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixresw2_distance_restraintsContext* CyanaMRParser::fixresw2_distance_restraints() {
  Fixresw2_distance_restraintsContext *_localctx = _tracker.createInstance<Fixresw2_distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 32, CyanaMRParser::RuleFixresw2_distance_restraints);

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
    setState(320); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(319);
              fixresw2_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(322); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 29, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixresw2_distance_restraintContext ------------------------------------------------------------------

CyanaMRParser::Fixresw2_distance_restraintContext::Fixresw2_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Fixresw2_distance_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Fixresw2_distance_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Fixresw2_distance_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Fixresw2_distance_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Fixresw2_distance_restraintContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Fixresw2_distance_restraintContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Fixresw2_distance_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Fixresw2_distance_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Fixresw2_distance_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixresw2_distance_restraint;
}


std::any CyanaMRParser::Fixresw2_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixresw2_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixresw2_distance_restraintContext* CyanaMRParser::fixresw2_distance_restraint() {
  Fixresw2_distance_restraintContext *_localctx = _tracker.createInstance<Fixresw2_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 34, CyanaMRParser::RuleFixresw2_distance_restraint);

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
    setState(324);
    gen_res_num();
    setState(325);
    gen_simple_name();
    setState(327);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 30, _ctx)) {
    case 1: {
      setState(326);
      comment();
      break;
    }

    default:
      break;
    }
    setState(338); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(338);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital:
                case CyanaMRParser::Simple_name: {
                  setState(329);
                  gen_simple_name();
                  setState(330);
                  gen_res_num();
                  setState(331);
                  gen_simple_name();
                  setState(332);
                  gen_simple_name();
                  setState(333);
                  number();
                  setState(334);
                  number();
                  setState(335);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(337);
                  comment();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(340); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 32, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixatm_distance_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Fixatm_distance_restraintsContext::Fixatm_distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Fixatm_distance_restraintContext *> CyanaMRParser::Fixatm_distance_restraintsContext::fixatm_distance_restraint() {
  return getRuleContexts<CyanaMRParser::Fixatm_distance_restraintContext>();
}

CyanaMRParser::Fixatm_distance_restraintContext* CyanaMRParser::Fixatm_distance_restraintsContext::fixatm_distance_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Fixatm_distance_restraintContext>(i);
}


size_t CyanaMRParser::Fixatm_distance_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixatm_distance_restraints;
}


std::any CyanaMRParser::Fixatm_distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixatm_distance_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixatm_distance_restraintsContext* CyanaMRParser::fixatm_distance_restraints() {
  Fixatm_distance_restraintsContext *_localctx = _tracker.createInstance<Fixatm_distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 36, CyanaMRParser::RuleFixatm_distance_restraints);

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
    setState(343); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(342);
              fixatm_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(345); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 33, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixatm_distance_restraintContext ------------------------------------------------------------------

CyanaMRParser::Fixatm_distance_restraintContext::Fixatm_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Fixatm_distance_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Fixatm_distance_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Fixatm_distance_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Fixatm_distance_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Fixatm_distance_restraintContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Fixatm_distance_restraintContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Fixatm_distance_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Fixatm_distance_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Fixatm_distance_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixatm_distance_restraint;
}


std::any CyanaMRParser::Fixatm_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixatm_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixatm_distance_restraintContext* CyanaMRParser::fixatm_distance_restraint() {
  Fixatm_distance_restraintContext *_localctx = _tracker.createInstance<Fixatm_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 38, CyanaMRParser::RuleFixatm_distance_restraint);

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
    setState(347);
    gen_res_num();
    setState(348);
    gen_simple_name();
    setState(349);
    gen_simple_name();
    setState(351);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 34, _ctx)) {
    case 1: {
      setState(350);
      comment();
      break;
    }

    default:
      break;
    }
    setState(359); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(359);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(353);
                  gen_res_num();
                  setState(354);
                  gen_simple_name();
                  setState(355);
                  gen_simple_name();
                  setState(356);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(358);
                  comment();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(361); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 36, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixatmw_distance_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Fixatmw_distance_restraintsContext::Fixatmw_distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Fixatmw_distance_restraintContext *> CyanaMRParser::Fixatmw_distance_restraintsContext::fixatmw_distance_restraint() {
  return getRuleContexts<CyanaMRParser::Fixatmw_distance_restraintContext>();
}

CyanaMRParser::Fixatmw_distance_restraintContext* CyanaMRParser::Fixatmw_distance_restraintsContext::fixatmw_distance_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Fixatmw_distance_restraintContext>(i);
}


size_t CyanaMRParser::Fixatmw_distance_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixatmw_distance_restraints;
}


std::any CyanaMRParser::Fixatmw_distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixatmw_distance_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixatmw_distance_restraintsContext* CyanaMRParser::fixatmw_distance_restraints() {
  Fixatmw_distance_restraintsContext *_localctx = _tracker.createInstance<Fixatmw_distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 40, CyanaMRParser::RuleFixatmw_distance_restraints);

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
    setState(364); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(363);
              fixatmw_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(366); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 37, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixatmw_distance_restraintContext ------------------------------------------------------------------

CyanaMRParser::Fixatmw_distance_restraintContext::Fixatmw_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Fixatmw_distance_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Fixatmw_distance_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Fixatmw_distance_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Fixatmw_distance_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Fixatmw_distance_restraintContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Fixatmw_distance_restraintContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Fixatmw_distance_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Fixatmw_distance_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Fixatmw_distance_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixatmw_distance_restraint;
}


std::any CyanaMRParser::Fixatmw_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixatmw_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixatmw_distance_restraintContext* CyanaMRParser::fixatmw_distance_restraint() {
  Fixatmw_distance_restraintContext *_localctx = _tracker.createInstance<Fixatmw_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 42, CyanaMRParser::RuleFixatmw_distance_restraint);

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
    setState(368);
    gen_res_num();
    setState(369);
    gen_simple_name();
    setState(370);
    gen_simple_name();
    setState(372);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 38, _ctx)) {
    case 1: {
      setState(371);
      comment();
      break;
    }

    default:
      break;
    }
    setState(381); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(381);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(374);
                  gen_res_num();
                  setState(375);
                  gen_simple_name();
                  setState(376);
                  gen_simple_name();
                  setState(377);
                  number();
                  setState(378);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(380);
                  comment();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(383); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 40, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixatmw2_distance_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Fixatmw2_distance_restraintsContext::Fixatmw2_distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Fixatmw2_distance_restraintContext *> CyanaMRParser::Fixatmw2_distance_restraintsContext::fixatmw2_distance_restraint() {
  return getRuleContexts<CyanaMRParser::Fixatmw2_distance_restraintContext>();
}

CyanaMRParser::Fixatmw2_distance_restraintContext* CyanaMRParser::Fixatmw2_distance_restraintsContext::fixatmw2_distance_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Fixatmw2_distance_restraintContext>(i);
}


size_t CyanaMRParser::Fixatmw2_distance_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixatmw2_distance_restraints;
}


std::any CyanaMRParser::Fixatmw2_distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixatmw2_distance_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixatmw2_distance_restraintsContext* CyanaMRParser::fixatmw2_distance_restraints() {
  Fixatmw2_distance_restraintsContext *_localctx = _tracker.createInstance<Fixatmw2_distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 44, CyanaMRParser::RuleFixatmw2_distance_restraints);

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
    setState(386); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(385);
              fixatmw2_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(388); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 41, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Fixatmw2_distance_restraintContext ------------------------------------------------------------------

CyanaMRParser::Fixatmw2_distance_restraintContext::Fixatmw2_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Fixatmw2_distance_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Fixatmw2_distance_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Fixatmw2_distance_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Fixatmw2_distance_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Fixatmw2_distance_restraintContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Fixatmw2_distance_restraintContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Fixatmw2_distance_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Fixatmw2_distance_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Fixatmw2_distance_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleFixatmw2_distance_restraint;
}


std::any CyanaMRParser::Fixatmw2_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitFixatmw2_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Fixatmw2_distance_restraintContext* CyanaMRParser::fixatmw2_distance_restraint() {
  Fixatmw2_distance_restraintContext *_localctx = _tracker.createInstance<Fixatmw2_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 46, CyanaMRParser::RuleFixatmw2_distance_restraint);

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
    setState(390);
    gen_res_num();
    setState(391);
    gen_simple_name();
    setState(392);
    gen_simple_name();
    setState(394);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 42, _ctx)) {
    case 1: {
      setState(393);
      comment();
      break;
    }

    default:
      break;
    }
    setState(404); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(404);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Integer:
                case CyanaMRParser::Capital_integer:
                case CyanaMRParser::Integer_capital: {
                  setState(396);
                  gen_res_num();
                  setState(397);
                  gen_simple_name();
                  setState(398);
                  gen_simple_name();
                  setState(399);
                  number();
                  setState(400);
                  number();
                  setState(401);
                  number();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(403);
                  comment();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(406); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 44, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Diana_distance_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Diana_distance_restraintsContext::Diana_distance_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Diana_distance_restraintContext *> CyanaMRParser::Diana_distance_restraintsContext::diana_distance_restraint() {
  return getRuleContexts<CyanaMRParser::Diana_distance_restraintContext>();
}

CyanaMRParser::Diana_distance_restraintContext* CyanaMRParser::Diana_distance_restraintsContext::diana_distance_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_distance_restraintContext>(i);
}


size_t CyanaMRParser::Diana_distance_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_distance_restraints;
}


std::any CyanaMRParser::Diana_distance_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_distance_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_distance_restraintsContext* CyanaMRParser::diana_distance_restraints() {
  Diana_distance_restraintsContext *_localctx = _tracker.createInstance<Diana_distance_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 48, CyanaMRParser::RuleDiana_distance_restraints);

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
    setState(409); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(408);
              diana_distance_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(411); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 45, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Diana_distance_restraintContext ------------------------------------------------------------------

CyanaMRParser::Diana_distance_restraintContext::Diana_distance_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Diana_distance_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Diana_distance_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Diana_distance_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Diana_distance_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Diana_distance_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Diana_distance_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Diana_distance_restraintContext::NoeUpp() {
  return getToken(CyanaMRParser::NoeUpp, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_distance_restraintContext::NoeLow() {
  return getToken(CyanaMRParser::NoeLow, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_distance_restraintContext::Simple_name() {
  return getToken(CyanaMRParser::Simple_name, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_distance_restraintContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}


size_t CyanaMRParser::Diana_distance_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_distance_restraint;
}


std::any CyanaMRParser::Diana_distance_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_distance_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_distance_restraintContext* CyanaMRParser::diana_distance_restraint() {
  Diana_distance_restraintContext *_localctx = _tracker.createInstance<Diana_distance_restraintContext>(_ctx, getState());
  enterRule(_localctx, 50, CyanaMRParser::RuleDiana_distance_restraint);
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
    setState(413);
    _la = _input->LA(1);
    if (!(_la == CyanaMRParser::NoeUpp

    || _la == CyanaMRParser::NoeLow)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(414);
    gen_simple_name();
    setState(415);
    gen_res_num();
    setState(416);
    gen_simple_name();
    setState(417);
    gen_simple_name();
    setState(418);
    gen_res_num();
    setState(419);
    gen_simple_name();
    setState(420);
    number();
    setState(427);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 46, _ctx)) {
    case 1: {
      setState(421);
      gen_simple_name();
      setState(422);
      gen_simple_name();
      setState(423);
      gen_res_num();
      setState(424);
      gen_simple_name();
      setState(425);
      number();
      break;
    }

    default:
      break;
    }
    setState(431);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 47, _ctx)) {
    case 1: {
      setState(429);
      match(CyanaMRParser::Simple_name);
      setState(430);
      match(CyanaMRParser::Integer);
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

//----------------- Diana_ssbond_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Diana_ssbond_restraintsContext::Diana_ssbond_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Diana_ssbond_restraintContext *> CyanaMRParser::Diana_ssbond_restraintsContext::diana_ssbond_restraint() {
  return getRuleContexts<CyanaMRParser::Diana_ssbond_restraintContext>();
}

CyanaMRParser::Diana_ssbond_restraintContext* CyanaMRParser::Diana_ssbond_restraintsContext::diana_ssbond_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_ssbond_restraintContext>(i);
}


size_t CyanaMRParser::Diana_ssbond_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_ssbond_restraints;
}


std::any CyanaMRParser::Diana_ssbond_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_ssbond_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_ssbond_restraintsContext* CyanaMRParser::diana_ssbond_restraints() {
  Diana_ssbond_restraintsContext *_localctx = _tracker.createInstance<Diana_ssbond_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 52, CyanaMRParser::RuleDiana_ssbond_restraints);

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
    setState(434); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(433);
              diana_ssbond_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(436); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 48, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Diana_ssbond_restraintContext ------------------------------------------------------------------

CyanaMRParser::Diana_ssbond_restraintContext::Diana_ssbond_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Diana_ssbond_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Diana_ssbond_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Diana_ssbond_restraintContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Diana_ssbond_restraintContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Diana_ssbond_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Diana_ssbond_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Diana_ssbond_restraintContext::SSUpp() {
  return getToken(CyanaMRParser::SSUpp, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_ssbond_restraintContext::SSLow() {
  return getToken(CyanaMRParser::SSLow, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_ssbond_restraintContext::Simple_name() {
  return getToken(CyanaMRParser::Simple_name, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_ssbond_restraintContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}


size_t CyanaMRParser::Diana_ssbond_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_ssbond_restraint;
}


std::any CyanaMRParser::Diana_ssbond_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_ssbond_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_ssbond_restraintContext* CyanaMRParser::diana_ssbond_restraint() {
  Diana_ssbond_restraintContext *_localctx = _tracker.createInstance<Diana_ssbond_restraintContext>(_ctx, getState());
  enterRule(_localctx, 54, CyanaMRParser::RuleDiana_ssbond_restraint);
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
    setState(438);
    _la = _input->LA(1);
    if (!(_la == CyanaMRParser::SSUpp

    || _la == CyanaMRParser::SSLow)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(439);
    gen_simple_name();
    setState(440);
    gen_res_num();
    setState(441);
    gen_simple_name();
    setState(442);
    gen_simple_name();
    setState(443);
    gen_res_num();
    setState(444);
    gen_simple_name();
    setState(445);
    number();
    setState(452);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 49, _ctx)) {
    case 1: {
      setState(446);
      gen_simple_name();
      setState(447);
      gen_simple_name();
      setState(448);
      gen_res_num();
      setState(449);
      gen_simple_name();
      setState(450);
      number();
      break;
    }

    default:
      break;
    }
    setState(456);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 50, _ctx)) {
    case 1: {
      setState(454);
      match(CyanaMRParser::Simple_name);
      setState(455);
      match(CyanaMRParser::Integer);
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

//----------------- Diana_torsion_angle_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Diana_torsion_angle_restraintsContext::Diana_torsion_angle_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Diana_torsion_angle_restraintContext *> CyanaMRParser::Diana_torsion_angle_restraintsContext::diana_torsion_angle_restraint() {
  return getRuleContexts<CyanaMRParser::Diana_torsion_angle_restraintContext>();
}

CyanaMRParser::Diana_torsion_angle_restraintContext* CyanaMRParser::Diana_torsion_angle_restraintsContext::diana_torsion_angle_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_torsion_angle_restraintContext>(i);
}


size_t CyanaMRParser::Diana_torsion_angle_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_torsion_angle_restraints;
}


std::any CyanaMRParser::Diana_torsion_angle_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_torsion_angle_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_torsion_angle_restraintsContext* CyanaMRParser::diana_torsion_angle_restraints() {
  Diana_torsion_angle_restraintsContext *_localctx = _tracker.createInstance<Diana_torsion_angle_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 56, CyanaMRParser::RuleDiana_torsion_angle_restraints);

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
    setState(459); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(458);
              diana_torsion_angle_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(461); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 51, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Diana_torsion_angle_restraintContext ------------------------------------------------------------------

CyanaMRParser::Diana_torsion_angle_restraintContext::Diana_torsion_angle_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Diana_torsion_angle_restraintContext::Angle() {
  return getToken(CyanaMRParser::Angle, 0);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Diana_torsion_angle_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Diana_torsion_angle_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Diana_torsion_angle_restraintContext::gen_res_num() {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(0);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Diana_torsion_angle_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Diana_torsion_angle_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Diana_torsion_angle_restraintContext::Simple_name() {
  return getToken(CyanaMRParser::Simple_name, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_torsion_angle_restraintContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}


size_t CyanaMRParser::Diana_torsion_angle_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_torsion_angle_restraint;
}


std::any CyanaMRParser::Diana_torsion_angle_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_torsion_angle_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_torsion_angle_restraintContext* CyanaMRParser::diana_torsion_angle_restraint() {
  Diana_torsion_angle_restraintContext *_localctx = _tracker.createInstance<Diana_torsion_angle_restraintContext>(_ctx, getState());
  enterRule(_localctx, 58, CyanaMRParser::RuleDiana_torsion_angle_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(463);
    match(CyanaMRParser::Angle);
    setState(464);
    gen_simple_name();
    setState(465);
    gen_res_num();
    setState(466);
    gen_simple_name();
    setState(467);
    number();
    setState(468);
    number();
    setState(471);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 52, _ctx)) {
    case 1: {
      setState(469);
      match(CyanaMRParser::Simple_name);
      setState(470);
      match(CyanaMRParser::Integer);
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

//----------------- Diana_coupling_constant_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Diana_coupling_constant_restraintsContext::Diana_coupling_constant_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Diana_coupling_constant_restraintContext *> CyanaMRParser::Diana_coupling_constant_restraintsContext::diana_coupling_constant_restraint() {
  return getRuleContexts<CyanaMRParser::Diana_coupling_constant_restraintContext>();
}

CyanaMRParser::Diana_coupling_constant_restraintContext* CyanaMRParser::Diana_coupling_constant_restraintsContext::diana_coupling_constant_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_coupling_constant_restraintContext>(i);
}


size_t CyanaMRParser::Diana_coupling_constant_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_coupling_constant_restraints;
}


std::any CyanaMRParser::Diana_coupling_constant_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_coupling_constant_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_coupling_constant_restraintsContext* CyanaMRParser::diana_coupling_constant_restraints() {
  Diana_coupling_constant_restraintsContext *_localctx = _tracker.createInstance<Diana_coupling_constant_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 60, CyanaMRParser::RuleDiana_coupling_constant_restraints);

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
    setState(474); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(473);
              diana_coupling_constant_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(476); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 53, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Diana_coupling_constant_restraintContext ------------------------------------------------------------------

CyanaMRParser::Diana_coupling_constant_restraintContext::Diana_coupling_constant_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Diana_coupling_constant_restraintContext::JCoupl() {
  return getToken(CyanaMRParser::JCoupl, 0);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Diana_coupling_constant_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Diana_coupling_constant_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Diana_coupling_constant_restraintContext::gen_res_num() {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(0);
}

CyanaMRParser::NumberContext* CyanaMRParser::Diana_coupling_constant_restraintContext::number() {
  return getRuleContext<CyanaMRParser::NumberContext>(0);
}

tree::TerminalNode* CyanaMRParser::Diana_coupling_constant_restraintContext::Simple_name() {
  return getToken(CyanaMRParser::Simple_name, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_coupling_constant_restraintContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}


size_t CyanaMRParser::Diana_coupling_constant_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_coupling_constant_restraint;
}


std::any CyanaMRParser::Diana_coupling_constant_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_coupling_constant_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_coupling_constant_restraintContext* CyanaMRParser::diana_coupling_constant_restraint() {
  Diana_coupling_constant_restraintContext *_localctx = _tracker.createInstance<Diana_coupling_constant_restraintContext>(_ctx, getState());
  enterRule(_localctx, 62, CyanaMRParser::RuleDiana_coupling_constant_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(478);
    match(CyanaMRParser::JCoupl);
    setState(479);
    gen_simple_name();
    setState(480);
    gen_res_num();
    setState(481);
    gen_simple_name();
    setState(482);
    gen_simple_name();
    setState(483);
    number();
    setState(486);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 54, _ctx)) {
    case 1: {
      setState(484);
      match(CyanaMRParser::Simple_name);
      setState(485);
      match(CyanaMRParser::Integer);
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

//----------------- Diana_chemical_shiftsContext ------------------------------------------------------------------

CyanaMRParser::Diana_chemical_shiftsContext::Diana_chemical_shiftsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Diana_chemical_shiftContext *> CyanaMRParser::Diana_chemical_shiftsContext::diana_chemical_shift() {
  return getRuleContexts<CyanaMRParser::Diana_chemical_shiftContext>();
}

CyanaMRParser::Diana_chemical_shiftContext* CyanaMRParser::Diana_chemical_shiftsContext::diana_chemical_shift(size_t i) {
  return getRuleContext<CyanaMRParser::Diana_chemical_shiftContext>(i);
}


size_t CyanaMRParser::Diana_chemical_shiftsContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_chemical_shifts;
}


std::any CyanaMRParser::Diana_chemical_shiftsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_chemical_shifts(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_chemical_shiftsContext* CyanaMRParser::diana_chemical_shifts() {
  Diana_chemical_shiftsContext *_localctx = _tracker.createInstance<Diana_chemical_shiftsContext>(_ctx, getState());
  enterRule(_localctx, 64, CyanaMRParser::RuleDiana_chemical_shifts);

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
    setState(489); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(488);
              diana_chemical_shift();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(491); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 55, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Diana_chemical_shiftContext ------------------------------------------------------------------

CyanaMRParser::Diana_chemical_shiftContext::Diana_chemical_shiftContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Diana_chemical_shiftContext::Shifts() {
  return getToken(CyanaMRParser::Shifts, 0);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Diana_chemical_shiftContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Diana_chemical_shiftContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Diana_chemical_shiftContext::gen_res_num() {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(0);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Diana_chemical_shiftContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Diana_chemical_shiftContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Diana_chemical_shiftContext::Simple_name() {
  return getToken(CyanaMRParser::Simple_name, 0);
}

tree::TerminalNode* CyanaMRParser::Diana_chemical_shiftContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}


size_t CyanaMRParser::Diana_chemical_shiftContext::getRuleIndex() const {
  return CyanaMRParser::RuleDiana_chemical_shift;
}


std::any CyanaMRParser::Diana_chemical_shiftContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDiana_chemical_shift(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Diana_chemical_shiftContext* CyanaMRParser::diana_chemical_shift() {
  Diana_chemical_shiftContext *_localctx = _tracker.createInstance<Diana_chemical_shiftContext>(_ctx, getState());
  enterRule(_localctx, 66, CyanaMRParser::RuleDiana_chemical_shift);

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
    setState(493);
    match(CyanaMRParser::Shifts);
    setState(494);
    gen_simple_name();
    setState(495);
    gen_res_num();
    setState(496);
    gen_simple_name();
    setState(497);
    number();
    setState(503);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 56, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(498);
        gen_simple_name();
        setState(499);
        number(); 
      }
      setState(505);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 56, _ctx);
    }
    setState(508);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 57, _ctx)) {
    case 1: {
      setState(506);
      match(CyanaMRParser::Simple_name);
      setState(507);
      match(CyanaMRParser::Integer);
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

//----------------- Distance_w_chain_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Distance_w_chain_restraintsContext::Distance_w_chain_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Distance_w_chain_restraintContext *> CyanaMRParser::Distance_w_chain_restraintsContext::distance_w_chain_restraint() {
  return getRuleContexts<CyanaMRParser::Distance_w_chain_restraintContext>();
}

CyanaMRParser::Distance_w_chain_restraintContext* CyanaMRParser::Distance_w_chain_restraintsContext::distance_w_chain_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Distance_w_chain_restraintContext>(i);
}


size_t CyanaMRParser::Distance_w_chain_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleDistance_w_chain_restraints;
}


std::any CyanaMRParser::Distance_w_chain_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_w_chain_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Distance_w_chain_restraintsContext* CyanaMRParser::distance_w_chain_restraints() {
  Distance_w_chain_restraintsContext *_localctx = _tracker.createInstance<Distance_w_chain_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 68, CyanaMRParser::RuleDistance_w_chain_restraints);

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
    setState(511); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(510);
              distance_w_chain_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(513); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 58, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_w_chain_restraintContext ------------------------------------------------------------------

CyanaMRParser::Distance_w_chain_restraintContext::Distance_w_chain_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> CyanaMRParser::Distance_w_chain_restraintContext::Integer() {
  return getTokens(CyanaMRParser::Integer);
}

tree::TerminalNode* CyanaMRParser::Distance_w_chain_restraintContext::Integer(size_t i) {
  return getToken(CyanaMRParser::Integer, i);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Distance_w_chain_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Distance_w_chain_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Distance_w_chain_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Distance_w_chain_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Distance_w_chain_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleDistance_w_chain_restraint;
}


std::any CyanaMRParser::Distance_w_chain_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_w_chain_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Distance_w_chain_restraintContext* CyanaMRParser::distance_w_chain_restraint() {
  Distance_w_chain_restraintContext *_localctx = _tracker.createInstance<Distance_w_chain_restraintContext>(_ctx, getState());
  enterRule(_localctx, 70, CyanaMRParser::RuleDistance_w_chain_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(515);
    match(CyanaMRParser::Integer);
    setState(516);
    gen_simple_name();
    setState(517);
    gen_simple_name();
    setState(518);
    gen_simple_name();
    setState(519);
    match(CyanaMRParser::Integer);
    setState(520);
    gen_simple_name();
    setState(521);
    gen_simple_name();
    setState(522);
    gen_simple_name();
    setState(523);
    number();
    setState(525);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 59, _ctx)) {
    case 1: {
      setState(524);
      number();
      break;
    }

    default:
      break;
    }
    setState(528);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 60, _ctx)) {
    case 1: {
      setState(527);
      number();
      break;
    }

    default:
      break;
    }
    setState(531);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 61, _ctx)) {
    case 1: {
      setState(530);
      number();
      break;
    }

    default:
      break;
    }
    setState(534);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 62, _ctx)) {
    case 1: {
      setState(533);
      number();
      break;
    }

    default:
      break;
    }
    setState(537);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 63, _ctx)) {
    case 1: {
      setState(536);
      number();
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

//----------------- Distance_w_chain2_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Distance_w_chain2_restraintsContext::Distance_w_chain2_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Distance_w_chain2_restraintContext *> CyanaMRParser::Distance_w_chain2_restraintsContext::distance_w_chain2_restraint() {
  return getRuleContexts<CyanaMRParser::Distance_w_chain2_restraintContext>();
}

CyanaMRParser::Distance_w_chain2_restraintContext* CyanaMRParser::Distance_w_chain2_restraintsContext::distance_w_chain2_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Distance_w_chain2_restraintContext>(i);
}


size_t CyanaMRParser::Distance_w_chain2_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleDistance_w_chain2_restraints;
}


std::any CyanaMRParser::Distance_w_chain2_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_w_chain2_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Distance_w_chain2_restraintsContext* CyanaMRParser::distance_w_chain2_restraints() {
  Distance_w_chain2_restraintsContext *_localctx = _tracker.createInstance<Distance_w_chain2_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 72, CyanaMRParser::RuleDistance_w_chain2_restraints);

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
    setState(540); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(539);
              distance_w_chain2_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(542); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 64, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_w_chain2_restraintContext ------------------------------------------------------------------

CyanaMRParser::Distance_w_chain2_restraintContext::Distance_w_chain2_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Distance_w_chain2_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Distance_w_chain2_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Distance_w_chain2_restraintContext::Integer() {
  return getTokens(CyanaMRParser::Integer);
}

tree::TerminalNode* CyanaMRParser::Distance_w_chain2_restraintContext::Integer(size_t i) {
  return getToken(CyanaMRParser::Integer, i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Distance_w_chain2_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Distance_w_chain2_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Distance_w_chain2_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleDistance_w_chain2_restraint;
}


std::any CyanaMRParser::Distance_w_chain2_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_w_chain2_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Distance_w_chain2_restraintContext* CyanaMRParser::distance_w_chain2_restraint() {
  Distance_w_chain2_restraintContext *_localctx = _tracker.createInstance<Distance_w_chain2_restraintContext>(_ctx, getState());
  enterRule(_localctx, 74, CyanaMRParser::RuleDistance_w_chain2_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(544);
    gen_simple_name();
    setState(545);
    match(CyanaMRParser::Integer);
    setState(546);
    gen_simple_name();
    setState(547);
    gen_simple_name();
    setState(548);
    gen_simple_name();
    setState(549);
    match(CyanaMRParser::Integer);
    setState(550);
    gen_simple_name();
    setState(551);
    gen_simple_name();
    setState(552);
    number();
    setState(554);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 65, _ctx)) {
    case 1: {
      setState(553);
      number();
      break;
    }

    default:
      break;
    }
    setState(557);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 66, _ctx)) {
    case 1: {
      setState(556);
      number();
      break;
    }

    default:
      break;
    }
    setState(560);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 67, _ctx)) {
    case 1: {
      setState(559);
      number();
      break;
    }

    default:
      break;
    }
    setState(563);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 68, _ctx)) {
    case 1: {
      setState(562);
      number();
      break;
    }

    default:
      break;
    }
    setState(566);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 69, _ctx)) {
    case 1: {
      setState(565);
      number();
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

//----------------- Distance_w_chain3_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Distance_w_chain3_restraintsContext::Distance_w_chain3_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Distance_w_chain3_restraintContext *> CyanaMRParser::Distance_w_chain3_restraintsContext::distance_w_chain3_restraint() {
  return getRuleContexts<CyanaMRParser::Distance_w_chain3_restraintContext>();
}

CyanaMRParser::Distance_w_chain3_restraintContext* CyanaMRParser::Distance_w_chain3_restraintsContext::distance_w_chain3_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Distance_w_chain3_restraintContext>(i);
}


size_t CyanaMRParser::Distance_w_chain3_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleDistance_w_chain3_restraints;
}


std::any CyanaMRParser::Distance_w_chain3_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_w_chain3_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Distance_w_chain3_restraintsContext* CyanaMRParser::distance_w_chain3_restraints() {
  Distance_w_chain3_restraintsContext *_localctx = _tracker.createInstance<Distance_w_chain3_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 76, CyanaMRParser::RuleDistance_w_chain3_restraints);

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
    setState(569); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(568);
              distance_w_chain3_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(571); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 70, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Distance_w_chain3_restraintContext ------------------------------------------------------------------

CyanaMRParser::Distance_w_chain3_restraintContext::Distance_w_chain3_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Distance_w_chain3_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Distance_w_chain3_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Distance_w_chain3_restraintContext::Integer() {
  return getTokens(CyanaMRParser::Integer);
}

tree::TerminalNode* CyanaMRParser::Distance_w_chain3_restraintContext::Integer(size_t i) {
  return getToken(CyanaMRParser::Integer, i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Distance_w_chain3_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Distance_w_chain3_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Distance_w_chain3_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleDistance_w_chain3_restraint;
}


std::any CyanaMRParser::Distance_w_chain3_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDistance_w_chain3_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Distance_w_chain3_restraintContext* CyanaMRParser::distance_w_chain3_restraint() {
  Distance_w_chain3_restraintContext *_localctx = _tracker.createInstance<Distance_w_chain3_restraintContext>(_ctx, getState());
  enterRule(_localctx, 78, CyanaMRParser::RuleDistance_w_chain3_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(573);
    gen_simple_name();
    setState(574);
    gen_simple_name();
    setState(575);
    match(CyanaMRParser::Integer);
    setState(576);
    gen_simple_name();
    setState(577);
    gen_simple_name();
    setState(578);
    gen_simple_name();
    setState(579);
    match(CyanaMRParser::Integer);
    setState(580);
    gen_simple_name();
    setState(581);
    number();
    setState(583);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 71, _ctx)) {
    case 1: {
      setState(582);
      number();
      break;
    }

    default:
      break;
    }
    setState(586);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 72, _ctx)) {
    case 1: {
      setState(585);
      number();
      break;
    }

    default:
      break;
    }
    setState(589);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 73, _ctx)) {
    case 1: {
      setState(588);
      number();
      break;
    }

    default:
      break;
    }
    setState(592);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 74, _ctx)) {
    case 1: {
      setState(591);
      number();
      break;
    }

    default:
      break;
    }
    setState(595);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 75, _ctx)) {
    case 1: {
      setState(594);
      number();
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

//----------------- Torsion_angle_w_chain_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Torsion_angle_w_chain_restraintsContext::Torsion_angle_w_chain_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Torsion_angle_w_chain_restraintContext *> CyanaMRParser::Torsion_angle_w_chain_restraintsContext::torsion_angle_w_chain_restraint() {
  return getRuleContexts<CyanaMRParser::Torsion_angle_w_chain_restraintContext>();
}

CyanaMRParser::Torsion_angle_w_chain_restraintContext* CyanaMRParser::Torsion_angle_w_chain_restraintsContext::torsion_angle_w_chain_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Torsion_angle_w_chain_restraintContext>(i);
}


size_t CyanaMRParser::Torsion_angle_w_chain_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleTorsion_angle_w_chain_restraints;
}


std::any CyanaMRParser::Torsion_angle_w_chain_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitTorsion_angle_w_chain_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Torsion_angle_w_chain_restraintsContext* CyanaMRParser::torsion_angle_w_chain_restraints() {
  Torsion_angle_w_chain_restraintsContext *_localctx = _tracker.createInstance<Torsion_angle_w_chain_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 80, CyanaMRParser::RuleTorsion_angle_w_chain_restraints);

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
    setState(598); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(597);
              torsion_angle_w_chain_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(600); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 76, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Torsion_angle_w_chain_restraintContext ------------------------------------------------------------------

CyanaMRParser::Torsion_angle_w_chain_restraintContext::Torsion_angle_w_chain_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Torsion_angle_w_chain_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Torsion_angle_w_chain_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Torsion_angle_w_chain_restraintContext::Integer() {
  return getTokens(CyanaMRParser::Integer);
}

tree::TerminalNode* CyanaMRParser::Torsion_angle_w_chain_restraintContext::Integer(size_t i) {
  return getToken(CyanaMRParser::Integer, i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Torsion_angle_w_chain_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Torsion_angle_w_chain_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}

tree::TerminalNode* CyanaMRParser::Torsion_angle_w_chain_restraintContext::Type() {
  return getToken(CyanaMRParser::Type, 0);
}

tree::TerminalNode* CyanaMRParser::Torsion_angle_w_chain_restraintContext::Equ_op() {
  return getToken(CyanaMRParser::Equ_op, 0);
}

tree::TerminalNode* CyanaMRParser::Torsion_angle_w_chain_restraintContext::Or() {
  return getToken(CyanaMRParser::Or, 0);
}


size_t CyanaMRParser::Torsion_angle_w_chain_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleTorsion_angle_w_chain_restraint;
}


std::any CyanaMRParser::Torsion_angle_w_chain_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitTorsion_angle_w_chain_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Torsion_angle_w_chain_restraintContext* CyanaMRParser::torsion_angle_w_chain_restraint() {
  Torsion_angle_w_chain_restraintContext *_localctx = _tracker.createInstance<Torsion_angle_w_chain_restraintContext>(_ctx, getState());
  enterRule(_localctx, 82, CyanaMRParser::RuleTorsion_angle_w_chain_restraint);
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
    setState(602);
    gen_simple_name();
    setState(603);
    match(CyanaMRParser::Integer);
    setState(604);
    gen_simple_name();
    setState(605);
    gen_simple_name();
    setState(606);
    number();
    setState(607);
    number();
    setState(609);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 77, _ctx)) {
    case 1: {
      setState(608);
      number();
      break;
    }

    default:
      break;
    }
    setState(614);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Type) {
      setState(611);
      match(CyanaMRParser::Type);
      setState(612);
      match(CyanaMRParser::Equ_op);
      setState(613);
      match(CyanaMRParser::Integer);
    }
    setState(617);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Or) {
      setState(616);
      match(CyanaMRParser::Or);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Cco_restraintsContext ------------------------------------------------------------------

CyanaMRParser::Cco_restraintsContext::Cco_restraintsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CyanaMRParser::Cco_restraintContext *> CyanaMRParser::Cco_restraintsContext::cco_restraint() {
  return getRuleContexts<CyanaMRParser::Cco_restraintContext>();
}

CyanaMRParser::Cco_restraintContext* CyanaMRParser::Cco_restraintsContext::cco_restraint(size_t i) {
  return getRuleContext<CyanaMRParser::Cco_restraintContext>(i);
}


size_t CyanaMRParser::Cco_restraintsContext::getRuleIndex() const {
  return CyanaMRParser::RuleCco_restraints;
}


std::any CyanaMRParser::Cco_restraintsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitCco_restraints(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Cco_restraintsContext* CyanaMRParser::cco_restraints() {
  Cco_restraintsContext *_localctx = _tracker.createInstance<Cco_restraintsContext>(_ctx, getState());
  enterRule(_localctx, 84, CyanaMRParser::RuleCco_restraints);

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
    setState(620); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(619);
              cco_restraint();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(622); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 80, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Cco_restraintContext ------------------------------------------------------------------

CyanaMRParser::Cco_restraintContext::Cco_restraintContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Cco_restraintContext::gen_res_num() {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(0);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Cco_restraintContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Cco_restraintContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::NumberContext *> CyanaMRParser::Cco_restraintContext::number() {
  return getRuleContexts<CyanaMRParser::NumberContext>();
}

CyanaMRParser::NumberContext* CyanaMRParser::Cco_restraintContext::number(size_t i) {
  return getRuleContext<CyanaMRParser::NumberContext>(i);
}


size_t CyanaMRParser::Cco_restraintContext::getRuleIndex() const {
  return CyanaMRParser::RuleCco_restraint;
}


std::any CyanaMRParser::Cco_restraintContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitCco_restraint(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Cco_restraintContext* CyanaMRParser::cco_restraint() {
  Cco_restraintContext *_localctx = _tracker.createInstance<Cco_restraintContext>(_ctx, getState());
  enterRule(_localctx, 86, CyanaMRParser::RuleCco_restraint);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(624);
    gen_res_num();
    setState(625);
    gen_simple_name();
    setState(626);
    gen_simple_name();
    setState(627);
    gen_simple_name();
    setState(628);
    number();
    setState(630);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 81, _ctx)) {
    case 1: {
      setState(629);
      number();
      break;
    }

    default:
      break;
    }
    setState(633);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 82, _ctx)) {
    case 1: {
      setState(632);
      number();
      break;
    }

    default:
      break;
    }
    setState(636);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 83, _ctx)) {
    case 1: {
      setState(635);
      number();
      break;
    }

    default:
      break;
    }
    setState(639);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 84, _ctx)) {
    case 1: {
      setState(638);
      number();
      break;
    }

    default:
      break;
    }
    setState(642);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 85, _ctx)) {
    case 1: {
      setState(641);
      number();
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

//----------------- Ssbond_macroContext ------------------------------------------------------------------

CyanaMRParser::Ssbond_macroContext::Ssbond_macroContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Ssbond_macroContext::Ssbond() {
  return getToken(CyanaMRParser::Ssbond, 0);
}

tree::TerminalNode* CyanaMRParser::Ssbond_macroContext::Ssbond_resids() {
  return getToken(CyanaMRParser::Ssbond_resids, 0);
}


size_t CyanaMRParser::Ssbond_macroContext::getRuleIndex() const {
  return CyanaMRParser::RuleSsbond_macro;
}


std::any CyanaMRParser::Ssbond_macroContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitSsbond_macro(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Ssbond_macroContext* CyanaMRParser::ssbond_macro() {
  Ssbond_macroContext *_localctx = _tracker.createInstance<Ssbond_macroContext>(_ctx, getState());
  enterRule(_localctx, 88, CyanaMRParser::RuleSsbond_macro);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(644);
    match(CyanaMRParser::Ssbond);
    setState(645);
    match(CyanaMRParser::Ssbond_resids);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Hbond_macroContext ------------------------------------------------------------------

CyanaMRParser::Hbond_macroContext::Hbond_macroContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Hbond() {
  return getToken(CyanaMRParser::Hbond, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Hbond_macroContext::Simple_name_HB() {
  return getTokens(CyanaMRParser::Simple_name_HB);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Simple_name_HB(size_t i) {
  return getToken(CyanaMRParser::Simple_name_HB, i);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Hbond_macroContext::Integer_HB() {
  return getTokens(CyanaMRParser::Integer_HB);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Integer_HB(size_t i) {
  return getToken(CyanaMRParser::Integer_HB, i);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::RETURN_HB() {
  return getToken(CyanaMRParser::RETURN_HB, 0);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Atom1() {
  return getToken(CyanaMRParser::Atom1, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Hbond_macroContext::Equ_op_HB() {
  return getTokens(CyanaMRParser::Equ_op_HB);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Equ_op_HB(size_t i) {
  return getToken(CyanaMRParser::Equ_op_HB, i);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Residue1() {
  return getToken(CyanaMRParser::Residue1, 0);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Atom2() {
  return getToken(CyanaMRParser::Atom2, 0);
}

tree::TerminalNode* CyanaMRParser::Hbond_macroContext::Residue2() {
  return getToken(CyanaMRParser::Residue2, 0);
}


size_t CyanaMRParser::Hbond_macroContext::getRuleIndex() const {
  return CyanaMRParser::RuleHbond_macro;
}


std::any CyanaMRParser::Hbond_macroContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitHbond_macro(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Hbond_macroContext* CyanaMRParser::hbond_macro() {
  Hbond_macroContext *_localctx = _tracker.createInstance<Hbond_macroContext>(_ctx, getState());
  enterRule(_localctx, 90, CyanaMRParser::RuleHbond_macro);
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
    setState(647);
    match(CyanaMRParser::Hbond);
    setState(650);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Atom1) {
      setState(648);
      match(CyanaMRParser::Atom1);
      setState(649);
      match(CyanaMRParser::Equ_op_HB);
    }
    setState(652);
    match(CyanaMRParser::Simple_name_HB);
    setState(655);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Residue1) {
      setState(653);
      match(CyanaMRParser::Residue1);
      setState(654);
      match(CyanaMRParser::Equ_op_HB);
    }
    setState(657);
    match(CyanaMRParser::Integer_HB);
    setState(660);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Atom2) {
      setState(658);
      match(CyanaMRParser::Atom2);
      setState(659);
      match(CyanaMRParser::Equ_op_HB);
    }
    setState(662);
    match(CyanaMRParser::Simple_name_HB);
    setState(665);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CyanaMRParser::Residue2) {
      setState(663);
      match(CyanaMRParser::Residue2);
      setState(664);
      match(CyanaMRParser::Equ_op_HB);
    }
    setState(667);
    match(CyanaMRParser::Integer_HB);
    setState(668);
    match(CyanaMRParser::RETURN_HB);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Link_statementContext ------------------------------------------------------------------

CyanaMRParser::Link_statementContext::Link_statementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Link_statementContext::Link() {
  return getToken(CyanaMRParser::Link, 0);
}

std::vector<CyanaMRParser::Gen_simple_nameContext *> CyanaMRParser::Link_statementContext::gen_simple_name() {
  return getRuleContexts<CyanaMRParser::Gen_simple_nameContext>();
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Link_statementContext::gen_simple_name(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(i);
}

std::vector<CyanaMRParser::Gen_res_numContext *> CyanaMRParser::Link_statementContext::gen_res_num() {
  return getRuleContexts<CyanaMRParser::Gen_res_numContext>();
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::Link_statementContext::gen_res_num(size_t i) {
  return getRuleContext<CyanaMRParser::Gen_res_numContext>(i);
}


size_t CyanaMRParser::Link_statementContext::getRuleIndex() const {
  return CyanaMRParser::RuleLink_statement;
}


std::any CyanaMRParser::Link_statementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitLink_statement(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Link_statementContext* CyanaMRParser::link_statement() {
  Link_statementContext *_localctx = _tracker.createInstance<Link_statementContext>(_ctx, getState());
  enterRule(_localctx, 92, CyanaMRParser::RuleLink_statement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(670);
    match(CyanaMRParser::Link);
    setState(671);
    gen_simple_name();
    setState(672);
    gen_res_num();
    setState(673);
    gen_simple_name();
    setState(674);
    gen_res_num();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Stereoassign_macroContext ------------------------------------------------------------------

CyanaMRParser::Stereoassign_macroContext::Stereoassign_macroContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Stereoassign_macroContext::Atom_stereo() {
  return getToken(CyanaMRParser::Atom_stereo, 0);
}

tree::TerminalNode* CyanaMRParser::Stereoassign_macroContext::Double_quote_string() {
  return getToken(CyanaMRParser::Double_quote_string, 0);
}

tree::TerminalNode* CyanaMRParser::Stereoassign_macroContext::RETURN_PR() {
  return getToken(CyanaMRParser::RETURN_PR, 0);
}


size_t CyanaMRParser::Stereoassign_macroContext::getRuleIndex() const {
  return CyanaMRParser::RuleStereoassign_macro;
}


std::any CyanaMRParser::Stereoassign_macroContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitStereoassign_macro(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Stereoassign_macroContext* CyanaMRParser::stereoassign_macro() {
  Stereoassign_macroContext *_localctx = _tracker.createInstance<Stereoassign_macroContext>(_ctx, getState());
  enterRule(_localctx, 94, CyanaMRParser::RuleStereoassign_macro);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(676);
    match(CyanaMRParser::Atom_stereo);
    setState(677);
    match(CyanaMRParser::Double_quote_string);
    setState(678);
    match(CyanaMRParser::RETURN_PR);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Declare_variableContext ------------------------------------------------------------------

CyanaMRParser::Declare_variableContext::Declare_variableContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Declare_variableContext::Var() {
  return getToken(CyanaMRParser::Var, 0);
}

tree::TerminalNode* CyanaMRParser::Declare_variableContext::RETURN_VA() {
  return getToken(CyanaMRParser::RETURN_VA, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Declare_variableContext::Simple_name_VA() {
  return getTokens(CyanaMRParser::Simple_name_VA);
}

tree::TerminalNode* CyanaMRParser::Declare_variableContext::Simple_name_VA(size_t i) {
  return getToken(CyanaMRParser::Simple_name_VA, i);
}


size_t CyanaMRParser::Declare_variableContext::getRuleIndex() const {
  return CyanaMRParser::RuleDeclare_variable;
}


std::any CyanaMRParser::Declare_variableContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitDeclare_variable(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Declare_variableContext* CyanaMRParser::declare_variable() {
  Declare_variableContext *_localctx = _tracker.createInstance<Declare_variableContext>(_ctx, getState());
  enterRule(_localctx, 96, CyanaMRParser::RuleDeclare_variable);
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
    setState(680);
    match(CyanaMRParser::Var);
    setState(684);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CyanaMRParser::Simple_name_VA) {
      setState(681);
      match(CyanaMRParser::Simple_name_VA);
      setState(686);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(687);
    match(CyanaMRParser::RETURN_VA);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Set_variableContext ------------------------------------------------------------------

CyanaMRParser::Set_variableContext::Set_variableContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Set_variableContext::SetVar() {
  return getToken(CyanaMRParser::SetVar, 0);
}


size_t CyanaMRParser::Set_variableContext::getRuleIndex() const {
  return CyanaMRParser::RuleSet_variable;
}


std::any CyanaMRParser::Set_variableContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitSet_variable(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Set_variableContext* CyanaMRParser::set_variable() {
  Set_variableContext *_localctx = _tracker.createInstance<Set_variableContext>(_ctx, getState());
  enterRule(_localctx, 98, CyanaMRParser::RuleSet_variable);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(689);
    match(CyanaMRParser::SetVar);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Unset_variableContext ------------------------------------------------------------------

CyanaMRParser::Unset_variableContext::Unset_variableContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Unset_variableContext::Unset() {
  return getToken(CyanaMRParser::Unset, 0);
}

tree::TerminalNode* CyanaMRParser::Unset_variableContext::RETURN_VA() {
  return getToken(CyanaMRParser::RETURN_VA, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Unset_variableContext::Simple_name_VA() {
  return getTokens(CyanaMRParser::Simple_name_VA);
}

tree::TerminalNode* CyanaMRParser::Unset_variableContext::Simple_name_VA(size_t i) {
  return getToken(CyanaMRParser::Simple_name_VA, i);
}


size_t CyanaMRParser::Unset_variableContext::getRuleIndex() const {
  return CyanaMRParser::RuleUnset_variable;
}


std::any CyanaMRParser::Unset_variableContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitUnset_variable(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Unset_variableContext* CyanaMRParser::unset_variable() {
  Unset_variableContext *_localctx = _tracker.createInstance<Unset_variableContext>(_ctx, getState());
  enterRule(_localctx, 100, CyanaMRParser::RuleUnset_variable);
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
    setState(691);
    match(CyanaMRParser::Unset);
    setState(695);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CyanaMRParser::Simple_name_VA) {
      setState(692);
      match(CyanaMRParser::Simple_name_VA);
      setState(697);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(698);
    match(CyanaMRParser::RETURN_VA);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Print_macroContext ------------------------------------------------------------------

CyanaMRParser::Print_macroContext::Print_macroContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Print_macroContext::Print() {
  return getToken(CyanaMRParser::Print, 0);
}

tree::TerminalNode* CyanaMRParser::Print_macroContext::Double_quote_string() {
  return getToken(CyanaMRParser::Double_quote_string, 0);
}

tree::TerminalNode* CyanaMRParser::Print_macroContext::RETURN_PR() {
  return getToken(CyanaMRParser::RETURN_PR, 0);
}


size_t CyanaMRParser::Print_macroContext::getRuleIndex() const {
  return CyanaMRParser::RulePrint_macro;
}


std::any CyanaMRParser::Print_macroContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitPrint_macro(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Print_macroContext* CyanaMRParser::print_macro() {
  Print_macroContext *_localctx = _tracker.createInstance<Print_macroContext>(_ctx, getState());
  enterRule(_localctx, 102, CyanaMRParser::RulePrint_macro);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(700);
    match(CyanaMRParser::Print);
    setState(701);
    match(CyanaMRParser::Double_quote_string);
    setState(702);
    match(CyanaMRParser::RETURN_PR);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Unambig_atom_name_mappingContext ------------------------------------------------------------------

CyanaMRParser::Unambig_atom_name_mappingContext::Unambig_atom_name_mappingContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Unambig_atom_name_mappingContext::Residue() {
  return getToken(CyanaMRParser::Residue, 0);
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Unambig_atom_name_mappingContext::gen_simple_name() {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(0);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Unambig_atom_name_mappingContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Unambig_atom_name_mappingContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::Mapping_listContext *> CyanaMRParser::Unambig_atom_name_mappingContext::mapping_list() {
  return getRuleContexts<CyanaMRParser::Mapping_listContext>();
}

CyanaMRParser::Mapping_listContext* CyanaMRParser::Unambig_atom_name_mappingContext::mapping_list(size_t i) {
  return getRuleContext<CyanaMRParser::Mapping_listContext>(i);
}


size_t CyanaMRParser::Unambig_atom_name_mappingContext::getRuleIndex() const {
  return CyanaMRParser::RuleUnambig_atom_name_mapping;
}


std::any CyanaMRParser::Unambig_atom_name_mappingContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitUnambig_atom_name_mapping(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Unambig_atom_name_mappingContext* CyanaMRParser::unambig_atom_name_mapping() {
  Unambig_atom_name_mappingContext *_localctx = _tracker.createInstance<Unambig_atom_name_mappingContext>(_ctx, getState());
  enterRule(_localctx, 104, CyanaMRParser::RuleUnambig_atom_name_mapping);

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
    setState(704);
    match(CyanaMRParser::Residue);
    setState(705);
    gen_simple_name();
    setState(707);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 92, _ctx)) {
    case 1: {
      setState(706);
      comment();
      break;
    }

    default:
      break;
    }
    setState(711); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(711);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Mapping: {
                  setState(709);
                  mapping_list();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(710);
                  comment();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(713); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 94, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Mapping_listContext ------------------------------------------------------------------

CyanaMRParser::Mapping_listContext::Mapping_listContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Mapping_listContext::Mapping() {
  return getToken(CyanaMRParser::Mapping, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Mapping_listContext::Simple_name_MP() {
  return getTokens(CyanaMRParser::Simple_name_MP);
}

tree::TerminalNode* CyanaMRParser::Mapping_listContext::Simple_name_MP(size_t i) {
  return getToken(CyanaMRParser::Simple_name_MP, i);
}

tree::TerminalNode* CyanaMRParser::Mapping_listContext::Equ_op_MP() {
  return getToken(CyanaMRParser::Equ_op_MP, 0);
}

tree::TerminalNode* CyanaMRParser::Mapping_listContext::RETURN_MP() {
  return getToken(CyanaMRParser::RETURN_MP, 0);
}


size_t CyanaMRParser::Mapping_listContext::getRuleIndex() const {
  return CyanaMRParser::RuleMapping_list;
}


std::any CyanaMRParser::Mapping_listContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitMapping_list(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Mapping_listContext* CyanaMRParser::mapping_list() {
  Mapping_listContext *_localctx = _tracker.createInstance<Mapping_listContext>(_ctx, getState());
  enterRule(_localctx, 106, CyanaMRParser::RuleMapping_list);
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
    setState(715);
    match(CyanaMRParser::Mapping);
    setState(716);
    match(CyanaMRParser::Simple_name_MP);
    setState(717);
    match(CyanaMRParser::Equ_op_MP);
    setState(719); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(718);
      match(CyanaMRParser::Simple_name_MP);
      setState(721); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == CyanaMRParser::Simple_name_MP);
    setState(723);
    match(CyanaMRParser::RETURN_MP);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ambig_atom_name_mappingContext ------------------------------------------------------------------

CyanaMRParser::Ambig_atom_name_mappingContext::Ambig_atom_name_mappingContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Ambig_atom_name_mappingContext::Residue() {
  return getToken(CyanaMRParser::Residue, 0);
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::Ambig_atom_name_mappingContext::gen_simple_name() {
  return getRuleContext<CyanaMRParser::Gen_simple_nameContext>(0);
}

std::vector<CyanaMRParser::CommentContext *> CyanaMRParser::Ambig_atom_name_mappingContext::comment() {
  return getRuleContexts<CyanaMRParser::CommentContext>();
}

CyanaMRParser::CommentContext* CyanaMRParser::Ambig_atom_name_mappingContext::comment(size_t i) {
  return getRuleContext<CyanaMRParser::CommentContext>(i);
}

std::vector<CyanaMRParser::Ambig_listContext *> CyanaMRParser::Ambig_atom_name_mappingContext::ambig_list() {
  return getRuleContexts<CyanaMRParser::Ambig_listContext>();
}

CyanaMRParser::Ambig_listContext* CyanaMRParser::Ambig_atom_name_mappingContext::ambig_list(size_t i) {
  return getRuleContext<CyanaMRParser::Ambig_listContext>(i);
}


size_t CyanaMRParser::Ambig_atom_name_mappingContext::getRuleIndex() const {
  return CyanaMRParser::RuleAmbig_atom_name_mapping;
}


std::any CyanaMRParser::Ambig_atom_name_mappingContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitAmbig_atom_name_mapping(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Ambig_atom_name_mappingContext* CyanaMRParser::ambig_atom_name_mapping() {
  Ambig_atom_name_mappingContext *_localctx = _tracker.createInstance<Ambig_atom_name_mappingContext>(_ctx, getState());
  enterRule(_localctx, 108, CyanaMRParser::RuleAmbig_atom_name_mapping);

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
    setState(725);
    match(CyanaMRParser::Residue);
    setState(726);
    gen_simple_name();
    setState(728);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 96, _ctx)) {
    case 1: {
      setState(727);
      comment();
      break;
    }

    default:
      break;
    }
    setState(732); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(732);
              _errHandler->sync(this);
              switch (_input->LA(1)) {
                case CyanaMRParser::Ambig: {
                  setState(730);
                  ambig_list();
                  break;
                }

                case CyanaMRParser::COMMENT: {
                  setState(731);
                  comment();
                  break;
                }

              default:
                throw NoViableAltException(this);
              }
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(734); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 98, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Ambig_listContext ------------------------------------------------------------------

CyanaMRParser::Ambig_listContext::Ambig_listContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Ambig_listContext::Ambig() {
  return getToken(CyanaMRParser::Ambig, 0);
}

tree::TerminalNode* CyanaMRParser::Ambig_listContext::Equ_op_MP() {
  return getToken(CyanaMRParser::Equ_op_MP, 0);
}

tree::TerminalNode* CyanaMRParser::Ambig_listContext::RETURN_MP() {
  return getToken(CyanaMRParser::RETURN_MP, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Ambig_listContext::Simple_name_MP() {
  return getTokens(CyanaMRParser::Simple_name_MP);
}

tree::TerminalNode* CyanaMRParser::Ambig_listContext::Simple_name_MP(size_t i) {
  return getToken(CyanaMRParser::Simple_name_MP, i);
}

tree::TerminalNode* CyanaMRParser::Ambig_listContext::Ambig_code_MP() {
  return getToken(CyanaMRParser::Ambig_code_MP, 0);
}

std::vector<tree::TerminalNode *> CyanaMRParser::Ambig_listContext::Integer_MP() {
  return getTokens(CyanaMRParser::Integer_MP);
}

tree::TerminalNode* CyanaMRParser::Ambig_listContext::Integer_MP(size_t i) {
  return getToken(CyanaMRParser::Integer_MP, i);
}


size_t CyanaMRParser::Ambig_listContext::getRuleIndex() const {
  return CyanaMRParser::RuleAmbig_list;
}


std::any CyanaMRParser::Ambig_listContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitAmbig_list(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Ambig_listContext* CyanaMRParser::ambig_list() {
  Ambig_listContext *_localctx = _tracker.createInstance<Ambig_listContext>(_ctx, getState());
  enterRule(_localctx, 110, CyanaMRParser::RuleAmbig_list);
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
    setState(736);
    match(CyanaMRParser::Ambig);
    setState(737);
    _la = _input->LA(1);
    if (!(_la == CyanaMRParser::Ambig_code_MP

    || _la == CyanaMRParser::Simple_name_MP)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(738);
    match(CyanaMRParser::Equ_op_MP);
    setState(741); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(739);
      match(CyanaMRParser::Simple_name_MP);
      setState(740);
      match(CyanaMRParser::Integer_MP);
      setState(743); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == CyanaMRParser::Simple_name_MP);
    setState(745);
    match(CyanaMRParser::RETURN_MP);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- NumberContext ------------------------------------------------------------------

CyanaMRParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::NumberContext::Float() {
  return getToken(CyanaMRParser::Float, 0);
}

tree::TerminalNode* CyanaMRParser::NumberContext::Float_DecimalComma() {
  return getToken(CyanaMRParser::Float_DecimalComma, 0);
}

tree::TerminalNode* CyanaMRParser::NumberContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}


size_t CyanaMRParser::NumberContext::getRuleIndex() const {
  return CyanaMRParser::RuleNumber;
}


std::any CyanaMRParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::NumberContext* CyanaMRParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 112, CyanaMRParser::RuleNumber);
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
    setState(747);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 28) != 0))) {
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

//----------------- Gen_res_numContext ------------------------------------------------------------------

CyanaMRParser::Gen_res_numContext::Gen_res_numContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Gen_res_numContext::Integer() {
  return getToken(CyanaMRParser::Integer, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_res_numContext::Capital_integer() {
  return getToken(CyanaMRParser::Capital_integer, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_res_numContext::Integer_capital() {
  return getToken(CyanaMRParser::Integer_capital, 0);
}


size_t CyanaMRParser::Gen_res_numContext::getRuleIndex() const {
  return CyanaMRParser::RuleGen_res_num;
}


std::any CyanaMRParser::Gen_res_numContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitGen_res_num(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Gen_res_numContext* CyanaMRParser::gen_res_num() {
  Gen_res_numContext *_localctx = _tracker.createInstance<Gen_res_numContext>(_ctx, getState());
  enterRule(_localctx, 114, CyanaMRParser::RuleGen_res_num);
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
    setState(749);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 6442450948) != 0))) {
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

//----------------- Gen_simple_nameContext ------------------------------------------------------------------

CyanaMRParser::Gen_simple_nameContext::Gen_simple_nameContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Gen_simple_nameContext::Simple_name() {
  return getToken(CyanaMRParser::Simple_name, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_simple_nameContext::Capital_integer() {
  return getToken(CyanaMRParser::Capital_integer, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_simple_nameContext::Integer_capital() {
  return getToken(CyanaMRParser::Integer_capital, 0);
}


size_t CyanaMRParser::Gen_simple_nameContext::getRuleIndex() const {
  return CyanaMRParser::RuleGen_simple_name;
}


std::any CyanaMRParser::Gen_simple_nameContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitGen_simple_name(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Gen_simple_nameContext* CyanaMRParser::gen_simple_name() {
  Gen_simple_nameContext *_localctx = _tracker.createInstance<Gen_simple_nameContext>(_ctx, getState());
  enterRule(_localctx, 116, CyanaMRParser::RuleGen_simple_name);
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
    setState(751);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 15032385536) != 0))) {
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

//----------------- Gen_atom_nameContext ------------------------------------------------------------------

CyanaMRParser::Gen_atom_nameContext::Gen_atom_nameContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CyanaMRParser::Gen_atom_nameContext::Simple_name() {
  return getToken(CyanaMRParser::Simple_name, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_atom_nameContext::Capital_integer() {
  return getToken(CyanaMRParser::Capital_integer, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_atom_nameContext::Integer_capital() {
  return getToken(CyanaMRParser::Integer_capital, 0);
}

tree::TerminalNode* CyanaMRParser::Gen_atom_nameContext::Ambig_code() {
  return getToken(CyanaMRParser::Ambig_code, 0);
}


size_t CyanaMRParser::Gen_atom_nameContext::getRuleIndex() const {
  return CyanaMRParser::RuleGen_atom_name;
}


std::any CyanaMRParser::Gen_atom_nameContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<CyanaMRParserVisitor*>(visitor))
    return parserVisitor->visitGen_atom_name(this);
  else
    return visitor->visitChildren(this);
}

CyanaMRParser::Gen_atom_nameContext* CyanaMRParser::gen_atom_name() {
  Gen_atom_nameContext *_localctx = _tracker.createInstance<Gen_atom_nameContext>(_ctx, getState());
  enterRule(_localctx, 118, CyanaMRParser::RuleGen_atom_name);
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
    setState(753);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 15032385538) != 0))) {
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

void CyanaMRParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  cyanamrparserParserInitialize();
#else
  ::antlr4::internal::call_once(cyanamrparserParserOnceFlag, cyanamrparserParserInitialize);
#endif
}
