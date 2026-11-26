# Generated from SparkyNPKParser.g4 by ANTLR 4.13.0
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
        4,1,51,228,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,3,0,24,8,0,1,0,1,0,4,0,28,
        8,0,11,0,12,0,29,1,0,4,0,33,8,0,11,0,12,0,34,1,0,4,0,38,8,0,11,0,
        12,0,39,1,0,4,0,43,8,0,11,0,12,0,44,1,0,4,0,48,8,0,11,0,12,0,49,
        1,0,4,0,53,8,0,11,0,12,0,54,1,0,5,0,58,8,0,10,0,12,0,61,9,0,1,0,
        1,0,1,1,1,1,1,1,1,1,3,1,69,8,1,1,1,3,1,72,8,1,1,1,3,1,75,8,1,1,1,
        3,1,78,8,1,1,1,3,1,81,8,1,1,1,3,1,84,8,1,1,1,3,1,87,8,1,1,1,3,1,
        90,8,1,1,1,3,1,93,8,1,1,1,3,1,96,8,1,1,1,3,1,99,8,1,1,1,1,1,3,1,
        103,8,1,1,1,3,1,106,8,1,1,1,1,1,3,1,110,8,1,1,1,3,1,113,8,1,1,1,
        3,1,116,8,1,1,1,3,1,119,8,1,1,1,3,1,122,8,1,1,1,3,1,125,8,1,1,1,
        3,1,128,8,1,1,1,3,1,131,8,1,1,1,3,1,134,8,1,1,1,3,1,137,8,1,1,1,
        3,1,140,8,1,1,1,3,1,143,8,1,1,1,3,1,146,8,1,1,1,1,1,3,1,150,8,1,
        1,2,1,2,1,2,1,2,5,2,156,8,2,10,2,12,2,159,9,2,1,2,5,2,162,8,2,10,
        2,12,2,165,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,5,3,174,8,3,10,3,12,3,
        177,9,3,1,3,5,3,180,8,3,10,3,12,3,183,9,3,1,3,1,3,1,4,1,4,1,4,1,
        4,1,4,5,4,192,8,4,10,4,12,4,195,9,4,1,4,5,4,198,8,4,10,4,12,4,201,
        9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,
        1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,
        10,12,14,16,18,20,0,7,2,0,1,1,10,12,1,1,19,19,1,0,10,12,1,0,11,12,
        1,0,3,4,1,0,3,6,2,0,3,4,13,17,266,0,23,1,0,0,0,2,64,1,0,0,0,4,151,
        1,0,0,0,6,168,1,0,0,0,8,186,1,0,0,0,10,204,1,0,0,0,12,209,1,0,0,
        0,14,215,1,0,0,0,16,221,1,0,0,0,18,223,1,0,0,0,20,225,1,0,0,0,22,
        24,5,19,0,0,23,22,1,0,0,0,23,24,1,0,0,0,24,59,1,0,0,0,25,58,3,2,
        1,0,26,28,3,10,5,0,27,26,1,0,0,0,28,29,1,0,0,0,29,27,1,0,0,0,29,
        30,1,0,0,0,30,58,1,0,0,0,31,33,3,12,6,0,32,31,1,0,0,0,33,34,1,0,
        0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,58,1,0,0,0,36,38,3,14,7,0,37,
        36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,58,1,0,0,
        0,41,43,3,4,2,0,42,41,1,0,0,0,43,44,1,0,0,0,44,42,1,0,0,0,44,45,
        1,0,0,0,45,58,1,0,0,0,46,48,3,6,3,0,47,46,1,0,0,0,48,49,1,0,0,0,
        49,47,1,0,0,0,49,50,1,0,0,0,50,58,1,0,0,0,51,53,3,8,4,0,52,51,1,
        0,0,0,53,54,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,58,1,0,0,0,56,
        58,5,19,0,0,57,25,1,0,0,0,57,27,1,0,0,0,57,32,1,0,0,0,57,37,1,0,
        0,0,57,42,1,0,0,0,57,47,1,0,0,0,57,52,1,0,0,0,57,56,1,0,0,0,58,61,
        1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,
        62,63,5,0,0,1,63,1,1,0,0,0,64,65,7,0,0,0,65,66,5,31,0,0,66,68,5,
        32,0,0,67,69,5,33,0,0,68,67,1,0,0,0,68,69,1,0,0,0,69,71,1,0,0,0,
        70,72,5,34,0,0,71,70,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,75,5,
        23,0,0,74,73,1,0,0,0,74,75,1,0,0,0,75,77,1,0,0,0,76,78,5,24,0,0,
        77,76,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,81,5,25,0,0,80,79,1,
        0,0,0,80,81,1,0,0,0,81,83,1,0,0,0,82,84,5,26,0,0,83,82,1,0,0,0,83,
        84,1,0,0,0,84,86,1,0,0,0,85,87,5,35,0,0,86,85,1,0,0,0,86,87,1,0,
        0,0,87,89,1,0,0,0,88,90,5,36,0,0,89,88,1,0,0,0,89,90,1,0,0,0,90,
        92,1,0,0,0,91,93,5,37,0,0,92,91,1,0,0,0,92,93,1,0,0,0,93,95,1,0,
        0,0,94,96,5,38,0,0,95,94,1,0,0,0,95,96,1,0,0,0,96,102,1,0,0,0,97,
        99,5,39,0,0,98,97,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,103,5,
        40,0,0,101,103,5,41,0,0,102,98,1,0,0,0,102,101,1,0,0,0,102,103,1,
        0,0,0,103,109,1,0,0,0,104,106,5,39,0,0,105,104,1,0,0,0,105,106,1,
        0,0,0,106,107,1,0,0,0,107,110,5,40,0,0,108,110,5,41,0,0,109,105,
        1,0,0,0,109,108,1,0,0,0,109,110,1,0,0,0,110,112,1,0,0,0,111,113,
        5,42,0,0,112,111,1,0,0,0,112,113,1,0,0,0,113,115,1,0,0,0,114,116,
        5,43,0,0,115,114,1,0,0,0,115,116,1,0,0,0,116,118,1,0,0,0,117,119,
        5,27,0,0,118,117,1,0,0,0,118,119,1,0,0,0,119,121,1,0,0,0,120,122,
        5,28,0,0,121,120,1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,125,
        5,29,0,0,124,123,1,0,0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,128,
        5,30,0,0,127,126,1,0,0,0,127,128,1,0,0,0,128,130,1,0,0,0,129,131,
        5,44,0,0,130,129,1,0,0,0,130,131,1,0,0,0,131,133,1,0,0,0,132,134,
        5,45,0,0,133,132,1,0,0,0,133,134,1,0,0,0,134,136,1,0,0,0,135,137,
        5,46,0,0,136,135,1,0,0,0,136,137,1,0,0,0,137,139,1,0,0,0,138,140,
        5,47,0,0,139,138,1,0,0,0,139,140,1,0,0,0,140,142,1,0,0,0,141,143,
        5,48,0,0,142,141,1,0,0,0,142,143,1,0,0,0,143,145,1,0,0,0,144,146,
        5,49,0,0,145,144,1,0,0,0,145,146,1,0,0,0,146,147,1,0,0,0,147,149,
        5,51,0,0,148,150,5,19,0,0,149,148,1,0,0,0,149,150,1,0,0,0,150,3,
        1,0,0,0,151,152,5,10,0,0,152,153,3,16,8,0,153,157,3,16,8,0,154,156,
        3,18,9,0,155,154,1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,0,157,158,
        1,0,0,0,158,163,1,0,0,0,159,157,1,0,0,0,160,162,3,20,10,0,161,160,
        1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,166,
        1,0,0,0,165,163,1,0,0,0,166,167,7,1,0,0,167,5,1,0,0,0,168,169,5,
        11,0,0,169,170,3,16,8,0,170,171,3,16,8,0,171,175,3,16,8,0,172,174,
        3,18,9,0,173,172,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,176,
        1,0,0,0,176,181,1,0,0,0,177,175,1,0,0,0,178,180,3,20,10,0,179,178,
        1,0,0,0,180,183,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,184,
        1,0,0,0,183,181,1,0,0,0,184,185,7,1,0,0,185,7,1,0,0,0,186,187,5,
        12,0,0,187,188,3,16,8,0,188,189,3,16,8,0,189,193,3,16,8,0,190,192,
        3,18,9,0,191,190,1,0,0,0,192,195,1,0,0,0,193,191,1,0,0,0,193,194,
        1,0,0,0,194,199,1,0,0,0,195,193,1,0,0,0,196,198,3,20,10,0,197,196,
        1,0,0,0,198,201,1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,202,
        1,0,0,0,201,199,1,0,0,0,202,203,7,1,0,0,203,9,1,0,0,0,204,205,7,
        2,0,0,205,206,3,16,8,0,206,207,3,16,8,0,207,208,7,1,0,0,208,11,1,
        0,0,0,209,210,7,3,0,0,210,211,3,16,8,0,211,212,3,16,8,0,212,213,
        3,16,8,0,213,214,7,1,0,0,214,13,1,0,0,0,215,216,5,12,0,0,216,217,
        3,16,8,0,217,218,3,16,8,0,218,219,3,16,8,0,219,220,7,1,0,0,220,15,
        1,0,0,0,221,222,7,4,0,0,222,17,1,0,0,0,223,224,7,5,0,0,224,19,1,
        0,0,0,225,226,7,6,0,0,226,21,1,0,0,0,42,23,29,34,39,44,49,54,57,
        59,68,71,74,77,80,83,86,89,92,95,98,102,105,109,112,115,118,121,
        124,127,130,133,136,139,142,145,149,157,163,175,181,193,199
    ]

class SparkyNPKParser ( Parser ):

    grammarFileName = "SparkyNPKParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'w2'", "'w3'", "'w4'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'Volume'", 
                     "'Fit RMS %'" ]

    symbolicNames = [ "<INVALID>", "Assignment", "W1", "Integer", "Float", 
                      "Real", "Real_vol", "SHARP_COMMENT", "EXCLM_COMMENT", 
                      "SMCLN_COMMENT", "Assignment_2d_ex", "Assignment_3d_ex", 
                      "Assignment_4d_ex", "Note_2d_ex", "Note_3d_ex", "Note_4d_ex", 
                      "Note_ex", "Simple_name", "SPACE", "RETURN", "ENCLOSE_COMMENT", 
                      "SECTION_COMMENT", "LINE_COMMENT", "W1_Hz_LA", "W2_Hz_LA", 
                      "W3_Hz_LA", "W4_Hz_LA", "Lw1_Hz_LA", "Lw2_Hz_LA", 
                      "Lw3_Hz_LA", "Lw4_Hz_LA", "W1_LA", "W2_LA", "W3_LA", 
                      "W4_LA", "Dev_w1_LA", "Dev_w2_LA", "Dev_w3_LA", "Dev_w4_LA", 
                      "Dummy_H_LA", "Height_LA", "Volume_LA", "Dummy_Rms_LA", 
                      "S_N_LA", "Atom1_LA", "Atom2_LA", "Atom3_LA", "Atom4_LA", 
                      "Distance_LA", "Note_LA", "SPACE_LA", "RETURN_LA" ]

    RULE_sparky_npk = 0
    RULE_data_label = 1
    RULE_peak_2d = 2
    RULE_peak_3d = 3
    RULE_peak_4d = 4
    RULE_peak_2d_po = 5
    RULE_peak_3d_po = 6
    RULE_peak_4d_po = 7
    RULE_position = 8
    RULE_number = 9
    RULE_note = 10

    ruleNames =  [ "sparky_npk", "data_label", "peak_2d", "peak_3d", "peak_4d", 
                   "peak_2d_po", "peak_3d_po", "peak_4d_po", "position", 
                   "number", "note" ]

    EOF = Token.EOF
    Assignment=1
    W1=2
    Integer=3
    Float=4
    Real=5
    Real_vol=6
    SHARP_COMMENT=7
    EXCLM_COMMENT=8
    SMCLN_COMMENT=9
    Assignment_2d_ex=10
    Assignment_3d_ex=11
    Assignment_4d_ex=12
    Note_2d_ex=13
    Note_3d_ex=14
    Note_4d_ex=15
    Note_ex=16
    Simple_name=17
    SPACE=18
    RETURN=19
    ENCLOSE_COMMENT=20
    SECTION_COMMENT=21
    LINE_COMMENT=22
    W1_Hz_LA=23
    W2_Hz_LA=24
    W3_Hz_LA=25
    W4_Hz_LA=26
    Lw1_Hz_LA=27
    Lw2_Hz_LA=28
    Lw3_Hz_LA=29
    Lw4_Hz_LA=30
    W1_LA=31
    W2_LA=32
    W3_LA=33
    W4_LA=34
    Dev_w1_LA=35
    Dev_w2_LA=36
    Dev_w3_LA=37
    Dev_w4_LA=38
    Dummy_H_LA=39
    Height_LA=40
    Volume_LA=41
    Dummy_Rms_LA=42
    S_N_LA=43
    Atom1_LA=44
    Atom2_LA=45
    Atom3_LA=46
    Atom4_LA=47
    Distance_LA=48
    Note_LA=49
    SPACE_LA=50
    RETURN_LA=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Sparky_npkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SparkyNPKParser.EOF, 0)

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyNPKParser.RETURN)
            else:
                return self.getToken(SparkyNPKParser.RETURN, i)

        def data_label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.Data_labelContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.Data_labelContext,i)


        def peak_2d_po(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.Peak_2d_poContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.Peak_2d_poContext,i)


        def peak_3d_po(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.Peak_3d_poContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.Peak_3d_poContext,i)


        def peak_4d_po(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.Peak_4d_poContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.Peak_4d_poContext,i)


        def peak_2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.Peak_2dContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.Peak_2dContext,i)


        def peak_3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.Peak_3dContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.Peak_3dContext,i)


        def peak_4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.Peak_4dContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.Peak_4dContext,i)


        def getRuleIndex(self):
            return SparkyNPKParser.RULE_sparky_npk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSparky_npk" ):
                listener.enterSparky_npk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSparky_npk" ):
                listener.exitSparky_npk(self)




    def sparky_npk(self):

        localctx = SparkyNPKParser.Sparky_npkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sparky_npk)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 22
                self.match(SparkyNPKParser.RETURN)


            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 531458) != 0):
                self.state = 57
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 25
                    self.data_label()
                    pass

                elif la_ == 2:
                    self.state = 27 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 26
                            self.peak_2d_po()

                        else:
                            raise NoViableAltException(self)
                        self.state = 29 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                    pass

                elif la_ == 3:
                    self.state = 32 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 31
                            self.peak_3d_po()

                        else:
                            raise NoViableAltException(self)
                        self.state = 34 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                    pass

                elif la_ == 4:
                    self.state = 37 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 36
                            self.peak_4d_po()

                        else:
                            raise NoViableAltException(self)
                        self.state = 39 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                    pass

                elif la_ == 5:
                    self.state = 42 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 41
                            self.peak_2d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 44 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                    pass

                elif la_ == 6:
                    self.state = 47 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 46
                            self.peak_3d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 49 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                    pass

                elif la_ == 7:
                    self.state = 52 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 51
                            self.peak_4d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 54 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                    pass

                elif la_ == 8:
                    self.state = 56
                    self.match(SparkyNPKParser.RETURN)
                    pass


                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(SparkyNPKParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_labelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def W1_LA(self):
            return self.getToken(SparkyNPKParser.W1_LA, 0)

        def W2_LA(self):
            return self.getToken(SparkyNPKParser.W2_LA, 0)

        def RETURN_LA(self):
            return self.getToken(SparkyNPKParser.RETURN_LA, 0)

        def Assignment(self):
            return self.getToken(SparkyNPKParser.Assignment, 0)

        def Assignment_2d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_2d_ex, 0)

        def Assignment_3d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_3d_ex, 0)

        def Assignment_4d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_4d_ex, 0)

        def W3_LA(self):
            return self.getToken(SparkyNPKParser.W3_LA, 0)

        def W4_LA(self):
            return self.getToken(SparkyNPKParser.W4_LA, 0)

        def W1_Hz_LA(self):
            return self.getToken(SparkyNPKParser.W1_Hz_LA, 0)

        def W2_Hz_LA(self):
            return self.getToken(SparkyNPKParser.W2_Hz_LA, 0)

        def W3_Hz_LA(self):
            return self.getToken(SparkyNPKParser.W3_Hz_LA, 0)

        def W4_Hz_LA(self):
            return self.getToken(SparkyNPKParser.W4_Hz_LA, 0)

        def Dev_w1_LA(self):
            return self.getToken(SparkyNPKParser.Dev_w1_LA, 0)

        def Dev_w2_LA(self):
            return self.getToken(SparkyNPKParser.Dev_w2_LA, 0)

        def Dev_w3_LA(self):
            return self.getToken(SparkyNPKParser.Dev_w3_LA, 0)

        def Dev_w4_LA(self):
            return self.getToken(SparkyNPKParser.Dev_w4_LA, 0)

        def Height_LA(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyNPKParser.Height_LA)
            else:
                return self.getToken(SparkyNPKParser.Height_LA, i)

        def Volume_LA(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyNPKParser.Volume_LA)
            else:
                return self.getToken(SparkyNPKParser.Volume_LA, i)

        def Dummy_Rms_LA(self):
            return self.getToken(SparkyNPKParser.Dummy_Rms_LA, 0)

        def S_N_LA(self):
            return self.getToken(SparkyNPKParser.S_N_LA, 0)

        def Lw1_Hz_LA(self):
            return self.getToken(SparkyNPKParser.Lw1_Hz_LA, 0)

        def Lw2_Hz_LA(self):
            return self.getToken(SparkyNPKParser.Lw2_Hz_LA, 0)

        def Lw3_Hz_LA(self):
            return self.getToken(SparkyNPKParser.Lw3_Hz_LA, 0)

        def Lw4_Hz_LA(self):
            return self.getToken(SparkyNPKParser.Lw4_Hz_LA, 0)

        def Atom1_LA(self):
            return self.getToken(SparkyNPKParser.Atom1_LA, 0)

        def Atom2_LA(self):
            return self.getToken(SparkyNPKParser.Atom2_LA, 0)

        def Atom3_LA(self):
            return self.getToken(SparkyNPKParser.Atom3_LA, 0)

        def Atom4_LA(self):
            return self.getToken(SparkyNPKParser.Atom4_LA, 0)

        def Distance_LA(self):
            return self.getToken(SparkyNPKParser.Distance_LA, 0)

        def Note_LA(self):
            return self.getToken(SparkyNPKParser.Note_LA, 0)

        def RETURN(self):
            return self.getToken(SparkyNPKParser.RETURN, 0)

        def Dummy_H_LA(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyNPKParser.Dummy_H_LA)
            else:
                return self.getToken(SparkyNPKParser.Dummy_H_LA, i)

        def getRuleIndex(self):
            return SparkyNPKParser.RULE_data_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_label" ):
                listener.enterData_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_label" ):
                listener.exitData_label(self)




    def data_label(self):

        localctx = SparkyNPKParser.Data_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_data_label)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7170) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 65
            self.match(SparkyNPKParser.W1_LA)
            self.state = 66
            self.match(SparkyNPKParser.W2_LA)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 67
                self.match(SparkyNPKParser.W3_LA)


            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 70
                self.match(SparkyNPKParser.W4_LA)


            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 73
                self.match(SparkyNPKParser.W1_Hz_LA)


            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 76
                self.match(SparkyNPKParser.W2_Hz_LA)


            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 79
                self.match(SparkyNPKParser.W3_Hz_LA)


            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 82
                self.match(SparkyNPKParser.W4_Hz_LA)


            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 85
                self.match(SparkyNPKParser.Dev_w1_LA)


            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 88
                self.match(SparkyNPKParser.Dev_w2_LA)


            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 91
                self.match(SparkyNPKParser.Dev_w3_LA)


            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 94
                self.match(SparkyNPKParser.Dev_w4_LA)


            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 97
                    self.match(SparkyNPKParser.Dummy_H_LA)


                self.state = 100
                self.match(SparkyNPKParser.Height_LA)

            elif la_ == 2:
                self.state = 101
                self.match(SparkyNPKParser.Volume_LA)


            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39, 40]:
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 104
                    self.match(SparkyNPKParser.Dummy_H_LA)


                self.state = 107
                self.match(SparkyNPKParser.Height_LA)
                pass
            elif token in [41]:
                self.state = 108
                self.match(SparkyNPKParser.Volume_LA)
                pass
            elif token in [27, 28, 29, 30, 42, 43, 44, 45, 46, 47, 48, 49, 51]:
                pass
            else:
                pass
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 111
                self.match(SparkyNPKParser.Dummy_Rms_LA)


            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 114
                self.match(SparkyNPKParser.S_N_LA)


            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 117
                self.match(SparkyNPKParser.Lw1_Hz_LA)


            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 120
                self.match(SparkyNPKParser.Lw2_Hz_LA)


            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 123
                self.match(SparkyNPKParser.Lw3_Hz_LA)


            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 126
                self.match(SparkyNPKParser.Lw4_Hz_LA)


            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 129
                self.match(SparkyNPKParser.Atom1_LA)


            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 132
                self.match(SparkyNPKParser.Atom2_LA)


            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 135
                self.match(SparkyNPKParser.Atom3_LA)


            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 138
                self.match(SparkyNPKParser.Atom4_LA)


            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 141
                self.match(SparkyNPKParser.Distance_LA)


            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 144
                self.match(SparkyNPKParser.Note_LA)


            self.state = 147
            self.match(SparkyNPKParser.RETURN_LA)
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 148
                self.match(SparkyNPKParser.RETURN)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Peak_2dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Assignment_2d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_2d_ex, 0)

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.PositionContext,i)


        def RETURN(self):
            return self.getToken(SparkyNPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyNPKParser.EOF, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.NumberContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.NoteContext,i)


        def getRuleIndex(self):
            return SparkyNPKParser.RULE_peak_2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_2d" ):
                listener.enterPeak_2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_2d" ):
                listener.exitPeak_2d(self)




    def peak_2d(self):

        localctx = SparkyNPKParser.Peak_2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_peak_2d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(SparkyNPKParser.Assignment_2d_ex)
            self.state = 152
            self.position()
            self.state = 153
            self.position()
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 154
                    self.number() 
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 253976) != 0):
                self.state = 160
                self.note()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
            _la = self._input.LA(1)
            if not(_la==-1 or _la==19):
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


    class Peak_3dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Assignment_3d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_3d_ex, 0)

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.PositionContext,i)


        def RETURN(self):
            return self.getToken(SparkyNPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyNPKParser.EOF, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.NumberContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.NoteContext,i)


        def getRuleIndex(self):
            return SparkyNPKParser.RULE_peak_3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_3d" ):
                listener.enterPeak_3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_3d" ):
                listener.exitPeak_3d(self)




    def peak_3d(self):

        localctx = SparkyNPKParser.Peak_3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_peak_3d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(SparkyNPKParser.Assignment_3d_ex)
            self.state = 169
            self.position()
            self.state = 170
            self.position()
            self.state = 171
            self.position()
            self.state = 175
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 172
                    self.number() 
                self.state = 177
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 253976) != 0):
                self.state = 178
                self.note()
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 184
            _la = self._input.LA(1)
            if not(_la==-1 or _la==19):
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


    class Peak_4dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Assignment_4d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_4d_ex, 0)

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.PositionContext,i)


        def RETURN(self):
            return self.getToken(SparkyNPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyNPKParser.EOF, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.NumberContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.NoteContext,i)


        def getRuleIndex(self):
            return SparkyNPKParser.RULE_peak_4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_4d" ):
                listener.enterPeak_4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_4d" ):
                listener.exitPeak_4d(self)




    def peak_4d(self):

        localctx = SparkyNPKParser.Peak_4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_peak_4d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(SparkyNPKParser.Assignment_4d_ex)
            self.state = 187
            self.position()
            self.state = 188
            self.position()
            self.state = 189
            self.position()
            self.state = 193
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 190
                    self.number() 
                self.state = 195
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 253976) != 0):
                self.state = 196
                self.note()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 202
            _la = self._input.LA(1)
            if not(_la==-1 or _la==19):
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


    class Peak_2d_poContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.PositionContext,i)


        def Assignment_2d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_2d_ex, 0)

        def Assignment_3d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_3d_ex, 0)

        def Assignment_4d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_4d_ex, 0)

        def RETURN(self):
            return self.getToken(SparkyNPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyNPKParser.EOF, 0)

        def getRuleIndex(self):
            return SparkyNPKParser.RULE_peak_2d_po

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_2d_po" ):
                listener.enterPeak_2d_po(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_2d_po" ):
                listener.exitPeak_2d_po(self)




    def peak_2d_po(self):

        localctx = SparkyNPKParser.Peak_2d_poContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_peak_2d_po)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 205
            self.position()
            self.state = 206
            self.position()
            self.state = 207
            _la = self._input.LA(1)
            if not(_la==-1 or _la==19):
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


    class Peak_3d_poContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.PositionContext,i)


        def Assignment_3d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_3d_ex, 0)

        def Assignment_4d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_4d_ex, 0)

        def RETURN(self):
            return self.getToken(SparkyNPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyNPKParser.EOF, 0)

        def getRuleIndex(self):
            return SparkyNPKParser.RULE_peak_3d_po

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_3d_po" ):
                listener.enterPeak_3d_po(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_3d_po" ):
                listener.exitPeak_3d_po(self)




    def peak_3d_po(self):

        localctx = SparkyNPKParser.Peak_3d_poContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_peak_3d_po)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 210
            self.position()
            self.state = 211
            self.position()
            self.state = 212
            self.position()
            self.state = 213
            _la = self._input.LA(1)
            if not(_la==-1 or _la==19):
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


    class Peak_4d_poContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Assignment_4d_ex(self):
            return self.getToken(SparkyNPKParser.Assignment_4d_ex, 0)

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyNPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(SparkyNPKParser.PositionContext,i)


        def RETURN(self):
            return self.getToken(SparkyNPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyNPKParser.EOF, 0)

        def getRuleIndex(self):
            return SparkyNPKParser.RULE_peak_4d_po

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_4d_po" ):
                listener.enterPeak_4d_po(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_4d_po" ):
                listener.exitPeak_4d_po(self)




    def peak_4d_po(self):

        localctx = SparkyNPKParser.Peak_4d_poContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_peak_4d_po)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(SparkyNPKParser.Assignment_4d_ex)
            self.state = 216
            self.position()
            self.state = 217
            self.position()
            self.state = 218
            self.position()
            self.state = 219
            _la = self._input.LA(1)
            if not(_la==-1 or _la==19):
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


    class PositionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Float(self):
            return self.getToken(SparkyNPKParser.Float, 0)

        def Integer(self):
            return self.getToken(SparkyNPKParser.Integer, 0)

        def getRuleIndex(self):
            return SparkyNPKParser.RULE_position

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPosition" ):
                listener.enterPosition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPosition" ):
                listener.exitPosition(self)




    def position(self):

        localctx = SparkyNPKParser.PositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_position)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
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


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Real_vol(self):
            return self.getToken(SparkyNPKParser.Real_vol, 0)

        def Real(self):
            return self.getToken(SparkyNPKParser.Real, 0)

        def Float(self):
            return self.getToken(SparkyNPKParser.Float, 0)

        def Integer(self):
            return self.getToken(SparkyNPKParser.Integer, 0)

        def getRuleIndex(self):
            return SparkyNPKParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = SparkyNPKParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0)):
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


    class NoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Simple_name(self):
            return self.getToken(SparkyNPKParser.Simple_name, 0)

        def Integer(self):
            return self.getToken(SparkyNPKParser.Integer, 0)

        def Float(self):
            return self.getToken(SparkyNPKParser.Float, 0)

        def Note_2d_ex(self):
            return self.getToken(SparkyNPKParser.Note_2d_ex, 0)

        def Note_3d_ex(self):
            return self.getToken(SparkyNPKParser.Note_3d_ex, 0)

        def Note_4d_ex(self):
            return self.getToken(SparkyNPKParser.Note_4d_ex, 0)

        def Note_ex(self):
            return self.getToken(SparkyNPKParser.Note_ex, 0)

        def getRuleIndex(self):
            return SparkyNPKParser.RULE_note

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNote" ):
                listener.enterNote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNote" ):
                listener.exitNote(self)




    def note(self):

        localctx = SparkyNPKParser.NoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_note)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 253976) != 0)):
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





