/*
 AMBER MR (Magnetic Restraint) parser grammar for ANTLR v4.
 Copyright 2022 Masashi Yokochi

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

parser grammar AmberMRParser;

options { tokenVocab=AmberMRLexer; }

amber_mr:
	(
	comment |
	nmr_restraint |
	noesy_volume_restraint |
	chemical_shift_restraint |
	pcs_restraint |
	dipolar_coupling_restraint |
	csa_restraint |
	unambig_atom_name_mapping |
	ambig_atom_name_mapping
	)*
	EOF;

comment:
	COMMENT Any_name* (RETURN_CM | EOF);

nmr_restraint:
	RST restraint_statement END?;

noesy_volume_restraint:
	NOEEXP noeexp_statement END?;

chemical_shift_restraint:
	SHF shf_statement END?;

pcs_restraint:
	PCSHF pcshf_statement END?;

dipolar_coupling_restraint:
	ALIGN align_statement END?;

csa_restraint:
	CSA csa_statement END?;

/* Amber: NMR restraints - 29.1 Distance, angle and torsional restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
restraint_statement:
	restraint_factor*;

restraint_factor:
	(IAT | IGR1 | IGR2 | IGR3 | IGR4 | IGR5 | IGR6 | IGR7 | IGR8) Equ_op_IA (Integers | MultiplicativeInt) (Comma_IA | End_IA) |
	(RSTWT | RJCOEF) Equ_op_RA (Reals | MultiplicativeReal) (Comma_RA | End_RA) |
	RESTRAINT Equ_op L_quot
		(distance_rst_func_call |
		angle_rst_func_call |
		torsion_rst_func_call |
		plane_point_angle_rst_func_call |
		plane_plane_angle_rst_func_call |
		coordinate2_rst_func_call |
		coordinate3_rst_func_call |
		coordinate4_rst_func_call)
	R_quot Comma? |
	(ATNAM_Lp | GRNAM1_Lp | GRNAM2_Lp | GRNAM3_Lp | GRNAM4_Lp | GRNAM5_Lp | GRNAM6_Lp | GRNAM7_Lp | GRNAM8_Lp) Decimal_AP R_paren_AP Equ_op_AP Qstring_AP Comma? |
	(ATNAM | GRNAM1 | GRNAM2 | GRNAM3 | GRNAM4 | GRNAM5 | GRNAM6 | GRNAM7 | GRNAM8) Equ_op_QA Qstrings (Comma_QA | End_QA) |
	(IRESID | IRSTYP | IALTD | IMULT | OUTXYZ | IR6 | IFNTYP) Equ_op_BP BoolInt Comma? |
	(NSTEP1 | NSTEP2 | IFVARI | NINC | IXPK | NXPK | ICONSTR) Equ_op_IP Integer Comma? |
	(R1 | R2 | R3 | R4 | RK2 | RK3 | R1A | R2A | R3A | R4A | RK2A | RK3A | R0 | K0 | R0A | K0A) Equ_op_RP Real Comma? |
	FXYZ Equ_op_BA BoolInts (Comma_BA | End_BA) |
	(IAT | IGR1 | IGR2 | IGR3 | IGR4 | IGR5 | IGR6 | IGR7 | IGR8) L_paren_IA Decimal R_paren_AR Equ_op_IA Integers (Comma_IA | End_IA) |
	RSTWT L_paren_RA Decimal R_paren_AR Equ_op_RA Reals (Comma_RA | End_RA);

/* Amber: NMR restraints - 29.2. NOESY volume restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
noeexp_statement:
	noeexp_factor*;

noeexp_factor:
	NPEAK Equ_op_IA (Integers | MultiplicativeInt) (Comma_IA | End_IA) |
	EMIX Equ_op_RA (Reals | MultiplicativeReal) (Comma_RA | End_RA) |
	(IHP | JHP) L_paren_IP Decimal Comma_AR Decimal R_paren_AR Equ_op_IP Integer Comma? |
	(AEXP | ARANGE | AWT) L_paren_RP Decimal Comma_AR Decimal R_paren_AR Equ_op_RP Real Comma? |
	(INVWT1 | INVWT2 | OMEGA | TAUROT | TAUMET | OSCALE) Equ_op_RP Real Comma? |
	ID2O Equ_op_BP BoolInt Comma? |
	NPEAK L_paren_IA Decimal R_paren_AR Equ_op_IA Integers (Comma_IA | End_IA) |
	EMIX L_paren_RA Decimal R_paren_AR Equ_op_RA Reals (Comma_RA | End_RA) |
	comment;

/* Amber: NMR restraints - 29.3. Chemical shift restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
shf_statement:
	shf_factor*;

shf_factor:
	(NRING | NPROT | NTER | CTER) Equ_op_IP Integer Comma? |
	(NATR | IPROT) L_paren_IP Decimal R_paren_AR Equ_op_IP Integer Comma? |
	IATR L_paren_IP Decimal Comma_AR Decimal R_paren_AR Equ_op_IP Integer Comma? |
	OBS L_paren_RP Decimal R_paren_AR Equ_op_RP Real Comma? |
	(STR | SHRANG | WT) L_paren_RA Decimal R_paren_AR Equ_op_RA (Reals | MultiplicativeReal) (Comma_RA | End_RA) |
	NAMR L_paren_QP Decimal R_paren_AR Equ_op_QP Qstring Comma? |
	SHCUT Equ_op_RP Real Comma? |
	comment;

/* Amber: NMR restraints - 29.4. Psuedocontact shift restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
pcshf_statement:
	pcshf_factor*;

pcshf_factor:
	(NPROT | NME) Equ_op_IP Integer Comma? |
	NMPMC Equ_op_QP Qstring Comma? |
	(IPROT | MLTPRO) L_paren_IP Decimal R_paren_AR Equ_op_IP Integer Comma? |
	(OPTPHI | OPTTET | OPTOMG | OPTA1 | OPTA2 | OBS) L_paren_RP Decimal R_paren_AR Equ_op_RP Real Comma? |
	(WT | TOLPRO) L_paren_RA Decimal R_paren_AR Equ_op_RA (Reals | MultiplicativeReal) (Comma_RA | End_RA) |
	OPTKON Equ_op_RP Real Comma? |
	comment;

/* Amber: NMR restraints - 29.5. Direct dipolar coupling restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
align_statement:
	align_factor*;

align_factor:
	(NDIP | DATASET | NUM_DATASETS) Equ_op_IP Integer Comma? |
	(ID | JD | DATASET) L_paren_IP Decimal R_paren_AR Equ_op_IP Integer Comma? |
	(DOBSL | DOBSU | DOBS) L_paren_RP Decimal R_paren_AR Equ_op_RP Real Comma? |
	(DWT | GIGJ | DIJ | DFAC_AL) L_paren_RA Decimal R_paren_AR Equ_op_RA Reals (Comma_RA | End_RA) |
	(DWT | GIGJ | DIJ | DFAC_AL) Equ_op_RA (Reals | MultiplicativeReal) (Comma_RA | End_RA) |
	(S11 | S12 | S13 | S22 | S23) Equ_op_RA Reals (Comma_RA | End_RA) |
	DCUT Equ_op_RP Real Comma? |
	FJ Equ_op_RP Real Comma? |
	FREEZEMOL Equ_op Logical Comma? |
	comment;

/* Amber: NMR restraints - 29.6. Residual CSA or pseudo-CSA restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
csa_statement:
	csa_factor*;

csa_factor:
	(NCSA | DATASETC) Equ_op_IP Integer Comma? |
	(ICSA | JCSA | KCSA) L_paren_IP Decimal R_paren_AR Equ_op_IP Integer Comma? |
	(COBSL | COBSU | COBS) L_paren_RP Decimal R_paren_AR Equ_op_RP Real Comma? |
	CWT Equ_op_RA (Reals | MultiplicativeReal) (Comma_RA | End_RA) |
	(SIGMA11 | SIGMA12 | SIGMA13 | SIGMA22 | SIGMA23 | FIELD | CCUT) Equ_op_RP Real Comma? |
	comment;

/* Amber 10 (ambmask): NMR restraints - 29.1 Distance, angle and torsional restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
distance_rst_func_call:
	DISTANCE_F L_paren_F restraint_func_expr Comma_F? restraint_func_expr R_paren_F |
	DISTANCE_F L_brace_F restraint_func_expr Comma_F? restraint_func_expr R_brace_F |
	DISTANCE_F L_brakt_F restraint_func_expr Comma_F? restraint_func_expr R_brakt_F;

angle_rst_func_call:
	ANGLE_F L_paren_F restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr R_paren_F |
	ANGLE_F L_brace_F restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr R_brace_F |
	ANGLE_F L_brakt_F restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr R_brakt_F;

plane_point_angle_rst_func_call:
	ANGLE_F L_paren_F restraint_func_expr Comma_F? plane_rst_func_call R_paren_F |
	ANGLE_F L_brace_F restraint_func_expr Comma_F? plane_rst_func_call R_brace_F |
	ANGLE_F L_brakt_F restraint_func_expr Comma_F? plane_rst_func_call R_brakt_F |
	ANGLE_F L_paren_F plane_rst_func_call Comma_F? restraint_func_expr R_paren_F |
	ANGLE_F L_brace_F plane_rst_func_call Comma_F? restraint_func_expr R_brace_F |
	ANGLE_F L_brakt_F plane_rst_func_call Comma_F? restraint_func_expr R_brakt_F;

plane_plane_angle_rst_func_call:
	ANGLE_F L_paren_F plane_rst_func_call Comma_F? plane_rst_func_call R_paren_F |
	ANGLE_F L_brace_F plane_rst_func_call Comma_F? plane_rst_func_call R_brace_F |
	ANGLE_F L_brakt_F plane_rst_func_call Comma_F? plane_rst_func_call R_brakt_F;

torsion_rst_func_call:
	TORSION_F L_paren_F restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr R_paren_F |
	TORSION_F L_brace_F restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr R_brace_F |
	TORSION_F L_brakt_F restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr R_brakt_F;

coordinate2_rst_func_call:
	COORDINATE_F L_paren_F distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F R_paren_F |
	COORDINATE_F L_brace_F distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F R_brace_F |
	COORDINATE_F L_brakt_F distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F R_brakt_F;

coordinate3_rst_func_call:
	COORDINATE_F L_paren_F distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F Comma_F?
				distance_rst_func_call Comma_F? Real_F R_paren_F |
	COORDINATE_F L_brace_F distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F Comma_F?
				distance_rst_func_call Comma_F? Real_F R_brace_F |
	COORDINATE_F L_brakt_F distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F Comma_F?
				distance_rst_func_call Comma_F? Real_F R_brakt_F;

coordinate4_rst_func_call:
	COORDINATE_F L_paren_F distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F Comma_F?
				distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F R_paren_F |
	COORDINATE_F L_brace_F distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F Comma_F?
				distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F R_brace_F |
	COORDINATE_F L_brakt_F distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F Comma_F?
				distance_rst_func_call Comma_F? Real_F Comma_F? distance_rst_func_call Comma_F? Real_F R_brakt_F;

restraint_func_expr:
	Integer_F |
	L_paren_F Integer_F R_paren_F |
	L_brace_F Integer_F R_brace_F |
	L_brakt_F Integer_F R_brakt_F |
	Ambmask_F |
	L_paren_F Ambmask_F R_paren_F |
	L_brace_F Ambmask_F R_brace_F |
	L_brakt_F Ambmask_F R_brakt_F |
	com_rst_func_call;

plane_rst_func_call:
	PLANE_F L_paren_F restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr R_paren_F |
	PLANE_F L_brace_F restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr R_brace_F |
	PLANE_F L_brakt_F restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr Comma_F? restraint_func_expr R_brakt_F;

com_rst_func_call:
	COM_F L_paren_F restraint_func_expr (Comma_F? restraint_func_expr)* R_paren_F |
	COM_F L_brace_F restraint_func_expr (Comma_F? restraint_func_expr)* R_brace_F |
	COM_F L_brakt_F restraint_func_expr (Comma_F? restraint_func_expr)* R_brakt_F;

/* AMBER atom nomenclature mapping generated by makeDIST_RST */
unambig_atom_name_mapping:
	Residue Simple_name
	mapping_list+;

mapping_list:
	Mapping Simple_name_MP Equ_op_MP Simple_name_MP+ RETURN_MP;

ambig_atom_name_mapping:
	Residue Simple_name
	ambig_list+;

ambig_list:
	Ambig (Simple_name_MP | Ambig_code_MP) Equ_op_MP (Simple_name_MP Integer_MP)+ RETURN_MP;

