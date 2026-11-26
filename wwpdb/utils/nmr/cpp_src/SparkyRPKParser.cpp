
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SparkyRPKParser.g4 by ANTLR 4.13.2


#include "SparkyRPKParserVisitor.h"

#include "SparkyRPKParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct SparkyRPKParserStaticData final {
  SparkyRPKParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  SparkyRPKParserStaticData(const SparkyRPKParserStaticData&) = delete;
  SparkyRPKParserStaticData(SparkyRPKParserStaticData&&) = delete;
  SparkyRPKParserStaticData& operator=(const SparkyRPKParserStaticData&) = delete;
  SparkyRPKParserStaticData& operator=(SparkyRPKParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag sparkyrpkparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<SparkyRPKParserStaticData> sparkyrpkparserParserStaticData = nullptr;

void sparkyrpkparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (sparkyrpkparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(sparkyrpkparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<SparkyRPKParserStaticData>(
    std::vector<std::string>{
      "sparky_rpk", "data_label", "data_label_wo_assign", "peak_2d", "peak_3d", 
      "peak_4d", "peak_wo_assign", "position", "number", "note"
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
  	4,1,51,272,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,1,0,3,0,22,8,0,1,0,1,0,1,0,4,0,27,8,0,11,0,12,0,
  	28,1,0,4,0,32,8,0,11,0,12,0,33,1,0,4,0,37,8,0,11,0,12,0,38,1,0,5,0,42,
  	8,0,10,0,12,0,45,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,53,8,1,1,1,3,1,56,8,
  	1,1,1,3,1,59,8,1,1,1,3,1,62,8,1,1,1,3,1,65,8,1,1,1,3,1,68,8,1,1,1,3,1,
  	71,8,1,1,1,3,1,74,8,1,1,1,3,1,77,8,1,1,1,3,1,80,8,1,1,1,3,1,83,8,1,1,
  	1,3,1,86,8,1,1,1,3,1,89,8,1,1,1,3,1,92,8,1,1,1,3,1,95,8,1,1,1,3,1,98,
  	8,1,1,1,3,1,101,8,1,1,1,3,1,104,8,1,1,1,3,1,107,8,1,1,1,3,1,110,8,1,1,
  	1,3,1,113,8,1,1,1,3,1,116,8,1,1,1,3,1,119,8,1,1,1,3,1,122,8,1,1,1,3,1,
  	125,8,1,1,1,1,1,3,1,129,8,1,1,2,1,2,1,2,3,2,134,8,2,1,2,3,2,137,8,2,1,
  	2,3,2,140,8,2,1,2,3,2,143,8,2,1,2,3,2,146,8,2,1,2,3,2,149,8,2,1,2,3,2,
  	152,8,2,1,2,3,2,155,8,2,1,2,3,2,158,8,2,1,2,3,2,161,8,2,1,2,3,2,164,8,
  	2,1,2,3,2,167,8,2,1,2,3,2,170,8,2,1,2,3,2,173,8,2,1,2,3,2,176,8,2,1,2,
  	3,2,179,8,2,1,2,3,2,182,8,2,1,2,3,2,185,8,2,1,2,3,2,188,8,2,1,2,3,2,191,
  	8,2,1,2,3,2,194,8,2,1,2,1,2,3,2,198,8,2,1,2,4,2,201,8,2,11,2,12,2,202,
  	1,3,1,3,1,3,1,3,4,3,209,8,3,11,3,12,3,210,1,3,5,3,214,8,3,10,3,12,3,217,
  	9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,4,4,226,8,4,11,4,12,4,227,1,4,5,4,231,
  	8,4,10,4,12,4,234,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,4,5,244,8,5,11,
  	5,12,5,245,1,5,5,5,249,8,5,10,5,12,5,252,9,5,1,5,1,5,1,6,4,6,257,8,6,
  	11,6,12,6,258,1,6,3,6,262,8,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,0,0,
  	10,0,2,4,6,8,10,12,14,16,18,0,5,2,0,1,1,10,12,1,1,19,19,1,0,3,4,1,0,3,
  	6,2,0,3,4,13,17,328,0,21,1,0,0,0,2,48,1,0,0,0,4,130,1,0,0,0,6,204,1,0,
  	0,0,8,220,1,0,0,0,10,237,1,0,0,0,12,256,1,0,0,0,14,265,1,0,0,0,16,267,
  	1,0,0,0,18,269,1,0,0,0,20,22,5,19,0,0,21,20,1,0,0,0,21,22,1,0,0,0,22,
  	43,1,0,0,0,23,42,3,2,1,0,24,42,3,4,2,0,25,27,3,6,3,0,26,25,1,0,0,0,27,
  	28,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,42,1,0,0,0,30,32,3,8,4,0,31,
  	30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,42,1,0,0,0,35,
  	37,3,10,5,0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,
  	42,1,0,0,0,40,42,5,19,0,0,41,23,1,0,0,0,41,24,1,0,0,0,41,26,1,0,0,0,41,
  	31,1,0,0,0,41,36,1,0,0,0,41,40,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,
  	44,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,46,47,5,0,0,1,47,1,1,0,0,0,48,
  	49,7,0,0,0,49,50,5,31,0,0,50,52,5,32,0,0,51,53,5,33,0,0,52,51,1,0,0,0,
  	52,53,1,0,0,0,53,55,1,0,0,0,54,56,5,34,0,0,55,54,1,0,0,0,55,56,1,0,0,
  	0,56,58,1,0,0,0,57,59,5,23,0,0,58,57,1,0,0,0,58,59,1,0,0,0,59,61,1,0,
  	0,0,60,62,5,24,0,0,61,60,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,65,5,
  	25,0,0,64,63,1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,68,5,26,0,0,67,66,
  	1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,71,5,35,0,0,70,69,1,0,0,0,70,71,
  	1,0,0,0,71,73,1,0,0,0,72,74,5,36,0,0,73,72,1,0,0,0,73,74,1,0,0,0,74,76,
  	1,0,0,0,75,77,5,37,0,0,76,75,1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,80,
  	5,38,0,0,79,78,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,83,5,41,0,0,82,
  	81,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,86,5,42,0,0,85,84,1,0,0,0,85,
  	86,1,0,0,0,86,88,1,0,0,0,87,89,5,39,0,0,88,87,1,0,0,0,88,89,1,0,0,0,89,
  	91,1,0,0,0,90,92,5,40,0,0,91,90,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,
  	95,5,43,0,0,94,93,1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,96,98,5,27,0,0,
  	97,96,1,0,0,0,97,98,1,0,0,0,98,100,1,0,0,0,99,101,5,28,0,0,100,99,1,0,
  	0,0,100,101,1,0,0,0,101,103,1,0,0,0,102,104,5,29,0,0,103,102,1,0,0,0,
  	103,104,1,0,0,0,104,106,1,0,0,0,105,107,5,30,0,0,106,105,1,0,0,0,106,
  	107,1,0,0,0,107,109,1,0,0,0,108,110,5,44,0,0,109,108,1,0,0,0,109,110,
  	1,0,0,0,110,112,1,0,0,0,111,113,5,45,0,0,112,111,1,0,0,0,112,113,1,0,
  	0,0,113,115,1,0,0,0,114,116,5,46,0,0,115,114,1,0,0,0,115,116,1,0,0,0,
  	116,118,1,0,0,0,117,119,5,47,0,0,118,117,1,0,0,0,118,119,1,0,0,0,119,
  	121,1,0,0,0,120,122,5,48,0,0,121,120,1,0,0,0,121,122,1,0,0,0,122,124,
  	1,0,0,0,123,125,5,49,0,0,124,123,1,0,0,0,124,125,1,0,0,0,125,126,1,0,
  	0,0,126,128,5,51,0,0,127,129,5,19,0,0,128,127,1,0,0,0,128,129,1,0,0,0,
  	129,3,1,0,0,0,130,131,5,2,0,0,131,133,5,32,0,0,132,134,5,33,0,0,133,132,
  	1,0,0,0,133,134,1,0,0,0,134,136,1,0,0,0,135,137,5,34,0,0,136,135,1,0,
  	0,0,136,137,1,0,0,0,137,139,1,0,0,0,138,140,5,23,0,0,139,138,1,0,0,0,
  	139,140,1,0,0,0,140,142,1,0,0,0,141,143,5,24,0,0,142,141,1,0,0,0,142,
  	143,1,0,0,0,143,145,1,0,0,0,144,146,5,25,0,0,145,144,1,0,0,0,145,146,
  	1,0,0,0,146,148,1,0,0,0,147,149,5,26,0,0,148,147,1,0,0,0,148,149,1,0,
  	0,0,149,151,1,0,0,0,150,152,5,35,0,0,151,150,1,0,0,0,151,152,1,0,0,0,
  	152,154,1,0,0,0,153,155,5,36,0,0,154,153,1,0,0,0,154,155,1,0,0,0,155,
  	157,1,0,0,0,156,158,5,37,0,0,157,156,1,0,0,0,157,158,1,0,0,0,158,160,
  	1,0,0,0,159,161,5,38,0,0,160,159,1,0,0,0,160,161,1,0,0,0,161,163,1,0,
  	0,0,162,164,5,41,0,0,163,162,1,0,0,0,163,164,1,0,0,0,164,166,1,0,0,0,
  	165,167,5,42,0,0,166,165,1,0,0,0,166,167,1,0,0,0,167,169,1,0,0,0,168,
  	170,5,39,0,0,169,168,1,0,0,0,169,170,1,0,0,0,170,172,1,0,0,0,171,173,
  	5,40,0,0,172,171,1,0,0,0,172,173,1,0,0,0,173,175,1,0,0,0,174,176,5,43,
  	0,0,175,174,1,0,0,0,175,176,1,0,0,0,176,178,1,0,0,0,177,179,5,27,0,0,
  	178,177,1,0,0,0,178,179,1,0,0,0,179,181,1,0,0,0,180,182,5,28,0,0,181,
  	180,1,0,0,0,181,182,1,0,0,0,182,184,1,0,0,0,183,185,5,29,0,0,184,183,
  	1,0,0,0,184,185,1,0,0,0,185,187,1,0,0,0,186,188,5,30,0,0,187,186,1,0,
  	0,0,187,188,1,0,0,0,188,190,1,0,0,0,189,191,5,48,0,0,190,189,1,0,0,0,
  	190,191,1,0,0,0,191,193,1,0,0,0,192,194,5,49,0,0,193,192,1,0,0,0,193,
  	194,1,0,0,0,194,195,1,0,0,0,195,197,5,51,0,0,196,198,5,19,0,0,197,196,
  	1,0,0,0,197,198,1,0,0,0,198,200,1,0,0,0,199,201,3,12,6,0,200,199,1,0,
  	0,0,201,202,1,0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,203,5,1,0,0,0,204,
  	205,5,10,0,0,205,206,3,14,7,0,206,208,3,14,7,0,207,209,3,16,8,0,208,207,
  	1,0,0,0,209,210,1,0,0,0,210,208,1,0,0,0,210,211,1,0,0,0,211,215,1,0,0,
  	0,212,214,3,18,9,0,213,212,1,0,0,0,214,217,1,0,0,0,215,213,1,0,0,0,215,
  	216,1,0,0,0,216,218,1,0,0,0,217,215,1,0,0,0,218,219,7,1,0,0,219,7,1,0,
  	0,0,220,221,5,11,0,0,221,222,3,14,7,0,222,223,3,14,7,0,223,225,3,14,7,
  	0,224,226,3,16,8,0,225,224,1,0,0,0,226,227,1,0,0,0,227,225,1,0,0,0,227,
  	228,1,0,0,0,228,232,1,0,0,0,229,231,3,18,9,0,230,229,1,0,0,0,231,234,
  	1,0,0,0,232,230,1,0,0,0,232,233,1,0,0,0,233,235,1,0,0,0,234,232,1,0,0,
  	0,235,236,7,1,0,0,236,9,1,0,0,0,237,238,5,12,0,0,238,239,3,14,7,0,239,
  	240,3,14,7,0,240,241,3,14,7,0,241,243,3,14,7,0,242,244,3,16,8,0,243,242,
  	1,0,0,0,244,245,1,0,0,0,245,243,1,0,0,0,245,246,1,0,0,0,246,250,1,0,0,
  	0,247,249,3,18,9,0,248,247,1,0,0,0,249,252,1,0,0,0,250,248,1,0,0,0,250,
  	251,1,0,0,0,251,253,1,0,0,0,252,250,1,0,0,0,253,254,7,1,0,0,254,11,1,
  	0,0,0,255,257,3,16,8,0,256,255,1,0,0,0,257,258,1,0,0,0,258,256,1,0,0,
  	0,258,259,1,0,0,0,259,261,1,0,0,0,260,262,3,18,9,0,261,260,1,0,0,0,261,
  	262,1,0,0,0,262,263,1,0,0,0,263,264,7,1,0,0,264,13,1,0,0,0,265,266,7,
  	2,0,0,266,15,1,0,0,0,267,268,7,3,0,0,268,17,1,0,0,0,269,270,7,4,0,0,270,
  	19,1,0,0,0,63,21,28,33,38,41,43,52,55,58,61,64,67,70,73,76,79,82,85,88,
  	91,94,97,100,103,106,109,112,115,118,121,124,128,133,136,139,142,145,
  	148,151,154,157,160,163,166,169,172,175,178,181,184,187,190,193,197,202,
  	210,215,227,232,245,250,258,261
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  sparkyrpkparserParserStaticData = std::move(staticData);
}

}

SparkyRPKParser::SparkyRPKParser(TokenStream *input) : SparkyRPKParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

SparkyRPKParser::SparkyRPKParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  SparkyRPKParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *sparkyrpkparserParserStaticData->atn, sparkyrpkparserParserStaticData->decisionToDFA, sparkyrpkparserParserStaticData->sharedContextCache, options);
}

SparkyRPKParser::~SparkyRPKParser() {
  delete _interpreter;
}

const atn::ATN& SparkyRPKParser::getATN() const {
  return *sparkyrpkparserParserStaticData->atn;
}

std::string SparkyRPKParser::getGrammarFileName() const {
  return "SparkyRPKParser.g4";
}

const std::vector<std::string>& SparkyRPKParser::getRuleNames() const {
  return sparkyrpkparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& SparkyRPKParser::getVocabulary() const {
  return sparkyrpkparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView SparkyRPKParser::getSerializedATN() const {
  return sparkyrpkparserParserStaticData->serializedATN;
}


//----------------- Sparky_rpkContext ------------------------------------------------------------------

SparkyRPKParser::Sparky_rpkContext::Sparky_rpkContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyRPKParser::Sparky_rpkContext::EOF() {
  return getToken(SparkyRPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> SparkyRPKParser::Sparky_rpkContext::RETURN() {
  return getTokens(SparkyRPKParser::RETURN);
}

tree::TerminalNode* SparkyRPKParser::Sparky_rpkContext::RETURN(size_t i) {
  return getToken(SparkyRPKParser::RETURN, i);
}

std::vector<SparkyRPKParser::Data_labelContext *> SparkyRPKParser::Sparky_rpkContext::data_label() {
  return getRuleContexts<SparkyRPKParser::Data_labelContext>();
}

SparkyRPKParser::Data_labelContext* SparkyRPKParser::Sparky_rpkContext::data_label(size_t i) {
  return getRuleContext<SparkyRPKParser::Data_labelContext>(i);
}

std::vector<SparkyRPKParser::Data_label_wo_assignContext *> SparkyRPKParser::Sparky_rpkContext::data_label_wo_assign() {
  return getRuleContexts<SparkyRPKParser::Data_label_wo_assignContext>();
}

SparkyRPKParser::Data_label_wo_assignContext* SparkyRPKParser::Sparky_rpkContext::data_label_wo_assign(size_t i) {
  return getRuleContext<SparkyRPKParser::Data_label_wo_assignContext>(i);
}

std::vector<SparkyRPKParser::Peak_2dContext *> SparkyRPKParser::Sparky_rpkContext::peak_2d() {
  return getRuleContexts<SparkyRPKParser::Peak_2dContext>();
}

SparkyRPKParser::Peak_2dContext* SparkyRPKParser::Sparky_rpkContext::peak_2d(size_t i) {
  return getRuleContext<SparkyRPKParser::Peak_2dContext>(i);
}

std::vector<SparkyRPKParser::Peak_3dContext *> SparkyRPKParser::Sparky_rpkContext::peak_3d() {
  return getRuleContexts<SparkyRPKParser::Peak_3dContext>();
}

SparkyRPKParser::Peak_3dContext* SparkyRPKParser::Sparky_rpkContext::peak_3d(size_t i) {
  return getRuleContext<SparkyRPKParser::Peak_3dContext>(i);
}

std::vector<SparkyRPKParser::Peak_4dContext *> SparkyRPKParser::Sparky_rpkContext::peak_4d() {
  return getRuleContexts<SparkyRPKParser::Peak_4dContext>();
}

SparkyRPKParser::Peak_4dContext* SparkyRPKParser::Sparky_rpkContext::peak_4d(size_t i) {
  return getRuleContext<SparkyRPKParser::Peak_4dContext>(i);
}


size_t SparkyRPKParser::Sparky_rpkContext::getRuleIndex() const {
  return SparkyRPKParser::RuleSparky_rpk;
}


std::any SparkyRPKParser::Sparky_rpkContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyRPKParserVisitor*>(visitor))
    return parserVisitor->visitSparky_rpk(this);
  else
    return visitor->visitChildren(this);
}

SparkyRPKParser::Sparky_rpkContext* SparkyRPKParser::sparky_rpk() {
  Sparky_rpkContext *_localctx = _tracker.createInstance<Sparky_rpkContext>(_ctx, getState());
  enterRule(_localctx, 0, SparkyRPKParser::RuleSparky_rpk);
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
    setState(21);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
    case 1: {
      setState(20);
      match(SparkyRPKParser::RETURN);
      break;
    }

    default:
      break;
    }
    setState(43);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 531462) != 0)) {
      setState(41);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 4, _ctx)) {
      case 1: {
        setState(23);
        data_label();
        break;
      }

      case 2: {
        setState(24);
        data_label_wo_assign();
        break;
      }

      case 3: {
        setState(26); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(25);
                  peak_2d();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(28); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 4: {
        setState(31); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(30);
                  peak_3d();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(33); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 2, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 5: {
        setState(36); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(35);
                  peak_4d();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(38); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 3, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 6: {
        setState(40);
        match(SparkyRPKParser::RETURN);
        break;
      }

      default:
        break;
      }
      setState(45);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(46);
    match(SparkyRPKParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Data_labelContext ------------------------------------------------------------------

SparkyRPKParser::Data_labelContext::Data_labelContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::W1_LA() {
  return getToken(SparkyRPKParser::W1_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::W2_LA() {
  return getToken(SparkyRPKParser::W2_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::RETURN_LA() {
  return getToken(SparkyRPKParser::RETURN_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Assignment() {
  return getToken(SparkyRPKParser::Assignment, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Assignment_2d_ex() {
  return getToken(SparkyRPKParser::Assignment_2d_ex, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Assignment_3d_ex() {
  return getToken(SparkyRPKParser::Assignment_3d_ex, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Assignment_4d_ex() {
  return getToken(SparkyRPKParser::Assignment_4d_ex, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::W3_LA() {
  return getToken(SparkyRPKParser::W3_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::W4_LA() {
  return getToken(SparkyRPKParser::W4_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::W1_Hz_LA() {
  return getToken(SparkyRPKParser::W1_Hz_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::W2_Hz_LA() {
  return getToken(SparkyRPKParser::W2_Hz_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::W3_Hz_LA() {
  return getToken(SparkyRPKParser::W3_Hz_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::W4_Hz_LA() {
  return getToken(SparkyRPKParser::W4_Hz_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Dev_w1_LA() {
  return getToken(SparkyRPKParser::Dev_w1_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Dev_w2_LA() {
  return getToken(SparkyRPKParser::Dev_w2_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Dev_w3_LA() {
  return getToken(SparkyRPKParser::Dev_w3_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Dev_w4_LA() {
  return getToken(SparkyRPKParser::Dev_w4_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Volume_LA() {
  return getToken(SparkyRPKParser::Volume_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Dummy_Rms_LA() {
  return getToken(SparkyRPKParser::Dummy_Rms_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Dummy_H_LA() {
  return getToken(SparkyRPKParser::Dummy_H_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Height_LA() {
  return getToken(SparkyRPKParser::Height_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::S_N_LA() {
  return getToken(SparkyRPKParser::S_N_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Lw1_Hz_LA() {
  return getToken(SparkyRPKParser::Lw1_Hz_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Lw2_Hz_LA() {
  return getToken(SparkyRPKParser::Lw2_Hz_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Lw3_Hz_LA() {
  return getToken(SparkyRPKParser::Lw3_Hz_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Lw4_Hz_LA() {
  return getToken(SparkyRPKParser::Lw4_Hz_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Atom1_LA() {
  return getToken(SparkyRPKParser::Atom1_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Atom2_LA() {
  return getToken(SparkyRPKParser::Atom2_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Atom3_LA() {
  return getToken(SparkyRPKParser::Atom3_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Atom4_LA() {
  return getToken(SparkyRPKParser::Atom4_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Distance_LA() {
  return getToken(SparkyRPKParser::Distance_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::Note_LA() {
  return getToken(SparkyRPKParser::Note_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_labelContext::RETURN() {
  return getToken(SparkyRPKParser::RETURN, 0);
}


size_t SparkyRPKParser::Data_labelContext::getRuleIndex() const {
  return SparkyRPKParser::RuleData_label;
}


std::any SparkyRPKParser::Data_labelContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyRPKParserVisitor*>(visitor))
    return parserVisitor->visitData_label(this);
  else
    return visitor->visitChildren(this);
}

SparkyRPKParser::Data_labelContext* SparkyRPKParser::data_label() {
  Data_labelContext *_localctx = _tracker.createInstance<Data_labelContext>(_ctx, getState());
  enterRule(_localctx, 2, SparkyRPKParser::RuleData_label);
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
    setState(48);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 7170) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(49);
    match(SparkyRPKParser::W1_LA);
    setState(50);
    match(SparkyRPKParser::W2_LA);
    setState(52);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::W3_LA) {
      setState(51);
      match(SparkyRPKParser::W3_LA);
    }
    setState(55);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::W4_LA) {
      setState(54);
      match(SparkyRPKParser::W4_LA);
    }
    setState(58);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::W1_Hz_LA) {
      setState(57);
      match(SparkyRPKParser::W1_Hz_LA);
    }
    setState(61);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::W2_Hz_LA) {
      setState(60);
      match(SparkyRPKParser::W2_Hz_LA);
    }
    setState(64);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::W3_Hz_LA) {
      setState(63);
      match(SparkyRPKParser::W3_Hz_LA);
    }
    setState(67);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::W4_Hz_LA) {
      setState(66);
      match(SparkyRPKParser::W4_Hz_LA);
    }
    setState(70);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Dev_w1_LA) {
      setState(69);
      match(SparkyRPKParser::Dev_w1_LA);
    }
    setState(73);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Dev_w2_LA) {
      setState(72);
      match(SparkyRPKParser::Dev_w2_LA);
    }
    setState(76);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Dev_w3_LA) {
      setState(75);
      match(SparkyRPKParser::Dev_w3_LA);
    }
    setState(79);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Dev_w4_LA) {
      setState(78);
      match(SparkyRPKParser::Dev_w4_LA);
    }
    setState(82);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Volume_LA) {
      setState(81);
      match(SparkyRPKParser::Volume_LA);
    }
    setState(85);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Dummy_Rms_LA) {
      setState(84);
      match(SparkyRPKParser::Dummy_Rms_LA);
    }
    setState(88);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Dummy_H_LA) {
      setState(87);
      match(SparkyRPKParser::Dummy_H_LA);
    }
    setState(91);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Height_LA) {
      setState(90);
      match(SparkyRPKParser::Height_LA);
    }
    setState(94);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::S_N_LA) {
      setState(93);
      match(SparkyRPKParser::S_N_LA);
    }
    setState(97);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Lw1_Hz_LA) {
      setState(96);
      match(SparkyRPKParser::Lw1_Hz_LA);
    }
    setState(100);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Lw2_Hz_LA) {
      setState(99);
      match(SparkyRPKParser::Lw2_Hz_LA);
    }
    setState(103);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Lw3_Hz_LA) {
      setState(102);
      match(SparkyRPKParser::Lw3_Hz_LA);
    }
    setState(106);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Lw4_Hz_LA) {
      setState(105);
      match(SparkyRPKParser::Lw4_Hz_LA);
    }
    setState(109);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Atom1_LA) {
      setState(108);
      match(SparkyRPKParser::Atom1_LA);
    }
    setState(112);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Atom2_LA) {
      setState(111);
      match(SparkyRPKParser::Atom2_LA);
    }
    setState(115);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Atom3_LA) {
      setState(114);
      match(SparkyRPKParser::Atom3_LA);
    }
    setState(118);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Atom4_LA) {
      setState(117);
      match(SparkyRPKParser::Atom4_LA);
    }
    setState(121);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Distance_LA) {
      setState(120);
      match(SparkyRPKParser::Distance_LA);
    }
    setState(124);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Note_LA) {
      setState(123);
      match(SparkyRPKParser::Note_LA);
    }
    setState(126);
    match(SparkyRPKParser::RETURN_LA);
    setState(128);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 31, _ctx)) {
    case 1: {
      setState(127);
      match(SparkyRPKParser::RETURN);
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

SparkyRPKParser::Data_label_wo_assignContext::Data_label_wo_assignContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::W1() {
  return getToken(SparkyRPKParser::W1, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::W2_LA() {
  return getToken(SparkyRPKParser::W2_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::RETURN_LA() {
  return getToken(SparkyRPKParser::RETURN_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::W3_LA() {
  return getToken(SparkyRPKParser::W3_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::W4_LA() {
  return getToken(SparkyRPKParser::W4_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::W1_Hz_LA() {
  return getToken(SparkyRPKParser::W1_Hz_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::W2_Hz_LA() {
  return getToken(SparkyRPKParser::W2_Hz_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::W3_Hz_LA() {
  return getToken(SparkyRPKParser::W3_Hz_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::W4_Hz_LA() {
  return getToken(SparkyRPKParser::W4_Hz_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::Dev_w1_LA() {
  return getToken(SparkyRPKParser::Dev_w1_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::Dev_w2_LA() {
  return getToken(SparkyRPKParser::Dev_w2_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::Dev_w3_LA() {
  return getToken(SparkyRPKParser::Dev_w3_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::Dev_w4_LA() {
  return getToken(SparkyRPKParser::Dev_w4_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::Volume_LA() {
  return getToken(SparkyRPKParser::Volume_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::Dummy_Rms_LA() {
  return getToken(SparkyRPKParser::Dummy_Rms_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::Dummy_H_LA() {
  return getToken(SparkyRPKParser::Dummy_H_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::Height_LA() {
  return getToken(SparkyRPKParser::Height_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::S_N_LA() {
  return getToken(SparkyRPKParser::S_N_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::Lw1_Hz_LA() {
  return getToken(SparkyRPKParser::Lw1_Hz_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::Lw2_Hz_LA() {
  return getToken(SparkyRPKParser::Lw2_Hz_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::Lw3_Hz_LA() {
  return getToken(SparkyRPKParser::Lw3_Hz_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::Lw4_Hz_LA() {
  return getToken(SparkyRPKParser::Lw4_Hz_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::Distance_LA() {
  return getToken(SparkyRPKParser::Distance_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::Note_LA() {
  return getToken(SparkyRPKParser::Note_LA, 0);
}

tree::TerminalNode* SparkyRPKParser::Data_label_wo_assignContext::RETURN() {
  return getToken(SparkyRPKParser::RETURN, 0);
}

std::vector<SparkyRPKParser::Peak_wo_assignContext *> SparkyRPKParser::Data_label_wo_assignContext::peak_wo_assign() {
  return getRuleContexts<SparkyRPKParser::Peak_wo_assignContext>();
}

SparkyRPKParser::Peak_wo_assignContext* SparkyRPKParser::Data_label_wo_assignContext::peak_wo_assign(size_t i) {
  return getRuleContext<SparkyRPKParser::Peak_wo_assignContext>(i);
}


size_t SparkyRPKParser::Data_label_wo_assignContext::getRuleIndex() const {
  return SparkyRPKParser::RuleData_label_wo_assign;
}


std::any SparkyRPKParser::Data_label_wo_assignContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyRPKParserVisitor*>(visitor))
    return parserVisitor->visitData_label_wo_assign(this);
  else
    return visitor->visitChildren(this);
}

SparkyRPKParser::Data_label_wo_assignContext* SparkyRPKParser::data_label_wo_assign() {
  Data_label_wo_assignContext *_localctx = _tracker.createInstance<Data_label_wo_assignContext>(_ctx, getState());
  enterRule(_localctx, 4, SparkyRPKParser::RuleData_label_wo_assign);
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
    match(SparkyRPKParser::W1);
    setState(131);
    match(SparkyRPKParser::W2_LA);
    setState(133);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::W3_LA) {
      setState(132);
      match(SparkyRPKParser::W3_LA);
    }
    setState(136);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::W4_LA) {
      setState(135);
      match(SparkyRPKParser::W4_LA);
    }
    setState(139);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::W1_Hz_LA) {
      setState(138);
      match(SparkyRPKParser::W1_Hz_LA);
    }
    setState(142);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::W2_Hz_LA) {
      setState(141);
      match(SparkyRPKParser::W2_Hz_LA);
    }
    setState(145);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::W3_Hz_LA) {
      setState(144);
      match(SparkyRPKParser::W3_Hz_LA);
    }
    setState(148);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::W4_Hz_LA) {
      setState(147);
      match(SparkyRPKParser::W4_Hz_LA);
    }
    setState(151);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Dev_w1_LA) {
      setState(150);
      match(SparkyRPKParser::Dev_w1_LA);
    }
    setState(154);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Dev_w2_LA) {
      setState(153);
      match(SparkyRPKParser::Dev_w2_LA);
    }
    setState(157);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Dev_w3_LA) {
      setState(156);
      match(SparkyRPKParser::Dev_w3_LA);
    }
    setState(160);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Dev_w4_LA) {
      setState(159);
      match(SparkyRPKParser::Dev_w4_LA);
    }
    setState(163);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Volume_LA) {
      setState(162);
      match(SparkyRPKParser::Volume_LA);
    }
    setState(166);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Dummy_Rms_LA) {
      setState(165);
      match(SparkyRPKParser::Dummy_Rms_LA);
    }
    setState(169);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Dummy_H_LA) {
      setState(168);
      match(SparkyRPKParser::Dummy_H_LA);
    }
    setState(172);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Height_LA) {
      setState(171);
      match(SparkyRPKParser::Height_LA);
    }
    setState(175);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::S_N_LA) {
      setState(174);
      match(SparkyRPKParser::S_N_LA);
    }
    setState(178);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Lw1_Hz_LA) {
      setState(177);
      match(SparkyRPKParser::Lw1_Hz_LA);
    }
    setState(181);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Lw2_Hz_LA) {
      setState(180);
      match(SparkyRPKParser::Lw2_Hz_LA);
    }
    setState(184);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Lw3_Hz_LA) {
      setState(183);
      match(SparkyRPKParser::Lw3_Hz_LA);
    }
    setState(187);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Lw4_Hz_LA) {
      setState(186);
      match(SparkyRPKParser::Lw4_Hz_LA);
    }
    setState(190);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Distance_LA) {
      setState(189);
      match(SparkyRPKParser::Distance_LA);
    }
    setState(193);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::Note_LA) {
      setState(192);
      match(SparkyRPKParser::Note_LA);
    }
    setState(195);
    match(SparkyRPKParser::RETURN_LA);
    setState(197);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyRPKParser::RETURN) {
      setState(196);
      match(SparkyRPKParser::RETURN);
    }
    setState(200); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(199);
      peak_wo_assign();
      setState(202); 
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

SparkyRPKParser::Peak_2dContext::Peak_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyRPKParser::Peak_2dContext::Assignment_2d_ex() {
  return getToken(SparkyRPKParser::Assignment_2d_ex, 0);
}

std::vector<SparkyRPKParser::PositionContext *> SparkyRPKParser::Peak_2dContext::position() {
  return getRuleContexts<SparkyRPKParser::PositionContext>();
}

SparkyRPKParser::PositionContext* SparkyRPKParser::Peak_2dContext::position(size_t i) {
  return getRuleContext<SparkyRPKParser::PositionContext>(i);
}

tree::TerminalNode* SparkyRPKParser::Peak_2dContext::RETURN() {
  return getToken(SparkyRPKParser::RETURN, 0);
}

tree::TerminalNode* SparkyRPKParser::Peak_2dContext::EOF() {
  return getToken(SparkyRPKParser::EOF, 0);
}

std::vector<SparkyRPKParser::NumberContext *> SparkyRPKParser::Peak_2dContext::number() {
  return getRuleContexts<SparkyRPKParser::NumberContext>();
}

SparkyRPKParser::NumberContext* SparkyRPKParser::Peak_2dContext::number(size_t i) {
  return getRuleContext<SparkyRPKParser::NumberContext>(i);
}

std::vector<SparkyRPKParser::NoteContext *> SparkyRPKParser::Peak_2dContext::note() {
  return getRuleContexts<SparkyRPKParser::NoteContext>();
}

SparkyRPKParser::NoteContext* SparkyRPKParser::Peak_2dContext::note(size_t i) {
  return getRuleContext<SparkyRPKParser::NoteContext>(i);
}


size_t SparkyRPKParser::Peak_2dContext::getRuleIndex() const {
  return SparkyRPKParser::RulePeak_2d;
}


std::any SparkyRPKParser::Peak_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyRPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_2d(this);
  else
    return visitor->visitChildren(this);
}

SparkyRPKParser::Peak_2dContext* SparkyRPKParser::peak_2d() {
  Peak_2dContext *_localctx = _tracker.createInstance<Peak_2dContext>(_ctx, getState());
  enterRule(_localctx, 6, SparkyRPKParser::RulePeak_2d);
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
    setState(204);
    match(SparkyRPKParser::Assignment_2d_ex);
    setState(205);
    position();
    setState(206);
    position();
    setState(208); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(207);
              number();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(210); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 55, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(215);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 253976) != 0)) {
      setState(212);
      note();
      setState(217);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(218);
    _la = _input->LA(1);
    if (!(_la == SparkyRPKParser::EOF

    || _la == SparkyRPKParser::RETURN)) {
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

SparkyRPKParser::Peak_3dContext::Peak_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyRPKParser::Peak_3dContext::Assignment_3d_ex() {
  return getToken(SparkyRPKParser::Assignment_3d_ex, 0);
}

std::vector<SparkyRPKParser::PositionContext *> SparkyRPKParser::Peak_3dContext::position() {
  return getRuleContexts<SparkyRPKParser::PositionContext>();
}

SparkyRPKParser::PositionContext* SparkyRPKParser::Peak_3dContext::position(size_t i) {
  return getRuleContext<SparkyRPKParser::PositionContext>(i);
}

tree::TerminalNode* SparkyRPKParser::Peak_3dContext::RETURN() {
  return getToken(SparkyRPKParser::RETURN, 0);
}

tree::TerminalNode* SparkyRPKParser::Peak_3dContext::EOF() {
  return getToken(SparkyRPKParser::EOF, 0);
}

std::vector<SparkyRPKParser::NumberContext *> SparkyRPKParser::Peak_3dContext::number() {
  return getRuleContexts<SparkyRPKParser::NumberContext>();
}

SparkyRPKParser::NumberContext* SparkyRPKParser::Peak_3dContext::number(size_t i) {
  return getRuleContext<SparkyRPKParser::NumberContext>(i);
}

std::vector<SparkyRPKParser::NoteContext *> SparkyRPKParser::Peak_3dContext::note() {
  return getRuleContexts<SparkyRPKParser::NoteContext>();
}

SparkyRPKParser::NoteContext* SparkyRPKParser::Peak_3dContext::note(size_t i) {
  return getRuleContext<SparkyRPKParser::NoteContext>(i);
}


size_t SparkyRPKParser::Peak_3dContext::getRuleIndex() const {
  return SparkyRPKParser::RulePeak_3d;
}


std::any SparkyRPKParser::Peak_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyRPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_3d(this);
  else
    return visitor->visitChildren(this);
}

SparkyRPKParser::Peak_3dContext* SparkyRPKParser::peak_3d() {
  Peak_3dContext *_localctx = _tracker.createInstance<Peak_3dContext>(_ctx, getState());
  enterRule(_localctx, 8, SparkyRPKParser::RulePeak_3d);
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
    setState(220);
    match(SparkyRPKParser::Assignment_3d_ex);
    setState(221);
    position();
    setState(222);
    position();
    setState(223);
    position();
    setState(225); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(224);
              number();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(227); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 57, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(232);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 253976) != 0)) {
      setState(229);
      note();
      setState(234);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(235);
    _la = _input->LA(1);
    if (!(_la == SparkyRPKParser::EOF

    || _la == SparkyRPKParser::RETURN)) {
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

SparkyRPKParser::Peak_4dContext::Peak_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyRPKParser::Peak_4dContext::Assignment_4d_ex() {
  return getToken(SparkyRPKParser::Assignment_4d_ex, 0);
}

std::vector<SparkyRPKParser::PositionContext *> SparkyRPKParser::Peak_4dContext::position() {
  return getRuleContexts<SparkyRPKParser::PositionContext>();
}

SparkyRPKParser::PositionContext* SparkyRPKParser::Peak_4dContext::position(size_t i) {
  return getRuleContext<SparkyRPKParser::PositionContext>(i);
}

tree::TerminalNode* SparkyRPKParser::Peak_4dContext::RETURN() {
  return getToken(SparkyRPKParser::RETURN, 0);
}

tree::TerminalNode* SparkyRPKParser::Peak_4dContext::EOF() {
  return getToken(SparkyRPKParser::EOF, 0);
}

std::vector<SparkyRPKParser::NumberContext *> SparkyRPKParser::Peak_4dContext::number() {
  return getRuleContexts<SparkyRPKParser::NumberContext>();
}

SparkyRPKParser::NumberContext* SparkyRPKParser::Peak_4dContext::number(size_t i) {
  return getRuleContext<SparkyRPKParser::NumberContext>(i);
}

std::vector<SparkyRPKParser::NoteContext *> SparkyRPKParser::Peak_4dContext::note() {
  return getRuleContexts<SparkyRPKParser::NoteContext>();
}

SparkyRPKParser::NoteContext* SparkyRPKParser::Peak_4dContext::note(size_t i) {
  return getRuleContext<SparkyRPKParser::NoteContext>(i);
}


size_t SparkyRPKParser::Peak_4dContext::getRuleIndex() const {
  return SparkyRPKParser::RulePeak_4d;
}


std::any SparkyRPKParser::Peak_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyRPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_4d(this);
  else
    return visitor->visitChildren(this);
}

SparkyRPKParser::Peak_4dContext* SparkyRPKParser::peak_4d() {
  Peak_4dContext *_localctx = _tracker.createInstance<Peak_4dContext>(_ctx, getState());
  enterRule(_localctx, 10, SparkyRPKParser::RulePeak_4d);
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
    setState(237);
    match(SparkyRPKParser::Assignment_4d_ex);
    setState(238);
    position();
    setState(239);
    position();
    setState(240);
    position();
    setState(241);
    position();
    setState(243); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(242);
              number();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(245); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 59, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(250);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 253976) != 0)) {
      setState(247);
      note();
      setState(252);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(253);
    _la = _input->LA(1);
    if (!(_la == SparkyRPKParser::EOF

    || _la == SparkyRPKParser::RETURN)) {
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

SparkyRPKParser::Peak_wo_assignContext::Peak_wo_assignContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyRPKParser::Peak_wo_assignContext::RETURN() {
  return getToken(SparkyRPKParser::RETURN, 0);
}

tree::TerminalNode* SparkyRPKParser::Peak_wo_assignContext::EOF() {
  return getToken(SparkyRPKParser::EOF, 0);
}

std::vector<SparkyRPKParser::NumberContext *> SparkyRPKParser::Peak_wo_assignContext::number() {
  return getRuleContexts<SparkyRPKParser::NumberContext>();
}

SparkyRPKParser::NumberContext* SparkyRPKParser::Peak_wo_assignContext::number(size_t i) {
  return getRuleContext<SparkyRPKParser::NumberContext>(i);
}

SparkyRPKParser::NoteContext* SparkyRPKParser::Peak_wo_assignContext::note() {
  return getRuleContext<SparkyRPKParser::NoteContext>(0);
}


size_t SparkyRPKParser::Peak_wo_assignContext::getRuleIndex() const {
  return SparkyRPKParser::RulePeak_wo_assign;
}


std::any SparkyRPKParser::Peak_wo_assignContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyRPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_wo_assign(this);
  else
    return visitor->visitChildren(this);
}

SparkyRPKParser::Peak_wo_assignContext* SparkyRPKParser::peak_wo_assign() {
  Peak_wo_assignContext *_localctx = _tracker.createInstance<Peak_wo_assignContext>(_ctx, getState());
  enterRule(_localctx, 12, SparkyRPKParser::RulePeak_wo_assign);
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
    setState(256); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(255);
              number();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(258); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 61, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
    setState(261);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 253976) != 0)) {
      setState(260);
      note();
    }
    setState(263);
    _la = _input->LA(1);
    if (!(_la == SparkyRPKParser::EOF

    || _la == SparkyRPKParser::RETURN)) {
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

//----------------- PositionContext ------------------------------------------------------------------

SparkyRPKParser::PositionContext::PositionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyRPKParser::PositionContext::Float() {
  return getToken(SparkyRPKParser::Float, 0);
}

tree::TerminalNode* SparkyRPKParser::PositionContext::Integer() {
  return getToken(SparkyRPKParser::Integer, 0);
}


size_t SparkyRPKParser::PositionContext::getRuleIndex() const {
  return SparkyRPKParser::RulePosition;
}


std::any SparkyRPKParser::PositionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyRPKParserVisitor*>(visitor))
    return parserVisitor->visitPosition(this);
  else
    return visitor->visitChildren(this);
}

SparkyRPKParser::PositionContext* SparkyRPKParser::position() {
  PositionContext *_localctx = _tracker.createInstance<PositionContext>(_ctx, getState());
  enterRule(_localctx, 14, SparkyRPKParser::RulePosition);
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
    if (!(_la == SparkyRPKParser::Integer

    || _la == SparkyRPKParser::Float)) {
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

SparkyRPKParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyRPKParser::NumberContext::Real_vol() {
  return getToken(SparkyRPKParser::Real_vol, 0);
}

tree::TerminalNode* SparkyRPKParser::NumberContext::Real() {
  return getToken(SparkyRPKParser::Real, 0);
}

tree::TerminalNode* SparkyRPKParser::NumberContext::Float() {
  return getToken(SparkyRPKParser::Float, 0);
}

tree::TerminalNode* SparkyRPKParser::NumberContext::Integer() {
  return getToken(SparkyRPKParser::Integer, 0);
}


size_t SparkyRPKParser::NumberContext::getRuleIndex() const {
  return SparkyRPKParser::RuleNumber;
}


std::any SparkyRPKParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyRPKParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

SparkyRPKParser::NumberContext* SparkyRPKParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 16, SparkyRPKParser::RuleNumber);
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
    setState(267);
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

SparkyRPKParser::NoteContext::NoteContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyRPKParser::NoteContext::Simple_name() {
  return getToken(SparkyRPKParser::Simple_name, 0);
}

tree::TerminalNode* SparkyRPKParser::NoteContext::Integer() {
  return getToken(SparkyRPKParser::Integer, 0);
}

tree::TerminalNode* SparkyRPKParser::NoteContext::Float() {
  return getToken(SparkyRPKParser::Float, 0);
}

tree::TerminalNode* SparkyRPKParser::NoteContext::Note_2d_ex() {
  return getToken(SparkyRPKParser::Note_2d_ex, 0);
}

tree::TerminalNode* SparkyRPKParser::NoteContext::Note_3d_ex() {
  return getToken(SparkyRPKParser::Note_3d_ex, 0);
}

tree::TerminalNode* SparkyRPKParser::NoteContext::Note_4d_ex() {
  return getToken(SparkyRPKParser::Note_4d_ex, 0);
}

tree::TerminalNode* SparkyRPKParser::NoteContext::Note_ex() {
  return getToken(SparkyRPKParser::Note_ex, 0);
}


size_t SparkyRPKParser::NoteContext::getRuleIndex() const {
  return SparkyRPKParser::RuleNote;
}


std::any SparkyRPKParser::NoteContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyRPKParserVisitor*>(visitor))
    return parserVisitor->visitNote(this);
  else
    return visitor->visitChildren(this);
}

SparkyRPKParser::NoteContext* SparkyRPKParser::note() {
  NoteContext *_localctx = _tracker.createInstance<NoteContext>(_ctx, getState());
  enterRule(_localctx, 18, SparkyRPKParser::RuleNote);
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
    setState(269);
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

void SparkyRPKParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  sparkyrpkparserParserInitialize();
#else
  ::antlr4::internal::call_once(sparkyrpkparserParserOnceFlag, sparkyrpkparserParserInitialize);
#endif
}
