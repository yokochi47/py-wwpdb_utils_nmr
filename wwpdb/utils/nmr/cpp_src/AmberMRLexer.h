
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/AmberMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  AmberMRLexer : public antlr4::Lexer {
public:
  enum {
    END = 1, RST = 2, IAT = 3, RSTWT = 4, RESTRAINT = 5, ATNAM_Lp = 6, ATNAM = 7, 
    IRESID = 8, NSTEP1 = 9, NSTEP2 = 10, IRSTYP = 11, IALTD = 12, IFVARI = 13, 
    NINC = 14, IMULT = 15, R1 = 16, R2 = 17, R3 = 18, R4 = 19, RK2 = 20, 
    RK3 = 21, R1A = 22, R2A = 23, R3A = 24, R4A = 25, RK2A = 26, RK3A = 27, 
    R0 = 28, K0 = 29, R0A = 30, K0A = 31, RJCOEF = 32, IGR1 = 33, IGR2 = 34, 
    IGR3 = 35, IGR4 = 36, IGR5 = 37, IGR6 = 38, IGR7 = 39, IGR8 = 40, FXYZ = 41, 
    OUTXYZ = 42, GRNAM1_Lp = 43, GRNAM2_Lp = 44, GRNAM3_Lp = 45, GRNAM4_Lp = 46, 
    GRNAM5_Lp = 47, GRNAM6_Lp = 48, GRNAM7_Lp = 49, GRNAM8_Lp = 50, GRNAM1 = 51, 
    GRNAM2 = 52, GRNAM3 = 53, GRNAM4 = 54, GRNAM5 = 55, GRNAM6 = 56, GRNAM7 = 57, 
    GRNAM8 = 58, IR6 = 59, IFNTYP = 60, IXPK = 61, NXPK = 62, ICONSTR = 63, 
    NOEEXP = 64, NPEAK = 65, EMIX = 66, IHP = 67, JHP = 68, AEXP = 69, ARANGE = 70, 
    AWT = 71, INVWT1 = 72, INVWT2 = 73, OMEGA = 74, TAUROT = 75, TAUMET = 76, 
    ID2O = 77, OSCALE = 78, SHF = 79, NRING = 80, NATR = 81, IATR = 82, 
    NAMR = 83, STR = 84, IPROT = 85, OBS = 86, SHRANG = 87, WT = 88, NPROT = 89, 
    SHCUT = 90, NTER = 91, CTER = 92, PCSHF = 93, NME = 94, NMPMC = 95, 
    OPTPHI = 96, OPTTET = 97, OPTOMG = 98, OPTA1 = 99, OPTA2 = 100, OPTKON = 101, 
    TOLPRO = 102, MLTPRO = 103, ALIGN = 104, NDIP = 105, ID = 106, JD = 107, 
    DOBSL = 108, DOBSU = 109, DOBS = 110, DWT = 111, DATASET = 112, NUM_DATASETS = 113, 
    S11 = 114, S12 = 115, S13 = 116, S22 = 117, S23 = 118, GIGJ = 119, DIJ = 120, 
    DCUT = 121, FJ = 122, DFAC_AL = 123, FREEZEMOL = 124, CSA = 125, NCSA = 126, 
    ICSA = 127, JCSA = 128, KCSA = 129, COBSL = 130, COBSU = 131, COBS = 132, 
    CWT = 133, DATASETC = 134, FIELD = 135, SIGMA11 = 136, SIGMA12 = 137, 
    SIGMA13 = 138, SIGMA22 = 139, SIGMA23 = 140, CCUT = 141, Comma = 142, 
    Residue = 143, Mapping = 144, Ambig = 145, SMCLN_COMMENT = 146, COMMENT = 147, 
    Logical = 148, L_paren = 149, R_paren = 150, L_brace = 151, R_brace = 152, 
    L_brakt = 153, R_brakt = 154, Equ_op = 155, L_quot = 156, Simple_name = 157, 
    SPACE = 158, SECTION_COMMENT = 159, Any_name = 160, SPACE_CM = 161, 
    RETURN_CM = 162, Equ_op_IP = 163, L_paren_IP = 164, Integer = 165, SPACE_IP = 166, 
    Equ_op_RP = 167, L_paren_RP = 168, Real = 169, SPACE_RP = 170, Equ_op_BP = 171, 
    BoolInt = 172, SPACE_BP = 173, L_paren_QP = 174, Equ_op_QP = 175, Qstring = 176, 
    Decimal_AP = 177, R_paren_AP = 178, Equ_op_AP = 179, SPACE_AP = 180, 
    Qstring_AP = 181, L_paren_IA = 182, Equ_op_IA = 183, Comma_IA = 184, 
    End_IA = 185, Asterisk_IA = 186, Integers = 187, MultiplicativeInt = 188, 
    COMMENT_IA = 189, L_paren_RA = 190, Equ_op_RA = 191, Comma_RA = 192, 
    End_RA = 193, Asterisk_RA = 194, Reals = 195, MultiplicativeReal = 196, 
    COMMENT_RA = 197, Equ_op_BA = 198, Comma_BA = 199, End_BA = 200, BoolInts = 201, 
    COMMENT_BA = 202, L_paren_QA = 203, Equ_op_QA = 204, Comma_QA = 205, 
    End_QA = 206, Qstrings = 207, COMMENT_QA = 208, Comma_AR = 209, R_paren_AR = 210, 
    Decimal = 211, SPACE_AR = 212, DISTANCE_F = 213, ANGLE_F = 214, TORSION_F = 215, 
    COORDINATE_F = 216, PLANE_F = 217, COM_F = 218, Integer_F = 219, Real_F = 220, 
    Ambmask_F = 221, Comma_F = 222, L_paren_F = 223, R_paren_F = 224, L_brace_F = 225, 
    R_brace_F = 226, L_brakt_F = 227, R_brakt_F = 228, R_quot = 229, SPACE_F = 230, 
    Ambig_code_MP = 231, Integer_MP = 232, Simple_name_MP = 233, Equ_op_MP = 234, 
    SPACE_MP = 235, RETURN_MP = 236, LINE_COMMENT_MP = 237
  };

  enum {
    COMMENT_MODE = 1, INT_PARAM_MODE = 2, REAL_PARAM_MODE = 3, BINT_PARAM_MODE = 4, 
    QSTR_PARAM_MODE = 5, AQSTR_PARAM_MODE = 6, AQSTR_PARAM_MODE_ = 7, INT_ARRAY_MODE = 8, 
    REAL_ARRAY_MODE = 9, BINT_ARRAY_MODE = 10, QSTR_ARRAY_MODE = 11, ARGUMENT_MODE = 12, 
    FUNC_CALL_MODE = 13, MAP_MODE = 14
  };

  explicit AmberMRLexer(antlr4::CharStream *input);

  ~AmberMRLexer() override;


  std::string getGrammarFileName() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const std::vector<std::string>& getChannelNames() const override;

  const std::vector<std::string>& getModeNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;

  const antlr4::atn::ATN& getATN() const override;

  // By default the static state used to implement the lexer is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:

  // Individual action functions triggered by action() above.

  // Individual semantic predicate functions triggered by sempred() above.

};

