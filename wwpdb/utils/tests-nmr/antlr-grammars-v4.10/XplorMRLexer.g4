/*
 XPLOR-NIH MR (Magnetic Restraint) lexer grammar for ANTLR v4.10 or later
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

options { caseInsensitive=true; }

Set:			'SET';
End:			'END';

/* XPLOR-NIH: Distance restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node377.html
*/
Noe:			'NOE';					// Noe { noe_statement } End

// noe_statement
Assign:			'ASSI' 'G'? 'N'?;			// selection selection Real Real Real [ Or_op selection selection ... ]
Asymptote:		'ASYM' 'P'? 'T'? 'O'? 'T'? 'E'?;	// Class_names Real
Average:		'AVER' 'A'? 'G'? (('I'? 'N'? 'G'?) | 'E'?) -> pushMode(AVER_MODE);	// Class_names Noe_avr_methods
Bhig:			'BHIG';					// Class_names Real
Ceiling:		'CEIL' 'I'? 'N'? 'G'?;			// = Real
Classification:		'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
CountViol:		'COUN' 'T'? 'V'? 'I'? 'O'? 'L'?;	// Class_name
Distribute:		'DIST' 'R'? 'I'? 'B'? 'U'? 'T'? 'E'?;	// Class_name Class_name Real
Monomers:		'MONO' 'M'? 'E'? 'R'? 'S'?;		// Class_names Integer
Ncount:			'NCOU' 'N'? 'T'?;			// Class_names Integer
Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// = Integer
Potential:		'POTE' 'N'? 'T'? 'I'? 'A'? 'L'? -> pushMode(POTE_MODE);		// Class_names Noe_potential
Predict:		'PRED' 'I'? 'C'? 'T'?;			// { predict_statement } End
Print:			'PRIN' 'T'?;
Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// = Real
Reset:			'RESE' 'T'?;
Rswitch:		'RSWI' 'T'? 'C'? 'H'?;			// Class_names Real
Scale:			'SCAL' 'E'?;				// Class_names Real
SoExponent:		'SOEX' 'P'? 'O'? 'N'? 'E'? 'N'? 'T'?;	// Class_names Real
SqConstant:		'SQCO' 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;			// Class_names Real
SqExponent:		'SQEX' 'P'? 'O'? 'N'? 'E'? 'N'? 'T'?;	// Class_names Real
SqOffset:		'SQOF' 'F'? 'S'? 'E'? 'T'?;		// Class_names Real
Temperature:		'TEMP' 'E'? 'R'? 'A'? 'T'? 'U'? 'R'? 'E'?;			// = Real

// NOE averaging methods
//Noe_avr_methods:	'R-6' | 'R-3' | 'SUM' | 'CENT' 'E'? 'R'?;

// NOE potential statement
//Noe_potential:	'BIHA' 'R'? 'M'? 'O'? 'N'? 'I'? 'C'? | 'LOGN' 'O'? 'R'? 'M'? 'A'? 'L'? | 'SQUA' 'R'? 'E'? '-'? 'W'? 'E'? 'L'? 'L'? | 'SOFT' '-'? 'S'? 'Q'? 'U'? 'A'? 'R'? 'E'? | 'SYMM' 'E'? 'T'? 'R'? 'Y'? | 'HIGH' | '3DPO';

// Predict statement
Cutoff:			'CUTOFF';				// = Real
Cuton:			'CUTON';				// = Real
From:			'FROM';					// = selection
To:			'TO';					// = selection

// 3rd party software extensions for NOE assign clause
Peak:			'PEAK';					// = Integer
Spectrum:		'SPECTRUM';				// = Integer
//Weight:		'WEIGHT';				// = Real
Volume:			'VOLUME';				// = Real
Vol:			'VOL';					// = Real
Ppm1:			'PPM1';					// = Real
Ppm2:			'PPM2';					// = Real
//Cv:			'CV';					// = Integer

/* XPLOR-NIH: Dihedral angle restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/cdih_syntax.html
*/
Restraints:		'REST' 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;	// Dihedral
Dihedral:		'DIHE' 'D'? 'R'? 'A'? 'L'?;		// Dihedral { dihedral_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection selection selection Real Real Real Integer
Nassign:		'NASS' 'I'? 'G'? 'N'?;			// = Integer
//Reset:		'RESE' 'T'?;
//Scale:		'SCAL' 'E'?;				// Real
Print_any:		'?';

/* XPLOR-NIH: RDC - Syntax (SANI - Susceptibility anisotropy)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node418.html
*/
Sanisotropy:		'SANI' 'S'? 'O'? 'T'? 'R'? 'O'? 'P'? 'Y'?;			 // Sanisotropy { sani_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection selection selection selection selection Real Real
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
Coefficients:		'COEF' 'F'? 'I'? 'C'? 'I'? 'E'? 'N'? 'T'? 'S'?;			// Real Real Real
ForceConstant:		'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
//Potential:		'POTE' 'N'? 'T'? 'I'? 'A'? 'L'? -> pushMode(POTE_MODE);		// Rdc_potential
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real
//Reset:		'RESE' 'T'?;

// RDC potential statement
//Rdc_potential:	'SQUA' 'R'? 'E'? '-'? 'W'? 'E'? 'L'? 'L'? | 'HARM' 'O'? 'N'? 'I'? 'C'?;

/* XPLOR-NIH: RDC - Syntax (XDIP)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node419.html
*/
Xdipolar:		'XDIP' 'O'? 'L'? 'A'? 'R'?;		// Xdipolar { xdip_statement } End
Dipolar:		'DIPO' 'L'? 'A'? 'R'?;			// Dipolar { xdip_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection selection selection selection selection Real Real Real [ Real Real Real ]
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
Type:			'TYPE' -> pushMode(TYPE_MODE);		// Rdc_dist_fix_types
//Scale:		'SCAL' 'E'?;				// Real
Sign:			'SIGN';					// Logical
//Average:		'AVER' 'A'? 'G'? 'E'? -> pushMode(AVER_MODE);			// Rdc_avr_methods
//Coefficients:		'COEF' 'F'? 'I'? 'C'? 'I'? 'E'? 'N'? 'T'? 'S'?;			// Real Real Real
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
//Potential:		'POTE' 'N'? 'T'? 'I'? 'A'? 'L'? -> pushMode(POTE_MODE);		// Rdc_potential
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real
//Reset:		'RESE' 'T'?;

// RDC distance fixing types
//Rdc_dist_fix_types:	'FIXD' | 'VARD';
// RDC averaging methods
//Rdc_avr_methods:	'SUM' | 'SUMD' 'I'? 'F'? | 'AVER' 'A'? 'G'? 'E'?;

/* XPLOR-NIH: RDC - Syntax (VEAN)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node420.html
*/
VeAngle:		'VEAN' 'G'? 'L'? 'E'?;			// VeAngle { vean_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection selection selection Real Real Real Real
Cv:			'CV';					// = Integer
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real Real
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
Partition:		'PART' 'I'? 'T'? 'I'? 'O'? 'N'?;	// = Integer
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real
//Reset:		'RESE' 'T'?;

/* XPLOR-NIH: RDC - Syntax (TENSO)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node421.html
*/
Tensor:			'TENSO' 'R'?;				// Tensor { tens_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection Real Real
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
//Coefficients:		'COEF' 'F'? 'I'? 'C'? 'I'? 'E'? 'N'? 'T'? 'S'?;			// Real
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
//Potential:		'POTE' 'N'? 'T'? 'I'? 'A'? 'L'? -> pushMode(POTE_MODE);		// Rdc_potential
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real
//Reset:		'RESE' 'T'?;

/* XPLOR-NIH: RDC - Syntax (ANIS)
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node422.html
*/
Anisotropy:		'ANIS' 'O'? 'T'? 'R'? 'O'? 'P'? 'Y'?;	// Anisotropy { anis_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection selection selection Real Real
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
//Coefficients:		'COEF' 'F'? 'I'? 'C'? 'I'? 'E'? 'N'? 'T'? 'S'?;			// Real Real Real Real
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real
//Nrestraints:		'NRES7 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
//Potential:		'POTE' 'N'? 'T'? 'I'? 'A'? 'L'? -> pushMode(POTE_MODE);		// Rdc_potential
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real
//Reset:		'RESE' 'T'?;
//Type:			'TYPE' -> pushMode(TYPE_MODE);		// Rdc_anis_types

// RDC anisotropy types
//Rdc_anis_types:	'RELAX' | 'MISC';

/* XPLOR-NIH: Planarity restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/plan_syntax.html
*/
//Restraints:		'REST' 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;	// Planar
Planar:			'PLAN' ('A' | 'E')? 'R'?;		// Planer { planar_statement } End

// planar_statement
Group:			'GROU' 'P'?;				// Group { planar_group_statement } End
Initialize:		'INIT' 'I'? 'A'? 'L'? 'I'? 'Z'? 'E'?;
//Print_any:		'?';

// group_statement
Selection:		'SELE' 'C'? 'T'? 'I'? 'O'? 'N'?;	// = selection
Weight:			'WEIG' 'H'? 'T'?;			// = Real

/* XPLOR-NIH: Harmonic coordiate restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node176.html
*/
//Restraints:		'REST' 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;	// Harmonic
Harmonic:		'HARM' 'O'? 'N'? 'I'? 'C'?;		// Harmonic { harmonic_statement } End

// harmonic_stetement
Exponent:		'EXPO' 'N'? 'E'? 'N'? 'T'?;		// = Integer
Normal:			'NORM' 'A'? 'L'?;			// = vector_3d

/* XPLOR-NIH: Antidiatance restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node398.html
*/
Xadc:			'XADC';					// Xadc { xadc_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
Expectation:		'EXPE' 'C'? 'T'? 'A'? 'T'? 'I'? 'O'? 'N'?;			// Integer Real
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real ( All | Class Class_name )
//Reset:		'RESE' 'T'?;
Size:			'SIZE';					// Real Integer
Zero:			'ZERO';

/* XPLOR-NIH: Scalar J-coupling restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node401.html
*/
Coupling:		'COUP' 'L'? 'I'? 'N'? 'G'?;		// Coupling { coupling_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection selection selection [ selection selection selection selection ] Real Real [ Real Real ]
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
//Coefficients:		'COEF' 'F'? 'I'? 'C'? 'I'? 'E'? 'N'? 'T'? 'S'?;			// Real Real Real Real
//Cv:			'CV';					// = Integer
Degeneracy:		'DEGE' 'N'? 'E'? 'R'? 'A'? 'C'? 'Y'?;	// Number_of_couplings
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real [ Real ]
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
//Partition:		'PART' 'I'? 'T'? 'I'? 'O'? 'N'?;	// = Integer
//Potential:		'POTE' 'N'? 'T'? 'I'? 'A'? 'L'? -> pushMode(POTE_MODE);		// Coupling_potential
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real ( All | Class Class_name )
//Reset:		'RESE' 'T'?;

//Number_of_couplings:	'1' | '2';
//Coupling_potential:	Rdc_potential;

/* XPLOR-NIH: Carbon chemical shift restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node404.html
*/
Carbon:			'CARB' 'O'? 'N'?;			// Carbon { carbon_shift_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection selection selection selection Real Real
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
//Expectation:		'EXPE' 'C'? 'T'? 'A'? 'T'? 'I'? 'O'? 'N'?;			// Integer Integer Real Real Real Real
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
PhiStep:		'PHIS' 'T'? 'E'? 'P'?;			// Real
PsiStep:		'PSIS' 'T'? 'E'? 'P'?;			// Real
//Potential:		'POTE' 'N'? 'T'? 'I'? 'A'? 'L'? -> pushMode(POTE_MODE);		// Rdc_potential
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real
Rcoil:			'RCOI' 'L'?;				// selection Real Real
//Reset:		'RESE' 'T'?;
//Zero:			'ZERO';

/* XPLOR-NIH: Proton chemical shift restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node407.html
*/
Proton:			'PROTON' 'S'? 'H'? 'I'? 'F'? 'T'? 'S'?;	// Proton { proton_shift_statement } End
Observed:		'OBSE' 'R'? 'V'? 'E'? 'D'?;		// selection [ selection ] Real [ Real ]
//Rcoil:		'RCOI' 'L'?;				// selection Real
//Anisotropy:		'ANIS' 'O'? 'T'? 'R'? 'O'? 'P'? 'Y'?;	// selection selection selection Co_or_Cn Logical? SC_or_BB
Amides:			'AMID' 'E'? 'S'?;			// selection
//Carbons:		'CARB' 'O'? 'N'? 'S'?;			// selection
Nitrogens:		'NITR' 'O'? 'G'? 'E'? 'N'? 'S'?;	// selection
Oxygens:		'OXYG' 'E'? 'N'? 'S'?;			// selection
RingAtoms:		'RING' 'A'? 'T'? 'O'? 'M'? 'S'?;	// Ring_resname selection selection selection selection selection [ selection ]
AlphasAndAmides:	'ALPH' 'A'? 'S'? 'A'? 'N'? 'D'? 'A'? 'M'? 'I'? 'D'? 'E'? 'S'?;	// selection
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
Error:			'ERRO' 'R'?;				// Real
//Degeneracy:		'DEGE' 'N'? 'E'? 'R'? 'A'? 'C'? 'Y'?;	// Number_of_shifts
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real [ Real ]
//Potential:		'POTE' 'N'? 'T'? 'I'? 'A'? 'L'? -> pushMode(POTE_MODE);		// Coupling_potential
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real ( All | Class Class_name ) Rmsd_or_Not
//Reset:		'RESE' 'T'?;

//CO_or_CN:		'CO' | 'CN';
//SC_or_BB:		'SC' | 'BB';
//Ring_resname:		'PHE' | 'TYR' | 'HIS' | 'TRP' ('5' | '6') | 'ADE' ('5' | '6') | 'GUA' ('5' | '6') | 'THY' | 'CYT' | 'URA';
//Rmsd_or_Not:		'RMSD' | 'NORM' 'S'? 'D'?;
//Number_of_shifts:	'1' | '2';

/* XPLOR-NIH: Dihedral angle database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node410.html
*/
Ramachandran:		'RAMA';					// Rama { ramachandran_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection selection selection [ selection selection selection selection ] [ selection selection selection selection ] [ selection selection selection selection ]
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
//Cutoff:		'CUTOFF';				// Real
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real
Gaussian:		'GAUS' 'S'? 'I'? 'A'? 'N'?;		// Real Real Real [ Real Real Real ] [ Real Real Real ] [ Real Real Real ]
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
Phase:			'PHAS' 'E'?;				// Real Real Real [ Real Real Real ] (Real Real Real ] (Real Real Real ]
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real ( All | Class Class_name )
Quartic:		'QUAR' 'T'? 'I'? 'C'?;			// Real Real Real [ Real Real Real ] [ Real Real Real ] [ Real Real Real ]
//Reset:		'RESE' 'T'?;
//Scale:		'SCAL' 'E'?;				// Real
Shape:			'SHAP' 'E'? -> pushMode(SHAP_MODE);	// Gauss_or_Quart
//Size:			'SIZE';					// Dimensions Real [ Real ] [ Real ] [ Real ]
Sort:			'SORT';
//Zero:			'ZERO';

//Gauss_or_Quart:	'GAUSS' | 'QUART';
Dimensions:		'ONED' | 'TWOD' | 'THREED' | 'FOURD';

/* XPLOR-NIH: Radius of gyration restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node413.html
*/
Collapse:		'COLL' 'A'? 'P'? 'S'? 'E'?;		// Collapse { collapse_statement } End
//Scale:		'SCAL' 'E'?;				// Real
//Assign:		'ASSI' 'G'? 'N'?;			// selection Real Real
//Print:		'PRIN' 'T'?;
//Reset:		'RESE' 'T'?;

/* XPLOR-NIH: Diffusion anisotropy restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node415.html
*/
Danisotropy:		'DANI' 'S'? 'O'? 'T'? 'R'? 'O'? 'P'? 'Y'?;			// Danisotropy { diffusion_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection selection selection selection selection Real Real
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
//Coefficients:		'COEF' 'F'? 'I'? 'C'? 'I'? 'E'? 'N'? 'T'? 'S'?;			// Real Real Real Real Real
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
//Potential:		'POTE' 'N'? 'T'? 'I'? 'A'? 'L'? -> pushMode(POTE_MODE);		// Rdc_potential
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real
//Reset:		'RESE' 'T'?;
//Type:			'TYPE' -> pushMode(TYPE_MODE);		// Diff_anis_types

// Diffusion anisotropy types
//Diff_anis_types:	D I F F | M I S C;

/* XPLOR-NIH: Residue-residue position/orientation database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node425.html
*/
Orient:			'ORIE' 'N'? 'T'?;			// Orient { orientation_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection selection selection
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
//Cutoff:		'CUTOFF';				// Real
Height:			'HEIG' 'H'? 'T'?;			// Real
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real
//Gaussian:		'GAUS' 'S'? 'I'? 'A'? 'N'?;		// Real Real Real Real Real Real Real
MaxGaussians:		'MAXG' 'A'? 'U'? 'S'? 'S'? 'I'? 'A'? 'N'? 'S'?;			// Integer
NewGaussian:		'NEWG' 'A'? 'U'? 'S'? 'S'? 'I'? 'A'? 'N'?;			// Real Real Real Real Real Real Real Real
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real ( All | Class Class_name )
//Quartic:		'QUAR' 'T'? 'I'? 'C'?;			// Real Real Real Real Real Real Real Real
//Reset:		'RESE' 'T'?;
//Residues:		'RESI' 'D'? 'U'? 'E'? 'S'?;		// Integer
//Size:			'SIZE';					// Real Real
//Zero:			'ZERO';

/* XPLOR-NIH: Chemical shift anisotropy restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node427.html
*/
Dcsa:			'DCSA';					// Dcsa { csa_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection selection selection selection selection selection Real Real Real
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
//Scale:		'SCAL' 'E'?:				// Real
//Type:			'TYPE' -> pushMode(TYPE_MODE);		// Csa_types
//Coefficients:		'COEF' 'F'? 'I'? 'C'? 'I'? 'E'? 'N'? 'T'? 'S'?;			// Real Real Real
Sigma:			'SIGM' 'A'?;				// Real Real Real
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
//Potential:		'POTE' 'N'? 'T'? 'I'? 'A'? 'L'? -> pushMode(POTE_MODE);		// Rdc_potential
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real
//Reset:		'RESE' 'T'?;

// Chemical shift anisotropy types
//Csa_types:		'PHOS' | 'CARB' | 'NITR';

/* XPLOR-NIH: Pseudo chemical shift anisotropy restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node430.html
*/
Pcsa:			'PCSA';					// Pcsa { pcsa_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection selection selection selection selection selection Real Real Real
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
//Scale:		'SCAL' 'E'?:				// Real
//Coefficients:		'COEF' 'F'? 'I'? 'C'? 'I'? 'E'? 'N'? 'T'? 'S'?;			// Real Real Real
//Sigma:		'SIGM' 'A'?;				// Real Real Real Real
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
//Potential:		'POTE' 'N'? 'T'? 'I'? 'A'? 'L'? -> pushMode(POTE_MODE);		// Rdc_potential
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real
//Reset:		'RESE' 'T'?;

/* XPLOR-NIH: One-bond coupling restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node433.html
*/
OneBond:		'ONEB' 'O'? 'N'? 'D'?;			// OneBond { one_bond_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection selection selection selection selection selection selection Real Real
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
//Coefficients:		'COEF' 'F'? 'I'? 'C'? 'I'? 'E'? 'N'? 'T'? 'S'?;			// Real Real Real Real Real Real Real
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
//Potential:		'POTE' 'N'? 'T'? 'I'? 'A'? 'L'? -> pushMode(POTE_MODE);		// Rdc_potential
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real
//Reset:		'RESE' 'T'?;

/* XPLOR-NIH: Angle database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node435.html
*/
AngleDb:		'ANGL' 'E'? 'D'? 'B'?;			// AngleDb { bond_angle_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection selection selection selection selection selection selection selection selection selection [ selection ]
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
DerivFlag:		'DERI' 'V'? 'F'? 'L'? 'A'? 'G'?;	// On_or_Off
//Expectation:		'EXPE' 'C'? 'T'? 'A'? 'T'? 'I'? 'O'? 'N'?;			// Integer Integer Real
//Error:		'ERRO' 'R'?;				// Real
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
//Potential:		'POTE' 'N'? 'T'? 'I'? 'A'? 'L'? -> pushMode(POTE_MODE);		// Rdc_potential
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real ( All | Class Class_name )
//Reset:		'RESE' 'T'?;
//Size:			'SIZE';					// Angle_or_Dihedral Integer Integer
//Zero:			'ZERO';

//On_or_Off:		'ON' | 'OFF';
//Angle_or_Dihedral:	'ANGL' 'E'? | 'DIHE' 'D'? 'R'? 'A'? 'L'?;

/* XPLOR-NIH: Paramagnetic relaxation enhancement restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node438.html
*/
PMagnetic:		'PMAG' 'N'? 'E'? 'T'? 'I'? 'C'?;	// PMagnetic { pre_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection Real Real
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// = Class_name
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// = Class_name Real
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// = Integer
//Potential:		'POTE' 'N'? 'T'? 'I'? 'A'? 'L'? -> pushMode(POTE_MODE);		// = Class_name Rdc_potential
Kconst:			'KCON' 'S'? 'T'?;			// = Class_name Real
Omega:			'OMEG' 'A'?;				// = Class_name Real
Tauc:			'TAUC';					// = Class_name Real Real
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real ( All | Class Class_name )
//Reset:		'RESE' 'T'?;
Debug:			'DEBU' 'G'?;

/* XPLOR-NIH: Paramagnetic pseudocontact shift restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node442.html
*/
Xpcs:			'XPCS';					// Xpcs { pcs_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection selection selection selection Real Real
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
Tolerance:		'TOLL';					// One_or_Zero
//Coefficients:		'COEF' 'F'? 'I'? 'C'? 'I'? 'E'? 'N'? 'T'? 'S'?;			// Real Real
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real ( All | Class Class_name )
//Reset:		'RESE' 'T'?;
Save:			'SAVE';					// Class_name
Fmed:			'FMED';					// Real Integer
ErrOn:			'ERRON';
ErrOff:			'ERROFF';
Fon:			'FON';
Foff:			'FOFF';
Son:			'SON';
Soff:			'SOFF';
Frun:			'FRUN';					// Integer

//One_or_Zero:		'1' | '0';

/* XPLOR-NIH: Paramagnetic residual dipolar coupling restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node445.html
*/
Xrdcoupling:		'XRDC' 'O'? 'U'? 'P'? 'L'? 'I'? 'N'? 'G'?;			// Xrdcoupling { xrdc_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection selection selection selection selection Real Real
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
//Tolerance:		'TOLL';					// One_or_Zero
//Coefficients:		'COEF' 'F'? 'I'? 'C'? 'I'? 'E'? 'N'? 'T'? 'S'?;			// Real Real
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
//ErrOn:		'ERRON';
//ErrOff:		'ERROFF';
//Fmed:			'FMED';
//Fon:			'FON';
//Foff:			'FOFF';
//Frun:			'FRUN':
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;
//Reset:		'RESE' 'T'?;
//Save:			'SAVE';					// Class_name
//Son:			'SON';
//Soff:			'SOFF';

/* XPLOR-NIH: Paramagnetic orientation restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node448.html
*/
Xangle:			'XANG' 'L'? 'E'?;			// Xangle { xang_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection Real Real Real
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real
//Reset:		'RESE' 'T'?;

/* XPLOR-NIH: Paramagnetic cross-correlation rate restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node450.html
*/
Xccr:			'XCCR';					// Xccr { xccr_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection selection Real Real
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
Weip:			'WEIP';					// One_or_Zero
//Coefficients:		'COEF' 'F'? 'I'? 'C'? 'I'? 'E'? 'N'? 'T'? 'S'?;			// Real
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real
//Reset:		'RESE' 'T'?;
//Frun:			'FRUN':					// Integer

/* XPLOR-NIH: Hydrogen bond geometry restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node452.html
*/
Hbda:			'HBDA';					// Hbda { hbda_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection selection
//Classification:	'CLAS' 'S'? 'I'? 'F'? 'I'? 'C'? 'A'? 'T'? 'I'? 'O'? 'N'?;	// Class_name
//ForceConstant:	'FORC' 'E'? 'C'? 'O'? 'N'? 'S'? 'T'? 'A'? 'N'? 'T'?;		// Real
//Nrestraints:		'NRES' 'T'? 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;			// Integer
//Print:		'PRIN' 'T'?;
//Threshold:		'THRE' 'S'? 'H'? 'O'? 'L'? 'D'?;	// Real
//Reset:		'RESE' 'T'?;

/* XPLOR-NIH: Hydrogen bond database restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node454.html
*/
Hbdb:			'HBDB';					// Hbdb { hbdb_statement } End
//Assign:		'ASSI' 'G'? 'N'?;			// selection selection
Kdir:			'KDIR';					// = Real
Klin:			'KLIN';					// = Reala
Nseg:			'NSEG';					// = Integer
Nmin:			'NMIN';					// = Integer
Nmax:			'NMAX';					// = Integer
Segm:			'SEGM';					// = Segment_name
Ohcut:			'OHCUT';				// = Real
Coh1cut:		'COH1' 'C'? 'U'? 'T'?;			// = Real
Coh2cut:		'COH2' 'C'? 'U'? 'T'?;			// = Real
Ohncut:			'OHNC' 'U'? 'T'?;			// = Real
Updfrq:			'UPDFRQ';				// = Integer
Prnfrq:			'PRNFRQ';				// = Integer
Freemode:		'FREEMODE';				// = One_or_Zero
Donor:			'DON' 'O'? 'R'?;
Acceptor:		'ACC' 'E'? 'P'? 'T'? 'O'? 'R'?;

/* XPLOR-NIH: NCS restraints - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/doc/current/xplor/node341.html
*/
Ncs:			'NCS';
//Restraints:		'REST' 'R'? 'A'? 'I'? 'N'? 'T'? 'S'?;	// Ncs

//Group:		'GROU' 'P'?;				// Group { ncs_group_statement } End
//Initialize:		'INIT' 'I'? 'A'? 'L'? 'I'? 'Z'? 'E'?;
//Print_any:		'?';

Equivalence:		'EQUI' 'V'? 'A'? 'L'? 'E'? 'N'? 'C'? 'E'?;
								// = selection
Sigb:			'SIGB';					// = Real
//Weight:		'WEIG' 'H'? 'T'?;			// = Real

/* XPLOR-NIH: Flags - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node125.html
*/
Flags:			'FLAG' 'S'? -> pushMode(FLAG_MODE);	// Flags { flag_statement } End

/* Atom selection - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node39.html
*/
All:			'ALL';
Around:			'AROU' 'N'? 'D'?;			// Real (factor as subject)
Atom:			'ATOM';					// Segment_names Residue_numbers Atom_names
Attribute:		'ATTR' 'I'? 'B'? 'U'? 'T'? 'E'? -> pushMode(ATTR_MODE);		// Abs? Attr_property Comparison_ops Real
BondedTo:		'BOND' 'E'? 'D'? 'T'? 'O'?;		// factor
ByGroup:		'BYGR' 'O'? 'U'? 'P'?;			// factor
ByRes:			'BYRE' 'S'?;				// factor
Chemical:		'CHEM' 'I'? 'C'? 'A'? 'L'?;		// Atom_types | Atom_type [ : Atom_type ]
Hydrogen:		'HYDR' 'O'? 'G'? 'E'? 'N'?;
Id:			'ID';					// Integer
Known:			'KNOW' 'N'?;
Name:			'NAME';					// Atom_names | Atom_name [ : Atom_name ]
//Not_op:		'NOT';					// factor
Point:			'POIN' 'T'?;				// vector_3d cut Real
Cut:			'CUT';
Previous:		'PREV' 'I'? 'O'? 'U'? 'S'?;
Pseudo:			'PSEU' 'D'? 'O'?;
Residue:		'RESI' 'D'? 'U'? 'E'?;			// Residue_numbers | Residue_number [ : Residue_number ]
Resname:		'RESN' 'A'? 'M'? 'E'?;			// Residue_names | Residue_name [ : Residue_name ]
Saround:		'SARO' 'U'? 'N'? 'D'?;			// Real (factor as subject)
SegIdentifier:		'SEGI' 'D'? 'E'? 'N'? 'T'? 'I'? 'F'? 'I'? 'E'? 'R'?;		// Segment_names | Segment_name [ : Segment_name ]
Store1:			'STORE1';
Store2:			'STORE2';
Store3:			'STORE3';
Store4:			'STORE4';
Store5:			'STORE5';
Store6:			'STORE6';
Store7:			'STORE7';
Store8:			'STORE8';
Store9:			'STORE9';
Tag:			'TAG';

/* Vector statement - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node42.html
*/
Vector:			'VECT' 'O'? 'R'?;			// vector_mode vector_expression selection

Do_Lp:			'DO' ' '* L_paren -> pushMode(VECTOR_EXPR_MODE);
Identity_Lp:		'IDEN' 'T'? 'I'? 'T'? 'Y'? ' '* L_paren -> pushMode(VECTOR_EXPR_MODE);
Show:			'SHOW' -> pushMode(VECTOR_SHOW_MODE);	// Vector_show_property

/* XPLOR-NIH: Evaluate statement - Syntax_
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node36.html
*/
Evaluate_Lp:		'EVAL' 'U'? 'A'? 'T'? 'E'? ' '* L_paren -> pushMode(VECTOR_EXPR_MODE);
								// ( evaluate_statement )

/* XPLOR-NIH: Patching the Molecular Structure - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node86.html
*/
Patch:			'PATC' 'H'?;				// ( patch_statement )
Reference:		'REFE' 'R'? 'E'? 'N'? 'C'? 'E'?;
Nil:			'NIL';

/* XPLOR-NIH: Parameter statement - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node50.html
*/
Parameter:		'PARA' 'M'? 'E'? 'T'? 'E'? 'R'?;	// ( parameter_statement )
UB:			'UB';
Mult:			'MULT';
HBonded:		'HBON' 'D'? 'E'? 'D'?;
Improper:		'IMPR' 'O'? 'P'? 'E'? 'R'?;
NBFix:			'NBFI' 'X'?;
NonB:			'NONB';
VDWOff:			'VDWO' 'F'? 'F'?;
Verbose:		'VERB' 'O'? 'S'? 'E'?;

/* XPLOR-NIH: Control statement - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/doc/current/xplor/node24.html
*/
For:			'FOR' -> pushMode(CTL_FOR_MODE);	// Symbol_name In ( Words ) Loop Loop_label { statements } End Loop Loop_label
Loop:			'LOOP' -> pushMode(LOOP_LABEL_MODE);

/* Three-dimentional vectors - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node15.html
*/
Tail:			'TAIL';
Head:			'HEAD';

// Logical operations
Or_op:			'OR';
And_op:			'AND';
Not_op:			'NOT';

/* Numbers and Strings - Syntax
 See also https://nmr.cit.nih.gov/xplor-nih/xplorMan/node14.html
*/
Comma:			',';
Complex:		L_paren Real Comma Real R_paren;
Integer:		'-'? DECIMAL;
Logical:		'TRUE' | 'FALSE' | 'ON' | 'OFF';
Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) ('E' ('+' | '-')? DECIMAL)?;
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

fragment ALPHA:		[A-Z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_';
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.' | '"' | '/';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
//fragment ATM_TYPE_CHAR:	ALPHA_NUM | '-' | '+';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;
fragment POST_WC_CHAR:	DEC_DIGIT | '\'' | 'P';
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
SECTION_COMMENT:	('#' | '!' | ';' | '\\' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | '>' '>'+ | 'REMARK' 'S'?) ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT:		('#' | '!' | ';' | '\\' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | '>' '>'+ | 'REMARK' 'S'?) ~[\r\n]* -> channel(HIDDEN);
SET_VARIABLE:		Set ([\r\n]*)? ~[\r\n]* ([\r\n]*)? End -> channel(HIDDEN);

mode ATTR_MODE; // Inside of Attribute tag

// Attribute properties
Abs:			'ABS';
Attr_properties:	('B' | 'BCOM' 'P'? | 'CHAR' 'G'? 'E'? | 'DX' | 'DY' | 'DZ' | 'FBET' 'A'? | 'HARM' 'O'? 'N'? 'I'? 'C'? 'S'? | 'MASS' | 'Q' | 'QCOM' 'P'? | 'REFX' | 'REFY' | 'REFZ' | 'RMSD' | 'VX' | 'VY' | 'VZ' | 'X' | 'XCOM' 'P'? | 'Y' | 'YCOM' 'P'? | 'Z' | 'ZCOM' 'P'? | 'STORE1' | 'STORE2' | 'STORE3' | 'STORE4' | 'STORE5' | 'STORE6' | 'STORE7' | 'STORE8' | 'STORE9');
Comparison_ops:		(Equ_op | Lt_op | Gt_op | Leq_op | Geq_op | Neq_op) -> popMode;

SPACE_AP:		[ \t\r\n]+ -> skip;

mode AVER_MODE; // Inside of Average tag

Averaging_methods:	('R-6' | 'R-3' | 'SUM' | 'CENT' 'E'? 'R'? | 'SUMD' 'I'? 'F'? | 'AVER' 'A'? 'G'? 'E'?) -> popMode;

Class_name_AM:		SIMPLE_NAME | '*';

SPACE_AM:		[ \t\r\n]+ -> skip;

mode POTE_MODE; // Inside of Potential tag

Equ_op_PT:		'=';

Potential_types:	('BIHA' 'R'? 'M'? 'O'? 'N'? 'I'? 'C'? | 'LOGN' 'O'? 'R'? 'M'? 'A'? 'L'? | 'SQUA' 'R'? 'E'? '-'? 'W'? 'E'? 'L'? 'L'? | 'SOFT' '-'? 'S'? 'Q'? 'U'? 'A'? 'R'? 'E'? | 'SYMM' 'E'? 'T'? 'R'? 'Y'? | 'HIGH' | '3DPO' | 'HARM' 'O'? 'N'? 'I'? 'C'?) -> popMode;

Class_name_PT:		SIMPLE_NAME | '*';

SPACE_PT:		[ \t\r\n]+ -> skip;

mode TYPE_MODE; // Inside of Type tag

// RDC distance fixing types
Rdc_dist_fix_types:	('FIXD' | 'VARD') -> popMode;

// RDC/Diffusion anisotropy types
Rdc_or_Diff_anis_types:	('RELAX' | 'DIFF' | 'MISC') -> popMode;

// Chemical shift anisotropy types
Csa_types:		('PHOS' | 'CARB' | 'NITR') -> popMode;

SPACE_TY:		[ \t\r\n]+ -> skip;

mode SHAP_MODE; // Inside of Shape tag

Gauss_or_Quart:		('GAUSS' | 'QUART') -> popMode;

SPACE_SH:		[ \t\r\n]+ -> skip;

mode FLAG_MODE; // Inside of flag statement

Exclude:		'EXCL' 'U'? 'D'? 'E'?;			// Class_name* | Any_class
Include:		'INCL' 'U'? 'D'? 'E'?;			// Class_name*

End_FL:			'END' -> popMode;

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
Real_VE:		(DECIMAL | DEC_DOT_DEC) ('E' ('+' | '-')? DECIMAL)?;

Atom_properties_VE:	('B' | 'BCOM' 'P'? | 'CHAR' 'G'? 'E'? | 'CHEM' 'I'? 'C'? 'A'? 'L'? | 'DX' | 'DY' | 'DZ' | 'FBET' 'A'? | 'HARM' 'O'? 'N'? 'I'? 'C'? 'S'? | 'MASS' | 'NAME' | 'Q' | 'QCOM' 'P'? | 'REFX' | 'REFY' | 'REFZ' | 'RESI' 'D'? 'U'? 'E'? | 'RESN' 'A'? 'M'? 'E'? | 'RMSD' | 'SEGI' 'D'? 'E'? 'N'? 'T'? 'I'? 'F'? 'I'? 'E'? 'R'? | 'STORE1' | 'STORE2' | 'STORE3' | 'STORE4' | 'STORE5' | 'STORE6' | 'STORE7' | 'STORE8' | 'STORE9' | 'PSEU' 'D'? 'O'? | 'VX' | 'VY' | 'VZ' | 'X' | 'XCOM' 'P'? | 'Y' | 'YCOM' 'P'? | 'Z' | 'ZCOM' 'P'?);

Abs_VE:			'ABS' -> pushMode(VECTOR_FUNC_MODE);
Acos_VE:		'ACOS' -> pushMode(VECTOR_FUNC_MODE);
Asin_VE:		'ASIN' -> pushMode(VECTOR_FUNC_MODE);
Cos_VE:			'COS' -> pushMode(VECTOR_FUNC_MODE);
Decode_VE:		'DECODE' -> pushMode(VECTOR_FUNC_MODE);
Encode_VE:		'ENCODE' -> pushMode(VECTOR_FUNC_MODE);
Exp_VE:			'EXP' -> pushMode(VECTOR_FUNC_MODE);
Gauss_VE:		'GAUSS' -> pushMode(VECTOR_FUNC_MODE);
Heavy_VE:		'HEAVY' -> pushMode(VECTOR_FUNC_MODE);
Int_VE:			'INT' -> pushMode(VECTOR_FUNC_MODE);
Log10_VE:		'LOG10' -> pushMode(VECTOR_FUNC_MODE);
Log_VE:			'LOG' -> pushMode(VECTOR_FUNC_MODE);
Max_VE:			'MAX' -> pushMode(VECTOR_FUNC_MODE);
Maxw_VE:		'MAXW' -> pushMode(VECTOR_FUNC_MODE);
Min_VE:			'MIN' -> pushMode(VECTOR_FUNC_MODE);
Mod_VE:			'MOD' -> pushMode(VECTOR_FUNC_MODE);
Norm_VE:		'NORM' -> pushMode(VECTOR_FUNC_MODE);
Random_VE:		'RAND' 'O'? 'M'? -> pushMode(VECTOR_FUNC_MODE);
Sign_VE:		'SIGN' -> pushMode(VECTOR_FUNC_MODE);
Sin_VE:			'SIN' -> pushMode(VECTOR_FUNC_MODE);
Sqrt_VE:		'SQRT' -> pushMode(VECTOR_FUNC_MODE);
Tan_VE:			'TAN' -> pushMode(VECTOR_FUNC_MODE);

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

Average_VS:		'AVE' 'R'? 'A'? 'G'? 'E'?;
Element_VS:		'ELEM' 'E'? 'N'? 'T'?;
Max_VS:			'MAX';
Min_VS:			'MIN';
Norm_VS:		'NORM';
Rms_VS:			'RMS';
Sum_VS:			'SUM';

Atom_properties_VS:	('B' | 'BCOM' 'P'? | 'CHAR' 'G'? 'E'? | 'DX' | 'DY' | 'DZ' | 'FBET' 'A'? | 'HARM' 'O'? 'N'? 'I'? 'C'? 'S'? | 'MASS' | 'Q' | 'QCOM' 'P'? | 'REFX' | 'REFY' | 'REFZ' | 'RMSD' | 'VX' | 'VY' | 'VZ' | 'X' | 'XCOM' 'P'? | 'Y' | 'YCOM' 'P'? | 'Z' | 'ZCOM' 'P'?);

SPACE_VS:		[ \t\r\n]+ -> skip;

mode CTL_FOR_MODE; // control statement for

L_paren_CF:		'(';
R_paren_CF:		')' -> popMode;
In_CF:			'IN';

Integer_CF:		'-'? DECIMAL;
Real_CF:		('+' | '-')? (DECIMAL | DEC_DOT_DEC) ('E' ('+' | '-')? DECIMAL)?;
Symbol_name_CF:		SYMBOL_NAME;
Simple_name_CF:		SIMPLE_NAME;

SPACE_CF:		[ \t\r\n]+ -> skip;
COMMENT_CF:		'{' (COMMENT_CF | .)*? '}' -> channel(HIDDEN);

mode LOOP_LABEL_MODE; // loop label

Simple_name_LL:		SIMPLE_NAME -> mode(DEFAULT_MODE);

SPACE_LL:		[ \t\r\n]+ -> skip;

