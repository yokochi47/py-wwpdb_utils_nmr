
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/GarretCSParser.g4 by ANTLR 4.13.2


#include "GarretCSParserVisitor.h"

#include "GarretCSParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct GarretCSParserStaticData final {
  GarretCSParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  GarretCSParserStaticData(const GarretCSParserStaticData&) = delete;
  GarretCSParserStaticData(GarretCSParserStaticData&&) = delete;
  GarretCSParserStaticData& operator=(const GarretCSParserStaticData&) = delete;
  GarretCSParserStaticData& operator=(GarretCSParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag garretcsparserParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<GarretCSParserStaticData> garretcsparserParserStaticData = nullptr;

void garretcsparserParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (garretcsparserParserStaticData != nullptr) {
    return;
  }
#else
  assert(garretcsparserParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<GarretCSParserStaticData>(
    std::vector<std::string>{
      "garret_cs", "residue_list", "res_id", "shift_list", "number"
    },
    std::vector<std::string>{
    },
    std::vector<std::string>{
      "", "Integer", "Float", "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", 
      "Simple_name", "SPACE", "RETURN", "SECTION_COMMENT", "LINE_COMMENT"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,10,44,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,3,0,12,8,0,1,0,
  	4,0,15,8,0,11,0,12,0,16,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
  	1,1,1,1,1,4,1,31,8,1,11,1,12,1,32,1,2,1,2,1,3,1,3,1,3,3,3,40,8,3,1,4,
  	1,4,1,4,0,0,5,0,2,4,6,8,0,2,2,0,1,1,6,6,2,0,1,2,6,6,43,0,11,1,0,0,0,2,
  	26,1,0,0,0,4,34,1,0,0,0,6,36,1,0,0,0,8,41,1,0,0,0,10,12,5,8,0,0,11,10,
  	1,0,0,0,11,12,1,0,0,0,12,14,1,0,0,0,13,15,3,2,1,0,14,13,1,0,0,0,15,16,
  	1,0,0,0,16,14,1,0,0,0,16,17,1,0,0,0,17,21,1,0,0,0,18,20,5,8,0,0,19,18,
  	1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,
  	1,0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,27,3,4,2,0,27,28,5,6,0,0,28,30,
  	5,8,0,0,29,31,3,6,3,0,30,29,1,0,0,0,31,32,1,0,0,0,32,30,1,0,0,0,32,33,
  	1,0,0,0,33,3,1,0,0,0,34,35,7,0,0,0,35,5,1,0,0,0,36,37,5,6,0,0,37,39,3,
  	8,4,0,38,40,5,8,0,0,39,38,1,0,0,0,39,40,1,0,0,0,40,7,1,0,0,0,41,42,7,
  	1,0,0,42,9,1,0,0,0,5,11,16,21,32,39
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  garretcsparserParserStaticData = std::move(staticData);
}

}

GarretCSParser::GarretCSParser(TokenStream *input) : GarretCSParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

GarretCSParser::GarretCSParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  GarretCSParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *garretcsparserParserStaticData->atn, garretcsparserParserStaticData->decisionToDFA, garretcsparserParserStaticData->sharedContextCache, options);
}

GarretCSParser::~GarretCSParser() {
  delete _interpreter;
}

const atn::ATN& GarretCSParser::getATN() const {
  return *garretcsparserParserStaticData->atn;
}

std::string GarretCSParser::getGrammarFileName() const {
  return "GarretCSParser.g4";
}

const std::vector<std::string>& GarretCSParser::getRuleNames() const {
  return garretcsparserParserStaticData->ruleNames;
}

const dfa::Vocabulary& GarretCSParser::getVocabulary() const {
  return garretcsparserParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView GarretCSParser::getSerializedATN() const {
  return garretcsparserParserStaticData->serializedATN;
}


//----------------- Garret_csContext ------------------------------------------------------------------

GarretCSParser::Garret_csContext::Garret_csContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GarretCSParser::Garret_csContext::EOF() {
  return getToken(GarretCSParser::EOF, 0);
}

std::vector<tree::TerminalNode *> GarretCSParser::Garret_csContext::RETURN() {
  return getTokens(GarretCSParser::RETURN);
}

tree::TerminalNode* GarretCSParser::Garret_csContext::RETURN(size_t i) {
  return getToken(GarretCSParser::RETURN, i);
}

std::vector<GarretCSParser::Residue_listContext *> GarretCSParser::Garret_csContext::residue_list() {
  return getRuleContexts<GarretCSParser::Residue_listContext>();
}

GarretCSParser::Residue_listContext* GarretCSParser::Garret_csContext::residue_list(size_t i) {
  return getRuleContext<GarretCSParser::Residue_listContext>(i);
}


size_t GarretCSParser::Garret_csContext::getRuleIndex() const {
  return GarretCSParser::RuleGarret_cs;
}


std::any GarretCSParser::Garret_csContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GarretCSParserVisitor*>(visitor))
    return parserVisitor->visitGarret_cs(this);
  else
    return visitor->visitChildren(this);
}

GarretCSParser::Garret_csContext* GarretCSParser::garret_cs() {
  Garret_csContext *_localctx = _tracker.createInstance<Garret_csContext>(_ctx, getState());
  enterRule(_localctx, 0, GarretCSParser::RuleGarret_cs);
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
    setState(11);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == GarretCSParser::RETURN) {
      setState(10);
      match(GarretCSParser::RETURN);
    }
    setState(14); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(13);
      residue_list();
      setState(16); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == GarretCSParser::Integer

    || _la == GarretCSParser::Simple_name);
    setState(21);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == GarretCSParser::RETURN) {
      setState(18);
      match(GarretCSParser::RETURN);
      setState(23);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(24);
    match(GarretCSParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Residue_listContext ------------------------------------------------------------------

GarretCSParser::Residue_listContext::Residue_listContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

GarretCSParser::Res_idContext* GarretCSParser::Residue_listContext::res_id() {
  return getRuleContext<GarretCSParser::Res_idContext>(0);
}

tree::TerminalNode* GarretCSParser::Residue_listContext::Simple_name() {
  return getToken(GarretCSParser::Simple_name, 0);
}

tree::TerminalNode* GarretCSParser::Residue_listContext::RETURN() {
  return getToken(GarretCSParser::RETURN, 0);
}

std::vector<GarretCSParser::Shift_listContext *> GarretCSParser::Residue_listContext::shift_list() {
  return getRuleContexts<GarretCSParser::Shift_listContext>();
}

GarretCSParser::Shift_listContext* GarretCSParser::Residue_listContext::shift_list(size_t i) {
  return getRuleContext<GarretCSParser::Shift_listContext>(i);
}


size_t GarretCSParser::Residue_listContext::getRuleIndex() const {
  return GarretCSParser::RuleResidue_list;
}


std::any GarretCSParser::Residue_listContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GarretCSParserVisitor*>(visitor))
    return parserVisitor->visitResidue_list(this);
  else
    return visitor->visitChildren(this);
}

GarretCSParser::Residue_listContext* GarretCSParser::residue_list() {
  Residue_listContext *_localctx = _tracker.createInstance<Residue_listContext>(_ctx, getState());
  enterRule(_localctx, 2, GarretCSParser::RuleResidue_list);

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
    setState(26);
    res_id();
    setState(27);
    match(GarretCSParser::Simple_name);
    setState(28);
    match(GarretCSParser::RETURN);
    setState(30); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(29);
              shift_list();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(32); 
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

//----------------- Res_idContext ------------------------------------------------------------------

GarretCSParser::Res_idContext::Res_idContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GarretCSParser::Res_idContext::Integer() {
  return getToken(GarretCSParser::Integer, 0);
}

tree::TerminalNode* GarretCSParser::Res_idContext::Simple_name() {
  return getToken(GarretCSParser::Simple_name, 0);
}


size_t GarretCSParser::Res_idContext::getRuleIndex() const {
  return GarretCSParser::RuleRes_id;
}


std::any GarretCSParser::Res_idContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GarretCSParserVisitor*>(visitor))
    return parserVisitor->visitRes_id(this);
  else
    return visitor->visitChildren(this);
}

GarretCSParser::Res_idContext* GarretCSParser::res_id() {
  Res_idContext *_localctx = _tracker.createInstance<Res_idContext>(_ctx, getState());
  enterRule(_localctx, 4, GarretCSParser::RuleRes_id);
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
    setState(34);
    _la = _input->LA(1);
    if (!(_la == GarretCSParser::Integer

    || _la == GarretCSParser::Simple_name)) {
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

//----------------- Shift_listContext ------------------------------------------------------------------

GarretCSParser::Shift_listContext::Shift_listContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GarretCSParser::Shift_listContext::Simple_name() {
  return getToken(GarretCSParser::Simple_name, 0);
}

GarretCSParser::NumberContext* GarretCSParser::Shift_listContext::number() {
  return getRuleContext<GarretCSParser::NumberContext>(0);
}

tree::TerminalNode* GarretCSParser::Shift_listContext::RETURN() {
  return getToken(GarretCSParser::RETURN, 0);
}


size_t GarretCSParser::Shift_listContext::getRuleIndex() const {
  return GarretCSParser::RuleShift_list;
}


std::any GarretCSParser::Shift_listContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GarretCSParserVisitor*>(visitor))
    return parserVisitor->visitShift_list(this);
  else
    return visitor->visitChildren(this);
}

GarretCSParser::Shift_listContext* GarretCSParser::shift_list() {
  Shift_listContext *_localctx = _tracker.createInstance<Shift_listContext>(_ctx, getState());
  enterRule(_localctx, 6, GarretCSParser::RuleShift_list);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(36);
    match(GarretCSParser::Simple_name);
    setState(37);
    number();
    setState(39);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 4, _ctx)) {
    case 1: {
      setState(38);
      match(GarretCSParser::RETURN);
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

//----------------- NumberContext ------------------------------------------------------------------

GarretCSParser::NumberContext::NumberContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* GarretCSParser::NumberContext::Float() {
  return getToken(GarretCSParser::Float, 0);
}

tree::TerminalNode* GarretCSParser::NumberContext::Integer() {
  return getToken(GarretCSParser::Integer, 0);
}

tree::TerminalNode* GarretCSParser::NumberContext::Simple_name() {
  return getToken(GarretCSParser::Simple_name, 0);
}


size_t GarretCSParser::NumberContext::getRuleIndex() const {
  return GarretCSParser::RuleNumber;
}


std::any GarretCSParser::NumberContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<GarretCSParserVisitor*>(visitor))
    return parserVisitor->visitNumber(this);
  else
    return visitor->visitChildren(this);
}

GarretCSParser::NumberContext* GarretCSParser::number() {
  NumberContext *_localctx = _tracker.createInstance<NumberContext>(_ctx, getState());
  enterRule(_localctx, 8, GarretCSParser::RuleNumber);
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
    setState(41);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 70) != 0))) {
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

void GarretCSParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  garretcsparserParserInitialize();
#else
  ::antlr4::internal::call_once(garretcsparserParserOnceFlag, garretcsparserParserInitialize);
#endif
}
