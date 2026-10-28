
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/XplorMRLexer.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  XplorMRLexer : public antlr4::Lexer {
public:
  enum {
    Set = 1, End = 2, Noe = 3, Assign = 4, Asymptote = 5, Average = 6, Bhig = 7, 
    Ceiling = 8, Classification = 9, CountViol = 10, Distribute = 11, Monomers = 12, 
    Ncount = 13, Nrestraints = 14, Potential = 15, Predict = 16, Print = 17, 
    Threshold = 18, Reset = 19, Rswitch = 20, Scale = 21, SoExponent = 22, 
    SqConstant = 23, SqExponent = 24, SqOffset = 25, Temperature = 26, Cutoff = 27, 
    Cuton = 28, From = 29, To = 30, Peak = 31, Spectrum = 32, Volume = 33, 
    Vol = 34, Ppm1 = 35, Ppm2 = 36, Restraints = 37, Dihedral = 38, Nassign = 39, 
    Print_any = 40, Sanisotropy = 41, Coefficients = 42, ForceConstant = 43, 
    Xdipolar = 44, Dipolar = 45, Type = 46, Sign = 47, VeAngle = 48, Cv = 49, 
    Partition = 50, Tensor = 51, Anisotropy = 52, Planar = 53, Group = 54, 
    Initialize = 55, Selection = 56, Weight = 57, Harmonic = 58, Exponent = 59, 
    Normal = 60, Xadc = 61, Expectation = 62, Size = 63, Zero = 64, Coupling = 65, 
    Degeneracy = 66, Carbon = 67, PhiStep = 68, PsiStep = 69, Rcoil = 70, 
    Proton = 71, Observed = 72, Amides = 73, Nitrogens = 74, Oxygens = 75, 
    RingAtoms = 76, AlphasAndAmides = 77, Error = 78, Ramachandran = 79, 
    Gaussian = 80, Phase = 81, Quartic = 82, Shape = 83, Sort = 84, Dimensions = 85, 
    Collapse = 86, Danisotropy = 87, Orient = 88, Height = 89, MaxGaussians = 90, 
    NewGaussian = 91, Dcsa = 92, Sigma = 93, Pcsa = 94, OneBond = 95, AngleDb = 96, 
    DerivFlag = 97, PMagnetic = 98, Kconst = 99, Omega = 100, Tauc = 101, 
    Debug = 102, Xpcs = 103, Tolerance = 104, Save = 105, Fmed = 106, ErrOn = 107, 
    ErrOff = 108, Fon = 109, Foff = 110, Son = 111, Soff = 112, Frun = 113, 
    Xrdcoupling = 114, Xangle = 115, Xccr = 116, Weip = 117, Hbda = 118, 
    Hbdb = 119, Kdir = 120, Klin = 121, Nseg = 122, Nmin = 123, Nmax = 124, 
    Segm = 125, Ohcut = 126, Coh1cut = 127, Coh2cut = 128, Ohncut = 129, 
    Updfrq = 130, Prnfrq = 131, Freemode = 132, Donor = 133, Acceptor = 134, 
    Ncs = 135, Equivalence = 136, Sigb = 137, Flags = 138, All = 139, Around = 140, 
    Atom = 141, Attribute = 142, BondedTo = 143, ByGroup = 144, ByRes = 145, 
    Chemical = 146, Hydrogen = 147, Id = 148, Known = 149, Name = 150, Point = 151, 
    Cut = 152, Previous = 153, Pseudo = 154, Residue = 155, Resname = 156, 
    Saround = 157, SegIdentifier = 158, Store1 = 159, Store2 = 160, Store3 = 161, 
    Store4 = 162, Store5 = 163, Store6 = 164, Store7 = 165, Store8 = 166, 
    Store9 = 167, Tag = 168, Vector = 169, Do_Lp = 170, Identity_Lp = 171, 
    Show = 172, Evaluate_Lp = 173, Patch = 174, Reference = 175, Nil = 176, 
    Parameter = 177, UB = 178, Mult = 179, HBonded = 180, Improper = 181, 
    NBFix = 182, NonB = 183, VDWOff = 184, Verbose = 185, For = 186, Loop = 187, 
    Tail = 188, Head = 189, Or_op = 190, And_op = 191, Not_op = 192, Comma = 193, 
    Complex = 194, Integer = 195, Logical = 196, Real = 197, Double_quote_string = 198, 
    SHARP_COMMENT = 199, EXCLM_COMMENT = 200, SMCLN_COMMENT = 201, Simple_name = 202, 
    Simple_names = 203, Integers = 204, L_paren = 205, R_paren = 206, Colon = 207, 
    Equ_op = 208, Lt_op = 209, Gt_op = 210, Leq_op = 211, Geq_op = 212, 
    Neq_op = 213, Symbol_name = 214, SPACE = 215, ENCLOSE_COMMENT = 216, 
    SECTION_COMMENT = 217, LINE_COMMENT = 218, SET_VARIABLE = 219, Abs = 220, 
    Attr_properties = 221, Comparison_ops = 222, SPACE_AP = 223, Equ_op_CL = 224, 
    Class_name = 225, SPACE_CL = 226, Averaging_methods = 227, Class_name_AM = 228, 
    SPACE_AM = 229, Equ_op_PT = 230, Potential_types = 231, Class_name_PT = 232, 
    SPACE_PT = 233, Rdc_dist_fix_types = 234, Rdc_or_Diff_anis_types = 235, 
    Csa_types = 236, SPACE_TY = 237, Gauss_or_Quart = 238, SPACE_SH = 239, 
    Exclude = 240, Include = 241, End_FL = 242, Class_name_FL = 243, Any_class = 244, 
    SPACE_FL = 245, R_paren_VE = 246, Equ_op_VE = 247, Add_op_VE = 248, 
    Sub_op_VE = 249, Mul_op_VE = 250, Div_op_VE = 251, Exp_op_VE = 252, 
    Comma_VE = 253, Integer_VE = 254, Real_VE = 255, Atom_properties_VE = 256, 
    Abs_VE = 257, Acos_VE = 258, Asin_VE = 259, Cos_VE = 260, Decode_VE = 261, 
    Encode_VE = 262, Exp_VE = 263, Gauss_VE = 264, Heavy_VE = 265, Int_VE = 266, 
    Log10_VE = 267, Log_VE = 268, Max_VE = 269, Maxw_VE = 270, Min_VE = 271, 
    Mod_VE = 272, Norm_VE = 273, Random_VE = 274, Sign_VE = 275, Sin_VE = 276, 
    Sqrt_VE = 277, Tan_VE = 278, Symbol_name_VE = 279, Simple_name_VE = 280, 
    Double_quote_string_VE = 281, SPACE_VE = 282, L_paren_VF = 283, SPACE_VF = 284, 
    L_paren_VS = 285, R_paren_VS = 286, Average_VS = 287, Element_VS = 288, 
    Max_VS = 289, Min_VS = 290, Norm_VS = 291, Rms_VS = 292, Sum_VS = 293, 
    Atom_properties_VS = 294, SPACE_VS = 295, L_paren_CF = 296, R_paren_CF = 297, 
    In_CF = 298, Integer_CF = 299, Real_CF = 300, Symbol_name_CF = 301, 
    Simple_name_CF = 302, SPACE_CF = 303, COMMENT_CF = 304, Simple_name_LL = 305, 
    SPACE_LL = 306
  };

  enum {
    ATTR_MODE = 1, CLAS_MODE = 2, AVER_MODE = 3, POTE_MODE = 4, TYPE_MODE = 5, 
    SHAP_MODE = 6, FLAG_MODE = 7, VECTOR_EXPR_MODE = 8, VECTOR_FUNC_MODE = 9, 
    VECTOR_SHOW_MODE = 10, CTL_FOR_MODE = 11, LOOP_LABEL_MODE = 12
  };

  explicit XplorMRLexer(antlr4::CharStream *input);

  ~XplorMRLexer() override;


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

