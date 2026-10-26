
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/XplorMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  XplorMRParser : public antlr4::Parser {
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
    Attr_properties = 221, Comparison_ops = 222, SPACE_AP = 223, Averaging_methods = 224, 
    Class_name_AM = 225, SPACE_AM = 226, Equ_op_PT = 227, Potential_types = 228, 
    Class_name_PT = 229, SPACE_PT = 230, Rdc_dist_fix_types = 231, Rdc_or_Diff_anis_types = 232, 
    Csa_types = 233, SPACE_TY = 234, Gauss_or_Quart = 235, SPACE_SH = 236, 
    Exclude = 237, Include = 238, End_FL = 239, Class_name = 240, Any_class = 241, 
    SPACE_FL = 242, R_paren_VE = 243, Equ_op_VE = 244, Add_op_VE = 245, 
    Sub_op_VE = 246, Mul_op_VE = 247, Div_op_VE = 248, Exp_op_VE = 249, 
    Comma_VE = 250, Integer_VE = 251, Real_VE = 252, Atom_properties_VE = 253, 
    Abs_VE = 254, Acos_VE = 255, Asin_VE = 256, Cos_VE = 257, Decode_VE = 258, 
    Encode_VE = 259, Exp_VE = 260, Gauss_VE = 261, Heavy_VE = 262, Int_VE = 263, 
    Log10_VE = 264, Log_VE = 265, Max_VE = 266, Maxw_VE = 267, Min_VE = 268, 
    Mod_VE = 269, Norm_VE = 270, Random_VE = 271, Sign_VE = 272, Sin_VE = 273, 
    Sqrt_VE = 274, Tan_VE = 275, Symbol_name_VE = 276, Simple_name_VE = 277, 
    Double_quote_string_VE = 278, SPACE_VE = 279, L_paren_VF = 280, SPACE_VF = 281, 
    L_paren_VS = 282, R_paren_VS = 283, Average_VS = 284, Element_VS = 285, 
    Max_VS = 286, Min_VS = 287, Norm_VS = 288, Rms_VS = 289, Sum_VS = 290, 
    Atom_properties_VS = 291, SPACE_VS = 292, L_paren_CF = 293, R_paren_CF = 294, 
    In_CF = 295, Integer_CF = 296, Real_CF = 297, Symbol_name_CF = 298, 
    Simple_name_CF = 299, SPACE_CF = 300, COMMENT_CF = 301, Simple_name_LL = 302, 
    SPACE_LL = 303
  };

  enum {
    RuleXplor_nih_mr = 0, RuleDistance_restraint = 1, RuleDihedral_angle_restraint = 2, 
    RuleRdc_restraint = 3, RulePlanar_restraint = 4, RuleHarmonic_restraint = 5, 
    RuleAntidistance_restraint = 6, RuleCoupling_restraint = 7, RuleCarbon_shift_restraint = 8, 
    RuleProton_shift_restraint = 9, RuleDihedral_angle_db_restraint = 10, 
    RuleRadius_of_gyration_restraint = 11, RuleDiffusion_anisotropy_restraint = 12, 
    RuleOrientation_db_restraint = 13, RuleCsa_restraint = 14, RulePcsa_restraint = 15, 
    RuleOne_bond_coupling_restraint = 16, RuleAngle_db_restraint = 17, RulePre_restraint = 18, 
    RulePcs_restraint = 19, RulePrdc_restraint = 20, RulePorientation_restraint = 21, 
    RulePccr_restraint = 22, RuleHbond_restraint = 23, RuleHbond_db_restraint = 24, 
    RuleNoe_statement = 25, RuleNoe_assign = 26, RulePredict_statement = 27, 
    RuleNoe_annotation = 28, RuleDihedral_statement = 29, RuleDihedral_assign = 30, 
    RuleSani_statement = 31, RuleSani_assign = 32, RuleXdip_statement = 33, 
    RuleXdip_assign = 34, RuleVean_statement = 35, RuleVean_assign = 36, 
    RuleTenso_statement = 37, RuleTenso_assign = 38, RuleAnis_statement = 39, 
    RuleAnis_assign = 40, RulePlanar_statement = 41, RulePlanar_group = 42, 
    RuleGroup_statement = 43, RuleHarmonic_statement = 44, RuleHarmonic_assign = 45, 
    RuleAntidistance_statement = 46, RuleXadc_assign = 47, RuleCoupling_statement = 48, 
    RuleCoup_assign = 49, RuleCarbon_shift_statement = 50, RuleCarbon_shift_assign = 51, 
    RuleCarbon_shift_rcoil = 52, RuleProton_shift_statement = 53, RuleObserved = 54, 
    RuleProton_shift_rcoil = 55, RuleProton_shift_anisotropy = 56, RuleProton_shift_amides = 57, 
    RuleProton_shift_carbons = 58, RuleProton_shift_nitrogens = 59, RuleProton_shift_oxygens = 60, 
    RuleProton_shift_ring_atoms = 61, RuleProton_shift_alphas_and_amides = 62, 
    RuleRamachandran_statement = 63, RuleRama_assign = 64, RuleCollapse_statement = 65, 
    RuleColl_assign = 66, RuleDiffusion_statement = 67, RuleDani_assign = 68, 
    RuleOrientation_statement = 69, RuleOrie_assign = 70, RuleCsa_statement = 71, 
    RuleCsa_assign = 72, RulePcsa_statement = 73, RuleOne_bond_coupling_statement = 74, 
    RuleOne_bond_assign = 75, RuleAngle_db_statement = 76, RuleAngle_db_assign = 77, 
    RulePre_statement = 78, RulePre_assign = 79, RulePcs_statement = 80, 
    RulePcs_assign = 81, RulePrdc_statement = 82, RulePrdc_assign = 83, 
    RulePorientation_statement = 84, RulePorientation_assign = 85, RulePccr_statement = 86, 
    RulePccr_assign = 87, RuleHbond_statement = 88, RuleHbond_assign = 89, 
    RuleHbond_db_statement = 90, RuleHbond_db_assign = 91, RuleNcs_restraint = 92, 
    RuleNcs_statement = 93, RuleNcs_group_statement = 94, RuleSelection = 95, 
    RuleSelection_expression = 96, RuleTerm = 97, RuleFactor = 98, RuleNumber = 99, 
    RuleNumber_f = 100, RuleNumber_s = 101, RuleNumber_a = 102, RuleClassification = 103, 
    RuleClass_name = 104, RuleFlag_statement = 105, RuleVector_statement = 106, 
    RuleVector_mode = 107, RuleVector_expression = 108, RuleVector_operation = 109, 
    RuleVflc = 110, RuleVector_func_call = 111, RuleVector_show_property = 112, 
    RuleEvaluate_statement = 113, RuleEvaluate_operation = 114, RulePatch_statement = 115, 
    RuleParameter_setting = 116, RuleParameter_statement = 117, RuleNoe_assign_loop = 118, 
    RuleDihedral_assign_loop = 119, RuleSani_assign_loop = 120, RuleXadc_assign_loop = 121, 
    RuleCoup_assign_loop = 122, RuleColl_assign_loop = 123, RuleCsa_assign_loop = 124, 
    RulePre_assign_loop = 125, RulePcs_assign_loop = 126, RuleHbond_assign_loop = 127, 
    RuleHbond_db_assign_loop = 128, RulePlanar_group_loop = 129
  };

  explicit XplorMRParser(antlr4::TokenStream *input);

  XplorMRParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~XplorMRParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Xplor_nih_mrContext;
  class Distance_restraintContext;
  class Dihedral_angle_restraintContext;
  class Rdc_restraintContext;
  class Planar_restraintContext;
  class Harmonic_restraintContext;
  class Antidistance_restraintContext;
  class Coupling_restraintContext;
  class Carbon_shift_restraintContext;
  class Proton_shift_restraintContext;
  class Dihedral_angle_db_restraintContext;
  class Radius_of_gyration_restraintContext;
  class Diffusion_anisotropy_restraintContext;
  class Orientation_db_restraintContext;
  class Csa_restraintContext;
  class Pcsa_restraintContext;
  class One_bond_coupling_restraintContext;
  class Angle_db_restraintContext;
  class Pre_restraintContext;
  class Pcs_restraintContext;
  class Prdc_restraintContext;
  class Porientation_restraintContext;
  class Pccr_restraintContext;
  class Hbond_restraintContext;
  class Hbond_db_restraintContext;
  class Noe_statementContext;
  class Noe_assignContext;
  class Predict_statementContext;
  class Noe_annotationContext;
  class Dihedral_statementContext;
  class Dihedral_assignContext;
  class Sani_statementContext;
  class Sani_assignContext;
  class Xdip_statementContext;
  class Xdip_assignContext;
  class Vean_statementContext;
  class Vean_assignContext;
  class Tenso_statementContext;
  class Tenso_assignContext;
  class Anis_statementContext;
  class Anis_assignContext;
  class Planar_statementContext;
  class Planar_groupContext;
  class Group_statementContext;
  class Harmonic_statementContext;
  class Harmonic_assignContext;
  class Antidistance_statementContext;
  class Xadc_assignContext;
  class Coupling_statementContext;
  class Coup_assignContext;
  class Carbon_shift_statementContext;
  class Carbon_shift_assignContext;
  class Carbon_shift_rcoilContext;
  class Proton_shift_statementContext;
  class ObservedContext;
  class Proton_shift_rcoilContext;
  class Proton_shift_anisotropyContext;
  class Proton_shift_amidesContext;
  class Proton_shift_carbonsContext;
  class Proton_shift_nitrogensContext;
  class Proton_shift_oxygensContext;
  class Proton_shift_ring_atomsContext;
  class Proton_shift_alphas_and_amidesContext;
  class Ramachandran_statementContext;
  class Rama_assignContext;
  class Collapse_statementContext;
  class Coll_assignContext;
  class Diffusion_statementContext;
  class Dani_assignContext;
  class Orientation_statementContext;
  class Orie_assignContext;
  class Csa_statementContext;
  class Csa_assignContext;
  class Pcsa_statementContext;
  class One_bond_coupling_statementContext;
  class One_bond_assignContext;
  class Angle_db_statementContext;
  class Angle_db_assignContext;
  class Pre_statementContext;
  class Pre_assignContext;
  class Pcs_statementContext;
  class Pcs_assignContext;
  class Prdc_statementContext;
  class Prdc_assignContext;
  class Porientation_statementContext;
  class Porientation_assignContext;
  class Pccr_statementContext;
  class Pccr_assignContext;
  class Hbond_statementContext;
  class Hbond_assignContext;
  class Hbond_db_statementContext;
  class Hbond_db_assignContext;
  class Ncs_restraintContext;
  class Ncs_statementContext;
  class Ncs_group_statementContext;
  class SelectionContext;
  class Selection_expressionContext;
  class TermContext;
  class FactorContext;
  class NumberContext;
  class Number_fContext;
  class Number_sContext;
  class Number_aContext;
  class ClassificationContext;
  class Class_nameContext;
  class Flag_statementContext;
  class Vector_statementContext;
  class Vector_modeContext;
  class Vector_expressionContext;
  class Vector_operationContext;
  class VflcContext;
  class Vector_func_callContext;
  class Vector_show_propertyContext;
  class Evaluate_statementContext;
  class Evaluate_operationContext;
  class Patch_statementContext;
  class Parameter_settingContext;
  class Parameter_statementContext;
  class Noe_assign_loopContext;
  class Dihedral_assign_loopContext;
  class Sani_assign_loopContext;
  class Xadc_assign_loopContext;
  class Coup_assign_loopContext;
  class Coll_assign_loopContext;
  class Csa_assign_loopContext;
  class Pre_assign_loopContext;
  class Pcs_assign_loopContext;
  class Hbond_assign_loopContext;
  class Hbond_db_assign_loopContext;
  class Planar_group_loopContext; 

  class  Xplor_nih_mrContext : public antlr4::ParserRuleContext {
  public:
    Xplor_nih_mrContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<Distance_restraintContext *> distance_restraint();
    Distance_restraintContext* distance_restraint(size_t i);
    std::vector<Dihedral_angle_restraintContext *> dihedral_angle_restraint();
    Dihedral_angle_restraintContext* dihedral_angle_restraint(size_t i);
    std::vector<Rdc_restraintContext *> rdc_restraint();
    Rdc_restraintContext* rdc_restraint(size_t i);
    std::vector<Planar_restraintContext *> planar_restraint();
    Planar_restraintContext* planar_restraint(size_t i);
    std::vector<Harmonic_restraintContext *> harmonic_restraint();
    Harmonic_restraintContext* harmonic_restraint(size_t i);
    std::vector<Antidistance_restraintContext *> antidistance_restraint();
    Antidistance_restraintContext* antidistance_restraint(size_t i);
    std::vector<Coupling_restraintContext *> coupling_restraint();
    Coupling_restraintContext* coupling_restraint(size_t i);
    std::vector<Carbon_shift_restraintContext *> carbon_shift_restraint();
    Carbon_shift_restraintContext* carbon_shift_restraint(size_t i);
    std::vector<Proton_shift_restraintContext *> proton_shift_restraint();
    Proton_shift_restraintContext* proton_shift_restraint(size_t i);
    std::vector<Dihedral_angle_db_restraintContext *> dihedral_angle_db_restraint();
    Dihedral_angle_db_restraintContext* dihedral_angle_db_restraint(size_t i);
    std::vector<Radius_of_gyration_restraintContext *> radius_of_gyration_restraint();
    Radius_of_gyration_restraintContext* radius_of_gyration_restraint(size_t i);
    std::vector<Diffusion_anisotropy_restraintContext *> diffusion_anisotropy_restraint();
    Diffusion_anisotropy_restraintContext* diffusion_anisotropy_restraint(size_t i);
    std::vector<Orientation_db_restraintContext *> orientation_db_restraint();
    Orientation_db_restraintContext* orientation_db_restraint(size_t i);
    std::vector<Csa_restraintContext *> csa_restraint();
    Csa_restraintContext* csa_restraint(size_t i);
    std::vector<Pcsa_restraintContext *> pcsa_restraint();
    Pcsa_restraintContext* pcsa_restraint(size_t i);
    std::vector<One_bond_coupling_restraintContext *> one_bond_coupling_restraint();
    One_bond_coupling_restraintContext* one_bond_coupling_restraint(size_t i);
    std::vector<Angle_db_restraintContext *> angle_db_restraint();
    Angle_db_restraintContext* angle_db_restraint(size_t i);
    std::vector<Pre_restraintContext *> pre_restraint();
    Pre_restraintContext* pre_restraint(size_t i);
    std::vector<Pcs_restraintContext *> pcs_restraint();
    Pcs_restraintContext* pcs_restraint(size_t i);
    std::vector<Prdc_restraintContext *> prdc_restraint();
    Prdc_restraintContext* prdc_restraint(size_t i);
    std::vector<Porientation_restraintContext *> porientation_restraint();
    Porientation_restraintContext* porientation_restraint(size_t i);
    std::vector<Pccr_restraintContext *> pccr_restraint();
    Pccr_restraintContext* pccr_restraint(size_t i);
    std::vector<Hbond_restraintContext *> hbond_restraint();
    Hbond_restraintContext* hbond_restraint(size_t i);
    std::vector<Hbond_db_restraintContext *> hbond_db_restraint();
    Hbond_db_restraintContext* hbond_db_restraint(size_t i);
    std::vector<Ncs_restraintContext *> ncs_restraint();
    Ncs_restraintContext* ncs_restraint(size_t i);
    std::vector<ClassificationContext *> classification();
    ClassificationContext* classification(size_t i);
    std::vector<Flag_statementContext *> flag_statement();
    Flag_statementContext* flag_statement(size_t i);
    std::vector<Vector_statementContext *> vector_statement();
    Vector_statementContext* vector_statement(size_t i);
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Patch_statementContext *> patch_statement();
    Patch_statementContext* patch_statement(size_t i);
    std::vector<Parameter_settingContext *> parameter_setting();
    Parameter_settingContext* parameter_setting(size_t i);
    std::vector<Noe_assign_loopContext *> noe_assign_loop();
    Noe_assign_loopContext* noe_assign_loop(size_t i);
    std::vector<Dihedral_assign_loopContext *> dihedral_assign_loop();
    Dihedral_assign_loopContext* dihedral_assign_loop(size_t i);
    std::vector<Sani_assign_loopContext *> sani_assign_loop();
    Sani_assign_loopContext* sani_assign_loop(size_t i);
    std::vector<Hbond_assign_loopContext *> hbond_assign_loop();
    Hbond_assign_loopContext* hbond_assign_loop(size_t i);
    std::vector<Hbond_db_assign_loopContext *> hbond_db_assign_loop();
    Hbond_db_assign_loopContext* hbond_db_assign_loop(size_t i);
    std::vector<Coup_assign_loopContext *> coup_assign_loop();
    Coup_assign_loopContext* coup_assign_loop(size_t i);
    std::vector<Xadc_assign_loopContext *> xadc_assign_loop();
    Xadc_assign_loopContext* xadc_assign_loop(size_t i);
    std::vector<Coll_assign_loopContext *> coll_assign_loop();
    Coll_assign_loopContext* coll_assign_loop(size_t i);
    std::vector<Csa_assign_loopContext *> csa_assign_loop();
    Csa_assign_loopContext* csa_assign_loop(size_t i);
    std::vector<Pre_assign_loopContext *> pre_assign_loop();
    Pre_assign_loopContext* pre_assign_loop(size_t i);
    std::vector<Pcs_assign_loopContext *> pcs_assign_loop();
    Pcs_assign_loopContext* pcs_assign_loop(size_t i);
    std::vector<Noe_assignContext *> noe_assign();
    Noe_assignContext* noe_assign(size_t i);
    std::vector<Dihedral_assignContext *> dihedral_assign();
    Dihedral_assignContext* dihedral_assign(size_t i);
    std::vector<Sani_assignContext *> sani_assign();
    Sani_assignContext* sani_assign(size_t i);
    std::vector<Planar_statementContext *> planar_statement();
    Planar_statementContext* planar_statement(size_t i);
    std::vector<Harmonic_assignContext *> harmonic_assign();
    Harmonic_assignContext* harmonic_assign(size_t i);
    std::vector<Hbond_assignContext *> hbond_assign();
    Hbond_assignContext* hbond_assign(size_t i);
    std::vector<Hbond_db_assignContext *> hbond_db_assign();
    Hbond_db_assignContext* hbond_db_assign(size_t i);
    std::vector<Coup_assignContext *> coup_assign();
    Coup_assignContext* coup_assign(size_t i);
    std::vector<Xadc_assignContext *> xadc_assign();
    Xadc_assignContext* xadc_assign(size_t i);
    std::vector<Coll_assignContext *> coll_assign();
    Coll_assignContext* coll_assign(size_t i);
    std::vector<Csa_assignContext *> csa_assign();
    Csa_assignContext* csa_assign(size_t i);
    std::vector<Pre_assignContext *> pre_assign();
    Pre_assignContext* pre_assign(size_t i);
    std::vector<Pcs_assignContext *> pcs_assign();
    Pcs_assignContext* pcs_assign(size_t i);
    std::vector<ObservedContext *> observed();
    ObservedContext* observed(size_t i);
    std::vector<Parameter_statementContext *> parameter_statement();
    Parameter_statementContext* parameter_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Xplor_nih_mrContext* xplor_nih_mr();

  class  Distance_restraintContext : public antlr4::ParserRuleContext {
  public:
    Distance_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Noe();
    antlr4::tree::TerminalNode *End();
    std::vector<Noe_statementContext *> noe_statement();
    Noe_statementContext* noe_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_restraintContext* distance_restraint();

  class  Dihedral_angle_restraintContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_angle_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Dihedral();
    antlr4::tree::TerminalNode *End();
    antlr4::tree::TerminalNode *Restraints();
    std::vector<Dihedral_statementContext *> dihedral_statement();
    Dihedral_statementContext* dihedral_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_angle_restraintContext* dihedral_angle_restraint();

  class  Rdc_restraintContext : public antlr4::ParserRuleContext {
  public:
    Rdc_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Sanisotropy();
    antlr4::tree::TerminalNode *End();
    std::vector<Sani_statementContext *> sani_statement();
    Sani_statementContext* sani_statement(size_t i);
    antlr4::tree::TerminalNode *Xdipolar();
    antlr4::tree::TerminalNode *Dipolar();
    std::vector<Xdip_statementContext *> xdip_statement();
    Xdip_statementContext* xdip_statement(size_t i);
    antlr4::tree::TerminalNode *VeAngle();
    std::vector<Vean_statementContext *> vean_statement();
    Vean_statementContext* vean_statement(size_t i);
    antlr4::tree::TerminalNode *Tensor();
    std::vector<Tenso_statementContext *> tenso_statement();
    Tenso_statementContext* tenso_statement(size_t i);
    antlr4::tree::TerminalNode *Anisotropy();
    std::vector<Anis_statementContext *> anis_statement();
    Anis_statementContext* anis_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rdc_restraintContext* rdc_restraint();

  class  Planar_restraintContext : public antlr4::ParserRuleContext {
  public:
    Planar_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Planar();
    antlr4::tree::TerminalNode *End();
    antlr4::tree::TerminalNode *Restraints();
    std::vector<Planar_statementContext *> planar_statement();
    Planar_statementContext* planar_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Planar_restraintContext* planar_restraint();

  class  Harmonic_restraintContext : public antlr4::ParserRuleContext {
  public:
    Harmonic_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Harmonic();
    antlr4::tree::TerminalNode *End();
    antlr4::tree::TerminalNode *Restraints();
    std::vector<Harmonic_statementContext *> harmonic_statement();
    Harmonic_statementContext* harmonic_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Harmonic_restraintContext* harmonic_restraint();

  class  Antidistance_restraintContext : public antlr4::ParserRuleContext {
  public:
    Antidistance_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Xadc();
    antlr4::tree::TerminalNode *End();
    std::vector<Antidistance_statementContext *> antidistance_statement();
    Antidistance_statementContext* antidistance_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Antidistance_restraintContext* antidistance_restraint();

  class  Coupling_restraintContext : public antlr4::ParserRuleContext {
  public:
    Coupling_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Coupling();
    antlr4::tree::TerminalNode *End();
    std::vector<Coupling_statementContext *> coupling_statement();
    Coupling_statementContext* coupling_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coupling_restraintContext* coupling_restraint();

  class  Carbon_shift_restraintContext : public antlr4::ParserRuleContext {
  public:
    Carbon_shift_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Carbon();
    antlr4::tree::TerminalNode *End();
    std::vector<Carbon_shift_statementContext *> carbon_shift_statement();
    Carbon_shift_statementContext* carbon_shift_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Carbon_shift_restraintContext* carbon_shift_restraint();

  class  Proton_shift_restraintContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Proton();
    antlr4::tree::TerminalNode *End();
    std::vector<Proton_shift_statementContext *> proton_shift_statement();
    Proton_shift_statementContext* proton_shift_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_restraintContext* proton_shift_restraint();

  class  Dihedral_angle_db_restraintContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_angle_db_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Ramachandran();
    antlr4::tree::TerminalNode *End();
    std::vector<Ramachandran_statementContext *> ramachandran_statement();
    Ramachandran_statementContext* ramachandran_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_angle_db_restraintContext* dihedral_angle_db_restraint();

  class  Radius_of_gyration_restraintContext : public antlr4::ParserRuleContext {
  public:
    Radius_of_gyration_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Collapse();
    antlr4::tree::TerminalNode *End();
    std::vector<Collapse_statementContext *> collapse_statement();
    Collapse_statementContext* collapse_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Radius_of_gyration_restraintContext* radius_of_gyration_restraint();

  class  Diffusion_anisotropy_restraintContext : public antlr4::ParserRuleContext {
  public:
    Diffusion_anisotropy_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Danisotropy();
    antlr4::tree::TerminalNode *End();
    std::vector<Diffusion_statementContext *> diffusion_statement();
    Diffusion_statementContext* diffusion_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Diffusion_anisotropy_restraintContext* diffusion_anisotropy_restraint();

  class  Orientation_db_restraintContext : public antlr4::ParserRuleContext {
  public:
    Orientation_db_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Orient();
    antlr4::tree::TerminalNode *End();
    std::vector<Orientation_statementContext *> orientation_statement();
    Orientation_statementContext* orientation_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Orientation_db_restraintContext* orientation_db_restraint();

  class  Csa_restraintContext : public antlr4::ParserRuleContext {
  public:
    Csa_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Dcsa();
    antlr4::tree::TerminalNode *End();
    std::vector<Csa_statementContext *> csa_statement();
    Csa_statementContext* csa_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Csa_restraintContext* csa_restraint();

  class  Pcsa_restraintContext : public antlr4::ParserRuleContext {
  public:
    Pcsa_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Pcsa();
    antlr4::tree::TerminalNode *End();
    std::vector<Pcsa_statementContext *> pcsa_statement();
    Pcsa_statementContext* pcsa_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pcsa_restraintContext* pcsa_restraint();

  class  One_bond_coupling_restraintContext : public antlr4::ParserRuleContext {
  public:
    One_bond_coupling_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *OneBond();
    antlr4::tree::TerminalNode *End();
    std::vector<One_bond_coupling_statementContext *> one_bond_coupling_statement();
    One_bond_coupling_statementContext* one_bond_coupling_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  One_bond_coupling_restraintContext* one_bond_coupling_restraint();

  class  Angle_db_restraintContext : public antlr4::ParserRuleContext {
  public:
    Angle_db_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *AngleDb();
    antlr4::tree::TerminalNode *End();
    std::vector<Angle_db_statementContext *> angle_db_statement();
    Angle_db_statementContext* angle_db_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angle_db_restraintContext* angle_db_restraint();

  class  Pre_restraintContext : public antlr4::ParserRuleContext {
  public:
    Pre_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *PMagnetic();
    antlr4::tree::TerminalNode *End();
    std::vector<Pre_statementContext *> pre_statement();
    Pre_statementContext* pre_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pre_restraintContext* pre_restraint();

  class  Pcs_restraintContext : public antlr4::ParserRuleContext {
  public:
    Pcs_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Xpcs();
    antlr4::tree::TerminalNode *End();
    std::vector<Pcs_statementContext *> pcs_statement();
    Pcs_statementContext* pcs_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pcs_restraintContext* pcs_restraint();

  class  Prdc_restraintContext : public antlr4::ParserRuleContext {
  public:
    Prdc_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Xrdcoupling();
    antlr4::tree::TerminalNode *End();
    std::vector<Prdc_statementContext *> prdc_statement();
    Prdc_statementContext* prdc_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Prdc_restraintContext* prdc_restraint();

  class  Porientation_restraintContext : public antlr4::ParserRuleContext {
  public:
    Porientation_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Xangle();
    antlr4::tree::TerminalNode *End();
    std::vector<Porientation_statementContext *> porientation_statement();
    Porientation_statementContext* porientation_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Porientation_restraintContext* porientation_restraint();

  class  Pccr_restraintContext : public antlr4::ParserRuleContext {
  public:
    Pccr_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Xccr();
    antlr4::tree::TerminalNode *End();
    std::vector<Pccr_statementContext *> pccr_statement();
    Pccr_statementContext* pccr_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pccr_restraintContext* pccr_restraint();

  class  Hbond_restraintContext : public antlr4::ParserRuleContext {
  public:
    Hbond_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Hbda();
    antlr4::tree::TerminalNode *End();
    std::vector<Hbond_statementContext *> hbond_statement();
    Hbond_statementContext* hbond_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Hbond_restraintContext* hbond_restraint();

  class  Hbond_db_restraintContext : public antlr4::ParserRuleContext {
  public:
    Hbond_db_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Hbdb();
    antlr4::tree::TerminalNode *End();
    std::vector<Hbond_db_statementContext *> hbond_db_statement();
    Hbond_db_statementContext* hbond_db_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Hbond_db_restraintContext* hbond_db_restraint();

  class  Noe_statementContext : public antlr4::ParserRuleContext {
  public:
    Noe_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Noe_assignContext *noe_assign();
    Noe_assign_loopContext *noe_assign_loop();
    antlr4::tree::TerminalNode *Asymptote();
    std::vector<Class_nameContext *> class_name();
    Class_nameContext* class_name(size_t i);
    Number_sContext *number_s();
    antlr4::tree::TerminalNode *Average();
    antlr4::tree::TerminalNode *Class_name_AM();
    antlr4::tree::TerminalNode *Averaging_methods();
    antlr4::tree::TerminalNode *Bhig();
    antlr4::tree::TerminalNode *Ceiling();
    antlr4::tree::TerminalNode *Equ_op();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *CountViol();
    antlr4::tree::TerminalNode *Distribute();
    antlr4::tree::TerminalNode *Monomers();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Ncount();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Class_name_PT();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Predict();
    Predict_statementContext *predict_statement();
    antlr4::tree::TerminalNode *End();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *Rswitch();
    antlr4::tree::TerminalNode *Scale();
    antlr4::tree::TerminalNode *SoExponent();
    antlr4::tree::TerminalNode *SqConstant();
    antlr4::tree::TerminalNode *SqExponent();
    antlr4::tree::TerminalNode *SqOffset();
    antlr4::tree::TerminalNode *Temperature();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Noe_statementContext* noe_statement();

  class  Noe_assignContext : public antlr4::ParserRuleContext {
  public:
    Noe_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Assign();
    antlr4::tree::TerminalNode* Assign(size_t i);
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<Noe_annotationContext *> noe_annotation();
    Noe_annotationContext* noe_annotation(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Or_op();
    antlr4::tree::TerminalNode* Or_op(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Noe_assignContext* noe_assign();

  class  Predict_statementContext : public antlr4::ParserRuleContext {
  public:
    Predict_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Cutoff();
    Number_sContext *number_s();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Cuton();
    antlr4::tree::TerminalNode *From();
    SelectionContext *selection();
    antlr4::tree::TerminalNode *To();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Predict_statementContext* predict_statement();

  class  Noe_annotationContext : public antlr4::ParserRuleContext {
  public:
    Noe_annotationContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Peak();
    Number_aContext *number_a();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Spectrum();
    antlr4::tree::TerminalNode *Weight();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Vol();
    antlr4::tree::TerminalNode *Ppm1();
    antlr4::tree::TerminalNode *Ppm2();
    antlr4::tree::TerminalNode *Cv();
    antlr4::tree::TerminalNode *Comma();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Noe_annotationContext* noe_annotation();

  class  Dihedral_statementContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Vector_statementContext *vector_statement();
    Dihedral_assignContext *dihedral_assign();
    Dihedral_assign_loopContext *dihedral_assign_loop();
    antlr4::tree::TerminalNode *Nassign();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *Scale();
    Number_sContext *number_s();
    antlr4::tree::TerminalNode *Print_any();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_statementContext* dihedral_statement();

  class  Dihedral_assignContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_assignContext* dihedral_assign();

  class  Sani_statementContext : public antlr4::ParserRuleContext {
  public:
    Sani_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Sani_assignContext *sani_assign();
    Sani_assign_loopContext *sani_assign_loop();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Coefficients();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Reset();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Sani_statementContext* sani_statement();

  class  Sani_assignContext : public antlr4::ParserRuleContext {
  public:
    Sani_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Sani_assignContext* sani_assign();

  class  Xdip_statementContext : public antlr4::ParserRuleContext {
  public:
    Xdip_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Xdip_assignContext *xdip_assign();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Type();
    antlr4::tree::TerminalNode *Rdc_dist_fix_types();
    antlr4::tree::TerminalNode *Scale();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Sign();
    antlr4::tree::TerminalNode *Logical();
    antlr4::tree::TerminalNode *Average();
    antlr4::tree::TerminalNode *Averaging_methods();
    antlr4::tree::TerminalNode *Coefficients();
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Reset();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Xdip_statementContext* xdip_statement();

  class  Xdip_assignContext : public antlr4::ParserRuleContext {
  public:
    Xdip_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Xdip_assignContext* xdip_assign();

  class  Vean_statementContext : public antlr4::ParserRuleContext {
  public:
    Vean_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Vean_assignContext *vean_assign();
    antlr4::tree::TerminalNode *Cv();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Equ_op();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *ForceConstant();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Partition();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Reset();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Vean_statementContext* vean_statement();

  class  Vean_assignContext : public antlr4::ParserRuleContext {
  public:
    Vean_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Vean_assignContext* vean_assign();

  class  Tenso_statementContext : public antlr4::ParserRuleContext {
  public:
    Tenso_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Tenso_assignContext *tenso_assign();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Coefficients();
    Number_sContext *number_s();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Reset();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Tenso_statementContext* tenso_statement();

  class  Tenso_assignContext : public antlr4::ParserRuleContext {
  public:
    Tenso_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Tenso_assignContext* tenso_assign();

  class  Anis_statementContext : public antlr4::ParserRuleContext {
  public:
    Anis_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Anis_assignContext *anis_assign();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Coefficients();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *Type();
    antlr4::tree::TerminalNode *Rdc_or_Diff_anis_types();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Anis_statementContext* anis_statement();

  class  Anis_assignContext : public antlr4::ParserRuleContext {
  public:
    Anis_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Anis_assignContext* anis_assign();

  class  Planar_statementContext : public antlr4::ParserRuleContext {
  public:
    Planar_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Vector_statementContext *vector_statement();
    Planar_groupContext *planar_group();
    Planar_group_loopContext *planar_group_loop();
    antlr4::tree::TerminalNode *Initialize();
    antlr4::tree::TerminalNode *Print_any();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Planar_statementContext* planar_statement();

  class  Planar_groupContext : public antlr4::ParserRuleContext {
  public:
    Planar_groupContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Group();
    antlr4::tree::TerminalNode *End();
    std::vector<Group_statementContext *> group_statement();
    Group_statementContext* group_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Planar_groupContext* planar_group();

  class  Group_statementContext : public antlr4::ParserRuleContext {
  public:
    Group_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Selection();
    SelectionContext *selection();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Weight();
    Number_sContext *number_s();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Group_statementContext* group_statement();

  class  Harmonic_statementContext : public antlr4::ParserRuleContext {
  public:
    Harmonic_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Vector_statementContext *vector_statement();
    antlr4::tree::TerminalNode *Exponent();
    antlr4::tree::TerminalNode *Integer();
    std::vector<antlr4::tree::TerminalNode *> Equ_op();
    antlr4::tree::TerminalNode* Equ_op(size_t i);
    antlr4::tree::TerminalNode *Normal();
    antlr4::tree::TerminalNode *L_paren();
    antlr4::tree::TerminalNode *R_paren();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *Tail();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Comma();
    antlr4::tree::TerminalNode* Comma(size_t i);
    antlr4::tree::TerminalNode *Head();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Harmonic_statementContext* harmonic_statement();

  class  Harmonic_assignContext : public antlr4::ParserRuleContext {
  public:
    Harmonic_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    SelectionContext *selection();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Harmonic_assignContext* harmonic_assign();

  class  Antidistance_statementContext : public antlr4::ParserRuleContext {
  public:
    Antidistance_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Xadc_assignContext *xadc_assign();
    Xadc_assign_loopContext *xadc_assign_loop();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Expectation();
    antlr4::tree::TerminalNode *Integer();
    Number_sContext *number_s();
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *All();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *Size();
    antlr4::tree::TerminalNode *Zero();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Antidistance_statementContext* antidistance_statement();

  class  Xadc_assignContext : public antlr4::ParserRuleContext {
  public:
    Xadc_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Xadc_assignContext* xadc_assign();

  class  Coupling_statementContext : public antlr4::ParserRuleContext {
  public:
    Coupling_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Coup_assignContext *coup_assign();
    Coup_assign_loopContext *coup_assign_loop();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Coefficients();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *Cv();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Degeneracy();
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Partition();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *All();
    antlr4::tree::TerminalNode *Reset();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coupling_statementContext* coupling_statement();

  class  Coup_assignContext : public antlr4::ParserRuleContext {
  public:
    Coup_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coup_assignContext* coup_assign();

  class  Carbon_shift_statementContext : public antlr4::ParserRuleContext {
  public:
    Carbon_shift_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Carbon_shift_assignContext *carbon_shift_assign();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Expectation();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *PhiStep();
    antlr4::tree::TerminalNode *PsiStep();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    Carbon_shift_rcoilContext *carbon_shift_rcoil();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *Zero();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Carbon_shift_statementContext* carbon_shift_statement();

  class  Carbon_shift_assignContext : public antlr4::ParserRuleContext {
  public:
    Carbon_shift_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Carbon_shift_assignContext* carbon_shift_assign();

  class  Carbon_shift_rcoilContext : public antlr4::ParserRuleContext {
  public:
    Carbon_shift_rcoilContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Rcoil();
    SelectionContext *selection();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Carbon_shift_rcoilContext* carbon_shift_rcoil();

  class  Proton_shift_statementContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    ObservedContext *observed();
    Proton_shift_rcoilContext *proton_shift_rcoil();
    Proton_shift_anisotropyContext *proton_shift_anisotropy();
    Proton_shift_amidesContext *proton_shift_amides();
    Proton_shift_carbonsContext *proton_shift_carbons();
    Proton_shift_nitrogensContext *proton_shift_nitrogens();
    Proton_shift_oxygensContext *proton_shift_oxygens();
    Proton_shift_ring_atomsContext *proton_shift_ring_atoms();
    Proton_shift_alphas_and_amidesContext *proton_shift_alphas_and_amides();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Error();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *Degeneracy();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *All();
    antlr4::tree::TerminalNode *Reset();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_statementContext* proton_shift_statement();

  class  ObservedContext : public antlr4::ParserRuleContext {
  public:
    ObservedContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Observed();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ObservedContext* observed();

  class  Proton_shift_rcoilContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_rcoilContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Rcoil();
    SelectionContext *selection();
    NumberContext *number();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_rcoilContext* proton_shift_rcoil();

  class  Proton_shift_anisotropyContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_anisotropyContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Anisotropy();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    antlr4::tree::TerminalNode *Logical();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_anisotropyContext* proton_shift_anisotropy();

  class  Proton_shift_amidesContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_amidesContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Amides();
    SelectionContext *selection();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_amidesContext* proton_shift_amides();

  class  Proton_shift_carbonsContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_carbonsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Carbon();
    SelectionContext *selection();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_carbonsContext* proton_shift_carbons();

  class  Proton_shift_nitrogensContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_nitrogensContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Nitrogens();
    SelectionContext *selection();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_nitrogensContext* proton_shift_nitrogens();

  class  Proton_shift_oxygensContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_oxygensContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Oxygens();
    SelectionContext *selection();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_oxygensContext* proton_shift_oxygens();

  class  Proton_shift_ring_atomsContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_ring_atomsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RingAtoms();
    antlr4::tree::TerminalNode *Simple_name();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_ring_atomsContext* proton_shift_ring_atoms();

  class  Proton_shift_alphas_and_amidesContext : public antlr4::ParserRuleContext {
  public:
    Proton_shift_alphas_and_amidesContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *AlphasAndAmides();
    SelectionContext *selection();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Proton_shift_alphas_and_amidesContext* proton_shift_alphas_and_amides();

  class  Ramachandran_statementContext : public antlr4::ParserRuleContext {
  public:
    Ramachandran_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Rama_assignContext *rama_assign();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Cutoff();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Gaussian();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Phase();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *All();
    antlr4::tree::TerminalNode *Quartic();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *Scale();
    antlr4::tree::TerminalNode *Shape();
    antlr4::tree::TerminalNode *Gauss_or_Quart();
    antlr4::tree::TerminalNode *Size();
    antlr4::tree::TerminalNode *Dimensions();
    antlr4::tree::TerminalNode *Sort();
    antlr4::tree::TerminalNode *Zero();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ramachandran_statementContext* ramachandran_statement();

  class  Rama_assignContext : public antlr4::ParserRuleContext {
  public:
    Rama_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Rama_assignContext* rama_assign();

  class  Collapse_statementContext : public antlr4::ParserRuleContext {
  public:
    Collapse_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Coll_assignContext *coll_assign();
    Coll_assign_loopContext *coll_assign_loop();
    antlr4::tree::TerminalNode *Scale();
    Number_sContext *number_s();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Reset();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Collapse_statementContext* collapse_statement();

  class  Coll_assignContext : public antlr4::ParserRuleContext {
  public:
    Coll_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    SelectionContext *selection();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coll_assignContext* coll_assign();

  class  Diffusion_statementContext : public antlr4::ParserRuleContext {
  public:
    Diffusion_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Dani_assignContext *dani_assign();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Coefficients();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *Type();
    antlr4::tree::TerminalNode *Rdc_or_Diff_anis_types();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Diffusion_statementContext* diffusion_statement();

  class  Dani_assignContext : public antlr4::ParserRuleContext {
  public:
    Dani_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dani_assignContext* dani_assign();

  class  Orientation_statementContext : public antlr4::ParserRuleContext {
  public:
    Orientation_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Orie_assignContext *orie_assign();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Cutoff();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *Height();
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Gaussian();
    antlr4::tree::TerminalNode *MaxGaussians();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *NewGaussian();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *All();
    antlr4::tree::TerminalNode *Quartic();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *Residue();
    antlr4::tree::TerminalNode *Size();
    antlr4::tree::TerminalNode *Zero();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Orientation_statementContext* orientation_statement();

  class  Orie_assignContext : public antlr4::ParserRuleContext {
  public:
    Orie_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Orie_assignContext* orie_assign();

  class  Csa_statementContext : public antlr4::ParserRuleContext {
  public:
    Csa_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Csa_assignContext *csa_assign();
    Csa_assign_loopContext *csa_assign_loop();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Scale();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Type();
    antlr4::tree::TerminalNode *Csa_types();
    antlr4::tree::TerminalNode *Coefficients();
    antlr4::tree::TerminalNode *Sigma();
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Reset();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Csa_statementContext* csa_statement();

  class  Csa_assignContext : public antlr4::ParserRuleContext {
  public:
    Csa_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Csa_assignContext* csa_assign();

  class  Pcsa_statementContext : public antlr4::ParserRuleContext {
  public:
    Pcsa_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Csa_assignContext *csa_assign();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Scale();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Coefficients();
    antlr4::tree::TerminalNode *Sigma();
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Reset();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pcsa_statementContext* pcsa_statement();

  class  One_bond_coupling_statementContext : public antlr4::ParserRuleContext {
  public:
    One_bond_coupling_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    One_bond_assignContext *one_bond_assign();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Coefficients();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Reset();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  One_bond_coupling_statementContext* one_bond_coupling_statement();

  class  One_bond_assignContext : public antlr4::ParserRuleContext {
  public:
    One_bond_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  One_bond_assignContext* one_bond_assign();

  class  Angle_db_statementContext : public antlr4::ParserRuleContext {
  public:
    Angle_db_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Angle_db_assignContext *angle_db_assign();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *DerivFlag();
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Expectation();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    Number_sContext *number_s();
    antlr4::tree::TerminalNode *Error();
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *All();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *Size();
    antlr4::tree::TerminalNode *AngleDb();
    antlr4::tree::TerminalNode *Dihedral();
    antlr4::tree::TerminalNode *Zero();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angle_db_statementContext* angle_db_statement();

  class  Angle_db_assignContext : public antlr4::ParserRuleContext {
  public:
    Angle_db_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angle_db_assignContext* angle_db_assign();

  class  Pre_statementContext : public antlr4::ParserRuleContext {
  public:
    Pre_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Pre_assignContext *pre_assign();
    Pre_assign_loopContext *pre_assign_loop();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *ForceConstant();
    Class_nameContext *class_name();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Potential();
    antlr4::tree::TerminalNode *Class_name_PT();
    antlr4::tree::TerminalNode *Potential_types();
    antlr4::tree::TerminalNode *Equ_op_PT();
    antlr4::tree::TerminalNode *Kconst();
    antlr4::tree::TerminalNode *Omega();
    antlr4::tree::TerminalNode *Tauc();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *All();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *Debug();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pre_statementContext* pre_statement();

  class  Pre_assignContext : public antlr4::ParserRuleContext {
  public:
    Pre_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pre_assignContext* pre_assign();

  class  Pcs_statementContext : public antlr4::ParserRuleContext {
  public:
    Pcs_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Pcs_assignContext *pcs_assign();
    Pcs_assign_loopContext *pcs_assign_loop();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Tolerance();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Coefficients();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *All();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *Save();
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Fmed();
    antlr4::tree::TerminalNode *ErrOn();
    antlr4::tree::TerminalNode *ErrOff();
    antlr4::tree::TerminalNode *Fon();
    antlr4::tree::TerminalNode *Foff();
    antlr4::tree::TerminalNode *Son();
    antlr4::tree::TerminalNode *Soff();
    antlr4::tree::TerminalNode *Frun();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pcs_statementContext* pcs_statement();

  class  Pcs_assignContext : public antlr4::ParserRuleContext {
  public:
    Pcs_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pcs_assignContext* pcs_assign();

  class  Prdc_statementContext : public antlr4::ParserRuleContext {
  public:
    Prdc_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Prdc_assignContext *prdc_assign();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Tolerance();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Coefficients();
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *ErrOn();
    antlr4::tree::TerminalNode *ErrOff();
    antlr4::tree::TerminalNode *Fmed();
    antlr4::tree::TerminalNode *Fon();
    antlr4::tree::TerminalNode *Foff();
    antlr4::tree::TerminalNode *Frun();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *Save();
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Son();
    antlr4::tree::TerminalNode *Soff();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Prdc_statementContext* prdc_statement();

  class  Prdc_assignContext : public antlr4::ParserRuleContext {
  public:
    Prdc_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Prdc_assignContext* prdc_assign();

  class  Porientation_statementContext : public antlr4::ParserRuleContext {
  public:
    Porientation_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Porientation_assignContext *porientation_assign();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *ForceConstant();
    Number_sContext *number_s();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Reset();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Porientation_statementContext* porientation_statement();

  class  Porientation_assignContext : public antlr4::ParserRuleContext {
  public:
    Porientation_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Porientation_assignContext* porientation_assign();

  class  Pccr_statementContext : public antlr4::ParserRuleContext {
  public:
    Pccr_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Pccr_assignContext *pccr_assign();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *Weip();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Coefficients();
    Number_sContext *number_s();
    antlr4::tree::TerminalNode *ForceConstant();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *Frun();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pccr_statementContext* pccr_statement();

  class  Pccr_assignContext : public antlr4::ParserRuleContext {
  public:
    Pccr_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pccr_assignContext* pccr_assign();

  class  Hbond_statementContext : public antlr4::ParserRuleContext {
  public:
    Hbond_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Hbond_assignContext *hbond_assign();
    Hbond_assign_loopContext *hbond_assign_loop();
    ClassificationContext *classification();
    antlr4::tree::TerminalNode *ForceConstant();
    Number_sContext *number_s();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Nrestraints();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Print();
    antlr4::tree::TerminalNode *Threshold();
    antlr4::tree::TerminalNode *Reset();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Hbond_statementContext* hbond_statement();

  class  Hbond_assignContext : public antlr4::ParserRuleContext {
  public:
    Hbond_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Hbond_assignContext* hbond_assign();

  class  Hbond_db_statementContext : public antlr4::ParserRuleContext {
  public:
    Hbond_db_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Hbond_db_assignContext *hbond_db_assign();
    Hbond_db_assign_loopContext *hbond_db_assign_loop();
    antlr4::tree::TerminalNode *Kdir();
    Number_sContext *number_s();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Klin();
    antlr4::tree::TerminalNode *Nseg();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Nmin();
    antlr4::tree::TerminalNode *Nmax();
    antlr4::tree::TerminalNode *Segm();
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Ohcut();
    antlr4::tree::TerminalNode *Coh1cut();
    antlr4::tree::TerminalNode *Coh2cut();
    antlr4::tree::TerminalNode *Ohncut();
    antlr4::tree::TerminalNode *Updfrq();
    antlr4::tree::TerminalNode *Prnfrq();
    antlr4::tree::TerminalNode *Freemode();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Hbond_db_statementContext* hbond_db_statement();

  class  Hbond_db_assignContext : public antlr4::ParserRuleContext {
  public:
    Hbond_db_assignContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Assign();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Hbond_db_assignContext* hbond_db_assign();

  class  Ncs_restraintContext : public antlr4::ParserRuleContext {
  public:
    Ncs_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Ncs();
    antlr4::tree::TerminalNode *Restraints();
    antlr4::tree::TerminalNode *End();
    std::vector<Ncs_statementContext *> ncs_statement();
    Ncs_statementContext* ncs_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ncs_restraintContext* ncs_restraint();

  class  Ncs_statementContext : public antlr4::ParserRuleContext {
  public:
    Ncs_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Group();
    antlr4::tree::TerminalNode *End();
    std::vector<Ncs_group_statementContext *> ncs_group_statement();
    Ncs_group_statementContext* ncs_group_statement(size_t i);
    antlr4::tree::TerminalNode *Initialize();
    antlr4::tree::TerminalNode *Print_any();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ncs_statementContext* ncs_statement();

  class  Ncs_group_statementContext : public antlr4::ParserRuleContext {
  public:
    Ncs_group_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Equivalence();
    SelectionContext *selection();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Sigb();
    Number_sContext *number_s();
    antlr4::tree::TerminalNode *Weight();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ncs_group_statementContext* ncs_group_statement();

  class  SelectionContext : public antlr4::ParserRuleContext {
  public:
    SelectionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_paren();
    Selection_expressionContext *selection_expression();
    antlr4::tree::TerminalNode *R_paren();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  SelectionContext* selection();

  class  Selection_expressionContext : public antlr4::ParserRuleContext {
  public:
    Selection_expressionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<TermContext *> term();
    TermContext* term(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Or_op();
    antlr4::tree::TerminalNode* Or_op(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Selection_expressionContext* selection_expression();

  class  TermContext : public antlr4::ParserRuleContext {
  public:
    TermContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<FactorContext *> factor();
    FactorContext* factor(size_t i);
    std::vector<antlr4::tree::TerminalNode *> And_op();
    antlr4::tree::TerminalNode* And_op(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  TermContext* term();

  class  FactorContext : public antlr4::ParserRuleContext {
  public:
    FactorContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_paren();
    Selection_expressionContext *selection_expression();
    antlr4::tree::TerminalNode *R_paren();
    antlr4::tree::TerminalNode *All();
    antlr4::tree::TerminalNode *Atom();
    std::vector<antlr4::tree::TerminalNode *> Simple_names();
    antlr4::tree::TerminalNode* Simple_names(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Double_quote_string();
    antlr4::tree::TerminalNode* Double_quote_string(size_t i);
    antlr4::tree::TerminalNode *Integers();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    antlr4::tree::TerminalNode *Logical();
    antlr4::tree::TerminalNode *Attribute();
    antlr4::tree::TerminalNode *Attr_properties();
    antlr4::tree::TerminalNode *Comparison_ops();
    std::vector<Number_fContext *> number_f();
    Number_fContext* number_f(size_t i);
    antlr4::tree::TerminalNode *Abs();
    antlr4::tree::TerminalNode *BondedTo();
    FactorContext *factor();
    antlr4::tree::TerminalNode *ByGroup();
    antlr4::tree::TerminalNode *ByRes();
    antlr4::tree::TerminalNode *Chemical();
    antlr4::tree::TerminalNode *Symbol_name();
    antlr4::tree::TerminalNode *Colon();
    antlr4::tree::TerminalNode *Hydrogen();
    antlr4::tree::TerminalNode *Id();
    antlr4::tree::TerminalNode *Known();
    antlr4::tree::TerminalNode *Name();
    antlr4::tree::TerminalNode *Not_op();
    antlr4::tree::TerminalNode *Point();
    antlr4::tree::TerminalNode *Cut();
    std::vector<antlr4::tree::TerminalNode *> Comma();
    antlr4::tree::TerminalNode* Comma(size_t i);
    antlr4::tree::TerminalNode *Tail();
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Equ_op();
    antlr4::tree::TerminalNode* Equ_op(size_t i);
    antlr4::tree::TerminalNode *Head();
    antlr4::tree::TerminalNode *Previous();
    antlr4::tree::TerminalNode *Pseudo();
    antlr4::tree::TerminalNode *Residue();
    antlr4::tree::TerminalNode *Resname();
    antlr4::tree::TerminalNode *SegIdentifier();
    antlr4::tree::TerminalNode *Store1();
    antlr4::tree::TerminalNode *Store2();
    antlr4::tree::TerminalNode *Store3();
    antlr4::tree::TerminalNode *Store4();
    antlr4::tree::TerminalNode *Store5();
    antlr4::tree::TerminalNode *Store6();
    antlr4::tree::TerminalNode *Store7();
    antlr4::tree::TerminalNode *Store8();
    antlr4::tree::TerminalNode *Store9();
    antlr4::tree::TerminalNode *Tag();
    antlr4::tree::TerminalNode *Donor();
    antlr4::tree::TerminalNode *Acceptor();
    antlr4::tree::TerminalNode *Around();
    antlr4::tree::TerminalNode *Saround();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  FactorContext* factor();
  FactorContext* factor(int precedence);
  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Symbol_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NumberContext* number();

  class  Number_fContext : public antlr4::ParserRuleContext {
  public:
    Number_fContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Number_fContext* number_f();

  class  Number_sContext : public antlr4::ParserRuleContext {
  public:
    Number_sContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Symbol_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Number_sContext* number_s();

  class  Number_aContext : public antlr4::ParserRuleContext {
  public:
    Number_aContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Number_aContext* number_a();

  class  ClassificationContext : public antlr4::ParserRuleContext {
  public:
    ClassificationContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Classification();
    Class_nameContext *class_name();
    antlr4::tree::TerminalNode *Equ_op();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  ClassificationContext* classification();

  class  Class_nameContext : public antlr4::ParserRuleContext {
  public:
    Class_nameContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Noe();
    antlr4::tree::TerminalNode *Restraints();
    antlr4::tree::TerminalNode *AngleDb();
    antlr4::tree::TerminalNode *HBonded();
    antlr4::tree::TerminalNode *Dihedral();
    antlr4::tree::TerminalNode *Improper();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Class_nameContext* class_name();

  class  Flag_statementContext : public antlr4::ParserRuleContext {
  public:
    Flag_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Flags();
    antlr4::tree::TerminalNode *Include();
    antlr4::tree::TerminalNode *End_FL();
    antlr4::tree::TerminalNode *Exclude();
    std::vector<antlr4::tree::TerminalNode *> Class_name();
    antlr4::tree::TerminalNode* Class_name(size_t i);
    antlr4::tree::TerminalNode *Any_class();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Flag_statementContext* flag_statement();

  class  Vector_statementContext : public antlr4::ParserRuleContext {
  public:
    Vector_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Vector();
    Vector_modeContext *vector_mode();
    SelectionContext *selection();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Vector_statementContext* vector_statement();

  class  Vector_modeContext : public antlr4::ParserRuleContext {
  public:
    Vector_modeContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Vector_expressionContext *vector_expression();
    antlr4::tree::TerminalNode *R_paren_VE();
    antlr4::tree::TerminalNode *Do_Lp();
    antlr4::tree::TerminalNode *Identity_Lp();
    antlr4::tree::TerminalNode *Show();
    Vector_show_propertyContext *vector_show_property();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Vector_modeContext* vector_mode();

  class  Vector_expressionContext : public antlr4::ParserRuleContext {
  public:
    Vector_expressionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Atom_properties_VE();
    antlr4::tree::TerminalNode *Equ_op_VE();
    Vector_operationContext *vector_operation();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Vector_expressionContext* vector_expression();

  class  Vector_operationContext : public antlr4::ParserRuleContext {
  public:
    Vector_operationContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    VflcContext *vflc();
    Vector_operationContext *vector_operation();
    antlr4::tree::TerminalNode *Add_op_VE();
    antlr4::tree::TerminalNode *Sub_op_VE();
    antlr4::tree::TerminalNode *Mul_op_VE();
    antlr4::tree::TerminalNode *Div_op_VE();
    antlr4::tree::TerminalNode *Exp_op_VE();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Vector_operationContext* vector_operation();

  class  VflcContext : public antlr4::ParserRuleContext {
  public:
    VflcContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Atom_properties_VE();
    Vector_func_callContext *vector_func_call();
    antlr4::tree::TerminalNode *Integer_VE();
    antlr4::tree::TerminalNode *Real_VE();
    antlr4::tree::TerminalNode *Simple_name_VE();
    antlr4::tree::TerminalNode *Symbol_name_VE();
    antlr4::tree::TerminalNode *Double_quote_string_VE();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  VflcContext* vflc();

  class  Vector_func_callContext : public antlr4::ParserRuleContext {
  public:
    Vector_func_callContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Abs_VE();
    antlr4::tree::TerminalNode *L_paren_VF();
    std::vector<VflcContext *> vflc();
    VflcContext* vflc(size_t i);
    antlr4::tree::TerminalNode *R_paren_VE();
    antlr4::tree::TerminalNode *Acos_VE();
    antlr4::tree::TerminalNode *Cos_VE();
    antlr4::tree::TerminalNode *Decode_VE();
    antlr4::tree::TerminalNode *Encode_VE();
    antlr4::tree::TerminalNode *Exp_VE();
    antlr4::tree::TerminalNode *Gauss_VE();
    antlr4::tree::TerminalNode *Heavy_VE();
    antlr4::tree::TerminalNode *Int_VE();
    antlr4::tree::TerminalNode *Log10_VE();
    antlr4::tree::TerminalNode *Log_VE();
    antlr4::tree::TerminalNode *Max_VE();
    std::vector<antlr4::tree::TerminalNode *> Comma_VE();
    antlr4::tree::TerminalNode* Comma_VE(size_t i);
    antlr4::tree::TerminalNode *Maxw_VE();
    antlr4::tree::TerminalNode *Min_VE();
    antlr4::tree::TerminalNode *Mod_VE();
    antlr4::tree::TerminalNode *Norm_VE();
    antlr4::tree::TerminalNode *Random_VE();
    antlr4::tree::TerminalNode *Sign_VE();
    antlr4::tree::TerminalNode *Sin_VE();
    antlr4::tree::TerminalNode *Sqrt_VE();
    antlr4::tree::TerminalNode *Tan_VE();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Vector_func_callContext* vector_func_call();

  class  Vector_show_propertyContext : public antlr4::ParserRuleContext {
  public:
    Vector_show_propertyContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *L_paren_VS();
    antlr4::tree::TerminalNode *Atom_properties_VS();
    antlr4::tree::TerminalNode *R_paren_VS();
    antlr4::tree::TerminalNode *Average_VS();
    antlr4::tree::TerminalNode *Element_VS();
    antlr4::tree::TerminalNode *Max_VS();
    antlr4::tree::TerminalNode *Min_VS();
    antlr4::tree::TerminalNode *Norm_VS();
    antlr4::tree::TerminalNode *Rms_VS();
    antlr4::tree::TerminalNode *Sum_VS();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Vector_show_propertyContext* vector_show_property();

  class  Evaluate_statementContext : public antlr4::ParserRuleContext {
  public:
    Evaluate_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Evaluate_Lp();
    antlr4::tree::TerminalNode *Symbol_name_VE();
    antlr4::tree::TerminalNode *Equ_op_VE();
    Evaluate_operationContext *evaluate_operation();
    antlr4::tree::TerminalNode *R_paren_VE();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Evaluate_statementContext* evaluate_statement();

  class  Evaluate_operationContext : public antlr4::ParserRuleContext {
  public:
    Evaluate_operationContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    VflcContext *vflc();
    Evaluate_operationContext *evaluate_operation();
    antlr4::tree::TerminalNode *Add_op_VE();
    antlr4::tree::TerminalNode *Sub_op_VE();
    antlr4::tree::TerminalNode *Mul_op_VE();
    antlr4::tree::TerminalNode *Div_op_VE();
    antlr4::tree::TerminalNode *Exp_op_VE();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Evaluate_operationContext* evaluate_operation();

  class  Patch_statementContext : public antlr4::ParserRuleContext {
  public:
    Patch_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Patch();
    std::vector<antlr4::tree::TerminalNode *> Reference();
    antlr4::tree::TerminalNode* Reference(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Equ_op();
    antlr4::tree::TerminalNode* Equ_op(size_t i);
    std::vector<SelectionContext *> selection();
    SelectionContext* selection(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<antlr4::tree::TerminalNode *> Nil();
    antlr4::tree::TerminalNode* Nil(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    Class_nameContext *class_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Patch_statementContext* patch_statement();

  class  Parameter_settingContext : public antlr4::ParserRuleContext {
  public:
    Parameter_settingContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Parameter();
    antlr4::tree::TerminalNode *End();
    std::vector<Parameter_statementContext *> parameter_statement();
    Parameter_statementContext* parameter_statement(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Parameter_settingContext* parameter_setting();

  class  Parameter_statementContext : public antlr4::ParserRuleContext {
  public:
    Parameter_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *AngleDb();
    std::vector<antlr4::tree::TerminalNode *> Simple_name();
    antlr4::tree::TerminalNode* Simple_name(size_t i);
    std::vector<Number_sContext *> number_s();
    Number_sContext* number_s(size_t i);
    antlr4::tree::TerminalNode *UB();
    antlr4::tree::TerminalNode *BondedTo();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    antlr4::tree::TerminalNode *Dihedral();
    antlr4::tree::TerminalNode *Improper();
    antlr4::tree::TerminalNode *Mult();
    antlr4::tree::TerminalNode *HBonded();
    std::vector<antlr4::tree::TerminalNode *> Simple_names();
    antlr4::tree::TerminalNode* Simple_names(size_t i);
    antlr4::tree::TerminalNode *NBFix();
    antlr4::tree::TerminalNode *NonB();
    antlr4::tree::TerminalNode *Reset();
    antlr4::tree::TerminalNode *VDWOff();
    antlr4::tree::TerminalNode *Verbose();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Parameter_statementContext* parameter_statement();

  class  Noe_assign_loopContext : public antlr4::ParserRuleContext {
  public:
    Noe_assign_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *For();
    antlr4::tree::TerminalNode *Symbol_name_CF();
    antlr4::tree::TerminalNode *In_CF();
    antlr4::tree::TerminalNode *L_paren_CF();
    antlr4::tree::TerminalNode *R_paren_CF();
    std::vector<antlr4::tree::TerminalNode *> Loop();
    antlr4::tree::TerminalNode* Loop(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LL();
    antlr4::tree::TerminalNode* Simple_name_LL(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Noe_assignContext *> noe_assign();
    Noe_assignContext* noe_assign(size_t i);
    std::vector<Distance_restraintContext *> distance_restraint();
    Distance_restraintContext* distance_restraint(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer_CF();
    antlr4::tree::TerminalNode* Integer_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_CF();
    antlr4::tree::TerminalNode* Real_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_CF();
    antlr4::tree::TerminalNode* Simple_name_CF(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Noe_assign_loopContext* noe_assign_loop();

  class  Dihedral_assign_loopContext : public antlr4::ParserRuleContext {
  public:
    Dihedral_assign_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *For();
    antlr4::tree::TerminalNode *Symbol_name_CF();
    antlr4::tree::TerminalNode *In_CF();
    antlr4::tree::TerminalNode *L_paren_CF();
    antlr4::tree::TerminalNode *R_paren_CF();
    std::vector<antlr4::tree::TerminalNode *> Loop();
    antlr4::tree::TerminalNode* Loop(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LL();
    antlr4::tree::TerminalNode* Simple_name_LL(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Dihedral_assignContext *> dihedral_assign();
    Dihedral_assignContext* dihedral_assign(size_t i);
    std::vector<Dihedral_angle_restraintContext *> dihedral_angle_restraint();
    Dihedral_angle_restraintContext* dihedral_angle_restraint(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer_CF();
    antlr4::tree::TerminalNode* Integer_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_CF();
    antlr4::tree::TerminalNode* Real_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_CF();
    antlr4::tree::TerminalNode* Simple_name_CF(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dihedral_assign_loopContext* dihedral_assign_loop();

  class  Sani_assign_loopContext : public antlr4::ParserRuleContext {
  public:
    Sani_assign_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *For();
    antlr4::tree::TerminalNode *Symbol_name_CF();
    antlr4::tree::TerminalNode *In_CF();
    antlr4::tree::TerminalNode *L_paren_CF();
    antlr4::tree::TerminalNode *R_paren_CF();
    std::vector<antlr4::tree::TerminalNode *> Loop();
    antlr4::tree::TerminalNode* Loop(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LL();
    antlr4::tree::TerminalNode* Simple_name_LL(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Sani_assignContext *> sani_assign();
    Sani_assignContext* sani_assign(size_t i);
    std::vector<Rdc_restraintContext *> rdc_restraint();
    Rdc_restraintContext* rdc_restraint(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer_CF();
    antlr4::tree::TerminalNode* Integer_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_CF();
    antlr4::tree::TerminalNode* Real_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_CF();
    antlr4::tree::TerminalNode* Simple_name_CF(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Sani_assign_loopContext* sani_assign_loop();

  class  Xadc_assign_loopContext : public antlr4::ParserRuleContext {
  public:
    Xadc_assign_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *For();
    antlr4::tree::TerminalNode *Symbol_name_CF();
    antlr4::tree::TerminalNode *In_CF();
    antlr4::tree::TerminalNode *L_paren_CF();
    antlr4::tree::TerminalNode *R_paren_CF();
    std::vector<antlr4::tree::TerminalNode *> Loop();
    antlr4::tree::TerminalNode* Loop(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LL();
    antlr4::tree::TerminalNode* Simple_name_LL(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Xadc_assignContext *> xadc_assign();
    Xadc_assignContext* xadc_assign(size_t i);
    std::vector<Antidistance_restraintContext *> antidistance_restraint();
    Antidistance_restraintContext* antidistance_restraint(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer_CF();
    antlr4::tree::TerminalNode* Integer_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_CF();
    antlr4::tree::TerminalNode* Real_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_CF();
    antlr4::tree::TerminalNode* Simple_name_CF(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Xadc_assign_loopContext* xadc_assign_loop();

  class  Coup_assign_loopContext : public antlr4::ParserRuleContext {
  public:
    Coup_assign_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *For();
    antlr4::tree::TerminalNode *Symbol_name_CF();
    antlr4::tree::TerminalNode *In_CF();
    antlr4::tree::TerminalNode *L_paren_CF();
    antlr4::tree::TerminalNode *R_paren_CF();
    std::vector<antlr4::tree::TerminalNode *> Loop();
    antlr4::tree::TerminalNode* Loop(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LL();
    antlr4::tree::TerminalNode* Simple_name_LL(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Coup_assignContext *> coup_assign();
    Coup_assignContext* coup_assign(size_t i);
    std::vector<Coupling_restraintContext *> coupling_restraint();
    Coupling_restraintContext* coupling_restraint(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer_CF();
    antlr4::tree::TerminalNode* Integer_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_CF();
    antlr4::tree::TerminalNode* Real_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_CF();
    antlr4::tree::TerminalNode* Simple_name_CF(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coup_assign_loopContext* coup_assign_loop();

  class  Coll_assign_loopContext : public antlr4::ParserRuleContext {
  public:
    Coll_assign_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *For();
    antlr4::tree::TerminalNode *Symbol_name_CF();
    antlr4::tree::TerminalNode *In_CF();
    antlr4::tree::TerminalNode *L_paren_CF();
    antlr4::tree::TerminalNode *R_paren_CF();
    std::vector<antlr4::tree::TerminalNode *> Loop();
    antlr4::tree::TerminalNode* Loop(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LL();
    antlr4::tree::TerminalNode* Simple_name_LL(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Coll_assignContext *> coll_assign();
    Coll_assignContext* coll_assign(size_t i);
    std::vector<Radius_of_gyration_restraintContext *> radius_of_gyration_restraint();
    Radius_of_gyration_restraintContext* radius_of_gyration_restraint(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer_CF();
    antlr4::tree::TerminalNode* Integer_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_CF();
    antlr4::tree::TerminalNode* Real_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_CF();
    antlr4::tree::TerminalNode* Simple_name_CF(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coll_assign_loopContext* coll_assign_loop();

  class  Csa_assign_loopContext : public antlr4::ParserRuleContext {
  public:
    Csa_assign_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *For();
    antlr4::tree::TerminalNode *Symbol_name_CF();
    antlr4::tree::TerminalNode *In_CF();
    antlr4::tree::TerminalNode *L_paren_CF();
    antlr4::tree::TerminalNode *R_paren_CF();
    std::vector<antlr4::tree::TerminalNode *> Loop();
    antlr4::tree::TerminalNode* Loop(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LL();
    antlr4::tree::TerminalNode* Simple_name_LL(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Csa_assignContext *> csa_assign();
    Csa_assignContext* csa_assign(size_t i);
    std::vector<Csa_restraintContext *> csa_restraint();
    Csa_restraintContext* csa_restraint(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer_CF();
    antlr4::tree::TerminalNode* Integer_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_CF();
    antlr4::tree::TerminalNode* Real_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_CF();
    antlr4::tree::TerminalNode* Simple_name_CF(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Csa_assign_loopContext* csa_assign_loop();

  class  Pre_assign_loopContext : public antlr4::ParserRuleContext {
  public:
    Pre_assign_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *For();
    antlr4::tree::TerminalNode *Symbol_name_CF();
    antlr4::tree::TerminalNode *In_CF();
    antlr4::tree::TerminalNode *L_paren_CF();
    antlr4::tree::TerminalNode *R_paren_CF();
    std::vector<antlr4::tree::TerminalNode *> Loop();
    antlr4::tree::TerminalNode* Loop(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LL();
    antlr4::tree::TerminalNode* Simple_name_LL(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Pre_assignContext *> pre_assign();
    Pre_assignContext* pre_assign(size_t i);
    std::vector<Pre_restraintContext *> pre_restraint();
    Pre_restraintContext* pre_restraint(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer_CF();
    antlr4::tree::TerminalNode* Integer_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_CF();
    antlr4::tree::TerminalNode* Real_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_CF();
    antlr4::tree::TerminalNode* Simple_name_CF(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pre_assign_loopContext* pre_assign_loop();

  class  Pcs_assign_loopContext : public antlr4::ParserRuleContext {
  public:
    Pcs_assign_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *For();
    antlr4::tree::TerminalNode *Symbol_name_CF();
    antlr4::tree::TerminalNode *In_CF();
    antlr4::tree::TerminalNode *L_paren_CF();
    antlr4::tree::TerminalNode *R_paren_CF();
    std::vector<antlr4::tree::TerminalNode *> Loop();
    antlr4::tree::TerminalNode* Loop(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LL();
    antlr4::tree::TerminalNode* Simple_name_LL(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Pcs_assignContext *> pcs_assign();
    Pcs_assignContext* pcs_assign(size_t i);
    std::vector<Pcs_restraintContext *> pcs_restraint();
    Pcs_restraintContext* pcs_restraint(size_t i);
    std::vector<Carbon_shift_restraintContext *> carbon_shift_restraint();
    Carbon_shift_restraintContext* carbon_shift_restraint(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer_CF();
    antlr4::tree::TerminalNode* Integer_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_CF();
    antlr4::tree::TerminalNode* Real_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_CF();
    antlr4::tree::TerminalNode* Simple_name_CF(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pcs_assign_loopContext* pcs_assign_loop();

  class  Hbond_assign_loopContext : public antlr4::ParserRuleContext {
  public:
    Hbond_assign_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *For();
    antlr4::tree::TerminalNode *Symbol_name_CF();
    antlr4::tree::TerminalNode *In_CF();
    antlr4::tree::TerminalNode *L_paren_CF();
    antlr4::tree::TerminalNode *R_paren_CF();
    std::vector<antlr4::tree::TerminalNode *> Loop();
    antlr4::tree::TerminalNode* Loop(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LL();
    antlr4::tree::TerminalNode* Simple_name_LL(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Hbond_assignContext *> hbond_assign();
    Hbond_assignContext* hbond_assign(size_t i);
    std::vector<Hbond_restraintContext *> hbond_restraint();
    Hbond_restraintContext* hbond_restraint(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer_CF();
    antlr4::tree::TerminalNode* Integer_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_CF();
    antlr4::tree::TerminalNode* Real_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_CF();
    antlr4::tree::TerminalNode* Simple_name_CF(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Hbond_assign_loopContext* hbond_assign_loop();

  class  Hbond_db_assign_loopContext : public antlr4::ParserRuleContext {
  public:
    Hbond_db_assign_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *For();
    antlr4::tree::TerminalNode *Symbol_name_CF();
    antlr4::tree::TerminalNode *In_CF();
    antlr4::tree::TerminalNode *L_paren_CF();
    antlr4::tree::TerminalNode *R_paren_CF();
    std::vector<antlr4::tree::TerminalNode *> Loop();
    antlr4::tree::TerminalNode* Loop(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LL();
    antlr4::tree::TerminalNode* Simple_name_LL(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Hbond_db_assignContext *> hbond_db_assign();
    Hbond_db_assignContext* hbond_db_assign(size_t i);
    std::vector<Hbond_db_restraintContext *> hbond_db_restraint();
    Hbond_db_restraintContext* hbond_db_restraint(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer_CF();
    antlr4::tree::TerminalNode* Integer_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_CF();
    antlr4::tree::TerminalNode* Real_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_CF();
    antlr4::tree::TerminalNode* Simple_name_CF(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Hbond_db_assign_loopContext* hbond_db_assign_loop();

  class  Planar_group_loopContext : public antlr4::ParserRuleContext {
  public:
    Planar_group_loopContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *For();
    antlr4::tree::TerminalNode *Symbol_name_CF();
    antlr4::tree::TerminalNode *In_CF();
    antlr4::tree::TerminalNode *L_paren_CF();
    antlr4::tree::TerminalNode *R_paren_CF();
    std::vector<antlr4::tree::TerminalNode *> Loop();
    antlr4::tree::TerminalNode* Loop(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_LL();
    antlr4::tree::TerminalNode* Simple_name_LL(size_t i);
    antlr4::tree::TerminalNode *End();
    std::vector<Evaluate_statementContext *> evaluate_statement();
    Evaluate_statementContext* evaluate_statement(size_t i);
    std::vector<Planar_groupContext *> planar_group();
    Planar_groupContext* planar_group(size_t i);
    std::vector<Planar_restraintContext *> planar_restraint();
    Planar_restraintContext* planar_restraint(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer_CF();
    antlr4::tree::TerminalNode* Integer_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_CF();
    antlr4::tree::TerminalNode* Real_CF(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Simple_name_CF();
    antlr4::tree::TerminalNode* Simple_name_CF(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Planar_group_loopContext* planar_group_loop();


  bool sempred(antlr4::RuleContext *_localctx, size_t ruleIndex, size_t predicateIndex) override;

  bool factorSempred(FactorContext *_localctx, size_t predicateIndex);

  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

