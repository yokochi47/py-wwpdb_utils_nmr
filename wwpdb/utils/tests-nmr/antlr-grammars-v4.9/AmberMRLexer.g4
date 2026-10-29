/*
 AMBER MR (Magnetic Restraint) lexer grammar for ANTLR v4.
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

END:			(('&' E N D) | '/') -> mode(DEFAULT_MODE);

/* Amber: NMR restraints - 29.1 Distance, angle and torsional restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
RST:			'&' R S T;

IAT:			I A T
			-> pushMode(INT_ARRAY_MODE);		// = Integer [ , Integer ]*
RSTWT:			R S T W T
			-> pushMode(REAL_ARRAY_MODE);		// = Real [ , Real ] [ , Real ] [ , Real ]
RESTRAINT:		R E S T R A I N T;			// = " RestraintFunctionCall " [ , " RestraintFunctionCall " ]*

fragment ATNAM_:	A T N A M;
ATNAM_Lp:		ATNAM_ ' '* L_paren
			-> pushMode(AQSTR_PARAM_MODE);		// = Quoted_atom_name
ATNAM:			ATNAM_
			-> pushMode(QSTR_ARRAY_MODE);		// = Quoted_atom_name [ , Quoted_atom_name ]*

IRESID:			I R E S I D
			-> pushMode(BINT_PARAM_MODE);		// = Boolint
NSTEP1:			N S T E P '1'
			-> pushMode(INT_PARAM_MODE);		// = Integer
NSTEP2:			N S T E P '2'
			-> pushMode(INT_PARAM_MODE);		// = Integer
IRSTYP:			I R S T Y P
			-> pushMode(BINT_PARAM_MODE);		// = Boolint
IALTD:			I A L T D
			-> pushMode(BINT_PARAM_MODE);		// = Boolint
IFVARI:			I F V A R I
			-> pushMode(INT_PARAM_MODE);		// = Integer
NINC:			N I N C
			-> pushMode(INT_PARAM_MODE);		// = Integer
IMULT:			I M U L T
			-> pushMode(BINT_PARAM_MODE);		// = Boolint

R1:			R '1'
			-> pushMode(REAL_PARAM_MODE);		// = Real
R2:			R '2'
			-> pushMode(REAL_PARAM_MODE);		// = Real
R3:			R '3'
			-> pushMode(REAL_PARAM_MODE);		// = Real
R4:			R '4'
			-> pushMode(REAL_PARAM_MODE);		// = Real

RK2:			R K '2'
			-> pushMode(REAL_PARAM_MODE);		// = Real
RK3:			R K '3'
			-> pushMode(REAL_PARAM_MODE);		// = Real

R1A:			R '1' A
			-> pushMode(REAL_PARAM_MODE);		// = Real
R2A:			R '2' A
			-> pushMode(REAL_PARAM_MODE);		// = Real
R3A:			R '3' A
			-> pushMode(REAL_PARAM_MODE);		// = Real
R4A:			R '4' A
			-> pushMode(REAL_PARAM_MODE);		// = Real

RK2A:			R K '2' A
			-> pushMode(REAL_PARAM_MODE);		// = Real
RK3A:			R K '3' A
			-> pushMode(REAL_PARAM_MODE);		// = Real

R0:			R '0'
			-> pushMode(REAL_PARAM_MODE);		// = Real
K0:			K '0'
			-> pushMode(REAL_PARAM_MODE);		// = Real
R0A:			R '0' A
			-> pushMode(REAL_PARAM_MODE);		// = Real
K0A:			K '0' A
			-> pushMode(REAL_PARAM_MODE);		// = Real

RJCOEF:			R J C O E F
			->pushMode(REAL_ARRAY_MODE);		// = Real, Real, Real

fragment IGR_:		I G R;					// = Integer [ , Integer ]*
IGR1:			IGR_ '1' -> pushMode(INT_ARRAY_MODE);
IGR2:			IGR_ '2' -> pushMode(INT_ARRAY_MODE);
IGR3:			IGR_ '3' -> pushMode(INT_ARRAY_MODE);
IGR4:			IGR_ '4' -> pushMode(INT_ARRAY_MODE);
IGR5:			IGR_ '5' -> pushMode(INT_ARRAY_MODE);
IGR6:			IGR_ '6' -> pushMode(INT_ARRAY_MODE);
IGR7:			IGR_ '7' -> pushMode(INT_ARRAY_MODE);
IGR8:			IGR_ '8' -> pushMode(INT_ARRAY_MODE);

FXYZ:			F X Y Z
			-> pushMode(BINT_ARRAY_MODE);		// = Boolint, Boolint, Boolint
OUTXYZ:			O U T X Y Z
			-> pushMode(BINT_PARAM_MODE);		// = Boolint

fragment GRNAM_:	G R N A M;
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

IR6:			I R '6'
			-> pushMode(BINT_PARAM_MODE);		// = Boolint
IFNTYP:			I F N T Y P
			-> pushMode(BINT_PARAM_MODE);		// = Boolint

IXPK:			I X P K
			-> pushMode(INT_PARAM_MODE);		// = Integer
NXPK:			N X P K
			-> pushMode(INT_PARAM_MODE);		// = Integer

ICONSTR:		I C O N S T R
			-> pushMode(INT_PARAM_MODE);		// = Integer

/* Amber: NMR restraints - 29.2. NOESY volume restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
NOEEXP:			'&' N O E E X P;

NPEAK:			N P E A K
			-> pushMode(INT_ARRAY_MODE);		// = IntArray
EMIX:			E M I X
			-> pushMode(REAL_ARRAY_MODE);		// = Real [ , Real ]*

IHP:			I H P
			-> pushMode(INT_PARAM_MODE);		// ihp(Integer, Integer) = IntArray
JHP:			J H P
			-> pushMode(INT_PARAM_MODE);		// jhp(Integer, Integer) = IntArray

AEXP:			A E X P
			-> pushMode(REAL_PARAM_MODE);		// aexp(Integer, Integer) = RealArray
ARANGE:			A R A N G E
			-> pushMode(REAL_PARAM_MODE);		// arange(Integer, Integer) = RealArray
AWT:			A W T
			-> pushMode(REAL_PARAM_MODE);		// awt(Integer, Integer) = RealArray

INVWT1:			I N V W T '1'
			-> pushMode(REAL_PARAM_MODE);		// = Real
INVWT2:			I N V W T '2'
			-> pushMode(REAL_PARAM_MODE);		// = Real

OMEGA:			O M E G A
			-> pushMode(REAL_PARAM_MODE);		// = Real
TAUROT:			T A U R O T
			-> pushMode(REAL_PARAM_MODE);		// = Real
TAUMET:			T A U M E T
			-> pushMode(REAL_PARAM_MODE);		// = Real
ID2O:			I D '2' O
			-> pushMode(BINT_PARAM_MODE);		// = Boolint
OSCALE:			O S C A L E
			-> pushMode(REAL_PARAM_MODE);		// = Real

/* Amber: NMR restraints - 29.3. Chemical shift restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
SHF:			'&' S H F;

NRING:			N R I N G
			-> pushMode(INT_PARAM_MODE);		// = Integer
NATR:			N A T R
			-> pushMode(INT_PARAM_MODE);		// natr(Integer) = Integer [ , Integer ]*
IATR:			I A T R
			-> pushMode(INT_PARAM_MODE);		// iatr(Integer) = Integer
NAMR:			N A M R
			-> pushMode(QSTR_PARAM_MODE);		// namr(Integer) = Quoted_atom_name
STR:			S T R
			-> pushMode(REAL_ARRAY_MODE);		// str(Integer) = Real [ , Real ]*
IPROT:			I P R O T
			-> pushMode(INT_PARAM_MODE);		// iprot(Integer) = Integer [ , Integer ]*
OBS:			O B S
			-> pushMode(REAL_PARAM_MODE);		// obs(Integer) = Real [ , Real ]*
SHRANG:			S H R A N G
			-> pushMode(REAL_ARRAY_MODE);		// shrang(Integer) = Real [ , Real ]*
WT:			W T
			-> pushMode(REAL_ARRAY_MODE);		// wt(Integer) = Real [ , Real ]*

NPROT:			N P R O T
			-> pushMode(INT_PARAM_MODE);		// = Integer
SHCUT:			S H C U T
			-> pushMode(REAL_PARAM_MODE);		// = Real
NTER:			N T E R
			-> pushMode(INT_PARAM_MODE);		// = Integer
CTER:			C T E R
			-> pushMode(INT_PARAM_MODE);		// = Integer

/* Amber: NMR restraints - 29.4. Psuedocontact shift restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
PCSHF:			'&' P C S H F;

//NPROT:		N P R O T;				// = Integer
NME:			N M E
			-> pushMode(INT_PARAM_MODE);		// = Integer
NMPMC:			N M P M C
			-> pushMode(QSTR_PARAM_MODE);		// = Quoted_atom_name

OPTPHI:			O P T P H I
			-> pushMode(REAL_PARAM_MODE);		// optphi(Integer) = Real [ , Real ]*
OPTTET:			O P T T E T
			-> pushMode(REAL_PARAM_MODE);		// opttet(Integer) = Real [ , Real ]*
OPTOMG:			O P T O M G
			-> pushMode(REAL_PARAM_MODE);		// optomg(Integer) = Real [ , Real ]*
OPTA1:			O P T A '1'
			-> pushMode(REAL_PARAM_MODE);		// opta1(Integer) = Real [ , Real ]*
OPTA2:			O P T A '2'
			-> pushMode(REAL_PARAM_MODE);		// opta2(Integer) = Real [ , Real ]*
OPTKON:			O P T K O N
			-> pushMode(REAL_PARAM_MODE);		// = Real

//fragment IPROT:	I P R O T;				// iprot(Integer) = Integer
//fragment OBS:		O B S;					// = Real
//fragment WT:		W T;					// = RealArray

TOLPRO:			T O L P R O
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray
MLTPRO:			M L T P R O
			-> pushMode(INT_PARAM_MODE);		// mltpro(Integer) = IntArray

/* Amber: NMR restraints - 29.5. Direct dipolar coupling restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
ALIGN:			'&' A L I G N;

NDIP:			N D I P
			-> pushMode(INT_PARAM_MODE);		// = Integer

ID:			I D
			-> pushMode(INT_PARAM_MODE);		// id(Integer) = Integer [ , Integer ]*
JD:			J D
			-> pushMode(INT_PARAM_MODE);		// jd(Integer) = Integer [ , Integer ]*

DOBSL:			D O B S L
			-> pushMode(REAL_PARAM_MODE);		// = Real [ , Real ]*
DOBSU:			D O B S U
			-> pushMode(REAL_PARAM_MODE);		// = Real [ , Real ]*
// note that 'dobs' is unauthorized item
DOBS:			D O B S
			-> pushMode(REAL_PARAM_MODE);		// = Real [ , Real ]*

DWT:			D W T
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray

DATASET:		D A T A S E T
			-> pushMode(INT_PARAM_MODE);		// = Integer
								// dataset(Integer) = Integer
NUM_DATASETS:		N U M '_' D A T A S E T S
			-> pushMode(INT_PARAM_MODE);		// = Integer

S11:			S '11'
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray
S12:			S '12'
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray
S13:			S '13'
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray
S22:			S '22'
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray
S23:			S '23'
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray

GIGJ:			G I G J
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray
DIJ:			D I J
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray
DCUT:			D C U T
			-> pushMode(REAL_PARAM_MODE);		// = Real
FJ:			F J
			-> pushMode(REAL_PARAM_MODE);		// = Real
DFAC_AL:		D F A C '_' A L
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray

FREEZEMOL:		F R E E Z E M O L;			// = Logical

/* Amber: NMR restraints - 29.6. Residual CSA or pseudo-CSA restraints - Syntax
 See also https://ambermd.org/Manuals.php (Amber 2021 Reference Manual)
*/
CSA:			'&' C S A;

NCSA:			N C S A
			-> pushMode(INT_PARAM_MODE);		// = Integer

ICSA:			I C S A
			-> pushMode(INT_PARAM_MODE);		// = icsa(Integer) = Integer [ , Integer ]*
JCSA:			J C S A
			-> pushMode(INT_PARAM_MODE);		// = jcsa(Integer) = Integer [ , Integer ]*
KCSA:			K C S A
			-> pushMode(INT_PARAM_MODE);		// = kcsa(Integer) = Integer [ , Integer ]*

COBSL:			C O B S L
			-> pushMode(REAL_PARAM_MODE);		// = Real [ , Real ]*
COBSU:			C O B S U
			-> pushMode(REAL_PARAM_MODE);		// = Real [ , Real ]*
// note that 'cobs' is unauthorized item
COBS:			C O B S
			-> pushMode(REAL_PARAM_MODE);		// = Real [ , Real ]*

CWT:			C W T
			-> pushMode(REAL_ARRAY_MODE);		// = RealArray

DATASETC:		D A T A S E T C
			-> pushMode(INT_PARAM_MODE);		// = Integer

FIELD:			F I E L D
			-> pushMode(REAL_PARAM_MODE);		// = Real

SIGMA11:		S I G M A '11'
			-> pushMode(REAL_PARAM_MODE);		// = Real
SIGMA12:		S I G M A '12'
			-> pushMode(REAL_PARAM_MODE);		// = Real
SIGMA13:		S I G M A '13'
			-> pushMode(REAL_PARAM_MODE);		// = Real
SIGMA22:		S I G M A '22'
			-> pushMode(REAL_PARAM_MODE);		// = Real
SIGMA23:		S I G M A '23'
			-> pushMode(REAL_PARAM_MODE);		// = Real

CCUT:			C C U T
			-> pushMode(REAL_PARAM_MODE);		// = Real

Comma:			',' -> mode(DEFAULT_MODE);
//Ampersand:		'&';

/* AMBER atom nomenclature mapping generated by makeDIST_RST */
Residue:		R E S I D U E;
Mapping:		M A P P I N G -> pushMode(MAP_MODE);
Ambig:			A M B I G -> pushMode(MAP_MODE);

SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

COMMENT:		('#' | '!')+ -> mode(COMMENT_MODE);

fragment INTEGER:	('+' | '-')? DECIMAL;
fragment REAL:		('+' | '-')? (DECIMAL | DEC_DOT_DEC) (E ('+' | '-')? DECIMAL)?;
Logical:		'.'? T R U E '.'? | '.'? F A L S E '.'?;
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL?) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;
fragment ONE_OR_ZERO:	'0' | '1';

fragment ALPHA:		[A-Za-z];
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

DISTANCE_F:		D I S T A N C E;
ANGLE_F:		A N G L E;
TORSION_F:		T O R S I O N;
COORDINATE_F:		C O O R D I N A T E;
PLANE_F:		P L A N E;
COM_F:			C O M;

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
RETURN_MP:		[\r\n] -> popMode;

//SECTION_COMMENT_MP:	('#' | '!' | ';' | '\\' | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+) ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT_MP:	('#' | '!' | ';' | '\\' | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+) ~[\r\n]* -> channel(HIDDEN);

