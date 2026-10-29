/*
 AMBER MR (Magnetic Restraint) lexer grammar for ANTLR v4.10 or later
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

lexer grammar AmberMRLexer;

options { caseInsensitive=true; }

END:			('&END' | '/') -> mode(DEFAULT_MODE);

/* Amber: NMR restraints - 29.1 Distance, angle and torsional restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
RST:			'&RST';

IAT:			'IAT'
			-> pushMode(INT_ARRAY_MODE);		// = Integer [ , Integer ]*
RSTWT:			'RSTWT'
			-> pushMode(REAL_ARRAY_MODE);		// = Real [ , Real ] [ , Real ] [ , Real ]
RESTRAINT:		'RESTRAINT';				// = " RestraintFunctionCall " [ , " RestraintFunctionCall " ]*

fragment ATNAM_:	'ATNAM';
ATNAM_Lp:		ATNAM_ ' '* L_paren
			-> pushMode(AQSTR_PARAM_MODE);		// = Quoted_atom_name
ATNAM:			ATNAM_
			-> pushMode(QSTR_ARRAY_MODE);		// = Quoted_atom_name [ , Quoted_atom_name ]*

IRESID:			'IRESID'
			-> pushMode(BINT_PARAM_MODE);		// = Boolint
NSTEP1:			'NSTEP1'
			-> pushMode(INT_PARAM_MODE);		// = Integer
NSTEP2:			'NSTEP2'
			-> pushMode(INT_PARAM_MODE);		// = Integer
IRSTYP:			'IRSTYP'
			-> pushMode(BINT_PARAM_MODE);		// = Boolint
IALTD:			'IALTD'
			-> pushMode(BINT_PARAM_MODE);		// = Boolint
IFVARI:			'IFVARI'
			-> pushMode(INT_PARAM_MODE);		// = Integer
NINC:			'NINC'
			-> pushMode(INT_PARAM_MODE);		// = Integer
IMULT:			'IMULT'
			-> pushMode(BINT_PARAM_MODE);		// = Boolint

R1:			'R1'
			-> pushMode(REAL_PARAM_MODE);		// = Real
R2:			'R2'
			-> pushMode(REAL_PARAM_MODE);		// = Real
R3:			'R3'
			-> pushMode(REAL_PARAM_MODE);		// = Real
R4:			'R4'
			-> pushMode(REAL_PARAM_MODE);		// = Real

RK2:			'RK2'
			-> pushMode(REAL_PARAM_MODE);		// = Real
RK3:			'RK3'
			-> pushMode(REAL_PARAM_MODE);		// = Real

R1A:			'R1A'
			-> pushMode(REAL_PARAM_MODE);		// = Real
R2A:			'R2A'
			-> pushMode(REAL_PARAM_MODE);		// = Real
R3A:			'R3A'
			-> pushMode(REAL_PARAM_MODE);		// = Real
R4A:			'R4A'
			-> pushMode(REAL_PARAM_MODE);		// = Real

RK2A:			'RK2A'
			-> pushMode(REAL_PARAM_MODE);		// = Real
RK3A:			'RK3A'
			-> pushMode(REAL_PARAM_MODE);		// = Real

R0:			'R0'
			-> pushMode(REAL_PARAM_MODE);		// = Real
K0:			'K0'
			-> pushMode(REAL_PARAM_MODE);		// = Real
R0A:			'R0A'
			-> pushMode(REAL_PARAM_MODE);		// = Real
K0A:			'K0A'
			-> pushMode(REAL_PARAM_MODE);		// = Real

RJCOEF:			'RJCOEF'
			->pushMode(REAL_ARRAY_MODE);		// = Real, Real, Real

fragment IGR_:		'IGR';					// = Integer [ , Integer ]*
IGR1:			IGR_ '1' -> pushMode(INT_ARRAY_MODE);
IGR2:			IGR_ '2' -> pushMode(INT_ARRAY_MODE);
IGR3:			IGR_ '3' -> pushMode(INT_ARRAY_MODE);
IGR4:			IGR_ '4' -> pushMode(INT_ARRAY_MODE);
IGR5:			IGR_ '5' -> pushMode(INT_ARRAY_MODE);
IGR6:			IGR_ '6' -> pushMode(INT_ARRAY_MODE);
IGR7:			IGR_ '7' -> pushMode(INT_ARRAY_MODE);
IGR8:			IGR_ '8' -> pushMode(INT_ARRAY_MODE);

FXYZ:			'FXYZ'
			-> pushMode(BINT_ARRAY_MODE);		// = Boolint, Boolint, Boolint
OUTXYZ:			'OUTXYZ'
			-> pushMode(BINT_PARAM_MODE);		// = Boolint

fragment GRNAM_:	'GRNAM';
GRNAM1_Lp:		GRNAM_ '1' ' '* L_paren
			-> pushMode(AQSTR_PARAM_MODE);		// = Quoted_atom_name
GRNAM2_Lp:		GRNAM_ '2' ' '* L_paren
			-> pushMode(AQSTR_PARAM_MODE);
GRNAM3_Lp:		GRNAM_ '3' ' '* L_paren
			-> pushMode(AQSTR_PARAM_MODE);
GRNAM4_Lp:		GRNAM_ '4' ' '* L_paren
			-> pushMode(AQSTR_PARAM_MODE);
GRNAM5_Lp:		GRNAM_ '5' ' '* L_paren
			-> pushMode(AQSTR_PARAM_MODE);
GRNAM6_Lp:		GRNAM_ '6' ' '* L_paren
			-> pushMode(AQSTR_PARAM_MODE);
GRNAM7_Lp:		GRNAM_ '7' ' '* L_paren
			-> pushMode(AQSTR_PARAM_MODE);
GRNAM8_Lp:		GRNAM_ '8' ' '* L_paren
			-> pushMode(AQSTR_PARAM_MODE);

GRNAM1:			GRNAM_ '1'
			-> pushMode(QSTR_ARRAY_MODE);		// = Quoted_atom_name [ , Quoted_atom_name ]*
GRNAM2:			GRNAM_ '2'
			-> pushMode(QSTR_ARRAY_MODE);
GRNAM3:			GRNAM_ '3'
			-> pushMode(QSTR_ARRAY_MODE);
GRNAM4:			GRNAM_ '4'
			-> pushMode(QSTR_ARRAY_MODE);
GRNAM5:			GRNAM_ '5'
			-> pushMode(QSTR_ARRAY_MODE);
GRNAM6:			GRNAM_ '6'
			-> pushMode(QSTR_ARRAY_MODE);
GRNAM7:			GRNAM_ '7'
			-> pushMode(QSTR_ARRAY_MODE);
GRNAM8:			GRNAM_ '8'
			-> pushMode(QSTR_ARRAY_MODE);

IR6:			'IR6'
			-> pushMode(BINT_PARAM_MODE);		// = Boolint
IFNTYP:			'IFNTYP'
			-> pushMode(BINT_PARAM_MODE);		// = Boolint

IXPK:			'IXPK'
			-> pushMode(INT_PARAM_MODE);		// = Integer
NXPK:			'NXPK'
			-> pushMode(INT_PARAM_MODE);		// = Integer

ICONSTR:		'ICONSTR'
			-> pushMode(INT_PARAM_MODE);		// = Integer

/* Amber: NMR restraints - 29.2. NOESY volume restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
NOEEXP:			'&NOEEXP';

NPEAK:			'NPEAK'
			-> pushMode(INT_ARRAY_MODE);		// = IntArray
EMIX:			'EMIX'
			-> pushMode(REAL_ARRAY_MODE);		// = Real [ , Real ]*

IHP:			'IHP'
			-> pushMode(INT_PARAM_MODE);		// ihp(Integer, Integer) = IntArray
JHP:			'JHP'
			-> pushMode(INT_PARAM_MODE);		// jhp(Integer, Integer) = IntArray

AEXP:			'AEXP'
			-> pushMode(REAL_PARAM_MODE);		// aexp(Integer, Integer) = RealArray
ARANGE:			'ARANGE'
			-> pushMode(REAL_PARAM_MODE);		// arange(Integer, Integer) = RealArray
AWT:			'AWT'
			-> pushMode(REAL_PARAM_MODE);		// awt(Integer, Integer) = RealArray

INVWT1:			'INVWT1'
			-> pushMode(REAL_PARAM_MODE);		// = Real
INVWT2:			'INVWT2'
			-> pushMode(REAL_PARAM_MODE);		// = Real

OMEGA:			'OMEGA'
			-> pushMode(REAL_PARAM_MODE);		// = Real
TAUROT:			'TAUROT'
			-> pushMode(REAL_PARAM_MODE);		// = Real
TAUMET:			'TAUMET'
			-> pushMode(REAL_PARAM_MODE);		// = Real
ID2O:			'ID2O'
			-> pushMode(BINT_PARAM_MODE);		// = Boolint
OSCALE:			'OSCALE'
			-> pushMode(REAL_PARAM_MODE);		// = Real

/* Amber: NMR restraints - 29.3. Chemical shift restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
SHF:			'&SHF';

NRING:			'NRING'
			-> pushMode(INT_PARAM_MODE);		// = Integer
NATR:			'NATR'
			-> pushMode(INT_PARAM_MODE);		// natr(Integer) = Integer [ , Integer ]*
IATR:			'IATR'
			-> pushMode(INT_PARAM_MODE);		// iatr(Integer) = Integer
NAMR:			'NAMR'
			-> pushMode(QSTR_PARAM_MODE);		// namr(Integer) = Quoted_atom_name
STR:			'STR'
			-> pushMode(REAL_ARRAY_MODE);		// str(Integer) = Real [ , Real ]*
IPROT:			'IPROT'
			-> pushMode(INT_PARAM_MODE);		// iprot(Integer) = Integer [ , Integer ]*
OBS:			'OBS'
			-> pushMode(REAL_PARAM_MODE);		// obs(Integer) = Real [ , Real ]*
SHRANG:			'SHRANG'
			-> pushMode(REAL_ARRAY_MODE);		// shrang(Integer) = Real [ , Real ]*
WT:			'WT'
			-> pushMode(REAL_ARRAY_MODE);		// wt(Integer) = Real [ , Real ]*

NPROT:			'NPROT'
			-> pushMode(INT_PARAM_MODE);		// = Integer
SHCUT:			'SHCUT'
			-> pushMode(REAL_PARAM_MODE);		// = Real
NTER:			'NTER'
			-> pushMode(INT_PARAM_MODE);		// = Integer
CTER:			'CTER'
			-> pushMode(INT_PARAM_MODE);		// = Integer

/* Amber: NMR restraints - 29.4. Psuedocontact shift restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
PCSHF:			'&PCSHF';

//NPROT:		'NPROT';				// = Integer
NME:			'NME'
			-> pushMode(INT_PARAM_MODE);		// = Integer
NMPMC:			'NMPMC'
			-> pushMode(QSTR_PARAM_MODE);		// = Quoted_atom_name

OPTPHI:			'OPTPHI'
			-> pushMode(REAL_PARAM_MODE);		// optphi(Integer) = Real [ , Real ]*
OPTTET:			'OPTTET'
			-> pushMode(REAL_PARAM_MODE);		// opttet(Integer) = Real [ , Real ]*
OPTOMG:			'OPTOMG'
			-> pushMode(REAL_PARAM_MODE);		// optomg(Integer) = Real [ , Real ]*
OPTA1:			'OPTA1'
			-> pushMode(REAL_PARAM_MODE);		// opta1(Integer) = Real [ , Real ]*
OPTA2:			'OPTA2'
			-> pushMode(REAL_PARAM_MODE);		// opta2(Integer) = Real [ , Real ]*
OPTKON:			'OPTKON'
			-> pushMode(REAL_PARAM_MODE);		// = Real

//fragment IPROT:	'IPROT';				// iprot(Integer) = Integer
//fragment OBS:		'OBS';					// = Real
//fragment WT:		'WT';					// = RealArray

TOLPRO:			'TOLPRO'
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray
MLTPRO:			'MLTPRO'
			-> pushMode(INT_PARAM_MODE);		// mltpro(Integer) = IntArray

/* Amber: NMR restraints - 29.5. Direct dipolar coupling restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
ALIGN:			'&ALIGN';

NDIP:			'NDIP'
			-> pushMode(INT_PARAM_MODE);		// = Integer

ID:			'ID'
			-> pushMode(INT_PARAM_MODE);		// id(Integer) = Integer [ , Integer ]*
JD:			'JD'
			-> pushMode(INT_PARAM_MODE);		// jd(Integer) = Integer [ , Integer ]*

DOBSL:			'DOBSL'
			-> pushMode(REAL_PARAM_MODE);		// = Real [ , Real ]*
DOBSU:			'DOBSU'
			-> pushMode(REAL_PARAM_MODE);		// = Real [ , Real ]*
// note that 'dobs' is unauthorized item
DOBS:			'DOBS'
			-> pushMode(REAL_PARAM_MODE);		// = Real [ , Real ]*

DWT:			'DWT'
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray

DATASET:		'DATASET'
			-> pushMode(INT_PARAM_MODE);		// = Integer
								// dataset(Integer) = Integer
NUM_DATASETS:		'NUM_DATASETS'
			-> pushMode(INT_PARAM_MODE);		// = Integer

S11:			'S11'
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray
S12:			'S12'
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray
S13:			'S13'
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray
S22:			'S22'
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray
S23:			'S23'
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray

GIGJ:			'GIGJ'
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray
DIJ:			'DIJ'
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray
DCUT:			'DCUT'
			-> pushMode(REAL_PARAM_MODE);		// = Real
FJ:			'FJ'
			-> pushMode(REAL_PARAM_MODE);		// = Real
DFAC_AL:		'DFAC_AL'
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray

FREEZEMOL:		'FREEZEMOL';				// = Logical

/* Amber: NMR restraints - 29.6. Residual CSA or pseudo-CSA restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
CSA:			'&CSA';

NCSA:			'NCSA'
			-> pushMode(INT_PARAM_MODE);		// = Integer

ICSA:			'ICSA'
			-> pushMode(INT_PARAM_MODE);		// = icsa(Integer) = Integer [ , Integer ]*
JCSA:			'JCSA'
			-> pushMode(INT_PARAM_MODE);		// = jcsa(Integer) = Integer [ , Integer ]*
KCSA:			'KCSA'
			-> pushMode(INT_PARAM_MODE);		// = kcsa(Integer) = Integer [ , Integer ]*

COBSL:			'COBSL'
			-> pushMode(REAL_PARAM_MODE);		// = Real [ , Real ]*
COBSU:			'COBSU'
			-> pushMode(REAL_PARAM_MODE);		// = Real [ , Real ]*
// note that 'cobs' is unauthorized item
COBS:			'COBS'
			-> pushMode(REAL_PARAM_MODE);		// = Real [ , Real ]*

CWT:			'CWT'
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray

DATASETC:		'DATASETC'
			-> pushMode(INT_PARAM_MODE);		// = Integer

FIELD:			'FIELD'
			-> pushMode(REAL_PARAM_MODE);		// = Real

SIGMA11:		'SIGMA11'
			-> pushMode(REAL_PARAM_MODE);		// = Real
SIGMA12:		'SIGMA12'
			-> pushMode(REAL_PARAM_MODE);		// = Real
SIGMA13:		'SIGMA13'
			-> pushMode(REAL_PARAM_MODE);		// = Real
SIGMA22:		'SIGMA22'
			-> pushMode(REAL_PARAM_MODE);		// = Real
SIGMA23:		'SIGMA23'
			-> pushMode(REAL_PARAM_MODE);		// = Real

CCUT:			'CCUT'
			-> pushMode(REAL_PARAM_MODE);		// = Real

Comma:			',' -> mode(DEFAULT_MODE);
//Ampersand:		'&';

/* AMBER atom nomenclature mapping generated by makeDIST_RST */
Residue:		'RESIDUE';
Mapping:		'MAPPING' -> pushMode(MAP_MODE);
Ambig:			'AMBIG' -> pushMode(MAP_MODE);

SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

COMMENT:		('#' | '!')+ -> mode(COMMENT_MODE);

fragment INTEGER:	('+' | '-')? DECIMAL;
fragment REAL:		('+' | '-')? (DECIMAL | DEC_DOT_DEC) ('E' ('+' | '-')? DECIMAL)?;
Logical:		'.'? 'TRUE' '.'? | '.'? 'FALSE' '.'?;
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL?) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;
fragment ONE_OR_ZERO:	'0' | '1';

fragment ALPHA:		[A-Z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_';
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.';
fragment QEXT_CHAR:	ALPHA_NUM | '\'' | '"' | ' ';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;
fragment ALPHA_EX_R:	[A-QS-Z];
fragment START_CHAR_EX_R:	ALPHA_EX_R | DEC_DIGIT | '_';
fragment SIMPLE_NAME_EX_R:	START_CHAR_EX_R NAME_CHAR*;
fragment QSTRING:	SIMPLE_NAME_EX_R | '\'' SIMPLE_NAME QEXT_CHAR* '\'' | '"' SIMPLE_NAME QEXT_CHAR* '"';

L_paren:		'(';
R_paren:		')';
L_brace:		'{';
R_brace:		'}';
L_brakt:		'[';
R_brakt:		']';
Equ_op:			'=';

L_quot:			'"' -> pushMode(FUNC_CALL_MODE);

Simple_name:		SIMPLE_NAME;

SPACE:			[ \t\r\n]+ -> skip;
SECTION_COMMENT:	('#' | '!' | ';' | '\\' | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+) ' '* [\r\n]+ -> channel(HIDDEN);

mode COMMENT_MODE;

Any_name:		~[ \t\r\n]+;

SPACE_CM:		[ \t]+ -> skip;
RETURN_CM:		[\r\n]+ -> mode(DEFAULT_MODE);

mode INT_PARAM_MODE;

Equ_op_IP:		'=';
L_paren_IP:		'(' -> pushMode(ARGUMENT_MODE);

Integer:		INTEGER -> popMode;

SPACE_IP:		[ \t\r\n]+ -> skip;

mode REAL_PARAM_MODE;

Equ_op_RP:		'=';
L_paren_RP:		'(' -> pushMode(ARGUMENT_MODE);


Real:			REAL -> popMode;

SPACE_RP:		[ \t\r\n]+ -> skip;

mode BINT_PARAM_MODE;

Equ_op_BP:		'=';

BoolInt:		ONE_OR_ZERO -> popMode;	// IRESID = 0 for the IAT points to the atoms, IRESID = 1 for the the IAT points to the residues
						// IRSTYP = 0 for target values are used directly, IRSTYP = 1 for target values are relatively displacement from the initial coordinates
						// IALTD = 0 for the penalty energy continues to rise in case of large distance violations, IALTD = 1 for the penalty energy is flattened out in that case
						// IMULT = 0 for R2A->RK2A, R3A->RK3A change linearly, IMULT = 1 for R2A->RK2A, R3A->RK3A change multicatively
						// IR6 = 0 for center-of-mass averaging, IR6 = 1 for <r^-6>^(-1/6) averaging of all interactions
						// IFNTYP = 0 for no time-averaged restraints, IFNTYP = 1 for enabling time-averaged restraints

SPACE_BP:		[ \t\r\n]+ -> skip;

mode QSTR_PARAM_MODE;

L_paren_QP:		'(' -> pushMode(ARGUMENT_MODE);
Equ_op_QP:		SPACE_QP '=' SPACE_QP;

Qstring:		(SPACE_QP QSTRING SPACE_QP) -> popMode;

fragment SPACE_QP:	[ \t\r\n]*;

mode AQSTR_PARAM_MODE;

Decimal_AP:		DECIMAL;

R_paren_AP:		')';
Equ_op_AP:		'=' -> pushMode(AQSTR_PARAM_MODE_);

SPACE_AP:		[ \t\r\n]+ -> skip;

mode AQSTR_PARAM_MODE_;

Qstring_AP:		(SPACE_AP_ QSTRING SPACE_AP_) -> mode(DEFAULT_MODE);

fragment SPACE_AP_:	[ \t\r\n]*;

mode INT_ARRAY_MODE;

L_paren_IA:		'(' -> pushMode(ARGUMENT_MODE);
Equ_op_IA:		SPACE_IA '=' SPACE_IA;
Comma_IA:		',' -> popMode;
End_IA:			'/' -> popMode;
Asterisk_IA:		SPACE_IA '*' SPACE_IA;

Integers:		SPACE_IA INTEGER SPACE_IA (Comma_IA SPACE_IA INTEGER SPACE_IA)* SPACE_IA;
MultiplicativeInt:	SPACE_IA INTEGER Asterisk_IA INTEGER SPACE_IA (Comma_IA SPACE_IA INTEGER Asterisk_IA INTEGER SPACE_IA)* SPACE_IA;

fragment SPACE_IA:	[ \t\r\n]*;

COMMENT_IA:		('#' | '!') -> popMode;

mode REAL_ARRAY_MODE;

L_paren_RA:		'(' -> pushMode(ARGUMENT_MODE);
Equ_op_RA:		SPACE_RA '=' SPACE_RA;
Comma_RA:		(',' | RETURN_RA) -> popMode;
End_RA:			'/' -> popMode;
Asterisk_RA:		SPACE_RA '*' SPACE_RA;

Reals:			SPACE_RA REAL SPACE_RA (Comma_RA SPACE_RA REAL SPACE_RA)* SPACE_RA;
MultiplicativeReal:	SPACE_RA INTEGER Asterisk_RA REAL SPACE_RA (Comma_RA SPACE_RA INTEGER Asterisk_RA REAL SPACE_RA)* SPACE_RA;

fragment RETURN_RA:	[\r\n]+;
fragment SPACE_RA:	[ \t]*;

COMMENT_RA:		('#' | '!') -> popMode;

mode BINT_ARRAY_MODE;

Equ_op_BA:		SPACE_BA '=' SPACE_BA;
Comma_BA:		',' -> popMode;
End_BA:			'/' -> popMode;

BoolInts:		SPACE_BA ONE_OR_ZERO SPACE_BA (Comma_BA SPACE_BA ONE_OR_ZERO SPACE_BA)* SPACE_BA;

fragment SPACE_BA:	[ \t\r\n]*;

COMMENT_BA:		('#' | '!') -> popMode;

mode QSTR_ARRAY_MODE;

L_paren_QA:		'(' -> pushMode(ARGUMENT_MODE);
Equ_op_QA:		SPACE_QA '=' SPACE_QA;
Comma_QA:		',' -> popMode;
End_QA:			'/' -> popMode;

Qstrings:		SPACE_QA QSTRING SPACE_QA (Comma_QA SPACE_QA QSTRING SPACE_QA)* SPACE_QA;

fragment SPACE_QA:	[ \t\r\n]*;

COMMENT_QA:		('#' | '!') -> popMode;

mode ARGUMENT_MODE;

Comma_AR:		',';
R_paren_AR:		')' -> popMode;

Decimal:		DECIMAL;

SPACE_AR:		[ \t\r\n]+ -> skip;

mode FUNC_CALL_MODE; // function call

DISTANCE_F:		'DISTANCE';
ANGLE_F:		'ANGLE';
TORSION_F:		'TORSION';
COORDINATE_F:		'COORDINATE';
PLANE_F:		'PLANE';
COM_F:			'COM';

Integer_F:		INTEGER;
Real_F:			REAL;
Ambmask_F:		':' INTEGER '@' SIMPLE_NAME; // ambmask format

Comma_F:		',';

L_paren_F:		'(';
R_paren_F:		')';
L_brace_F:		'{';
R_brace_F:		'}';
L_brakt_F:		'[';
R_brakt_F:		']';

R_quot:			'"' -> popMode;

SPACE_F:		[ \t\r\n]+ -> skip;

mode MAP_MODE;

Ambig_code_MP:		(DECIMAL '-' DECIMAL ':' DECIMAL | (ALPHA | '_') SIMPLE_NAME '.' DECIMAL);
Integer_MP:		INTEGER;
Simple_name_MP:		SIMPLE_NAME;

Equ_op_MP:		'=';

SPACE_MP:		[ \t]+ -> skip;
RETURN_MP:		[\r\n]+ -> popMode;

//SECTION_COMMENT_MP:	('#' | '!' | ';' | '\\' | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+) ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT_MP:	('#' | '!' | ';' | '\\' | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+) ~[\r\n]* -> channel(HIDDEN);

