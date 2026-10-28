/*
 CNS MR (Magnetic Restraint) lexer grammar for ANTLR v4.
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

lexer grammar CnsMRLexer;

/* Case-Insensitive Lexing
 See also https://github.com/antlr/antlr4/blob/master/doc/case-insensitive-lexing.md
*/
fragment A:		[aA]; // match either an 'a' or 'A'
fragment B:		[bB];
fragment C:		[cC];
fragment D:		[dD];
fragment E:		[eE];
fragment F:		[fF];
fragment G:		[gG];
fragment H:		[hH];
fragment I:		[iI];
fragment J:		[jJ];
fragment K:		[kK];
fragment L:		[lL];
fragment M:		[mM];
fragment N:		[nN];
fragment O:		[oO];
fragment P:		[pP];
fragment Q:		[qQ];
fragment R:		[rR];
fragment S:		[sS];
fragment T:		[tT];
fragment U:		[uU];
fragment V:		[vV];
fragment W:		[wW];
fragment X:		[xX];
fragment Y:		[yY];
fragment Z:		[zZ];

Set:			S E T;
End:			E N D;

/* CNS: Distance restraints - Syntax - noe
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Noe:			N O E;					// Noe { noe_statement } End

// noe_statement
Analysis:		A N A L Y? S? I? S? -> pushMode(ANAL_MODE);	// = Noe_analysis
Assign:			A S S I G? N?;				// selection selection Real Real Real [ Or_op selection selection ... ]
Asymptote:		A S Y M P? T? O? T? E?;			// Class_names Real
Average:		A V E R A? G? ((I? N? G?) | E?) -> pushMode(AVER_MODE);	// Class_names Noe_avr_methods
Bhig:			B H I G;				// Class_names Real
Ceiling:		C E I L I? N? G?;			// = Real
Classification:		C L A S S? I? F? I? C? A? T? I? O? N? -> pushMode(CLAS_MODE);	// Class_name
CountViol:		C O U N T? V? I? O? L?;			// Class_name
Cv:			C V;					// = Integer
Den:			D E N;					// Initialize | ( Update Gamma = Real Kappa = Real )
Distribute:		D I S T R? I? B? U? T? E?;		// Class_name Class_name Real
Ensemble:		E N S E M? B? L? E?;			// Ensemble { ensemble_statement } End
Monomers:		M O N O M? E? R? S?;			// Class_names Integer
Ncount:			N C O U N? T?;				// Class_names Integer
Nrestraints:		N R E S T? R? A? I? N? T? S?;		// = Integer
Outd:			O U T D;
Partition:		P A R T I? T? I? O? N?;			// = Integer
Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// Class_names Noe_potential
Predict:		P R E D I? C? T?;			// { predict_statement } End
Print:			P R I N T?;
Raverage:		R A V E R? A? G? E?;			// Class_name Raverage_statement End
Threshold:		T H R E S? H? O? L? D?;			// = Real
Reset:			R E S E T?;
Rswitch:		R S W I T? C? H?;			// Class_names Real
Scale:			S C A L E?;				// Class_names Real
SoExponent:		S O E X P? O? N? E? N? T?;		// Class_names Real
SqConstant:		S Q C O O? N? S? T? A? N? T?;		// Class_names Real
SqExponent:		S Q E X P? O? N? E? N? T?;		// Class_names Real
SqOffset:		S Q O F F? S? E? T?;			// Class_names Real
Taverage:		T A V E R? A? G? E?;			// Class_name Taverage_statement End
Temperature:		T E M P E? R? A? T? U? R? E?;		// = Real

// NOE analysis
//Noe_analysis:		C U R R E? N? T? | T A V E R? A? G? E? | R A V E R? A? G? E?;

Initialize:		I N I T I? A? L? I? Z? E?;
Update:			U P D A T? E?;				// Gamma = Real Kappa = Real
Gamma:			G A M M A?;
Kappa:			K A P P A?;

// NOE averaging methods
//Noe_avr_methods:	R '-6' | R '-3' | S U M | C E N T E? R?;

// NOE potential statement
//Noe_potential:	B I H A R? M? O? N? I? C? | L O G N O? R? M? A? L? | S Q U A R? E? '-'? W? E? L? L? | S O F T '-'? S? Q? U? A? R? E? | S Y M M E? T? R? Y? | H I G H | '3' D P O;

// Predict statement
Cutoff:			C U T O F F;				// = Real
Cuton:			C U T O N;				// = Real
From:			F R O M;				// = selection
To:			T O;					// = selection

// 3rd party software extensions for NOE assign clause
Peak:			P E A K;				// = Integer
Spectrum:		S P E C T R U M;			// = Integer
//Weight:		W E I G H T;				// = Real
Volume:			V O L U M E;				// = Real
Vol:			V O L;					// = Real
Ppm1:			P P M '1';				// = Real
Ppm2:			P P M '2';				// = Real
//Cv:			C V;					// = Integer

/* CNS: Dihedral angle restraints - Syntax - restranits/dihedral
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Restraints:		R E S T R? A? I? N? T? S?;		// Dihedral
Dihedral:		D I H E D? R? A? L?;			// Dihedral { dihedral_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection Real Real Real Integer
//Cv:			C V;					// = Integer
Nassign:		N A S S I? G? N?;			// = Integer
//Partition:		P A R T I? T? I? O? N?;			// = Integer
//Reset:		R E S E T?;
//Scale:		S C A L E?;				// = Real
Print_any:		'?';

/* CNS: Plane restraints - Syntax - restraints/plane
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
//Restraints:		R E S T R? A? I? N? T? S?;		// Plane
Plane:			P L A N (E | A)? R?;			// Plane { planar_statement } End

// planar_statement
Group:			G R O U P?;				// Group { planar_group_statement } End
//Initialize:		I N I T I? A? L? I? Z? E?;
//Print_any:		'?';

// group_statement
Selection:		S E L E C? T? I? O? N? '='?;		// = selection
Weight:			W E I G H? T?;				// = Real

/* CNS: Plane restraints - Syntax - restraints/harmonic
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
//Restraints:		R E S T R? A? I? N? T? S?;		// Harmonic
Harmonic:		H A R M O? N? I? C?;			// Harmonic { harmonic_statement } End

// harmonic_stetement
Exponent:		E X P O N? E? N? T?;			// = Integer
Normal:			N O R M A? L?;				// = vector_3d

/* CNS: Suscetibility anisotropy restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Sanisotropy:		S A N I S? O? T? R? O? P? Y?;		// Sanisotropy { sani_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection selection Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// = Class_name
Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real Real Real
ForceConstant:		F O R C E? C? O? N? S? T? A? N? T?;	// = Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// = Integer
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// = Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
//Reset:		R E S E T?;

// RDC potential statement
//Rdc_potential:	S Q U A R? E? '-'? W? E? L? L? | H A R M O? N? I? C?;

/* CNS: Scalar J-coupling restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Coupling:		C O U P L? I? N? G?;			// Coupling { coupling_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection [ selection selection selection selection ] Real Real [ Real Real ]
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// = Class_name
//Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real Real Real Real
//Cv:			C V;					// = Integer
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real [ Real ]
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// = Integer
//Partition:		P A R T I? T? I? O? N?;			// = Integer
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// = Coupling_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real ( All | Class = Class_name )
//Reset:		R E S E T?;

//Coupling_potential:	Rdc_potential | M U L T I? P? L? E?;

/* CNS: Carbon chemical shift restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Carbon:			C A R B O? N?;				// Carbon { carbon_shift_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// = Class_name
Expectation:		E X P E C? T? A? T? I? O? N?;		// Integer Integer Real Real Real Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// = Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// = Integer
PhiStep:		P H I S T? E? P?;			// = Real
PsiStep:		P S I S T? E? P?;			// = Real
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// = Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
Rcoil:			R C O I L?;				// selection Real Real
//Reset:		R E S E T?;
Zero:			Z E R O;

/* CNS: Proton chemical shift restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Proton:			P R O T O N S? H? I? F? T? S?;	// Proton { proton_shift_statement } End
Observed:		O B S E R? V? E? D?;			// selection [ selection ] Real [ Real ]
//Rcoil:		R C O I L?;				// selection Real
Anisotropy:		A N I S O? T? R? O? P? Y?;		// selection selection selection Co_or_Cn Logical? SC_or_BB
Amides:			A M I D E? S?;				// selection
//Carbons:		C A R B O? N? S?;			// selection
Nitrogens:		N I T R O? G? E? N? S?;			// selection
Oxygens:		O X Y G E? N? S?;			// selection
RingAtoms:		R I N G A? T? O? M? S?;			// Ring_resname selection selection selection selection selection [ selection ]
AlphasAndAmides:	A L P H A? S? A? N? D? A? M? I? D? E? S?;	// selection
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// = Class_name
Error:			E R R O R?;				// Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real [ Real ]
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// Coupling_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real ( All | Class = Class_name ) Rmsd_or_Not
//Reset:		R E S E T?;

//CO_or_CN:		C O | C N;
//SC_or_BB:		S C | B B;
//Ring_resname:		P H E | T Y R | H I S | T R P ('5' | '6') | A D E ('5' | '6') | G U A ('5' | '6') | T H Y | C Y T | U R A;
//Rmsd_or_Not:		R M S D | N O R M S? D?;

/* CNS: Conformation database restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Conformation:		C O N F O? R? M? A? T? I? O? N?;	// Conformation { conformation_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection [ selection selection selection selection ] [ selection selection selection selection ] [ selection selection selection selection ]
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// = Class_name
Compressed:		C O M P R? E? S? S? E? D?;
//Expectation:		E X P E C? T? A? T? I? O? N?;		// Integer [ Integer ] [ Integer ] [ Integer ] Real
//Error:		E R R O R?;				// = Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// = Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// = Integer
Phase:			P H A S E?;				// Integer Integer Integer [ Integer Integer Integer ] (Integer Integer Integer ] (Integer Integer Integer ]
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// = Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real ( All | Class = Class_name )
//Reset:		R E S E T?;
Size:			S I Z E;				// Dimensions Integer [ Integer ] [ Integer ] [ Integer ]
//Zero:			Z E R O;

Dimensions:		O N E D | T W O D | T H R E E D | F O U R D;

/* CNS: Diffusion anisotropy restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Danisotropy:		D A N I S? O? T? R? O? P? Y?;		// Danisotropy { diffusion_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection selection Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// = Class_name
//Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real Real Real Real Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// = Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// = Integer
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// = Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
//Reset:		R E S E T?;

/* CNS: One-bond coupling restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
OneBond:		O N E B O? N? D?;			// OneBond { one_bond_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection selection selection selection Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// = Class_name
//Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real Real Real Real Real Real Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// = Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// = Integer
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// = Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
//Reset:		R E S E T?;

/* CNS: Angle database restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
AngleDb:		A N G L E? D? A? T? A? B? A? S? E?;	// AngleDb { bond_angle_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection selection selection selection selection selection selection [ selection ]
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// = Class_name
DerivFlag:		D E R I V? F? L? A? G?;			// On_or_Off
//Expectation:		E X P E C? T? A? T? I? O? N?;		// Integer Integer Real
//Error:		E R R O R?;				// = Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// = Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// = Integer
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// = Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real ( All | Class = Class_name )
//Reset:		R E S E T?;
//Size:			S I Z E;				// Angle_or_Dihedral Integer Integer
//Zero:			Z E R O;

//On_or_Off:		O N | O F F;
//Angle_or_Dihedral:	A N G L E? | D I H E D? R? A? L?;

/* CNS: NCS restraints - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Ncs:			N C S;
//Restraints:		R E S T R? A? I? N? T? S?;		// Ncs

//Group:		G R O U P?;				// Group { ncs_group_statement } End
//Initialize:		I N I T I? A? L? I? Z? E?;
//Print_any:		'?';

Equivalence:		E Q U I V? A? L? E? N? C? E? '='?;	// = selection
Sigb:			S I G B;				// = Real
//Weight:		W E I G H? T?;				// = Real

/* CNS: Flags - Syntax
 See alos https://nmr.cit.nih.gov/xplor-nih/xplorMan/node125.html (compatible with XPLOR-NIH)
*/
Flags:			F L A G S? -> pushMode(FLAG_MODE);	// Flags { flag_statement } End

/* Atom selection - Syntax - identity/atom-selection
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
All:			A L L;
Around:			A R O U N? D?;				// Real (factor as subject)
Atom:			A T O M;				// Segment_names Residue_numbers Atom_names
Attribute:		A T T R I? B? U? T? E? -> pushMode(ATTR_MODE);	// Abs? Attr_property Comparison_ops Real
BondedTo:		B O N D E? D? T? O?;			// factor
ByGroup:		B Y G R O? U? P?;			// factor
ByRes:			B Y R E S?;				// factor
Chemical:		C H E M I? C? A? L?;			// Atom_types | Atom_type [ : Atom_type ]
Fbox:			F B O X;				// real real real real real real
Hydrogen:		H Y D R O? G? E? N?;
Id:			I D;					// Integer
Known:			K N O W N?;
Name:			N A M E;				// Atom_names | Atom_name [ : Atom_name ]
NONE:			N O N E;
//Not_op:		N O T;					// factor
Point:			P O I N T?;				// vector_3d cut Real
Cut:			C U T;
Previous:		P R E V I? O? U? S?;
Pseudo:			P S E U D? O?;
Residue:		R E S I D? U? E?;			// Residue_numbers | Residue_number [ : Residue_number ]
Resname:		R E S N A? M? E?;			// Residue_names | Residue_name [ : Residue_name ]
Saround:		S A R O U? N? D?;			// Real (factor as subject)
SegIdentifier:		S E G I D? E? N? T? I? F? I? E? R?;	// Segment_names | Segment_name [ : Segment_name ]
Sfbox:			S F B O X;				// real real real real real real
Store1:			S T O R E '1';
Store2:			S T O R E '2';
Store3:			S T O R E '3';
Store4:			S T O R E '4';
Store5:			S T O R E '5';
Store6:			S T O R E '6';
Store7:			S T O R E '7';
Store8:			S T O R E '8';
Store9:			S T O R E '9';
Tag:			T A G;

/* Vector statement - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node42.html (compatible with XPLOR-NIH)
*/
Vector:			V E C T O? R?;				// vector_mode vector_expression selection

Do_Lp:			D O ' '* L_paren -> pushMode(VECTOR_EXPR_MODE);
Identity_Lp:		I D E N T? I? T? Y? ' '* L_paren -> pushMode(VECTOR_EXPR_MODE);
Show:			S H O W -> pushMode(VECTOR_SHOW_MODE);	// Vector_show_property

/* CNS: Global statement/Evaluate statement - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Evaluate_Lp:		E V A L U? A? T? E? ' '* L_paren -> pushMode(VECTOR_EXPR_MODE);
								// ( evaluate_statement )

/* CNS: Patch molecular topology database - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Patch:			P A T C H;				// ( patch_statement )
Reference:		R E F E R? E? N? C? E?;
Nil:			N I L;

/* CNS: Parameter statement - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Parameter:		P A R A M? E? T? E? R?;			// ( parameter_statement )
UB:			U B;
Mult:			M U L T;
HBonded:		H B O N D? E? D?;
Improper:		I M P R O? P? E? R?;
NBFix:			N B F I X?;
NonB:			N O N B;
VDWOff:			V D W O F? F?;
Verbose:		V E R B O? S? E?;

/* CNS: Control statement - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
For:			F O R -> pushMode(CTL_FOR_MODE);	// Symbol_name In ( Words ) Loop Loop_label { statements } End Loop Loop_label
Loop:			L O O P -> pushMode(LOOP_LABEL_MODE);

/* Three-dimentional vectors - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Tail:			T A I L '='?;
Head:			H E A D '='?;

// Logical operations
Or_op:			O R;
And_op:			A N D;
Not_op:			N O T;

/* Numbers and Strings - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
Comma:			',';
Complex:		L_paren Real Comma Real R_paren;
Integer:		'-'? DECIMAL;
Logical:		'TRUE' | 'FALSE' | 'ON' | 'OFF';
Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) (E ('+' | '-')? DECIMAL)?;
Double_quote_string:	'"' ~["\r\n]* '"';
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL?) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

SHARP_COMMENT:		'#'+ ~[\r\n]* '#'* ~[\r\n]* -> channel(HIDDEN);
EXCLM_COMMENT:		'!'+ ~[\r\n]* '!'* ~[\r\n]* -> channel(HIDDEN);
SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

Simple_name:		SIMPLE_NAME;
Simple_names:		(WILDCARD | WILDCARD* SIMPLE_NAME WILDCARD+ (SIMPLE_NAME | WILDCARD)*) POST_WC_CHAR*;
Integers:		(WILDCARD | WILDCARD* Integer WILDCARD+) DEC_DIGIT*;

/* Wildcard - Syntax
 See also https://www.mrc-lmb.cam.ac.uk/public/xtal/doc/cns/cns_1.3/syntax_manual/frame.html
*/
fragment WILDCARD:	'*' | '%' | '#' | '+';

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_';
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.' | '"';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
//fragment ATM_TYPE_CHAR:	ALPHA_NUM | '-' | '+';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;
fragment POST_WC_CHAR:	DEC_DIGIT | '\'' | P;
fragment SYMBOL_NAME:	'$' START_CHAR+;

L_paren:		'(';
R_paren:		')';
Colon:			':';
Equ_op:			'=';
Lt_op:			'<';
Gt_op:			'>';
Leq_op:			'<=';
Geq_op:			'>=';
Neq_op:			'#';

Symbol_name:		SYMBOL_NAME;

SPACE:			[ \t\r\n]+ -> skip;
ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	('#' | '!' | ';' | '\\' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | '>' '>'+ | R E M A R K S?) ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT:		('#' | '!' | ';' | '\\' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | '>' '>'+ | R E M A R K S?) ~[\r\n]* -> channel(HIDDEN);
SET_VARIABLE:		Set ([\r\n]*)? ~[\r\n]* ([\r\n]*)? End -> channel(HIDDEN);

mode ATTR_MODE; // Inside of Attribute tag

// Attribute properties
Abs:			A B S;
Attr_properties:	(B | B C O M P? | C H A R G? E? | D X | D Y | D Z | F B E T A? | H A R M O? N? I? C? S? | M A S S | Q | Q C O M P? | R E F X | R E F Y | R E F Z | R M S D | V X | V Y | V Z | X | X C O M P? | Y | Y C O M P? | Z | Z C O M P? | S T O R E '1' | S T O R E '2' | S T O R E '3' | S T O R E '4' | S T O R E '5' | S T O R E '6' | S T O R E '7' | S T O R E '8' | S T O R E '9' | S C A T T E R '_' A '1' | S C A T T E R '_' A '2' | S C A T T E R '_' A '3' | S C A T T E R '_' A '4' | S C A T T E R '_' B '1' | S C A T T E R '_' B '2' | S C A T T E R '_' B '3' | S C A T T E R '_' B '4' | S C A T T E R '_' C | S C A T T E R '_' F P | S C A T T E R '_' F D P);
Comparison_ops:		(Equ_op | Lt_op | Gt_op | Leq_op | Geq_op | Neq_op) -> popMode;

SPACE_AP:		[ \t\r\n]+ -> skip;

mode CLAS_MODE; // Inside of Classification tag

Equ_op_CL:		'=';

Class_name:		(SIMPLE_NAME | '*') -> popMode;

SPACE_CL:		[ \t\r\n]+ -> skip;

mode AVER_MODE; // Inside of Averaging tag

Averaging_methods:	(R '-6' | R '-3' | S U M | C E N T E? R?) -> popMode;

Class_name_AM:		SIMPLE_NAME | '*';

SPACE_AM:		[ \t\r\n]+ -> skip;

mode POTE_MODE; // Inside of Potential tag

Equ_op_PT:		'=';

Potential_types:	(B I H A R? M? O? N? I? C? | L O G N O? R? M? A? L? | S Q U A R? E? '-'? W? E? L? L? | S O F T '-'? S? Q? U? A? R? E? | S Y M M E? T? R? Y? | H I G H | '3' D P O | H A R M O? N? I? C? | M U L T I? P? L? E?) -> popMode;

Class_name_PT:		SIMPLE_NAME | '*';

SPACE_PT:		[ \t\r\n]+ -> skip;

mode ANAL_MODE; // Inside of Noe/Analysis tag

Noe_analysis:		(C U R R E? N? T? | T A V E R? A? G? E? | R A V E R? A? G? E?) -> popMode;

SPACE_NA:		[ \t\r\n]+ -> skip;

mode FLAG_MODE; // Inside of flag statement

Exclude:		E X C L U? D? E?;			// Class_name* | Any_class
Include:		I N C L U? D? E?;			// Class_name*

End_FL:			E N D -> popMode;

Class_name_FL:		SIMPLE_NAME;
Any_class:		'*';

SPACE_FL:		[ \t\r\n]+ -> skip;

mode VECTOR_EXPR_MODE; // vector expression

R_paren_VE:		')' -> popMode;

Equ_op_VE:		'=';
Add_op_VE:		'+';
Sub_op_VE:		'-';
Mul_op_VE:		'*';
Div_op_VE:		'/';
Exp_op_VE:		('^' | '*' '*');
Comma_VE:		',';

Integer_VE:		DECIMAL;
Real_VE:		(DECIMAL | DEC_DOT_DEC) (E ('+' | '-')? DECIMAL)?;

Atom_properties_VE:	(B | B C O M P? | C H A R G? E? | C H E M I? C? A? L? | D X | D Y | D Z | F B E T A? | H A R M O? N? I? C? S? | M A S S | N A M E | Q | Q C O M P? | R E F X | R E F Y | R E F Z | R E S I D? U? E? | R E S N A? M? E? | R M S D | S E G I D? E? N? T? I? F? I? E? R? | S T O R E '1' | S T O R E '2' | S T O R E '3' | S T O R E '4' | S T O R E '5' | S T O R E '6' | S T O R E '7' | S T O R E '8' | S T O R E '9' | P S E U D? O? | V X | V Y | V Z | X | X C O M P? | Y | Y C O M P? | Z | Z C O M P?);

Abs_VE:			A B S -> pushMode(VECTOR_FUNC_MODE);
Acos_VE:		A C O S -> pushMode(VECTOR_FUNC_MODE);
Asin_VE:		A S I N -> pushMode(VECTOR_FUNC_MODE);
Cos_VE:			C O S -> pushMode(VECTOR_FUNC_MODE);
Decode_VE:		D E C O D E -> pushMode(VECTOR_FUNC_MODE);
Encode_VE:		E N C O D E -> pushMode(VECTOR_FUNC_MODE);
Exp_VE:			E X P -> pushMode(VECTOR_FUNC_MODE);
Gauss_VE:		G A U S S -> pushMode(VECTOR_FUNC_MODE);
Heavy_VE:		H E A V Y -> pushMode(VECTOR_FUNC_MODE);
Int_VE:			I N T -> pushMode(VECTOR_FUNC_MODE);
Log10_VE:		L O G '1' '0' -> pushMode(VECTOR_FUNC_MODE);
Log_VE:			L O G -> pushMode(VECTOR_FUNC_MODE);
Max_VE:			M A X -> pushMode(VECTOR_FUNC_MODE);
Maxw_VE:		M A X W -> pushMode(VECTOR_FUNC_MODE);
Min_VE:			M I N -> pushMode(VECTOR_FUNC_MODE);
Mod_VE:			M O D -> pushMode(VECTOR_FUNC_MODE);
Norm_VE:		N O R M -> pushMode(VECTOR_FUNC_MODE);
Random_VE:		R A N D O? M? -> pushMode(VECTOR_FUNC_MODE);
Sign_VE:		S I G N -> pushMode(VECTOR_FUNC_MODE);
Sin_VE:			S I N -> pushMode(VECTOR_FUNC_MODE);
Sqrt_VE:		S Q R T -> pushMode(VECTOR_FUNC_MODE);
Tan_VE:			T A N -> pushMode(VECTOR_FUNC_MODE);

Symbol_name_VE:		SYMBOL_NAME;
Simple_name_VE:		SIMPLE_NAME;
Double_quote_string_VE:	'"' ~["\r\n]* '"';

SPACE_VE:		[ \t\r\n]+ -> skip;

mode VECTOR_FUNC_MODE; // vector function

L_paren_VF:		'(' -> pushMode(VECTOR_EXPR_MODE);

SPACE_VF:		[ \t\r\n]+ -> skip;

mode VECTOR_SHOW_MODE; // vector show

L_paren_VS:		'(';
R_paren_VS:		')' -> popMode;

Average_VS:		A V E R? A? G? E?;
Element_VS:		E L E M E? N? T?;
Max_VS:			M A X;
Min_VS:			M I N;
Norm_VS:		N O R M;
Rms_VS:			R M S;
Sum_VS:			S U M;

Atom_properties_VS:	(B | B C O M P? | C H A R G? E? | D X | D Y | D Z | F B E T A? | H A R M O? N? I? C? S? | M A S S | Q | Q C O M P? | R E F X | R E F Y | R E F Z | R M S D | V X | V Y | V Z | X | X C O M P? | Y | Y C O M P? | Z | Z C O M P?);

SPACE_VS:		[ \t\r\n]+ -> skip;

mode CTL_FOR_MODE; // control statement for

L_paren_CF:		'(';
R_paren_CF:		')' -> popMode;
In_CF:			I N;

Integer_CF:		'-'? DECIMAL;
Real_CF:		('+' | '-')? (DECIMAL | DEC_DOT_DEC) (E ('+' | '-')? DECIMAL)?;
Symbol_name_CF:		SYMBOL_NAME;
Simple_name_CF:		SIMPLE_NAME;

SPACE_CF:		[ \t\r\n]+ -> skip;
COMMENT_CF:		'{' (COMMENT_CF | .)*? '}' -> channel(HIDDEN);

mode LOOP_LABEL_MODE; // loop label

Simple_name_LL:		SIMPLE_NAME -> mode(DEFAULT_MODE);

SPACE_LL:		[ \t\r\n]+ -> skip;

