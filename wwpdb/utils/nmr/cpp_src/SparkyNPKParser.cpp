
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/SparkyNPKParser.g4 by ANTLR 4.13.2


#include "SparkyNPKParserVisitor.h"

#include "SparkyNPKParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct SparkyNPKParserStaticData final {
  SparkyNPKParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  SparkyNPKParserStaticData(const SparkyNPKParserStaticData&) = delete;
  SparkyNPKParserStaticData(SparkyNPKParserStaticData&&) = delete;
  SparkyNPKParserStaticData& operator=(const SparkyNPKParserStaticData&) = delete;
  SparkyNPKParserStaticData& operator=(SparkyNPKParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag sparkynpkparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<SparkyNPKParserStaticData> sparkynpkparserParserStaticData = nullptr;

void sparkynpkparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (sparkynpkparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(sparkynpkparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<SparkyNPKParserStaticData>(
    std::vector<std::string>{
      "sparky_npk", "data_label", "peak_2d", "peak_3d", "peak_4d", "peak_2d_po", 
      "peak_3d_po", "peak_4d_po", "position", "number", "note"
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
  	4,1,51,228,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,3,0,24,8,0,1,0,1,0,4,0,28,8,0,11,
  	0,12,0,29,1,0,4,0,33,8,0,11,0,12,0,34,1,0,4,0,38,8,0,11,0,12,0,39,1,0,
  	4,0,43,8,0,11,0,12,0,44,1,0,4,0,48,8,0,11,0,12,0,49,1,0,4,0,53,8,0,11,
  	0,12,0,54,1,0,5,0,58,8,0,10,0,12,0,61,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,
  	69,8,1,1,1,3,1,72,8,1,1,1,3,1,75,8,1,1,1,3,1,78,8,1,1,1,3,1,81,8,1,1,
  	1,3,1,84,8,1,1,1,3,1,87,8,1,1,1,3,1,90,8,1,1,1,3,1,93,8,1,1,1,3,1,96,
  	8,1,1,1,3,1,99,8,1,1,1,1,1,3,1,103,8,1,1,1,3,1,106,8,1,1,1,1,1,3,1,110,
  	8,1,1,1,3,1,113,8,1,1,1,3,1,116,8,1,1,1,3,1,119,8,1,1,1,3,1,122,8,1,1,
  	1,3,1,125,8,1,1,1,3,1,128,8,1,1,1,3,1,131,8,1,1,1,3,1,134,8,1,1,1,3,1,
  	137,8,1,1,1,3,1,140,8,1,1,1,3,1,143,8,1,1,1,3,1,146,8,1,1,1,1,1,3,1,150,
  	8,1,1,2,1,2,1,2,1,2,5,2,156,8,2,10,2,12,2,159,9,2,1,2,5,2,162,8,2,10,
  	2,12,2,165,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,5,3,174,8,3,10,3,12,3,177,
  	9,3,1,3,5,3,180,8,3,10,3,12,3,183,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,5,4,
  	192,8,4,10,4,12,4,195,9,4,1,4,5,4,198,8,4,10,4,12,4,201,9,4,1,4,1,4,1,
  	5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,
  	1,8,1,9,1,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,7,2,0,
  	1,1,10,12,1,1,19,19,1,0,10,12,1,0,11,12,1,0,3,4,1,0,3,6,2,0,3,4,13,17,
  	266,0,23,1,0,0,0,2,64,1,0,0,0,4,151,1,0,0,0,6,168,1,0,0,0,8,186,1,0,0,
  	0,10,204,1,0,0,0,12,209,1,0,0,0,14,215,1,0,0,0,16,221,1,0,0,0,18,223,
  	1,0,0,0,20,225,1,0,0,0,22,24,5,19,0,0,23,22,1,0,0,0,23,24,1,0,0,0,24,
  	59,1,0,0,0,25,58,3,2,1,0,26,28,3,10,5,0,27,26,1,0,0,0,28,29,1,0,0,0,29,
  	27,1,0,0,0,29,30,1,0,0,0,30,58,1,0,0,0,31,33,3,12,6,0,32,31,1,0,0,0,33,
  	34,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,58,1,0,0,0,36,38,3,14,7,0,37,
  	36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,58,1,0,0,0,41,
  	43,3,4,2,0,42,41,1,0,0,0,43,44,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,
  	58,1,0,0,0,46,48,3,6,3,0,47,46,1,0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,
  	50,1,0,0,0,50,58,1,0,0,0,51,53,3,8,4,0,52,51,1,0,0,0,53,54,1,0,0,0,54,
  	52,1,0,0,0,54,55,1,0,0,0,55,58,1,0,0,0,56,58,5,19,0,0,57,25,1,0,0,0,57,
  	27,1,0,0,0,57,32,1,0,0,0,57,37,1,0,0,0,57,42,1,0,0,0,57,47,1,0,0,0,57,
  	52,1,0,0,0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,
  	62,1,0,0,0,61,59,1,0,0,0,62,63,5,0,0,1,63,1,1,0,0,0,64,65,7,0,0,0,65,
  	66,5,31,0,0,66,68,5,32,0,0,67,69,5,33,0,0,68,67,1,0,0,0,68,69,1,0,0,0,
  	69,71,1,0,0,0,70,72,5,34,0,0,71,70,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,
  	0,73,75,5,23,0,0,74,73,1,0,0,0,74,75,1,0,0,0,75,77,1,0,0,0,76,78,5,24,
  	0,0,77,76,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,81,5,25,0,0,80,79,1,
  	0,0,0,80,81,1,0,0,0,81,83,1,0,0,0,82,84,5,26,0,0,83,82,1,0,0,0,83,84,
  	1,0,0,0,84,86,1,0,0,0,85,87,5,35,0,0,86,85,1,0,0,0,86,87,1,0,0,0,87,89,
  	1,0,0,0,88,90,5,36,0,0,89,88,1,0,0,0,89,90,1,0,0,0,90,92,1,0,0,0,91,93,
  	5,37,0,0,92,91,1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,96,5,38,0,0,95,
  	94,1,0,0,0,95,96,1,0,0,0,96,102,1,0,0,0,97,99,5,39,0,0,98,97,1,0,0,0,
  	98,99,1,0,0,0,99,100,1,0,0,0,100,103,5,40,0,0,101,103,5,41,0,0,102,98,
  	1,0,0,0,102,101,1,0,0,0,102,103,1,0,0,0,103,109,1,0,0,0,104,106,5,39,
  	0,0,105,104,1,0,0,0,105,106,1,0,0,0,106,107,1,0,0,0,107,110,5,40,0,0,
  	108,110,5,41,0,0,109,105,1,0,0,0,109,108,1,0,0,0,109,110,1,0,0,0,110,
  	112,1,0,0,0,111,113,5,42,0,0,112,111,1,0,0,0,112,113,1,0,0,0,113,115,
  	1,0,0,0,114,116,5,43,0,0,115,114,1,0,0,0,115,116,1,0,0,0,116,118,1,0,
  	0,0,117,119,5,27,0,0,118,117,1,0,0,0,118,119,1,0,0,0,119,121,1,0,0,0,
  	120,122,5,28,0,0,121,120,1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,
  	125,5,29,0,0,124,123,1,0,0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,128,
  	5,30,0,0,127,126,1,0,0,0,127,128,1,0,0,0,128,130,1,0,0,0,129,131,5,44,
  	0,0,130,129,1,0,0,0,130,131,1,0,0,0,131,133,1,0,0,0,132,134,5,45,0,0,
  	133,132,1,0,0,0,133,134,1,0,0,0,134,136,1,0,0,0,135,137,5,46,0,0,136,
  	135,1,0,0,0,136,137,1,0,0,0,137,139,1,0,0,0,138,140,5,47,0,0,139,138,
  	1,0,0,0,139,140,1,0,0,0,140,142,1,0,0,0,141,143,5,48,0,0,142,141,1,0,
  	0,0,142,143,1,0,0,0,143,145,1,0,0,0,144,146,5,49,0,0,145,144,1,0,0,0,
  	145,146,1,0,0,0,146,147,1,0,0,0,147,149,5,51,0,0,148,150,5,19,0,0,149,
  	148,1,0,0,0,149,150,1,0,0,0,150,3,1,0,0,0,151,152,5,10,0,0,152,153,3,
  	16,8,0,153,157,3,16,8,0,154,156,3,18,9,0,155,154,1,0,0,0,156,159,1,0,
  	0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,163,1,0,0,0,159,157,1,0,0,0,160,
  	162,3,20,10,0,161,160,1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,164,
  	1,0,0,0,164,166,1,0,0,0,165,163,1,0,0,0,166,167,7,1,0,0,167,5,1,0,0,0,
  	168,169,5,11,0,0,169,170,3,16,8,0,170,171,3,16,8,0,171,175,3,16,8,0,172,
  	174,3,18,9,0,173,172,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,176,
  	1,0,0,0,176,181,1,0,0,0,177,175,1,0,0,0,178,180,3,20,10,0,179,178,1,0,
  	0,0,180,183,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,184,1,0,0,0,183,
  	181,1,0,0,0,184,185,7,1,0,0,185,7,1,0,0,0,186,187,5,12,0,0,187,188,3,
  	16,8,0,188,189,3,16,8,0,189,193,3,16,8,0,190,192,3,18,9,0,191,190,1,0,
  	0,0,192,195,1,0,0,0,193,191,1,0,0,0,193,194,1,0,0,0,194,199,1,0,0,0,195,
  	193,1,0,0,0,196,198,3,20,10,0,197,196,1,0,0,0,198,201,1,0,0,0,199,197,
  	1,0,0,0,199,200,1,0,0,0,200,202,1,0,0,0,201,199,1,0,0,0,202,203,7,1,0,
  	0,203,9,1,0,0,0,204,205,7,2,0,0,205,206,3,16,8,0,206,207,3,16,8,0,207,
  	208,7,1,0,0,208,11,1,0,0,0,209,210,7,3,0,0,210,211,3,16,8,0,211,212,3,
  	16,8,0,212,213,3,16,8,0,213,214,7,1,0,0,214,13,1,0,0,0,215,216,5,12,0,
  	0,216,217,3,16,8,0,217,218,3,16,8,0,218,219,3,16,8,0,219,220,7,1,0,0,
  	220,15,1,0,0,0,221,222,7,4,0,0,222,17,1,0,0,0,223,224,7,5,0,0,224,19,
  	1,0,0,0,225,226,7,6,0,0,226,21,1,0,0,0,42,23,29,34,39,44,49,54,57,59,
  	68,71,74,77,80,83,86,89,92,95,98,102,105,109,112,115,118,121,124,127,
  	130,133,136,139,142,145,149,157,163,175,181,193,199
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  sparkynpkparserParserStaticData = std::move(staticData);
}

}

SparkyNPKParser::SparkyNPKParser(TokenStream *input) : SparkyNPKParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

SparkyNPKParser::SparkyNPKParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  SparkyNPKParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *sparkynpkparserParserStaticData->atn, sparkynpkparserParserStaticData->decisionToDFA, sparkynpkparserParserStaticData->sharedContextCache, options);
}

SparkyNPKParser::~SparkyNPKParser() {
  delete _interpreter;
}

const atn::ATN& SparkyNPKParser::getATN() const {
  return *sparkynpkparserParserStaticData->atn;
}

std::string SparkyNPKParser::getGrammarFileName() const {
  return "SparkyNPKParser.g4";
}

const std::vector<std::string>& SparkyNPKParser::getRuleNames() const {
  return sparkynpkparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& SparkyNPKParser::getVocabulary() const {
  return sparkynpkparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView SparkyNPKParser::getSerializedATN() const {
  return sparkynpkparserParserStaticData->serializedATN;
}


//----------------- Sparky_npkContext ------------------------------------------------------------------

SparkyNPKParser::Sparky_npkContext::Sparky_npkContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyNPKParser::Sparky_npkContext::EOF() {
  return getToken(SparkyNPKParser::EOF, 0);
}

std::vector<tree::TerminalNode *> SparkyNPKParser::Sparky_npkContext::RETURN() {
  return getTokens(SparkyNPKParser::RETURN);
}

tree::TerminalNode* SparkyNPKParser::Sparky_npkContext::RETURN(size_t i) {
  return getToken(SparkyNPKParser::RETURN, i);
}

std::vector<SparkyNPKParser::Data_labelContext *> SparkyNPKParser::Sparky_npkContext::data_label() {
  return getRuleContexts<SparkyNPKParser::Data_labelContext>();
}

SparkyNPKParser::Data_labelContext* SparkyNPKParser::Sparky_npkContext::data_label(size_t i) {
  return getRuleContext<SparkyNPKParser::Data_labelContext>(i);
}

std::vector<SparkyNPKParser::Peak_2d_poContext *> SparkyNPKParser::Sparky_npkContext::peak_2d_po() {
  return getRuleContexts<SparkyNPKParser::Peak_2d_poContext>();
}

SparkyNPKParser::Peak_2d_poContext* SparkyNPKParser::Sparky_npkContext::peak_2d_po(size_t i) {
  return getRuleContext<SparkyNPKParser::Peak_2d_poContext>(i);
}

std::vector<SparkyNPKParser::Peak_3d_poContext *> SparkyNPKParser::Sparky_npkContext::peak_3d_po() {
  return getRuleContexts<SparkyNPKParser::Peak_3d_poContext>();
}

SparkyNPKParser::Peak_3d_poContext* SparkyNPKParser::Sparky_npkContext::peak_3d_po(size_t i) {
  return getRuleContext<SparkyNPKParser::Peak_3d_poContext>(i);
}

std::vector<SparkyNPKParser::Peak_4d_poContext *> SparkyNPKParser::Sparky_npkContext::peak_4d_po() {
  return getRuleContexts<SparkyNPKParser::Peak_4d_poContext>();
}

SparkyNPKParser::Peak_4d_poContext* SparkyNPKParser::Sparky_npkContext::peak_4d_po(size_t i) {
  return getRuleContext<SparkyNPKParser::Peak_4d_poContext>(i);
}

std::vector<SparkyNPKParser::Peak_2dContext *> SparkyNPKParser::Sparky_npkContext::peak_2d() {
  return getRuleContexts<SparkyNPKParser::Peak_2dContext>();
}

SparkyNPKParser::Peak_2dContext* SparkyNPKParser::Sparky_npkContext::peak_2d(size_t i) {
  return getRuleContext<SparkyNPKParser::Peak_2dContext>(i);
}

std::vector<SparkyNPKParser::Peak_3dContext *> SparkyNPKParser::Sparky_npkContext::peak_3d() {
  return getRuleContexts<SparkyNPKParser::Peak_3dContext>();
}

SparkyNPKParser::Peak_3dContext* SparkyNPKParser::Sparky_npkContext::peak_3d(size_t i) {
  return getRuleContext<SparkyNPKParser::Peak_3dContext>(i);
}

std::vector<SparkyNPKParser::Peak_4dContext *> SparkyNPKParser::Sparky_npkContext::peak_4d() {
  return getRuleContexts<SparkyNPKParser::Peak_4dContext>();
}

SparkyNPKParser::Peak_4dContext* SparkyNPKParser::Sparky_npkContext::peak_4d(size_t i) {
  return getRuleContext<SparkyNPKParser::Peak_4dContext>(i);
}


size_t SparkyNPKParser::Sparky_npkContext::getRuleIndex() const {
  return SparkyNPKParser::RuleSparky_npk;
}


std::any SparkyNPKParser::Sparky_npkContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyNPKParserVisitor*>(visitor))
    return parserVisitor->visitSparky_npk(this);
  else
    return visitor->visitChildren(this);
}

SparkyNPKParser::Sparky_npkContext* SparkyNPKParser::sparky_npk() {
  Sparky_npkContext *_localctx = _tracker.createInstance<Sparky_npkContext>(_ctx, getState());
  enterRule(_localctx, 0, SparkyNPKParser::RuleSparky_npk);
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
    setState(23);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
    case 1: {
      setState(22);
      match(SparkyNPKParser::RETURN);
      break;
    }

    default:
      break;
    }
    setState(59);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 531458) != 0)) {
      setState(57);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 7, _ctx)) {
      case 1: {
        setState(25);
        data_label();
        break;
      }

      case 2: {
        setState(27); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(26);
                  peak_2d_po();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(29); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 3: {
        setState(32); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(31);
                  peak_3d_po();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(34); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 2, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 4: {
        setState(37); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(36);
                  peak_4d_po();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(39); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 3, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 5: {
        setState(42); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(41);
                  peak_2d();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(44); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 4, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 6: {
        setState(47); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(46);
                  peak_3d();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(49); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 5, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 7: {
        setState(52); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(51);
                  peak_4d();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(54); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 6, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 8: {
        setState(56);
        match(SparkyNPKParser::RETURN);
        break;
      }

      default:
        break;
      }
      setState(61);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(62);
    match(SparkyNPKParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Data_labelContext ------------------------------------------------------------------

SparkyNPKParser::Data_labelContext::Data_labelContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::W1_LA() {
  return getToken(SparkyNPKParser::W1_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::W2_LA() {
  return getToken(SparkyNPKParser::W2_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::RETURN_LA() {
  return getToken(SparkyNPKParser::RETURN_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Assignment() {
  return getToken(SparkyNPKParser::Assignment, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Assignment_2d_ex() {
  return getToken(SparkyNPKParser::Assignment_2d_ex, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Assignment_3d_ex() {
  return getToken(SparkyNPKParser::Assignment_3d_ex, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Assignment_4d_ex() {
  return getToken(SparkyNPKParser::Assignment_4d_ex, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::W3_LA() {
  return getToken(SparkyNPKParser::W3_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::W4_LA() {
  return getToken(SparkyNPKParser::W4_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::W1_Hz_LA() {
  return getToken(SparkyNPKParser::W1_Hz_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::W2_Hz_LA() {
  return getToken(SparkyNPKParser::W2_Hz_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::W3_Hz_LA() {
  return getToken(SparkyNPKParser::W3_Hz_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::W4_Hz_LA() {
  return getToken(SparkyNPKParser::W4_Hz_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Dev_w1_LA() {
  return getToken(SparkyNPKParser::Dev_w1_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Dev_w2_LA() {
  return getToken(SparkyNPKParser::Dev_w2_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Dev_w3_LA() {
  return getToken(SparkyNPKParser::Dev_w3_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Dev_w4_LA() {
  return getToken(SparkyNPKParser::Dev_w4_LA, 0);
}

std::vector<tree::TerminalNode *> SparkyNPKParser::Data_labelContext::Height_LA() {
  return getTokens(SparkyNPKParser::Height_LA);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Height_LA(size_t i) {
  return getToken(SparkyNPKParser::Height_LA, i);
}

std::vector<tree::TerminalNode *> SparkyNPKParser::Data_labelContext::Volume_LA() {
  return getTokens(SparkyNPKParser::Volume_LA);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Volume_LA(size_t i) {
  return getToken(SparkyNPKParser::Volume_LA, i);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Dummy_Rms_LA() {
  return getToken(SparkyNPKParser::Dummy_Rms_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::S_N_LA() {
  return getToken(SparkyNPKParser::S_N_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Lw1_Hz_LA() {
  return getToken(SparkyNPKParser::Lw1_Hz_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Lw2_Hz_LA() {
  return getToken(SparkyNPKParser::Lw2_Hz_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Lw3_Hz_LA() {
  return getToken(SparkyNPKParser::Lw3_Hz_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Lw4_Hz_LA() {
  return getToken(SparkyNPKParser::Lw4_Hz_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Atom1_LA() {
  return getToken(SparkyNPKParser::Atom1_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Atom2_LA() {
  return getToken(SparkyNPKParser::Atom2_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Atom3_LA() {
  return getToken(SparkyNPKParser::Atom3_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Atom4_LA() {
  return getToken(SparkyNPKParser::Atom4_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Distance_LA() {
  return getToken(SparkyNPKParser::Distance_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Note_LA() {
  return getToken(SparkyNPKParser::Note_LA, 0);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::RETURN() {
  return getToken(SparkyNPKParser::RETURN, 0);
}

std::vector<tree::TerminalNode *> SparkyNPKParser::Data_labelContext::Dummy_H_LA() {
  return getTokens(SparkyNPKParser::Dummy_H_LA);
}

tree::TerminalNode* SparkyNPKParser::Data_labelContext::Dummy_H_LA(size_t i) {
  return getToken(SparkyNPKParser::Dummy_H_LA, i);
}


size_t SparkyNPKParser::Data_labelContext::getRuleIndex() const {
  return SparkyNPKParser::RuleData_label;
}


std::any SparkyNPKParser::Data_labelContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyNPKParserVisitor*>(visitor))
    return parserVisitor->visitData_label(this);
  else
    return visitor->visitChildren(this);
}

SparkyNPKParser::Data_labelContext* SparkyNPKParser::data_label() {
  Data_labelContext *_localctx = _tracker.createInstance<Data_labelContext>(_ctx, getState());
  enterRule(_localctx, 2, SparkyNPKParser::RuleData_label);
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
    setState(64);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 7170) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(65);
    match(SparkyNPKParser::W1_LA);
    setState(66);
    match(SparkyNPKParser::W2_LA);
    setState(68);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::W3_LA) {
      setState(67);
      match(SparkyNPKParser::W3_LA);
    }
    setState(71);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::W4_LA) {
      setState(70);
      match(SparkyNPKParser::W4_LA);
    }
    setState(74);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::W1_Hz_LA) {
      setState(73);
      match(SparkyNPKParser::W1_Hz_LA);
    }
    setState(77);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::W2_Hz_LA) {
      setState(76);
      match(SparkyNPKParser::W2_Hz_LA);
    }
    setState(80);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::W3_Hz_LA) {
      setState(79);
      match(SparkyNPKParser::W3_Hz_LA);
    }
    setState(83);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::W4_Hz_LA) {
      setState(82);
      match(SparkyNPKParser::W4_Hz_LA);
    }
    setState(86);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Dev_w1_LA) {
      setState(85);
      match(SparkyNPKParser::Dev_w1_LA);
    }
    setState(89);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Dev_w2_LA) {
      setState(88);
      match(SparkyNPKParser::Dev_w2_LA);
    }
    setState(92);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Dev_w3_LA) {
      setState(91);
      match(SparkyNPKParser::Dev_w3_LA);
    }
    setState(95);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Dev_w4_LA) {
      setState(94);
      match(SparkyNPKParser::Dev_w4_LA);
    }
    setState(102);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 20, _ctx)) {
    case 1: {
      setState(98);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == SparkyNPKParser::Dummy_H_LA) {
        setState(97);
        match(SparkyNPKParser::Dummy_H_LA);
      }
      setState(100);
      match(SparkyNPKParser::Height_LA);
      break;
    }

    case 2: {
      setState(101);
      match(SparkyNPKParser::Volume_LA);
      break;
    }

    default:
      break;
    }
    setState(109);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case SparkyNPKParser::Dummy_H_LA:
      case SparkyNPKParser::Height_LA: {
        setState(105);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == SparkyNPKParser::Dummy_H_LA) {
          setState(104);
          match(SparkyNPKParser::Dummy_H_LA);
        }
        setState(107);
        match(SparkyNPKParser::Height_LA);
        break;
      }

      case SparkyNPKParser::Volume_LA: {
        setState(108);
        match(SparkyNPKParser::Volume_LA);
        break;
      }

      case SparkyNPKParser::Lw1_Hz_LA:
      case SparkyNPKParser::Lw2_Hz_LA:
      case SparkyNPKParser::Lw3_Hz_LA:
      case SparkyNPKParser::Lw4_Hz_LA:
      case SparkyNPKParser::Dummy_Rms_LA:
      case SparkyNPKParser::S_N_LA:
      case SparkyNPKParser::Atom1_LA:
      case SparkyNPKParser::Atom2_LA:
      case SparkyNPKParser::Atom3_LA:
      case SparkyNPKParser::Atom4_LA:
      case SparkyNPKParser::Distance_LA:
      case SparkyNPKParser::Note_LA:
      case SparkyNPKParser::RETURN_LA: {
        break;
      }

    default:
      break;
    }
    setState(112);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Dummy_Rms_LA) {
      setState(111);
      match(SparkyNPKParser::Dummy_Rms_LA);
    }
    setState(115);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::S_N_LA) {
      setState(114);
      match(SparkyNPKParser::S_N_LA);
    }
    setState(118);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Lw1_Hz_LA) {
      setState(117);
      match(SparkyNPKParser::Lw1_Hz_LA);
    }
    setState(121);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Lw2_Hz_LA) {
      setState(120);
      match(SparkyNPKParser::Lw2_Hz_LA);
    }
    setState(124);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Lw3_Hz_LA) {
      setState(123);
      match(SparkyNPKParser::Lw3_Hz_LA);
    }
    setState(127);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Lw4_Hz_LA) {
      setState(126);
      match(SparkyNPKParser::Lw4_Hz_LA);
    }
    setState(130);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Atom1_LA) {
      setState(129);
      match(SparkyNPKParser::Atom1_LA);
    }
    setState(133);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Atom2_LA) {
      setState(132);
      match(SparkyNPKParser::Atom2_LA);
    }
    setState(136);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Atom3_LA) {
      setState(135);
      match(SparkyNPKParser::Atom3_LA);
    }
    setState(139);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Atom4_LA) {
      setState(138);
      match(SparkyNPKParser::Atom4_LA);
    }
    setState(142);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Distance_LA) {
      setState(141);
      match(SparkyNPKParser::Distance_LA);
    }
    setState(145);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Note_LA) {
      setState(144);
      match(SparkyNPKParser::Note_LA);
    }
    setState(147);
    match(SparkyNPKParser::RETURN_LA);
    setState(149);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 35, _ctx)) {
    case 1: {
      setState(148);
      match(SparkyNPKParser::RETURN);
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

//----------------- Peak_2dContext ------------------------------------------------------------------

SparkyNPKParser::Peak_2dContext::Peak_2dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyNPKParser::Peak_2dContext::Assignment_2d_ex() {
  return getToken(SparkyNPKParser::Assignment_2d_ex, 0);
}

std::vector<SparkyNPKParser::PositionContext *> SparkyNPKParser::Peak_2dContext::position() {
  return getRuleContexts<SparkyNPKParser::PositionContext>();
}

SparkyNPKParser::PositionContext* SparkyNPKParser::Peak_2dContext::position(size_t i) {
  return getRuleContext<SparkyNPKParser::PositionContext>(i);
}

tree::TerminalNode* SparkyNPKParser::Peak_2dContext::RETURN() {
  return getToken(SparkyNPKParser::RETURN, 0);
}

tree::TerminalNode* SparkyNPKParser::Peak_2dContext::EOF() {
  return getToken(SparkyNPKParser::EOF, 0);
}

std::vector<SparkyNPKParser::NumberContext *> SparkyNPKParser::Peak_2dContext::number() {
  return getRuleContexts<SparkyNPKParser::NumberContext>();
}

SparkyNPKParser::NumberContext* SparkyNPKParser::Peak_2dContext::number(size_t i) {
  return getRuleContext<SparkyNPKParser::NumberContext>(i);
}

std::vector<SparkyNPKParser::NoteContext *> SparkyNPKParser::Peak_2dContext::note() {
  return getRuleContexts<SparkyNPKParser::NoteContext>();
}

SparkyNPKParser::NoteContext* SparkyNPKParser::Peak_2dContext::note(size_t i) {
  return getRuleContext<SparkyNPKParser::NoteContext>(i);
}


size_t SparkyNPKParser::Peak_2dContext::getRuleIndex() const {
  return SparkyNPKParser::RulePeak_2d;
}


std::any SparkyNPKParser::Peak_2dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyNPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_2d(this);
  else
    return visitor->visitChildren(this);
}

SparkyNPKParser::Peak_2dContext* SparkyNPKParser::peak_2d() {
  Peak_2dContext *_localctx = _tracker.createInstance<Peak_2dContext>(_ctx, getState());
  enterRule(_localctx, 4, SparkyNPKParser::RulePeak_2d);
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
    setState(151);
    match(SparkyNPKParser::Assignment_2d_ex);
    setState(152);
    position();
    setState(153);
    position();
    setState(157);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 36, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(154);
        number(); 
      }
      setState(159);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 36, _ctx);
    }
    setState(163);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 253976) != 0)) {
      setState(160);
      note();
      setState(165);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(166);
    _la = _input->LA(1);
    if (!(_la == SparkyNPKParser::EOF

    || _la == SparkyNPKParser::RETURN)) {
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

SparkyNPKParser::Peak_3dContext::Peak_3dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyNPKParser::Peak_3dContext::Assignment_3d_ex() {
  return getToken(SparkyNPKParser::Assignment_3d_ex, 0);
}

std::vector<SparkyNPKParser::PositionContext *> SparkyNPKParser::Peak_3dContext::position() {
  return getRuleContexts<SparkyNPKParser::PositionContext>();
}

SparkyNPKParser::PositionContext* SparkyNPKParser::Peak_3dContext::position(size_t i) {
  return getRuleContext<SparkyNPKParser::PositionContext>(i);
}

tree::TerminalNode* SparkyNPKParser::Peak_3dContext::RETURN() {
  return getToken(SparkyNPKParser::RETURN, 0);
}

tree::TerminalNode* SparkyNPKParser::Peak_3dContext::EOF() {
  return getToken(SparkyNPKParser::EOF, 0);
}

std::vector<SparkyNPKParser::NumberContext *> SparkyNPKParser::Peak_3dContext::number() {
  return getRuleContexts<SparkyNPKParser::NumberContext>();
}

SparkyNPKParser::NumberContext* SparkyNPKParser::Peak_3dContext::number(size_t i) {
  return getRuleContext<SparkyNPKParser::NumberContext>(i);
}

std::vector<SparkyNPKParser::NoteContext *> SparkyNPKParser::Peak_3dContext::note() {
  return getRuleContexts<SparkyNPKParser::NoteContext>();
}

SparkyNPKParser::NoteContext* SparkyNPKParser::Peak_3dContext::note(size_t i) {
  return getRuleContext<SparkyNPKParser::NoteContext>(i);
}


size_t SparkyNPKParser::Peak_3dContext::getRuleIndex() const {
  return SparkyNPKParser::RulePeak_3d;
}


std::any SparkyNPKParser::Peak_3dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyNPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_3d(this);
  else
    return visitor->visitChildren(this);
}

SparkyNPKParser::Peak_3dContext* SparkyNPKParser::peak_3d() {
  Peak_3dContext *_localctx = _tracker.createInstance<Peak_3dContext>(_ctx, getState());
  enterRule(_localctx, 6, SparkyNPKParser::RulePeak_3d);
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
    setState(168);
    match(SparkyNPKParser::Assignment_3d_ex);
    setState(169);
    position();
    setState(170);
    position();
    setState(171);
    position();
    setState(175);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 38, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(172);
        number(); 
      }
      setState(177);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 38, _ctx);
    }
    setState(181);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 253976) != 0)) {
      setState(178);
      note();
      setState(183);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(184);
    _la = _input->LA(1);
    if (!(_la == SparkyNPKParser::EOF

    || _la == SparkyNPKParser::RETURN)) {
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

SparkyNPKParser::Peak_4dContext::Peak_4dContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyNPKParser::Peak_4dContext::Assignment_4d_ex() {
  return getToken(SparkyNPKParser::Assignment_4d_ex, 0);
}

std::vector<SparkyNPKParser::PositionContext *> SparkyNPKParser::Peak_4dContext::position() {
  return getRuleContexts<SparkyNPKParser::PositionContext>();
}

SparkyNPKParser::PositionContext* SparkyNPKParser::Peak_4dContext::position(size_t i) {
  return getRuleContext<SparkyNPKParser::PositionContext>(i);
}

tree::TerminalNode* SparkyNPKParser::Peak_4dContext::RETURN() {
  return getToken(SparkyNPKParser::RETURN, 0);
}

tree::TerminalNode* SparkyNPKParser::Peak_4dContext::EOF() {
  return getToken(SparkyNPKParser::EOF, 0);
}

std::vector<SparkyNPKParser::NumberContext *> SparkyNPKParser::Peak_4dContext::number() {
  return getRuleContexts<SparkyNPKParser::NumberContext>();
}

SparkyNPKParser::NumberContext* SparkyNPKParser::Peak_4dContext::number(size_t i) {
  return getRuleContext<SparkyNPKParser::NumberContext>(i);
}

std::vector<SparkyNPKParser::NoteContext *> SparkyNPKParser::Peak_4dContext::note() {
  return getRuleContexts<SparkyNPKParser::NoteContext>();
}

SparkyNPKParser::NoteContext* SparkyNPKParser::Peak_4dContext::note(size_t i) {
  return getRuleContext<SparkyNPKParser::NoteContext>(i);
}


size_t SparkyNPKParser::Peak_4dContext::getRuleIndex() const {
  return SparkyNPKParser::RulePeak_4d;
}


std::any SparkyNPKParser::Peak_4dContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyNPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_4d(this);
  else
    return visitor->visitChildren(this);
}

SparkyNPKParser::Peak_4dContext* SparkyNPKParser::peak_4d() {
  Peak_4dContext *_localctx = _tracker.createInstance<Peak_4dContext>(_ctx, getState());
  enterRule(_localctx, 8, SparkyNPKParser::RulePeak_4d);
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
    setState(186);
    match(SparkyNPKParser::Assignment_4d_ex);
    setState(187);
    position();
    setState(188);
    position();
    setState(189);
    position();
    setState(193);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 40, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(190);
        number(); 
      }
      setState(195);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 40, _ctx);
    }
    setState(199);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 253976) != 0)) {
      setState(196);
      note();
      setState(201);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(202);
    _la = _input->LA(1);
    if (!(_la == SparkyNPKParser::EOF

    || _la == SparkyNPKParser::RETURN)) {
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

//----------------- Peak_2d_poContext ------------------------------------------------------------------

SparkyNPKParser::Peak_2d_poContext::Peak_2d_poContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<SparkyNPKParser::PositionContext *> SparkyNPKParser::Peak_2d_poContext::position() {
  return getRuleContexts<SparkyNPKParser::PositionContext>();
}

SparkyNPKParser::PositionContext* SparkyNPKParser::Peak_2d_poContext::position(size_t i) {
  return getRuleContext<SparkyNPKParser::PositionContext>(i);
}

tree::TerminalNode* SparkyNPKParser::Peak_2d_poContext::Assignment_2d_ex() {
  return getToken(SparkyNPKParser::Assignment_2d_ex, 0);
}

tree::TerminalNode* SparkyNPKParser::Peak_2d_poContext::Assignment_3d_ex() {
  return getToken(SparkyNPKParser::Assignment_3d_ex, 0);
}

tree::TerminalNode* SparkyNPKParser::Peak_2d_poContext::Assignment_4d_ex() {
  return getToken(SparkyNPKParser::Assignment_4d_ex, 0);
}

tree::TerminalNode* SparkyNPKParser::Peak_2d_poContext::RETURN() {
  return getToken(SparkyNPKParser::RETURN, 0);
}

tree::TerminalNode* SparkyNPKParser::Peak_2d_poContext::EOF() {
  return getToken(SparkyNPKParser::EOF, 0);
}


size_t SparkyNPKParser::Peak_2d_poContext::getRuleIndex() const {
  return SparkyNPKParser::RulePeak_2d_po;
}


std::any SparkyNPKParser::Peak_2d_poContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyNPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_2d_po(this);
  else
    return visitor->visitChildren(this);
}

SparkyNPKParser::Peak_2d_poContext* SparkyNPKParser::peak_2d_po() {
  Peak_2d_poContext *_localctx = _tracker.createInstance<Peak_2d_poContext>(_ctx, getState());
  enterRule(_localctx, 10, SparkyNPKParser::RulePeak_2d_po);
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
    setState(204);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 7168) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(205);
    position();
    setState(206);
    position();
    setState(207);
    _la = _input->LA(1);
    if (!(_la == SparkyNPKParser::EOF

    || _la == SparkyNPKParser::RETURN)) {
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

//----------------- Peak_3d_poContext ------------------------------------------------------------------

SparkyNPKParser::Peak_3d_poContext::Peak_3d_poContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<SparkyNPKParser::PositionContext *> SparkyNPKParser::Peak_3d_poContext::position() {
  return getRuleContexts<SparkyNPKParser::PositionContext>();
}

SparkyNPKParser::PositionContext* SparkyNPKParser::Peak_3d_poContext::position(size_t i) {
  return getRuleContext<SparkyNPKParser::PositionContext>(i);
}

tree::TerminalNode* SparkyNPKParser::Peak_3d_poContext::Assignment_3d_ex() {
  return getToken(SparkyNPKParser::Assignment_3d_ex, 0);
}

tree::TerminalNode* SparkyNPKParser::Peak_3d_poContext::Assignment_4d_ex() {
  return getToken(SparkyNPKParser::Assignment_4d_ex, 0);
}

tree::TerminalNode* SparkyNPKParser::Peak_3d_poContext::RETURN() {
  return getToken(SparkyNPKParser::RETURN, 0);
}

tree::TerminalNode* SparkyNPKParser::Peak_3d_poContext::EOF() {
  return getToken(SparkyNPKParser::EOF, 0);
}


size_t SparkyNPKParser::Peak_3d_poContext::getRuleIndex() const {
  return SparkyNPKParser::RulePeak_3d_po;
}


std::any SparkyNPKParser::Peak_3d_poContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyNPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_3d_po(this);
  else
    return visitor->visitChildren(this);
}

SparkyNPKParser::Peak_3d_poContext* SparkyNPKParser::peak_3d_po() {
  Peak_3d_poContext *_localctx = _tracker.createInstance<Peak_3d_poContext>(_ctx, getState());
  enterRule(_localctx, 12, SparkyNPKParser::RulePeak_3d_po);
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
    setState(209);
    _la = _input->LA(1);
    if (!(_la == SparkyNPKParser::Assignment_3d_ex

    || _la == SparkyNPKParser::Assignment_4d_ex)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(210);
    position();
    setState(211);
    position();
    setState(212);
    position();
    setState(213);
    _la = _input->LA(1);
    if (!(_la == SparkyNPKParser::EOF

    || _la == SparkyNPKParser::RETURN)) {
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

//----------------- Peak_4d_poContext ------------------------------------------------------------------

SparkyNPKParser::Peak_4d_poContext::Peak_4d_poContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyNPKParser::Peak_4d_poContext::Assignment_4d_ex() {
  return getToken(SparkyNPKParser::Assignment_4d_ex, 0);
}

std::vector<SparkyNPKParser::PositionContext *> SparkyNPKParser::Peak_4d_poContext::position() {
  return getRuleContexts<SparkyNPKParser::PositionContext>();
}

SparkyNPKParser::PositionContext* SparkyNPKParser::Peak_4d_poContext::position(size_t i) {
  return getRuleContext<SparkyNPKParser::PositionContext>(i);
}

tree::TerminalNode* SparkyNPKParser::Peak_4d_poContext::RETURN() {
  return getToken(SparkyNPKParser::RETURN, 0);
}

tree::TerminalNode* SparkyNPKParser::Peak_4d_poContext::EOF() {
  return getToken(SparkyNPKParser::EOF, 0);
}


size_t SparkyNPKParser::Peak_4d_poContext::getRuleIndex() const {
  return SparkyNPKParser::RulePeak_4d_po;
}


std::any SparkyNPKParser::Peak_4d_poContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyNPKParserVisitor*>(visitor))
    return parserVisitor->visitPeak_4d_po(this);
  else
    return visitor->visitChildren(this);
}

SparkyNPKParser::Peak_4d_poContext* SparkyNPKParser::peak_4d_po() {
  Peak_4d_poContext *_localctx = _tracker.createInstance<Peak_4d_poContext>(_ctx, getState());
  enterRule(_localctx, 14, SparkyNPKParser::RulePeak_4d_po);
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
    setState(215);
    match(SparkyNPKParser::Assignment_4d_ex);
    setState(216);
    position();
    setState(217);
    position();
    setState(218);
    position();
    setState(219);
    _la = _input->LA(1);
    if (!(_la == SparkyNPKParser::EOF

    || _la == SparkyNPKParser::RETURN)) {
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

SparkyNPKParser::PositionContext::PositionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyNPKParser::PositionContext::Float() {
  return getToken(SparkyNPKParser::Float, 0);
}

tree::TerminalNode* SparkyNPKParser::PositionContext::Integer() {
  return getToken(SparkyNPKParser::Integer, 0);
}


size_t SparkyNPKParser::PositionContext::getRuleIndex() const {
  return SparkyNPKParser::RulePosition;
}


std::any SparkyNPKParser::PositionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyNPKParserVisitor*>(visitor))
    return parserVisitor->visitPosition(this);
  else
    return visitor->visitChildren(this);
}

SparkyNPKParser::PositionContext* SparkyNPKParser::position() {
  PositionContext *_localctx = _tracker.createInstance<PositionContext>(_ctx, getState());
  enterRule(_localctx, 16, SparkyNPKParser::RulePosition);
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
    setState(221);
    _la = _input->LA(1);
    if (!(_la == SparkyNPKParser::Integer

    || _la == SparkyNPKParser::Float)) {
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

SparkyNPKParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyNPKParser::NumberContext::Real_vol() {
  return getToken(SparkyNPKParser::Real_vol, 0);
}

tree::TerminalNode* SparkyNPKParser::NumberContext::Real() {
  return getToken(SparkyNPKParser::Real, 0);
}

tree::TerminalNode* SparkyNPKParser::NumberContext::Float() {
  return getToken(SparkyNPKParser::Float, 0);
}

tree::TerminalNode* SparkyNPKParser::NumberContext::Integer() {
  return getToken(SparkyNPKParser::Integer, 0);
}


size_t SparkyNPKParser::NumberContext::getRuleIndex() const {
  return SparkyNPKParser::RuleNumber;
}


std::any SparkyNPKParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyNPKParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

SparkyNPKParser::NumberContext* SparkyNPKParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 18, SparkyNPKParser::RuleNumber);
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
    setState(223);
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

SparkyNPKParser::NoteContext::NoteContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* SparkyNPKParser::NoteContext::Simple_name() {
  return getToken(SparkyNPKParser::Simple_name, 0);
}

tree::TerminalNode* SparkyNPKParser::NoteContext::Integer() {
  return getToken(SparkyNPKParser::Integer, 0);
}

tree::TerminalNode* SparkyNPKParser::NoteContext::Float() {
  return getToken(SparkyNPKParser::Float, 0);
}

tree::TerminalNode* SparkyNPKParser::NoteContext::Note_2d_ex() {
  return getToken(SparkyNPKParser::Note_2d_ex, 0);
}

tree::TerminalNode* SparkyNPKParser::NoteContext::Note_3d_ex() {
  return getToken(SparkyNPKParser::Note_3d_ex, 0);
}

tree::TerminalNode* SparkyNPKParser::NoteContext::Note_4d_ex() {
  return getToken(SparkyNPKParser::Note_4d_ex, 0);
}

tree::TerminalNode* SparkyNPKParser::NoteContext::Note_ex() {
  return getToken(SparkyNPKParser::Note_ex, 0);
}


size_t SparkyNPKParser::NoteContext::getRuleIndex() const {
  return SparkyNPKParser::RuleNote;
}


std::any SparkyNPKParser::NoteContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<SparkyNPKParserVisitor*>(visitor))
    return parserVisitor->visitNote(this);
  else
    return visitor->visitChildren(this);
}

SparkyNPKParser::NoteContext* SparkyNPKParser::note() {
  NoteContext *_localctx = _tracker.createInstance<NoteContext>(_ctx, getState());
  enterRule(_localctx, 20, SparkyNPKParser::RuleNote);
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
    setState(225);
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

void SparkyNPKParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  sparkynpkparserParserInitialize();
#else
  ::antlr4::internal::call_once(sparkynpkparserParserOnceFlag, sparkynpkparserParserInitialize);
#endif
}
