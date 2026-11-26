# Generated from GarretCSParser.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,44,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,3,0,12,8,0,
        1,0,4,0,15,8,0,11,0,12,0,16,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,
        1,0,1,1,1,1,1,1,1,1,4,1,31,8,1,11,1,12,1,32,1,2,1,2,1,3,1,3,1,3,
        3,3,40,8,3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,2,2,0,1,1,6,6,2,0,1,2,6,
        6,43,0,11,1,0,0,0,2,26,1,0,0,0,4,34,1,0,0,0,6,36,1,0,0,0,8,41,1,
        0,0,0,10,12,5,8,0,0,11,10,1,0,0,0,11,12,1,0,0,0,12,14,1,0,0,0,13,
        15,3,2,1,0,14,13,1,0,0,0,15,16,1,0,0,0,16,14,1,0,0,0,16,17,1,0,0,
        0,17,21,1,0,0,0,18,20,5,8,0,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,
        1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,
        25,1,1,0,0,0,26,27,3,4,2,0,27,28,5,6,0,0,28,30,5,8,0,0,29,31,3,6,
        3,0,30,29,1,0,0,0,31,32,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,3,
        1,0,0,0,34,35,7,0,0,0,35,5,1,0,0,0,36,37,5,6,0,0,37,39,3,8,4,0,38,
        40,5,8,0,0,39,38,1,0,0,0,39,40,1,0,0,0,40,7,1,0,0,0,41,42,7,1,0,
        0,42,9,1,0,0,0,5,11,16,21,32,39
    ]

class GarretCSParser ( Parser ):

    grammarFileName = "GarretCSParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "Integer", "Float", "SHARP_COMMENT", 
                      "EXCLM_COMMENT", "SMCLN_COMMENT", "Simple_name", "SPACE", 
                      "RETURN", "SECTION_COMMENT", "LINE_COMMENT" ]

    RULE_garret_cs = 0
    RULE_residue_list = 1
    RULE_res_id = 2
    RULE_shift_list = 3
    RULE_number = 4

    ruleNames =  [ "garret_cs", "residue_list", "res_id", "shift_list", 
                   "number" ]

    EOF = Token.EOF
    Integer=1
    Float=2
    SHARP_COMMENT=3
    EXCLM_COMMENT=4
    SMCLN_COMMENT=5
    Simple_name=6
    SPACE=7
    RETURN=8
    SECTION_COMMENT=9
    LINE_COMMENT=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Garret_csContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GarretCSParser.EOF, 0)

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(GarretCSParser.RETURN)
            else:
                return self.getToken(GarretCSParser.RETURN, i)

        def residue_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GarretCSParser.Residue_listContext)
            else:
                return self.getTypedRuleContext(GarretCSParser.Residue_listContext,i)


        def getRuleIndex(self):
            return GarretCSParser.RULE_garret_cs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGarret_cs" ):
                listener.enterGarret_cs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGarret_cs" ):
                listener.exitGarret_cs(self)




    def garret_cs(self):

        localctx = GarretCSParser.Garret_csContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_garret_cs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 10
                self.match(GarretCSParser.RETURN)


            self.state = 14 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 13
                self.residue_list()
                self.state = 16 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==6):
                    break

            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 18
                self.match(GarretCSParser.RETURN)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(GarretCSParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Residue_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def res_id(self):
            return self.getTypedRuleContext(GarretCSParser.Res_idContext,0)


        def Simple_name(self):
            return self.getToken(GarretCSParser.Simple_name, 0)

        def RETURN(self):
            return self.getToken(GarretCSParser.RETURN, 0)

        def shift_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GarretCSParser.Shift_listContext)
            else:
                return self.getTypedRuleContext(GarretCSParser.Shift_listContext,i)


        def getRuleIndex(self):
            return GarretCSParser.RULE_residue_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResidue_list" ):
                listener.enterResidue_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResidue_list" ):
                listener.exitResidue_list(self)




    def residue_list(self):

        localctx = GarretCSParser.Residue_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_residue_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.res_id()
            self.state = 27
            self.match(GarretCSParser.Simple_name)
            self.state = 28
            self.match(GarretCSParser.RETURN)
            self.state = 30 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 29
                    self.shift_list()

                else:
                    raise NoViableAltException(self)
                self.state = 32 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Res_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self):
            return self.getToken(GarretCSParser.Integer, 0)

        def Simple_name(self):
            return self.getToken(GarretCSParser.Simple_name, 0)

        def getRuleIndex(self):
            return GarretCSParser.RULE_res_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRes_id" ):
                listener.enterRes_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRes_id" ):
                listener.exitRes_id(self)




    def res_id(self):

        localctx = GarretCSParser.Res_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_res_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            _la = self._input.LA(1)
            if not(_la==1 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Shift_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Simple_name(self):
            return self.getToken(GarretCSParser.Simple_name, 0)

        def number(self):
            return self.getTypedRuleContext(GarretCSParser.NumberContext,0)


        def RETURN(self):
            return self.getToken(GarretCSParser.RETURN, 0)

        def getRuleIndex(self):
            return GarretCSParser.RULE_shift_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShift_list" ):
                listener.enterShift_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShift_list" ):
                listener.exitShift_list(self)




    def shift_list(self):

        localctx = GarretCSParser.Shift_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_shift_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(GarretCSParser.Simple_name)
            self.state = 37
            self.number()
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 38
                self.match(GarretCSParser.RETURN)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Float(self):
            return self.getToken(GarretCSParser.Float, 0)

        def Integer(self):
            return self.getToken(GarretCSParser.Integer, 0)

        def Simple_name(self):
            return self.getToken(GarretCSParser.Simple_name, 0)

        def getRuleIndex(self):
            return GarretCSParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = GarretCSParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 70) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





