
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/AmberMRParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  AmberMRParser : public antlr4::Parser {
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
    RuleAmber_mr = 0, RuleComment = 1, RuleNmr_restraint = 2, RuleNoesy_volume_restraint = 3, 
    RuleChemical_shift_restraint = 4, RulePcs_restraint = 5, RuleDipolar_coupling_restraint = 6, 
    RuleCsa_restraint = 7, RuleRestraint_statement = 8, RuleRestraint_factor = 9, 
    RuleNoeexp_statement = 10, RuleNoeexp_factor = 11, RuleShf_statement = 12, 
    RuleShf_factor = 13, RulePcshf_statement = 14, RulePcshf_factor = 15, 
    RuleAlign_statement = 16, RuleAlign_factor = 17, RuleCsa_statement = 18, 
    RuleCsa_factor = 19, RuleDistance_rst_func_call = 20, RuleAngle_rst_func_call = 21, 
    RulePlane_point_angle_rst_func_call = 22, RulePlane_plane_angle_rst_func_call = 23, 
    RuleTorsion_rst_func_call = 24, RuleCoordinate2_rst_func_call = 25, 
    RuleCoordinate3_rst_func_call = 26, RuleCoordinate4_rst_func_call = 27, 
    RuleRestraint_func_expr = 28, RulePlane_rst_func_call = 29, RuleCom_rst_func_call = 30, 
    RuleUnambig_atom_name_mapping = 31, RuleMapping_list = 32, RuleAmbig_atom_name_mapping = 33, 
    RuleAmbig_list = 34
  };

  explicit AmberMRParser(antlr4::TokenStream *input);

  AmberMRParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~AmberMRParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Amber_mrContext;
  class CommentContext;
  class Nmr_restraintContext;
  class Noesy_volume_restraintContext;
  class Chemical_shift_restraintContext;
  class Pcs_restraintContext;
  class Dipolar_coupling_restraintContext;
  class Csa_restraintContext;
  class Restraint_statementContext;
  class Restraint_factorContext;
  class Noeexp_statementContext;
  class Noeexp_factorContext;
  class Shf_statementContext;
  class Shf_factorContext;
  class Pcshf_statementContext;
  class Pcshf_factorContext;
  class Align_statementContext;
  class Align_factorContext;
  class Csa_statementContext;
  class Csa_factorContext;
  class Distance_rst_func_callContext;
  class Angle_rst_func_callContext;
  class Plane_point_angle_rst_func_callContext;
  class Plane_plane_angle_rst_func_callContext;
  class Torsion_rst_func_callContext;
  class Coordinate2_rst_func_callContext;
  class Coordinate3_rst_func_callContext;
  class Coordinate4_rst_func_callContext;
  class Restraint_func_exprContext;
  class Plane_rst_func_callContext;
  class Com_rst_func_callContext;
  class Unambig_atom_name_mappingContext;
  class Mapping_listContext;
  class Ambig_atom_name_mappingContext;
  class Ambig_listContext; 

  class  Amber_mrContext : public antlr4::ParserRuleContext {
  public:
    Amber_mrContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<Nmr_restraintContext *> nmr_restraint();
    Nmr_restraintContext* nmr_restraint(size_t i);
    std::vector<Noesy_volume_restraintContext *> noesy_volume_restraint();
    Noesy_volume_restraintContext* noesy_volume_restraint(size_t i);
    std::vector<Chemical_shift_restraintContext *> chemical_shift_restraint();
    Chemical_shift_restraintContext* chemical_shift_restraint(size_t i);
    std::vector<Pcs_restraintContext *> pcs_restraint();
    Pcs_restraintContext* pcs_restraint(size_t i);
    std::vector<Dipolar_coupling_restraintContext *> dipolar_coupling_restraint();
    Dipolar_coupling_restraintContext* dipolar_coupling_restraint(size_t i);
    std::vector<Csa_restraintContext *> csa_restraint();
    Csa_restraintContext* csa_restraint(size_t i);
    std::vector<Unambig_atom_name_mappingContext *> unambig_atom_name_mapping();
    Unambig_atom_name_mappingContext* unambig_atom_name_mapping(size_t i);
    std::vector<Ambig_atom_name_mappingContext *> ambig_atom_name_mapping();
    Ambig_atom_name_mappingContext* ambig_atom_name_mapping(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Amber_mrContext* amber_mr();

  class  CommentContext : public antlr4::ParserRuleContext {
  public:
    CommentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *COMMENT();
    antlr4::tree::TerminalNode *RETURN_CM();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Any_name();
    antlr4::tree::TerminalNode* Any_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  CommentContext* comment();

  class  Nmr_restraintContext : public antlr4::ParserRuleContext {
  public:
    Nmr_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RST();
    Restraint_statementContext *restraint_statement();
    antlr4::tree::TerminalNode *END();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Nmr_restraintContext* nmr_restraint();

  class  Noesy_volume_restraintContext : public antlr4::ParserRuleContext {
  public:
    Noesy_volume_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *NOEEXP();
    Noeexp_statementContext *noeexp_statement();
    antlr4::tree::TerminalNode *END();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Noesy_volume_restraintContext* noesy_volume_restraint();

  class  Chemical_shift_restraintContext : public antlr4::ParserRuleContext {
  public:
    Chemical_shift_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *SHF();
    Shf_statementContext *shf_statement();
    antlr4::tree::TerminalNode *END();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Chemical_shift_restraintContext* chemical_shift_restraint();

  class  Pcs_restraintContext : public antlr4::ParserRuleContext {
  public:
    Pcs_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *PCSHF();
    Pcshf_statementContext *pcshf_statement();
    antlr4::tree::TerminalNode *END();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pcs_restraintContext* pcs_restraint();

  class  Dipolar_coupling_restraintContext : public antlr4::ParserRuleContext {
  public:
    Dipolar_coupling_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *ALIGN();
    Align_statementContext *align_statement();
    antlr4::tree::TerminalNode *END();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Dipolar_coupling_restraintContext* dipolar_coupling_restraint();

  class  Csa_restraintContext : public antlr4::ParserRuleContext {
  public:
    Csa_restraintContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *CSA();
    Csa_statementContext *csa_statement();
    antlr4::tree::TerminalNode *END();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Csa_restraintContext* csa_restraint();

  class  Restraint_statementContext : public antlr4::ParserRuleContext {
  public:
    Restraint_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Restraint_factorContext *> restraint_factor();
    Restraint_factorContext* restraint_factor(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Restraint_statementContext* restraint_statement();

  class  Restraint_factorContext : public antlr4::ParserRuleContext {
  public:
    Restraint_factorContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Equ_op_IA();
    antlr4::tree::TerminalNode *IAT();
    antlr4::tree::TerminalNode *IGR1();
    antlr4::tree::TerminalNode *IGR2();
    antlr4::tree::TerminalNode *IGR3();
    antlr4::tree::TerminalNode *IGR4();
    antlr4::tree::TerminalNode *IGR5();
    antlr4::tree::TerminalNode *IGR6();
    antlr4::tree::TerminalNode *IGR7();
    antlr4::tree::TerminalNode *IGR8();
    antlr4::tree::TerminalNode *Integers();
    antlr4::tree::TerminalNode *MultiplicativeInt();
    antlr4::tree::TerminalNode *Comma_IA();
    antlr4::tree::TerminalNode *End_IA();
    antlr4::tree::TerminalNode *Equ_op_RA();
    antlr4::tree::TerminalNode *RSTWT();
    antlr4::tree::TerminalNode *RJCOEF();
    antlr4::tree::TerminalNode *Reals();
    antlr4::tree::TerminalNode *MultiplicativeReal();
    antlr4::tree::TerminalNode *Comma_RA();
    antlr4::tree::TerminalNode *End_RA();
    antlr4::tree::TerminalNode *RESTRAINT();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *L_quot();
    antlr4::tree::TerminalNode *R_quot();
    Distance_rst_func_callContext *distance_rst_func_call();
    Angle_rst_func_callContext *angle_rst_func_call();
    Torsion_rst_func_callContext *torsion_rst_func_call();
    Plane_point_angle_rst_func_callContext *plane_point_angle_rst_func_call();
    Plane_plane_angle_rst_func_callContext *plane_plane_angle_rst_func_call();
    Coordinate2_rst_func_callContext *coordinate2_rst_func_call();
    Coordinate3_rst_func_callContext *coordinate3_rst_func_call();
    Coordinate4_rst_func_callContext *coordinate4_rst_func_call();
    antlr4::tree::TerminalNode *Comma();
    antlr4::tree::TerminalNode *Decimal_AP();
    antlr4::tree::TerminalNode *R_paren_AP();
    antlr4::tree::TerminalNode *Equ_op_AP();
    antlr4::tree::TerminalNode *Qstring_AP();
    antlr4::tree::TerminalNode *ATNAM_Lp();
    antlr4::tree::TerminalNode *GRNAM1_Lp();
    antlr4::tree::TerminalNode *GRNAM2_Lp();
    antlr4::tree::TerminalNode *GRNAM3_Lp();
    antlr4::tree::TerminalNode *GRNAM4_Lp();
    antlr4::tree::TerminalNode *GRNAM5_Lp();
    antlr4::tree::TerminalNode *GRNAM6_Lp();
    antlr4::tree::TerminalNode *GRNAM7_Lp();
    antlr4::tree::TerminalNode *GRNAM8_Lp();
    antlr4::tree::TerminalNode *Equ_op_QA();
    antlr4::tree::TerminalNode *Qstrings();
    antlr4::tree::TerminalNode *ATNAM();
    antlr4::tree::TerminalNode *GRNAM1();
    antlr4::tree::TerminalNode *GRNAM2();
    antlr4::tree::TerminalNode *GRNAM3();
    antlr4::tree::TerminalNode *GRNAM4();
    antlr4::tree::TerminalNode *GRNAM5();
    antlr4::tree::TerminalNode *GRNAM6();
    antlr4::tree::TerminalNode *GRNAM7();
    antlr4::tree::TerminalNode *GRNAM8();
    antlr4::tree::TerminalNode *Comma_QA();
    antlr4::tree::TerminalNode *End_QA();
    antlr4::tree::TerminalNode *Equ_op_BP();
    antlr4::tree::TerminalNode *BoolInt();
    antlr4::tree::TerminalNode *IRESID();
    antlr4::tree::TerminalNode *IRSTYP();
    antlr4::tree::TerminalNode *IALTD();
    antlr4::tree::TerminalNode *IMULT();
    antlr4::tree::TerminalNode *OUTXYZ();
    antlr4::tree::TerminalNode *IR6();
    antlr4::tree::TerminalNode *IFNTYP();
    antlr4::tree::TerminalNode *Equ_op_IP();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *NSTEP1();
    antlr4::tree::TerminalNode *NSTEP2();
    antlr4::tree::TerminalNode *IFVARI();
    antlr4::tree::TerminalNode *NINC();
    antlr4::tree::TerminalNode *IXPK();
    antlr4::tree::TerminalNode *NXPK();
    antlr4::tree::TerminalNode *ICONSTR();
    antlr4::tree::TerminalNode *Equ_op_RP();
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *R1();
    antlr4::tree::TerminalNode *R2();
    antlr4::tree::TerminalNode *R3();
    antlr4::tree::TerminalNode *R4();
    antlr4::tree::TerminalNode *RK2();
    antlr4::tree::TerminalNode *RK3();
    antlr4::tree::TerminalNode *R1A();
    antlr4::tree::TerminalNode *R2A();
    antlr4::tree::TerminalNode *R3A();
    antlr4::tree::TerminalNode *R4A();
    antlr4::tree::TerminalNode *RK2A();
    antlr4::tree::TerminalNode *RK3A();
    antlr4::tree::TerminalNode *R0();
    antlr4::tree::TerminalNode *K0();
    antlr4::tree::TerminalNode *R0A();
    antlr4::tree::TerminalNode *K0A();
    antlr4::tree::TerminalNode *FXYZ();
    antlr4::tree::TerminalNode *Equ_op_BA();
    antlr4::tree::TerminalNode *BoolInts();
    antlr4::tree::TerminalNode *Comma_BA();
    antlr4::tree::TerminalNode *End_BA();
    antlr4::tree::TerminalNode *L_paren_IA();
    antlr4::tree::TerminalNode *Decimal();
    antlr4::tree::TerminalNode *R_paren_AR();
    antlr4::tree::TerminalNode *L_paren_RA();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Restraint_factorContext* restraint_factor();

  class  Noeexp_statementContext : public antlr4::ParserRuleContext {
  public:
    Noeexp_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Noeexp_factorContext *> noeexp_factor();
    Noeexp_factorContext* noeexp_factor(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Noeexp_statementContext* noeexp_statement();

  class  Noeexp_factorContext : public antlr4::ParserRuleContext {
  public:
    Noeexp_factorContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *NPEAK();
    antlr4::tree::TerminalNode *Equ_op_IA();
    antlr4::tree::TerminalNode *Integers();
    antlr4::tree::TerminalNode *MultiplicativeInt();
    antlr4::tree::TerminalNode *Comma_IA();
    antlr4::tree::TerminalNode *End_IA();
    antlr4::tree::TerminalNode *EMIX();
    antlr4::tree::TerminalNode *Equ_op_RA();
    antlr4::tree::TerminalNode *Reals();
    antlr4::tree::TerminalNode *MultiplicativeReal();
    antlr4::tree::TerminalNode *Comma_RA();
    antlr4::tree::TerminalNode *End_RA();
    antlr4::tree::TerminalNode *L_paren_IP();
    std::vector<antlr4::tree::TerminalNode *> Decimal();
    antlr4::tree::TerminalNode* Decimal(size_t i);
    antlr4::tree::TerminalNode *Comma_AR();
    antlr4::tree::TerminalNode *R_paren_AR();
    antlr4::tree::TerminalNode *Equ_op_IP();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *IHP();
    antlr4::tree::TerminalNode *JHP();
    antlr4::tree::TerminalNode *Comma();
    antlr4::tree::TerminalNode *L_paren_RP();
    antlr4::tree::TerminalNode *Equ_op_RP();
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *AEXP();
    antlr4::tree::TerminalNode *ARANGE();
    antlr4::tree::TerminalNode *AWT();
    antlr4::tree::TerminalNode *INVWT1();
    antlr4::tree::TerminalNode *INVWT2();
    antlr4::tree::TerminalNode *OMEGA();
    antlr4::tree::TerminalNode *TAUROT();
    antlr4::tree::TerminalNode *TAUMET();
    antlr4::tree::TerminalNode *OSCALE();
    antlr4::tree::TerminalNode *ID2O();
    antlr4::tree::TerminalNode *Equ_op_BP();
    antlr4::tree::TerminalNode *BoolInt();
    antlr4::tree::TerminalNode *L_paren_IA();
    antlr4::tree::TerminalNode *L_paren_RA();
    CommentContext *comment();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Noeexp_factorContext* noeexp_factor();

  class  Shf_statementContext : public antlr4::ParserRuleContext {
  public:
    Shf_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Shf_factorContext *> shf_factor();
    Shf_factorContext* shf_factor(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Shf_statementContext* shf_statement();

  class  Shf_factorContext : public antlr4::ParserRuleContext {
  public:
    Shf_factorContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Equ_op_IP();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *NRING();
    antlr4::tree::TerminalNode *NPROT();
    antlr4::tree::TerminalNode *NTER();
    antlr4::tree::TerminalNode *CTER();
    antlr4::tree::TerminalNode *Comma();
    antlr4::tree::TerminalNode *L_paren_IP();
    std::vector<antlr4::tree::TerminalNode *> Decimal();
    antlr4::tree::TerminalNode* Decimal(size_t i);
    antlr4::tree::TerminalNode *R_paren_AR();
    antlr4::tree::TerminalNode *NATR();
    antlr4::tree::TerminalNode *IPROT();
    antlr4::tree::TerminalNode *IATR();
    antlr4::tree::TerminalNode *Comma_AR();
    antlr4::tree::TerminalNode *OBS();
    antlr4::tree::TerminalNode *L_paren_RP();
    antlr4::tree::TerminalNode *Equ_op_RP();
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *L_paren_RA();
    antlr4::tree::TerminalNode *Equ_op_RA();
    antlr4::tree::TerminalNode *STR();
    antlr4::tree::TerminalNode *SHRANG();
    antlr4::tree::TerminalNode *WT();
    antlr4::tree::TerminalNode *Reals();
    antlr4::tree::TerminalNode *MultiplicativeReal();
    antlr4::tree::TerminalNode *Comma_RA();
    antlr4::tree::TerminalNode *End_RA();
    antlr4::tree::TerminalNode *NAMR();
    antlr4::tree::TerminalNode *L_paren_QP();
    antlr4::tree::TerminalNode *Equ_op_QP();
    antlr4::tree::TerminalNode *Qstring();
    antlr4::tree::TerminalNode *SHCUT();
    CommentContext *comment();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Shf_factorContext* shf_factor();

  class  Pcshf_statementContext : public antlr4::ParserRuleContext {
  public:
    Pcshf_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Pcshf_factorContext *> pcshf_factor();
    Pcshf_factorContext* pcshf_factor(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pcshf_statementContext* pcshf_statement();

  class  Pcshf_factorContext : public antlr4::ParserRuleContext {
  public:
    Pcshf_factorContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Equ_op_IP();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *NPROT();
    antlr4::tree::TerminalNode *NME();
    antlr4::tree::TerminalNode *Comma();
    antlr4::tree::TerminalNode *NMPMC();
    antlr4::tree::TerminalNode *Equ_op_QP();
    antlr4::tree::TerminalNode *Qstring();
    antlr4::tree::TerminalNode *L_paren_IP();
    antlr4::tree::TerminalNode *Decimal();
    antlr4::tree::TerminalNode *R_paren_AR();
    antlr4::tree::TerminalNode *IPROT();
    antlr4::tree::TerminalNode *MLTPRO();
    antlr4::tree::TerminalNode *L_paren_RP();
    antlr4::tree::TerminalNode *Equ_op_RP();
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *OPTPHI();
    antlr4::tree::TerminalNode *OPTTET();
    antlr4::tree::TerminalNode *OPTOMG();
    antlr4::tree::TerminalNode *OPTA1();
    antlr4::tree::TerminalNode *OPTA2();
    antlr4::tree::TerminalNode *OBS();
    antlr4::tree::TerminalNode *L_paren_RA();
    antlr4::tree::TerminalNode *Equ_op_RA();
    antlr4::tree::TerminalNode *WT();
    antlr4::tree::TerminalNode *TOLPRO();
    antlr4::tree::TerminalNode *Reals();
    antlr4::tree::TerminalNode *MultiplicativeReal();
    antlr4::tree::TerminalNode *Comma_RA();
    antlr4::tree::TerminalNode *End_RA();
    antlr4::tree::TerminalNode *OPTKON();
    CommentContext *comment();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Pcshf_factorContext* pcshf_factor();

  class  Align_statementContext : public antlr4::ParserRuleContext {
  public:
    Align_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Align_factorContext *> align_factor();
    Align_factorContext* align_factor(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Align_statementContext* align_statement();

  class  Align_factorContext : public antlr4::ParserRuleContext {
  public:
    Align_factorContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Equ_op_IP();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *NDIP();
    antlr4::tree::TerminalNode *DATASET();
    antlr4::tree::TerminalNode *NUM_DATASETS();
    antlr4::tree::TerminalNode *Comma();
    antlr4::tree::TerminalNode *L_paren_IP();
    antlr4::tree::TerminalNode *Decimal();
    antlr4::tree::TerminalNode *R_paren_AR();
    antlr4::tree::TerminalNode *ID();
    antlr4::tree::TerminalNode *JD();
    antlr4::tree::TerminalNode *L_paren_RP();
    antlr4::tree::TerminalNode *Equ_op_RP();
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *DOBSL();
    antlr4::tree::TerminalNode *DOBSU();
    antlr4::tree::TerminalNode *DOBS();
    antlr4::tree::TerminalNode *L_paren_RA();
    antlr4::tree::TerminalNode *Equ_op_RA();
    antlr4::tree::TerminalNode *Reals();
    antlr4::tree::TerminalNode *DWT();
    antlr4::tree::TerminalNode *GIGJ();
    antlr4::tree::TerminalNode *DIJ();
    antlr4::tree::TerminalNode *DFAC_AL();
    antlr4::tree::TerminalNode *Comma_RA();
    antlr4::tree::TerminalNode *End_RA();
    antlr4::tree::TerminalNode *MultiplicativeReal();
    antlr4::tree::TerminalNode *S11();
    antlr4::tree::TerminalNode *S12();
    antlr4::tree::TerminalNode *S13();
    antlr4::tree::TerminalNode *S22();
    antlr4::tree::TerminalNode *S23();
    antlr4::tree::TerminalNode *DCUT();
    antlr4::tree::TerminalNode *FJ();
    antlr4::tree::TerminalNode *FREEZEMOL();
    antlr4::tree::TerminalNode *Equ_op();
    antlr4::tree::TerminalNode *Logical();
    CommentContext *comment();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Align_factorContext* align_factor();

  class  Csa_statementContext : public antlr4::ParserRuleContext {
  public:
    Csa_statementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Csa_factorContext *> csa_factor();
    Csa_factorContext* csa_factor(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Csa_statementContext* csa_statement();

  class  Csa_factorContext : public antlr4::ParserRuleContext {
  public:
    Csa_factorContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Equ_op_IP();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *NCSA();
    antlr4::tree::TerminalNode *DATASETC();
    antlr4::tree::TerminalNode *Comma();
    antlr4::tree::TerminalNode *L_paren_IP();
    antlr4::tree::TerminalNode *Decimal();
    antlr4::tree::TerminalNode *R_paren_AR();
    antlr4::tree::TerminalNode *ICSA();
    antlr4::tree::TerminalNode *JCSA();
    antlr4::tree::TerminalNode *KCSA();
    antlr4::tree::TerminalNode *L_paren_RP();
    antlr4::tree::TerminalNode *Equ_op_RP();
    antlr4::tree::TerminalNode *Real();
    antlr4::tree::TerminalNode *COBSL();
    antlr4::tree::TerminalNode *COBSU();
    antlr4::tree::TerminalNode *COBS();
    antlr4::tree::TerminalNode *CWT();
    antlr4::tree::TerminalNode *Equ_op_RA();
    antlr4::tree::TerminalNode *Reals();
    antlr4::tree::TerminalNode *MultiplicativeReal();
    antlr4::tree::TerminalNode *Comma_RA();
    antlr4::tree::TerminalNode *End_RA();
    antlr4::tree::TerminalNode *SIGMA11();
    antlr4::tree::TerminalNode *SIGMA12();
    antlr4::tree::TerminalNode *SIGMA13();
    antlr4::tree::TerminalNode *SIGMA22();
    antlr4::tree::TerminalNode *SIGMA23();
    antlr4::tree::TerminalNode *FIELD();
    antlr4::tree::TerminalNode *CCUT();
    CommentContext *comment();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Csa_factorContext* csa_factor();

  class  Distance_rst_func_callContext : public antlr4::ParserRuleContext {
  public:
    Distance_rst_func_callContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *DISTANCE_F();
    antlr4::tree::TerminalNode *L_paren_F();
    std::vector<Restraint_func_exprContext *> restraint_func_expr();
    Restraint_func_exprContext* restraint_func_expr(size_t i);
    antlr4::tree::TerminalNode *R_paren_F();
    antlr4::tree::TerminalNode *Comma_F();
    antlr4::tree::TerminalNode *L_brace_F();
    antlr4::tree::TerminalNode *R_brace_F();
    antlr4::tree::TerminalNode *L_brakt_F();
    antlr4::tree::TerminalNode *R_brakt_F();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Distance_rst_func_callContext* distance_rst_func_call();

  class  Angle_rst_func_callContext : public antlr4::ParserRuleContext {
  public:
    Angle_rst_func_callContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *ANGLE_F();
    antlr4::tree::TerminalNode *L_paren_F();
    std::vector<Restraint_func_exprContext *> restraint_func_expr();
    Restraint_func_exprContext* restraint_func_expr(size_t i);
    antlr4::tree::TerminalNode *R_paren_F();
    std::vector<antlr4::tree::TerminalNode *> Comma_F();
    antlr4::tree::TerminalNode* Comma_F(size_t i);
    antlr4::tree::TerminalNode *L_brace_F();
    antlr4::tree::TerminalNode *R_brace_F();
    antlr4::tree::TerminalNode *L_brakt_F();
    antlr4::tree::TerminalNode *R_brakt_F();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Angle_rst_func_callContext* angle_rst_func_call();

  class  Plane_point_angle_rst_func_callContext : public antlr4::ParserRuleContext {
  public:
    Plane_point_angle_rst_func_callContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *ANGLE_F();
    antlr4::tree::TerminalNode *L_paren_F();
    Restraint_func_exprContext *restraint_func_expr();
    Plane_rst_func_callContext *plane_rst_func_call();
    antlr4::tree::TerminalNode *R_paren_F();
    antlr4::tree::TerminalNode *Comma_F();
    antlr4::tree::TerminalNode *L_brace_F();
    antlr4::tree::TerminalNode *R_brace_F();
    antlr4::tree::TerminalNode *L_brakt_F();
    antlr4::tree::TerminalNode *R_brakt_F();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Plane_point_angle_rst_func_callContext* plane_point_angle_rst_func_call();

  class  Plane_plane_angle_rst_func_callContext : public antlr4::ParserRuleContext {
  public:
    Plane_plane_angle_rst_func_callContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *ANGLE_F();
    antlr4::tree::TerminalNode *L_paren_F();
    std::vector<Plane_rst_func_callContext *> plane_rst_func_call();
    Plane_rst_func_callContext* plane_rst_func_call(size_t i);
    antlr4::tree::TerminalNode *R_paren_F();
    antlr4::tree::TerminalNode *Comma_F();
    antlr4::tree::TerminalNode *L_brace_F();
    antlr4::tree::TerminalNode *R_brace_F();
    antlr4::tree::TerminalNode *L_brakt_F();
    antlr4::tree::TerminalNode *R_brakt_F();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Plane_plane_angle_rst_func_callContext* plane_plane_angle_rst_func_call();

  class  Torsion_rst_func_callContext : public antlr4::ParserRuleContext {
  public:
    Torsion_rst_func_callContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *TORSION_F();
    antlr4::tree::TerminalNode *L_paren_F();
    std::vector<Restraint_func_exprContext *> restraint_func_expr();
    Restraint_func_exprContext* restraint_func_expr(size_t i);
    antlr4::tree::TerminalNode *R_paren_F();
    std::vector<antlr4::tree::TerminalNode *> Comma_F();
    antlr4::tree::TerminalNode* Comma_F(size_t i);
    antlr4::tree::TerminalNode *L_brace_F();
    antlr4::tree::TerminalNode *R_brace_F();
    antlr4::tree::TerminalNode *L_brakt_F();
    antlr4::tree::TerminalNode *R_brakt_F();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Torsion_rst_func_callContext* torsion_rst_func_call();

  class  Coordinate2_rst_func_callContext : public antlr4::ParserRuleContext {
  public:
    Coordinate2_rst_func_callContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *COORDINATE_F();
    antlr4::tree::TerminalNode *L_paren_F();
    std::vector<Distance_rst_func_callContext *> distance_rst_func_call();
    Distance_rst_func_callContext* distance_rst_func_call(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_F();
    antlr4::tree::TerminalNode* Real_F(size_t i);
    antlr4::tree::TerminalNode *R_paren_F();
    std::vector<antlr4::tree::TerminalNode *> Comma_F();
    antlr4::tree::TerminalNode* Comma_F(size_t i);
    antlr4::tree::TerminalNode *L_brace_F();
    antlr4::tree::TerminalNode *R_brace_F();
    antlr4::tree::TerminalNode *L_brakt_F();
    antlr4::tree::TerminalNode *R_brakt_F();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coordinate2_rst_func_callContext* coordinate2_rst_func_call();

  class  Coordinate3_rst_func_callContext : public antlr4::ParserRuleContext {
  public:
    Coordinate3_rst_func_callContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *COORDINATE_F();
    antlr4::tree::TerminalNode *L_paren_F();
    std::vector<Distance_rst_func_callContext *> distance_rst_func_call();
    Distance_rst_func_callContext* distance_rst_func_call(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_F();
    antlr4::tree::TerminalNode* Real_F(size_t i);
    antlr4::tree::TerminalNode *R_paren_F();
    std::vector<antlr4::tree::TerminalNode *> Comma_F();
    antlr4::tree::TerminalNode* Comma_F(size_t i);
    antlr4::tree::TerminalNode *L_brace_F();
    antlr4::tree::TerminalNode *R_brace_F();
    antlr4::tree::TerminalNode *L_brakt_F();
    antlr4::tree::TerminalNode *R_brakt_F();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coordinate3_rst_func_callContext* coordinate3_rst_func_call();

  class  Coordinate4_rst_func_callContext : public antlr4::ParserRuleContext {
  public:
    Coordinate4_rst_func_callContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *COORDINATE_F();
    antlr4::tree::TerminalNode *L_paren_F();
    std::vector<Distance_rst_func_callContext *> distance_rst_func_call();
    Distance_rst_func_callContext* distance_rst_func_call(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Real_F();
    antlr4::tree::TerminalNode* Real_F(size_t i);
    antlr4::tree::TerminalNode *R_paren_F();
    std::vector<antlr4::tree::TerminalNode *> Comma_F();
    antlr4::tree::TerminalNode* Comma_F(size_t i);
    antlr4::tree::TerminalNode *L_brace_F();
    antlr4::tree::TerminalNode *R_brace_F();
    antlr4::tree::TerminalNode *L_brakt_F();
    antlr4::tree::TerminalNode *R_brakt_F();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Coordinate4_rst_func_callContext* coordinate4_rst_func_call();

  class  Restraint_func_exprContext : public antlr4::ParserRuleContext {
  public:
    Restraint_func_exprContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer_F();
    antlr4::tree::TerminalNode *L_paren_F();
    antlr4::tree::TerminalNode *R_paren_F();
    antlr4::tree::TerminalNode *L_brace_F();
    antlr4::tree::TerminalNode *R_brace_F();
    antlr4::tree::TerminalNode *L_brakt_F();
    antlr4::tree::TerminalNode *R_brakt_F();
    antlr4::tree::TerminalNode *Ambmask_F();
    Com_rst_func_callContext *com_rst_func_call();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Restraint_func_exprContext* restraint_func_expr();

  class  Plane_rst_func_callContext : public antlr4::ParserRuleContext {
  public:
    Plane_rst_func_callContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *PLANE_F();
    antlr4::tree::TerminalNode *L_paren_F();
    std::vector<Restraint_func_exprContext *> restraint_func_expr();
    Restraint_func_exprContext* restraint_func_expr(size_t i);
    antlr4::tree::TerminalNode *R_paren_F();
    std::vector<antlr4::tree::TerminalNode *> Comma_F();
    antlr4::tree::TerminalNode* Comma_F(size_t i);
    antlr4::tree::TerminalNode *L_brace_F();
    antlr4::tree::TerminalNode *R_brace_F();
    antlr4::tree::TerminalNode *L_brakt_F();
    antlr4::tree::TerminalNode *R_brakt_F();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Plane_rst_func_callContext* plane_rst_func_call();

  class  Com_rst_func_callContext : public antlr4::ParserRuleContext {
  public:
    Com_rst_func_callContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *COM_F();
    antlr4::tree::TerminalNode *L_paren_F();
    std::vector<Restraint_func_exprContext *> restraint_func_expr();
    Restraint_func_exprContext* restraint_func_expr(size_t i);
    antlr4::tree::TerminalNode *R_paren_F();
    std::vector<antlr4::tree::TerminalNode *> Comma_F();
    antlr4::tree::TerminalNode* Comma_F(size_t i);
    antlr4::tree::TerminalNode *L_brace_F();
    antlr4::tree::TerminalNode *R_brace_F();
    antlr4::tree::TerminalNode *L_brakt_F();
    antlr4::tree::TerminalNode *R_brakt_F();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Com_rst_func_callContext* com_rst_func_call();

  class  Unambig_atom_name_mappingContext : public antlr4::ParserRuleContext {
  public:
    Unambig_atom_name_mappingContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Residue();
    antlr4::tree::TerminalNode *Simple_name();
    std::vector<Mapping_listContext *> mapping_list();
    Mapping_listContext* mapping_list(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Unambig_atom_name_mappingContext* unambig_atom_name_mapping();

  class  Mapping_listContext : public antlr4::ParserRuleContext {
  public:
    Mapping_listContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Mapping();
    std::vector<antlr4::tree::TerminalNode *> Simple_name_MP();
    antlr4::tree::TerminalNode* Simple_name_MP(size_t i);
    antlr4::tree::TerminalNode *Equ_op_MP();
    antlr4::tree::TerminalNode *RETURN_MP();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Mapping_listContext* mapping_list();

  class  Ambig_atom_name_mappingContext : public antlr4::ParserRuleContext {
  public:
    Ambig_atom_name_mappingContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Residue();
    antlr4::tree::TerminalNode *Simple_name();
    std::vector<Ambig_listContext *> ambig_list();
    Ambig_listContext* ambig_list(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ambig_atom_name_mappingContext* ambig_atom_name_mapping();

  class  Ambig_listContext : public antlr4::ParserRuleContext {
  public:
    Ambig_listContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Ambig();
    antlr4::tree::TerminalNode *Equ_op_MP();
    antlr4::tree::TerminalNode *RETURN_MP();
    std::vector<antlr4::tree::TerminalNode *> Simple_name_MP();
    antlr4::tree::TerminalNode* Simple_name_MP(size_t i);
    antlr4::tree::TerminalNode *Ambig_code_MP();
    std::vector<antlr4::tree::TerminalNode *> Integer_MP();
    antlr4::tree::TerminalNode* Integer_MP(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ambig_listContext* ambig_list();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

