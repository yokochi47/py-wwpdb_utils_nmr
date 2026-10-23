
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/NmrViewNPKParser.g4 by ANTLR 4.13.2


#include "NmrViewNPKParserVisitor.h"

#include "NmrViewNPKParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct NmrViewNPKParserStaticData final {
  NmrViewNPKParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  NmrViewNPKParserStaticData(const NmrViewNPKParserStaticData&) = delete;
  NmrViewNPKParserStaticData(NmrViewNPKParserStaticData&&) = delete;
  NmrViewNPKParserStaticData& operator=(const NmrViewNPKParserStaticData&) = delete;
  NmrViewNPKParserStaticData& operator=(NmrViewNPKParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag nmrviewnpkparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<NmrViewNPKParserStaticData> nmrviewnpkparserParserStaticData = nullptr;

void nmrviewnpkparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (nmrviewnpkparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(nmrviewnpkparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<NmrViewNPKParserStaticData>(
    std::vector<std::string>{
      "nmrview_npk", "data_label", "labels", "peak_list_2d", "peak_2d", 
      "peak_list_3d", "peak_3d", "peak_list_4d", "peak_4d", "peak_list_wo_eju_2d", 
      "peak_wo_eju_2d", "peak_list_wo_eju_3d", "peak_wo_eju_3d", "peak_list_wo_eju_4d", 
      "peak_wo_eju_4d", "label", "jcoupling", "number"
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
  	4,1,37,480,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,3,0,38,8,0,1,0,1,0,1,0,1,0,1,0,1,
  	0,1,0,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,
  	60,8,1,1,1,5,1,63,8,1,10,1,12,1,66,9,1,1,1,1,1,4,1,70,8,1,11,1,12,1,71,
  	1,1,5,1,75,8,1,10,1,12,1,78,9,1,1,1,4,1,81,8,1,11,1,12,1,82,1,1,1,1,4,
  	1,87,8,1,11,1,12,1,88,1,1,1,1,4,1,93,8,1,11,1,12,1,94,1,2,4,2,98,8,2,
  	11,2,12,2,99,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
  	1,3,1,3,1,3,1,3,3,3,120,8,3,1,3,1,3,3,3,124,8,3,1,3,4,3,127,8,3,11,3,
  	12,3,128,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
  	1,4,1,4,1,4,1,4,3,4,150,8,4,1,4,4,4,153,8,4,11,4,12,4,154,1,4,1,4,1,5,
  	1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
  	5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,184,8,5,1,5,1,5,3,5,188,8,5,1,5,4,5,191,
  	8,5,11,5,12,5,192,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
  	1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,221,8,6,1,6,4,
  	6,224,8,6,11,6,12,6,225,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
  	7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
  	1,7,1,7,1,7,1,7,1,7,3,7,262,8,7,1,7,1,7,3,7,266,8,7,1,7,4,7,269,8,7,11,
  	7,12,7,270,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
  	8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
  	1,8,3,8,306,8,8,1,8,4,8,309,8,8,11,8,12,8,310,1,8,1,8,1,9,1,9,1,9,1,9,
  	1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,327,8,9,1,9,1,9,3,9,331,8,9,1,9,4,
  	9,334,8,9,11,9,12,9,335,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
  	1,10,1,10,1,10,1,10,3,10,351,8,10,1,10,4,10,354,8,10,11,10,12,10,355,
  	1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
  	1,11,1,11,1,11,1,11,3,11,376,8,11,1,11,1,11,3,11,380,8,11,1,11,4,11,383,
  	8,11,11,11,12,11,384,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
  	1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,404,8,12,1,12,4,12,407,8,12,11,
  	12,12,12,408,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
  	13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,433,8,13,1,
  	13,1,13,3,13,437,8,13,1,13,4,13,440,8,13,11,13,12,13,441,1,14,1,14,1,
  	14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
  	14,1,14,1,14,1,14,1,14,3,14,465,8,14,1,14,4,14,468,8,14,11,14,12,14,469,
  	1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,17,0,0,18,0,2,4,6,8,10,12,14,
  	16,18,20,22,24,26,28,30,32,34,0,4,1,1,10,10,2,0,30,31,34,34,2,0,3,3,8,
  	8,2,0,2,4,8,8,508,0,37,1,0,0,0,2,54,1,0,0,0,4,97,1,0,0,0,6,101,1,0,0,
  	0,8,130,1,0,0,0,10,158,1,0,0,0,12,194,1,0,0,0,14,229,1,0,0,0,16,272,1,
  	0,0,0,18,314,1,0,0,0,20,337,1,0,0,0,22,359,1,0,0,0,24,386,1,0,0,0,26,
  	412,1,0,0,0,28,443,1,0,0,0,30,473,1,0,0,0,32,475,1,0,0,0,34,477,1,0,0,
  	0,36,38,5,10,0,0,37,36,1,0,0,0,37,38,1,0,0,0,38,49,1,0,0,0,39,48,3,2,
  	1,0,40,48,3,6,3,0,41,48,3,10,5,0,42,48,3,14,7,0,43,48,3,18,9,0,44,48,
  	3,22,11,0,45,48,3,26,13,0,46,48,5,10,0,0,47,39,1,0,0,0,47,40,1,0,0,0,
  	47,41,1,0,0,0,47,42,1,0,0,0,47,43,1,0,0,0,47,44,1,0,0,0,47,45,1,0,0,0,
  	47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,
  	51,49,1,0,0,0,52,53,5,0,0,1,53,1,1,0,0,0,54,55,5,1,0,0,55,56,5,14,0,0,
  	56,57,5,15,0,0,57,59,5,16,0,0,58,60,5,17,0,0,59,58,1,0,0,0,59,60,1,0,
  	0,0,60,64,1,0,0,0,61,63,5,33,0,0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,
  	0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,64,1,0,0,0,67,69,3,4,2,0,68,70,5,
  	33,0,0,69,68,1,0,0,0,70,71,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,76,
  	1,0,0,0,73,75,5,30,0,0,74,73,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,
  	1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,79,81,5,33,0,0,80,79,1,0,0,0,81,82,
  	1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,86,3,4,2,0,85,87,
  	5,33,0,0,86,85,1,0,0,0,87,88,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,90,
  	1,0,0,0,90,92,3,4,2,0,91,93,5,33,0,0,92,91,1,0,0,0,93,94,1,0,0,0,94,92,
  	1,0,0,0,94,95,1,0,0,0,95,3,1,0,0,0,96,98,3,30,15,0,97,96,1,0,0,0,98,99,
  	1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,5,1,0,0,0,101,102,5,18,0,0,102,
  	103,5,19,0,0,103,104,5,20,0,0,104,105,5,21,0,0,105,106,5,22,0,0,106,107,
  	5,23,0,0,107,108,5,24,0,0,108,109,5,18,0,0,109,110,5,19,0,0,110,111,5,
  	20,0,0,111,112,5,21,0,0,112,113,5,22,0,0,113,114,5,23,0,0,114,115,5,24,
  	0,0,115,116,5,25,0,0,116,117,5,26,0,0,117,119,5,27,0,0,118,120,5,28,0,
  	0,119,118,1,0,0,0,119,120,1,0,0,0,120,121,1,0,0,0,121,123,5,29,0,0,122,
  	124,5,10,0,0,123,122,1,0,0,0,123,124,1,0,0,0,124,126,1,0,0,0,125,127,
  	3,8,4,0,126,125,1,0,0,0,127,128,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,
  	0,129,7,1,0,0,0,130,131,5,2,0,0,131,132,5,8,0,0,132,133,3,34,17,0,133,
  	134,3,34,17,0,134,135,3,34,17,0,135,136,5,8,0,0,136,137,3,32,16,0,137,
  	138,5,8,0,0,138,139,5,8,0,0,139,140,3,34,17,0,140,141,3,34,17,0,141,142,
  	3,34,17,0,142,143,5,8,0,0,143,144,3,32,16,0,144,145,5,8,0,0,145,146,3,
  	34,17,0,146,147,3,34,17,0,147,149,5,2,0,0,148,150,5,8,0,0,149,148,1,0,
  	0,0,149,150,1,0,0,0,150,152,1,0,0,0,151,153,5,2,0,0,152,151,1,0,0,0,153,
  	154,1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,156,1,0,0,0,156,157,7,
  	0,0,0,157,9,1,0,0,0,158,159,5,18,0,0,159,160,5,19,0,0,160,161,5,20,0,
  	0,161,162,5,21,0,0,162,163,5,22,0,0,163,164,5,23,0,0,164,165,5,24,0,0,
  	165,166,5,18,0,0,166,167,5,19,0,0,167,168,5,20,0,0,168,169,5,21,0,0,169,
  	170,5,22,0,0,170,171,5,23,0,0,171,172,5,24,0,0,172,173,5,18,0,0,173,174,
  	5,19,0,0,174,175,5,20,0,0,175,176,5,21,0,0,176,177,5,22,0,0,177,178,5,
  	23,0,0,178,179,5,24,0,0,179,180,5,25,0,0,180,181,5,26,0,0,181,183,5,27,
  	0,0,182,184,5,28,0,0,183,182,1,0,0,0,183,184,1,0,0,0,184,185,1,0,0,0,
  	185,187,5,29,0,0,186,188,5,10,0,0,187,186,1,0,0,0,187,188,1,0,0,0,188,
  	190,1,0,0,0,189,191,3,12,6,0,190,189,1,0,0,0,191,192,1,0,0,0,192,190,
  	1,0,0,0,192,193,1,0,0,0,193,11,1,0,0,0,194,195,5,2,0,0,195,196,5,8,0,
  	0,196,197,3,34,17,0,197,198,3,34,17,0,198,199,3,34,17,0,199,200,5,8,0,
  	0,200,201,3,32,16,0,201,202,5,8,0,0,202,203,5,8,0,0,203,204,3,34,17,0,
  	204,205,3,34,17,0,205,206,3,34,17,0,206,207,5,8,0,0,207,208,3,32,16,0,
  	208,209,5,8,0,0,209,210,5,8,0,0,210,211,3,34,17,0,211,212,3,34,17,0,212,
  	213,3,34,17,0,213,214,5,8,0,0,214,215,3,32,16,0,215,216,5,8,0,0,216,217,
  	3,34,17,0,217,218,3,34,17,0,218,220,5,2,0,0,219,221,5,8,0,0,220,219,1,
  	0,0,0,220,221,1,0,0,0,221,223,1,0,0,0,222,224,5,2,0,0,223,222,1,0,0,0,
  	224,225,1,0,0,0,225,223,1,0,0,0,225,226,1,0,0,0,226,227,1,0,0,0,227,228,
  	7,0,0,0,228,13,1,0,0,0,229,230,5,18,0,0,230,231,5,19,0,0,231,232,5,20,
  	0,0,232,233,5,21,0,0,233,234,5,22,0,0,234,235,5,23,0,0,235,236,5,24,0,
  	0,236,237,5,18,0,0,237,238,5,19,0,0,238,239,5,20,0,0,239,240,5,21,0,0,
  	240,241,5,22,0,0,241,242,5,23,0,0,242,243,5,24,0,0,243,244,5,18,0,0,244,
  	245,5,19,0,0,245,246,5,20,0,0,246,247,5,21,0,0,247,248,5,22,0,0,248,249,
  	5,23,0,0,249,250,5,24,0,0,250,251,5,18,0,0,251,252,5,19,0,0,252,253,5,
  	20,0,0,253,254,5,21,0,0,254,255,5,22,0,0,255,256,5,23,0,0,256,257,5,24,
  	0,0,257,258,5,25,0,0,258,259,5,26,0,0,259,261,5,27,0,0,260,262,5,28,0,
  	0,261,260,1,0,0,0,261,262,1,0,0,0,262,263,1,0,0,0,263,265,5,29,0,0,264,
  	266,5,10,0,0,265,264,1,0,0,0,265,266,1,0,0,0,266,268,1,0,0,0,267,269,
  	3,16,8,0,268,267,1,0,0,0,269,270,1,0,0,0,270,268,1,0,0,0,270,271,1,0,
  	0,0,271,15,1,0,0,0,272,273,5,2,0,0,273,274,5,8,0,0,274,275,3,34,17,0,
  	275,276,3,34,17,0,276,277,3,34,17,0,277,278,5,8,0,0,278,279,3,32,16,0,
  	279,280,5,8,0,0,280,281,5,8,0,0,281,282,3,34,17,0,282,283,3,34,17,0,283,
  	284,3,34,17,0,284,285,5,8,0,0,285,286,3,32,16,0,286,287,5,8,0,0,287,288,
  	5,8,0,0,288,289,3,34,17,0,289,290,3,34,17,0,290,291,3,34,17,0,291,292,
  	5,8,0,0,292,293,3,32,16,0,293,294,5,8,0,0,294,295,5,8,0,0,295,296,3,34,
  	17,0,296,297,3,34,17,0,297,298,3,34,17,0,298,299,5,8,0,0,299,300,3,32,
  	16,0,300,301,5,8,0,0,301,302,3,34,17,0,302,303,3,34,17,0,303,305,5,2,
  	0,0,304,306,5,8,0,0,305,304,1,0,0,0,305,306,1,0,0,0,306,308,1,0,0,0,307,
  	309,5,2,0,0,308,307,1,0,0,0,309,310,1,0,0,0,310,308,1,0,0,0,310,311,1,
  	0,0,0,311,312,1,0,0,0,312,313,7,0,0,0,313,17,1,0,0,0,314,315,5,18,0,0,
  	315,316,5,19,0,0,316,317,5,20,0,0,317,318,5,21,0,0,318,319,5,18,0,0,319,
  	320,5,19,0,0,320,321,5,20,0,0,321,322,5,21,0,0,322,323,5,25,0,0,323,324,
  	5,26,0,0,324,326,5,27,0,0,325,327,5,28,0,0,326,325,1,0,0,0,326,327,1,
  	0,0,0,327,328,1,0,0,0,328,330,5,29,0,0,329,331,5,10,0,0,330,329,1,0,0,
  	0,330,331,1,0,0,0,331,333,1,0,0,0,332,334,3,20,10,0,333,332,1,0,0,0,334,
  	335,1,0,0,0,335,333,1,0,0,0,335,336,1,0,0,0,336,19,1,0,0,0,337,338,5,
  	2,0,0,338,339,5,8,0,0,339,340,3,34,17,0,340,341,3,34,17,0,341,342,3,34,
  	17,0,342,343,5,8,0,0,343,344,3,34,17,0,344,345,3,34,17,0,345,346,3,34,
  	17,0,346,347,3,34,17,0,347,348,3,34,17,0,348,350,5,2,0,0,349,351,5,8,
  	0,0,350,349,1,0,0,0,350,351,1,0,0,0,351,353,1,0,0,0,352,354,5,2,0,0,353,
  	352,1,0,0,0,354,355,1,0,0,0,355,353,1,0,0,0,355,356,1,0,0,0,356,357,1,
  	0,0,0,357,358,7,0,0,0,358,21,1,0,0,0,359,360,5,18,0,0,360,361,5,19,0,
  	0,361,362,5,20,0,0,362,363,5,21,0,0,363,364,5,18,0,0,364,365,5,19,0,0,
  	365,366,5,20,0,0,366,367,5,21,0,0,367,368,5,18,0,0,368,369,5,19,0,0,369,
  	370,5,20,0,0,370,371,5,21,0,0,371,372,5,25,0,0,372,373,5,26,0,0,373,375,
  	5,27,0,0,374,376,5,28,0,0,375,374,1,0,0,0,375,376,1,0,0,0,376,377,1,0,
  	0,0,377,379,5,29,0,0,378,380,5,10,0,0,379,378,1,0,0,0,379,380,1,0,0,0,
  	380,382,1,0,0,0,381,383,3,24,12,0,382,381,1,0,0,0,383,384,1,0,0,0,384,
  	382,1,0,0,0,384,385,1,0,0,0,385,23,1,0,0,0,386,387,5,2,0,0,387,388,5,
  	8,0,0,388,389,3,34,17,0,389,390,3,34,17,0,390,391,3,34,17,0,391,392,5,
  	8,0,0,392,393,3,34,17,0,393,394,3,34,17,0,394,395,3,34,17,0,395,396,5,
  	8,0,0,396,397,3,34,17,0,397,398,3,34,17,0,398,399,3,34,17,0,399,400,3,
  	34,17,0,400,401,3,34,17,0,401,403,5,2,0,0,402,404,5,8,0,0,403,402,1,0,
  	0,0,403,404,1,0,0,0,404,406,1,0,0,0,405,407,5,2,0,0,406,405,1,0,0,0,407,
  	408,1,0,0,0,408,406,1,0,0,0,408,409,1,0,0,0,409,410,1,0,0,0,410,411,7,
  	0,0,0,411,25,1,0,0,0,412,413,5,18,0,0,413,414,5,19,0,0,414,415,5,20,0,
  	0,415,416,5,21,0,0,416,417,5,18,0,0,417,418,5,19,0,0,418,419,5,20,0,0,
  	419,420,5,21,0,0,420,421,5,18,0,0,421,422,5,19,0,0,422,423,5,20,0,0,423,
  	424,5,21,0,0,424,425,5,18,0,0,425,426,5,19,0,0,426,427,5,20,0,0,427,428,
  	5,21,0,0,428,429,5,25,0,0,429,430,5,26,0,0,430,432,5,27,0,0,431,433,5,
  	28,0,0,432,431,1,0,0,0,432,433,1,0,0,0,433,434,1,0,0,0,434,436,5,29,0,
  	0,435,437,5,10,0,0,436,435,1,0,0,0,436,437,1,0,0,0,437,439,1,0,0,0,438,
  	440,3,28,14,0,439,438,1,0,0,0,440,441,1,0,0,0,441,439,1,0,0,0,441,442,
  	1,0,0,0,442,27,1,0,0,0,443,444,5,2,0,0,444,445,5,8,0,0,445,446,3,34,17,
  	0,446,447,3,34,17,0,447,448,3,34,17,0,448,449,5,8,0,0,449,450,3,34,17,
  	0,450,451,3,34,17,0,451,452,3,34,17,0,452,453,5,8,0,0,453,454,3,34,17,
  	0,454,455,3,34,17,0,455,456,3,34,17,0,456,457,5,8,0,0,457,458,3,34,17,
  	0,458,459,3,34,17,0,459,460,3,34,17,0,460,461,3,34,17,0,461,462,3,34,
  	17,0,462,464,5,2,0,0,463,465,5,8,0,0,464,463,1,0,0,0,464,465,1,0,0,0,
  	465,467,1,0,0,0,466,468,5,2,0,0,467,466,1,0,0,0,468,469,1,0,0,0,469,467,
  	1,0,0,0,469,470,1,0,0,0,470,471,1,0,0,0,471,472,7,0,0,0,472,29,1,0,0,
  	0,473,474,7,1,0,0,474,31,1,0,0,0,475,476,7,2,0,0,476,33,1,0,0,0,477,478,
  	7,3,0,0,478,35,1,0,0,0,41,37,47,49,59,64,71,76,82,88,94,99,119,123,128,
  	149,154,183,187,192,220,225,261,265,270,305,310,326,330,335,350,355,375,
  	379,384,403,408,432,436,441,464,469
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  nmrviewnpkparserParserStaticData = std::move(staticData);
}

}

NmrViewNPKParser::NmrViewNPKParser(TokenStream *input) : NmrViewNPKParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

NmrViewNPKParser::NmrViewNPKParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  NmrViewNPKParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *nmrviewnpkparserParserStaticData->atn, nmrviewnpkparserParserStaticData->decisionToDFA, nmrviewnpkparserParserStaticData->sharedContextCache, options);
}

NmrViewNPKParser::~NmrViewNPKParser() {
  delete _interpreter;
}

const atn::ATN& NmrViewNPKParser::getATN() const {
  return *nmrviewnpkparserParserStaticData->atn;
}

std::string NmrViewNPKParser::getGrammarFileName() const {
  return "NmrViewNPKParser.g4";
}

const std::vector<std::string>& NmrViewNPKParser::getRuleNames() const {
  return nmrviewnpkparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& NmrViewNPKParser::getVocabulary() const {
  return nmrviewnpkparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView NmrViewNPKParser::getSerializedATN() const {
  return nmrviewnpkparserParserStaticData->serializedATN;
}


//----------------- Nmrview_npkContext ------------------------------------------------------------------

NmrViewNPKParser::Nmrview_npkContext::Nmrview_npkContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrViewNPKParser::Nmrview_npkContext::EOF() {
  return getToken(NmrViewNPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Nmrview_npkContext::RETURN() {
  return getTokens(NmrViewNPKParser::RETURN);
}

tree::TerminalNode* NmrViewNPKParser::Nmrview_npkContext::RETURN(size_t i) {
  return getToken(NmrViewNPKParser::RETURN, i);
}

std::vector<NmrViewNPKParser::Data_labelContext *> NmrViewNPKParser::Nmrview_npkContext::data_label() {
  return getRuleContexts<NmrViewNPKParser::Data_labelContext>();
}

NmrViewNPKParser::Data_labelContext* NmrViewNPKParser::Nmrview_npkContext::data_label(size_t i) {
  return getRuleContext<NmrViewNPKParser::Data_labelContext>(i);
}

std::vector<NmrViewNPKParser::Peak_list_2dContext *> NmrViewNPKParser::Nmrview_npkContext::peak_list_2d() {
  return getRuleContexts<NmrViewNPKParser::Peak_list_2dContext>();
}

NmrViewNPKParser::Peak_list_2dContext* NmrViewNPKParser::Nmrview_npkContext::peak_list_2d(size_t i) {
  return getRuleContext<NmrViewNPKParser::Peak_list_2dContext>(i);
}

std::vector<NmrViewNPKParser::Peak_list_3dContext *> NmrViewNPKParser::Nmrview_npkContext::peak_list_3d() {
  return getRuleContexts<NmrViewNPKParser::Peak_list_3dContext>();
}

NmrViewNPKParser::Peak_list_3dContext* NmrViewNPKParser::Nmrview_npkContext::peak_list_3d(size_t i) {
  return getRuleContext<NmrViewNPKParser::Peak_list_3dContext>(i);
}

std::vector<NmrViewNPKParser::Peak_list_4dContext *> NmrViewNPKParser::Nmrview_npkContext::peak_list_4d() {
  return getRuleContexts<NmrViewNPKParser::Peak_list_4dContext>();
}

NmrViewNPKParser::Peak_list_4dContext* NmrViewNPKParser::Nmrview_npkContext::peak_list_4d(size_t i) {
  return getRuleContext<NmrViewNPKParser::Peak_list_4dContext>(i);
}

std::vector<NmrViewNPKParser::Peak_list_wo_eju_2dContext *> NmrViewNPKParser::Nmrview_npkContext::peak_list_wo_eju_2d() {
  return getRuleContexts<NmrViewNPKParser::Peak_list_wo_eju_2dContext>();
}

NmrViewNPKParser::Peak_list_wo_eju_2dContext* NmrViewNPKParser::Nmrview_npkContext::peak_list_wo_eju_2d(size_t i) {
  return getRuleContext<NmrViewNPKParser::Peak_list_wo_eju_2dContext>(i);
}

std::vector<NmrViewNPKParser::Peak_list_wo_eju_3dContext *> NmrViewNPKParser::Nmrview_npkContext::peak_list_wo_eju_3d() {
  return getRuleContexts<NmrViewNPKParser::Peak_list_wo_eju_3dContext>();
}

NmrViewNPKParser::Peak_list_wo_eju_3dContext* NmrViewNPKParser::Nmrview_npkContext::peak_list_wo_eju_3d(size_t i) {
  return getRuleContext<NmrViewNPKParser::Peak_list_wo_eju_3dContext>(i);
}

std::vector<NmrViewNPKParser::Peak_list_wo_eju_4dContext *> NmrViewNPKParser::Nmrview_npkContext::peak_list_wo_eju_4d() {
  return getRuleContexts<NmrViewNPKParser::Peak_list_wo_eju_4dContext>();
}

NmrViewNPKParser::Peak_list_wo_eju_4dContext* NmrViewNPKParser::Nmrview_npkContext::peak_list_wo_eju_4d(size_t i) {
  return getRuleContext<NmrViewNPKParser::Peak_list_wo_eju_4dContext>(i);
}


size_t NmrViewNPKParser::Nmrview_npkContext::getRuleIndex() const {
  return NmrViewNPKParser::RuleNmrview_npk;
}


std::any NmrViewNPKParser::Nmrview_npkContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewNPKParserVisitor*>(visitor))
    return parserVisitor->visitNmrview_npk(this);
  else
    return visitor->visitChildren(this);
}

NmrViewNPKParser::Nmrview_npkContext* NmrViewNPKParser::nmrview_npk() {
  Nmrview_npkContext *_localctx = _tracker.createInstance<Nmrview_npkContext>(_ctx, getState());
  enterRule(_localctx, 0, NmrViewNPKParser::RuleNmrview_npk);
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
    setState(37);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
    case 1: {
      setState(36);
      match(NmrViewNPKParser::RETURN);
      break;
    }

    default:
      break;
    }
    setState(49);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 263170) != 0)) {
      setState(47);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx)) {
      case 1: {
        setState(39);
        data_label();
        break;
      }

      case 2: {
        setState(40);
        peak_list_2d();
        break;
      }

      case 3: {
        setState(41);
        peak_list_3d();
        break;
      }

      case 4: {
        setState(42);
        peak_list_4d();
        break;
      }

      case 5: {
        setState(43);
        peak_list_wo_eju_2d();
        break;
      }

      case 6: {
        setState(44);
        peak_list_wo_eju_3d();
        break;
      }

      case 7: {
        setState(45);
        peak_list_wo_eju_4d();
        break;
      }

      case 8: {
        setState(46);
        match(NmrViewNPKParser::RETURN);
        break;
      }

      default:
        break;
      }
      setState(51);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(52);
    match(NmrViewNPKParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Data_labelContext ------------------------------------------------------------------

NmrViewNPKParser::Data_labelContext::Data_labelContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrViewNPKParser::Data_labelContext::Label() {
  return getToken(NmrViewNPKParser::Label, 0);
}

tree::TerminalNode* NmrViewNPKParser::Data_labelContext::Dataset() {
  return getToken(NmrViewNPKParser::Dataset, 0);
}

tree::TerminalNode* NmrViewNPKParser::Data_labelContext::Sw() {
  return getToken(NmrViewNPKParser::Sw, 0);
}

tree::TerminalNode* NmrViewNPKParser::Data_labelContext::Sf() {
  return getToken(NmrViewNPKParser::Sf, 0);
}

std::vector<NmrViewNPKParser::LabelsContext *> NmrViewNPKParser::Data_labelContext::labels() {
  return getRuleContexts<NmrViewNPKParser::LabelsContext>();
}

NmrViewNPKParser::LabelsContext* NmrViewNPKParser::Data_labelContext::labels(size_t i) {
  return getRuleContext<NmrViewNPKParser::LabelsContext>(i);
}

tree::TerminalNode* NmrViewNPKParser::Data_labelContext::Condition() {
  return getToken(NmrViewNPKParser::Condition, 0);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Data_labelContext::SINGLE_NL_LA() {
  return getTokens(NmrViewNPKParser::SINGLE_NL_LA);
}

tree::TerminalNode* NmrViewNPKParser::Data_labelContext::SINGLE_NL_LA(size_t i) {
  return getToken(NmrViewNPKParser::SINGLE_NL_LA, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Data_labelContext::Simple_name_LA() {
  return getTokens(NmrViewNPKParser::Simple_name_LA);
}

tree::TerminalNode* NmrViewNPKParser::Data_labelContext::Simple_name_LA(size_t i) {
  return getToken(NmrViewNPKParser::Simple_name_LA, i);
}


size_t NmrViewNPKParser::Data_labelContext::getRuleIndex() const {
  return NmrViewNPKParser::RuleData_label;
}


std::any NmrViewNPKParser::Data_labelContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewNPKParserVisitor*>(visitor))
    return parserVisitor->visitData_label(this);
  else
    return visitor->visitChildren(this);
}

NmrViewNPKParser::Data_labelContext* NmrViewNPKParser::data_label() {
  Data_labelContext *_localctx = _tracker.createInstance<Data_labelContext>(_ctx, getState());
  enterRule(_localctx, 2, NmrViewNPKParser::RuleData_label);
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
    setState(54);
    match(NmrViewNPKParser::Label);
    setState(55);
    match(NmrViewNPKParser::Dataset);
    setState(56);
    match(NmrViewNPKParser::Sw);
    setState(57);
    match(NmrViewNPKParser::Sf);
    setState(59);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewNPKParser::Condition) {
      setState(58);
      match(NmrViewNPKParser::Condition);
    }
    setState(64);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == NmrViewNPKParser::SINGLE_NL_LA) {
      setState(61);
      match(NmrViewNPKParser::SINGLE_NL_LA);
      setState(66);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(67);
    labels();
    setState(69); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(68);
              match(NmrViewNPKParser::SINGLE_NL_LA);
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(71); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 5, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(76);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == NmrViewNPKParser::Simple_name_LA) {
      setState(73);
      match(NmrViewNPKParser::Simple_name_LA);
      setState(78);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(80); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(79);
      match(NmrViewNPKParser::SINGLE_NL_LA);
      setState(82); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewNPKParser::SINGLE_NL_LA);
    setState(84);
    labels();
    setState(86); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(85);
      match(NmrViewNPKParser::SINGLE_NL_LA);
      setState(88); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewNPKParser::SINGLE_NL_LA);
    setState(90);
    labels();
    setState(92); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(91);
      match(NmrViewNPKParser::SINGLE_NL_LA);
      setState(94); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewNPKParser::SINGLE_NL_LA);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- LabelsContext ------------------------------------------------------------------

NmrViewNPKParser::LabelsContext::LabelsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<NmrViewNPKParser::LabelContext *> NmrViewNPKParser::LabelsContext::label() {
  return getRuleContexts<NmrViewNPKParser::LabelContext>();
}

NmrViewNPKParser::LabelContext* NmrViewNPKParser::LabelsContext::label(size_t i) {
  return getRuleContext<NmrViewNPKParser::LabelContext>(i);
}


size_t NmrViewNPKParser::LabelsContext::getRuleIndex() const {
  return NmrViewNPKParser::RuleLabels;
}


std::any NmrViewNPKParser::LabelsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewNPKParserVisitor*>(visitor))
    return parserVisitor->visitLabels(this);
  else
    return visitor->visitChildren(this);
}

NmrViewNPKParser::LabelsContext* NmrViewNPKParser::labels() {
  LabelsContext *_localctx = _tracker.createInstance<LabelsContext>(_ctx, getState());
  enterRule(_localctx, 4, NmrViewNPKParser::RuleLabels);
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
    setState(97); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(96);
      label();
      setState(99); 
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

NmrViewNPKParser::Peak_list_2dContext::Peak_list_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_2dContext::L_name() {
  return getTokens(NmrViewNPKParser::L_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_2dContext::L_name(size_t i) {
  return getToken(NmrViewNPKParser::L_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_2dContext::P_name() {
  return getTokens(NmrViewNPKParser::P_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_2dContext::P_name(size_t i) {
  return getToken(NmrViewNPKParser::P_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_2dContext::W_name() {
  return getTokens(NmrViewNPKParser::W_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_2dContext::W_name(size_t i) {
  return getToken(NmrViewNPKParser::W_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_2dContext::B_name() {
  return getTokens(NmrViewNPKParser::B_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_2dContext::B_name(size_t i) {
  return getToken(NmrViewNPKParser::B_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_2dContext::E_name() {
  return getTokens(NmrViewNPKParser::E_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_2dContext::E_name(size_t i) {
  return getToken(NmrViewNPKParser::E_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_2dContext::J_name() {
  return getTokens(NmrViewNPKParser::J_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_2dContext::J_name(size_t i) {
  return getToken(NmrViewNPKParser::J_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_2dContext::U_name() {
  return getTokens(NmrViewNPKParser::U_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_2dContext::U_name(size_t i) {
  return getToken(NmrViewNPKParser::U_name, i);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_2dContext::Vol() {
  return getToken(NmrViewNPKParser::Vol, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_2dContext::Int() {
  return getToken(NmrViewNPKParser::Int, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_2dContext::Stat() {
  return getToken(NmrViewNPKParser::Stat, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_2dContext::Flag0() {
  return getToken(NmrViewNPKParser::Flag0, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_2dContext::Comment() {
  return getToken(NmrViewNPKParser::Comment, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_2dContext::RETURN() {
  return getToken(NmrViewNPKParser::RETURN, 0);
}

std::vector<NmrViewNPKParser::Peak_2dContext *> NmrViewNPKParser::Peak_list_2dContext::peak_2d() {
  return getRuleContexts<NmrViewNPKParser::Peak_2dContext>();
}

NmrViewNPKParser::Peak_2dContext* NmrViewNPKParser::Peak_list_2dContext::peak_2d(size_t i) {
  return getRuleContext<NmrViewNPKParser::Peak_2dContext>(i);
}


size_t NmrViewNPKParser::Peak_list_2dContext::getRuleIndex() const {
  return NmrViewNPKParser::RulePeak_list_2d;
}


std::any NmrViewNPKParser::Peak_list_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewNPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_2d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewNPKParser::Peak_list_2dContext* NmrViewNPKParser::peak_list_2d() {
  Peak_list_2dContext *_localctx = _tracker.createInstance<Peak_list_2dContext>(_ctx, getState());
  enterRule(_localctx, 6, NmrViewNPKParser::RulePeak_list_2d);
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
    setState(101);
    match(NmrViewNPKParser::L_name);
    setState(102);
    match(NmrViewNPKParser::P_name);
    setState(103);
    match(NmrViewNPKParser::W_name);
    setState(104);
    match(NmrViewNPKParser::B_name);
    setState(105);
    match(NmrViewNPKParser::E_name);
    setState(106);
    match(NmrViewNPKParser::J_name);
    setState(107);
    match(NmrViewNPKParser::U_name);
    setState(108);
    match(NmrViewNPKParser::L_name);
    setState(109);
    match(NmrViewNPKParser::P_name);
    setState(110);
    match(NmrViewNPKParser::W_name);
    setState(111);
    match(NmrViewNPKParser::B_name);
    setState(112);
    match(NmrViewNPKParser::E_name);
    setState(113);
    match(NmrViewNPKParser::J_name);
    setState(114);
    match(NmrViewNPKParser::U_name);
    setState(115);
    match(NmrViewNPKParser::Vol);
    setState(116);
    match(NmrViewNPKParser::Int);
    setState(117);
    match(NmrViewNPKParser::Stat);
    setState(119);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewNPKParser::Comment) {
      setState(118);
      match(NmrViewNPKParser::Comment);
    }
    setState(121);
    match(NmrViewNPKParser::Flag0);
    setState(123);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewNPKParser::RETURN) {
      setState(122);
      match(NmrViewNPKParser::RETURN);
    }
    setState(126); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(125);
      peak_2d();
      setState(128); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewNPKParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_2dContext ------------------------------------------------------------------

NmrViewNPKParser::Peak_2dContext::Peak_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_2dContext::Integer() {
  return getTokens(NmrViewNPKParser::Integer);
}

tree::TerminalNode* NmrViewNPKParser::Peak_2dContext::Integer(size_t i) {
  return getToken(NmrViewNPKParser::Integer, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_2dContext::Simple_name() {
  return getTokens(NmrViewNPKParser::Simple_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_2dContext::Simple_name(size_t i) {
  return getToken(NmrViewNPKParser::Simple_name, i);
}

std::vector<NmrViewNPKParser::NumberContext *> NmrViewNPKParser::Peak_2dContext::number() {
  return getRuleContexts<NmrViewNPKParser::NumberContext>();
}

NmrViewNPKParser::NumberContext* NmrViewNPKParser::Peak_2dContext::number(size_t i) {
  return getRuleContext<NmrViewNPKParser::NumberContext>(i);
}

std::vector<NmrViewNPKParser::JcouplingContext *> NmrViewNPKParser::Peak_2dContext::jcoupling() {
  return getRuleContexts<NmrViewNPKParser::JcouplingContext>();
}

NmrViewNPKParser::JcouplingContext* NmrViewNPKParser::Peak_2dContext::jcoupling(size_t i) {
  return getRuleContext<NmrViewNPKParser::JcouplingContext>(i);
}

tree::TerminalNode* NmrViewNPKParser::Peak_2dContext::RETURN() {
  return getToken(NmrViewNPKParser::RETURN, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_2dContext::EOF() {
  return getToken(NmrViewNPKParser::EOF, 0);
}


size_t NmrViewNPKParser::Peak_2dContext::getRuleIndex() const {
  return NmrViewNPKParser::RulePeak_2d;
}


std::any NmrViewNPKParser::Peak_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewNPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_2d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewNPKParser::Peak_2dContext* NmrViewNPKParser::peak_2d() {
  Peak_2dContext *_localctx = _tracker.createInstance<Peak_2dContext>(_ctx, getState());
  enterRule(_localctx, 8, NmrViewNPKParser::RulePeak_2d);
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
    setState(130);
    match(NmrViewNPKParser::Integer);
    setState(131);
    match(NmrViewNPKParser::Simple_name);
    setState(132);
    number();
    setState(133);
    number();
    setState(134);
    number();
    setState(135);
    match(NmrViewNPKParser::Simple_name);
    setState(136);
    jcoupling();
    setState(137);
    match(NmrViewNPKParser::Simple_name);
    setState(138);
    match(NmrViewNPKParser::Simple_name);
    setState(139);
    number();
    setState(140);
    number();
    setState(141);
    number();
    setState(142);
    match(NmrViewNPKParser::Simple_name);
    setState(143);
    jcoupling();
    setState(144);
    match(NmrViewNPKParser::Simple_name);
    setState(145);
    number();
    setState(146);
    number();
    setState(147);
    match(NmrViewNPKParser::Integer);
    setState(149);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewNPKParser::Simple_name) {
      setState(148);
      match(NmrViewNPKParser::Simple_name);
    }
    setState(152); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(151);
      match(NmrViewNPKParser::Integer);
      setState(154); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewNPKParser::Integer);
    setState(156);
    _la = _input->LA(1);
    if (!(_la == NmrViewNPKParser::EOF

    || _la == NmrViewNPKParser::RETURN)) {
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

NmrViewNPKParser::Peak_list_3dContext::Peak_list_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_3dContext::L_name() {
  return getTokens(NmrViewNPKParser::L_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_3dContext::L_name(size_t i) {
  return getToken(NmrViewNPKParser::L_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_3dContext::P_name() {
  return getTokens(NmrViewNPKParser::P_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_3dContext::P_name(size_t i) {
  return getToken(NmrViewNPKParser::P_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_3dContext::W_name() {
  return getTokens(NmrViewNPKParser::W_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_3dContext::W_name(size_t i) {
  return getToken(NmrViewNPKParser::W_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_3dContext::B_name() {
  return getTokens(NmrViewNPKParser::B_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_3dContext::B_name(size_t i) {
  return getToken(NmrViewNPKParser::B_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_3dContext::E_name() {
  return getTokens(NmrViewNPKParser::E_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_3dContext::E_name(size_t i) {
  return getToken(NmrViewNPKParser::E_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_3dContext::J_name() {
  return getTokens(NmrViewNPKParser::J_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_3dContext::J_name(size_t i) {
  return getToken(NmrViewNPKParser::J_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_3dContext::U_name() {
  return getTokens(NmrViewNPKParser::U_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_3dContext::U_name(size_t i) {
  return getToken(NmrViewNPKParser::U_name, i);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_3dContext::Vol() {
  return getToken(NmrViewNPKParser::Vol, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_3dContext::Int() {
  return getToken(NmrViewNPKParser::Int, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_3dContext::Stat() {
  return getToken(NmrViewNPKParser::Stat, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_3dContext::Flag0() {
  return getToken(NmrViewNPKParser::Flag0, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_3dContext::Comment() {
  return getToken(NmrViewNPKParser::Comment, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_3dContext::RETURN() {
  return getToken(NmrViewNPKParser::RETURN, 0);
}

std::vector<NmrViewNPKParser::Peak_3dContext *> NmrViewNPKParser::Peak_list_3dContext::peak_3d() {
  return getRuleContexts<NmrViewNPKParser::Peak_3dContext>();
}

NmrViewNPKParser::Peak_3dContext* NmrViewNPKParser::Peak_list_3dContext::peak_3d(size_t i) {
  return getRuleContext<NmrViewNPKParser::Peak_3dContext>(i);
}


size_t NmrViewNPKParser::Peak_list_3dContext::getRuleIndex() const {
  return NmrViewNPKParser::RulePeak_list_3d;
}


std::any NmrViewNPKParser::Peak_list_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewNPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_3d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewNPKParser::Peak_list_3dContext* NmrViewNPKParser::peak_list_3d() {
  Peak_list_3dContext *_localctx = _tracker.createInstance<Peak_list_3dContext>(_ctx, getState());
  enterRule(_localctx, 10, NmrViewNPKParser::RulePeak_list_3d);
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
    setState(158);
    match(NmrViewNPKParser::L_name);
    setState(159);
    match(NmrViewNPKParser::P_name);
    setState(160);
    match(NmrViewNPKParser::W_name);
    setState(161);
    match(NmrViewNPKParser::B_name);
    setState(162);
    match(NmrViewNPKParser::E_name);
    setState(163);
    match(NmrViewNPKParser::J_name);
    setState(164);
    match(NmrViewNPKParser::U_name);
    setState(165);
    match(NmrViewNPKParser::L_name);
    setState(166);
    match(NmrViewNPKParser::P_name);
    setState(167);
    match(NmrViewNPKParser::W_name);
    setState(168);
    match(NmrViewNPKParser::B_name);
    setState(169);
    match(NmrViewNPKParser::E_name);
    setState(170);
    match(NmrViewNPKParser::J_name);
    setState(171);
    match(NmrViewNPKParser::U_name);
    setState(172);
    match(NmrViewNPKParser::L_name);
    setState(173);
    match(NmrViewNPKParser::P_name);
    setState(174);
    match(NmrViewNPKParser::W_name);
    setState(175);
    match(NmrViewNPKParser::B_name);
    setState(176);
    match(NmrViewNPKParser::E_name);
    setState(177);
    match(NmrViewNPKParser::J_name);
    setState(178);
    match(NmrViewNPKParser::U_name);
    setState(179);
    match(NmrViewNPKParser::Vol);
    setState(180);
    match(NmrViewNPKParser::Int);
    setState(181);
    match(NmrViewNPKParser::Stat);
    setState(183);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewNPKParser::Comment) {
      setState(182);
      match(NmrViewNPKParser::Comment);
    }
    setState(185);
    match(NmrViewNPKParser::Flag0);
    setState(187);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewNPKParser::RETURN) {
      setState(186);
      match(NmrViewNPKParser::RETURN);
    }
    setState(190); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(189);
      peak_3d();
      setState(192); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewNPKParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_3dContext ------------------------------------------------------------------

NmrViewNPKParser::Peak_3dContext::Peak_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_3dContext::Integer() {
  return getTokens(NmrViewNPKParser::Integer);
}

tree::TerminalNode* NmrViewNPKParser::Peak_3dContext::Integer(size_t i) {
  return getToken(NmrViewNPKParser::Integer, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_3dContext::Simple_name() {
  return getTokens(NmrViewNPKParser::Simple_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_3dContext::Simple_name(size_t i) {
  return getToken(NmrViewNPKParser::Simple_name, i);
}

std::vector<NmrViewNPKParser::NumberContext *> NmrViewNPKParser::Peak_3dContext::number() {
  return getRuleContexts<NmrViewNPKParser::NumberContext>();
}

NmrViewNPKParser::NumberContext* NmrViewNPKParser::Peak_3dContext::number(size_t i) {
  return getRuleContext<NmrViewNPKParser::NumberContext>(i);
}

std::vector<NmrViewNPKParser::JcouplingContext *> NmrViewNPKParser::Peak_3dContext::jcoupling() {
  return getRuleContexts<NmrViewNPKParser::JcouplingContext>();
}

NmrViewNPKParser::JcouplingContext* NmrViewNPKParser::Peak_3dContext::jcoupling(size_t i) {
  return getRuleContext<NmrViewNPKParser::JcouplingContext>(i);
}

tree::TerminalNode* NmrViewNPKParser::Peak_3dContext::RETURN() {
  return getToken(NmrViewNPKParser::RETURN, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_3dContext::EOF() {
  return getToken(NmrViewNPKParser::EOF, 0);
}


size_t NmrViewNPKParser::Peak_3dContext::getRuleIndex() const {
  return NmrViewNPKParser::RulePeak_3d;
}


std::any NmrViewNPKParser::Peak_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewNPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_3d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewNPKParser::Peak_3dContext* NmrViewNPKParser::peak_3d() {
  Peak_3dContext *_localctx = _tracker.createInstance<Peak_3dContext>(_ctx, getState());
  enterRule(_localctx, 12, NmrViewNPKParser::RulePeak_3d);
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
    setState(194);
    match(NmrViewNPKParser::Integer);
    setState(195);
    match(NmrViewNPKParser::Simple_name);
    setState(196);
    number();
    setState(197);
    number();
    setState(198);
    number();
    setState(199);
    match(NmrViewNPKParser::Simple_name);
    setState(200);
    jcoupling();
    setState(201);
    match(NmrViewNPKParser::Simple_name);
    setState(202);
    match(NmrViewNPKParser::Simple_name);
    setState(203);
    number();
    setState(204);
    number();
    setState(205);
    number();
    setState(206);
    match(NmrViewNPKParser::Simple_name);
    setState(207);
    jcoupling();
    setState(208);
    match(NmrViewNPKParser::Simple_name);
    setState(209);
    match(NmrViewNPKParser::Simple_name);
    setState(210);
    number();
    setState(211);
    number();
    setState(212);
    number();
    setState(213);
    match(NmrViewNPKParser::Simple_name);
    setState(214);
    jcoupling();
    setState(215);
    match(NmrViewNPKParser::Simple_name);
    setState(216);
    number();
    setState(217);
    number();
    setState(218);
    match(NmrViewNPKParser::Integer);
    setState(220);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewNPKParser::Simple_name) {
      setState(219);
      match(NmrViewNPKParser::Simple_name);
    }
    setState(223); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(222);
      match(NmrViewNPKParser::Integer);
      setState(225); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewNPKParser::Integer);
    setState(227);
    _la = _input->LA(1);
    if (!(_la == NmrViewNPKParser::EOF

    || _la == NmrViewNPKParser::RETURN)) {
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

NmrViewNPKParser::Peak_list_4dContext::Peak_list_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_4dContext::L_name() {
  return getTokens(NmrViewNPKParser::L_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_4dContext::L_name(size_t i) {
  return getToken(NmrViewNPKParser::L_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_4dContext::P_name() {
  return getTokens(NmrViewNPKParser::P_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_4dContext::P_name(size_t i) {
  return getToken(NmrViewNPKParser::P_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_4dContext::W_name() {
  return getTokens(NmrViewNPKParser::W_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_4dContext::W_name(size_t i) {
  return getToken(NmrViewNPKParser::W_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_4dContext::B_name() {
  return getTokens(NmrViewNPKParser::B_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_4dContext::B_name(size_t i) {
  return getToken(NmrViewNPKParser::B_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_4dContext::E_name() {
  return getTokens(NmrViewNPKParser::E_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_4dContext::E_name(size_t i) {
  return getToken(NmrViewNPKParser::E_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_4dContext::J_name() {
  return getTokens(NmrViewNPKParser::J_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_4dContext::J_name(size_t i) {
  return getToken(NmrViewNPKParser::J_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_4dContext::U_name() {
  return getTokens(NmrViewNPKParser::U_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_4dContext::U_name(size_t i) {
  return getToken(NmrViewNPKParser::U_name, i);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_4dContext::Vol() {
  return getToken(NmrViewNPKParser::Vol, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_4dContext::Int() {
  return getToken(NmrViewNPKParser::Int, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_4dContext::Stat() {
  return getToken(NmrViewNPKParser::Stat, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_4dContext::Flag0() {
  return getToken(NmrViewNPKParser::Flag0, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_4dContext::Comment() {
  return getToken(NmrViewNPKParser::Comment, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_4dContext::RETURN() {
  return getToken(NmrViewNPKParser::RETURN, 0);
}

std::vector<NmrViewNPKParser::Peak_4dContext *> NmrViewNPKParser::Peak_list_4dContext::peak_4d() {
  return getRuleContexts<NmrViewNPKParser::Peak_4dContext>();
}

NmrViewNPKParser::Peak_4dContext* NmrViewNPKParser::Peak_list_4dContext::peak_4d(size_t i) {
  return getRuleContext<NmrViewNPKParser::Peak_4dContext>(i);
}


size_t NmrViewNPKParser::Peak_list_4dContext::getRuleIndex() const {
  return NmrViewNPKParser::RulePeak_list_4d;
}


std::any NmrViewNPKParser::Peak_list_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewNPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_4d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewNPKParser::Peak_list_4dContext* NmrViewNPKParser::peak_list_4d() {
  Peak_list_4dContext *_localctx = _tracker.createInstance<Peak_list_4dContext>(_ctx, getState());
  enterRule(_localctx, 14, NmrViewNPKParser::RulePeak_list_4d);
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
    match(NmrViewNPKParser::L_name);
    setState(230);
    match(NmrViewNPKParser::P_name);
    setState(231);
    match(NmrViewNPKParser::W_name);
    setState(232);
    match(NmrViewNPKParser::B_name);
    setState(233);
    match(NmrViewNPKParser::E_name);
    setState(234);
    match(NmrViewNPKParser::J_name);
    setState(235);
    match(NmrViewNPKParser::U_name);
    setState(236);
    match(NmrViewNPKParser::L_name);
    setState(237);
    match(NmrViewNPKParser::P_name);
    setState(238);
    match(NmrViewNPKParser::W_name);
    setState(239);
    match(NmrViewNPKParser::B_name);
    setState(240);
    match(NmrViewNPKParser::E_name);
    setState(241);
    match(NmrViewNPKParser::J_name);
    setState(242);
    match(NmrViewNPKParser::U_name);
    setState(243);
    match(NmrViewNPKParser::L_name);
    setState(244);
    match(NmrViewNPKParser::P_name);
    setState(245);
    match(NmrViewNPKParser::W_name);
    setState(246);
    match(NmrViewNPKParser::B_name);
    setState(247);
    match(NmrViewNPKParser::E_name);
    setState(248);
    match(NmrViewNPKParser::J_name);
    setState(249);
    match(NmrViewNPKParser::U_name);
    setState(250);
    match(NmrViewNPKParser::L_name);
    setState(251);
    match(NmrViewNPKParser::P_name);
    setState(252);
    match(NmrViewNPKParser::W_name);
    setState(253);
    match(NmrViewNPKParser::B_name);
    setState(254);
    match(NmrViewNPKParser::E_name);
    setState(255);
    match(NmrViewNPKParser::J_name);
    setState(256);
    match(NmrViewNPKParser::U_name);
    setState(257);
    match(NmrViewNPKParser::Vol);
    setState(258);
    match(NmrViewNPKParser::Int);
    setState(259);
    match(NmrViewNPKParser::Stat);
    setState(261);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewNPKParser::Comment) {
      setState(260);
      match(NmrViewNPKParser::Comment);
    }
    setState(263);
    match(NmrViewNPKParser::Flag0);
    setState(265);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewNPKParser::RETURN) {
      setState(264);
      match(NmrViewNPKParser::RETURN);
    }
    setState(268); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(267);
      peak_4d();
      setState(270); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewNPKParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_4dContext ------------------------------------------------------------------

NmrViewNPKParser::Peak_4dContext::Peak_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_4dContext::Integer() {
  return getTokens(NmrViewNPKParser::Integer);
}

tree::TerminalNode* NmrViewNPKParser::Peak_4dContext::Integer(size_t i) {
  return getToken(NmrViewNPKParser::Integer, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_4dContext::Simple_name() {
  return getTokens(NmrViewNPKParser::Simple_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_4dContext::Simple_name(size_t i) {
  return getToken(NmrViewNPKParser::Simple_name, i);
}

std::vector<NmrViewNPKParser::NumberContext *> NmrViewNPKParser::Peak_4dContext::number() {
  return getRuleContexts<NmrViewNPKParser::NumberContext>();
}

NmrViewNPKParser::NumberContext* NmrViewNPKParser::Peak_4dContext::number(size_t i) {
  return getRuleContext<NmrViewNPKParser::NumberContext>(i);
}

std::vector<NmrViewNPKParser::JcouplingContext *> NmrViewNPKParser::Peak_4dContext::jcoupling() {
  return getRuleContexts<NmrViewNPKParser::JcouplingContext>();
}

NmrViewNPKParser::JcouplingContext* NmrViewNPKParser::Peak_4dContext::jcoupling(size_t i) {
  return getRuleContext<NmrViewNPKParser::JcouplingContext>(i);
}

tree::TerminalNode* NmrViewNPKParser::Peak_4dContext::RETURN() {
  return getToken(NmrViewNPKParser::RETURN, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_4dContext::EOF() {
  return getToken(NmrViewNPKParser::EOF, 0);
}


size_t NmrViewNPKParser::Peak_4dContext::getRuleIndex() const {
  return NmrViewNPKParser::RulePeak_4d;
}


std::any NmrViewNPKParser::Peak_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewNPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_4d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewNPKParser::Peak_4dContext* NmrViewNPKParser::peak_4d() {
  Peak_4dContext *_localctx = _tracker.createInstance<Peak_4dContext>(_ctx, getState());
  enterRule(_localctx, 16, NmrViewNPKParser::RulePeak_4d);
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
    setState(272);
    match(NmrViewNPKParser::Integer);
    setState(273);
    match(NmrViewNPKParser::Simple_name);
    setState(274);
    number();
    setState(275);
    number();
    setState(276);
    number();
    setState(277);
    match(NmrViewNPKParser::Simple_name);
    setState(278);
    jcoupling();
    setState(279);
    match(NmrViewNPKParser::Simple_name);
    setState(280);
    match(NmrViewNPKParser::Simple_name);
    setState(281);
    number();
    setState(282);
    number();
    setState(283);
    number();
    setState(284);
    match(NmrViewNPKParser::Simple_name);
    setState(285);
    jcoupling();
    setState(286);
    match(NmrViewNPKParser::Simple_name);
    setState(287);
    match(NmrViewNPKParser::Simple_name);
    setState(288);
    number();
    setState(289);
    number();
    setState(290);
    number();
    setState(291);
    match(NmrViewNPKParser::Simple_name);
    setState(292);
    jcoupling();
    setState(293);
    match(NmrViewNPKParser::Simple_name);
    setState(294);
    match(NmrViewNPKParser::Simple_name);
    setState(295);
    number();
    setState(296);
    number();
    setState(297);
    number();
    setState(298);
    match(NmrViewNPKParser::Simple_name);
    setState(299);
    jcoupling();
    setState(300);
    match(NmrViewNPKParser::Simple_name);
    setState(301);
    number();
    setState(302);
    number();
    setState(303);
    match(NmrViewNPKParser::Integer);
    setState(305);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewNPKParser::Simple_name) {
      setState(304);
      match(NmrViewNPKParser::Simple_name);
    }
    setState(308); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(307);
      match(NmrViewNPKParser::Integer);
      setState(310); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewNPKParser::Integer);
    setState(312);
    _la = _input->LA(1);
    if (!(_la == NmrViewNPKParser::EOF

    || _la == NmrViewNPKParser::RETURN)) {
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

NmrViewNPKParser::Peak_list_wo_eju_2dContext::Peak_list_wo_eju_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_wo_eju_2dContext::L_name() {
  return getTokens(NmrViewNPKParser::L_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_2dContext::L_name(size_t i) {
  return getToken(NmrViewNPKParser::L_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_wo_eju_2dContext::P_name() {
  return getTokens(NmrViewNPKParser::P_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_2dContext::P_name(size_t i) {
  return getToken(NmrViewNPKParser::P_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_wo_eju_2dContext::W_name() {
  return getTokens(NmrViewNPKParser::W_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_2dContext::W_name(size_t i) {
  return getToken(NmrViewNPKParser::W_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_wo_eju_2dContext::B_name() {
  return getTokens(NmrViewNPKParser::B_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_2dContext::B_name(size_t i) {
  return getToken(NmrViewNPKParser::B_name, i);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_2dContext::Vol() {
  return getToken(NmrViewNPKParser::Vol, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_2dContext::Int() {
  return getToken(NmrViewNPKParser::Int, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_2dContext::Stat() {
  return getToken(NmrViewNPKParser::Stat, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_2dContext::Flag0() {
  return getToken(NmrViewNPKParser::Flag0, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_2dContext::Comment() {
  return getToken(NmrViewNPKParser::Comment, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_2dContext::RETURN() {
  return getToken(NmrViewNPKParser::RETURN, 0);
}

std::vector<NmrViewNPKParser::Peak_wo_eju_2dContext *> NmrViewNPKParser::Peak_list_wo_eju_2dContext::peak_wo_eju_2d() {
  return getRuleContexts<NmrViewNPKParser::Peak_wo_eju_2dContext>();
}

NmrViewNPKParser::Peak_wo_eju_2dContext* NmrViewNPKParser::Peak_list_wo_eju_2dContext::peak_wo_eju_2d(size_t i) {
  return getRuleContext<NmrViewNPKParser::Peak_wo_eju_2dContext>(i);
}


size_t NmrViewNPKParser::Peak_list_wo_eju_2dContext::getRuleIndex() const {
  return NmrViewNPKParser::RulePeak_list_wo_eju_2d;
}


std::any NmrViewNPKParser::Peak_list_wo_eju_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewNPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_wo_eju_2d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewNPKParser::Peak_list_wo_eju_2dContext* NmrViewNPKParser::peak_list_wo_eju_2d() {
  Peak_list_wo_eju_2dContext *_localctx = _tracker.createInstance<Peak_list_wo_eju_2dContext>(_ctx, getState());
  enterRule(_localctx, 18, NmrViewNPKParser::RulePeak_list_wo_eju_2d);
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
    setState(314);
    match(NmrViewNPKParser::L_name);
    setState(315);
    match(NmrViewNPKParser::P_name);
    setState(316);
    match(NmrViewNPKParser::W_name);
    setState(317);
    match(NmrViewNPKParser::B_name);
    setState(318);
    match(NmrViewNPKParser::L_name);
    setState(319);
    match(NmrViewNPKParser::P_name);
    setState(320);
    match(NmrViewNPKParser::W_name);
    setState(321);
    match(NmrViewNPKParser::B_name);
    setState(322);
    match(NmrViewNPKParser::Vol);
    setState(323);
    match(NmrViewNPKParser::Int);
    setState(324);
    match(NmrViewNPKParser::Stat);
    setState(326);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewNPKParser::Comment) {
      setState(325);
      match(NmrViewNPKParser::Comment);
    }
    setState(328);
    match(NmrViewNPKParser::Flag0);
    setState(330);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewNPKParser::RETURN) {
      setState(329);
      match(NmrViewNPKParser::RETURN);
    }
    setState(333); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(332);
      peak_wo_eju_2d();
      setState(335); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewNPKParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_wo_eju_2dContext ------------------------------------------------------------------

NmrViewNPKParser::Peak_wo_eju_2dContext::Peak_wo_eju_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_wo_eju_2dContext::Integer() {
  return getTokens(NmrViewNPKParser::Integer);
}

tree::TerminalNode* NmrViewNPKParser::Peak_wo_eju_2dContext::Integer(size_t i) {
  return getToken(NmrViewNPKParser::Integer, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_wo_eju_2dContext::Simple_name() {
  return getTokens(NmrViewNPKParser::Simple_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_wo_eju_2dContext::Simple_name(size_t i) {
  return getToken(NmrViewNPKParser::Simple_name, i);
}

std::vector<NmrViewNPKParser::NumberContext *> NmrViewNPKParser::Peak_wo_eju_2dContext::number() {
  return getRuleContexts<NmrViewNPKParser::NumberContext>();
}

NmrViewNPKParser::NumberContext* NmrViewNPKParser::Peak_wo_eju_2dContext::number(size_t i) {
  return getRuleContext<NmrViewNPKParser::NumberContext>(i);
}

tree::TerminalNode* NmrViewNPKParser::Peak_wo_eju_2dContext::RETURN() {
  return getToken(NmrViewNPKParser::RETURN, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_wo_eju_2dContext::EOF() {
  return getToken(NmrViewNPKParser::EOF, 0);
}


size_t NmrViewNPKParser::Peak_wo_eju_2dContext::getRuleIndex() const {
  return NmrViewNPKParser::RulePeak_wo_eju_2d;
}


std::any NmrViewNPKParser::Peak_wo_eju_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewNPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_wo_eju_2d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewNPKParser::Peak_wo_eju_2dContext* NmrViewNPKParser::peak_wo_eju_2d() {
  Peak_wo_eju_2dContext *_localctx = _tracker.createInstance<Peak_wo_eju_2dContext>(_ctx, getState());
  enterRule(_localctx, 20, NmrViewNPKParser::RulePeak_wo_eju_2d);
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
    setState(337);
    match(NmrViewNPKParser::Integer);
    setState(338);
    match(NmrViewNPKParser::Simple_name);
    setState(339);
    number();
    setState(340);
    number();
    setState(341);
    number();
    setState(342);
    match(NmrViewNPKParser::Simple_name);
    setState(343);
    number();
    setState(344);
    number();
    setState(345);
    number();
    setState(346);
    number();
    setState(347);
    number();
    setState(348);
    match(NmrViewNPKParser::Integer);
    setState(350);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewNPKParser::Simple_name) {
      setState(349);
      match(NmrViewNPKParser::Simple_name);
    }
    setState(353); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(352);
      match(NmrViewNPKParser::Integer);
      setState(355); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewNPKParser::Integer);
    setState(357);
    _la = _input->LA(1);
    if (!(_la == NmrViewNPKParser::EOF

    || _la == NmrViewNPKParser::RETURN)) {
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

NmrViewNPKParser::Peak_list_wo_eju_3dContext::Peak_list_wo_eju_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_wo_eju_3dContext::L_name() {
  return getTokens(NmrViewNPKParser::L_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_3dContext::L_name(size_t i) {
  return getToken(NmrViewNPKParser::L_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_wo_eju_3dContext::P_name() {
  return getTokens(NmrViewNPKParser::P_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_3dContext::P_name(size_t i) {
  return getToken(NmrViewNPKParser::P_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_wo_eju_3dContext::W_name() {
  return getTokens(NmrViewNPKParser::W_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_3dContext::W_name(size_t i) {
  return getToken(NmrViewNPKParser::W_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_wo_eju_3dContext::B_name() {
  return getTokens(NmrViewNPKParser::B_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_3dContext::B_name(size_t i) {
  return getToken(NmrViewNPKParser::B_name, i);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_3dContext::Vol() {
  return getToken(NmrViewNPKParser::Vol, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_3dContext::Int() {
  return getToken(NmrViewNPKParser::Int, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_3dContext::Stat() {
  return getToken(NmrViewNPKParser::Stat, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_3dContext::Flag0() {
  return getToken(NmrViewNPKParser::Flag0, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_3dContext::Comment() {
  return getToken(NmrViewNPKParser::Comment, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_3dContext::RETURN() {
  return getToken(NmrViewNPKParser::RETURN, 0);
}

std::vector<NmrViewNPKParser::Peak_wo_eju_3dContext *> NmrViewNPKParser::Peak_list_wo_eju_3dContext::peak_wo_eju_3d() {
  return getRuleContexts<NmrViewNPKParser::Peak_wo_eju_3dContext>();
}

NmrViewNPKParser::Peak_wo_eju_3dContext* NmrViewNPKParser::Peak_list_wo_eju_3dContext::peak_wo_eju_3d(size_t i) {
  return getRuleContext<NmrViewNPKParser::Peak_wo_eju_3dContext>(i);
}


size_t NmrViewNPKParser::Peak_list_wo_eju_3dContext::getRuleIndex() const {
  return NmrViewNPKParser::RulePeak_list_wo_eju_3d;
}


std::any NmrViewNPKParser::Peak_list_wo_eju_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewNPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_wo_eju_3d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewNPKParser::Peak_list_wo_eju_3dContext* NmrViewNPKParser::peak_list_wo_eju_3d() {
  Peak_list_wo_eju_3dContext *_localctx = _tracker.createInstance<Peak_list_wo_eju_3dContext>(_ctx, getState());
  enterRule(_localctx, 22, NmrViewNPKParser::RulePeak_list_wo_eju_3d);
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
    setState(359);
    match(NmrViewNPKParser::L_name);
    setState(360);
    match(NmrViewNPKParser::P_name);
    setState(361);
    match(NmrViewNPKParser::W_name);
    setState(362);
    match(NmrViewNPKParser::B_name);
    setState(363);
    match(NmrViewNPKParser::L_name);
    setState(364);
    match(NmrViewNPKParser::P_name);
    setState(365);
    match(NmrViewNPKParser::W_name);
    setState(366);
    match(NmrViewNPKParser::B_name);
    setState(367);
    match(NmrViewNPKParser::L_name);
    setState(368);
    match(NmrViewNPKParser::P_name);
    setState(369);
    match(NmrViewNPKParser::W_name);
    setState(370);
    match(NmrViewNPKParser::B_name);
    setState(371);
    match(NmrViewNPKParser::Vol);
    setState(372);
    match(NmrViewNPKParser::Int);
    setState(373);
    match(NmrViewNPKParser::Stat);
    setState(375);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewNPKParser::Comment) {
      setState(374);
      match(NmrViewNPKParser::Comment);
    }
    setState(377);
    match(NmrViewNPKParser::Flag0);
    setState(379);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewNPKParser::RETURN) {
      setState(378);
      match(NmrViewNPKParser::RETURN);
    }
    setState(382); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(381);
      peak_wo_eju_3d();
      setState(384); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewNPKParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_wo_eju_3dContext ------------------------------------------------------------------

NmrViewNPKParser::Peak_wo_eju_3dContext::Peak_wo_eju_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_wo_eju_3dContext::Integer() {
  return getTokens(NmrViewNPKParser::Integer);
}

tree::TerminalNode* NmrViewNPKParser::Peak_wo_eju_3dContext::Integer(size_t i) {
  return getToken(NmrViewNPKParser::Integer, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_wo_eju_3dContext::Simple_name() {
  return getTokens(NmrViewNPKParser::Simple_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_wo_eju_3dContext::Simple_name(size_t i) {
  return getToken(NmrViewNPKParser::Simple_name, i);
}

std::vector<NmrViewNPKParser::NumberContext *> NmrViewNPKParser::Peak_wo_eju_3dContext::number() {
  return getRuleContexts<NmrViewNPKParser::NumberContext>();
}

NmrViewNPKParser::NumberContext* NmrViewNPKParser::Peak_wo_eju_3dContext::number(size_t i) {
  return getRuleContext<NmrViewNPKParser::NumberContext>(i);
}

tree::TerminalNode* NmrViewNPKParser::Peak_wo_eju_3dContext::RETURN() {
  return getToken(NmrViewNPKParser::RETURN, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_wo_eju_3dContext::EOF() {
  return getToken(NmrViewNPKParser::EOF, 0);
}


size_t NmrViewNPKParser::Peak_wo_eju_3dContext::getRuleIndex() const {
  return NmrViewNPKParser::RulePeak_wo_eju_3d;
}


std::any NmrViewNPKParser::Peak_wo_eju_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewNPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_wo_eju_3d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewNPKParser::Peak_wo_eju_3dContext* NmrViewNPKParser::peak_wo_eju_3d() {
  Peak_wo_eju_3dContext *_localctx = _tracker.createInstance<Peak_wo_eju_3dContext>(_ctx, getState());
  enterRule(_localctx, 24, NmrViewNPKParser::RulePeak_wo_eju_3d);
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
    setState(386);
    match(NmrViewNPKParser::Integer);
    setState(387);
    match(NmrViewNPKParser::Simple_name);
    setState(388);
    number();
    setState(389);
    number();
    setState(390);
    number();
    setState(391);
    match(NmrViewNPKParser::Simple_name);
    setState(392);
    number();
    setState(393);
    number();
    setState(394);
    number();
    setState(395);
    match(NmrViewNPKParser::Simple_name);
    setState(396);
    number();
    setState(397);
    number();
    setState(398);
    number();
    setState(399);
    number();
    setState(400);
    number();
    setState(401);
    match(NmrViewNPKParser::Integer);
    setState(403);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewNPKParser::Simple_name) {
      setState(402);
      match(NmrViewNPKParser::Simple_name);
    }
    setState(406); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(405);
      match(NmrViewNPKParser::Integer);
      setState(408); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewNPKParser::Integer);
    setState(410);
    _la = _input->LA(1);
    if (!(_la == NmrViewNPKParser::EOF

    || _la == NmrViewNPKParser::RETURN)) {
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

NmrViewNPKParser::Peak_list_wo_eju_4dContext::Peak_list_wo_eju_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_wo_eju_4dContext::L_name() {
  return getTokens(NmrViewNPKParser::L_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_4dContext::L_name(size_t i) {
  return getToken(NmrViewNPKParser::L_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_wo_eju_4dContext::P_name() {
  return getTokens(NmrViewNPKParser::P_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_4dContext::P_name(size_t i) {
  return getToken(NmrViewNPKParser::P_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_wo_eju_4dContext::W_name() {
  return getTokens(NmrViewNPKParser::W_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_4dContext::W_name(size_t i) {
  return getToken(NmrViewNPKParser::W_name, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_list_wo_eju_4dContext::B_name() {
  return getTokens(NmrViewNPKParser::B_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_4dContext::B_name(size_t i) {
  return getToken(NmrViewNPKParser::B_name, i);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_4dContext::Vol() {
  return getToken(NmrViewNPKParser::Vol, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_4dContext::Int() {
  return getToken(NmrViewNPKParser::Int, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_4dContext::Stat() {
  return getToken(NmrViewNPKParser::Stat, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_4dContext::Flag0() {
  return getToken(NmrViewNPKParser::Flag0, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_4dContext::Comment() {
  return getToken(NmrViewNPKParser::Comment, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_list_wo_eju_4dContext::RETURN() {
  return getToken(NmrViewNPKParser::RETURN, 0);
}

std::vector<NmrViewNPKParser::Peak_wo_eju_4dContext *> NmrViewNPKParser::Peak_list_wo_eju_4dContext::peak_wo_eju_4d() {
  return getRuleContexts<NmrViewNPKParser::Peak_wo_eju_4dContext>();
}

NmrViewNPKParser::Peak_wo_eju_4dContext* NmrViewNPKParser::Peak_list_wo_eju_4dContext::peak_wo_eju_4d(size_t i) {
  return getRuleContext<NmrViewNPKParser::Peak_wo_eju_4dContext>(i);
}


size_t NmrViewNPKParser::Peak_list_wo_eju_4dContext::getRuleIndex() const {
  return NmrViewNPKParser::RulePeak_list_wo_eju_4d;
}


std::any NmrViewNPKParser::Peak_list_wo_eju_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewNPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_list_wo_eju_4d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewNPKParser::Peak_list_wo_eju_4dContext* NmrViewNPKParser::peak_list_wo_eju_4d() {
  Peak_list_wo_eju_4dContext *_localctx = _tracker.createInstance<Peak_list_wo_eju_4dContext>(_ctx, getState());
  enterRule(_localctx, 26, NmrViewNPKParser::RulePeak_list_wo_eju_4d);
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
    setState(412);
    match(NmrViewNPKParser::L_name);
    setState(413);
    match(NmrViewNPKParser::P_name);
    setState(414);
    match(NmrViewNPKParser::W_name);
    setState(415);
    match(NmrViewNPKParser::B_name);
    setState(416);
    match(NmrViewNPKParser::L_name);
    setState(417);
    match(NmrViewNPKParser::P_name);
    setState(418);
    match(NmrViewNPKParser::W_name);
    setState(419);
    match(NmrViewNPKParser::B_name);
    setState(420);
    match(NmrViewNPKParser::L_name);
    setState(421);
    match(NmrViewNPKParser::P_name);
    setState(422);
    match(NmrViewNPKParser::W_name);
    setState(423);
    match(NmrViewNPKParser::B_name);
    setState(424);
    match(NmrViewNPKParser::L_name);
    setState(425);
    match(NmrViewNPKParser::P_name);
    setState(426);
    match(NmrViewNPKParser::W_name);
    setState(427);
    match(NmrViewNPKParser::B_name);
    setState(428);
    match(NmrViewNPKParser::Vol);
    setState(429);
    match(NmrViewNPKParser::Int);
    setState(430);
    match(NmrViewNPKParser::Stat);
    setState(432);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewNPKParser::Comment) {
      setState(431);
      match(NmrViewNPKParser::Comment);
    }
    setState(434);
    match(NmrViewNPKParser::Flag0);
    setState(436);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewNPKParser::RETURN) {
      setState(435);
      match(NmrViewNPKParser::RETURN);
    }
    setState(439); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(438);
      peak_wo_eju_4d();
      setState(441); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewNPKParser::Integer);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_wo_eju_4dContext ------------------------------------------------------------------

NmrViewNPKParser::Peak_wo_eju_4dContext::Peak_wo_eju_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_wo_eju_4dContext::Integer() {
  return getTokens(NmrViewNPKParser::Integer);
}

tree::TerminalNode* NmrViewNPKParser::Peak_wo_eju_4dContext::Integer(size_t i) {
  return getToken(NmrViewNPKParser::Integer, i);
}

std::vector<tree::TerminalNode *> NmrViewNPKParser::Peak_wo_eju_4dContext::Simple_name() {
  return getTokens(NmrViewNPKParser::Simple_name);
}

tree::TerminalNode* NmrViewNPKParser::Peak_wo_eju_4dContext::Simple_name(size_t i) {
  return getToken(NmrViewNPKParser::Simple_name, i);
}

std::vector<NmrViewNPKParser::NumberContext *> NmrViewNPKParser::Peak_wo_eju_4dContext::number() {
  return getRuleContexts<NmrViewNPKParser::NumberContext>();
}

NmrViewNPKParser::NumberContext* NmrViewNPKParser::Peak_wo_eju_4dContext::number(size_t i) {
  return getRuleContext<NmrViewNPKParser::NumberContext>(i);
}

tree::TerminalNode* NmrViewNPKParser::Peak_wo_eju_4dContext::RETURN() {
  return getToken(NmrViewNPKParser::RETURN, 0);
}

tree::TerminalNode* NmrViewNPKParser::Peak_wo_eju_4dContext::EOF() {
  return getToken(NmrViewNPKParser::EOF, 0);
}


size_t NmrViewNPKParser::Peak_wo_eju_4dContext::getRuleIndex() const {
  return NmrViewNPKParser::RulePeak_wo_eju_4d;
}


std::any NmrViewNPKParser::Peak_wo_eju_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewNPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_wo_eju_4d(this);
  else
    return visitor->visitChildren(this);
}

NmrViewNPKParser::Peak_wo_eju_4dContext* NmrViewNPKParser::peak_wo_eju_4d() {
  Peak_wo_eju_4dContext *_localctx = _tracker.createInstance<Peak_wo_eju_4dContext>(_ctx, getState());
  enterRule(_localctx, 28, NmrViewNPKParser::RulePeak_wo_eju_4d);
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
    setState(443);
    match(NmrViewNPKParser::Integer);
    setState(444);
    match(NmrViewNPKParser::Simple_name);
    setState(445);
    number();
    setState(446);
    number();
    setState(447);
    number();
    setState(448);
    match(NmrViewNPKParser::Simple_name);
    setState(449);
    number();
    setState(450);
    number();
    setState(451);
    number();
    setState(452);
    match(NmrViewNPKParser::Simple_name);
    setState(453);
    number();
    setState(454);
    number();
    setState(455);
    number();
    setState(456);
    match(NmrViewNPKParser::Simple_name);
    setState(457);
    number();
    setState(458);
    number();
    setState(459);
    number();
    setState(460);
    number();
    setState(461);
    number();
    setState(462);
    match(NmrViewNPKParser::Integer);
    setState(464);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == NmrViewNPKParser::Simple_name) {
      setState(463);
      match(NmrViewNPKParser::Simple_name);
    }
    setState(467); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(466);
      match(NmrViewNPKParser::Integer);
      setState(469); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == NmrViewNPKParser::Integer);
    setState(471);
    _la = _input->LA(1);
    if (!(_la == NmrViewNPKParser::EOF

    || _la == NmrViewNPKParser::RETURN)) {
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

NmrViewNPKParser::LabelContext::LabelContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrViewNPKParser::LabelContext::Float_LA() {
  return getToken(NmrViewNPKParser::Float_LA, 0);
}

tree::TerminalNode* NmrViewNPKParser::LabelContext::Simple_name_LA() {
  return getToken(NmrViewNPKParser::Simple_name_LA, 0);
}

tree::TerminalNode* NmrViewNPKParser::LabelContext::ENCLOSE_DATA_LA() {
  return getToken(NmrViewNPKParser::ENCLOSE_DATA_LA, 0);
}


size_t NmrViewNPKParser::LabelContext::getRuleIndex() const {
  return NmrViewNPKParser::RuleLabel;
}


std::any NmrViewNPKParser::LabelContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewNPKParserVisitor*>(visitor))
    return parserVisitor->visitLabel(this);
  else
    return visitor->visitChildren(this);
}

NmrViewNPKParser::LabelContext* NmrViewNPKParser::label() {
  LabelContext *_localctx = _tracker.createInstance<LabelContext>(_ctx, getState());
  enterRule(_localctx, 30, NmrViewNPKParser::RuleLabel);
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
    setState(473);
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

NmrViewNPKParser::JcouplingContext::JcouplingContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrViewNPKParser::JcouplingContext::Float() {
  return getToken(NmrViewNPKParser::Float, 0);
}

tree::TerminalNode* NmrViewNPKParser::JcouplingContext::Simple_name() {
  return getToken(NmrViewNPKParser::Simple_name, 0);
}


size_t NmrViewNPKParser::JcouplingContext::getRuleIndex() const {
  return NmrViewNPKParser::RuleJcoupling;
}


std::any NmrViewNPKParser::JcouplingContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewNPKParserVisitor*>(visitor))
    return parserVisitor->visitJcoupling(this);
  else
    return visitor->visitChildren(this);
}

NmrViewNPKParser::JcouplingContext* NmrViewNPKParser::jcoupling() {
  JcouplingContext *_localctx = _tracker.createInstance<JcouplingContext>(_ctx, getState());
  enterRule(_localctx, 32, NmrViewNPKParser::RuleJcoupling);
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
    if (!(_la == NmrViewNPKParser::Float

    || _la == NmrViewNPKParser::Simple_name)) {
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

//----------------- NumberContext ------------------------------------------------------------------

NmrViewNPKParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* NmrViewNPKParser::NumberContext::Real() {
  return getToken(NmrViewNPKParser::Real, 0);
}

tree::TerminalNode* NmrViewNPKParser::NumberContext::Float() {
  return getToken(NmrViewNPKParser::Float, 0);
}

tree::TerminalNode* NmrViewNPKParser::NumberContext::Integer() {
  return getToken(NmrViewNPKParser::Integer, 0);
}

tree::TerminalNode* NmrViewNPKParser::NumberContext::Simple_name() {
  return getToken(NmrViewNPKParser::Simple_name, 0);
}


size_t NmrViewNPKParser::NumberContext::getRuleIndex() const {
  return NmrViewNPKParser::RuleNumber;
}


std::any NmrViewNPKParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<NmrViewNPKParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

NmrViewNPKParser::NumberContext* NmrViewNPKParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 34, NmrViewNPKParser::RuleNumber);
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
    setState(477);
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

void NmrViewNPKParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  nmrviewnpkparserParserInitialize();
#else
  ::antlr4::internal::call_once(nmrviewnpkparserParserOnceFlag, nmrviewnpkparserParserInitialize);
#endif
}
