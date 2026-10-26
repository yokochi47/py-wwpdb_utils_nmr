/*
 CNS MR (Magnetic Restraint) parser grammar for ANTLR v4.
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

parser grammar CnsMRParser;

options { tokenVocab=CnsMRLexer; }

cns_mr:
	(
	distance_restraint |
	dihedral_angle_restraint |
	plane_restraint |
	harmonic_restraint |
	rdc_restraint |
	coupling_restraint |
	carbon_shift_restraint |
	proton_shift_restraint |
	conformation_db_restraint |
	diffusion_anisotropy_restraint |
	one_bond_coupling_restraint |
	angle_db_restraint |
	ncs_restraint |
	classification |
	flag_statement |
	vector_statement |
	evaluate_statement |
	patch_statement |
	parameter_setting |
	noe_assign_loop |		// allowing bare assign clauses for Distance restraints
	dihedral_assign_loop |		// allowing bare assign clauses for Dihedral angle restraints
	sani_assign_loop |		// allowing bare assign clauses for RDC restraints
	coup_assign_loop |		// allowing bare assign clauses for Scaler J-coupling restraints
	carbon_shift_assign_loop |	// allowing bare assign clauses for Carbon chemical shift restraints
	noe_assign |			// allowing bare assign clauses for Distance restraints
	dihedral_assign |		// allowing bare assign clauses for Dihedral angle restraints
	sani_assign |			// allowing bare assign clauses for RDC restraints
	plane_statement |		// allowing bare group clauses for Plane restraints
	harmonic_assign |		// allowing individual assign clauses for Harmonic coordinate restraints
	coup_assign |			// allowing bare assign clauses for Scaler J-coupling restraints
	carbon_shift_assign |		// allowing bare assign clauses for Carbon chemical shift restraints
	observed |			// allowing bare observed clauses for Proton chemical shift restraints
	parameter_statement		// allowing bare parameter statement
	)*
	EOF;

distance_restraint:
	Noe noe_statement* End;

dihedral_angle_restraint:
	Restraints? Dihedral dihedral_statement* End;

plane_restraint:
	Restraints? Plane plane_statement* End;

harmonic_restraint:
	Restraints? Harmonic harmonic_statement* End;

rdc_restraint:
	Sanisotropy sani_statement* End;

coupling_restraint:
	Coupling coupling_statement* End;

carbon_shift_restraint:
	Carbon carbon_shift_statement* End;

proton_shift_restraint:
	Proton proton_shift_statement* End;

conformation_db_restraint:
	Conformation conformation_statement* End;

diffusion_anisotropy_restraint:
	Danisotropy diffusion_statement* End;

one_bond_coupling_restraint:
	OneBond one_bond_coupling_statement* End;

angle_db_restraint:
	AngleDb angle_db_statement* End;

/* CNS: Distance restraints - Syntax - noe
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
noe_statement:
	Analysis Equ_op? Noe_analysis |
	noe_assign |
	noe_assign_loop |
	Asymptote class_name number_s |
	Average Class_name_AM Averaging_methods |
	Bhig class_name number_s |
	Ceiling Equ_op? number_s |
	classification |
	CountViol class_name |
	Cv Equ_op? Integer |
	Den Initialize |
	Den Update Gamma Equ_op? number_s Kappa Equ_op? number_s |
	Distribute class_name class_name number_s |
	Ensemble *? End |
	Monomers class_name Integer |
	Ncount class_name Integer |
	Nrestraints Equ_op? Integer |
	Outd |
	Partition Equ_op? Integer |
	Potential Class_name_PT Potential_types |
	Predict predict_statement End |
	Print Threshold Equ_op? number_s |
	Raverage class_name *? End |
	Reset |
	Rswitch class_name number_s |
	Scale class_name number_s |
	SoExponent class_name number_s |
	SqConstant class_name number_s |
	SqExponent class_name number_s |
	SqOffset class_name number_s |
	Taverage class_name *? End |
	Temperature Equ_op? number_s;

noe_assign:
	Assign selection selection number number? number?
	noe_annotation*
	(Or_op Assign? selection selection number? number? number?)*;

predict_statement:
	Cutoff Equ_op? number_s | Cuton Equ_op? number_s | From selection | To selection;

noe_annotation:
	Peak Equ_op? number_a |
	Spectrum Equ_op? number_a |
	Weight Equ_op? number_a |
	(Volume | Vol) Equ_op? number_a |
	Ppm1 Equ_op? number_a |
	Ppm2 Equ_op? number_a |
	Cv Equ_op? number_a |
	Comma;

/* CNS: Dihedral angle restraints - Syntax - restranits/dihedral
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
dihedral_statement:
	vector_statement |
	dihedral_assign |
	dihedral_assign_loop |
	Cv Equ_op? Integer |
	Nassign Equ_op? Integer |
	Partition Equ_op? Integer |
	Reset |
	Scale Equ_op? number_s |
	Print_any;

dihedral_assign:
	Assign selection selection selection selection number number number Integer;

/* CNS: Plane restraints - Syntax - restraints/plane
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
plane_statement:
	vector_statement |
	plane_group |
	plane_group_loop |
	Initialize |
	Print_any;

plane_group:
	Group group_statement* End;

group_statement:
	Selection Equ_op? selection |
	Weight Equ_op? number_s;

/* CNS: Harmonic coordinate restraints - Syntax - restraints/harmonic
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
harmonic_statement:
	vector_statement |
	Exponent Equ_op? Integer |
	Normal Equ_op? L_paren (number_s Comma? number_s Comma? number_s | Tail Equ_op? selection Comma? (Head Equ_op? selection)?) R_paren;

harmonic_assign:
	Assign selection number number number;

/* CNS: Suscetibility anisotropy restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
sani_statement:
	sani_assign |
	sani_assign_loop |
	classification |
	Coefficients number_s number_s number_s |
	ForceConstant Equ_op? number_s |
	Nrestraints Equ_op? Integer |
	Potential Equ_op_PT? Potential_types |
	Print Threshold number_s |
	Reset;

sani_assign:
	Assign selection selection selection selection selection selection number number? number?;

/* CNS: Scalar J-coupling restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
coupling_statement:
	coup_assign |
	coup_assign_loop |
	classification |
	Coefficients number_s number_s number_s number_s |
	Cv Equ_op? Integer |
	ForceConstant number_s number_s? |
	Nrestraints Equ_op? Integer |
	Partition Equ_op? Integer |
	Potential Equ_op_PT? Potential_types |
	Print Threshold number_s (All | classification) |
	Reset;

coup_assign:
	Assign selection selection selection selection (selection selection selection selection)? number number (number number)?;

/* CNS: Carbon chemical shift restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
carbon_shift_statement:
	carbon_shift_assign |
	carbon_shift_assign_loop |
	classification |
	Expectation Integer Integer number_s number_s number_s |
	ForceConstant Equ_op? number_s |
	Nrestraints Equ_op? Integer |
	PhiStep Equ_op? number_s |
	PsiStep Equ_op? number_s |
	Potential Equ_op_PT? Potential_types |
	Print Threshold number_s |
	carbon_shift_rcoil |
	Reset |
	Zero;

carbon_shift_assign:
	Assign selection selection selection selection selection number number;

carbon_shift_rcoil:
	Rcoil selection number number;

/* CNS: Proton chemical shift restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
proton_shift_statement:
	observed |
	proton_shift_rcoil |
	proton_shift_anisotropy |
	proton_shift_amides |
	proton_shift_carbons |
	proton_shift_nitrogens |
	proton_shift_oxygens |
	proton_shift_ring_atoms |
	proton_shift_alphas_and_amides |
	classification |
	Error Equ_op? number_s |
	ForceConstant number_s number_s? |
	Potential Potential_types |
	Print Threshold number_s (All | classification) Simple_name |
	Reset;

observed:
	Observed selection selection? number number?;

proton_shift_rcoil:
	Rcoil selection number;

proton_shift_anisotropy:
	Anisotropy selection selection selection Simple_name Logical? Simple_name;

proton_shift_amides:
	Amides selection;

proton_shift_carbons:
	Carbon selection;

proton_shift_nitrogens:
	Nitrogens selection;

proton_shift_oxygens:
	Oxygens selection;

proton_shift_ring_atoms:
	RingAtoms Simple_name selection selection selection selection selection selection?;

proton_shift_alphas_and_amides:
	AlphasAndAmides selection;

/* CNS: Conformation database restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
conformation_statement:
	conf_assign |
	classification |
	Compressed |
	Expectation Integer Integer? Integer? Integer? number_s |
	Error Equ_op? number_s |
	ForceConstant Equ_op? number_s |
	Nrestraints Equ_op? Integer |
	Phase Integer Integer Integer (Integer Integer Integer)? (Integer Integer Integer)? (Integer Integer Integer)? |
	Potential Equ_op_PT? Potential_types |
	Print Threshold number_s (All | classification) |
	Reset |
	Size Dimensions Integer Integer? Integer? Integer? |
	Zero;

conf_assign:
	Assign selection selection selection selection (selection selection selection selection)? (selection selection selection selection)? (selection selection selection selection)?;

/* CNS: Diffusion anisotropy restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
diffusion_statement:
	dani_assign |
	classification |
	Coefficients number_s number_s number_s number_s number_s |
	ForceConstant Equ_op? number_s |
	Nrestraints Equ_op? Integer |
	Potential Equ_op_PT? Potential_types |
	Print Threshold number_s |
	Reset;

dani_assign:
	Assign selection selection selection selection selection selection number number?;

/* CNS: One-bond coupling restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
one_bond_coupling_statement:
	one_bond_assign |
	classification |
	Coefficients number_s number_s number_s number_s number_s number_s number_s |
	ForceConstant Equ_op? number_s |
	Nrestraints Equ_op? Integer |
	Potential Equ_op_PT? Potential_types |
	Print Threshold number_s |
	Reset;

one_bond_assign:
	Assign selection selection selection selection selection selection selection selection number number;

/* CNS: Angle database restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
angle_db_statement:
	angle_db_assign |
	classification |
	DerivFlag Equ_op? Simple_name |
	Expectation Integer Integer number_s |
	Error Equ_op? number_s |
	ForceConstant Equ_op? number_s |
	Nrestraints Equ_op? Integer |
	Potential Equ_op_PT? Potential_types |
	Print Threshold number_s (All | classification) |
	Reset |
	Size (AngleDb | Dihedral) Integer Integer |
	Zero;

angle_db_assign:
	Assign selection selection selection selection selection selection selection selection selection selection selection selection?;

/* CNS: NCS restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
ncs_restraint:
	Ncs Restraints ncs_statement* End;

ncs_statement:
	Group ncs_group_statement* End |
	Initialize |
	Print_any;

ncs_group_statement:
	Equivalence Equ_op? selection |
	Sigb Equ_op? number_s |
	Weight Equ_op? number_s;

/* Atom selection - Syntax - identity/atom-selection
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
selection:
	L_paren selection_expression R_paren;

selection_expression:
	term (Or_op term)*;

term:
	factor (And_op factor)*;

factor:
	L_paren selection_expression R_paren |
	All |
	factor Around number_f |
	Atom (Simple_names | Simple_name | Double_quote_string) (Integers | Integer) (Simple_names | Simple_name | Double_quote_string | Logical) |
	Attribute Abs? Attr_properties Comparison_ops number_f |
	BondedTo factor |
	ByGroup factor |
	ByRes factor |
	Chemical (Simple_names | Simple_name (Colon Simple_name)? | Symbol_name) |
	Fbox number_f number_f number_f number_f number_f number_f |
	Hydrogen |
	Id Integer |
	Known |
	Name (Simple_names | Simple_name (Colon Simple_name)? | Double_quote_string (Colon Double_quote_string)? | Symbol_name | Logical) |
	NONE |
	Not_op factor |
	Point L_paren number_f Comma? number_f Comma? number_f R_paren Cut number_f |
	Point L_paren Tail Equ_op? selection Comma? (Head Equ_op? selection)? R_paren Cut number_f |
	Previous |
	Pseudo |
	Residue (Integers | Integer (Colon Integer)? | Symbol_name) |
	Resname (Simple_names | Simple_name (Colon Simple_name)? | Symbol_name) |
	factor Saround number_f |
	SegIdentifier Equ_op? (Simple_names | Simple_name (Colon Simple_name)? | Double_quote_string (Colon Double_quote_string)? | Symbol_name | Integer) |
	Sfbox number_f number_f number_f number_f number_f number_f |
	Store1 | Store2 | Store3 | Store4 | Store5 | Store6 | Store7 | Store8 | Store9 |
	Tag;

/* Three-dimentional vectors - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html

vector_3d:
	L_paren number_f Comma? number_f Comma? number_f R_paren |
	L_paren Tail Equ_op? selection Comma? (Head Equ_op? selection)? R_paren;
*/

/* number expression in assign */
number:	Real | Integer | Symbol_name;

/* number expression in factor */
number_f:
	Real | Integer;

/* number expression in statement */
number_s:
	Real | Integer | Symbol_name;

/* number expression in annotation */
number_a:
	Real | Integer;

/* classification */
classification:
	Classification Equ_op? class_name;

/* class name */
class_name:
	Simple_name | Noe | Restraints | AngleDb | HBonded | Dihedral | Improper;

/* XPLOR-NIH: Flags - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node125.html (compatible with XPLOR-NIH)
*/
flag_statement:
	Flags (Exclude (Class_name* | Any_class))? Include Class_name* End_FL;

/* Vector statement - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node42.html (compatible with XPLOR-NIH)
*/
vector_statement:
	Vector vector_mode selection;

vector_mode:
	(Do_Lp | Identity_Lp) vector_expression R_paren_VE |
	Show vector_show_property;

vector_expression:
	Atom_properties_VE (Equ_op_VE vector_operation)?;

vector_operation:
	vflc ((Add_op_VE | Sub_op_VE | Mul_op_VE | Div_op_VE | Exp_op_VE) vector_operation)?;

vflc:
	Atom_properties_VE | vector_func_call | Integer_VE | Real_VE | Simple_name_VE | Symbol_name_VE | Double_quote_string_VE;

vector_func_call:
	Abs_VE L_paren_VF vflc R_paren_VE |
	Acos_VE L_paren_VF vflc R_paren_VE |
	Cos_VE L_paren_VF vflc R_paren_VE |
	Decode_VE L_paren_VF vflc R_paren_VE |
	Encode_VE L_paren_VF vflc R_paren_VE |
	Exp_VE L_paren_VF vflc R_paren_VE |
	Gauss_VE L_paren_VF vflc R_paren_VE |
	Heavy_VE L_paren_VF vflc R_paren_VE |
	Int_VE L_paren_VF vflc R_paren_VE |
	Log10_VE L_paren_VF vflc R_paren_VE |
	Log_VE L_paren_VF vflc R_paren_VE |
	Max_VE L_paren_VF vflc (Comma_VE vflc)* R_paren_VE |
	Maxw_VE L_paren_VF vflc R_paren_VE |
	Min_VE L_paren_VF vflc (Comma_VE vflc)* R_paren_VE |
	Mod_VE L_paren_VF vflc Comma_VE vflc R_paren_VE |
	Norm_VE L_paren_VF vflc R_paren_VE |
	Random_VE L_paren_VF R_paren_VE |
	Sign_VE L_paren_VF vflc R_paren_VE |
	Sin_VE L_paren_VF vflc R_paren_VE |
	Sqrt_VE L_paren_VF vflc R_paren_VE |
	Tan_VE L_paren_VF vflc R_paren_VE;

vector_show_property:
	(Average_VS | Element_VS | Max_VS | Min_VS | Norm_VS | Rms_VS | Sum_VS) L_paren_VS Atom_properties_VS R_paren_VS;

/* CNS: Global statement/Evaluate statement - Syntax_
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
evaluate_statement:
	Evaluate_Lp Symbol_name_VE Equ_op_VE evaluate_operation R_paren_VE;

evaluate_operation:
	vflc ((Add_op_VE | Sub_op_VE | Mul_op_VE | Div_op_VE | Exp_op_VE) evaluate_operation)?;

/* CNS: Patch molecular topology database - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
patch_statement:
	Patch class_name? Reference Equ_op (Nil | Integer) Equ_op selection (Reference Equ_op (Nil | Integer) Equ_op selection)? End;

/* CNS: Parameter statement - Syntax (implement only type-based statement)
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
parameter_setting:
	Parameter parameter_statement* End;

parameter_statement:
	AngleDb Simple_name Simple_name Simple_name number_s number_s (UB number_s number_s)? |
	BondedTo Simple_name Simple_name number_s number_s |
	(Dihedral | Improper) Simple_name Simple_name Simple_name Simple_name (Mult Integer)? number_s Integer number_s |
	HBonded Simple_names Simple_names number_s number_s |
	NBFix Simple_name Simple_name number_s number_s number_s number_s |
	NonB Simple_name number_s number_s number_s number_s |
	(Reset | VDWOff) Simple_name |
	Verbose;

/* CNS: Control statement - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
noe_assign_loop:
	For Symbol_name_CF
	In_CF L_paren_CF (Integer_CF* | Real_CF* | Simple_name_CF*) R_paren_CF Loop Simple_name_LL
	(evaluate_statement | noe_assign | distance_restraint)*
	End Loop Simple_name_LL;

dihedral_assign_loop:
	For Symbol_name_CF
	In_CF L_paren_CF (Integer_CF* | Real_CF* | Simple_name_CF*) R_paren_CF Loop Simple_name_LL
	(evaluate_statement | dihedral_assign | dihedral_angle_restraint)*
	End Loop Simple_name_LL;

sani_assign_loop:
	For Symbol_name_CF
	In_CF L_paren_CF (Integer_CF* | Real_CF* | Simple_name_CF*) R_paren_CF Loop Simple_name_LL
	(evaluate_statement | sani_assign | rdc_restraint)*
	End Loop Simple_name_LL;

coup_assign_loop:
	For Symbol_name_CF
	In_CF L_paren_CF (Integer_CF* | Real_CF* | Simple_name_CF*) R_paren_CF Loop Simple_name_LL
	(evaluate_statement | coup_assign | coupling_restraint)*
	End Loop Simple_name_LL;

carbon_shift_assign_loop:
	For Symbol_name_CF
	In_CF L_paren_CF (Integer_CF* | Real_CF* | Simple_name_CF*) R_paren_CF Loop Simple_name_LL
	(evaluate_statement | carbon_shift_assign | carbon_shift_restraint)*
	End Loop Simple_name_LL;

plane_group_loop:
	For Symbol_name_CF
	In_CF L_paren_CF (Integer_CF* | Real_CF* | Simple_name_CF*) R_paren_CF Loop Simple_name_LL
	(evaluate_statement | plane_group | plane_restraint)*
	End Loop Simple_name_LL;

