
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrViewPKParser.g4 by ANTLR 4.13.2


#include "NmrViewPKParserVisitor.h"

#include "NmrViewPKParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct NmrViewPKParserStaticData final {
  NmrViewPKParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  NmrViewPKParserStaticData(const NmrViewPKParserStaticData&) = delete;
  NmrViewPKParserStaticData(NmrViewPKParserStaticData&&) = delete;
  NmrViewPKParserStaticData& operator=(const NmrViewPKParserStaticData&) = delete;
  NmrViewPKParserStaticData& operator=(NmrViewPKParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag nmrviewpkparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<NmrViewPKParserStaticData> nmrviewpkparserParserStaticData = nullptr;

void nmrviewpkparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (nmrviewpkparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(nmrviewpkparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<NmrViewPKParserStaticData>(
    std::vector<std::string>{
      "nmrview_pk", "data_label", "labels", "peak_list_2d", "peak_2d", "peak_list_3d", 
      "peak_3d", "peak_list_4d", "peak_4d", "peak_list_wo_eju_2d", "peak_wo_eju_2d", 
      "peak_list_wo_eju_3d", "peak_wo_eju_3d", "peak_list_wo_eju_4d", "peak_wo_eju_4d", 
      "label", "jcoupling", "number", "enclose_data"
    },
    std::vector<std::string>{
      "", "'label'", "", "", "", "", "", "", "", "", "", "", "", "", "'dataset'", 
      "'sw'", "'sf'", "'condition'", "", "", "", "", "", "", "", "'vol'", 
      "'int'", "'stat'", "'comment'", "", "", "", "", "'\\n'"
    },
    std::vector<std::string>{
      "", "Label", "Integer", "Float", "Real", "SHARP_COMMENT", "EXCLM_COMMENT", 
      "SMCLN_COMMENT", "Simple_name", "SPACE", "RETURN", "L_brace", "SECTION_COMMENT", 
      "LINE_COMMENT", "Dataset", "Sw", "Sf", "Condition", "L_name", "P_name", 
      "W_name", "B_name", "E_name", "J_name", "U_name", "Vol", "Int", "Stat", 
      "Comment", "Flag0", "Simple_name_LA", "Float_LA", "SPACE_LA", "SINGLE_NL_LA", 
      "ENCLOSE_DATA_LA", "Any_name", "SPACE_CM", "R_brace"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,37,494,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,3,0,40,8,0,1,0,1,0,1,0,
  	1,0,1,0,1,0,1,0,1,0,5,0,50,8,0,10,0,12,0,53,9,0,1,0,1,0,1,1,1,1,1,1,1,
  	1,1,1,3,1,62,8,1,1,1,5,1,65,8,1,10,1,12,1,68,9,1,1,1,1,1,4,1,72,8,1,11,
  	1,12,1,73,1,1,5,1,77,8,1,10,1,12,1,80,9,1,1,1,4,1,83,8,1,11,1,12,1,84,
  	1,1,1,1,4,1,89,8,1,11,1,12,1,90,1,1,1,1,4,1,95,8,1,11,1,12,1,96,1,2,4,
  	2,100,8,2,11,2,12,2,101,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
  	3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,122,8,3,1,3,1,3,3,3,126,8,3,1,3,4,3,129,
  	8,3,11,3,12,3,130,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
  	1,4,1,4,1,4,1,4,1,4,1,4,3,4,152,8,4,1,4,4,4,155,8,4,11,4,12,4,156,1,4,
  	1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
  	5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,186,8,5,1,5,1,5,3,5,190,8,5,1,5,
  	4,5,193,8,5,11,5,12,5,194,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
  	1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,223,8,
  	6,1,6,4,6,226,8,6,11,6,12,6,227,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
  	7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
  	1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,264,8,7,1,7,1,7,3,7,268,8,7,1,7,4,7,271,
  	8,7,11,7,12,7,272,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
  	1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
  	8,1,8,1,8,3,8,308,8,8,1,8,4,8,311,8,8,11,8,12,8,312,1,8,1,8,1,9,1,9,1,
  	9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,329,8,9,1,9,1,9,3,9,333,8,9,
  	1,9,4,9,336,8,9,11,9,12,9,337,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
  	1,10,1,10,1,10,1,10,1,10,3,10,353,8,10,1,10,4,10,356,8,10,11,10,12,10,
  	357,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
  	1,11,1,11,1,11,1,11,1,11,3,11,378,8,11,1,11,1,11,3,11,382,8,11,1,11,4,
  	11,385,8,11,11,11,12,11,386,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
  	12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,406,8,12,1,12,4,12,409,
  	8,12,11,12,12,12,410,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
  	1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,435,
  	8,13,1,13,1,13,3,13,439,8,13,1,13,4,13,442,8,13,11,13,12,13,443,1,14,
  	1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
  	1,14,1,14,1,14,1,14,1,14,1,14,3,14,467,8,14,1,14,4,14,470,8,14,11,14,
  	12,14,471,1,14,1,14,1,15,1,15,1,16,1,16,1,16,3,16,481,8,16,1,17,1,17,
  	1,18,1,18,5,18,487,8,18,10,18,12,18,490,9,18,1,18,1,18,1,18,0,0,19,0,
  	2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,3,1,1,10,10,2,0,30,
  	31,34,34,2,0,2,4,8,8,524,0,39,1,0,0,0,2,56,1,0,0,0,4,99,1,0,0,0,6,103,
  	1,0,0,0,8,132,1,0,0,0,10,160,1,0,0,0,12,196,1,0,0,0,14,231,1,0,0,0,16,
  	274,1,0,0,0,18,316,1,0,0,0,20,339,1,0,0,0,22,361,1,0,0,0,24,388,1,0,0,
  	0,26,414,1,0,0,0,28,445,1,0,0,0,30,475,1,0,0,0,32,480,1,0,0,0,34,482,
  	1,0,0,0,36,484,1,0,0,0,38,40,5,10,0,0,39,38,1,0,0,0,39,40,1,0,0,0,40,
  	51,1,0,0,0,41,50,3,2,1,0,42,50,3,6,3,0,43,50,3,10,5,0,44,50,3,14,7,0,
  	45,50,3,18,9,0,46,50,3,22,11,0,47,50,3,26,13,0,48,50,5,10,0,0,49,41,1,
  	0,0,0,49,42,1,0,0,0,49,43,1,0,0,0,49,44,1,0,0,0,49,45,1,0,0,0,49,46,1,
  	0,0,0,49,47,1,0,0,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,
  	0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,0,0,1,55,1,1,0,0,0,56,57,5,
  	1,0,0,57,58,5,14,0,0,58,59,5,15,0,0,59,61,5,16,0,0,60,62,5,17,0,0,61,
  	60,1,0,0,0,61,62,1,0,0,0,62,66,1,0,0,0,63,65,5,33,0,0,64,63,1,0,0,0,65,
  	68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,0,68,66,1,0,0,0,69,
  	71,3,4,2,0,70,72,5,33,0,0,71,70,1,0,0,0,72,73,1,0,0,0,73,71,1,0,0,0,73,
  	74,1,0,0,0,74,78,1,0,0,0,75,77,5,30,0,0,76,75,1,0,0,0,77,80,1,0,0,0,78,
  	76,1,0,0,0,78,79,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,81,83,5,33,0,0,82,
  	81,1,0,0,0,83,84,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,86,1,0,0,0,86,
  	88,3,4,2,0,87,89,5,33,0,0,88,87,1,0,0,0,89,90,1,0,0,0,90,88,1,0,0,0,90,
  	91,1,0,0,0,91,92,1,0,0,0,92,94,3,4,2,0,93,95,5,33,0,0,94,93,1,0,0,0,95,
  	96,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,3,1,0,0,0,98,100,3,30,15,0,
  	99,98,1,0,0,0,100,101,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,5,1,
  	0,0,0,103,104,5,18,0,0,104,105,5,19,0,0,105,106,5,20,0,0,106,107,5,21,
  	0,0,107,108,5,22,0,0,108,109,5,23,0,0,109,110,5,24,0,0,110,111,5,18,0,
  	0,111,112,5,19,0,0,112,113,5,20,0,0,113,114,5,21,0,0,114,115,5,22,0,0,
  	115,116,5,23,0,0,116,117,5,24,0,0,117,118,5,25,0,0,118,119,5,26,0,0,119,
  	121,5,27,0,0,120,122,5,28,0,0,121,120,1,0,0,0,121,122,1,0,0,0,122,123,
  	1,0,0,0,123,125,5,29,0,0,124,126,5,10,0,0,125,124,1,0,0,0,125,126,1,0,
  	0,0,126,128,1,0,0,0,127,129,3,8,4,0,128,127,1,0,0,0,129,130,1,0,0,0,130,
  	128,1,0,0,0,130,131,1,0,0,0,131,7,1,0,0,0,132,133,5,2,0,0,133,134,3,36,
  	18,0,134,135,3,34,17,0,135,136,3,34,17,0,136,137,3,34,17,0,137,138,5,
  	8,0,0,138,139,3,32,16,0,139,140,3,36,18,0,140,141,3,36,18,0,141,142,3,
  	34,17,0,142,143,3,34,17,0,143,144,3,34,17,0,144,145,5,8,0,0,145,146,3,
  	32,16,0,146,147,3,36,18,0,147,148,3,34,17,0,148,149,3,34,17,0,149,151,
  	5,2,0,0,150,152,3,36,18,0,151,150,1,0,0,0,151,152,1,0,0,0,152,154,1,0,
  	0,0,153,155,5,2,0,0,154,153,1,0,0,0,155,156,1,0,0,0,156,154,1,0,0,0,156,
  	157,1,0,0,0,157,158,1,0,0,0,158,159,7,0,0,0,159,9,1,0,0,0,160,161,5,18,
  	0,0,161,162,5,19,0,0,162,163,5,20,0,0,163,164,5,21,0,0,164,165,5,22,0,
  	0,165,166,5,23,0,0,166,167,5,24,0,0,167,168,5,18,0,0,168,169,5,19,0,0,
  	169,170,5,20,0,0,170,171,5,21,0,0,171,172,5,22,0,0,172,173,5,23,0,0,173,
  	174,5,24,0,0,174,175,5,18,0,0,175,176,5,19,0,0,176,177,5,20,0,0,177,178,
  	5,21,0,0,178,179,5,22,0,0,179,180,5,23,0,0,180,181,5,24,0,0,181,182,5,
  	25,0,0,182,183,5,26,0,0,183,185,5,27,0,0,184,186,5,28,0,0,185,184,1,0,
  	0,0,185,186,1,0,0,0,186,187,1,0,0,0,187,189,5,29,0,0,188,190,5,10,0,0,
  	189,188,1,0,0,0,189,190,1,0,0,0,190,192,1,0,0,0,191,193,3,12,6,0,192,
  	191,1,0,0,0,193,194,1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,0,195,11,1,
  	0,0,0,196,197,5,2,0,0,197,198,3,36,18,0,198,199,3,34,17,0,199,200,3,34,
  	17,0,200,201,3,34,17,0,201,202,5,8,0,0,202,203,3,32,16,0,203,204,3,36,
  	18,0,204,205,3,36,18,0,205,206,3,34,17,0,206,207,3,34,17,0,207,208,3,
  	34,17,0,208,209,5,8,0,0,209,210,3,32,16,0,210,211,3,36,18,0,211,212,3,
  	36,18,0,212,213,3,34,17,0,213,214,3,34,17,0,214,215,3,34,17,0,215,216,
  	5,8,0,0,216,217,3,32,16,0,217,218,3,36,18,0,218,219,3,34,17,0,219,220,
  	3,34,17,0,220,222,5,2,0,0,221,223,3,36,18,0,222,221,1,0,0,0,222,223,1,
  	0,0,0,223,225,1,0,0,0,224,226,5,2,0,0,225,224,1,0,0,0,226,227,1,0,0,0,
  	227,225,1,0,0,0,227,228,1,0,0,0,228,229,1,0,0,0,229,230,7,0,0,0,230,13,
  	1,0,0,0,231,232,5,18,0,0,232,233,5,19,0,0,233,234,5,20,0,0,234,235,5,
  	21,0,0,235,236,5,22,0,0,236,237,5,23,0,0,237,238,5,24,0,0,238,239,5,18,
  	0,0,239,240,5,19,0,0,240,241,5,20,0,0,241,242,5,21,0,0,242,243,5,22,0,
  	0,243,244,5,23,0,0,244,245,5,24,0,0,245,246,5,18,0,0,246,247,5,19,0,0,
  	247,248,5,20,0,0,248,249,5,21,0,0,249,250,5,22,0,0,250,251,5,23,0,0,251,
  	252,5,24,0,0,252,253,5,18,0,0,253,254,5,19,0,0,254,255,5,20,0,0,255,256,
  	5,21,0,0,256,257,5,22,0,0,257,258,5,23,0,0,258,259,5,24,0,0,259,260,5,
  	25,0,0,260,261,5,26,0,0,261,263,5,27,0,0,262,264,5,28,0,0,263,262,1,0,
  	0,0,263,264,1,0,0,0,264,265,1,0,0,0,265,267,5,29,0,0,266,268,5,10,0,0,
  	267,266,1,0,0,0,267,268,1,0,0,0,268,270,1,0,0,0,269,271,3,16,8,0,270,
  	269,1,0,0,0,271,272,1,0,0,0,272,270,1,0,0,0,272,273,1,0,0,0,273,15,1,
  	0,0,0,274,275,5,2,0,0,275,276,3,36,18,0,276,277,3,34,17,0,277,278,3,34,
  	17,0,278,279,3,34,17,0,279,280,5,8,0,0,280,281,3,32,16,0,281,282,3,36,
  	18,0,282,283,3,36,18,0,283,284,3,34,17,0,284,285,3,34,17,0,285,286,3,
  	34,17,0,286,287,5,8,0,0,287,288,3,32,16,0,288,289,3,36,18,0,289,290,3,
  	36,18,0,290,291,3,34,17,0,291,292,3,34,17,0,292,293,3,34,17,0,293,294,
  	5,8,0,0,294,295,3,32,16,0,295,296,3,36,18,0,296,297,3,36,18,0,297,298,
  	3,34,17,0,298,299,3,34,17,0,299,300,3,34,17,0,300,301,5,8,0,0,301,302,
  	3,32,16,0,302,303,3,36,18,0,303,304,3,34,17,0,304,305,3,34,17,0,305,307,
  	5,2,0,0,306,308,3,36,18,0,307,306,1,0,0,0,307,308,1,0,0,0,308,310,1,0,
  	0,0,309,311,5,2,0,0,310,309,1,0,0,0,311,312,1,0,0,0,312,310,1,0,0,0,312,
  	313,1,0,0,0,313,314,1,0,0,0,314,315,7,0,0,0,315,17,1,0,0,0,316,317,5,
  	18,0,0,317,318,5,19,0,0,318,319,5,20,0,0,319,320,5,21,0,0,320,321,5,18,
  	0,0,321,322,5,19,0,0,322,323,5,20,0,0,323,324,5,21,0,0,324,325,5,25,0,
  	0,325,326,5,26,0,0,326,328,5,27,0,0,327,329,5,28,0,0,328,327,1,0,0,0,
  	328,329,1,0,0,0,329,330,1,0,0,0,330,332,5,29,0,0,331,333,5,10,0,0,332,
  	331,1,0,0,0,332,333,1,0,0,0,333,335,1,0,0,0,334,336,3,20,10,0,335,334,
  	1,0,0,0,336,337,1,0,0,0,337,335,1,0,0,0,337,338,1,0,0,0,338,19,1,0,0,
  	0,339,340,5,2,0,0,340,341,3,36,18,0,341,342,3,34,17,0,342,343,3,34,17,
  	0,343,344,3,34,17,0,344,345,3,36,18,0,345,346,3,34,17,0,346,347,3,34,
  	17,0,347,348,3,34,17,0,348,349,3,34,17,0,349,350,3,34,17,0,350,352,5,
  	2,0,0,351,353,3,36,18,0,352,351,1,0,0,0,352,353,1,0,0,0,353,355,1,0,0,
  	0,354,356,5,2,0,0,355,354,1,0,0,0,356,357,1,0,0,0,357,355,1,0,0,0,357,
  	358,1,0,0,0,358,359,1,0,0,0,359,360,7,0,0,0,360,21,1,0,0,0,361,362,5,
  	18,0,0,362,363,5,19,0,0,363,364,5,20,0,0,364,365,5,21,0,0,365,366,5,18,
  	0,0,366,367,5,19,0,0,367,368,5,20,0,0,368,369,5,21,0,0,369,370,5,18,0,
  	0,370,371,5,19,0,0,371,372,5,20,0,0,372,373,5,21,0,0,373,374,5,25,0,0,
  	374,375,5,26,0,0,375,377,5,27,0,0,376,378,5,28,0,0,377,376,1,0,0,0,377,
  	378,1,0,0,0,378,379,1,0,0,0,379,381,5,29,0,0,380,382,5,10,0,0,381,380,
  	1,0,0,0,381,382,1,0,0,0,382,384,1,0,0,0,383,385,3,24,12,0,384,383,1,0,
  	0,0,385,386,1,0,0,0,386,384,1,0,0,0,386,387,1,0,0,0,387,23,1,0,0,0,388,
  	389,5,2,0,0,389,390,3,36,18,0,390,391,3,34,17,0,391,392,3,34,17,0,392,
  	393,3,34,17,0,393,394,3,36,18,0,394,395,3,34,17,0,395,396,3,34,17,0,396,
  	397,3,34,17,0,397,398,3,36,18,0,398,399,3,34,17,0,399,400,3,34,17,0,400,
  	401,3,34,17,0,401,402,3,34,17,0,402,403,3,34,17,0,403,405,5,2,0,0,404,
  	406,3,36,18,0,405,404,1,0,0,0,405,406,1,0,0,0,406,408,1,0,0,0,407,409,
  	5,2,0,0,408,407,1,0,0,0,409,410,1,0,0,0,410,408,1,0,0,0,410,411,1,0,0,
  	0,411,412,1,0,0,0,412,413,7,0,0,0,413,25,1,0,0,0,414,415,5,18,0,0,415,
  	416,5,19,0,0,416,417,5,20,0,0,417,418,5,21,0,0,418,419,5,18,0,0,419,420,
  	5,19,0,0,420,421,5,20,0,0,421,422,5,21,0,0,422,423,5,18,0,0,423,424,5,
  	19,0,0,424,425,5,20,0,0,425,426,5,21,0,0,426,427,5,18,0,0,427,428,5,19,
  	0,0,428,429,5,20,0,0,429,430,5,21,0,0,430,431,5,25,0,0,431,432,5,26,0,
  	0,432,434,5,27,0,0,433,435,5,28,0,0,434,433,1,0,0,0,434,435,1,0,0,0,435,
  	436,1,0,0,0,436,438,5,29,0,0,437,439,5,10,0,0,438,437,1,0,0,0,438,439,
  	1,0,0,0,439,441,1,0,0,0,440,442,3,28,14,0,441,440,1,0,0,0,442,443,1,0,
  	0,0,443,441,1,0,0,0,443,444,1,0,0,0,444,27,1,0,0,0,445,446,5,2,0,0,446,
  	447,3,36,18,0,447,448,3,34,17,0,448,449,3,34,17,0,449,450,3,34,17,0,450,
  	451,3,36,18,0,451,452,3,34,17,0,452,453,3,34,17,0,453,454,3,34,17,0,454,
  	455,3,36,18,0,455,456,3,34,17,0,456,457,3,34,17,0,457,458,3,34,17,0,458,
  	459,3,36,18,0,459,460,3,34,17,0,460,461,3,34,17,0,461,462,3,34,17,0,462,
  	463,3,34,17,0,463,464,3,34,17,0,464,466,5,2,0,0,465,467,3,36,18,0,466,
  	465,1,0,0,0,466,467,1,0,0,0,467,469,1,0,0,0,468,470,5,2,0,0,469,468,1,
  	0,0,0,470,471,1,0,0,0,471,469,1,0,0,0,471,472,1,0,0,0,472,473,1,0,0,0,
  	473,474,7,0,0,0,474,29,1,0,0,0,475,476,7,1,0,0,476,31,1,0,0,0,477,481,
  	5,3,0,0,478,481,5,8,0,0,479,481,3,36,18,0,480,477,1,0,0,0,480,478,1,0,
  	0,0,480,479,1,0,0,0,481,33,1,0,0,0,482,483,7,2,0,0,483,35,1,0,0,0,484,
  	488,5,11,0,0,485,487,5,35,0,0,486,485,1,0,0,0,487,490,1,0,0,0,488,486,
  	1,0,0,0,488,489,1,0,0,0,489,491,1,0,0,0,490,488,1,0,0,0,491,492,5,37,
  	0,0,492,37,1,0,0,0,43,39,49,51,61,66,73,78,84,90,96,101,121,125,130,151,
  	156,185,189,194,222,227,263,267,272,307,312,328,332,337,352,357,377,381,
  	386,405,410,434,438,443,466,471,480,488
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  nmrviewpkparserParserStaticData = std::move(staticData);
}

}

NmrViewPKParser::NmrViewPKParser(TokenStream *input) : NmrViewPKParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

NmrViewPKParser::NmrViewPKParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  NmrViewPKParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *nmrviewpkparserParserStaticData->atn, nmrviewpkparserParserStaticData->decisionToDFA, nmrviewpkparserParserStaticData->sharedContextCache, options);
}

NmrViewPKParser::~NmrViewPKParser() {
  delete _interpreter;
}

const atn::ATN& NmrViewPKParser::getATN() const {
  return *nmrviewpkparserParserStaticData->atn;
}

std::string NmrViewPKParser::getGrammarFileName() const {
  return "NmrViewPKParser.g4";
}

const std::vector<std::string>& NmrViewPKParser::getRuleNames() const {
  return nmrviewpkparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& NmrViewPKParser::getVocabulary() const {
  return nmrviewpkparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView NmrViewPKParser::getSerializedATN() const {
  return nmrviewpkparserParserStaticData->serializedATN;
}


//----------------- Nmrview_pkContext ------------------------------------------------------------------

NmrViewPKParser::Nmrview_pkContext::Nmrview_pkContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrViewPKParser::Nmrview_pkContext::EOF() {
  return getToken(NmrViewPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Nmrview_pkContext::RETURN() {
  return getTokens(NmrViewPKParser::RETURN);
}

tree::TerminalNode* NmrViewPKParser::Nmrview_pkContext::RETURN(size_t i) {
  return getToken(NmrViewPKParser::RETURN, i);
}

std::vector<NmrViewPKParser::Data_labelContext *> NmrViewPKParser::Nmrview_pkContext::data_label() {
  return getRuleContexts<NmrViewPKParser::Data_labelContext>();
}

NmrViewPKParser::Data_labelContext* NmrViewPKParser::Nmrview_pkContext::data_label(size_t i) {
  return getRuleContext<NmrViewPKParser::Data_labelContext>(i);
}

std::vector<NmrViewPKParser::Peak_list_2dContext *> NmrViewPKParser::Nmrview_pkContext::peak_list_2d() {
  return getRuleContexts<NmrViewPKParser::Peak_list_2dContext>();
}

NmrViewPKParser::Peak_list_2dContext* NmrViewPKParser::Nmrview_pkContext::peak_list_2d(size_t i) {
  return getRuleContext<NmrViewPKParser::Peak_list_2dContext>(i);
}

std::vector<NmrViewPKParser::Peak_list_3dContext *> NmrViewPKParser::Nmrview_pkContext::peak_list_3d() {
  return getRuleContexts<NmrViewPKParser::Peak_list_3dContext>();
}

NmrViewPKParser::Peak_list_3dContext* NmrViewPKParser::Nmrview_pkContext::peak_list_3d(size_t i) {
  return getRuleContext<NmrViewPKParser::Peak_list_3dContext>(i);
}

std::vector<NmrViewPKParser::Peak_list_4dContext *> NmrViewPKParser::Nmrview_pkContext::peak_list_4d() {
  return getRuleContexts<NmrViewPKParser::Peak_list_4dContext>();
}

NmrViewPKParser::Peak_list_4dContext* NmrViewPKParser::Nmrview_pkContext::peak_list_4d(size_t i) {
  return getRuleContext<NmrViewPKParser::Peak_list_4dContext>(i);
}

std::vector<NmrViewPKParser::Peak_list_wo_eju_2dContext *> NmrViewPKParser::Nmrview_pkContext::peak_list_wo_eju_2d() {
  return getRuleContexts<NmrViewPKParser::Peak_list_wo_eju_2dContext>();
}

NmrViewPKParser::Peak_list_wo_eju_2dContext* NmrViewPKParser::Nmrview_pkContext::peak_list_wo_eju_2d(size_t i) {
  return getRuleContext<NmrViewPKParser::Peak_list_wo_eju_2dContext>(i);
}

std::vector<NmrViewPKParser::Peak_list_wo_eju_3dContext *> NmrViewPKParser::Nmrview_pkContext::peak_list_wo_eju_3d() {
  return getRuleContexts<NmrViewPKParser::Peak_list_wo_eju_3dContext>();
}

NmrViewPKParser::Peak_list_wo_eju_3dContext* NmrViewPKParser::Nmrview_pkContext::peak_list_wo_eju_3d(size_t i) {
  return getRuleContext<NmrViewPKParser::Peak_list_wo_eju_3dContext>(i);
}

std::vector<NmrViewPKParser::Peak_list_wo_eju_4dContext *> NmrViewPKParser::Nmrview_pkContext::peak_list_wo_eju_4d() {
  return getRuleContexts<NmrViewPKParser::Peak_list_wo_eju_4dContext>();
}

NmrViewPKParser::Peak_list_wo_eju_4dContext* NmrViewPKParser::Nmrview_pkContext::peak_list_wo_eju_4d(size_t i) {
  return getRuleContext<NmrViewPKParser::Peak_list_wo_eju_4dContext>(i);
}


size_t NmrViewPKParser::Nmrview_pkContext::getRuleIndex() const {
  return NmrViewPKParser::RuleNmrview_pk;
}


std::any NmrViewPKParser::Nmrview_pkContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewPKParserVisitor*>(visitor))
    return parserVisitor->visitNmrview_pk(this);
  else
    return visitor->visitChildren(this);
}

NmrViewPKParser::Nmrview_pkContext* NmrViewPKParser::nmrview_pk() {
  Nmrview_pkContext *_localctx = _tracker.createInstance<Nmrview_pkContext>(_ctx, getState());
  enterRule(_localctx, 0, NmrViewPKParser::RuleNmrview_pk);
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
    setState(39);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
    case 1: {
      setState(38);
      match(NmrViewPKParser::RETURN);
      break;
    }

    default:
      break;
    }
    setState(51);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 263170) != 0)) {
      setState(49);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx)) {
      case 1: {
        setState(41);
        data_label();
        break;
      }

      case 2: {
        setState(42);
        peak_list_2d();
        break;
      }

      case 3: {
        setState(43);
        peak_list_3d();
        break;
      }

      case 4: {
        setState(44);
        peak_list_4d();
        break;
      }

      case 5: {
        setState(45);
        peak_list_wo_eju_2d();
        break;
      }

      case 6: {
        setState(46);
        peak_list_wo_eju_3d();
        break;
      }

      case 7: {
        setState(47);
        peak_list_wo_eju_4d();
        break;
      }

      case 8: {
        setState(48);
        match(NmrViewPKParser::RETURN);
        break;
      }

      default:
        break;
      }
      setState(53);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(54);
    match(NmrViewPKParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Data_labelContext ------------------------------------------------------------------

NmrViewPKParser::Data_labelContext::Data_labelContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrViewPKParser::Data_labelContext::Label() {
  return getToken(NmrViewPKParser::Label, 0);
}

tree::TerminalNode* NmrViewPKParser::Data_labelContext::Dataset() {
  return getToken(NmrViewPKParser::Dataset, 0);
}

tree::TerminalNode* NmrViewPKParser::Data_labelContext::Sw() {
  return getToken(NmrViewPKParser::Sw, 0);
}

tree::TerminalNode* NmrViewPKParser::Data_labelContext::Sf() {
  return getToken(NmrViewPKParser::Sf, 0);
}

std::vector<NmrViewPKParser::LabelsContext *> NmrViewPKParser::Data_labelContext::labels() {
  return getRuleContexts<NmrViewPKParser::LabelsContext>();
}

NmrViewPKParser::LabelsContext* NmrViewPKParser::Data_labelContext::labels(size_t i) {
  return getRuleContext<NmrViewPKParser::LabelsContext>(i);
}

tree::TerminalNode* NmrViewPKParser::Data_labelContext::Condition() {
  return getToken(NmrViewPKParser::Condition, 0);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Data_labelContext::SINGLE_NL_LA() {
  return getTokens(NmrViewPKParser::SINGLE_NL_LA);
}

tree::TerminalNode* NmrViewPKParser::Data_labelContext::SINGLE_NL_LA(size_t i) {
  return getToken(NmrViewPKParser::SINGLE_NL_LA, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Data_labelContext::Simple_name_LA() {
  return getTokens(NmrViewPKParser::Simple_name_LA);
}

tree::TerminalNode* NmrViewPKParser::Data_labelContext::Simple_name_LA(size_t i) {
  return getToken(NmrViewPKParser::Simple_name_LA, i);
}


size_t NmrViewPKParser::Data_labelContext::getRuleIndex() const {
  return NmrViewPKParser::RuleData_label;
}


std::any NmrViewPKParser::Data_labelContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewPKParserVisitor*>(visitor))
    return parserVisitor->visitData_label(this);
  else
    return visitor->visitChildren(this);
}

NmrViewPKParser::Data_labelContext* NmrViewPKParser::data_label() {
  Data_labelContext *_localctx = _tracker.createInstance<Data_labelContext>(_ctx, getState());
  enterRule(_localctx, 2, NmrViewPKParser::RuleData_label);
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
    setState(56);
    match(NmrViewPKParser::Label);
    setState(57);
    match(NmrViewPKParser::Dataset);
    setState(58);
    match(NmrViewPKParser::Sw);
    setState(59);
    match(NmrViewPKParser::Sf);
    setState(61);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewPKParser::Condition) {
      setState(60);
      match(NmrViewPKParser::Condition);
    }
    setState(66);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == NmrViewPKParser::SINGLE_NL_LA) {
      setState(63);
      match(NmrViewPKParser::SINGLE_NL_LA);
      setState(68);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(69);
    labels();
    setState(71); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(70);
              match(NmrViewPKParser::SINGLE_NL_LA);
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(73); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 5, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(78);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == NmrViewPKParser::Simple_name_LA) {
      setState(75);
      match(NmrViewPKParser::Simple_name_LA);
      setState(80);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(82); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(81);
      match(NmrViewPKParser::SINGLE_NL_LA);
      setState(84); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewPKParser::SINGLE_NL_LA);
    setState(86);
    labels();
    setState(88); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(87);
      match(NmrViewPKParser::SINGLE_NL_LA);
      setState(90); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewPKParser::SINGLE_NL_LA);
    setState(92);
    labels();
    setState(94); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(93);
      match(NmrViewPKParser::SINGLE_NL_LA);
      setState(96); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewPKParser::SINGLE_NL_LA);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- LabelsContext ------------------------------------------------------------------

NmrViewPKParser::LabelsContext::LabelsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<NmrViewPKParser::LabelContext *> NmrViewPKParser::LabelsContext::label() {
  return getRuleContexts<NmrViewPKParser::LabelContext>();
}

NmrViewPKParser::LabelContext* NmrViewPKParser::LabelsContext::label(size_t i) {
  return getRuleContext<NmrViewPKParser::LabelContext>(i);
}


size_t NmrViewPKParser::LabelsContext::getRuleIndex() const {
  return NmrViewPKParser::RuleLabels;
}


std::any NmrViewPKParser::LabelsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewPKParserVisitor*>(visitor))
    return parserVisitor->visitLabels(this);
  else
    return visitor->visitChildren(this);
}

NmrViewPKParser::LabelsContext* NmrViewPKParser::labels() {
  LabelsContext *_localctx = _tracker.createInstance<LabelsContext>(_ctx, getState());
  enterRule(_localctx, 4, NmrViewPKParser::RuleLabels);
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
    setState(99); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(98);
      label();
      setState(101); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 20401094656) != 0));
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_list_2dContext ------------------------------------------------------------------

NmrViewPKParser::Peak_list_2dContext::Peak_list_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_2dContext::L_name() {
  return getTokens(NmrViewPKParser::L_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_2dContext::L_name(size_t i) {
  return getToken(NmrViewPKParser::L_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_2dContext::P_name() {
  return getTokens(NmrViewPKParser::P_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_2dContext::P_name(size_t i) {
  return getToken(NmrViewPKParser::P_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_2dContext::W_name() {
  return getTokens(NmrViewPKParser::W_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_2dContext::W_name(size_t i) {
  return getToken(NmrViewPKParser::W_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_2dContext::B_name() {
  return getTokens(NmrViewPKParser::B_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_2dContext::B_name(size_t i) {
  return getToken(NmrViewPKParser::B_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_2dContext::E_name() {
  return getTokens(NmrViewPKParser::E_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_2dContext::E_name(size_t i) {
  return getToken(NmrViewPKParser::E_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_2dContext::J_name() {
  return getTokens(NmrViewPKParser::J_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_2dContext::J_name(size_t i) {
  return getToken(NmrViewPKParser::J_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_2dContext::U_name() {
  return getTokens(NmrViewPKParser::U_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_2dContext::U_name(size_t i) {
  return getToken(NmrViewPKParser::U_name, i);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_2dContext::Vol() {
  return getToken(NmrViewPKParser::Vol, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_2dContext::Int() {
  return getToken(NmrViewPKParser::Int, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_2dContext::Stat() {
  return getToken(NmrViewPKParser::Stat, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_2dContext::Flag0() {
  return getToken(NmrViewPKParser::Flag0, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_2dContext::Comment() {
  return getToken(NmrViewPKParser::Comment, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_2dContext::RETURN() {
  return getToken(NmrViewPKParser::RETURN, 0);
}

std::vector<NmrViewPKParser::Peak_2dContext *> NmrViewPKParser::Peak_list_2dContext::peak_2d() {
  return getRuleContexts<NmrViewPKParser::Peak_2dContext>();
}

NmrViewPKParser::Peak_2dContext* NmrViewPKParser::Peak_list_2dContext::peak_2d(size_t i) {
  return getRuleContext<NmrViewPKParser::Peak_2dContext>(i);
}


size_t NmrViewPKParser::Peak_list_2dContext::getRuleIndex() const {
  return NmrViewPKParser::RulePeak_list_2d;
}


std::any NmrViewPKParser::Peak_list_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_2d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewPKParser::Peak_list_2dContext* NmrViewPKParser::peak_list_2d() {
  Peak_list_2dContext *_localctx = _tracker.createInstance<Peak_list_2dContext>(_ctx, getState());
  enterRule(_localctx, 6, NmrViewPKParser::RulePeak_list_2d);
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
    setState(103);
    match(NmrViewPKParser::L_name);
    setState(104);
    match(NmrViewPKParser::P_name);
    setState(105);
    match(NmrViewPKParser::W_name);
    setState(106);
    match(NmrViewPKParser::B_name);
    setState(107);
    match(NmrViewPKParser::E_name);
    setState(108);
    match(NmrViewPKParser::J_name);
    setState(109);
    match(NmrViewPKParser::U_name);
    setState(110);
    match(NmrViewPKParser::L_name);
    setState(111);
    match(NmrViewPKParser::P_name);
    setState(112);
    match(NmrViewPKParser::W_name);
    setState(113);
    match(NmrViewPKParser::B_name);
    setState(114);
    match(NmrViewPKParser::E_name);
    setState(115);
    match(NmrViewPKParser::J_name);
    setState(116);
    match(NmrViewPKParser::U_name);
    setState(117);
    match(NmrViewPKParser::Vol);
    setState(118);
    match(NmrViewPKParser::Int);
    setState(119);
    match(NmrViewPKParser::Stat);
    setState(121);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewPKParser::Comment) {
      setState(120);
      match(NmrViewPKParser::Comment);
    }
    setState(123);
    match(NmrViewPKParser::Flag0);
    setState(125);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewPKParser::RETURN) {
      setState(124);
      match(NmrViewPKParser::RETURN);
    }
    setState(128); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(127);
      peak_2d();
      setState(130); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewPKParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_2dContext ------------------------------------------------------------------

NmrViewPKParser::Peak_2dContext::Peak_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_2dContext::Integer() {
  return getTokens(NmrViewPKParser::Integer);
}

tree::TerminalNode* NmrViewPKParser::Peak_2dContext::Integer(size_t i) {
  return getToken(NmrViewPKParser::Integer, i);
}

std::vector<NmrViewPKParser::Enclose_dataContext *> NmrViewPKParser::Peak_2dContext::enclose_data() {
  return getRuleContexts<NmrViewPKParser::Enclose_dataContext>();
}

NmrViewPKParser::Enclose_dataContext* NmrViewPKParser::Peak_2dContext::enclose_data(size_t i) {
  return getRuleContext<NmrViewPKParser::Enclose_dataContext>(i);
}

std::vector<NmrViewPKParser::NumberContext *> NmrViewPKParser::Peak_2dContext::number() {
  return getRuleContexts<NmrViewPKParser::NumberContext>();
}

NmrViewPKParser::NumberContext* NmrViewPKParser::Peak_2dContext::number(size_t i) {
  return getRuleContext<NmrViewPKParser::NumberContext>(i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_2dContext::Simple_name() {
  return getTokens(NmrViewPKParser::Simple_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_2dContext::Simple_name(size_t i) {
  return getToken(NmrViewPKParser::Simple_name, i);
}

std::vector<NmrViewPKParser::JcouplingContext *> NmrViewPKParser::Peak_2dContext::jcoupling() {
  return getRuleContexts<NmrViewPKParser::JcouplingContext>();
}

NmrViewPKParser::JcouplingContext* NmrViewPKParser::Peak_2dContext::jcoupling(size_t i) {
  return getRuleContext<NmrViewPKParser::JcouplingContext>(i);
}

tree::TerminalNode* NmrViewPKParser::Peak_2dContext::RETURN() {
  return getToken(NmrViewPKParser::RETURN, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_2dContext::EOF() {
  return getToken(NmrViewPKParser::EOF, 0);
}


size_t NmrViewPKParser::Peak_2dContext::getRuleIndex() const {
  return NmrViewPKParser::RulePeak_2d;
}


std::any NmrViewPKParser::Peak_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_2d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewPKParser::Peak_2dContext* NmrViewPKParser::peak_2d() {
  Peak_2dContext *_localctx = _tracker.createInstance<Peak_2dContext>(_ctx, getState());
  enterRule(_localctx, 8, NmrViewPKParser::RulePeak_2d);
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
    setState(132);
    match(NmrViewPKParser::Integer);
    setState(133);
    enclose_data();
    setState(134);
    number();
    setState(135);
    number();
    setState(136);
    number();
    setState(137);
    match(NmrViewPKParser::Simple_name);
    setState(138);
    jcoupling();
    setState(139);
    enclose_data();
    setState(140);
    enclose_data();
    setState(141);
    number();
    setState(142);
    number();
    setState(143);
    number();
    setState(144);
    match(NmrViewPKParser::Simple_name);
    setState(145);
    jcoupling();
    setState(146);
    enclose_data();
    setState(147);
    number();
    setState(148);
    number();
    setState(149);
    match(NmrViewPKParser::Integer);
    setState(151);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewPKParser::L_brace) {
      setState(150);
      enclose_data();
    }
    setState(154); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(153);
      match(NmrViewPKParser::Integer);
      setState(156); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewPKParser::Integer);
    setState(158);
    _la = _input->LA(1);
    if (!(_la == NmrViewPKParser::EOF

    || _la == NmrViewPKParser::RETURN)) {
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

//----------------- Peak_list_3dContext ------------------------------------------------------------------

NmrViewPKParser::Peak_list_3dContext::Peak_list_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_3dContext::L_name() {
  return getTokens(NmrViewPKParser::L_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_3dContext::L_name(size_t i) {
  return getToken(NmrViewPKParser::L_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_3dContext::P_name() {
  return getTokens(NmrViewPKParser::P_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_3dContext::P_name(size_t i) {
  return getToken(NmrViewPKParser::P_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_3dContext::W_name() {
  return getTokens(NmrViewPKParser::W_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_3dContext::W_name(size_t i) {
  return getToken(NmrViewPKParser::W_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_3dContext::B_name() {
  return getTokens(NmrViewPKParser::B_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_3dContext::B_name(size_t i) {
  return getToken(NmrViewPKParser::B_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_3dContext::E_name() {
  return getTokens(NmrViewPKParser::E_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_3dContext::E_name(size_t i) {
  return getToken(NmrViewPKParser::E_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_3dContext::J_name() {
  return getTokens(NmrViewPKParser::J_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_3dContext::J_name(size_t i) {
  return getToken(NmrViewPKParser::J_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_3dContext::U_name() {
  return getTokens(NmrViewPKParser::U_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_3dContext::U_name(size_t i) {
  return getToken(NmrViewPKParser::U_name, i);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_3dContext::Vol() {
  return getToken(NmrViewPKParser::Vol, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_3dContext::Int() {
  return getToken(NmrViewPKParser::Int, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_3dContext::Stat() {
  return getToken(NmrViewPKParser::Stat, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_3dContext::Flag0() {
  return getToken(NmrViewPKParser::Flag0, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_3dContext::Comment() {
  return getToken(NmrViewPKParser::Comment, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_3dContext::RETURN() {
  return getToken(NmrViewPKParser::RETURN, 0);
}

std::vector<NmrViewPKParser::Peak_3dContext *> NmrViewPKParser::Peak_list_3dContext::peak_3d() {
  return getRuleContexts<NmrViewPKParser::Peak_3dContext>();
}

NmrViewPKParser::Peak_3dContext* NmrViewPKParser::Peak_list_3dContext::peak_3d(size_t i) {
  return getRuleContext<NmrViewPKParser::Peak_3dContext>(i);
}


size_t NmrViewPKParser::Peak_list_3dContext::getRuleIndex() const {
  return NmrViewPKParser::RulePeak_list_3d;
}


std::any NmrViewPKParser::Peak_list_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_3d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewPKParser::Peak_list_3dContext* NmrViewPKParser::peak_list_3d() {
  Peak_list_3dContext *_localctx = _tracker.createInstance<Peak_list_3dContext>(_ctx, getState());
  enterRule(_localctx, 10, NmrViewPKParser::RulePeak_list_3d);
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
    setState(160);
    match(NmrViewPKParser::L_name);
    setState(161);
    match(NmrViewPKParser::P_name);
    setState(162);
    match(NmrViewPKParser::W_name);
    setState(163);
    match(NmrViewPKParser::B_name);
    setState(164);
    match(NmrViewPKParser::E_name);
    setState(165);
    match(NmrViewPKParser::J_name);
    setState(166);
    match(NmrViewPKParser::U_name);
    setState(167);
    match(NmrViewPKParser::L_name);
    setState(168);
    match(NmrViewPKParser::P_name);
    setState(169);
    match(NmrViewPKParser::W_name);
    setState(170);
    match(NmrViewPKParser::B_name);
    setState(171);
    match(NmrViewPKParser::E_name);
    setState(172);
    match(NmrViewPKParser::J_name);
    setState(173);
    match(NmrViewPKParser::U_name);
    setState(174);
    match(NmrViewPKParser::L_name);
    setState(175);
    match(NmrViewPKParser::P_name);
    setState(176);
    match(NmrViewPKParser::W_name);
    setState(177);
    match(NmrViewPKParser::B_name);
    setState(178);
    match(NmrViewPKParser::E_name);
    setState(179);
    match(NmrViewPKParser::J_name);
    setState(180);
    match(NmrViewPKParser::U_name);
    setState(181);
    match(NmrViewPKParser::Vol);
    setState(182);
    match(NmrViewPKParser::Int);
    setState(183);
    match(NmrViewPKParser::Stat);
    setState(185);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewPKParser::Comment) {
      setState(184);
      match(NmrViewPKParser::Comment);
    }
    setState(187);
    match(NmrViewPKParser::Flag0);
    setState(189);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewPKParser::RETURN) {
      setState(188);
      match(NmrViewPKParser::RETURN);
    }
    setState(192); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(191);
      peak_3d();
      setState(194); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewPKParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_3dContext ------------------------------------------------------------------

NmrViewPKParser::Peak_3dContext::Peak_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_3dContext::Integer() {
  return getTokens(NmrViewPKParser::Integer);
}

tree::TerminalNode* NmrViewPKParser::Peak_3dContext::Integer(size_t i) {
  return getToken(NmrViewPKParser::Integer, i);
}

std::vector<NmrViewPKParser::Enclose_dataContext *> NmrViewPKParser::Peak_3dContext::enclose_data() {
  return getRuleContexts<NmrViewPKParser::Enclose_dataContext>();
}

NmrViewPKParser::Enclose_dataContext* NmrViewPKParser::Peak_3dContext::enclose_data(size_t i) {
  return getRuleContext<NmrViewPKParser::Enclose_dataContext>(i);
}

std::vector<NmrViewPKParser::NumberContext *> NmrViewPKParser::Peak_3dContext::number() {
  return getRuleContexts<NmrViewPKParser::NumberContext>();
}

NmrViewPKParser::NumberContext* NmrViewPKParser::Peak_3dContext::number(size_t i) {
  return getRuleContext<NmrViewPKParser::NumberContext>(i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_3dContext::Simple_name() {
  return getTokens(NmrViewPKParser::Simple_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_3dContext::Simple_name(size_t i) {
  return getToken(NmrViewPKParser::Simple_name, i);
}

std::vector<NmrViewPKParser::JcouplingContext *> NmrViewPKParser::Peak_3dContext::jcoupling() {
  return getRuleContexts<NmrViewPKParser::JcouplingContext>();
}

NmrViewPKParser::JcouplingContext* NmrViewPKParser::Peak_3dContext::jcoupling(size_t i) {
  return getRuleContext<NmrViewPKParser::JcouplingContext>(i);
}

tree::TerminalNode* NmrViewPKParser::Peak_3dContext::RETURN() {
  return getToken(NmrViewPKParser::RETURN, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_3dContext::EOF() {
  return getToken(NmrViewPKParser::EOF, 0);
}


size_t NmrViewPKParser::Peak_3dContext::getRuleIndex() const {
  return NmrViewPKParser::RulePeak_3d;
}


std::any NmrViewPKParser::Peak_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_3d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewPKParser::Peak_3dContext* NmrViewPKParser::peak_3d() {
  Peak_3dContext *_localctx = _tracker.createInstance<Peak_3dContext>(_ctx, getState());
  enterRule(_localctx, 12, NmrViewPKParser::RulePeak_3d);
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
    setState(196);
    match(NmrViewPKParser::Integer);
    setState(197);
    enclose_data();
    setState(198);
    number();
    setState(199);
    number();
    setState(200);
    number();
    setState(201);
    match(NmrViewPKParser::Simple_name);
    setState(202);
    jcoupling();
    setState(203);
    enclose_data();
    setState(204);
    enclose_data();
    setState(205);
    number();
    setState(206);
    number();
    setState(207);
    number();
    setState(208);
    match(NmrViewPKParser::Simple_name);
    setState(209);
    jcoupling();
    setState(210);
    enclose_data();
    setState(211);
    enclose_data();
    setState(212);
    number();
    setState(213);
    number();
    setState(214);
    number();
    setState(215);
    match(NmrViewPKParser::Simple_name);
    setState(216);
    jcoupling();
    setState(217);
    enclose_data();
    setState(218);
    number();
    setState(219);
    number();
    setState(220);
    match(NmrViewPKParser::Integer);
    setState(222);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewPKParser::L_brace) {
      setState(221);
      enclose_data();
    }
    setState(225); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(224);
      match(NmrViewPKParser::Integer);
      setState(227); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewPKParser::Integer);
    setState(229);
    _la = _input->LA(1);
    if (!(_la == NmrViewPKParser::EOF

    || _la == NmrViewPKParser::RETURN)) {
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

//----------------- Peak_list_4dContext ------------------------------------------------------------------

NmrViewPKParser::Peak_list_4dContext::Peak_list_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_4dContext::L_name() {
  return getTokens(NmrViewPKParser::L_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_4dContext::L_name(size_t i) {
  return getToken(NmrViewPKParser::L_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_4dContext::P_name() {
  return getTokens(NmrViewPKParser::P_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_4dContext::P_name(size_t i) {
  return getToken(NmrViewPKParser::P_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_4dContext::W_name() {
  return getTokens(NmrViewPKParser::W_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_4dContext::W_name(size_t i) {
  return getToken(NmrViewPKParser::W_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_4dContext::B_name() {
  return getTokens(NmrViewPKParser::B_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_4dContext::B_name(size_t i) {
  return getToken(NmrViewPKParser::B_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_4dContext::E_name() {
  return getTokens(NmrViewPKParser::E_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_4dContext::E_name(size_t i) {
  return getToken(NmrViewPKParser::E_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_4dContext::J_name() {
  return getTokens(NmrViewPKParser::J_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_4dContext::J_name(size_t i) {
  return getToken(NmrViewPKParser::J_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_4dContext::U_name() {
  return getTokens(NmrViewPKParser::U_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_4dContext::U_name(size_t i) {
  return getToken(NmrViewPKParser::U_name, i);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_4dContext::Vol() {
  return getToken(NmrViewPKParser::Vol, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_4dContext::Int() {
  return getToken(NmrViewPKParser::Int, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_4dContext::Stat() {
  return getToken(NmrViewPKParser::Stat, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_4dContext::Flag0() {
  return getToken(NmrViewPKParser::Flag0, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_4dContext::Comment() {
  return getToken(NmrViewPKParser::Comment, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_4dContext::RETURN() {
  return getToken(NmrViewPKParser::RETURN, 0);
}

std::vector<NmrViewPKParser::Peak_4dContext *> NmrViewPKParser::Peak_list_4dContext::peak_4d() {
  return getRuleContexts<NmrViewPKParser::Peak_4dContext>();
}

NmrViewPKParser::Peak_4dContext* NmrViewPKParser::Peak_list_4dContext::peak_4d(size_t i) {
  return getRuleContext<NmrViewPKParser::Peak_4dContext>(i);
}


size_t NmrViewPKParser::Peak_list_4dContext::getRuleIndex() const {
  return NmrViewPKParser::RulePeak_list_4d;
}


std::any NmrViewPKParser::Peak_list_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_4d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewPKParser::Peak_list_4dContext* NmrViewPKParser::peak_list_4d() {
  Peak_list_4dContext *_localctx = _tracker.createInstance<Peak_list_4dContext>(_ctx, getState());
  enterRule(_localctx, 14, NmrViewPKParser::RulePeak_list_4d);
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
    setState(231);
    match(NmrViewPKParser::L_name);
    setState(232);
    match(NmrViewPKParser::P_name);
    setState(233);
    match(NmrViewPKParser::W_name);
    setState(234);
    match(NmrViewPKParser::B_name);
    setState(235);
    match(NmrViewPKParser::E_name);
    setState(236);
    match(NmrViewPKParser::J_name);
    setState(237);
    match(NmrViewPKParser::U_name);
    setState(238);
    match(NmrViewPKParser::L_name);
    setState(239);
    match(NmrViewPKParser::P_name);
    setState(240);
    match(NmrViewPKParser::W_name);
    setState(241);
    match(NmrViewPKParser::B_name);
    setState(242);
    match(NmrViewPKParser::E_name);
    setState(243);
    match(NmrViewPKParser::J_name);
    setState(244);
    match(NmrViewPKParser::U_name);
    setState(245);
    match(NmrViewPKParser::L_name);
    setState(246);
    match(NmrViewPKParser::P_name);
    setState(247);
    match(NmrViewPKParser::W_name);
    setState(248);
    match(NmrViewPKParser::B_name);
    setState(249);
    match(NmrViewPKParser::E_name);
    setState(250);
    match(NmrViewPKParser::J_name);
    setState(251);
    match(NmrViewPKParser::U_name);
    setState(252);
    match(NmrViewPKParser::L_name);
    setState(253);
    match(NmrViewPKParser::P_name);
    setState(254);
    match(NmrViewPKParser::W_name);
    setState(255);
    match(NmrViewPKParser::B_name);
    setState(256);
    match(NmrViewPKParser::E_name);
    setState(257);
    match(NmrViewPKParser::J_name);
    setState(258);
    match(NmrViewPKParser::U_name);
    setState(259);
    match(NmrViewPKParser::Vol);
    setState(260);
    match(NmrViewPKParser::Int);
    setState(261);
    match(NmrViewPKParser::Stat);
    setState(263);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewPKParser::Comment) {
      setState(262);
      match(NmrViewPKParser::Comment);
    }
    setState(265);
    match(NmrViewPKParser::Flag0);
    setState(267);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewPKParser::RETURN) {
      setState(266);
      match(NmrViewPKParser::RETURN);
    }
    setState(270); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(269);
      peak_4d();
      setState(272); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewPKParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_4dContext ------------------------------------------------------------------

NmrViewPKParser::Peak_4dContext::Peak_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_4dContext::Integer() {
  return getTokens(NmrViewPKParser::Integer);
}

tree::TerminalNode* NmrViewPKParser::Peak_4dContext::Integer(size_t i) {
  return getToken(NmrViewPKParser::Integer, i);
}

std::vector<NmrViewPKParser::Enclose_dataContext *> NmrViewPKParser::Peak_4dContext::enclose_data() {
  return getRuleContexts<NmrViewPKParser::Enclose_dataContext>();
}

NmrViewPKParser::Enclose_dataContext* NmrViewPKParser::Peak_4dContext::enclose_data(size_t i) {
  return getRuleContext<NmrViewPKParser::Enclose_dataContext>(i);
}

std::vector<NmrViewPKParser::NumberContext *> NmrViewPKParser::Peak_4dContext::number() {
  return getRuleContexts<NmrViewPKParser::NumberContext>();
}

NmrViewPKParser::NumberContext* NmrViewPKParser::Peak_4dContext::number(size_t i) {
  return getRuleContext<NmrViewPKParser::NumberContext>(i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_4dContext::Simple_name() {
  return getTokens(NmrViewPKParser::Simple_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_4dContext::Simple_name(size_t i) {
  return getToken(NmrViewPKParser::Simple_name, i);
}

std::vector<NmrViewPKParser::JcouplingContext *> NmrViewPKParser::Peak_4dContext::jcoupling() {
  return getRuleContexts<NmrViewPKParser::JcouplingContext>();
}

NmrViewPKParser::JcouplingContext* NmrViewPKParser::Peak_4dContext::jcoupling(size_t i) {
  return getRuleContext<NmrViewPKParser::JcouplingContext>(i);
}

tree::TerminalNode* NmrViewPKParser::Peak_4dContext::RETURN() {
  return getToken(NmrViewPKParser::RETURN, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_4dContext::EOF() {
  return getToken(NmrViewPKParser::EOF, 0);
}


size_t NmrViewPKParser::Peak_4dContext::getRuleIndex() const {
  return NmrViewPKParser::RulePeak_4d;
}


std::any NmrViewPKParser::Peak_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_4d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewPKParser::Peak_4dContext* NmrViewPKParser::peak_4d() {
  Peak_4dContext *_localctx = _tracker.createInstance<Peak_4dContext>(_ctx, getState());
  enterRule(_localctx, 16, NmrViewPKParser::RulePeak_4d);
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
    setState(274);
    match(NmrViewPKParser::Integer);
    setState(275);
    enclose_data();
    setState(276);
    number();
    setState(277);
    number();
    setState(278);
    number();
    setState(279);
    match(NmrViewPKParser::Simple_name);
    setState(280);
    jcoupling();
    setState(281);
    enclose_data();
    setState(282);
    enclose_data();
    setState(283);
    number();
    setState(284);
    number();
    setState(285);
    number();
    setState(286);
    match(NmrViewPKParser::Simple_name);
    setState(287);
    jcoupling();
    setState(288);
    enclose_data();
    setState(289);
    enclose_data();
    setState(290);
    number();
    setState(291);
    number();
    setState(292);
    number();
    setState(293);
    match(NmrViewPKParser::Simple_name);
    setState(294);
    jcoupling();
    setState(295);
    enclose_data();
    setState(296);
    enclose_data();
    setState(297);
    number();
    setState(298);
    number();
    setState(299);
    number();
    setState(300);
    match(NmrViewPKParser::Simple_name);
    setState(301);
    jcoupling();
    setState(302);
    enclose_data();
    setState(303);
    number();
    setState(304);
    number();
    setState(305);
    match(NmrViewPKParser::Integer);
    setState(307);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewPKParser::L_brace) {
      setState(306);
      enclose_data();
    }
    setState(310); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(309);
      match(NmrViewPKParser::Integer);
      setState(312); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewPKParser::Integer);
    setState(314);
    _la = _input->LA(1);
    if (!(_la == NmrViewPKParser::EOF

    || _la == NmrViewPKParser::RETURN)) {
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

//----------------- Peak_list_wo_eju_2dContext ------------------------------------------------------------------

NmrViewPKParser::Peak_list_wo_eju_2dContext::Peak_list_wo_eju_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_wo_eju_2dContext::L_name() {
  return getTokens(NmrViewPKParser::L_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_2dContext::L_name(size_t i) {
  return getToken(NmrViewPKParser::L_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_wo_eju_2dContext::P_name() {
  return getTokens(NmrViewPKParser::P_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_2dContext::P_name(size_t i) {
  return getToken(NmrViewPKParser::P_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_wo_eju_2dContext::W_name() {
  return getTokens(NmrViewPKParser::W_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_2dContext::W_name(size_t i) {
  return getToken(NmrViewPKParser::W_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_wo_eju_2dContext::B_name() {
  return getTokens(NmrViewPKParser::B_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_2dContext::B_name(size_t i) {
  return getToken(NmrViewPKParser::B_name, i);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_2dContext::Vol() {
  return getToken(NmrViewPKParser::Vol, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_2dContext::Int() {
  return getToken(NmrViewPKParser::Int, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_2dContext::Stat() {
  return getToken(NmrViewPKParser::Stat, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_2dContext::Flag0() {
  return getToken(NmrViewPKParser::Flag0, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_2dContext::Comment() {
  return getToken(NmrViewPKParser::Comment, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_2dContext::RETURN() {
  return getToken(NmrViewPKParser::RETURN, 0);
}

std::vector<NmrViewPKParser::Peak_wo_eju_2dContext *> NmrViewPKParser::Peak_list_wo_eju_2dContext::peak_wo_eju_2d() {
  return getRuleContexts<NmrViewPKParser::Peak_wo_eju_2dContext>();
}

NmrViewPKParser::Peak_wo_eju_2dContext* NmrViewPKParser::Peak_list_wo_eju_2dContext::peak_wo_eju_2d(size_t i) {
  return getRuleContext<NmrViewPKParser::Peak_wo_eju_2dContext>(i);
}


size_t NmrViewPKParser::Peak_list_wo_eju_2dContext::getRuleIndex() const {
  return NmrViewPKParser::RulePeak_list_wo_eju_2d;
}


std::any NmrViewPKParser::Peak_list_wo_eju_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_wo_eju_2d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewPKParser::Peak_list_wo_eju_2dContext* NmrViewPKParser::peak_list_wo_eju_2d() {
  Peak_list_wo_eju_2dContext *_localctx = _tracker.createInstance<Peak_list_wo_eju_2dContext>(_ctx, getState());
  enterRule(_localctx, 18, NmrViewPKParser::RulePeak_list_wo_eju_2d);
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
    setState(316);
    match(NmrViewPKParser::L_name);
    setState(317);
    match(NmrViewPKParser::P_name);
    setState(318);
    match(NmrViewPKParser::W_name);
    setState(319);
    match(NmrViewPKParser::B_name);
    setState(320);
    match(NmrViewPKParser::L_name);
    setState(321);
    match(NmrViewPKParser::P_name);
    setState(322);
    match(NmrViewPKParser::W_name);
    setState(323);
    match(NmrViewPKParser::B_name);
    setState(324);
    match(NmrViewPKParser::Vol);
    setState(325);
    match(NmrViewPKParser::Int);
    setState(326);
    match(NmrViewPKParser::Stat);
    setState(328);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewPKParser::Comment) {
      setState(327);
      match(NmrViewPKParser::Comment);
    }
    setState(330);
    match(NmrViewPKParser::Flag0);
    setState(332);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewPKParser::RETURN) {
      setState(331);
      match(NmrViewPKParser::RETURN);
    }
    setState(335); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(334);
      peak_wo_eju_2d();
      setState(337); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewPKParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_wo_eju_2dContext ------------------------------------------------------------------

NmrViewPKParser::Peak_wo_eju_2dContext::Peak_wo_eju_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_wo_eju_2dContext::Integer() {
  return getTokens(NmrViewPKParser::Integer);
}

tree::TerminalNode* NmrViewPKParser::Peak_wo_eju_2dContext::Integer(size_t i) {
  return getToken(NmrViewPKParser::Integer, i);
}

std::vector<NmrViewPKParser::Enclose_dataContext *> NmrViewPKParser::Peak_wo_eju_2dContext::enclose_data() {
  return getRuleContexts<NmrViewPKParser::Enclose_dataContext>();
}

NmrViewPKParser::Enclose_dataContext* NmrViewPKParser::Peak_wo_eju_2dContext::enclose_data(size_t i) {
  return getRuleContext<NmrViewPKParser::Enclose_dataContext>(i);
}

std::vector<NmrViewPKParser::NumberContext *> NmrViewPKParser::Peak_wo_eju_2dContext::number() {
  return getRuleContexts<NmrViewPKParser::NumberContext>();
}

NmrViewPKParser::NumberContext* NmrViewPKParser::Peak_wo_eju_2dContext::number(size_t i) {
  return getRuleContext<NmrViewPKParser::NumberContext>(i);
}

tree::TerminalNode* NmrViewPKParser::Peak_wo_eju_2dContext::RETURN() {
  return getToken(NmrViewPKParser::RETURN, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_wo_eju_2dContext::EOF() {
  return getToken(NmrViewPKParser::EOF, 0);
}


size_t NmrViewPKParser::Peak_wo_eju_2dContext::getRuleIndex() const {
  return NmrViewPKParser::RulePeak_wo_eju_2d;
}


std::any NmrViewPKParser::Peak_wo_eju_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_wo_eju_2d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewPKParser::Peak_wo_eju_2dContext* NmrViewPKParser::peak_wo_eju_2d() {
  Peak_wo_eju_2dContext *_localctx = _tracker.createInstance<Peak_wo_eju_2dContext>(_ctx, getState());
  enterRule(_localctx, 20, NmrViewPKParser::RulePeak_wo_eju_2d);
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
    setState(339);
    match(NmrViewPKParser::Integer);
    setState(340);
    enclose_data();
    setState(341);
    number();
    setState(342);
    number();
    setState(343);
    number();
    setState(344);
    enclose_data();
    setState(345);
    number();
    setState(346);
    number();
    setState(347);
    number();
    setState(348);
    number();
    setState(349);
    number();
    setState(350);
    match(NmrViewPKParser::Integer);
    setState(352);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewPKParser::L_brace) {
      setState(351);
      enclose_data();
    }
    setState(355); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(354);
      match(NmrViewPKParser::Integer);
      setState(357); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewPKParser::Integer);
    setState(359);
    _la = _input->LA(1);
    if (!(_la == NmrViewPKParser::EOF

    || _la == NmrViewPKParser::RETURN)) {
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

//----------------- Peak_list_wo_eju_3dContext ------------------------------------------------------------------

NmrViewPKParser::Peak_list_wo_eju_3dContext::Peak_list_wo_eju_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_wo_eju_3dContext::L_name() {
  return getTokens(NmrViewPKParser::L_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_3dContext::L_name(size_t i) {
  return getToken(NmrViewPKParser::L_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_wo_eju_3dContext::P_name() {
  return getTokens(NmrViewPKParser::P_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_3dContext::P_name(size_t i) {
  return getToken(NmrViewPKParser::P_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_wo_eju_3dContext::W_name() {
  return getTokens(NmrViewPKParser::W_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_3dContext::W_name(size_t i) {
  return getToken(NmrViewPKParser::W_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_wo_eju_3dContext::B_name() {
  return getTokens(NmrViewPKParser::B_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_3dContext::B_name(size_t i) {
  return getToken(NmrViewPKParser::B_name, i);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_3dContext::Vol() {
  return getToken(NmrViewPKParser::Vol, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_3dContext::Int() {
  return getToken(NmrViewPKParser::Int, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_3dContext::Stat() {
  return getToken(NmrViewPKParser::Stat, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_3dContext::Flag0() {
  return getToken(NmrViewPKParser::Flag0, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_3dContext::Comment() {
  return getToken(NmrViewPKParser::Comment, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_3dContext::RETURN() {
  return getToken(NmrViewPKParser::RETURN, 0);
}

std::vector<NmrViewPKParser::Peak_wo_eju_3dContext *> NmrViewPKParser::Peak_list_wo_eju_3dContext::peak_wo_eju_3d() {
  return getRuleContexts<NmrViewPKParser::Peak_wo_eju_3dContext>();
}

NmrViewPKParser::Peak_wo_eju_3dContext* NmrViewPKParser::Peak_list_wo_eju_3dContext::peak_wo_eju_3d(size_t i) {
  return getRuleContext<NmrViewPKParser::Peak_wo_eju_3dContext>(i);
}


size_t NmrViewPKParser::Peak_list_wo_eju_3dContext::getRuleIndex() const {
  return NmrViewPKParser::RulePeak_list_wo_eju_3d;
}


std::any NmrViewPKParser::Peak_list_wo_eju_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_wo_eju_3d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewPKParser::Peak_list_wo_eju_3dContext* NmrViewPKParser::peak_list_wo_eju_3d() {
  Peak_list_wo_eju_3dContext *_localctx = _tracker.createInstance<Peak_list_wo_eju_3dContext>(_ctx, getState());
  enterRule(_localctx, 22, NmrViewPKParser::RulePeak_list_wo_eju_3d);
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
    setState(361);
    match(NmrViewPKParser::L_name);
    setState(362);
    match(NmrViewPKParser::P_name);
    setState(363);
    match(NmrViewPKParser::W_name);
    setState(364);
    match(NmrViewPKParser::B_name);
    setState(365);
    match(NmrViewPKParser::L_name);
    setState(366);
    match(NmrViewPKParser::P_name);
    setState(367);
    match(NmrViewPKParser::W_name);
    setState(368);
    match(NmrViewPKParser::B_name);
    setState(369);
    match(NmrViewPKParser::L_name);
    setState(370);
    match(NmrViewPKParser::P_name);
    setState(371);
    match(NmrViewPKParser::W_name);
    setState(372);
    match(NmrViewPKParser::B_name);
    setState(373);
    match(NmrViewPKParser::Vol);
    setState(374);
    match(NmrViewPKParser::Int);
    setState(375);
    match(NmrViewPKParser::Stat);
    setState(377);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewPKParser::Comment) {
      setState(376);
      match(NmrViewPKParser::Comment);
    }
    setState(379);
    match(NmrViewPKParser::Flag0);
    setState(381);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewPKParser::RETURN) {
      setState(380);
      match(NmrViewPKParser::RETURN);
    }
    setState(384); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(383);
      peak_wo_eju_3d();
      setState(386); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewPKParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_wo_eju_3dContext ------------------------------------------------------------------

NmrViewPKParser::Peak_wo_eju_3dContext::Peak_wo_eju_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_wo_eju_3dContext::Integer() {
  return getTokens(NmrViewPKParser::Integer);
}

tree::TerminalNode* NmrViewPKParser::Peak_wo_eju_3dContext::Integer(size_t i) {
  return getToken(NmrViewPKParser::Integer, i);
}

std::vector<NmrViewPKParser::Enclose_dataContext *> NmrViewPKParser::Peak_wo_eju_3dContext::enclose_data() {
  return getRuleContexts<NmrViewPKParser::Enclose_dataContext>();
}

NmrViewPKParser::Enclose_dataContext* NmrViewPKParser::Peak_wo_eju_3dContext::enclose_data(size_t i) {
  return getRuleContext<NmrViewPKParser::Enclose_dataContext>(i);
}

std::vector<NmrViewPKParser::NumberContext *> NmrViewPKParser::Peak_wo_eju_3dContext::number() {
  return getRuleContexts<NmrViewPKParser::NumberContext>();
}

NmrViewPKParser::NumberContext* NmrViewPKParser::Peak_wo_eju_3dContext::number(size_t i) {
  return getRuleContext<NmrViewPKParser::NumberContext>(i);
}

tree::TerminalNode* NmrViewPKParser::Peak_wo_eju_3dContext::RETURN() {
  return getToken(NmrViewPKParser::RETURN, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_wo_eju_3dContext::EOF() {
  return getToken(NmrViewPKParser::EOF, 0);
}


size_t NmrViewPKParser::Peak_wo_eju_3dContext::getRuleIndex() const {
  return NmrViewPKParser::RulePeak_wo_eju_3d;
}


std::any NmrViewPKParser::Peak_wo_eju_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_wo_eju_3d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewPKParser::Peak_wo_eju_3dContext* NmrViewPKParser::peak_wo_eju_3d() {
  Peak_wo_eju_3dContext *_localctx = _tracker.createInstance<Peak_wo_eju_3dContext>(_ctx, getState());
  enterRule(_localctx, 24, NmrViewPKParser::RulePeak_wo_eju_3d);
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
    setState(388);
    match(NmrViewPKParser::Integer);
    setState(389);
    enclose_data();
    setState(390);
    number();
    setState(391);
    number();
    setState(392);
    number();
    setState(393);
    enclose_data();
    setState(394);
    number();
    setState(395);
    number();
    setState(396);
    number();
    setState(397);
    enclose_data();
    setState(398);
    number();
    setState(399);
    number();
    setState(400);
    number();
    setState(401);
    number();
    setState(402);
    number();
    setState(403);
    match(NmrViewPKParser::Integer);
    setState(405);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewPKParser::L_brace) {
      setState(404);
      enclose_data();
    }
    setState(408); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(407);
      match(NmrViewPKParser::Integer);
      setState(410); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewPKParser::Integer);
    setState(412);
    _la = _input->LA(1);
    if (!(_la == NmrViewPKParser::EOF

    || _la == NmrViewPKParser::RETURN)) {
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

//----------------- Peak_list_wo_eju_4dContext ------------------------------------------------------------------

NmrViewPKParser::Peak_list_wo_eju_4dContext::Peak_list_wo_eju_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_wo_eju_4dContext::L_name() {
  return getTokens(NmrViewPKParser::L_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_4dContext::L_name(size_t i) {
  return getToken(NmrViewPKParser::L_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_wo_eju_4dContext::P_name() {
  return getTokens(NmrViewPKParser::P_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_4dContext::P_name(size_t i) {
  return getToken(NmrViewPKParser::P_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_wo_eju_4dContext::W_name() {
  return getTokens(NmrViewPKParser::W_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_4dContext::W_name(size_t i) {
  return getToken(NmrViewPKParser::W_name, i);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_list_wo_eju_4dContext::B_name() {
  return getTokens(NmrViewPKParser::B_name);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_4dContext::B_name(size_t i) {
  return getToken(NmrViewPKParser::B_name, i);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_4dContext::Vol() {
  return getToken(NmrViewPKParser::Vol, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_4dContext::Int() {
  return getToken(NmrViewPKParser::Int, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_4dContext::Stat() {
  return getToken(NmrViewPKParser::Stat, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_4dContext::Flag0() {
  return getToken(NmrViewPKParser::Flag0, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_4dContext::Comment() {
  return getToken(NmrViewPKParser::Comment, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_list_wo_eju_4dContext::RETURN() {
  return getToken(NmrViewPKParser::RETURN, 0);
}

std::vector<NmrViewPKParser::Peak_wo_eju_4dContext *> NmrViewPKParser::Peak_list_wo_eju_4dContext::peak_wo_eju_4d() {
  return getRuleContexts<NmrViewPKParser::Peak_wo_eju_4dContext>();
}

NmrViewPKParser::Peak_wo_eju_4dContext* NmrViewPKParser::Peak_list_wo_eju_4dContext::peak_wo_eju_4d(size_t i) {
  return getRuleContext<NmrViewPKParser::Peak_wo_eju_4dContext>(i);
}


size_t NmrViewPKParser::Peak_list_wo_eju_4dContext::getRuleIndex() const {
  return NmrViewPKParser::RulePeak_list_wo_eju_4d;
}


std::any NmrViewPKParser::Peak_list_wo_eju_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_wo_eju_4d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewPKParser::Peak_list_wo_eju_4dContext* NmrViewPKParser::peak_list_wo_eju_4d() {
  Peak_list_wo_eju_4dContext *_localctx = _tracker.createInstance<Peak_list_wo_eju_4dContext>(_ctx, getState());
  enterRule(_localctx, 26, NmrViewPKParser::RulePeak_list_wo_eju_4d);
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
    setState(414);
    match(NmrViewPKParser::L_name);
    setState(415);
    match(NmrViewPKParser::P_name);
    setState(416);
    match(NmrViewPKParser::W_name);
    setState(417);
    match(NmrViewPKParser::B_name);
    setState(418);
    match(NmrViewPKParser::L_name);
    setState(419);
    match(NmrViewPKParser::P_name);
    setState(420);
    match(NmrViewPKParser::W_name);
    setState(421);
    match(NmrViewPKParser::B_name);
    setState(422);
    match(NmrViewPKParser::L_name);
    setState(423);
    match(NmrViewPKParser::P_name);
    setState(424);
    match(NmrViewPKParser::W_name);
    setState(425);
    match(NmrViewPKParser::B_name);
    setState(426);
    match(NmrViewPKParser::L_name);
    setState(427);
    match(NmrViewPKParser::P_name);
    setState(428);
    match(NmrViewPKParser::W_name);
    setState(429);
    match(NmrViewPKParser::B_name);
    setState(430);
    match(NmrViewPKParser::Vol);
    setState(431);
    match(NmrViewPKParser::Int);
    setState(432);
    match(NmrViewPKParser::Stat);
    setState(434);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewPKParser::Comment) {
      setState(433);
      match(NmrViewPKParser::Comment);
    }
    setState(436);
    match(NmrViewPKParser::Flag0);
    setState(438);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewPKParser::RETURN) {
      setState(437);
      match(NmrViewPKParser::RETURN);
    }
    setState(441); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(440);
      peak_wo_eju_4d();
      setState(443); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewPKParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_wo_eju_4dContext ------------------------------------------------------------------

NmrViewPKParser::Peak_wo_eju_4dContext::Peak_wo_eju_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Peak_wo_eju_4dContext::Integer() {
  return getTokens(NmrViewPKParser::Integer);
}

tree::TerminalNode* NmrViewPKParser::Peak_wo_eju_4dContext::Integer(size_t i) {
  return getToken(NmrViewPKParser::Integer, i);
}

std::vector<NmrViewPKParser::Enclose_dataContext *> NmrViewPKParser::Peak_wo_eju_4dContext::enclose_data() {
  return getRuleContexts<NmrViewPKParser::Enclose_dataContext>();
}

NmrViewPKParser::Enclose_dataContext* NmrViewPKParser::Peak_wo_eju_4dContext::enclose_data(size_t i) {
  return getRuleContext<NmrViewPKParser::Enclose_dataContext>(i);
}

std::vector<NmrViewPKParser::NumberContext *> NmrViewPKParser::Peak_wo_eju_4dContext::number() {
  return getRuleContexts<NmrViewPKParser::NumberContext>();
}

NmrViewPKParser::NumberContext* NmrViewPKParser::Peak_wo_eju_4dContext::number(size_t i) {
  return getRuleContext<NmrViewPKParser::NumberContext>(i);
}

tree::TerminalNode* NmrViewPKParser::Peak_wo_eju_4dContext::RETURN() {
  return getToken(NmrViewPKParser::RETURN, 0);
}

tree::TerminalNode* NmrViewPKParser::Peak_wo_eju_4dContext::EOF() {
  return getToken(NmrViewPKParser::EOF, 0);
}


size_t NmrViewPKParser::Peak_wo_eju_4dContext::getRuleIndex() const {
  return NmrViewPKParser::RulePeak_wo_eju_4d;
}


std::any NmrViewPKParser::Peak_wo_eju_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_wo_eju_4d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewPKParser::Peak_wo_eju_4dContext* NmrViewPKParser::peak_wo_eju_4d() {
  Peak_wo_eju_4dContext *_localctx = _tracker.createInstance<Peak_wo_eju_4dContext>(_ctx, getState());
  enterRule(_localctx, 28, NmrViewPKParser::RulePeak_wo_eju_4d);
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
    setState(445);
    match(NmrViewPKParser::Integer);
    setState(446);
    enclose_data();
    setState(447);
    number();
    setState(448);
    number();
    setState(449);
    number();
    setState(450);
    enclose_data();
    setState(451);
    number();
    setState(452);
    number();
    setState(453);
    number();
    setState(454);
    enclose_data();
    setState(455);
    number();
    setState(456);
    number();
    setState(457);
    number();
    setState(458);
    enclose_data();
    setState(459);
    number();
    setState(460);
    number();
    setState(461);
    number();
    setState(462);
    number();
    setState(463);
    number();
    setState(464);
    match(NmrViewPKParser::Integer);
    setState(466);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewPKParser::L_brace) {
      setState(465);
      enclose_data();
    }
    setState(469); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(468);
      match(NmrViewPKParser::Integer);
      setState(471); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewPKParser::Integer);
    setState(473);
    _la = _input->LA(1);
    if (!(_la == NmrViewPKParser::EOF

    || _la == NmrViewPKParser::RETURN)) {
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

//----------------- LabelContext ------------------------------------------------------------------

NmrViewPKParser::LabelContext::LabelContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrViewPKParser::LabelContext::Float_LA() {
  return getToken(NmrViewPKParser::Float_LA, 0);
}

tree::TerminalNode* NmrViewPKParser::LabelContext::Simple_name_LA() {
  return getToken(NmrViewPKParser::Simple_name_LA, 0);
}

tree::TerminalNode* NmrViewPKParser::LabelContext::ENCLOSE_DATA_LA() {
  return getToken(NmrViewPKParser::ENCLOSE_DATA_LA, 0);
}


size_t NmrViewPKParser::LabelContext::getRuleIndex() const {
  return NmrViewPKParser::RuleLabel;
}


std::any NmrViewPKParser::LabelContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewPKParserVisitor*>(visitor))
    return parserVisitor->visitLabel(this);
  else
    return visitor->visitChildren(this);
}

NmrViewPKParser::LabelContext* NmrViewPKParser::label() {
  LabelContext *_localctx = _tracker.createInstance<LabelContext>(_ctx, getState());
  enterRule(_localctx, 30, NmrViewPKParser::RuleLabel);
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
    setState(475);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 20401094656) != 0))) {
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

//----------------- JcouplingContext ------------------------------------------------------------------

NmrViewPKParser::JcouplingContext::JcouplingContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrViewPKParser::JcouplingContext::Float() {
  return getToken(NmrViewPKParser::Float, 0);
}

tree::TerminalNode* NmrViewPKParser::JcouplingContext::Simple_name() {
  return getToken(NmrViewPKParser::Simple_name, 0);
}

NmrViewPKParser::Enclose_dataContext* NmrViewPKParser::JcouplingContext::enclose_data() {
  return getRuleContext<NmrViewPKParser::Enclose_dataContext>(0);
}


size_t NmrViewPKParser::JcouplingContext::getRuleIndex() const {
  return NmrViewPKParser::RuleJcoupling;
}


std::any NmrViewPKParser::JcouplingContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewPKParserVisitor*>(visitor))
    return parserVisitor->visitJcoupling(this);
  else
    return visitor->visitChildren(this);
}

NmrViewPKParser::JcouplingContext* NmrViewPKParser::jcoupling() {
  JcouplingContext *_localctx = _tracker.createInstance<JcouplingContext>(_ctx, getState());
  enterRule(_localctx, 32, NmrViewPKParser::RuleJcoupling);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(480);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case NmrViewPKParser::Float: {
        enterOuterAlt(_localctx, 1);
        setState(477);
        match(NmrViewPKParser::Float);
        break;
      }

      case NmrViewPKParser::Simple_name: {
        enterOuterAlt(_localctx, 2);
        setState(478);
        match(NmrViewPKParser::Simple_name);
        break;
      }

      case NmrViewPKParser::L_brace: {
        enterOuterAlt(_localctx, 3);
        setState(479);
        enclose_data();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- NumberContext ------------------------------------------------------------------

NmrViewPKParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrViewPKParser::NumberContext::Real() {
  return getToken(NmrViewPKParser::Real, 0);
}

tree::TerminalNode* NmrViewPKParser::NumberContext::Float() {
  return getToken(NmrViewPKParser::Float, 0);
}

tree::TerminalNode* NmrViewPKParser::NumberContext::Integer() {
  return getToken(NmrViewPKParser::Integer, 0);
}

tree::TerminalNode* NmrViewPKParser::NumberContext::Simple_name() {
  return getToken(NmrViewPKParser::Simple_name, 0);
}


size_t NmrViewPKParser::NumberContext::getRuleIndex() const {
  return NmrViewPKParser::RuleNumber;
}


std::any NmrViewPKParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewPKParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

NmrViewPKParser::NumberContext* NmrViewPKParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 34, NmrViewPKParser::RuleNumber);
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
    setState(482);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 284) != 0))) {
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

//----------------- Enclose_dataContext ------------------------------------------------------------------

NmrViewPKParser::Enclose_dataContext::Enclose_dataContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrViewPKParser::Enclose_dataContext::L_brace() {
  return getToken(NmrViewPKParser::L_brace, 0);
}

tree::TerminalNode* NmrViewPKParser::Enclose_dataContext::R_brace() {
  return getToken(NmrViewPKParser::R_brace, 0);
}

std::vector<tree::TerminalNode *> NmrViewPKParser::Enclose_dataContext::Any_name() {
  return getTokens(NmrViewPKParser::Any_name);
}

tree::TerminalNode* NmrViewPKParser::Enclose_dataContext::Any_name(size_t i) {
  return getToken(NmrViewPKParser::Any_name, i);
}


size_t NmrViewPKParser::Enclose_dataContext::getRuleIndex() const {
  return NmrViewPKParser::RuleEnclose_data;
}


std::any NmrViewPKParser::Enclose_dataContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewPKParserVisitor*>(visitor))
    return parserVisitor->visitEnclose_data(this);
  else
    return visitor->visitChildren(this);
}

NmrViewPKParser::Enclose_dataContext* NmrViewPKParser::enclose_data() {
  Enclose_dataContext *_localctx = _tracker.createInstance<Enclose_dataContext>(_ctx, getState());
  enterRule(_localctx, 36, NmrViewPKParser::RuleEnclose_data);
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
    setState(484);
    match(NmrViewPKParser::L_brace);
    setState(488);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == NmrViewPKParser::Any_name) {
      setState(485);
      match(NmrViewPKParser::Any_name);
      setState(490);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(491);
    match(NmrViewPKParser::R_brace);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

void NmrViewPKParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  nmrviewpkparserParserInitialize();
#else
  ::antlr4::internal::call_once(nmrviewpkparserParserOnceFlag, nmrviewpkparserParserInitialize);
#endif
}
