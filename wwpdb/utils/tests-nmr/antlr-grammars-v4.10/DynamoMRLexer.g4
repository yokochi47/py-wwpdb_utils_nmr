/*
 DYNAMO/PALES/TALOS MR (Magnetic Restraint) lexer grammar for ANTLR v4.
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

lexer grammar DynamoMRLexer;

/* DYNAMO: Syntax
 See also https://spin.niddk.nih.gov/NMRPipe/dynamo/
*/

/* PALES: Syntax
 See also https://spin.niddk.nih.gov/bax/software/PALES/
*/

Data:			'DATA' -> pushMode(DATA_MODE);

Vars:			'VARS' -> pushMode(VARS_MODE);

Format:			'FORMAT' -> pushMode(FORMAT_MODE);

Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC);
Float_DecimalComma:	('+' | '-')? DEC_COM_DEC;
//Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) ([Ee] ('+' | '-')? DECIMAL)?;
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL?) | ('.' DECIMAL);
fragment DEC_COM_DEC:	(DECIMAL ',' DECIMAL?) | (',' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

SHARP_COMMENT:		'#'+ ~[\r\n]* '#'* ~[\r\n]* -> channel(HIDDEN);
EXCLM_COMMENT:		'!'+ ~[\r\n]* '!'* ~[\r\n]* -> channel(HIDDEN);
SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

Simple_name:		SIMPLE_NAME;
//Residue_number:	Integer;
//Residue_name:		SIMPLE_NAME;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_';
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.' | '"' | '*' | '#' | '|';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

SPACE:			[ \t\r\n]+ -> skip;
ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK' 'S'?) ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT:		('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK' 'S'?) ~[\r\n]* -> channel(HIDDEN);

mode DATA_MODE;

First_resid:		'FIRST_RESID';
Sequence:		'SEQUENCE' -> pushMode(SEQ_MODE);
Db_name:		'DB_NAME';
Tab_name:		'TAB_NAME';
Tab_id:			'TAB_ID';

Pales_mode:		'PALES_MODE';
Tensor_mode:		'TENSOR_MODE';
Saupe_matrix:		'SAUPE_MATRIX';
S_DA:			'S';
Saupe:			'SAUPE';
Irreducible_rep:	'IRREDUCIBLE_REP';
Irreducible:		'IRREDUCIBLE';
General_magnitude:	'GENERAL_MAGNITUDE';
Mapping_corr:		'MAPPING_COOR';
Mapping:		'MAPPING';
Inv:			'INV';
Eigenvalues:		'EIGENVALUES';
Eigenvectors:		'EIGENVECTORS';
X_axis:			'X_AXIS';
Y_axis:			'Y_AXIS';
Z_axis:			'Z_AXIS';
Q_euler_solutions:	'Q_EULER_SOLUTIONS';
Q_euler_angles:		'Q_EULER_ANGLES';
Euler_solutions:	'EULER_SOLUTIONS';
Euler_angles:		'EULER_ANGLES';
Da:			'Da';
Dr:			'Dr';
Aa:			'Aa';
Ar:			'Ar';
Da_hn:			'Da_HN';
Rhombicity:		'Rhombicity';
N:			'N';
Rms:			'RMS';
Chi2:			'Chi2';
Corr:			'CORR';
R:			'R';
Q:			'Q';
Regression:		'REGRESSION';
Offset:			'OFFSET';
Slope:			'SLOPE';
Bax:			'BAX';
Plus_minus:		'+/-';
Hz:			'Hz';

Comma_DA:		',';
L_paren_DA:		'(';
R_paren_DA:		')';
L_brkt_DA:		'[';
R_brkt_DA:		']';

Integer_DA:		('+' | '-')? DECIMAL;
Float_DA:		('+' | '-')? (DECIMAL | DEC_DOT_DEC);
Real_DA:		('+' | '-')? (DECIMAL | DEC_DOT_DEC) ([Ee] ('+' | '-')? DECIMAL)?;

Simple_name_DA:		SIMPLE_NAME;

SPACE_DA:		[ \t]+ -> skip;
RETURN_DA:		[\r\n]+ -> popMode;

//SECTION_COMMENT_DA:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK' 'S'?) ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT_DA:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK' 'S'?) ~[\r\n]* -> channel(HIDDEN);

mode SEQ_MODE;

One_letter_code:	[ABCDEFGHIKLMNPQRSTVWYZ]+;

SPACE_SQ:		[ \t]+ -> skip;
RETURN_SQ:		[\r\n]+ -> mode(DEFAULT_MODE);

//SECTION_COMMENT_SQ:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK' 'S'?) ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT_SQ:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK' 'S'?) ~[\r\n]* -> channel(HIDDEN);

mode VARS_MODE;

Index:			'INDEX';
Group:			'GROUP';

Segname_I:		'SEGNAME_I';
Resid_I:		'RESID_I';
Resname_I:		'RESNAME_I';
Atomname_I:		'ATOMNAME_I';

Segname_J:		'SEGNAME_J';
Resid_J:		'RESID_J';
Resname_J:		'RESNAME_J';
Atomname_J:		'ATOMNAME_J';

Segname_K:		'SEGNAME_K';
Resid_K:		'RESID_K';
Resname_K:		'RESNAME_K';
Atomname_K:		'ATOMNAME_K';

Segname_L:		'SEGNAME_L';
Resid_L:		'RESID_L';
Resname_L:		'RESNAME_L';
Atomname_L:		'ATOMNAME_L';

Resid:			'RESID';
Resname:		'RESNAME';

A:			[Aa];
B:			[Bb];
C:			[Cc];
D:			[Dd];
DD:			[Dd] [Dd];
DI:			[Dd] [Ii];
D_diff:			[Dd] '_' [Dd] [Ii] [Ff] [Ff];	
D_obs:			[Dd] '_' [Oo] [Bb] [Ss];	
FC:			[Ff] [Cc];
S:			[Ss];
W:			[Ww];

D_Lo:			'D_LO';
D_Hi:			'D_HI';
Angle_Lo:		'ANGLE_LO';
Angle_Hi:		'ANGLE_HI';
Phase:			'PHASE';
ObsJ:			'OBSJ';

Phi:			'PHI';
Psi:			'PSI';
Dphi:			'DPHI';
Dpsi:			'DPSI';
Dist:			'DIST';
S2:			'S2';
Count:			'COUNT';
Cs_count:		'CS_COUNT';
Class:			'CLASS';

SPACE_VA:		[ \t]+ -> skip;
RETURN_VA:		[\r\n]+ -> popMode;

//SECTION_COMMENT_VA:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK' 'S'?) ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT_VA:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK' 'S'?) ~[\r\n]* -> channel(HIDDEN);

mode FORMAT_MODE;

Format_code:		'%' '+'? DECIMAL? ('s' | 'd' | '.' DECIMAL ('f' | 'e') | '+'? 'e');

SPACE_FO:		[ \t]+ -> skip;
RETURN_FO:		[\r\n]+ -> popMode;

//SECTION_COMMENT_FO:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK' 'S'?) ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT_FO:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK' 'S'?) ~[\r\n]* -> channel(HIDDEN);

