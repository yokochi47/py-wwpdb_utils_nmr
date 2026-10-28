/*
 XPLOR-NIH MR (Magnetic Restraint) parser grammar for ANTLR v4.
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

parser grammar XplorMRParser;

options { tokenVocab=XplorMRLexer; }

xplor_nih_mr:
	(
	distance_restraint |
	dihedral_angle_restraint |
	rdc_restraint |
	planar_restraint |
	harmonic_restraint |
	antidistance_restraint |
	coupling_restraint |
	carbon_shift_restraint |
	proton_shift_restraint |
	dihedral_angle_db_restraint |
	radius_of_gyration_restraint |
	diffusion_anisotropy_restraint |
	orientation_db_restraint |
	csa_restraint |
	pcsa_restraint |
	one_bond_coupling_restraint |
	angle_db_restraint |
	pre_restraint |
	pcs_restraint |
	prdc_restraint |
	porientation_restraint |
	pccr_restraint |
	hbond_restraint |
	hbond_db_restraint |
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
	hbond_assign_loop |		// allowing bare assign clauses for Hydrogen bond geometry restraints
	hbond_db_assign_loop |		// allowing bare assign clauses for Hydrogen bond database restraints
	coup_assign_loop |		// allowing bare assign clauses for Scaler J-coupling restraints
	xadc_assign_loop |		// allowing bare assign clauses for Antidistance restraints
	coll_assign_loop |		// allowing bare assign clauses for Radius of gyration restraints
	csa_assign_loop |		// allowing bare assign clauses for CSA restraints
	pre_assign_loop |		// allowing bare assign clauses for PRE restraints
	pcs_assign_loop |		// allowing bare assign clauses for PCS restraints or Carbon chemical shift restraints
	noe_assign |			// allowing bare assign clauses for Distance restraints
	dihedral_assign |		// allowing bare assign clauses for Dihedral angle restraints
	sani_assign |			// allowing bare assign clauses for RDC restraints
	planar_statement |		// allowing bare group clauses for Planarity restraints
	harmonic_assign |		// allowing individual assign clauses for Harmonic coordinate restraints
	hbond_assign |			// allowing bare assign clauses for Hydrogen bond geometry restraints
	hbond_db_assign |		// allowing bare assign clauses for Hydrogen bond database restraints
	coup_assign |			// allowing bare assign clauses for Scaler J-coupling or RDC (VEAN) restraints
	xadc_assign |			// allowing bare assign clauses for Antidistance restraints
	coll_assign |			// allowing bare assign clauses for Radius of gyration restraints
	csa_assign |			// allowing bare assign clauses for CSA restraints
	pre_assign |			// allowing bare assign clauses for PRE restraints
	pcs_assign |			// allowing bare assign clauses for PCS restraints or Carbon chemical shift restraints
	observed |			// allowing bare observed clauses for Proton chemical shift restraints
	parameter_statement		// allowing bare parameter statement
	)*
	EOF;

distance_restraint:
	Noe noe_statement* End;

dihedral_angle_restraint:
	Restraints? Dihedral dihedral_statement* End;

rdc_restraint:
	Sanisotropy sani_statement* End |
	(Xdipolar | Dipolar) xdip_statement* End |
	VeAngle vean_statement* End |
	Tensor tenso_statement* End |
	Anisotropy anis_statement* End;

planar_restraint:
	Restraints? Planar planar_statement* End;

harmonic_restraint:
	Restraints? Harmonic harmonic_statement* End;

antidistance_restraint:
	Xadc antidistance_statement* End;

coupling_restraint:
	Coupling coupling_statement* End;

carbon_shift_restraint:
	Carbon carbon_shift_statement* End;

proton_shift_restraint:
	Proton proton_shift_statement* End;

dihedral_angle_db_restraint:
	Ramachandran ramachandran_statement* End;

radius_of_gyration_restraint:
	Collapse collapse_statement* End;

diffusion_anisotropy_restraint:
	Danisotropy diffusion_statement* End;

orientation_db_restraint:
	Orient orientation_statement* End;

csa_restraint:
	Dcsa csa_statement* End;

pcsa_restraint:
	Pcsa pcsa_statement* End;

one_bond_coupling_restraint:
	OneBond one_bond_coupling_statement* End;

angle_db_restraint:
	AngleDb angle_db_statement* End;

pre_restraint:
	PMagnetic pre_statement* End;

pcs_restraint:
	Xpcs pcs_statement* End;

prdc_restraint:
	Xrdcoupling prdc_statement* End;

porientation_restraint:
	Xangle porientation_statement* End;

pccr_restraint:
	Xccr pccr_statement* End;

hbond_restraint:
	Hbda hbond_statement* End;

hbond_db_restraint:
	Hbdb hbond_db_statement* End;

/* XPLOR-NIH: Distance restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node377.html
*/
noe_statement:
	noe_assign |
	noe_assign_loop |
	classification |
	Asymptote class_name number_s |
	Average Class_name_AM Averaging_methods |
	Bhig class_name number_s |
	Ceiling Equ_op? number_s |
	CountViol class_name |
	Distribute class_name class_name number_s |
	Monomers class_name Integer |
	Ncount class_name Integer |
	Nrestraints Equ_op? Integer |
	Potential Class_name_PT Potential_types |
	Predict predict_statement End |
	Print Threshold Equ_op? number_s |
	Reset |
	Rswitch class_name number_s |
	Scale class_name number_s |
	SoExponent class_name number_s |
	SqConstant class_name number_s |
	SqExponent class_name number_s |
	SqOffset class_name number_s |
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
	Cv Equ_op? number_a? |
	Comma;

/* XPLOR-NIH: Dihedral angle restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/cdih_syntax.html
*/
dihedral_statement:
	vector_statement |
	dihedral_assign |
	dihedral_assign_loop |
	Nassign Equ_op? Integer |
	Reset |
	Scale Equ_op? number_s |
	Print_any;

dihedral_assign:
	Assign selection selection selection selection number number number Integer;

/* XPLOR-NIH: Residual Dipolar Couplings - Syntax (SANI - Susceptibility anisotropy)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node418.html
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

/* XPLOR-NIH: Residual Dipolar Couplings - Syntax (XDIP)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node419.html
*/
xdip_statement:
	xdip_assign |
	classification |
	Type Rdc_dist_fix_types |
	Scale Equ_op? number_s |
	Sign Logical |
	Average Averaging_methods |
	Coefficients number_s number_s number_s |
	ForceConstant Equ_op? number_s |
	Nrestraints Equ_op? Integer |
	Potential Equ_op_PT? Potential_types |
	Print Threshold number_s |
	Reset;

xdip_assign:
	Assign selection selection selection selection selection selection number number (number | number number number number)?;

/* XPLOR-NIH: Residual Dipolar Couplings - Syntax (VEAN)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node420.html
*/
vean_statement:
	vean_assign |
	Cv Equ_op? Integer |
	classification |
	ForceConstant Equ_op? number_s number_s |
	Nrestraints Equ_op? Integer |
	Partition Equ_op? Integer |
	Print Threshold number_s |
	Reset;

vean_assign:
	Assign selection selection selection selection number number (number number)?;

/* XPLOR-NIH: Residual Dipolar Couplings - Syntax (TENSO)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node421.html
*/
tenso_statement:
	tenso_assign |
	classification |
	Coefficients number_s |
	Nrestraints Equ_op? Integer |
	Potential Equ_op_PT? Potential_types |
	Print Threshold number_s |
	Reset;

tenso_assign:
	Assign selection selection number number?;

/* XPLOR-NIH: Residual Dipolar Couplings - Syntax (ANIS)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node422.html
*/
anis_statement:
	anis_assign |
	classification |
	Coefficients number_s number_s number_s number_s |
	ForceConstant Equ_op? number_s |
	Nrestraints Equ_op? Integer |
	Potential Equ_op_PT? Potential_types |
	Print Threshold number_s |
	Reset |
	Type Rdc_or_Diff_anis_types;

anis_assign:
	Assign selection selection selection selection number number?;

/* XPLOR-NIH: Planarity restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/plan_syntax.html
*/
planar_statement:
	vector_statement |
	planar_group |
	planar_group_loop |
	Initialize |
	Print_any;

planar_group:
	Group group_statement* End;

group_statement:
	Selection Equ_op? selection |
	Weight Equ_op? number_s;

/* XPLOR-NIH: Harmonic coordiate restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node176.html
*/
harmonic_statement:
	vector_statement |
	Exponent Equ_op? Integer |
	Normal Equ_op? L_paren (number_s Comma? number_s Comma? number_s | Tail Equ_op? selection Comma? (Head Equ_op? selection)?) R_paren;

harmonic_assign:
	Assign selection number number number;

/* XPLOR-NIH: Antidiatance restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node398.html
*/
antidistance_statement:
	xadc_assign |
	xadc_assign_loop |
	classification |
	Expectation Integer number_s |
	ForceConstant Equ_op? number_s |
	Nrestraints Equ_op? Integer |
	Print Threshold number_s (All | classification) |
	Reset |
	Size number_s Integer |
	Zero;

xadc_assign:
	Assign selection selection;

/* XPLOR-NIH: Scalar J-coupling restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node401.html
*/
coupling_statement:
	coup_assign |
	coup_assign_loop |
	classification |
	Coefficients number_s number_s number_s number_s |
	Cv Equ_op? Integer |
	Degeneracy Integer |
	ForceConstant number_s number_s? |
	Nrestraints Equ_op? Integer |
	Partition Equ_op? Integer |
	Potential Equ_op_PT? Potential_types |
	Print Threshold number_s (All | classification) |
	Reset;

coup_assign:
	Assign selection selection selection selection (selection selection selection selection)? number number (number number)?;

/* XPLOR-NIH: Carbon chemical shift restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node404.html
*/
carbon_shift_statement:
	carbon_shift_assign |
	classification |
	Expectation Integer Integer number_s number_s number_s |
	ForceConstant Equ_op? number_s |
	Nrestraints Equ_op? Integer |
	PhiStep number_s |
	PsiStep number_s |
	Potential Equ_op_PT? Potential_types |
	Print Threshold number_s |
	carbon_shift_rcoil |
	Reset |
	Zero;

carbon_shift_assign:
	Assign selection selection selection selection selection number number;

carbon_shift_rcoil:
	Rcoil selection number number;

/* XPLOR-NIH: Proton chemical shift restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node407.html
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
	Error number_s |
	Degeneracy Integer |
	ForceConstant number_s number_s? |
	Potential Equ_op_PT? Potential_types |
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

/* XPLOR-NIH: Dihedral angle database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node410.html
*/
ramachandran_statement:
	rama_assign |
	classification |
	Cutoff number_s |
	ForceConstant Equ_op? number_s |
	Gaussian number_s number_s number_s (number_s number_s number_s)? (number_s number_s number_s)? (number_s number_s number_s)? |
	Nrestraints Equ_op? Integer |
	Phase number_s number_s number_s (number_s number_s number_s)? (number_s number_s number_s)? (number_s number_s number_s)? |
	Print Threshold number_s (All | classification) |
	Quartic number_s number_s number_s (number_s number_s number_s)? (number_s number_s number_s)? (number_s number_s number_s)? |
	Reset |
	Scale Equ_op? number_s |
	Shape Gauss_or_Quart |
	Size Dimensions number_s number_s? number_s? number_s? |
	Sort |
	Zero;

rama_assign:
	Assign selection selection selection selection (selection selection selection selection)? (selection selection selection selection)? (selection selection selection selection)?;

/* XPLOR-NIH: Radius of gyration restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node413.html
*/
collapse_statement:
	coll_assign |
	coll_assign_loop |
	Scale Equ_op? number_s |
	Print |
	Reset;

coll_assign:
	Assign selection number number;

/* XPLOR-NIH: Diffusion anisotropy restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node415.html
*/
diffusion_statement:
	dani_assign |
	classification |
	Coefficients number_s number_s number_s number_s number_s |
	ForceConstant Equ_op? number_s |
	Nrestraints Equ_op? Integer |
	Potential Equ_op_PT? Potential_types |
	Print Threshold number_s |
	Reset |
	Type Rdc_or_Diff_anis_types;

dani_assign:
	Assign selection selection selection selection selection selection number number?;

/* XPLOR-NIH: Residue-residue position/orientation database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node425.html
*/
orientation_statement:
	orie_assign |
	classification |
	Cutoff number_s |
	Height number_s |
	ForceConstant Equ_op? number_s |
	Gaussian number_s number_s number_s number_s number_s number_s number_s |
	MaxGaussians Integer |
	NewGaussian number_s number_s number_s number_s number_s number_s number_s number_s |
	Nrestraints Equ_op? Integer |
	Print Threshold number_s (All | classification) |
	Quartic number_s number_s number_s number_s number_s number_s number_s |
	Reset |
	Residue Integer |
	Size number_s number_s |
	Zero;

orie_assign:
	Assign selection selection selection selection;

/* XPLOR-NIH: Chemical shift anisotropy restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node427.html
*/
csa_statement:
	csa_assign |
	csa_assign_loop |
	classification |
	Scale Equ_op? number_s |
	Type Csa_types |
	Coefficients number_s number_s number_s |
	Sigma number_s number_s number_s |
	ForceConstant Equ_op? number_s |
	Nrestraints Equ_op? Integer |
	Potential Equ_op_PT? Potential_types |
	Print Threshold number_s |
	Reset;

csa_assign:
	Assign selection selection selection selection selection selection selection number number? number?;

/* XPLOR-NIH: Pseudo chemical shift anisotropy restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node430.html
*/
pcsa_statement:
	csa_assign |
	classification |
	Scale Equ_op? number_s |
	Coefficients number_s number_s number_s |
	Sigma number_s number_s number_s number_s |
	ForceConstant Equ_op? number_s |
	Nrestraints Equ_op? Integer |
	Potential Equ_op_PT? Potential_types |
	Print Threshold number_s |
	Reset;

/* XPLOR-NIH: One-bond coupling restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node433.html
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

/* XPLOR-NIH: Angle database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node435.html
*/
angle_db_statement:
	angle_db_assign |
	classification |
	DerivFlag Simple_name |
	Expectation Integer Integer number_s |
	Error number_s |
	ForceConstant Equ_op? number_s |
	Nrestraints Equ_op? Integer |
	Potential Equ_op_PT? Potential_types |
	Print Threshold number_s (All | classification) |
	Reset |
	Size (AngleDb | Dihedral) Integer Integer |
	Zero;

angle_db_assign:
	Assign selection selection selection selection selection selection selection selection selection selection selection selection?;

/* XPLOR-NIH: Paramagnetic relaxation enhancement restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node438.html
*/
pre_statement:
	pre_assign |
	pre_assign_loop |
	classification |
	ForceConstant Equ_op? class_name number_s |
	Nrestraints Equ_op? Integer |
	Potential Equ_op_PT? Class_name_PT Potential_types |
	Kconst Equ_op? class_name number_s |
	Omega Equ_op? class_name number_s |
	Tauc Equ_op? class_name number_s number_s |
	Print Threshold number_s (All | classification) |
	Reset |
	Debug;

pre_assign:
	Assign selection selection number number?;

/* XPLOR-NIH: Paramagnetic pseudocontact shift restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node442.html
*/
pcs_statement:
	pcs_assign |
	pcs_assign_loop |
	classification |
	Tolerance Integer |
	Coefficients number_s number_s |
	ForceConstant Equ_op? number_s |
	Nrestraints Equ_op? Integer |
	Print Threshold number_s (All | classification) |
	Reset |
	Save Simple_name |
	Fmed number_s Integer |
	ErrOn |
	ErrOff |
	Fon |
	Foff |
	Son |
	Soff |
	Frun Integer;

pcs_assign:
	Assign selection selection selection selection selection number number? number?;

/* XPLOR-NIH: Paramagnetic residual dipolar coupling restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node445.html
*/
prdc_statement:
	prdc_assign |
	classification |
	Tolerance Integer |
	Coefficients number_s number_s |
	ForceConstant Equ_op? number_s |
	Nrestraints Equ_op? Integer |
	ErrOn |
	ErrOff |
	Fmed |
	Fon |
	Foff |
	Frun |
	Print Threshold |
	Reset |
	Save Simple_name |
	Son |
	Soff;

prdc_assign:
	Assign selection selection selection selection selection selection number number?;

/* XPLOR-NIH: Paramagnetic orientation restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node448.html
*/
porientation_statement:
	porientation_assign |
	classification |
	ForceConstant Equ_op? number_s |
	Nrestraints Equ_op? Integer |
	Print Threshold number_s |
	Reset;

porientation_assign:
	Assign selection selection number number number;

/* XPLOR-NIH: Paramagnetic cross-correlation rate restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node450.html
*/
pccr_statement:
	pccr_assign |
	classification |
	Weip Integer |
	Coefficients number_s |
	ForceConstant Equ_op? number_s |
	Nrestraints Equ_op? Integer |
	Print Threshold number_s |
	Reset |
	Frun Integer;

pccr_assign:
	Assign selection selection selection number number?;

/* XPLOR-NIH: Hydrogen bond geometry restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node452.html
*/
hbond_statement:
	hbond_assign |
	hbond_assign_loop |
	classification |
	ForceConstant Equ_op? number_s |
	Nrestraints Equ_op? Integer |
	Print Threshold number_s |
	Reset;

hbond_assign:
	Assign selection selection selection;

/* XPLOR-NIH: Hydrogen bond database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node454.html
*/
hbond_db_statement:
	hbond_db_assign |
	hbond_db_assign_loop |
	Kdir Equ_op? number_s |
	Klin Equ_op? number_s |
	Nseg Equ_op? Integer |
	Nmin Equ_op? Integer |
	Nmax Equ_op? Integer |
	Segm Equ_op? Simple_name |
	Ohcut Equ_op? number_s |
	Coh1cut Equ_op? number_s |
	Coh2cut Equ_op? number_s |
	Ohncut Equ_op? number_s |
	Updfrq Equ_op? Integer |
	Prnfrq Equ_op? Integer |
	Freemode Equ_op? Integer;

hbond_db_assign:
	Assign selection selection;

/* XPLOR-NIH: NCS restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/doc/current/xplor/node341.html
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

/* Atom selection - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node39.html
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
	Hydrogen |
	Id Integer |
	Known |
	Name (Simple_names | Simple_name (Colon Simple_name)? | Double_quote_string (Colon Double_quote_string)? | Symbol_name | Logical) |
	Not_op factor |
	Point L_paren number_f Comma? number_f Comma? number_f R_paren Cut number_f |
	Point L_paren Tail Equ_op? selection Comma? (Head Equ_op? selection)? R_paren Cut number_f |
	Previous |
	Pseudo |
	Residue (Integers | Integer (Colon Integer)? | Symbol_name) |
	Resname (Simple_names | Simple_name (Colon Simple_name)? | Symbol_name) |
	factor Saround number_f |
	SegIdentifier Equ_op? (Simple_names | Simple_name (Colon Simple_name)? | Double_quote_string (Colon Double_quote_string)? | Symbol_name | Integer) |
	Store1 | Store2 | Store3 | Store4 | Store5 | Store6 | Store7 | Store8 | Store9 |
	Tag |
	Donor | Acceptor;

/* Three-dimentional vectors - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node15.html

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
	Classification Equ_op_CL? Class_name;

/* class name */
class_name:
	Simple_name | Noe | Restraints | AngleDb | HBonded | Dihedral | Improper | Average;

/* XPLOR-NIH: Flags - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node125.html
*/
flag_statement:
	Flags (Exclude (Class_name_FL* | Any_class))? Include Class_name_FL* End_FL;

/* Vector statement - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node42.html
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

/* XPLOR-NIH: Evaluate statement - Syntax_
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node36.html
*/
evaluate_statement:
	Evaluate_Lp Symbol_name_VE Equ_op_VE evaluate_operation R_paren_VE;

evaluate_operation:
	vflc ((Add_op_VE | Sub_op_VE | Mul_op_VE | Div_op_VE | Exp_op_VE) evaluate_operation)?;

/* XPLOR-NIH: Patching the Molecular Structure - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node86.html
*/
patch_statement:
	Patch class_name? Reference Equ_op (Nil | Integer) Equ_op selection (Reference Equ_op (Nil | Integer) Equ_op selection)? End;

/* XPLOR-NIH: Parameter statement - Syntax (implement only type-based statement)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node50.html
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

/* XPLOR-NIH: Control statement - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/doc/current/xplor/node24.html
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

xadc_assign_loop:
	For Symbol_name_CF
	In_CF L_paren_CF (Integer_CF* | Real_CF* | Simple_name_CF*) R_paren_CF Loop Simple_name_LL
	(evaluate_statement | xadc_assign | antidistance_restraint)*
	End Loop Simple_name_LL;

coup_assign_loop:
	For Symbol_name_CF
	In_CF L_paren_CF (Integer_CF* | Real_CF* | Simple_name_CF*) R_paren_CF Loop Simple_name_LL
	(evaluate_statement | coup_assign | coupling_restraint)*
	End Loop Simple_name_LL;

coll_assign_loop:
	For Symbol_name_CF
	In_CF L_paren_CF (Integer_CF* | Real_CF* | Simple_name_CF*) R_paren_CF Loop Simple_name_LL
	(evaluate_statement | coll_assign | radius_of_gyration_restraint)*
	End Loop Simple_name_LL;

csa_assign_loop:
	For Symbol_name_CF
	In_CF L_paren_CF (Integer_CF* | Real_CF* | Simple_name_CF*) R_paren_CF Loop Simple_name_LL
	(evaluate_statement | csa_assign | csa_restraint)*
	End Loop Simple_name_LL;

pre_assign_loop:
	For Symbol_name_CF
	In_CF L_paren_CF (Integer_CF* | Real_CF* | Simple_name_CF*) R_paren_CF Loop Simple_name_LL
	(evaluate_statement | pre_assign | pre_restraint)*
	End Loop Simple_name_LL;

pcs_assign_loop:
	For Symbol_name_CF
	In_CF L_paren_CF (Integer_CF* | Real_CF* | Simple_name_CF*) R_paren_CF Loop Simple_name_LL
	(evaluate_statement | pcs_assign | pcs_restraint | carbon_shift_restraint)*
	End Loop Simple_name_LL;

hbond_assign_loop:
	For Symbol_name_CF
	In_CF L_paren_CF (Integer_CF* | Real_CF* | Simple_name_CF*) R_paren_CF Loop Simple_name_LL
	(evaluate_statement | hbond_assign | hbond_restraint)*
	End Loop Simple_name_LL;

hbond_db_assign_loop:
	For Symbol_name_CF
	In_CF L_paren_CF (Integer_CF* | Real_CF* | Simple_name_CF*) R_paren_CF Loop Simple_name_LL
	(evaluate_statement | hbond_db_assign | hbond_db_restraint)*
	End Loop Simple_name_LL;

planar_group_loop:
	For Symbol_name_CF
	In_CF L_paren_CF (Integer_CF* | Real_CF* | Simple_name_CF*) R_paren_CF Loop Simple_name_LL
	(evaluate_statement | planar_group | planar_restraint)*
	End Loop Simple_name_LL;

