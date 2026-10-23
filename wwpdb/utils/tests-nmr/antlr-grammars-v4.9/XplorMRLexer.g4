/*
 XPLOR-NIH MR (Magnetic Restraint) lexer grammar for ANTLR v4.9
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

lexer grammar XplorMRLexer;

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

/* XPLOR-NIH: Distance restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node377.html
*/
Noe:			N O E;					// Noe { noe_statement } End

// noe_statement
Assign:			A S S I G? N?;				// selection selection Real Real Real [ Or_op selection selection ... ]
Asymptote:		A S Y M P? T? O? T? E?;			// Class_names Real
Average:		A V E R A? G? ((I? N? G?) | E?) -> pushMode(AVER_MODE);	// Class_names Noe_avr_methods
Bhig:			B H I G;				// Class_names Real
Ceiling:		C E I L I? N? G?;			// = Real
Classification:		C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
CountViol:		C O U N T? V? I? O? L?;			// Class_name
Distribute:		D I S T R? I? B? U? T? E?;		// Class_name Class_name Real
Monomers:		M O N O M? E? R? S?;			// Class_names Integer
Ncount:			N C O U N? T?;				// Class_names Integer
Nrestraints:		N R E S T? R? A? I? N? T? S?;		// = Integer
Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// Class_names Noe_potential
Predict:		P R E D I? C? T?;			// { predict_statement } End
Print:			P R I N T?;
Threshold:		T H R E S? H? O? L? D?;			// = Real
Reset:			R E S E T?;
Rswitch:		R S W I T? C? H?;			// Class_names Real
Scale:			S C A L E?;				// Class_names Real
SoExponent:		S O E X P? O? N? E? N? T?;		// Class_names Real
SqConstant:		S Q C O O? N? S? T? A? N? T?;		// Class_names Real
SqExponent:		S Q E X P? O? N? E? N? T?;		// Class_names Real
SqOffset:		S Q O F F? S? E? T?;			// Class_names Real
Temperature:		T E M P E? R? A? T? U? R? E?;		// = Real

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

/* XPLOR-NIH: Dihedral angle restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/cdih_syntax.html
*/
Restraints:		R E S T R? A? I? N? T? S?;		// Dihedral
Dihedral:		D I H E D? R? A? L?;			// Dihedral { dihedral_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection Real Real Real Integer
Nassign:		N A S S I? G? N?;			// = Integer
//Reset:		R E S E T?;
//Scale:		S C A L E?;				// Real
Print_any:		'?';

/* XPLOR-NIH: RDC - Syntax (SANI - Susceptibility anisotropy)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node418.html
*/
Sanisotropy:		S A N I S? O? T? R? O? P? Y?;		// Sanisotropy { sani_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection selection Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real Real Real
ForceConstant:		F O R C E? C? O? N? S? T? A? N? T?;	// Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
//Reset:		R E S E T?;

// RDC potential statement
//Rdc_potential:	S Q U A R? E? '-' W? E? L? L? | H A R M O? N? I? C?;

/* XPLOR-NIH: RDC - Syntax (XDIP)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node419.html
*/
Xdipolar:		X D I P O? L? A? R?;			// Xdipolar { xdip_statement } End
Dipolar:		D I P O L? A? R?;			// Dipolar { xdip_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection selection Real Real Real [ Real Real Real ]
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
Type:			T Y P E -> pushMode(TYPE_MODE);		// Rdc_dist_fix_types
//Scale:		S C A L E?;				// Real
Sign:			S I G N;				// Logical
//Average:		A V E R A? G? E? -> pushMode(AVER_MODE);	// Rdc_avr_methods
//Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real Real Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
//Reset:		R E S E T?;

// RDC distance fixing types
//Rdc_dist_fix_types:	F I X D | V A R D;
// RDC averaging methods
//Rdc_avr_methods:	S U M | S U M D I? F? | A V E R A? G? E?;

/* XPLOR-NIH: RDC - Syntax (VEAN)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node420.html
*/
VeAngle:		V E A N G? L? E?;			// VeAngle { vean_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection Real Real Real Real
Cv:			C V;					// = Integer
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
Partition:		P A R T I? T? I? O? N?;			// = Integer
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
//Reset:		R E S E T?;

/* XPLOR-NIH: RDC - Syntax (TENSO)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node421.html
*/
Tensor:			T E N S O R?;				// Tensor { tens_statement } End
//Assign:		A S S I G? N?;				// selection selection Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
//Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
//Reset:		R E S E T?;

/* XPLOR-NIH: RDC - Syntax (ANIS)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node422.html
*/
Anisotropy:		A N I S O? T? R? O? P? Y?;		// Anisotropy { anis_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
//Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real Real Real Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
//Reset:		R E S E T?;
//Type:			T Y P E -> pushMode(TYPE_MODE);		// Rdc_anis_types

// RDC anisotropy types
//Rdc_anis_types:	R E L A X | M I S C;

/* XPLOR-NIH: Planarity restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/plan_syntax.html
*/
//Restraints:		R E S T R? A? I? N? T? S?;		// Planar
Planar:			P L A N (A | E)? R?;			// Planer { planar_statement } End

// planar_statement
Group:			G R O U P?;				// Group { planar_group_statement } End
Initialize:		I N I T I? A? L? I? Z? E?;
//Print_any:		'?';

// group_statement
Selection:		S E L E C? T? I? O? N?;			// = selection
Weight:			W E I G H? T?;				// = Real

/* XPLOR-NIH: Harmonic coordiate restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node176.html
*/
//Restraints:		R E S T R? A? I? N? T? S?;		// Harmonic
Harmonic:		H A R M O? N? I? C?;			// Harmonic { harmonic_statement } End

// harmonic_stetement
Exponent:		E X P O N? E? N? T?;			// = Integer
Normal:			N O R M A? L?;				// = vector_3d

/* XPLOR-NIH: Antidiatance restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node398.html
*/
Xadc:			X A D C;				// Xadc { xadc_statement } End
//Assign:		A S S I G? N?;				// selection selection
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
Expectation:		E X P E C? T? A? T? I? O? N?;		// Integer Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real ( All | Class Class_name )
//Reset:		R E S E T?;
Size:			S I Z E;				// Real Integer
Zero:			Z E R O;

/* XPLOR-NIH: Scalar J-coupling restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node401.html
*/
Coupling:		C O U P L? I? N? G?;			// Coupling { coupling_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection [ selection selection selection selection ] Real Real [ Real Real ]
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
//Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real Real Real Real
//Cv:			C V;					// = Integer
Degeneracy:		D E G E N? E? R? A? C? Y?;		// Number_of_couplings
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real [ Real ]
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
//Partition:		P A R T I? T? I? O? N?;			// = Integer
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// Coupling_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real ( All | Class Class_name )
//Reset:		R E S E T?;

//Number_of_couplings:	'1' | '2';
//Coupling_potential:	Rdc_potential;

/* XPLOR-NIH: Carbon chemical shift restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node404.html
*/
Carbon:			C A R B O? N?;				// Carbon { carbon_shift_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
//Expectation:		E X P E C? T? A? T? I? O? N?;		// Integer Integer Real Real Real Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
PhiStep:		P H I S T? E? P?;			// Real
PsiStep:		P S I S T? E? P?;			// Real
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
Rcoil:			R C O I L?;				// selection Real Real
//Reset:		R E S E T?;
//Zero:			Z E R O;

/* XPLOR-NIH: Proton chemical shift restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node407.html
*/
Proton:			P R O T O N S? H? I? F? T? S?;	// Proton { proton_shift_statement } End
Observed:		O B S E R? V? E? D?;			// selection [ selection ] Real [ Real ]
//Rcoil:		R C O I L?;				// selection Real
//Anisotropy:		A N I S O? T? R? O? P? Y?;		// selection selection selection Co_or_Cn Logical? SC_or_BB
Amides:			A M I D E? S?;				// selection
//Carbons:		C A R B O? N? S?;			// selection
Nitrogens:		N I T R O? G? E? N? S?;			// selection
Oxygens:		O X Y G E? N? S?;			// selection
RingAtoms:		R I N G A? T? O? M? S?;			// Ring_resname selection selection selection selection selection [ selection ]
AlphasAndAmides:	A L P H A? S? A? N? D? A? M? I? D? E? S?;	// selection
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
Error:			E R R O R?;				// Real
//Degeneracy:		D E G E N? E? R? A? C? Y?;		// Number_of_shifts
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real [ Real ]
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// Coupling_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real ( All | Class Class_name ) Rmsd_or_Not
//Reset:		R E S E T?;

//CO_or_CN:		C O | C N;
//SC_or_BB:		S C | B B;
//Ring_resname:		P H E | T Y R | H I S | T R P ('5' | '6') | A D E ('5' | '6') | G U A ('5' | '6') | T H Y | C Y T | U R A;
//Rmsd_or_Not:		R M S D | N O R M S? D?;
//Number_of_shifts:	'1' | '2';

/* XPLOR-NIH: Dihedral angle database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node410.html
*/
Ramachandran:		R A M A;				// Rama { ramachandran_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection [ selection selection selection selection ] [ selection selection selection selection ] [ selection selection selection selection ]
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
//Cutoff:		C U T O F F;				// Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real
Gaussian:		G A U S S? I? A? N?;			// Real Real Real [ Real Real Real ] [ Real Real Real ] [ Real Real Real ]
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
Phase:			P H A S E?;				// Real Real Real [ Real Real Real ] (Real Real Real ] (Real Real Real ]
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real ( All | Class Class_name )
Quartic:		Q U A R T? I? C?;			// Real Real Real [ Real Real Real ] [ Real Real Real ] [ Real Real Real ]
//Reset:		R E S E T?;
//Scale:		S C A L E?;				// Real
Shape:			S H A P E? -> pushMode(SHAP_MODE);	// Gauss_or_Quart
//Size:			S I Z E;				// Dimensions Real [ Real ] [ Real ] [ Real ]
Sort:			S O R T;
//Zero:			Z E R O;

//Gauss_or_Quart:	G A U S S | Q U A R T;
Dimensions:		O N E D | T W O D | T H R E E D | F O U R D;

/* XPLOR-NIH: Radius of gyration restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node413.html
*/
Collapse:		C O L L A? P? S? E?;			// Collapse { collapse_statement } End
//Scale:		S C A L E?;				// Real
//Assign:		A S S I G? N?;				// selection Real Real
//Print:		P R I N T?;
//Reset:		R E S E T?;

/* XPLOR-NIH: Diffusion anisotropy restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node415.html
*/
Danisotropy:		D A N I S? O? T? R? O? P? Y?;		// Danisotropy { diffusion_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection selection Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
//Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real Real Real Real Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
//Reset:		R E S E T?;
//Type:			T Y P E -> pushMode(TYPE_MODE);		// Diff_anis_types

// Diffusion anisotropy types
//Diff_anis_types:	D I F F | M I S C;

/* XPLOR-NIH: Residue-residue position/orientation database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node425.html
*/
Orient:			O R I E N? T?;				// Orient { orientation_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
//Cutoff:		C U T O F F;				// Real
Height:			H E I G H? T?;				// Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real
//Gaussian:		G A U S S? I? A? N?;			// Real Real Real Real Real Real Real
MaxGaussians:		M A X G A? U? S? S? I? A? N? S?;	// Integer
NewGaussian:		N E W G A? U? S? S? I? A? N?;		// Real Real Real Real Real Real Real Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real ( All | Class Class_name )
//Quartic:		Q U A R T? I? C?;			// Real Real Real Real Real Real Real Real
//Reset:		R E S E T?;
//Residues:		R E S I D? U? E? S?;			// Integer
//Size:			S I Z E;				// Real Real
//Zero:			Z E R O;

/* XPLOR-NIH: Chemical shift anisotropy restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node427.html
*/
Dcsa:			D C S A;				// Dcsa { csa_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection selection selection Real Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
//Scale:		S C A L E?:				// Real
//Type:			T Y P E -> pushMode(TYPE_MODE);		// Csa_types
//Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real Real Real
Sigma:			S I G M A?;				// Real Real Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
//Reset:		R E S E T?;

// Chemical shift anisotropy types
//Csa_types:		P H O S | C A R B | N I T R;

/* XPLOR-NIH: Pseudo chemical shift anisotropy restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node430.html
*/
Pcsa:			P C S A;				// Pcsa { pcsa_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection selection selection Real Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
//Scale:		S C A L E?:				// Real
//Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real Real Real
//Sigma:		S I G M A?;				// Real Real Real Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
//Reset:		R E S E T?;

/* XPLOR-NIH: One-bond coupling restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node433.html
*/
OneBond:		O N E B O? N? D?;			// OneBond { one_bond_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection selection selection selection Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
//Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real Real Real Real Real Real Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
//Reset:		R E S E T?;

/* XPLOR-NIH: Angle database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node435.html
*/
AngleDb:		A N G L E? D? B?;			// AngleDb { bond_angle_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection selection selection selection selection selection selection [ selection ]
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
DerivFlag:		D E R I V? F? L? A? G?;			// On_or_Off
//Expectation:		E X P E C? T? A? T? I? O? N?;		// Integer Integer Real
//Error:		E R R O R?;				// Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// Rdc_potential
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real ( All | Class Class_name )
//Reset:		R E S E T?;
//Size:			S I Z E;				// Angle_or_Dihedral Integer Integer
//Zero:			Z E R O;

//On_or_Off:		O N | O F F;
//Angle_or_Dihedral:	A N G L E? | D I H E D? R? A? L?;

/* XPLOR-NIH: Paramagnetic relaxation enhancement restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node438.html
*/
PMagnetic:		P M A G N? E? T? I? C?;			// PMagnetic { pre_statement } End
//Assign:		A S S I G? N?;				// selection selection Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// = Class_name
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// = Class_name Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// = Integer
//Potential:		P O T E N? T? I? A? L? -> pushMode(POTE_MODE);	// = Class_name Rdc_potential
Kconst:			K C O N S? T?;				// = Class_name Real
Omega:			O M E G A?;				// = Class_name Real
Tauc:			T A U C;				// = Class_name Real Real
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real ( All | Class Class_name )
//Reset:		R E S E T?;
Debug:			D E B U G?;

/* XPLOR-NIH: Paramagnetic pseudocontact shift restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node442.html
*/
Xpcs:			X P C S;				// Xpcs { pcs_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
Tolerance:		T O L L;				// One_or_Zero
//Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real ( All | Class Class_name )
//Reset:		R E S E T?;
Save:			S A V E;				// Class_name
Fmed:			F M E D;				// Real Integer
ErrOn:			E R R O N;
ErrOff:			E R R O F F;
Fon:			F O N;
Foff:			F O F F;
Son:			S O N;
Soff:			S O F F;
Frun:			F R U N;				// Integer

//One_or_Zero:		'1' | '0';

/* XPLOR-NIH: Paramagnetic residual dipolar coupling restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node445.html
*/
Xrdcoupling:		X R D C O? U? P? L? I? N? G?;		// Xrdcoupling { xrdc_statement } End
//Assign:		A S S I G? N?;				// selection selection selection selection selection selection Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
//Tolerance:		T O L L;				// One_or_Zero
//Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
//ErrOn:		E R R O N;
//ErrOff:		E R R O F F;
//Fmed:			F M E D;
//Fon:			F O N;
//Foff:			F O F F;
//Frun:			F R U N:
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;
//Reset:		R E S E T?;
//Save:			S A V E;				// Class_name
//Son:			S O N;
//Soff:			S O F F;

/* XPLOR-NIH: Paramagnetic orientation restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node448.html
*/
Xangle:			X A N G L? E?;				// Xangle { xang_statement } End
//Assign:		A S S I G? N?;				// selection selection Real Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
//Reset:		R E S E T?;

/* XPLOR-NIH: Paramagnetic cross-correlation rate restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node450.html
*/
Xccr:			X C C R;				// Xccr { xccr_statement } End
//Assign:		A S S I G? N?;				// selection selection selection Real Real
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
Weip:			W E I P;				// One_or_Zero
//Coefficients:		C O E F F? I? C? I? E? N? T? S?;	// Real
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
//Reset:		R E S E T?;
//Frun:			F R U N:				// Integer

/* XPLOR-NIH: Hydrogen bond geometry restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node452.html
*/
Hbda:			H B D A;				// Hbda { hbda_statement } End
//Assign:		A S S I G? N?;				// selection selection selection
//Classification:	C L A S S? I? F? I? C? A? T? I? O? N?;	// Class_name
//ForceConstant:	F O R C E? C? O? N? S? T? A? N? T?;	// Real
//Nrestraints:		N R E S T? R? A? I? N? T? S?;		// Integer
//Print:		P R I N T?;
//Threshold:		T H R E S? H? O? L? D?;			// Real
//Reset:		R E S E T?;

/* XPLOR-NIH: Hydrogen bond database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node454.html
*/
Hbdb:			H B D B;				// Hbdb { hbdb_statement } End
//Assign:		A S S I G? N?;				// selection selection
Kdir:			K D I R;				// = Real
Klin:			K L I N;				// = Reala
Nseg:			N S E G;				// = Integer
Nmin:			N M I N;				// = Integer
Nmax:			N M A X;				// = Integer
Segm:			S E G M;				// = Segment_name
Ohcut:			O H C U T;				// = Real
Coh1cut:		C O H '1' C? U? T?;			// = Real
Coh2cut:		C O H '2' C? U? T?;			// = Real
Ohncut:			O H N C U? T?;				// = Real
Updfrq:			U P D F R Q;				// = Integer
Prnfrq:			P R N F R Q;				// = Integer
Freemode:		F R E E M O D E;			// = One_or_Zero
Donor:			D O N O? R?;
Acceptor:		A C C E? P? T? O? R?;

/* XPLOR-NIH: NCS restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/doc/current/xplor/node341.html
*/
Ncs:			N C S;
//Restraints:		R E S T R? A? I? N? T? S?;		// Ncs

//Group:		G R O U P?;				// Group { ncs_group_statement } End
//Initialize:		I N I T I? A? L? I? Z? E?;
//Print_any:		'?';

Equivalence:		E Q U I V? A? L? E? N? C? E?;		// = selection
Sigb:			S I G B;				// = Real
//Weight:		W E I G H? T?;				// = Real

/* XPLOR-NIH: Flags - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node125.html
*/
Flags:			F L A G S? -> pushMode(FLAG_MODE);	// Flags { flag_statement } End

/* Atom selection - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node39.html
*/
All:			A L L;
Around:			A R O U N? D?;				// Real (factor as subject)
Atom:			A T O M;				// Segment_names Residue_numbers Atom_names
Attribute:		A T T R I? B? U? T? E? -> pushMode(ATTR_MODE);	// Abs? Attr_property Comparison_ops Real
BondedTo:		B O N D E? D? T? O?;			// factor
ByGroup:		B Y G R O? U? P?;			// factor
ByRes:			B Y R E S?;				// factor
Chemical:		C H E M I? C? A? L?;			// Atom_types | Atom_type [ : Atom_type ]
Hydrogen:		H Y D R O? G? E? N?;
Id:			I D;					// Integer
Known:			K N O W N?;
Name:			N A M E;				// Atom_names | Atom_name [ : Atom_name ]
//Not_op:		N O T;					// factor
Point:			P O I N T?;				// vector_3d cut Real
Cut:			C U T;
Previous:		P R E V I? O? U? S?;
Pseudo:			P S E U D? O?;
Residue:		R E S I D? U? E?;			// Residue_numbers | Residue_number [ : Residue_number ]
Resname:		R E S N A? M? E?;			// Residue_names | Residue_name [ : Residue_name ]
Saround:		S A R O U? N? D?;			// Real (factor as subject)
SegIdentifier:		S E G I D? E? N? T? I? F? I? E? R?;	// Segment_names | Segment_name [ : Segment_name ]
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
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node42.html
*/
Vector:			V E C T O? R?;				// vector_mode vector_expression selection

Do_Lp:			D O ' '* L_paren -> pushMode(VECTOR_EXPR_MODE);
Identity_Lp:		I D E N T? I? T? Y? ' '* L_paren -> pushMode(VECTOR_EXPR_MODE);
Show:			S H O W -> pushMode(VECTOR_SHOW_MODE);		// Vector_show_property

/* XPLOR-NIH: Evaluate statement - Syntax_
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node36.html
*/
Evaluate_Lp:		E V A L U? A? T? E? ' '* L_paren -> pushMode(VECTOR_EXPR_MODE);
								// ( evaluate_statement )

/* XPLOR-NIH: Patching the Molecular Structure - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node86.html
*/
Patch:			P A T C H;				// ( patch_statement )
Reference:		R E F E R? E? N? C? E?;
Nil:			N I L;

/* XPLOR-NIH: Parameter statement - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node50.html
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

/* XPLOR-NIH: Control statement - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/doc/current/xplor/node24.html
*/
For:			F O R -> pushMode(CTL_FOR_MODE);	// Symbol_name In ( Words ) Loop Loop_label { statements } End Loop Loop_label
Loop:			L O O P -> pushMode(LOOP_LABEL_MODE);

/* Three-dimentional vectors - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node15.html
*/
Tail:			T A I L;
Head:			H E A D;

// Logical operations
Or_op:			O R;
And_op:			A N D;
Not_op:			N O T;

/* Numbers and Strings - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node14.html
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
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node19.html
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
Attr_properties:	(B | B C O M P? | C H A R G? E? | D X | D Y | D Z | F B E T A? | H A R M O? N? I? C? S? | M A S S | Q | Q C O M P? | R E F X | R E F Y | R E F Z | R M S D | V X | V Y | V Z | X | X C O M P? | Y | Y C O M P? | Z | Z C O M P? | S T O R E '1' | S T O R E '2' | S T O R E '3' | S T O R E '4' | S T O R E '5' | S T O R E '6' | S T O R E '7' | S T O R E '8' | S T O R E '9');
Comparison_ops:		(Equ_op | Lt_op | Gt_op | Leq_op | Geq_op | Neq_op) -> popMode;

SPACE_AP:		[ \t\r\n]+ -> skip;

mode AVER_MODE; // Inside of Average tag

Averaging_methods:	(R '-6' | R '-3' | S U M | C E N T E? R? | S U M D I? F? | A V E R A? G? E?) -> popMode;

Class_name_AM:		SIMPLE_NAME;

SPACE_AM:		[ \t\r\n]+ -> skip;

mode POTE_MODE; // Inside of Potential tag

Equ_op_PT:		'=';

Potential_types:	(B I H A R? M? O? N? I? C? | L O G N O? R? M? A? L? | S Q U A R? E? '-'? W? E? L? L? | S O F T '-'? S? Q? U? A? R? E? | S Y M M E? T? R? Y? | H I G H | '3' D P O | H A R M O? N? I? C?) -> popMode;

Class_name_PT:		SIMPLE_NAME;

SPACE_PT:		[ \t\r\n]+ -> skip;

mode TYPE_MODE; // Inside of Type tag

// RDC distance fixing types
Rdc_dist_fix_types:	(F I X D | V A R D) -> popMode;

// RDC/Diffusion anisotropy types
Rdc_or_Diff_anis_types:	(R E L A X | D I F F | M I S C) -> popMode;

// Chemical shift anisotropy types
Csa_types:		(P H O S | C A R B | N I T R) -> popMode;

SPACE_TY:		[ \t\r\n]+ -> skip;

mode SHAP_MODE; // Inside of Shape tag

Gauss_or_Quart:		(G A U S S | Q U A R T) -> popMode;

SPACE_SH:		[ \t\r\n]+ -> skip;

mode FLAG_MODE; // Inside of flag statement

Exclude:		E X C L U? D? E?;			// Class_name* | Any_class
Include:		I N C L U? D? E?;			// Class_name*

End_FL:			E N D -> popMode;

Class_name:		SIMPLE_NAME;
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

