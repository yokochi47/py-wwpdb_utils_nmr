# Generated from SparkyRPKParser.g4 by ANTLR 4.13.0
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
        4,1,51,272,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,3,0,22,8,0,1,0,1,0,1,0,4,0,27,8,0,
        11,0,12,0,28,1,0,4,0,32,8,0,11,0,12,0,33,1,0,4,0,37,8,0,11,0,12,
        0,38,1,0,5,0,42,8,0,10,0,12,0,45,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,
        53,8,1,1,1,3,1,56,8,1,1,1,3,1,59,8,1,1,1,3,1,62,8,1,1,1,3,1,65,8,
        1,1,1,3,1,68,8,1,1,1,3,1,71,8,1,1,1,3,1,74,8,1,1,1,3,1,77,8,1,1,
        1,3,1,80,8,1,1,1,3,1,83,8,1,1,1,3,1,86,8,1,1,1,3,1,89,8,1,1,1,3,
        1,92,8,1,1,1,3,1,95,8,1,1,1,3,1,98,8,1,1,1,3,1,101,8,1,1,1,3,1,104,
        8,1,1,1,3,1,107,8,1,1,1,3,1,110,8,1,1,1,3,1,113,8,1,1,1,3,1,116,
        8,1,1,1,3,1,119,8,1,1,1,3,1,122,8,1,1,1,3,1,125,8,1,1,1,1,1,3,1,
        129,8,1,1,2,1,2,1,2,3,2,134,8,2,1,2,3,2,137,8,2,1,2,3,2,140,8,2,
        1,2,3,2,143,8,2,1,2,3,2,146,8,2,1,2,3,2,149,8,2,1,2,3,2,152,8,2,
        1,2,3,2,155,8,2,1,2,3,2,158,8,2,1,2,3,2,161,8,2,1,2,3,2,164,8,2,
        1,2,3,2,167,8,2,1,2,3,2,170,8,2,1,2,3,2,173,8,2,1,2,3,2,176,8,2,
        1,2,3,2,179,8,2,1,2,3,2,182,8,2,1,2,3,2,185,8,2,1,2,3,2,188,8,2,
        1,2,3,2,191,8,2,1,2,3,2,194,8,2,1,2,1,2,3,2,198,8,2,1,2,4,2,201,
        8,2,11,2,12,2,202,1,3,1,3,1,3,1,3,4,3,209,8,3,11,3,12,3,210,1,3,
        5,3,214,8,3,10,3,12,3,217,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,4,4,226,
        8,4,11,4,12,4,227,1,4,5,4,231,8,4,10,4,12,4,234,9,4,1,4,1,4,1,5,
        1,5,1,5,1,5,1,5,1,5,4,5,244,8,5,11,5,12,5,245,1,5,5,5,249,8,5,10,
        5,12,5,252,9,5,1,5,1,5,1,6,4,6,257,8,6,11,6,12,6,258,1,6,3,6,262,
        8,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,
        16,18,0,5,2,0,1,1,10,12,1,1,19,19,1,0,3,4,1,0,3,6,2,0,3,4,13,17,
        328,0,21,1,0,0,0,2,48,1,0,0,0,4,130,1,0,0,0,6,204,1,0,0,0,8,220,
        1,0,0,0,10,237,1,0,0,0,12,256,1,0,0,0,14,265,1,0,0,0,16,267,1,0,
        0,0,18,269,1,0,0,0,20,22,5,19,0,0,21,20,1,0,0,0,21,22,1,0,0,0,22,
        43,1,0,0,0,23,42,3,2,1,0,24,42,3,4,2,0,25,27,3,6,3,0,26,25,1,0,0,
        0,27,28,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,42,1,0,0,0,30,32,
        3,8,4,0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,
        34,42,1,0,0,0,35,37,3,10,5,0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,1,
        0,0,0,38,39,1,0,0,0,39,42,1,0,0,0,40,42,5,19,0,0,41,23,1,0,0,0,41,
        24,1,0,0,0,41,26,1,0,0,0,41,31,1,0,0,0,41,36,1,0,0,0,41,40,1,0,0,
        0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,43,
        1,0,0,0,46,47,5,0,0,1,47,1,1,0,0,0,48,49,7,0,0,0,49,50,5,31,0,0,
        50,52,5,32,0,0,51,53,5,33,0,0,52,51,1,0,0,0,52,53,1,0,0,0,53,55,
        1,0,0,0,54,56,5,34,0,0,55,54,1,0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,
        57,59,5,23,0,0,58,57,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,0,60,62,5,
        24,0,0,61,60,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,65,5,25,0,0,
        64,63,1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,68,5,26,0,0,67,66,1,
        0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,71,5,35,0,0,70,69,1,0,0,0,70,
        71,1,0,0,0,71,73,1,0,0,0,72,74,5,36,0,0,73,72,1,0,0,0,73,74,1,0,
        0,0,74,76,1,0,0,0,75,77,5,37,0,0,76,75,1,0,0,0,76,77,1,0,0,0,77,
        79,1,0,0,0,78,80,5,38,0,0,79,78,1,0,0,0,79,80,1,0,0,0,80,82,1,0,
        0,0,81,83,5,41,0,0,82,81,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,
        86,5,42,0,0,85,84,1,0,0,0,85,86,1,0,0,0,86,88,1,0,0,0,87,89,5,39,
        0,0,88,87,1,0,0,0,88,89,1,0,0,0,89,91,1,0,0,0,90,92,5,40,0,0,91,
        90,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,95,5,43,0,0,94,93,1,0,
        0,0,94,95,1,0,0,0,95,97,1,0,0,0,96,98,5,27,0,0,97,96,1,0,0,0,97,
        98,1,0,0,0,98,100,1,0,0,0,99,101,5,28,0,0,100,99,1,0,0,0,100,101,
        1,0,0,0,101,103,1,0,0,0,102,104,5,29,0,0,103,102,1,0,0,0,103,104,
        1,0,0,0,104,106,1,0,0,0,105,107,5,30,0,0,106,105,1,0,0,0,106,107,
        1,0,0,0,107,109,1,0,0,0,108,110,5,44,0,0,109,108,1,0,0,0,109,110,
        1,0,0,0,110,112,1,0,0,0,111,113,5,45,0,0,112,111,1,0,0,0,112,113,
        1,0,0,0,113,115,1,0,0,0,114,116,5,46,0,0,115,114,1,0,0,0,115,116,
        1,0,0,0,116,118,1,0,0,0,117,119,5,47,0,0,118,117,1,0,0,0,118,119,
        1,0,0,0,119,121,1,0,0,0,120,122,5,48,0,0,121,120,1,0,0,0,121,122,
        1,0,0,0,122,124,1,0,0,0,123,125,5,49,0,0,124,123,1,0,0,0,124,125,
        1,0,0,0,125,126,1,0,0,0,126,128,5,51,0,0,127,129,5,19,0,0,128,127,
        1,0,0,0,128,129,1,0,0,0,129,3,1,0,0,0,130,131,5,2,0,0,131,133,5,
        32,0,0,132,134,5,33,0,0,133,132,1,0,0,0,133,134,1,0,0,0,134,136,
        1,0,0,0,135,137,5,34,0,0,136,135,1,0,0,0,136,137,1,0,0,0,137,139,
        1,0,0,0,138,140,5,23,0,0,139,138,1,0,0,0,139,140,1,0,0,0,140,142,
        1,0,0,0,141,143,5,24,0,0,142,141,1,0,0,0,142,143,1,0,0,0,143,145,
        1,0,0,0,144,146,5,25,0,0,145,144,1,0,0,0,145,146,1,0,0,0,146,148,
        1,0,0,0,147,149,5,26,0,0,148,147,1,0,0,0,148,149,1,0,0,0,149,151,
        1,0,0,0,150,152,5,35,0,0,151,150,1,0,0,0,151,152,1,0,0,0,152,154,
        1,0,0,0,153,155,5,36,0,0,154,153,1,0,0,0,154,155,1,0,0,0,155,157,
        1,0,0,0,156,158,5,37,0,0,157,156,1,0,0,0,157,158,1,0,0,0,158,160,
        1,0,0,0,159,161,5,38,0,0,160,159,1,0,0,0,160,161,1,0,0,0,161,163,
        1,0,0,0,162,164,5,41,0,0,163,162,1,0,0,0,163,164,1,0,0,0,164,166,
        1,0,0,0,165,167,5,42,0,0,166,165,1,0,0,0,166,167,1,0,0,0,167,169,
        1,0,0,0,168,170,5,39,0,0,169,168,1,0,0,0,169,170,1,0,0,0,170,172,
        1,0,0,0,171,173,5,40,0,0,172,171,1,0,0,0,172,173,1,0,0,0,173,175,
        1,0,0,0,174,176,5,43,0,0,175,174,1,0,0,0,175,176,1,0,0,0,176,178,
        1,0,0,0,177,179,5,27,0,0,178,177,1,0,0,0,178,179,1,0,0,0,179,181,
        1,0,0,0,180,182,5,28,0,0,181,180,1,0,0,0,181,182,1,0,0,0,182,184,
        1,0,0,0,183,185,5,29,0,0,184,183,1,0,0,0,184,185,1,0,0,0,185,187,
        1,0,0,0,186,188,5,30,0,0,187,186,1,0,0,0,187,188,1,0,0,0,188,190,
        1,0,0,0,189,191,5,48,0,0,190,189,1,0,0,0,190,191,1,0,0,0,191,193,
        1,0,0,0,192,194,5,49,0,0,193,192,1,0,0,0,193,194,1,0,0,0,194,195,
        1,0,0,0,195,197,5,51,0,0,196,198,5,19,0,0,197,196,1,0,0,0,197,198,
        1,0,0,0,198,200,1,0,0,0,199,201,3,12,6,0,200,199,1,0,0,0,201,202,
        1,0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,203,5,1,0,0,0,204,205,5,
        10,0,0,205,206,3,14,7,0,206,208,3,14,7,0,207,209,3,16,8,0,208,207,
        1,0,0,0,209,210,1,0,0,0,210,208,1,0,0,0,210,211,1,0,0,0,211,215,
        1,0,0,0,212,214,3,18,9,0,213,212,1,0,0,0,214,217,1,0,0,0,215,213,
        1,0,0,0,215,216,1,0,0,0,216,218,1,0,0,0,217,215,1,0,0,0,218,219,
        7,1,0,0,219,7,1,0,0,0,220,221,5,11,0,0,221,222,3,14,7,0,222,223,
        3,14,7,0,223,225,3,14,7,0,224,226,3,16,8,0,225,224,1,0,0,0,226,227,
        1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,232,1,0,0,0,229,231,
        3,18,9,0,230,229,1,0,0,0,231,234,1,0,0,0,232,230,1,0,0,0,232,233,
        1,0,0,0,233,235,1,0,0,0,234,232,1,0,0,0,235,236,7,1,0,0,236,9,1,
        0,0,0,237,238,5,12,0,0,238,239,3,14,7,0,239,240,3,14,7,0,240,241,
        3,14,7,0,241,243,3,14,7,0,242,244,3,16,8,0,243,242,1,0,0,0,244,245,
        1,0,0,0,245,243,1,0,0,0,245,246,1,0,0,0,246,250,1,0,0,0,247,249,
        3,18,9,0,248,247,1,0,0,0,249,252,1,0,0,0,250,248,1,0,0,0,250,251,
        1,0,0,0,251,253,1,0,0,0,252,250,1,0,0,0,253,254,7,1,0,0,254,11,1,
        0,0,0,255,257,3,16,8,0,256,255,1,0,0,0,257,258,1,0,0,0,258,256,1,
        0,0,0,258,259,1,0,0,0,259,261,1,0,0,0,260,262,3,18,9,0,261,260,1,
        0,0,0,261,262,1,0,0,0,262,263,1,0,0,0,263,264,7,1,0,0,264,13,1,0,
        0,0,265,266,7,2,0,0,266,15,1,0,0,0,267,268,7,3,0,0,268,17,1,0,0,
        0,269,270,7,4,0,0,270,19,1,0,0,0,63,21,28,33,38,41,43,52,55,58,61,
        64,67,70,73,76,79,82,85,88,91,94,97,100,103,106,109,112,115,118,
        121,124,128,133,136,139,142,145,148,151,154,157,160,163,166,169,
        172,175,178,181,184,187,190,193,197,202,210,215,227,232,245,250,
        258,261
    ]

class SparkyRPKParser ( Parser ):

    grammarFileName = "SparkyRPKParser.g4"

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

    RULE_sparky_rpk = 0
    RULE_data_label = 1
    RULE_data_label_wo_assign = 2
    RULE_peak_2d = 3
    RULE_peak_3d = 4
    RULE_peak_4d = 5
    RULE_peak_wo_assign = 6
    RULE_position = 7
    RULE_number = 8
    RULE_note = 9

    ruleNames =  [ "sparky_rpk", "data_label", "data_label_wo_assign", "peak_2d", 
                   "peak_3d", "peak_4d", "peak_wo_assign", "position", "number", 
                   "note" ]

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




    class Sparky_rpkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SparkyRPKParser.EOF, 0)

        def RETURN(self, i:int=None):
            if i is None:
                return self.getTokens(SparkyRPKParser.RETURN)
            else:
                return self.getToken(SparkyRPKParser.RETURN, i)

        def data_label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.Data_labelContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.Data_labelContext,i)


        def data_label_wo_assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.Data_label_wo_assignContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.Data_label_wo_assignContext,i)


        def peak_2d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.Peak_2dContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.Peak_2dContext,i)


        def peak_3d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.Peak_3dContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.Peak_3dContext,i)


        def peak_4d(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.Peak_4dContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.Peak_4dContext,i)


        def getRuleIndex(self):
            return SparkyRPKParser.RULE_sparky_rpk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSparky_rpk" ):
                listener.enterSparky_rpk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSparky_rpk" ):
                listener.exitSparky_rpk(self)




    def sparky_rpk(self):

        localctx = SparkyRPKParser.Sparky_rpkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sparky_rpk)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 20
                self.match(SparkyRPKParser.RETURN)


            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 531462) != 0):
                self.state = 41
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 23
                    self.data_label()
                    pass

                elif la_ == 2:
                    self.state = 24
                    self.data_label_wo_assign()
                    pass

                elif la_ == 3:
                    self.state = 26 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 25
                            self.peak_2d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 28 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                    pass

                elif la_ == 4:
                    self.state = 31 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 30
                            self.peak_3d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 33 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                    pass

                elif la_ == 5:
                    self.state = 36 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 35
                            self.peak_4d()

                        else:
                            raise NoViableAltException(self)
                        self.state = 38 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                    pass

                elif la_ == 6:
                    self.state = 40
                    self.match(SparkyRPKParser.RETURN)
                    pass


                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(SparkyRPKParser.EOF)
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
            return self.getToken(SparkyRPKParser.W1_LA, 0)

        def W2_LA(self):
            return self.getToken(SparkyRPKParser.W2_LA, 0)

        def RETURN_LA(self):
            return self.getToken(SparkyRPKParser.RETURN_LA, 0)

        def Assignment(self):
            return self.getToken(SparkyRPKParser.Assignment, 0)

        def Assignment_2d_ex(self):
            return self.getToken(SparkyRPKParser.Assignment_2d_ex, 0)

        def Assignment_3d_ex(self):
            return self.getToken(SparkyRPKParser.Assignment_3d_ex, 0)

        def Assignment_4d_ex(self):
            return self.getToken(SparkyRPKParser.Assignment_4d_ex, 0)

        def W3_LA(self):
            return self.getToken(SparkyRPKParser.W3_LA, 0)

        def W4_LA(self):
            return self.getToken(SparkyRPKParser.W4_LA, 0)

        def W1_Hz_LA(self):
            return self.getToken(SparkyRPKParser.W1_Hz_LA, 0)

        def W2_Hz_LA(self):
            return self.getToken(SparkyRPKParser.W2_Hz_LA, 0)

        def W3_Hz_LA(self):
            return self.getToken(SparkyRPKParser.W3_Hz_LA, 0)

        def W4_Hz_LA(self):
            return self.getToken(SparkyRPKParser.W4_Hz_LA, 0)

        def Dev_w1_LA(self):
            return self.getToken(SparkyRPKParser.Dev_w1_LA, 0)

        def Dev_w2_LA(self):
            return self.getToken(SparkyRPKParser.Dev_w2_LA, 0)

        def Dev_w3_LA(self):
            return self.getToken(SparkyRPKParser.Dev_w3_LA, 0)

        def Dev_w4_LA(self):
            return self.getToken(SparkyRPKParser.Dev_w4_LA, 0)

        def Volume_LA(self):
            return self.getToken(SparkyRPKParser.Volume_LA, 0)

        def Dummy_Rms_LA(self):
            return self.getToken(SparkyRPKParser.Dummy_Rms_LA, 0)

        def Dummy_H_LA(self):
            return self.getToken(SparkyRPKParser.Dummy_H_LA, 0)

        def Height_LA(self):
            return self.getToken(SparkyRPKParser.Height_LA, 0)

        def S_N_LA(self):
            return self.getToken(SparkyRPKParser.S_N_LA, 0)

        def Lw1_Hz_LA(self):
            return self.getToken(SparkyRPKParser.Lw1_Hz_LA, 0)

        def Lw2_Hz_LA(self):
            return self.getToken(SparkyRPKParser.Lw2_Hz_LA, 0)

        def Lw3_Hz_LA(self):
            return self.getToken(SparkyRPKParser.Lw3_Hz_LA, 0)

        def Lw4_Hz_LA(self):
            return self.getToken(SparkyRPKParser.Lw4_Hz_LA, 0)

        def Atom1_LA(self):
            return self.getToken(SparkyRPKParser.Atom1_LA, 0)

        def Atom2_LA(self):
            return self.getToken(SparkyRPKParser.Atom2_LA, 0)

        def Atom3_LA(self):
            return self.getToken(SparkyRPKParser.Atom3_LA, 0)

        def Atom4_LA(self):
            return self.getToken(SparkyRPKParser.Atom4_LA, 0)

        def Distance_LA(self):
            return self.getToken(SparkyRPKParser.Distance_LA, 0)

        def Note_LA(self):
            return self.getToken(SparkyRPKParser.Note_LA, 0)

        def RETURN(self):
            return self.getToken(SparkyRPKParser.RETURN, 0)

        def getRuleIndex(self):
            return SparkyRPKParser.RULE_data_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_label" ):
                listener.enterData_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_label" ):
                listener.exitData_label(self)




    def data_label(self):

        localctx = SparkyRPKParser.Data_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_data_label)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7170) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 49
            self.match(SparkyRPKParser.W1_LA)
            self.state = 50
            self.match(SparkyRPKParser.W2_LA)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 51
                self.match(SparkyRPKParser.W3_LA)


            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 54
                self.match(SparkyRPKParser.W4_LA)


            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 57
                self.match(SparkyRPKParser.W1_Hz_LA)


            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 60
                self.match(SparkyRPKParser.W2_Hz_LA)


            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 63
                self.match(SparkyRPKParser.W3_Hz_LA)


            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 66
                self.match(SparkyRPKParser.W4_Hz_LA)


            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 69
                self.match(SparkyRPKParser.Dev_w1_LA)


            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 72
                self.match(SparkyRPKParser.Dev_w2_LA)


            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 75
                self.match(SparkyRPKParser.Dev_w3_LA)


            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 78
                self.match(SparkyRPKParser.Dev_w4_LA)


            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 81
                self.match(SparkyRPKParser.Volume_LA)


            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 84
                self.match(SparkyRPKParser.Dummy_Rms_LA)


            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 87
                self.match(SparkyRPKParser.Dummy_H_LA)


            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 90
                self.match(SparkyRPKParser.Height_LA)


            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 93
                self.match(SparkyRPKParser.S_N_LA)


            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 96
                self.match(SparkyRPKParser.Lw1_Hz_LA)


            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 99
                self.match(SparkyRPKParser.Lw2_Hz_LA)


            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 102
                self.match(SparkyRPKParser.Lw3_Hz_LA)


            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 105
                self.match(SparkyRPKParser.Lw4_Hz_LA)


            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 108
                self.match(SparkyRPKParser.Atom1_LA)


            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 111
                self.match(SparkyRPKParser.Atom2_LA)


            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 114
                self.match(SparkyRPKParser.Atom3_LA)


            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 117
                self.match(SparkyRPKParser.Atom4_LA)


            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 120
                self.match(SparkyRPKParser.Distance_LA)


            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 123
                self.match(SparkyRPKParser.Note_LA)


            self.state = 126
            self.match(SparkyRPKParser.RETURN_LA)
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 127
                self.match(SparkyRPKParser.RETURN)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_label_wo_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def W1(self):
            return self.getToken(SparkyRPKParser.W1, 0)

        def W2_LA(self):
            return self.getToken(SparkyRPKParser.W2_LA, 0)

        def RETURN_LA(self):
            return self.getToken(SparkyRPKParser.RETURN_LA, 0)

        def W3_LA(self):
            return self.getToken(SparkyRPKParser.W3_LA, 0)

        def W4_LA(self):
            return self.getToken(SparkyRPKParser.W4_LA, 0)

        def W1_Hz_LA(self):
            return self.getToken(SparkyRPKParser.W1_Hz_LA, 0)

        def W2_Hz_LA(self):
            return self.getToken(SparkyRPKParser.W2_Hz_LA, 0)

        def W3_Hz_LA(self):
            return self.getToken(SparkyRPKParser.W3_Hz_LA, 0)

        def W4_Hz_LA(self):
            return self.getToken(SparkyRPKParser.W4_Hz_LA, 0)

        def Dev_w1_LA(self):
            return self.getToken(SparkyRPKParser.Dev_w1_LA, 0)

        def Dev_w2_LA(self):
            return self.getToken(SparkyRPKParser.Dev_w2_LA, 0)

        def Dev_w3_LA(self):
            return self.getToken(SparkyRPKParser.Dev_w3_LA, 0)

        def Dev_w4_LA(self):
            return self.getToken(SparkyRPKParser.Dev_w4_LA, 0)

        def Volume_LA(self):
            return self.getToken(SparkyRPKParser.Volume_LA, 0)

        def Dummy_Rms_LA(self):
            return self.getToken(SparkyRPKParser.Dummy_Rms_LA, 0)

        def Dummy_H_LA(self):
            return self.getToken(SparkyRPKParser.Dummy_H_LA, 0)

        def Height_LA(self):
            return self.getToken(SparkyRPKParser.Height_LA, 0)

        def S_N_LA(self):
            return self.getToken(SparkyRPKParser.S_N_LA, 0)

        def Lw1_Hz_LA(self):
            return self.getToken(SparkyRPKParser.Lw1_Hz_LA, 0)

        def Lw2_Hz_LA(self):
            return self.getToken(SparkyRPKParser.Lw2_Hz_LA, 0)

        def Lw3_Hz_LA(self):
            return self.getToken(SparkyRPKParser.Lw3_Hz_LA, 0)

        def Lw4_Hz_LA(self):
            return self.getToken(SparkyRPKParser.Lw4_Hz_LA, 0)

        def Distance_LA(self):
            return self.getToken(SparkyRPKParser.Distance_LA, 0)

        def Note_LA(self):
            return self.getToken(SparkyRPKParser.Note_LA, 0)

        def RETURN(self):
            return self.getToken(SparkyRPKParser.RETURN, 0)

        def peak_wo_assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.Peak_wo_assignContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.Peak_wo_assignContext,i)


        def getRuleIndex(self):
            return SparkyRPKParser.RULE_data_label_wo_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_label_wo_assign" ):
                listener.enterData_label_wo_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_label_wo_assign" ):
                listener.exitData_label_wo_assign(self)




    def data_label_wo_assign(self):

        localctx = SparkyRPKParser.Data_label_wo_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_data_label_wo_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(SparkyRPKParser.W1)
            self.state = 131
            self.match(SparkyRPKParser.W2_LA)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 132
                self.match(SparkyRPKParser.W3_LA)


            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 135
                self.match(SparkyRPKParser.W4_LA)


            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 138
                self.match(SparkyRPKParser.W1_Hz_LA)


            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 141
                self.match(SparkyRPKParser.W2_Hz_LA)


            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 144
                self.match(SparkyRPKParser.W3_Hz_LA)


            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 147
                self.match(SparkyRPKParser.W4_Hz_LA)


            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 150
                self.match(SparkyRPKParser.Dev_w1_LA)


            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 153
                self.match(SparkyRPKParser.Dev_w2_LA)


            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 156
                self.match(SparkyRPKParser.Dev_w3_LA)


            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 159
                self.match(SparkyRPKParser.Dev_w4_LA)


            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 162
                self.match(SparkyRPKParser.Volume_LA)


            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 165
                self.match(SparkyRPKParser.Dummy_Rms_LA)


            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 168
                self.match(SparkyRPKParser.Dummy_H_LA)


            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 171
                self.match(SparkyRPKParser.Height_LA)


            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 174
                self.match(SparkyRPKParser.S_N_LA)


            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 177
                self.match(SparkyRPKParser.Lw1_Hz_LA)


            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 180
                self.match(SparkyRPKParser.Lw2_Hz_LA)


            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 183
                self.match(SparkyRPKParser.Lw3_Hz_LA)


            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 186
                self.match(SparkyRPKParser.Lw4_Hz_LA)


            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 189
                self.match(SparkyRPKParser.Distance_LA)


            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 192
                self.match(SparkyRPKParser.Note_LA)


            self.state = 195
            self.match(SparkyRPKParser.RETURN_LA)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 196
                self.match(SparkyRPKParser.RETURN)


            self.state = 200 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 199
                self.peak_wo_assign()
                self.state = 202 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0)):
                    break

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
            return self.getToken(SparkyRPKParser.Assignment_2d_ex, 0)

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.PositionContext,i)


        def RETURN(self):
            return self.getToken(SparkyRPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyRPKParser.EOF, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.NumberContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.NoteContext,i)


        def getRuleIndex(self):
            return SparkyRPKParser.RULE_peak_2d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_2d" ):
                listener.enterPeak_2d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_2d" ):
                listener.exitPeak_2d(self)




    def peak_2d(self):

        localctx = SparkyRPKParser.Peak_2dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_peak_2d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(SparkyRPKParser.Assignment_2d_ex)
            self.state = 205
            self.position()
            self.state = 206
            self.position()
            self.state = 208 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 207
                    self.number()

                else:
                    raise NoViableAltException(self)
                self.state = 210 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 253976) != 0):
                self.state = 212
                self.note()
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 218
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
            return self.getToken(SparkyRPKParser.Assignment_3d_ex, 0)

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.PositionContext,i)


        def RETURN(self):
            return self.getToken(SparkyRPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyRPKParser.EOF, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.NumberContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.NoteContext,i)


        def getRuleIndex(self):
            return SparkyRPKParser.RULE_peak_3d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_3d" ):
                listener.enterPeak_3d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_3d" ):
                listener.exitPeak_3d(self)




    def peak_3d(self):

        localctx = SparkyRPKParser.Peak_3dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_peak_3d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(SparkyRPKParser.Assignment_3d_ex)
            self.state = 221
            self.position()
            self.state = 222
            self.position()
            self.state = 223
            self.position()
            self.state = 225 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 224
                    self.number()

                else:
                    raise NoViableAltException(self)
                self.state = 227 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 253976) != 0):
                self.state = 229
                self.note()
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 235
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
            return self.getToken(SparkyRPKParser.Assignment_4d_ex, 0)

        def position(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.PositionContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.PositionContext,i)


        def RETURN(self):
            return self.getToken(SparkyRPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyRPKParser.EOF, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.NumberContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.NoteContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.NoteContext,i)


        def getRuleIndex(self):
            return SparkyRPKParser.RULE_peak_4d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_4d" ):
                listener.enterPeak_4d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_4d" ):
                listener.exitPeak_4d(self)




    def peak_4d(self):

        localctx = SparkyRPKParser.Peak_4dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_peak_4d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(SparkyRPKParser.Assignment_4d_ex)
            self.state = 238
            self.position()
            self.state = 239
            self.position()
            self.state = 240
            self.position()
            self.state = 241
            self.position()
            self.state = 243 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 242
                    self.number()

                else:
                    raise NoViableAltException(self)
                self.state = 245 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 253976) != 0):
                self.state = 247
                self.note()
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 253
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


    class Peak_wo_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(SparkyRPKParser.RETURN, 0)

        def EOF(self):
            return self.getToken(SparkyRPKParser.EOF, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SparkyRPKParser.NumberContext)
            else:
                return self.getTypedRuleContext(SparkyRPKParser.NumberContext,i)


        def note(self):
            return self.getTypedRuleContext(SparkyRPKParser.NoteContext,0)


        def getRuleIndex(self):
            return SparkyRPKParser.RULE_peak_wo_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeak_wo_assign" ):
                listener.enterPeak_wo_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeak_wo_assign" ):
                listener.exitPeak_wo_assign(self)




    def peak_wo_assign(self):

        localctx = SparkyRPKParser.Peak_wo_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_peak_wo_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 255
                    self.number()

                else:
                    raise NoViableAltException(self)
                self.state = 258 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)

            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 253976) != 0):
                self.state = 260
                self.note()


            self.state = 263
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
            return self.getToken(SparkyRPKParser.Float, 0)

        def Integer(self):
            return self.getToken(SparkyRPKParser.Integer, 0)

        def getRuleIndex(self):
            return SparkyRPKParser.RULE_position

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPosition" ):
                listener.enterPosition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPosition" ):
                listener.exitPosition(self)




    def position(self):

        localctx = SparkyRPKParser.PositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_position)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
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
            return self.getToken(SparkyRPKParser.Real_vol, 0)

        def Real(self):
            return self.getToken(SparkyRPKParser.Real, 0)

        def Float(self):
            return self.getToken(SparkyRPKParser.Float, 0)

        def Integer(self):
            return self.getToken(SparkyRPKParser.Integer, 0)

        def getRuleIndex(self):
            return SparkyRPKParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = SparkyRPKParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
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
            return self.getToken(SparkyRPKParser.Simple_name, 0)

        def Integer(self):
            return self.getToken(SparkyRPKParser.Integer, 0)

        def Float(self):
            return self.getToken(SparkyRPKParser.Float, 0)

        def Note_2d_ex(self):
            return self.getToken(SparkyRPKParser.Note_2d_ex, 0)

        def Note_3d_ex(self):
            return self.getToken(SparkyRPKParser.Note_3d_ex, 0)

        def Note_4d_ex(self):
            return self.getToken(SparkyRPKParser.Note_4d_ex, 0)

        def Note_ex(self):
            return self.getToken(SparkyRPKParser.Note_ex, 0)

        def getRuleIndex(self):
            return SparkyRPKParser.RULE_note

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNote" ):
                listener.enterNote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNote" ):
                listener.exitNote(self)




    def note(self):

        localctx = SparkyRPKParser.NoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_note)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
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





