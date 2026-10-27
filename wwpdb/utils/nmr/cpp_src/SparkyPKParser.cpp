
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SparkyPKParser.g4 by ANTLR 4.13.2


#include "SparkyPKParserVisitor.h"

#include "SparkyPKParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct SparkyPKParserStaticData final {
  SparkyPKParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  SparkyPKParserStaticData(const SparkyPKParserStaticData&) = delete;
  SparkyPKParserStaticData(SparkyPKParserStaticData&&) = delete;
  SparkyPKParserStaticData& operator=(const SparkyPKParserStaticData&) = delete;
  SparkyPKParserStaticData& operator=(SparkyPKParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag sparkypkparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<SparkyPKParserStaticData> sparkypkparserParserStaticData = nullptr;

void sparkypkparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (sparkypkparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(sparkypkparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<SparkyPKParserStaticData>(
    std::vector<std::string>{
      "sparky_pk", "data_label", "data_label_wo_assign", "peak_2d", "peak_3d", 
      "peak_4d", "peak_wo_assign", "number", "note"
    },
    std::vector<std::string>{
      "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 
      "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "'w2'", 
      "'w3'", "'w4'", "", "", "", "", "", "", "'Volume'", "'Fit RMS %'"
    },
    std::vector<std::string>{
      "", "Assignment", "W1", "Integer", "Float", "Real", "Real_vol", "SHARP_COMMENT", 
      "EXCLM_COMMENT", "SMCLN_COMMENT", "Assignment_2d_ex", "Assignment_3d_ex", 
      "Assignment_4d_ex", "Note_2d_ex", "Note_3d_ex", "Note_4d_ex", "Note_ex", 
      "Simple_name", "SPACE", "RETURN", "ENCLOSE_COMMENT", "SECTION_COMMENT", 
      "LINE_COMMENT", "W1_Hz_LA", "W2_Hz_LA", "W3_Hz_LA", "W4_Hz_LA", "Lw1_Hz_LA", 
      "Lw2_Hz_LA", "Lw3_Hz_LA", "Lw4_Hz_LA", "W1_LA", "W2_LA", "W3_LA", 
      "W4_LA", "Dev_w1_LA", "Dev_w2_LA", "Dev_w3_LA", "Dev_w4_LA", "Dummy_H_LA", 
      "Height_LA", "Volume_LA", "Dummy_Rms_LA", "S_N_LA", "Atom1_LA", "Atom2_LA", 
      "Atom3_LA", "Atom4_LA", "Distance_LA", "Note_LA", "SPACE_LA", "RETURN_LA"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,51,268,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,1,0,3,0,20,8,0,1,0,1,0,1,0,4,0,25,8,0,11,0,12,0,26,1,0,
  	4,0,30,8,0,11,0,12,0,31,1,0,4,0,35,8,0,11,0,12,0,36,1,0,5,0,40,8,0,10,
  	0,12,0,43,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,51,8,1,1,1,3,1,54,8,1,1,1,3,
  	1,57,8,1,1,1,3,1,60,8,1,1,1,3,1,63,8,1,1,1,3,1,66,8,1,1,1,3,1,69,8,1,
  	1,1,3,1,72,8,1,1,1,3,1,75,8,1,1,1,3,1,78,8,1,1,1,3,1,81,8,1,1,1,3,1,84,
  	8,1,1,1,3,1,87,8,1,1,1,3,1,90,8,1,1,1,3,1,93,8,1,1,1,3,1,96,8,1,1,1,3,
  	1,99,8,1,1,1,3,1,102,8,1,1,1,3,1,105,8,1,1,1,3,1,108,8,1,1,1,3,1,111,
  	8,1,1,1,3,1,114,8,1,1,1,3,1,117,8,1,1,1,3,1,120,8,1,1,1,3,1,123,8,1,1,
  	1,1,1,3,1,127,8,1,1,2,1,2,1,2,3,2,132,8,2,1,2,3,2,135,8,2,1,2,3,2,138,
  	8,2,1,2,3,2,141,8,2,1,2,3,2,144,8,2,1,2,3,2,147,8,2,1,2,3,2,150,8,2,1,
  	2,3,2,153,8,2,1,2,3,2,156,8,2,1,2,3,2,159,8,2,1,2,3,2,162,8,2,1,2,3,2,
  	165,8,2,1,2,3,2,168,8,2,1,2,3,2,171,8,2,1,2,3,2,174,8,2,1,2,3,2,177,8,
  	2,1,2,3,2,180,8,2,1,2,3,2,183,8,2,1,2,3,2,186,8,2,1,2,3,2,189,8,2,1,2,
  	3,2,192,8,2,1,2,1,2,3,2,196,8,2,1,2,4,2,199,8,2,11,2,12,2,200,1,3,1,3,
  	1,3,1,3,4,3,207,8,3,11,3,12,3,208,1,3,5,3,212,8,3,10,3,12,3,215,9,3,1,
  	3,1,3,1,4,1,4,1,4,1,4,1,4,4,4,224,8,4,11,4,12,4,225,1,4,5,4,229,8,4,10,
  	4,12,4,232,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,4,5,242,8,5,11,5,12,5,
  	243,1,5,5,5,247,8,5,10,5,12,5,250,9,5,1,5,1,5,1,6,4,6,255,8,6,11,6,12,
  	6,256,1,6,3,6,260,8,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,
  	12,14,16,0,4,2,0,1,1,10,12,1,1,19,19,1,0,3,6,2,0,3,4,13,17,325,0,19,1,
  	0,0,0,2,46,1,0,0,0,4,128,1,0,0,0,6,202,1,0,0,0,8,218,1,0,0,0,10,235,1,
  	0,0,0,12,254,1,0,0,0,14,263,1,0,0,0,16,265,1,0,0,0,18,20,5,19,0,0,19,
  	18,1,0,0,0,19,20,1,0,0,0,20,41,1,0,0,0,21,40,3,2,1,0,22,40,3,4,2,0,23,
  	25,3,6,3,0,24,23,1,0,0,0,25,26,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,
  	40,1,0,0,0,28,30,3,8,4,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,
  	32,1,0,0,0,32,40,1,0,0,0,33,35,3,10,5,0,34,33,1,0,0,0,35,36,1,0,0,0,36,
  	34,1,0,0,0,36,37,1,0,0,0,37,40,1,0,0,0,38,40,5,19,0,0,39,21,1,0,0,0,39,
  	22,1,0,0,0,39,24,1,0,0,0,39,29,1,0,0,0,39,34,1,0,0,0,39,38,1,0,0,0,40,
  	43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,
  	45,5,0,0,1,45,1,1,0,0,0,46,47,7,0,0,0,47,48,5,31,0,0,48,50,5,32,0,0,49,
  	51,5,33,0,0,50,49,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,54,5,34,0,0,
  	53,52,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,57,5,23,0,0,56,55,1,0,0,
  	0,56,57,1,0,0,0,57,59,1,0,0,0,58,60,5,24,0,0,59,58,1,0,0,0,59,60,1,0,
  	0,0,60,62,1,0,0,0,61,63,5,25,0,0,62,61,1,0,0,0,62,63,1,0,0,0,63,65,1,
  	0,0,0,64,66,5,26,0,0,65,64,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,69,
  	5,35,0,0,68,67,1,0,0,0,68,69,1,0,0,0,69,71,1,0,0,0,70,72,5,36,0,0,71,
  	70,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,75,5,37,0,0,74,73,1,0,0,0,74,
  	75,1,0,0,0,75,77,1,0,0,0,76,78,5,38,0,0,77,76,1,0,0,0,77,78,1,0,0,0,78,
  	83,1,0,0,0,79,81,5,39,0,0,80,79,1,0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,
  	84,5,40,0,0,83,80,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,0,85,87,5,41,0,0,
  	86,85,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,90,5,42,0,0,89,88,1,0,0,
  	0,89,90,1,0,0,0,90,92,1,0,0,0,91,93,5,43,0,0,92,91,1,0,0,0,92,93,1,0,
  	0,0,93,95,1,0,0,0,94,96,5,27,0,0,95,94,1,0,0,0,95,96,1,0,0,0,96,98,1,
  	0,0,0,97,99,5,28,0,0,98,97,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,102,
  	5,29,0,0,101,100,1,0,0,0,101,102,1,0,0,0,102,104,1,0,0,0,103,105,5,30,
  	0,0,104,103,1,0,0,0,104,105,1,0,0,0,105,107,1,0,0,0,106,108,5,44,0,0,
  	107,106,1,0,0,0,107,108,1,0,0,0,108,110,1,0,0,0,109,111,5,45,0,0,110,
  	109,1,0,0,0,110,111,1,0,0,0,111,113,1,0,0,0,112,114,5,46,0,0,113,112,
  	1,0,0,0,113,114,1,0,0,0,114,116,1,0,0,0,115,117,5,47,0,0,116,115,1,0,
  	0,0,116,117,1,0,0,0,117,119,1,0,0,0,118,120,5,48,0,0,119,118,1,0,0,0,
  	119,120,1,0,0,0,120,122,1,0,0,0,121,123,5,49,0,0,122,121,1,0,0,0,122,
  	123,1,0,0,0,123,124,1,0,0,0,124,126,5,51,0,0,125,127,5,19,0,0,126,125,
  	1,0,0,0,126,127,1,0,0,0,127,3,1,0,0,0,128,129,5,2,0,0,129,131,5,32,0,
  	0,130,132,5,33,0,0,131,130,1,0,0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,
  	135,5,34,0,0,134,133,1,0,0,0,134,135,1,0,0,0,135,137,1,0,0,0,136,138,
  	5,23,0,0,137,136,1,0,0,0,137,138,1,0,0,0,138,140,1,0,0,0,139,141,5,24,
  	0,0,140,139,1,0,0,0,140,141,1,0,0,0,141,143,1,0,0,0,142,144,5,25,0,0,
  	143,142,1,0,0,0,143,144,1,0,0,0,144,146,1,0,0,0,145,147,5,26,0,0,146,
  	145,1,0,0,0,146,147,1,0,0,0,147,149,1,0,0,0,148,150,5,35,0,0,149,148,
  	1,0,0,0,149,150,1,0,0,0,150,152,1,0,0,0,151,153,5,36,0,0,152,151,1,0,
  	0,0,152,153,1,0,0,0,153,155,1,0,0,0,154,156,5,37,0,0,155,154,1,0,0,0,
  	155,156,1,0,0,0,156,158,1,0,0,0,157,159,5,38,0,0,158,157,1,0,0,0,158,
  	159,1,0,0,0,159,164,1,0,0,0,160,162,5,39,0,0,161,160,1,0,0,0,161,162,
  	1,0,0,0,162,163,1,0,0,0,163,165,5,40,0,0,164,161,1,0,0,0,164,165,1,0,
  	0,0,165,167,1,0,0,0,166,168,5,41,0,0,167,166,1,0,0,0,167,168,1,0,0,0,
  	168,170,1,0,0,0,169,171,5,42,0,0,170,169,1,0,0,0,170,171,1,0,0,0,171,
  	173,1,0,0,0,172,174,5,43,0,0,173,172,1,0,0,0,173,174,1,0,0,0,174,176,
  	1,0,0,0,175,177,5,27,0,0,176,175,1,0,0,0,176,177,1,0,0,0,177,179,1,0,
  	0,0,178,180,5,28,0,0,179,178,1,0,0,0,179,180,1,0,0,0,180,182,1,0,0,0,
  	181,183,5,29,0,0,182,181,1,0,0,0,182,183,1,0,0,0,183,185,1,0,0,0,184,
  	186,5,30,0,0,185,184,1,0,0,0,185,186,1,0,0,0,186,188,1,0,0,0,187,189,
  	5,48,0,0,188,187,1,0,0,0,188,189,1,0,0,0,189,191,1,0,0,0,190,192,5,49,
  	0,0,191,190,1,0,0,0,191,192,1,0,0,0,192,193,1,0,0,0,193,195,5,51,0,0,
  	194,196,5,19,0,0,195,194,1,0,0,0,195,196,1,0,0,0,196,198,1,0,0,0,197,
  	199,3,12,6,0,198,197,1,0,0,0,199,200,1,0,0,0,200,198,1,0,0,0,200,201,
  	1,0,0,0,201,5,1,0,0,0,202,203,5,10,0,0,203,204,5,4,0,0,204,206,5,4,0,
  	0,205,207,3,14,7,0,206,205,1,0,0,0,207,208,1,0,0,0,208,206,1,0,0,0,208,
  	209,1,0,0,0,209,213,1,0,0,0,210,212,3,16,8,0,211,210,1,0,0,0,212,215,
  	1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,216,1,0,0,0,215,213,1,0,0,
  	0,216,217,7,1,0,0,217,7,1,0,0,0,218,219,5,11,0,0,219,220,5,4,0,0,220,
  	221,5,4,0,0,221,223,5,4,0,0,222,224,3,14,7,0,223,222,1,0,0,0,224,225,
  	1,0,0,0,225,223,1,0,0,0,225,226,1,0,0,0,226,230,1,0,0,0,227,229,3,16,
  	8,0,228,227,1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,230,231,1,0,0,0,231,
  	233,1,0,0,0,232,230,1,0,0,0,233,234,7,1,0,0,234,9,1,0,0,0,235,236,5,12,
  	0,0,236,237,5,4,0,0,237,238,5,4,0,0,238,239,5,4,0,0,239,241,5,4,0,0,240,
  	242,3,14,7,0,241,240,1,0,0,0,242,243,1,0,0,0,243,241,1,0,0,0,243,244,
  	1,0,0,0,244,248,1,0,0,0,245,247,3,16,8,0,246,245,1,0,0,0,247,250,1,0,
  	0,0,248,246,1,0,0,0,248,249,1,0,0,0,249,251,1,0,0,0,250,248,1,0,0,0,251,
  	252,7,1,0,0,252,11,1,0,0,0,253,255,3,14,7,0,254,253,1,0,0,0,255,256,1,
  	0,0,0,256,254,1,0,0,0,256,257,1,0,0,0,257,259,1,0,0,0,258,260,3,16,8,
  	0,259,258,1,0,0,0,259,260,1,0,0,0,260,261,1,0,0,0,261,262,7,1,0,0,262,
  	13,1,0,0,0,263,264,7,2,0,0,264,15,1,0,0,0,265,266,7,3,0,0,266,17,1,0,
  	0,0,63,19,26,31,36,39,41,50,53,56,59,62,65,68,71,74,77,80,83,86,89,92,
  	95,98,101,104,107,110,113,116,119,122,126,131,134,137,140,143,146,149,
  	152,155,158,161,164,167,170,173,176,179,182,185,188,191,195,200,208,213,
  	225,230,243,248,256,259
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  sparkypkparserParserStaticData = std::move(staticData);
}

}

SparkyPKParser::SparkyPKParser(TokenStream *input) : SparkyPKParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

SparkyPKParser::SparkyPKParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  SparkyPKParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *sparkypkparserParserStaticData->atn, sparkypkparserParserStaticData->decisionToDFA, sparkypkparserParserStaticData->sharedContextCache, options);
}

SparkyPKParser::~SparkyPKParser() {
  delete _interpreter;
}

const atn::ATN& SparkyPKParser::getATN() const {
  return *sparkypkparserParserStaticData->atn;
}

std::string SparkyPKParser::getGrammarFileName() const {
  return "SparkyPKParser.g4";
}

const std::vector<std::string>& SparkyPKParser::getRuleNames() const {
  return sparkypkparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& SparkyPKParser::getVocabulary() const {
  return sparkypkparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView SparkyPKParser::getSerializedATN() const {
  return sparkypkparserParserStaticData->serializedATN;
}


//----------------- Sparky_pkContext ------------------------------------------------------------------

SparkyPKParser::Sparky_pkContext::Sparky_pkContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyPKParser::Sparky_pkContext::EOF() {
  return getToken(SparkyPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> SparkyPKParser::Sparky_pkContext::RETURN() {
  return getTokens(SparkyPKParser::RETURN);
}

tree::TerminalNode* SparkyPKParser::Sparky_pkContext::RETURN(size_t i) {
  return getToken(SparkyPKParser::RETURN, i);
}

std::vector<SparkyPKParser::Data_labelContext *> SparkyPKParser::Sparky_pkContext::data_label() {
  return getRuleContexts<SparkyPKParser::Data_labelContext>();
}

SparkyPKParser::Data_labelContext* SparkyPKParser::Sparky_pkContext::data_label(size_t i) {
  return getRuleContext<SparkyPKParser::Data_labelContext>(i);
}

std::vector<SparkyPKParser::Data_label_wo_assignContext *> SparkyPKParser::Sparky_pkContext::data_label_wo_assign() {
  return getRuleContexts<SparkyPKParser::Data_label_wo_assignContext>();
}

SparkyPKParser::Data_label_wo_assignContext* SparkyPKParser::Sparky_pkContext::data_label_wo_assign(size_t i) {
  return getRuleContext<SparkyPKParser::Data_label_wo_assignContext>(i);
}

std::vector<SparkyPKParser::Peak_2dContext *> SparkyPKParser::Sparky_pkContext::peak_2d() {
  return getRuleContexts<SparkyPKParser::Peak_2dContext>();
}

SparkyPKParser::Peak_2dContext* SparkyPKParser::Sparky_pkContext::peak_2d(size_t i) {
  return getRuleContext<SparkyPKParser::Peak_2dContext>(i);
}

std::vector<SparkyPKParser::Peak_3dContext *> SparkyPKParser::Sparky_pkContext::peak_3d() {
  return getRuleContexts<SparkyPKParser::Peak_3dContext>();
}

SparkyPKParser::Peak_3dContext* SparkyPKParser::Sparky_pkContext::peak_3d(size_t i) {
  return getRuleContext<SparkyPKParser::Peak_3dContext>(i);
}

std::vector<SparkyPKParser::Peak_4dContext *> SparkyPKParser::Sparky_pkContext::peak_4d() {
  return getRuleContexts<SparkyPKParser::Peak_4dContext>();
}

SparkyPKParser::Peak_4dContext* SparkyPKParser::Sparky_pkContext::peak_4d(size_t i) {
  return getRuleContext<SparkyPKParser::Peak_4dContext>(i);
}


size_t SparkyPKParser::Sparky_pkContext::getRuleIndex() const {
  return SparkyPKParser::RuleSparky_pk;
}


std::any SparkyPKParser::Sparky_pkContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyPKParserVisitor*>(visitor))
    return parserVisitor->visitSparky_pk(this);
  else
    return visitor->visitChildren(this);
}

SparkyPKParser::Sparky_pkContext* SparkyPKParser::sparky_pk() {
  Sparky_pkContext *_localctx = _tracker.createInstance<Sparky_pkContext>(_ctx, getState());
  enterRule(_localctx, 0, SparkyPKParser::RuleSparky_pk);
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
    setState(19);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
    case 1: {
      setState(18);
      match(SparkyPKParser::RETURN);
      break;
    }

    default:
      break;
    }
    setState(41);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 531462) != 0)) {
      setState(39);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 4, _ctx)) {
      case 1: {
        setState(21);
        data_label();
        break;
      }

      case 2: {
        setState(22);
        data_label_wo_assign();
        break;
      }

      case 3: {
        setState(24); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(23);
                  peak_2d();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(26); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 4: {
        setState(29); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(28);
                  peak_3d();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(31); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 2, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 5: {
        setState(34); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(33);
                  peak_4d();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(36); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 3, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 6: {
        setState(38);
        match(SparkyPKParser::RETURN);
        break;
      }

      default:
        break;
      }
      setState(43);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(44);
    match(SparkyPKParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Data_labelContext ------------------------------------------------------------------

SparkyPKParser::Data_labelContext::Data_labelContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::W1_LA() {
  return getToken(SparkyPKParser::W1_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::W2_LA() {
  return getToken(SparkyPKParser::W2_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::RETURN_LA() {
  return getToken(SparkyPKParser::RETURN_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Assignment() {
  return getToken(SparkyPKParser::Assignment, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Assignment_2d_ex() {
  return getToken(SparkyPKParser::Assignment_2d_ex, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Assignment_3d_ex() {
  return getToken(SparkyPKParser::Assignment_3d_ex, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Assignment_4d_ex() {
  return getToken(SparkyPKParser::Assignment_4d_ex, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::W3_LA() {
  return getToken(SparkyPKParser::W3_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::W4_LA() {
  return getToken(SparkyPKParser::W4_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::W1_Hz_LA() {
  return getToken(SparkyPKParser::W1_Hz_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::W2_Hz_LA() {
  return getToken(SparkyPKParser::W2_Hz_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::W3_Hz_LA() {
  return getToken(SparkyPKParser::W3_Hz_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::W4_Hz_LA() {
  return getToken(SparkyPKParser::W4_Hz_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Dev_w1_LA() {
  return getToken(SparkyPKParser::Dev_w1_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Dev_w2_LA() {
  return getToken(SparkyPKParser::Dev_w2_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Dev_w3_LA() {
  return getToken(SparkyPKParser::Dev_w3_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Dev_w4_LA() {
  return getToken(SparkyPKParser::Dev_w4_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Height_LA() {
  return getToken(SparkyPKParser::Height_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Volume_LA() {
  return getToken(SparkyPKParser::Volume_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Dummy_Rms_LA() {
  return getToken(SparkyPKParser::Dummy_Rms_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::S_N_LA() {
  return getToken(SparkyPKParser::S_N_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Lw1_Hz_LA() {
  return getToken(SparkyPKParser::Lw1_Hz_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Lw2_Hz_LA() {
  return getToken(SparkyPKParser::Lw2_Hz_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Lw3_Hz_LA() {
  return getToken(SparkyPKParser::Lw3_Hz_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Lw4_Hz_LA() {
  return getToken(SparkyPKParser::Lw4_Hz_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Atom1_LA() {
  return getToken(SparkyPKParser::Atom1_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Atom2_LA() {
  return getToken(SparkyPKParser::Atom2_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Atom3_LA() {
  return getToken(SparkyPKParser::Atom3_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Atom4_LA() {
  return getToken(SparkyPKParser::Atom4_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Distance_LA() {
  return getToken(SparkyPKParser::Distance_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Note_LA() {
  return getToken(SparkyPKParser::Note_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::RETURN() {
  return getToken(SparkyPKParser::RETURN, 0);
}

tree::TerminalNode* SparkyPKParser::Data_labelContext::Dummy_H_LA() {
  return getToken(SparkyPKParser::Dummy_H_LA, 0);
}


size_t SparkyPKParser::Data_labelContext::getRuleIndex() const {
  return SparkyPKParser::RuleData_label;
}


std::any SparkyPKParser::Data_labelContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyPKParserVisitor*>(visitor))
    return parserVisitor->visitData_label(this);
  else
    return visitor->visitChildren(this);
}

SparkyPKParser::Data_labelContext* SparkyPKParser::data_label() {
  Data_labelContext *_localctx = _tracker.createInstance<Data_labelContext>(_ctx, getState());
  enterRule(_localctx, 2, SparkyPKParser::RuleData_label);
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
    setState(46);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 7170) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(47);
    match(SparkyPKParser::W1_LA);
    setState(48);
    match(SparkyPKParser::W2_LA);
    setState(50);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::W3_LA) {
      setState(49);
      match(SparkyPKParser::W3_LA);
    }
    setState(53);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::W4_LA) {
      setState(52);
      match(SparkyPKParser::W4_LA);
    }
    setState(56);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::W1_Hz_LA) {
      setState(55);
      match(SparkyPKParser::W1_Hz_LA);
    }
    setState(59);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::W2_Hz_LA) {
      setState(58);
      match(SparkyPKParser::W2_Hz_LA);
    }
    setState(62);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::W3_Hz_LA) {
      setState(61);
      match(SparkyPKParser::W3_Hz_LA);
    }
    setState(65);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::W4_Hz_LA) {
      setState(64);
      match(SparkyPKParser::W4_Hz_LA);
    }
    setState(68);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Dev_w1_LA) {
      setState(67);
      match(SparkyPKParser::Dev_w1_LA);
    }
    setState(71);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Dev_w2_LA) {
      setState(70);
      match(SparkyPKParser::Dev_w2_LA);
    }
    setState(74);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Dev_w3_LA) {
      setState(73);
      match(SparkyPKParser::Dev_w3_LA);
    }
    setState(77);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Dev_w4_LA) {
      setState(76);
      match(SparkyPKParser::Dev_w4_LA);
    }
    setState(83);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Dummy_H_LA

    || _la == SparkyPKParser::Height_LA) {
      setState(80);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == SparkyPKParser::Dummy_H_LA) {
        setState(79);
        match(SparkyPKParser::Dummy_H_LA);
      }
      setState(82);
      match(SparkyPKParser::Height_LA);
    }
    setState(86);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Volume_LA) {
      setState(85);
      match(SparkyPKParser::Volume_LA);
    }
    setState(89);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Dummy_Rms_LA) {
      setState(88);
      match(SparkyPKParser::Dummy_Rms_LA);
    }
    setState(92);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::S_N_LA) {
      setState(91);
      match(SparkyPKParser::S_N_LA);
    }
    setState(95);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Lw1_Hz_LA) {
      setState(94);
      match(SparkyPKParser::Lw1_Hz_LA);
    }
    setState(98);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Lw2_Hz_LA) {
      setState(97);
      match(SparkyPKParser::Lw2_Hz_LA);
    }
    setState(101);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Lw3_Hz_LA) {
      setState(100);
      match(SparkyPKParser::Lw3_Hz_LA);
    }
    setState(104);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Lw4_Hz_LA) {
      setState(103);
      match(SparkyPKParser::Lw4_Hz_LA);
    }
    setState(107);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Atom1_LA) {
      setState(106);
      match(SparkyPKParser::Atom1_LA);
    }
    setState(110);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Atom2_LA) {
      setState(109);
      match(SparkyPKParser::Atom2_LA);
    }
    setState(113);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Atom3_LA) {
      setState(112);
      match(SparkyPKParser::Atom3_LA);
    }
    setState(116);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Atom4_LA) {
      setState(115);
      match(SparkyPKParser::Atom4_LA);
    }
    setState(119);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Distance_LA) {
      setState(118);
      match(SparkyPKParser::Distance_LA);
    }
    setState(122);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Note_LA) {
      setState(121);
      match(SparkyPKParser::Note_LA);
    }
    setState(124);
    match(SparkyPKParser::RETURN_LA);
    setState(126);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 31, _ctx)) {
    case 1: {
      setState(125);
      match(SparkyPKParser::RETURN);
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

//----------------- Data_label_wo_assignContext ------------------------------------------------------------------

SparkyPKParser::Data_label_wo_assignContext::Data_label_wo_assignContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::W1() {
  return getToken(SparkyPKParser::W1, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::W2_LA() {
  return getToken(SparkyPKParser::W2_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::RETURN_LA() {
  return getToken(SparkyPKParser::RETURN_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::W3_LA() {
  return getToken(SparkyPKParser::W3_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::W4_LA() {
  return getToken(SparkyPKParser::W4_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::W1_Hz_LA() {
  return getToken(SparkyPKParser::W1_Hz_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::W2_Hz_LA() {
  return getToken(SparkyPKParser::W2_Hz_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::W3_Hz_LA() {
  return getToken(SparkyPKParser::W3_Hz_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::W4_Hz_LA() {
  return getToken(SparkyPKParser::W4_Hz_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::Dev_w1_LA() {
  return getToken(SparkyPKParser::Dev_w1_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::Dev_w2_LA() {
  return getToken(SparkyPKParser::Dev_w2_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::Dev_w3_LA() {
  return getToken(SparkyPKParser::Dev_w3_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::Dev_w4_LA() {
  return getToken(SparkyPKParser::Dev_w4_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::Height_LA() {
  return getToken(SparkyPKParser::Height_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::Volume_LA() {
  return getToken(SparkyPKParser::Volume_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::Dummy_Rms_LA() {
  return getToken(SparkyPKParser::Dummy_Rms_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::S_N_LA() {
  return getToken(SparkyPKParser::S_N_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::Lw1_Hz_LA() {
  return getToken(SparkyPKParser::Lw1_Hz_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::Lw2_Hz_LA() {
  return getToken(SparkyPKParser::Lw2_Hz_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::Lw3_Hz_LA() {
  return getToken(SparkyPKParser::Lw3_Hz_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::Lw4_Hz_LA() {
  return getToken(SparkyPKParser::Lw4_Hz_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::Distance_LA() {
  return getToken(SparkyPKParser::Distance_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::Note_LA() {
  return getToken(SparkyPKParser::Note_LA, 0);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::RETURN() {
  return getToken(SparkyPKParser::RETURN, 0);
}

std::vector<SparkyPKParser::Peak_wo_assignContext *> SparkyPKParser::Data_label_wo_assignContext::peak_wo_assign() {
  return getRuleContexts<SparkyPKParser::Peak_wo_assignContext>();
}

SparkyPKParser::Peak_wo_assignContext* SparkyPKParser::Data_label_wo_assignContext::peak_wo_assign(size_t i) {
  return getRuleContext<SparkyPKParser::Peak_wo_assignContext>(i);
}

tree::TerminalNode* SparkyPKParser::Data_label_wo_assignContext::Dummy_H_LA() {
  return getToken(SparkyPKParser::Dummy_H_LA, 0);
}


size_t SparkyPKParser::Data_label_wo_assignContext::getRuleIndex() const {
  return SparkyPKParser::RuleData_label_wo_assign;
}


std::any SparkyPKParser::Data_label_wo_assignContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyPKParserVisitor*>(visitor))
    return parserVisitor->visitData_label_wo_assign(this);
  else
    return visitor->visitChildren(this);
}

SparkyPKParser::Data_label_wo_assignContext* SparkyPKParser::data_label_wo_assign() {
  Data_label_wo_assignContext *_localctx = _tracker.createInstance<Data_label_wo_assignContext>(_ctx, getState());
  enterRule(_localctx, 4, SparkyPKParser::RuleData_label_wo_assign);
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
    setState(128);
    match(SparkyPKParser::W1);
    setState(129);
    match(SparkyPKParser::W2_LA);
    setState(131);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::W3_LA) {
      setState(130);
      match(SparkyPKParser::W3_LA);
    }
    setState(134);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::W4_LA) {
      setState(133);
      match(SparkyPKParser::W4_LA);
    }
    setState(137);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::W1_Hz_LA) {
      setState(136);
      match(SparkyPKParser::W1_Hz_LA);
    }
    setState(140);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::W2_Hz_LA) {
      setState(139);
      match(SparkyPKParser::W2_Hz_LA);
    }
    setState(143);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::W3_Hz_LA) {
      setState(142);
      match(SparkyPKParser::W3_Hz_LA);
    }
    setState(146);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::W4_Hz_LA) {
      setState(145);
      match(SparkyPKParser::W4_Hz_LA);
    }
    setState(149);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Dev_w1_LA) {
      setState(148);
      match(SparkyPKParser::Dev_w1_LA);
    }
    setState(152);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Dev_w2_LA) {
      setState(151);
      match(SparkyPKParser::Dev_w2_LA);
    }
    setState(155);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Dev_w3_LA) {
      setState(154);
      match(SparkyPKParser::Dev_w3_LA);
    }
    setState(158);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Dev_w4_LA) {
      setState(157);
      match(SparkyPKParser::Dev_w4_LA);
    }
    setState(164);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Dummy_H_LA

    || _la == SparkyPKParser::Height_LA) {
      setState(161);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == SparkyPKParser::Dummy_H_LA) {
        setState(160);
        match(SparkyPKParser::Dummy_H_LA);
      }
      setState(163);
      match(SparkyPKParser::Height_LA);
    }
    setState(167);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Volume_LA) {
      setState(166);
      match(SparkyPKParser::Volume_LA);
    }
    setState(170);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Dummy_Rms_LA) {
      setState(169);
      match(SparkyPKParser::Dummy_Rms_LA);
    }
    setState(173);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::S_N_LA) {
      setState(172);
      match(SparkyPKParser::S_N_LA);
    }
    setState(176);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Lw1_Hz_LA) {
      setState(175);
      match(SparkyPKParser::Lw1_Hz_LA);
    }
    setState(179);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Lw2_Hz_LA) {
      setState(178);
      match(SparkyPKParser::Lw2_Hz_LA);
    }
    setState(182);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Lw3_Hz_LA) {
      setState(181);
      match(SparkyPKParser::Lw3_Hz_LA);
    }
    setState(185);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Lw4_Hz_LA) {
      setState(184);
      match(SparkyPKParser::Lw4_Hz_LA);
    }
    setState(188);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Distance_LA) {
      setState(187);
      match(SparkyPKParser::Distance_LA);
    }
    setState(191);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::Note_LA) {
      setState(190);
      match(SparkyPKParser::Note_LA);
    }
    setState(193);
    match(SparkyPKParser::RETURN_LA);
    setState(195);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyPKParser::RETURN) {
      setState(194);
      match(SparkyPKParser::RETURN);
    }
    setState(198); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(197);
      peak_wo_assign();
      setState(200); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 120) != 0));
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Peak_2dContext ------------------------------------------------------------------

SparkyPKParser::Peak_2dContext::Peak_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyPKParser::Peak_2dContext::Assignment_2d_ex() {
  return getToken(SparkyPKParser::Assignment_2d_ex, 0);
}

std::vector<tree::TerminalNode *> SparkyPKParser::Peak_2dContext::Float() {
  return getTokens(SparkyPKParser::Float);
}

tree::TerminalNode* SparkyPKParser::Peak_2dContext::Float(size_t i) {
  return getToken(SparkyPKParser::Float, i);
}

tree::TerminalNode* SparkyPKParser::Peak_2dContext::RETURN() {
  return getToken(SparkyPKParser::RETURN, 0);
}

tree::TerminalNode* SparkyPKParser::Peak_2dContext::EOF() {
  return getToken(SparkyPKParser::EOF, 0);
}

std::vector<SparkyPKParser::NumberContext *> SparkyPKParser::Peak_2dContext::number() {
  return getRuleContexts<SparkyPKParser::NumberContext>();
}

SparkyPKParser::NumberContext* SparkyPKParser::Peak_2dContext::number(size_t i) {
  return getRuleContext<SparkyPKParser::NumberContext>(i);
}

std::vector<SparkyPKParser::NoteContext *> SparkyPKParser::Peak_2dContext::note() {
  return getRuleContexts<SparkyPKParser::NoteContext>();
}

SparkyPKParser::NoteContext* SparkyPKParser::Peak_2dContext::note(size_t i) {
  return getRuleContext<SparkyPKParser::NoteContext>(i);
}


size_t SparkyPKParser::Peak_2dContext::getRuleIndex() const {
  return SparkyPKParser::RulePeak_2d;
}


std::any SparkyPKParser::Peak_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_2d(this);
  else
    return visitor->visitChildren(this);
}

SparkyPKParser::Peak_2dContext* SparkyPKParser::peak_2d() {
  Peak_2dContext *_localctx = _tracker.createInstance<Peak_2dContext>(_ctx, getState());
  enterRule(_localctx, 6, SparkyPKParser::RulePeak_2d);
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
    setState(202);
    match(SparkyPKParser::Assignment_2d_ex);
    setState(203);
    match(SparkyPKParser::Float);
    setState(204);
    match(SparkyPKParser::Float);
    setState(206); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(205);
              number();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(208); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 55, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(213);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 253976) != 0)) {
      setState(210);
      note();
      setState(215);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(216);
    _la = _input->LA(1);
    if (!(_la == SparkyPKParser::EOF

    || _la == SparkyPKParser::RETURN)) {
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

//----------------- Peak_3dContext ------------------------------------------------------------------

SparkyPKParser::Peak_3dContext::Peak_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyPKParser::Peak_3dContext::Assignment_3d_ex() {
  return getToken(SparkyPKParser::Assignment_3d_ex, 0);
}

std::vector<tree::TerminalNode *> SparkyPKParser::Peak_3dContext::Float() {
  return getTokens(SparkyPKParser::Float);
}

tree::TerminalNode* SparkyPKParser::Peak_3dContext::Float(size_t i) {
  return getToken(SparkyPKParser::Float, i);
}

tree::TerminalNode* SparkyPKParser::Peak_3dContext::RETURN() {
  return getToken(SparkyPKParser::RETURN, 0);
}

tree::TerminalNode* SparkyPKParser::Peak_3dContext::EOF() {
  return getToken(SparkyPKParser::EOF, 0);
}

std::vector<SparkyPKParser::NumberContext *> SparkyPKParser::Peak_3dContext::number() {
  return getRuleContexts<SparkyPKParser::NumberContext>();
}

SparkyPKParser::NumberContext* SparkyPKParser::Peak_3dContext::number(size_t i) {
  return getRuleContext<SparkyPKParser::NumberContext>(i);
}

std::vector<SparkyPKParser::NoteContext *> SparkyPKParser::Peak_3dContext::note() {
  return getRuleContexts<SparkyPKParser::NoteContext>();
}

SparkyPKParser::NoteContext* SparkyPKParser::Peak_3dContext::note(size_t i) {
  return getRuleContext<SparkyPKParser::NoteContext>(i);
}


size_t SparkyPKParser::Peak_3dContext::getRuleIndex() const {
  return SparkyPKParser::RulePeak_3d;
}


std::any SparkyPKParser::Peak_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_3d(this);
  else
    return visitor->visitChildren(this);
}

SparkyPKParser::Peak_3dContext* SparkyPKParser::peak_3d() {
  Peak_3dContext *_localctx = _tracker.createInstance<Peak_3dContext>(_ctx, getState());
  enterRule(_localctx, 8, SparkyPKParser::RulePeak_3d);
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
    setState(218);
    match(SparkyPKParser::Assignment_3d_ex);
    setState(219);
    match(SparkyPKParser::Float);
    setState(220);
    match(SparkyPKParser::Float);
    setState(221);
    match(SparkyPKParser::Float);
    setState(223); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(222);
              number();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(225); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 57, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(230);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 253976) != 0)) {
      setState(227);
      note();
      setState(232);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(233);
    _la = _input->LA(1);
    if (!(_la == SparkyPKParser::EOF

    || _la == SparkyPKParser::RETURN)) {
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

//----------------- Peak_4dContext ------------------------------------------------------------------

SparkyPKParser::Peak_4dContext::Peak_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyPKParser::Peak_4dContext::Assignment_4d_ex() {
  return getToken(SparkyPKParser::Assignment_4d_ex, 0);
}

std::vector<tree::TerminalNode *> SparkyPKParser::Peak_4dContext::Float() {
  return getTokens(SparkyPKParser::Float);
}

tree::TerminalNode* SparkyPKParser::Peak_4dContext::Float(size_t i) {
  return getToken(SparkyPKParser::Float, i);
}

tree::TerminalNode* SparkyPKParser::Peak_4dContext::RETURN() {
  return getToken(SparkyPKParser::RETURN, 0);
}

tree::TerminalNode* SparkyPKParser::Peak_4dContext::EOF() {
  return getToken(SparkyPKParser::EOF, 0);
}

std::vector<SparkyPKParser::NumberContext *> SparkyPKParser::Peak_4dContext::number() {
  return getRuleContexts<SparkyPKParser::NumberContext>();
}

SparkyPKParser::NumberContext* SparkyPKParser::Peak_4dContext::number(size_t i) {
  return getRuleContext<SparkyPKParser::NumberContext>(i);
}

std::vector<SparkyPKParser::NoteContext *> SparkyPKParser::Peak_4dContext::note() {
  return getRuleContexts<SparkyPKParser::NoteContext>();
}

SparkyPKParser::NoteContext* SparkyPKParser::Peak_4dContext::note(size_t i) {
  return getRuleContext<SparkyPKParser::NoteContext>(i);
}


size_t SparkyPKParser::Peak_4dContext::getRuleIndex() const {
  return SparkyPKParser::RulePeak_4d;
}


std::any SparkyPKParser::Peak_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_4d(this);
  else
    return visitor->visitChildren(this);
}

SparkyPKParser::Peak_4dContext* SparkyPKParser::peak_4d() {
  Peak_4dContext *_localctx = _tracker.createInstance<Peak_4dContext>(_ctx, getState());
  enterRule(_localctx, 10, SparkyPKParser::RulePeak_4d);
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
    setState(235);
    match(SparkyPKParser::Assignment_4d_ex);
    setState(236);
    match(SparkyPKParser::Float);
    setState(237);
    match(SparkyPKParser::Float);
    setState(238);
    match(SparkyPKParser::Float);
    setState(239);
    match(SparkyPKParser::Float);
    setState(241); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(240);
              number();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(243); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 59, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(248);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 253976) != 0)) {
      setState(245);
      note();
      setState(250);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(251);
    _la = _input->LA(1);
    if (!(_la == SparkyPKParser::EOF

    || _la == SparkyPKParser::RETURN)) {
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

//----------------- Peak_wo_assignContext ------------------------------------------------------------------

SparkyPKParser::Peak_wo_assignContext::Peak_wo_assignContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyPKParser::Peak_wo_assignContext::RETURN() {
  return getToken(SparkyPKParser::RETURN, 0);
}

tree::TerminalNode* SparkyPKParser::Peak_wo_assignContext::EOF() {
  return getToken(SparkyPKParser::EOF, 0);
}

std::vector<SparkyPKParser::NumberContext *> SparkyPKParser::Peak_wo_assignContext::number() {
  return getRuleContexts<SparkyPKParser::NumberContext>();
}

SparkyPKParser::NumberContext* SparkyPKParser::Peak_wo_assignContext::number(size_t i) {
  return getRuleContext<SparkyPKParser::NumberContext>(i);
}

SparkyPKParser::NoteContext* SparkyPKParser::Peak_wo_assignContext::note() {
  return getRuleContext<SparkyPKParser::NoteContext>(0);
}


size_t SparkyPKParser::Peak_wo_assignContext::getRuleIndex() const {
  return SparkyPKParser::RulePeak_wo_assign;
}


std::any SparkyPKParser::Peak_wo_assignContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_wo_assign(this);
  else
    return visitor->visitChildren(this);
}

SparkyPKParser::Peak_wo_assignContext* SparkyPKParser::peak_wo_assign() {
  Peak_wo_assignContext *_localctx = _tracker.createInstance<Peak_wo_assignContext>(_ctx, getState());
  enterRule(_localctx, 12, SparkyPKParser::RulePeak_wo_assign);
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
    setState(254); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(253);
              number();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(256); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 61, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(259);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 253976) != 0)) {
      setState(258);
      note();
    }
    setState(261);
    _la = _input->LA(1);
    if (!(_la == SparkyPKParser::EOF

    || _la == SparkyPKParser::RETURN)) {
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

SparkyPKParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyPKParser::NumberContext::Real_vol() {
  return getToken(SparkyPKParser::Real_vol, 0);
}

tree::TerminalNode* SparkyPKParser::NumberContext::Real() {
  return getToken(SparkyPKParser::Real, 0);
}

tree::TerminalNode* SparkyPKParser::NumberContext::Float() {
  return getToken(SparkyPKParser::Float, 0);
}

tree::TerminalNode* SparkyPKParser::NumberContext::Integer() {
  return getToken(SparkyPKParser::Integer, 0);
}


size_t SparkyPKParser::NumberContext::getRuleIndex() const {
  return SparkyPKParser::RuleNumber;
}


std::any SparkyPKParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyPKParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

SparkyPKParser::NumberContext* SparkyPKParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 14, SparkyPKParser::RuleNumber);
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
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 120) != 0))) {
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

//----------------- NoteContext ------------------------------------------------------------------

SparkyPKParser::NoteContext::NoteContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyPKParser::NoteContext::Simple_name() {
  return getToken(SparkyPKParser::Simple_name, 0);
}

tree::TerminalNode* SparkyPKParser::NoteContext::Integer() {
  return getToken(SparkyPKParser::Integer, 0);
}

tree::TerminalNode* SparkyPKParser::NoteContext::Float() {
  return getToken(SparkyPKParser::Float, 0);
}

tree::TerminalNode* SparkyPKParser::NoteContext::Note_2d_ex() {
  return getToken(SparkyPKParser::Note_2d_ex, 0);
}

tree::TerminalNode* SparkyPKParser::NoteContext::Note_3d_ex() {
  return getToken(SparkyPKParser::Note_3d_ex, 0);
}

tree::TerminalNode* SparkyPKParser::NoteContext::Note_4d_ex() {
  return getToken(SparkyPKParser::Note_4d_ex, 0);
}

tree::TerminalNode* SparkyPKParser::NoteContext::Note_ex() {
  return getToken(SparkyPKParser::Note_ex, 0);
}


size_t SparkyPKParser::NoteContext::getRuleIndex() const {
  return SparkyPKParser::RuleNote;
}


std::any SparkyPKParser::NoteContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyPKParserVisitor*>(visitor))
    return parserVisitor->visitNote(this);
  else
    return visitor->visitChildren(this);
}

SparkyPKParser::NoteContext* SparkyPKParser::note() {
  NoteContext *_localctx = _tracker.createInstance<NoteContext>(_ctx, getState());
  enterRule(_localctx, 16, SparkyPKParser::RuleNote);
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
    setState(265);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 253976) != 0))) {
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

void SparkyPKParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  sparkypkparserParserInitialize();
#else
  ::antlr4::internal::call_once(sparkypkparserParserOnceFlag, sparkypkparserParserInitialize);
#endif
}
