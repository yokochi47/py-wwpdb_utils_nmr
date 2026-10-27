
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
      "peak_3d_po", "peak_4d_po", "number", "note"
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
  	4,1,51,226,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,1,0,3,0,22,8,0,1,0,1,0,4,0,26,8,0,11,0,12,0,27,
  	1,0,4,0,31,8,0,11,0,12,0,32,1,0,4,0,36,8,0,11,0,12,0,37,1,0,4,0,41,8,
  	0,11,0,12,0,42,1,0,4,0,46,8,0,11,0,12,0,47,1,0,4,0,51,8,0,11,0,12,0,52,
  	1,0,5,0,56,8,0,10,0,12,0,59,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,67,8,1,1,
  	1,3,1,70,8,1,1,1,3,1,73,8,1,1,1,3,1,76,8,1,1,1,3,1,79,8,1,1,1,3,1,82,
  	8,1,1,1,3,1,85,8,1,1,1,3,1,88,8,1,1,1,3,1,91,8,1,1,1,3,1,94,8,1,1,1,3,
  	1,97,8,1,1,1,1,1,3,1,101,8,1,1,1,3,1,104,8,1,1,1,1,1,3,1,108,8,1,1,1,
  	3,1,111,8,1,1,1,3,1,114,8,1,1,1,3,1,117,8,1,1,1,3,1,120,8,1,1,1,3,1,123,
  	8,1,1,1,3,1,126,8,1,1,1,3,1,129,8,1,1,1,3,1,132,8,1,1,1,3,1,135,8,1,1,
  	1,3,1,138,8,1,1,1,3,1,141,8,1,1,1,3,1,144,8,1,1,1,1,1,3,1,148,8,1,1,2,
  	1,2,1,2,1,2,5,2,154,8,2,10,2,12,2,157,9,2,1,2,5,2,160,8,2,10,2,12,2,163,
  	9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,5,3,172,8,3,10,3,12,3,175,9,3,1,3,5,3,
  	178,8,3,10,3,12,3,181,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,191,8,4,
  	10,4,12,4,194,9,4,1,4,5,4,197,8,4,10,4,12,4,200,9,4,1,4,1,4,1,5,1,5,1,
  	5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,
  	1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,6,2,0,1,1,10,12,1,1,19,
  	19,1,0,10,12,1,0,11,12,1,0,3,6,2,0,3,4,13,17,265,0,21,1,0,0,0,2,62,1,
  	0,0,0,4,149,1,0,0,0,6,166,1,0,0,0,8,184,1,0,0,0,10,203,1,0,0,0,12,208,
  	1,0,0,0,14,214,1,0,0,0,16,221,1,0,0,0,18,223,1,0,0,0,20,22,5,19,0,0,21,
  	20,1,0,0,0,21,22,1,0,0,0,22,57,1,0,0,0,23,56,3,2,1,0,24,26,3,10,5,0,25,
  	24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,56,1,0,0,0,29,
  	31,3,12,6,0,30,29,1,0,0,0,31,32,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,
  	56,1,0,0,0,34,36,3,14,7,0,35,34,1,0,0,0,36,37,1,0,0,0,37,35,1,0,0,0,37,
  	38,1,0,0,0,38,56,1,0,0,0,39,41,3,4,2,0,40,39,1,0,0,0,41,42,1,0,0,0,42,
  	40,1,0,0,0,42,43,1,0,0,0,43,56,1,0,0,0,44,46,3,6,3,0,45,44,1,0,0,0,46,
  	47,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,56,1,0,0,0,49,51,3,8,4,0,50,
  	49,1,0,0,0,51,52,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,56,1,0,0,0,54,
  	56,5,19,0,0,55,23,1,0,0,0,55,25,1,0,0,0,55,30,1,0,0,0,55,35,1,0,0,0,55,
  	40,1,0,0,0,55,45,1,0,0,0,55,50,1,0,0,0,55,54,1,0,0,0,56,59,1,0,0,0,57,
  	55,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,57,1,0,0,0,60,61,5,0,0,1,61,
  	1,1,0,0,0,62,63,7,0,0,0,63,64,5,31,0,0,64,66,5,32,0,0,65,67,5,33,0,0,
  	66,65,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,0,68,70,5,34,0,0,69,68,1,0,0,
  	0,69,70,1,0,0,0,70,72,1,0,0,0,71,73,5,23,0,0,72,71,1,0,0,0,72,73,1,0,
  	0,0,73,75,1,0,0,0,74,76,5,24,0,0,75,74,1,0,0,0,75,76,1,0,0,0,76,78,1,
  	0,0,0,77,79,5,25,0,0,78,77,1,0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,80,82,
  	5,26,0,0,81,80,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,85,5,35,0,0,84,
  	83,1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,88,5,36,0,0,87,86,1,0,0,0,87,
  	88,1,0,0,0,88,90,1,0,0,0,89,91,5,37,0,0,90,89,1,0,0,0,90,91,1,0,0,0,91,
  	93,1,0,0,0,92,94,5,38,0,0,93,92,1,0,0,0,93,94,1,0,0,0,94,100,1,0,0,0,
  	95,97,5,39,0,0,96,95,1,0,0,0,96,97,1,0,0,0,97,98,1,0,0,0,98,101,5,40,
  	0,0,99,101,5,41,0,0,100,96,1,0,0,0,100,99,1,0,0,0,100,101,1,0,0,0,101,
  	107,1,0,0,0,102,104,5,39,0,0,103,102,1,0,0,0,103,104,1,0,0,0,104,105,
  	1,0,0,0,105,108,5,40,0,0,106,108,5,41,0,0,107,103,1,0,0,0,107,106,1,0,
  	0,0,107,108,1,0,0,0,108,110,1,0,0,0,109,111,5,42,0,0,110,109,1,0,0,0,
  	110,111,1,0,0,0,111,113,1,0,0,0,112,114,5,43,0,0,113,112,1,0,0,0,113,
  	114,1,0,0,0,114,116,1,0,0,0,115,117,5,27,0,0,116,115,1,0,0,0,116,117,
  	1,0,0,0,117,119,1,0,0,0,118,120,5,28,0,0,119,118,1,0,0,0,119,120,1,0,
  	0,0,120,122,1,0,0,0,121,123,5,29,0,0,122,121,1,0,0,0,122,123,1,0,0,0,
  	123,125,1,0,0,0,124,126,5,30,0,0,125,124,1,0,0,0,125,126,1,0,0,0,126,
  	128,1,0,0,0,127,129,5,44,0,0,128,127,1,0,0,0,128,129,1,0,0,0,129,131,
  	1,0,0,0,130,132,5,45,0,0,131,130,1,0,0,0,131,132,1,0,0,0,132,134,1,0,
  	0,0,133,135,5,46,0,0,134,133,1,0,0,0,134,135,1,0,0,0,135,137,1,0,0,0,
  	136,138,5,47,0,0,137,136,1,0,0,0,137,138,1,0,0,0,138,140,1,0,0,0,139,
  	141,5,48,0,0,140,139,1,0,0,0,140,141,1,0,0,0,141,143,1,0,0,0,142,144,
  	5,49,0,0,143,142,1,0,0,0,143,144,1,0,0,0,144,145,1,0,0,0,145,147,5,51,
  	0,0,146,148,5,19,0,0,147,146,1,0,0,0,147,148,1,0,0,0,148,3,1,0,0,0,149,
  	150,5,10,0,0,150,151,5,4,0,0,151,155,5,4,0,0,152,154,3,16,8,0,153,152,
  	1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,161,1,0,0,
  	0,157,155,1,0,0,0,158,160,3,18,9,0,159,158,1,0,0,0,160,163,1,0,0,0,161,
  	159,1,0,0,0,161,162,1,0,0,0,162,164,1,0,0,0,163,161,1,0,0,0,164,165,7,
  	1,0,0,165,5,1,0,0,0,166,167,5,11,0,0,167,168,5,4,0,0,168,169,5,4,0,0,
  	169,173,5,4,0,0,170,172,3,16,8,0,171,170,1,0,0,0,172,175,1,0,0,0,173,
  	171,1,0,0,0,173,174,1,0,0,0,174,179,1,0,0,0,175,173,1,0,0,0,176,178,3,
  	18,9,0,177,176,1,0,0,0,178,181,1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,
  	0,180,182,1,0,0,0,181,179,1,0,0,0,182,183,7,1,0,0,183,7,1,0,0,0,184,185,
  	5,12,0,0,185,186,5,4,0,0,186,187,5,4,0,0,187,188,5,4,0,0,188,192,5,4,
  	0,0,189,191,3,16,8,0,190,189,1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,
  	192,193,1,0,0,0,193,198,1,0,0,0,194,192,1,0,0,0,195,197,3,18,9,0,196,
  	195,1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,201,1,
  	0,0,0,200,198,1,0,0,0,201,202,7,1,0,0,202,9,1,0,0,0,203,204,7,2,0,0,204,
  	205,5,4,0,0,205,206,5,4,0,0,206,207,7,1,0,0,207,11,1,0,0,0,208,209,7,
  	3,0,0,209,210,5,4,0,0,210,211,5,4,0,0,211,212,5,4,0,0,212,213,7,1,0,0,
  	213,13,1,0,0,0,214,215,5,12,0,0,215,216,5,4,0,0,216,217,5,4,0,0,217,218,
  	5,4,0,0,218,219,5,4,0,0,219,220,7,1,0,0,220,15,1,0,0,0,221,222,7,4,0,
  	0,222,17,1,0,0,0,223,224,7,5,0,0,224,19,1,0,0,0,42,21,27,32,37,42,47,
  	52,55,57,66,69,72,75,78,81,84,87,90,93,96,100,103,107,110,113,116,119,
  	122,125,128,131,134,137,140,143,147,155,161,173,179,192,198
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
    setState(21);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 0, _ctx)) {
    case 1: {
      setState(20);
      match(SparkyNPKParser::RETURN);
      break;
    }

    default:
      break;
    }
    setState(57);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 531458) != 0)) {
      setState(55);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 7, _ctx)) {
      case 1: {
        setState(23);
        data_label();
        break;
      }

      case 2: {
        setState(25); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(24);
                  peak_2d_po();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(27); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 3: {
        setState(30); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(29);
                  peak_3d_po();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(32); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 2, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 4: {
        setState(35); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(34);
                  peak_4d_po();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(37); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 3, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 5: {
        setState(40); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(39);
                  peak_2d();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(42); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 4, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 6: {
        setState(45); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(44);
                  peak_3d();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(47); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 5, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 7: {
        setState(50); 
        _errHandler->sync(this);
        alt = 1;
        do {
          switch (alt) {
            case 1: {
                  setState(49);
                  peak_4d();
                  break;
                }

          default:
            throw NoViableAltException(this);
          }
          setState(52); 
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 6, _ctx);
        } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
        break;
      }

      case 8: {
        setState(54);
        match(SparkyNPKParser::RETURN);
        break;
      }

      default:
        break;
      }
      setState(59);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(60);
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
    setState(62);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 7170) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(63);
    match(SparkyNPKParser::W1_LA);
    setState(64);
    match(SparkyNPKParser::W2_LA);
    setState(66);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::W3_LA) {
      setState(65);
      match(SparkyNPKParser::W3_LA);
    }
    setState(69);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::W4_LA) {
      setState(68);
      match(SparkyNPKParser::W4_LA);
    }
    setState(72);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::W1_Hz_LA) {
      setState(71);
      match(SparkyNPKParser::W1_Hz_LA);
    }
    setState(75);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::W2_Hz_LA) {
      setState(74);
      match(SparkyNPKParser::W2_Hz_LA);
    }
    setState(78);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::W3_Hz_LA) {
      setState(77);
      match(SparkyNPKParser::W3_Hz_LA);
    }
    setState(81);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::W4_Hz_LA) {
      setState(80);
      match(SparkyNPKParser::W4_Hz_LA);
    }
    setState(84);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Dev_w1_LA) {
      setState(83);
      match(SparkyNPKParser::Dev_w1_LA);
    }
    setState(87);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Dev_w2_LA) {
      setState(86);
      match(SparkyNPKParser::Dev_w2_LA);
    }
    setState(90);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Dev_w3_LA) {
      setState(89);
      match(SparkyNPKParser::Dev_w3_LA);
    }
    setState(93);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Dev_w4_LA) {
      setState(92);
      match(SparkyNPKParser::Dev_w4_LA);
    }
    setState(100);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 20, _ctx)) {
    case 1: {
      setState(96);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == SparkyNPKParser::Dummy_H_LA) {
        setState(95);
        match(SparkyNPKParser::Dummy_H_LA);
      }
      setState(98);
      match(SparkyNPKParser::Height_LA);
      break;
    }

    case 2: {
      setState(99);
      match(SparkyNPKParser::Volume_LA);
      break;
    }

    default:
      break;
    }
    setState(107);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case SparkyNPKParser::Dummy_H_LA:
      case SparkyNPKParser::Height_LA: {
        setState(103);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == SparkyNPKParser::Dummy_H_LA) {
          setState(102);
          match(SparkyNPKParser::Dummy_H_LA);
        }
        setState(105);
        match(SparkyNPKParser::Height_LA);
        break;
      }

      case SparkyNPKParser::Volume_LA: {
        setState(106);
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
    setState(110);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Dummy_Rms_LA) {
      setState(109);
      match(SparkyNPKParser::Dummy_Rms_LA);
    }
    setState(113);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::S_N_LA) {
      setState(112);
      match(SparkyNPKParser::S_N_LA);
    }
    setState(116);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Lw1_Hz_LA) {
      setState(115);
      match(SparkyNPKParser::Lw1_Hz_LA);
    }
    setState(119);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Lw2_Hz_LA) {
      setState(118);
      match(SparkyNPKParser::Lw2_Hz_LA);
    }
    setState(122);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Lw3_Hz_LA) {
      setState(121);
      match(SparkyNPKParser::Lw3_Hz_LA);
    }
    setState(125);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Lw4_Hz_LA) {
      setState(124);
      match(SparkyNPKParser::Lw4_Hz_LA);
    }
    setState(128);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Atom1_LA) {
      setState(127);
      match(SparkyNPKParser::Atom1_LA);
    }
    setState(131);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Atom2_LA) {
      setState(130);
      match(SparkyNPKParser::Atom2_LA);
    }
    setState(134);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Atom3_LA) {
      setState(133);
      match(SparkyNPKParser::Atom3_LA);
    }
    setState(137);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Atom4_LA) {
      setState(136);
      match(SparkyNPKParser::Atom4_LA);
    }
    setState(140);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Distance_LA) {
      setState(139);
      match(SparkyNPKParser::Distance_LA);
    }
    setState(143);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == SparkyNPKParser::Note_LA) {
      setState(142);
      match(SparkyNPKParser::Note_LA);
    }
    setState(145);
    match(SparkyNPKParser::RETURN_LA);
    setState(147);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 35, _ctx)) {
    case 1: {
      setState(146);
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

std::vector<tree::TerminalNode *> SparkyNPKParser::Peak_2dContext::Float() {
  return getTokens(SparkyNPKParser::Float);
}

tree::TerminalNode* SparkyNPKParser::Peak_2dContext::Float(size_t i) {
  return getToken(SparkyNPKParser::Float, i);
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
    setState(149);
    match(SparkyNPKParser::Assignment_2d_ex);
    setState(150);
    match(SparkyNPKParser::Float);
    setState(151);
    match(SparkyNPKParser::Float);
    setState(155);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 36, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(152);
        number(); 
      }
      setState(157);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 36, _ctx);
    }
    setState(161);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 253976) != 0)) {
      setState(158);
      note();
      setState(163);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(164);
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

std::vector<tree::TerminalNode *> SparkyNPKParser::Peak_3dContext::Float() {
  return getTokens(SparkyNPKParser::Float);
}

tree::TerminalNode* SparkyNPKParser::Peak_3dContext::Float(size_t i) {
  return getToken(SparkyNPKParser::Float, i);
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
    setState(166);
    match(SparkyNPKParser::Assignment_3d_ex);
    setState(167);
    match(SparkyNPKParser::Float);
    setState(168);
    match(SparkyNPKParser::Float);
    setState(169);
    match(SparkyNPKParser::Float);
    setState(173);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 38, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(170);
        number(); 
      }
      setState(175);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 38, _ctx);
    }
    setState(179);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 253976) != 0)) {
      setState(176);
      note();
      setState(181);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(182);
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

std::vector<tree::TerminalNode *> SparkyNPKParser::Peak_4dContext::Float() {
  return getTokens(SparkyNPKParser::Float);
}

tree::TerminalNode* SparkyNPKParser::Peak_4dContext::Float(size_t i) {
  return getToken(SparkyNPKParser::Float, i);
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
    setState(184);
    match(SparkyNPKParser::Assignment_4d_ex);
    setState(185);
    match(SparkyNPKParser::Float);
    setState(186);
    match(SparkyNPKParser::Float);
    setState(187);
    match(SparkyNPKParser::Float);
    setState(188);
    match(SparkyNPKParser::Float);
    setState(192);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 40, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(189);
        number(); 
      }
      setState(194);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 40, _ctx);
    }
    setState(198);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 253976) != 0)) {
      setState(195);
      note();
      setState(200);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(201);
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

std::vector<tree::TerminalNode *> SparkyNPKParser::Peak_2d_poContext::Float() {
  return getTokens(SparkyNPKParser::Float);
}

tree::TerminalNode* SparkyNPKParser::Peak_2d_poContext::Float(size_t i) {
  return getToken(SparkyNPKParser::Float, i);
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
    setState(203);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 7168) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(204);
    match(SparkyNPKParser::Float);
    setState(205);
    match(SparkyNPKParser::Float);
    setState(206);
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

std::vector<tree::TerminalNode *> SparkyNPKParser::Peak_3d_poContext::Float() {
  return getTokens(SparkyNPKParser::Float);
}

tree::TerminalNode* SparkyNPKParser::Peak_3d_poContext::Float(size_t i) {
  return getToken(SparkyNPKParser::Float, i);
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
    setState(208);
    _la = _input->LA(1);
    if (!(_la == SparkyNPKParser::Assignment_3d_ex

    || _la == SparkyNPKParser::Assignment_4d_ex)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(209);
    match(SparkyNPKParser::Float);
    setState(210);
    match(SparkyNPKParser::Float);
    setState(211);
    match(SparkyNPKParser::Float);
    setState(212);
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

std::vector<tree::TerminalNode *> SparkyNPKParser::Peak_4d_poContext::Float() {
  return getTokens(SparkyNPKParser::Float);
}

tree::TerminalNode* SparkyNPKParser::Peak_4d_poContext::Float(size_t i) {
  return getToken(SparkyNPKParser::Float, i);
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
    setState(214);
    match(SparkyNPKParser::Assignment_4d_ex);
    setState(215);
    match(SparkyNPKParser::Float);
    setState(216);
    match(SparkyNPKParser::Float);
    setState(217);
    match(SparkyNPKParser::Float);
    setState(218);
    match(SparkyNPKParser::Float);
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
  enterRule(_localctx, 16, SparkyNPKParser::RuleNumber);
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
  enterRule(_localctx, 18, SparkyNPKParser::RuleNote);
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
