# Generated from BiosymMRParser.g4 by ANTLR 4.13.0
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
        4,1,25,242,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,5,0,59,8,0,10,0,12,0,62,9,0,1,0,1,0,1,1,4,1,67,8,1,11,
        1,12,1,68,1,2,3,2,72,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,
        83,8,2,1,3,4,3,86,8,3,11,3,12,3,87,1,4,3,4,91,8,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,5,4,5,102,8,5,11,5,12,5,103,1,6,3,6,107,8,6,
        1,6,1,6,1,6,1,6,1,6,1,7,4,7,115,8,7,11,7,12,7,116,1,8,3,8,120,8,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,136,
        8,8,1,8,1,8,1,8,3,8,141,8,8,1,8,1,8,1,8,3,8,146,8,8,1,9,4,9,149,
        8,9,11,9,12,9,150,1,10,3,10,154,8,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,11,4,11,167,8,11,11,11,12,11,168,1,12,3,
        12,172,8,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,4,13,182,8,13,
        11,13,12,13,183,1,14,3,14,187,8,14,1,14,1,14,1,14,1,15,4,15,193,
        8,15,11,15,12,15,194,1,16,3,16,198,8,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        3,22,231,8,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        0,0,24,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,0,3,1,0,1,3,1,0,21,22,2,0,16,16,23,23,248,0,60,1,0,0,0,
        2,66,1,0,0,0,4,71,1,0,0,0,6,85,1,0,0,0,8,90,1,0,0,0,10,101,1,0,0,
        0,12,106,1,0,0,0,14,114,1,0,0,0,16,119,1,0,0,0,18,148,1,0,0,0,20,
        153,1,0,0,0,22,166,1,0,0,0,24,171,1,0,0,0,26,181,1,0,0,0,28,186,
        1,0,0,0,30,192,1,0,0,0,32,197,1,0,0,0,34,205,1,0,0,0,36,207,1,0,
        0,0,38,209,1,0,0,0,40,211,1,0,0,0,42,215,1,0,0,0,44,223,1,0,0,0,
        46,234,1,0,0,0,48,59,3,2,1,0,49,59,3,6,3,0,50,59,3,10,5,0,51,59,
        3,14,7,0,52,59,3,18,9,0,53,59,3,22,11,0,54,59,3,26,13,0,55,59,3,
        30,15,0,56,59,3,34,17,0,57,59,3,38,19,0,58,48,1,0,0,0,58,49,1,0,
        0,0,58,50,1,0,0,0,58,51,1,0,0,0,58,52,1,0,0,0,58,53,1,0,0,0,58,54,
        1,0,0,0,58,55,1,0,0,0,58,56,1,0,0,0,58,57,1,0,0,0,59,62,1,0,0,0,
        60,58,1,0,0,0,60,61,1,0,0,0,61,63,1,0,0,0,62,60,1,0,0,0,63,64,5,
        0,0,1,64,1,1,0,0,0,65,67,3,4,2,0,66,65,1,0,0,0,67,68,1,0,0,0,68,
        66,1,0,0,0,68,69,1,0,0,0,69,3,1,0,0,0,70,72,5,10,0,0,71,70,1,0,0,
        0,71,72,1,0,0,0,72,73,1,0,0,0,73,74,5,9,0,0,74,75,5,9,0,0,75,76,
        3,36,18,0,76,77,3,36,18,0,77,78,3,36,18,0,78,79,3,36,18,0,79,80,
        3,36,18,0,80,82,3,36,18,0,81,83,3,36,18,0,82,81,1,0,0,0,82,83,1,
        0,0,0,83,5,1,0,0,0,84,86,3,8,4,0,85,84,1,0,0,0,86,87,1,0,0,0,87,
        85,1,0,0,0,87,88,1,0,0,0,88,7,1,0,0,0,89,91,5,10,0,0,90,89,1,0,0,
        0,90,91,1,0,0,0,91,92,1,0,0,0,92,93,5,9,0,0,93,94,5,9,0,0,94,95,
        3,36,18,0,95,96,3,36,18,0,96,97,3,36,18,0,97,98,3,36,18,0,98,99,
        3,36,18,0,99,9,1,0,0,0,100,102,3,12,6,0,101,100,1,0,0,0,102,103,
        1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,11,1,0,0,0,105,107,5,
        10,0,0,106,105,1,0,0,0,106,107,1,0,0,0,107,108,1,0,0,0,108,109,5,
        9,0,0,109,110,5,9,0,0,110,111,3,36,18,0,111,112,3,36,18,0,112,13,
        1,0,0,0,113,115,3,16,8,0,114,113,1,0,0,0,115,116,1,0,0,0,116,114,
        1,0,0,0,116,117,1,0,0,0,117,15,1,0,0,0,118,120,5,10,0,0,119,118,
        1,0,0,0,119,120,1,0,0,0,120,121,1,0,0,0,121,122,5,9,0,0,122,123,
        5,9,0,0,123,124,5,9,0,0,124,125,5,9,0,0,125,126,3,36,18,0,126,127,
        3,36,18,0,127,128,3,36,18,0,128,129,3,36,18,0,129,130,3,36,18,0,
        130,131,3,36,18,0,131,135,3,36,18,0,132,133,3,36,18,0,133,134,3,
        36,18,0,134,136,1,0,0,0,135,132,1,0,0,0,135,136,1,0,0,0,136,140,
        1,0,0,0,137,138,3,36,18,0,138,139,3,36,18,0,139,141,1,0,0,0,140,
        137,1,0,0,0,140,141,1,0,0,0,141,145,1,0,0,0,142,143,3,36,18,0,143,
        144,3,36,18,0,144,146,1,0,0,0,145,142,1,0,0,0,145,146,1,0,0,0,146,
        17,1,0,0,0,147,149,3,20,10,0,148,147,1,0,0,0,149,150,1,0,0,0,150,
        148,1,0,0,0,150,151,1,0,0,0,151,19,1,0,0,0,152,154,5,10,0,0,153,
        152,1,0,0,0,153,154,1,0,0,0,154,155,1,0,0,0,155,156,5,9,0,0,156,
        157,5,9,0,0,157,158,5,9,0,0,158,159,5,9,0,0,159,160,3,36,18,0,160,
        161,3,36,18,0,161,162,3,36,18,0,162,163,3,36,18,0,163,164,3,36,18,
        0,164,21,1,0,0,0,165,167,3,24,12,0,166,165,1,0,0,0,167,168,1,0,0,
        0,168,166,1,0,0,0,168,169,1,0,0,0,169,23,1,0,0,0,170,172,5,10,0,
        0,171,170,1,0,0,0,171,172,1,0,0,0,172,173,1,0,0,0,173,174,5,9,0,
        0,174,175,5,9,0,0,175,176,5,9,0,0,176,177,5,9,0,0,177,178,3,36,18,
        0,178,179,3,36,18,0,179,25,1,0,0,0,180,182,3,28,14,0,181,180,1,0,
        0,0,182,183,1,0,0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,27,1,0,0,
        0,185,187,5,10,0,0,186,185,1,0,0,0,186,187,1,0,0,0,187,188,1,0,0,
        0,188,189,5,9,0,0,189,190,5,8,0,0,190,29,1,0,0,0,191,193,3,32,16,
        0,192,191,1,0,0,0,193,194,1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,
        0,195,31,1,0,0,0,196,198,5,10,0,0,197,196,1,0,0,0,197,198,1,0,0,
        0,198,199,1,0,0,0,199,200,5,9,0,0,200,201,5,9,0,0,201,202,5,9,0,
        0,202,203,5,9,0,0,203,204,5,9,0,0,204,33,1,0,0,0,205,206,5,4,0,0,
        206,35,1,0,0,0,207,208,7,0,0,0,208,37,1,0,0,0,209,210,3,40,20,0,
        210,39,1,0,0,0,211,212,3,42,21,0,212,213,3,44,22,0,213,214,3,46,
        23,0,214,41,1,0,0,0,215,216,5,11,0,0,216,217,5,17,0,0,217,218,5,
        16,0,0,218,219,5,20,0,0,219,220,5,16,0,0,220,221,5,16,0,0,221,222,
        5,25,0,0,222,43,1,0,0,0,223,224,5,11,0,0,224,225,5,18,0,0,225,226,
        5,16,0,0,226,227,7,1,0,0,227,228,5,16,0,0,228,230,5,16,0,0,229,231,
        5,16,0,0,230,229,1,0,0,0,230,231,1,0,0,0,231,232,1,0,0,0,232,233,
        5,25,0,0,233,45,1,0,0,0,234,235,5,11,0,0,235,236,5,19,0,0,236,237,
        5,16,0,0,237,238,7,2,0,0,238,239,5,16,0,0,239,240,5,25,0,0,240,47,
        1,0,0,0,23,58,60,68,71,82,87,90,103,106,116,119,135,140,145,150,
        153,168,171,183,186,194,197,230
    ]

class BiosymMRParser ( Parser ):

    grammarFileName = "BiosymMRParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'restraint'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'create'", "'function'", "'target'", 
                     "'distance'", "'quadratic'", "'flatBottomed'", "'relative'" ]

    symbolicNames = [ "<INVALID>", "Integer", "Float", "Float_DecimalComma", 
                      "Real", "SHARP_COMMENT", "EXCLM_COMMENT", "SMCLN_COMMENT", 
                      "Chiral_code", "Atom_selection", "Ordinal", "Restraint", 
                      "SPACE", "ENCLOSE_COMMENT", "SECTION_COMMENT", "LINE_COMMENT", 
                      "Double_quote_string", "Create", "Function", "Target", 
                      "Distance", "Quadratic", "Flat_bottomed", "Relative", 
                      "SPACE_II", "RETURN_II" ]

    RULE_biosym_mr = 0
    RULE_distance_restraints = 1
    RULE_distance_restraint = 2
    RULE_distance_constraints = 3
    RULE_distance_constraint = 4
    RULE_distance_wo_w_constraints = 5
    RULE_distance_wo_w_constraint = 6
    RULE_dihedral_angle_restraints = 7
    RULE_dihedral_angle_restraint = 8
    RULE_dihedral_angle_constraints = 9
    RULE_dihedral_angle_constraint = 10
    RULE_dihedral_angle_wo_w_constraints = 11
    RULE_dihedral_angle_wo_w_constraint = 12
    RULE_chirality_constraints = 13
    RULE_chirality_constraint = 14
    RULE_prochirality_constraints = 15
    RULE_prochirality_constraint = 16
    RULE_mixing_time = 17
    RULE_number = 18
    RULE_ins_distance_restraints = 19
    RULE_ins_distance_restraint = 20
    RULE_decl_create = 21
    RULE_decl_function = 22
    RULE_decl_target = 23

    ruleNames =  [ "biosym_mr", "distance_restraints", "distance_restraint", 
                   "distance_constraints", "distance_constraint", "distance_wo_w_constraints", 
                   "distance_wo_w_constraint", "dihedral_angle_restraints", 
                   "dihedral_angle_restraint", "dihedral_angle_constraints", 
                   "dihedral_angle_constraint", "dihedral_angle_wo_w_constraints", 
                   "dihedral_angle_wo_w_constraint", "chirality_constraints", 
                   "chirality_constraint", "prochirality_constraints", "prochirality_constraint", 
                   "mixing_time", "number", "ins_distance_restraints", "ins_distance_restraint", 
                   "decl_create", "decl_function", "decl_target" ]

    EOF = Token.EOF
    Integer=1
    Float=2
    Float_DecimalComma=3
    Real=4
    SHARP_COMMENT=5
    EXCLM_COMMENT=6
    SMCLN_COMMENT=7
    Chiral_code=8
    Atom_selection=9
    Ordinal=10
    Restraint=11
    SPACE=12
    ENCLOSE_COMMENT=13
    SECTION_COMMENT=14
    LINE_COMMENT=15
    Double_quote_string=16
    Create=17
    Function=18
    Target=19
    Distance=20
    Quadratic=21
    Flat_bottomed=22
    Relative=23
    SPACE_II=24
    RETURN_II=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Biosym_mrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BiosymMRParser.EOF, 0)

        def distance_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Distance_restraintsContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Distance_restraintsContext,i)


        def distance_constraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Distance_constraintsContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Distance_constraintsContext,i)


        def distance_wo_w_constraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Distance_wo_w_constraintsContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Distance_wo_w_constraintsContext,i)


        def dihedral_angle_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Dihedral_angle_restraintsContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Dihedral_angle_restraintsContext,i)


        def dihedral_angle_constraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Dihedral_angle_constraintsContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Dihedral_angle_constraintsContext,i)


        def dihedral_angle_wo_w_constraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Dihedral_angle_wo_w_constraintsContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Dihedral_angle_wo_w_constraintsContext,i)


        def chirality_constraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Chirality_constraintsContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Chirality_constraintsContext,i)


        def prochirality_constraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Prochirality_constraintsContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Prochirality_constraintsContext,i)


        def mixing_time(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Mixing_timeContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Mixing_timeContext,i)


        def ins_distance_restraints(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Ins_distance_restraintsContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Ins_distance_restraintsContext,i)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_biosym_mr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBiosym_mr" ):
                listener.enterBiosym_mr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBiosym_mr" ):
                listener.exitBiosym_mr(self)




    def biosym_mr(self):

        localctx = BiosymMRParser.Biosym_mrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_biosym_mr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3600) != 0):
                self.state = 58
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 48
                    self.distance_restraints()
                    pass

                elif la_ == 2:
                    self.state = 49
                    self.distance_constraints()
                    pass

                elif la_ == 3:
                    self.state = 50
                    self.distance_wo_w_constraints()
                    pass

                elif la_ == 4:
                    self.state = 51
                    self.dihedral_angle_restraints()
                    pass

                elif la_ == 5:
                    self.state = 52
                    self.dihedral_angle_constraints()
                    pass

                elif la_ == 6:
                    self.state = 53
                    self.dihedral_angle_wo_w_constraints()
                    pass

                elif la_ == 7:
                    self.state = 54
                    self.chirality_constraints()
                    pass

                elif la_ == 8:
                    self.state = 55
                    self.prochirality_constraints()
                    pass

                elif la_ == 9:
                    self.state = 56
                    self.mixing_time()
                    pass

                elif la_ == 10:
                    self.state = 57
                    self.ins_distance_restraints()
                    pass


                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self.match(BiosymMRParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def distance_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Distance_restraintContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Distance_restraintContext,i)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_distance_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_restraints" ):
                listener.enterDistance_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_restraints" ):
                listener.exitDistance_restraints(self)




    def distance_restraints(self):

        localctx = BiosymMRParser.Distance_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_distance_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 65
                    self.distance_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 68 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Atom_selection(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Atom_selection)
            else:
                return self.getToken(BiosymMRParser.Atom_selection, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.NumberContext,i)


        def Ordinal(self):
            return self.getToken(BiosymMRParser.Ordinal, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_distance_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_restraint" ):
                listener.enterDistance_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_restraint" ):
                listener.exitDistance_restraint(self)




    def distance_restraint(self):

        localctx = BiosymMRParser.Distance_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_distance_restraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 70
                self.match(BiosymMRParser.Ordinal)


            self.state = 73
            self.match(BiosymMRParser.Atom_selection)
            self.state = 74
            self.match(BiosymMRParser.Atom_selection)
            self.state = 75
            self.number()
            self.state = 76
            self.number()
            self.state = 77
            self.number()
            self.state = 78
            self.number()
            self.state = 79
            self.number()
            self.state = 80
            self.number()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 81
                self.number()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_constraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def distance_constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Distance_constraintContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Distance_constraintContext,i)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_distance_constraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_constraints" ):
                listener.enterDistance_constraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_constraints" ):
                listener.exitDistance_constraints(self)




    def distance_constraints(self):

        localctx = BiosymMRParser.Distance_constraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_distance_constraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 84
                    self.distance_constraint()

                else:
                    raise NoViableAltException(self)
                self.state = 87 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_constraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Atom_selection(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Atom_selection)
            else:
                return self.getToken(BiosymMRParser.Atom_selection, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.NumberContext,i)


        def Ordinal(self):
            return self.getToken(BiosymMRParser.Ordinal, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_distance_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_constraint" ):
                listener.enterDistance_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_constraint" ):
                listener.exitDistance_constraint(self)




    def distance_constraint(self):

        localctx = BiosymMRParser.Distance_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_distance_constraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 89
                self.match(BiosymMRParser.Ordinal)


            self.state = 92
            self.match(BiosymMRParser.Atom_selection)
            self.state = 93
            self.match(BiosymMRParser.Atom_selection)
            self.state = 94
            self.number()
            self.state = 95
            self.number()
            self.state = 96
            self.number()
            self.state = 97
            self.number()
            self.state = 98
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_wo_w_constraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def distance_wo_w_constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Distance_wo_w_constraintContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Distance_wo_w_constraintContext,i)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_distance_wo_w_constraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_wo_w_constraints" ):
                listener.enterDistance_wo_w_constraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_wo_w_constraints" ):
                listener.exitDistance_wo_w_constraints(self)




    def distance_wo_w_constraints(self):

        localctx = BiosymMRParser.Distance_wo_w_constraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_distance_wo_w_constraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 100
                    self.distance_wo_w_constraint()

                else:
                    raise NoViableAltException(self)
                self.state = 103 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Distance_wo_w_constraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Atom_selection(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Atom_selection)
            else:
                return self.getToken(BiosymMRParser.Atom_selection, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.NumberContext,i)


        def Ordinal(self):
            return self.getToken(BiosymMRParser.Ordinal, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_distance_wo_w_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistance_wo_w_constraint" ):
                listener.enterDistance_wo_w_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistance_wo_w_constraint" ):
                listener.exitDistance_wo_w_constraint(self)




    def distance_wo_w_constraint(self):

        localctx = BiosymMRParser.Distance_wo_w_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_distance_wo_w_constraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 105
                self.match(BiosymMRParser.Ordinal)


            self.state = 108
            self.match(BiosymMRParser.Atom_selection)
            self.state = 109
            self.match(BiosymMRParser.Atom_selection)
            self.state = 110
            self.number()
            self.state = 111
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dihedral_angle_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dihedral_angle_restraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Dihedral_angle_restraintContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Dihedral_angle_restraintContext,i)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_dihedral_angle_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDihedral_angle_restraints" ):
                listener.enterDihedral_angle_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDihedral_angle_restraints" ):
                listener.exitDihedral_angle_restraints(self)




    def dihedral_angle_restraints(self):

        localctx = BiosymMRParser.Dihedral_angle_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dihedral_angle_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 113
                    self.dihedral_angle_restraint()

                else:
                    raise NoViableAltException(self)
                self.state = 116 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dihedral_angle_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Atom_selection(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Atom_selection)
            else:
                return self.getToken(BiosymMRParser.Atom_selection, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.NumberContext,i)


        def Ordinal(self):
            return self.getToken(BiosymMRParser.Ordinal, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_dihedral_angle_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDihedral_angle_restraint" ):
                listener.enterDihedral_angle_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDihedral_angle_restraint" ):
                listener.exitDihedral_angle_restraint(self)




    def dihedral_angle_restraint(self):

        localctx = BiosymMRParser.Dihedral_angle_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dihedral_angle_restraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 118
                self.match(BiosymMRParser.Ordinal)


            self.state = 121
            self.match(BiosymMRParser.Atom_selection)
            self.state = 122
            self.match(BiosymMRParser.Atom_selection)
            self.state = 123
            self.match(BiosymMRParser.Atom_selection)
            self.state = 124
            self.match(BiosymMRParser.Atom_selection)
            self.state = 125
            self.number()
            self.state = 126
            self.number()
            self.state = 127
            self.number()
            self.state = 128
            self.number()
            self.state = 129
            self.number()
            self.state = 130
            self.number()
            self.state = 131
            self.number()
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 132
                self.number()
                self.state = 133
                self.number()


            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 137
                self.number()
                self.state = 138
                self.number()


            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 142
                self.number()
                self.state = 143
                self.number()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dihedral_angle_constraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dihedral_angle_constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Dihedral_angle_constraintContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Dihedral_angle_constraintContext,i)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_dihedral_angle_constraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDihedral_angle_constraints" ):
                listener.enterDihedral_angle_constraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDihedral_angle_constraints" ):
                listener.exitDihedral_angle_constraints(self)




    def dihedral_angle_constraints(self):

        localctx = BiosymMRParser.Dihedral_angle_constraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_dihedral_angle_constraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 147
                    self.dihedral_angle_constraint()

                else:
                    raise NoViableAltException(self)
                self.state = 150 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dihedral_angle_constraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Atom_selection(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Atom_selection)
            else:
                return self.getToken(BiosymMRParser.Atom_selection, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.NumberContext,i)


        def Ordinal(self):
            return self.getToken(BiosymMRParser.Ordinal, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_dihedral_angle_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDihedral_angle_constraint" ):
                listener.enterDihedral_angle_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDihedral_angle_constraint" ):
                listener.exitDihedral_angle_constraint(self)




    def dihedral_angle_constraint(self):

        localctx = BiosymMRParser.Dihedral_angle_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_dihedral_angle_constraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 152
                self.match(BiosymMRParser.Ordinal)


            self.state = 155
            self.match(BiosymMRParser.Atom_selection)
            self.state = 156
            self.match(BiosymMRParser.Atom_selection)
            self.state = 157
            self.match(BiosymMRParser.Atom_selection)
            self.state = 158
            self.match(BiosymMRParser.Atom_selection)
            self.state = 159
            self.number()
            self.state = 160
            self.number()
            self.state = 161
            self.number()
            self.state = 162
            self.number()
            self.state = 163
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dihedral_angle_wo_w_constraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dihedral_angle_wo_w_constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Dihedral_angle_wo_w_constraintContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Dihedral_angle_wo_w_constraintContext,i)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_dihedral_angle_wo_w_constraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDihedral_angle_wo_w_constraints" ):
                listener.enterDihedral_angle_wo_w_constraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDihedral_angle_wo_w_constraints" ):
                listener.exitDihedral_angle_wo_w_constraints(self)




    def dihedral_angle_wo_w_constraints(self):

        localctx = BiosymMRParser.Dihedral_angle_wo_w_constraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dihedral_angle_wo_w_constraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 165
                    self.dihedral_angle_wo_w_constraint()

                else:
                    raise NoViableAltException(self)
                self.state = 168 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dihedral_angle_wo_w_constraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Atom_selection(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Atom_selection)
            else:
                return self.getToken(BiosymMRParser.Atom_selection, i)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.NumberContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.NumberContext,i)


        def Ordinal(self):
            return self.getToken(BiosymMRParser.Ordinal, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_dihedral_angle_wo_w_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDihedral_angle_wo_w_constraint" ):
                listener.enterDihedral_angle_wo_w_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDihedral_angle_wo_w_constraint" ):
                listener.exitDihedral_angle_wo_w_constraint(self)




    def dihedral_angle_wo_w_constraint(self):

        localctx = BiosymMRParser.Dihedral_angle_wo_w_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_dihedral_angle_wo_w_constraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 170
                self.match(BiosymMRParser.Ordinal)


            self.state = 173
            self.match(BiosymMRParser.Atom_selection)
            self.state = 174
            self.match(BiosymMRParser.Atom_selection)
            self.state = 175
            self.match(BiosymMRParser.Atom_selection)
            self.state = 176
            self.match(BiosymMRParser.Atom_selection)
            self.state = 177
            self.number()
            self.state = 178
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Chirality_constraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chirality_constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Chirality_constraintContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Chirality_constraintContext,i)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_chirality_constraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChirality_constraints" ):
                listener.enterChirality_constraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChirality_constraints" ):
                listener.exitChirality_constraints(self)




    def chirality_constraints(self):

        localctx = BiosymMRParser.Chirality_constraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_chirality_constraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 180
                    self.chirality_constraint()

                else:
                    raise NoViableAltException(self)
                self.state = 183 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Chirality_constraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Atom_selection(self):
            return self.getToken(BiosymMRParser.Atom_selection, 0)

        def Chiral_code(self):
            return self.getToken(BiosymMRParser.Chiral_code, 0)

        def Ordinal(self):
            return self.getToken(BiosymMRParser.Ordinal, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_chirality_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChirality_constraint" ):
                listener.enterChirality_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChirality_constraint" ):
                listener.exitChirality_constraint(self)




    def chirality_constraint(self):

        localctx = BiosymMRParser.Chirality_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_chirality_constraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 185
                self.match(BiosymMRParser.Ordinal)


            self.state = 188
            self.match(BiosymMRParser.Atom_selection)
            self.state = 189
            self.match(BiosymMRParser.Chiral_code)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prochirality_constraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prochirality_constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BiosymMRParser.Prochirality_constraintContext)
            else:
                return self.getTypedRuleContext(BiosymMRParser.Prochirality_constraintContext,i)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_prochirality_constraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProchirality_constraints" ):
                listener.enterProchirality_constraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProchirality_constraints" ):
                listener.exitProchirality_constraints(self)




    def prochirality_constraints(self):

        localctx = BiosymMRParser.Prochirality_constraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_prochirality_constraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 191
                    self.prochirality_constraint()

                else:
                    raise NoViableAltException(self)
                self.state = 194 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prochirality_constraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Atom_selection(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Atom_selection)
            else:
                return self.getToken(BiosymMRParser.Atom_selection, i)

        def Ordinal(self):
            return self.getToken(BiosymMRParser.Ordinal, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_prochirality_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProchirality_constraint" ):
                listener.enterProchirality_constraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProchirality_constraint" ):
                listener.exitProchirality_constraint(self)




    def prochirality_constraint(self):

        localctx = BiosymMRParser.Prochirality_constraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_prochirality_constraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 196
                self.match(BiosymMRParser.Ordinal)


            self.state = 199
            self.match(BiosymMRParser.Atom_selection)
            self.state = 200
            self.match(BiosymMRParser.Atom_selection)
            self.state = 201
            self.match(BiosymMRParser.Atom_selection)
            self.state = 202
            self.match(BiosymMRParser.Atom_selection)
            self.state = 203
            self.match(BiosymMRParser.Atom_selection)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mixing_timeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Real(self):
            return self.getToken(BiosymMRParser.Real, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_mixing_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMixing_time" ):
                listener.enterMixing_time(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMixing_time" ):
                listener.exitMixing_time(self)




    def mixing_time(self):

        localctx = BiosymMRParser.Mixing_timeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_mixing_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(BiosymMRParser.Real)
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
            return self.getToken(BiosymMRParser.Float, 0)

        def Float_DecimalComma(self):
            return self.getToken(BiosymMRParser.Float_DecimalComma, 0)

        def Integer(self):
            return self.getToken(BiosymMRParser.Integer, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = BiosymMRParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
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


    class Ins_distance_restraintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ins_distance_restraint(self):
            return self.getTypedRuleContext(BiosymMRParser.Ins_distance_restraintContext,0)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_ins_distance_restraints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIns_distance_restraints" ):
                listener.enterIns_distance_restraints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIns_distance_restraints" ):
                listener.exitIns_distance_restraints(self)




    def ins_distance_restraints(self):

        localctx = BiosymMRParser.Ins_distance_restraintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_ins_distance_restraints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.ins_distance_restraint()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ins_distance_restraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_create(self):
            return self.getTypedRuleContext(BiosymMRParser.Decl_createContext,0)


        def decl_function(self):
            return self.getTypedRuleContext(BiosymMRParser.Decl_functionContext,0)


        def decl_target(self):
            return self.getTypedRuleContext(BiosymMRParser.Decl_targetContext,0)


        def getRuleIndex(self):
            return BiosymMRParser.RULE_ins_distance_restraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIns_distance_restraint" ):
                listener.enterIns_distance_restraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIns_distance_restraint" ):
                listener.exitIns_distance_restraint(self)




    def ins_distance_restraint(self):

        localctx = BiosymMRParser.Ins_distance_restraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_ins_distance_restraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.decl_create()
            self.state = 212
            self.decl_function()
            self.state = 213
            self.decl_target()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_createContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Restraint(self):
            return self.getToken(BiosymMRParser.Restraint, 0)

        def Create(self):
            return self.getToken(BiosymMRParser.Create, 0)

        def Double_quote_string(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Double_quote_string)
            else:
                return self.getToken(BiosymMRParser.Double_quote_string, i)

        def Distance(self):
            return self.getToken(BiosymMRParser.Distance, 0)

        def RETURN_II(self):
            return self.getToken(BiosymMRParser.RETURN_II, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_decl_create

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_create" ):
                listener.enterDecl_create(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_create" ):
                listener.exitDecl_create(self)




    def decl_create(self):

        localctx = BiosymMRParser.Decl_createContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_decl_create)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(BiosymMRParser.Restraint)
            self.state = 216
            self.match(BiosymMRParser.Create)
            self.state = 217
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 218
            self.match(BiosymMRParser.Distance)
            self.state = 219
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 220
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 221
            self.match(BiosymMRParser.RETURN_II)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Restraint(self):
            return self.getToken(BiosymMRParser.Restraint, 0)

        def Function(self):
            return self.getToken(BiosymMRParser.Function, 0)

        def Double_quote_string(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Double_quote_string)
            else:
                return self.getToken(BiosymMRParser.Double_quote_string, i)

        def RETURN_II(self):
            return self.getToken(BiosymMRParser.RETURN_II, 0)

        def Quadratic(self):
            return self.getToken(BiosymMRParser.Quadratic, 0)

        def Flat_bottomed(self):
            return self.getToken(BiosymMRParser.Flat_bottomed, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_decl_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_function" ):
                listener.enterDecl_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_function" ):
                listener.exitDecl_function(self)




    def decl_function(self):

        localctx = BiosymMRParser.Decl_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_decl_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(BiosymMRParser.Restraint)
            self.state = 224
            self.match(BiosymMRParser.Function)
            self.state = 225
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 226
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 227
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 228
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 229
                self.match(BiosymMRParser.Double_quote_string)


            self.state = 232
            self.match(BiosymMRParser.RETURN_II)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_targetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Restraint(self):
            return self.getToken(BiosymMRParser.Restraint, 0)

        def Target(self):
            return self.getToken(BiosymMRParser.Target, 0)

        def Double_quote_string(self, i:int=None):
            if i is None:
                return self.getTokens(BiosymMRParser.Double_quote_string)
            else:
                return self.getToken(BiosymMRParser.Double_quote_string, i)

        def RETURN_II(self):
            return self.getToken(BiosymMRParser.RETURN_II, 0)

        def Relative(self):
            return self.getToken(BiosymMRParser.Relative, 0)

        def getRuleIndex(self):
            return BiosymMRParser.RULE_decl_target

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_target" ):
                listener.enterDecl_target(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_target" ):
                listener.exitDecl_target(self)




    def decl_target(self):

        localctx = BiosymMRParser.Decl_targetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_decl_target)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(BiosymMRParser.Restraint)
            self.state = 235
            self.match(BiosymMRParser.Target)
            self.state = 236
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 237
            _la = self._input.LA(1)
            if not(_la==16 or _la==23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 238
            self.match(BiosymMRParser.Double_quote_string)
            self.state = 239
            self.match(BiosymMRParser.RETURN_II)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





