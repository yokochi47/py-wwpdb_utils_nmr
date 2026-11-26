/*
 PIPP (Assigned chemical shift) lexer grammar for ANTLR v4.
 Copyright 2025 Masashi Yokochi

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

lexer grammar PippCSLexer;

Shift_fl_frmt:		'SHIFT_FL_FRMT';
Res_siad:		'RES_SIAD';

First_res_in_seq:	'FIRST_RES_IN_SEQ';

Exp_peak_pick_tbl:	'EXP_PEAK_PICK_TBL' -> pushMode(EXT_TBL_MODE);

Res_ID:			'RES_ID';
Res_type:		'RES_TYPE';
Prev_type:		'PREV_TYPE';
Cur_type:		'CUR_TYPE';
Spin_system_ID:		'SPIN_SYSTEM_ID';
Heterogeneity:		'HETEROGENEITY';

End_res_def:		'END_RES_DEF';

Type_pred:		ALPHA+ '(' (DECIMAL | DEC_DOT_DEC) ')';
Note_begin:		'(' -> pushMode(MULTIPLE_NOTE_MODE);

Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC);
// Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) ([Ee] ('+' | '-')? DECIMAL)?;
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;
fragment SEPARATOR:	[,:|/];
fragment NOTE:		('+' | '-')? (ALPHA+ '.' DECIMAL | SIMPLE_NAME);

SHARP_COMMENT:		'#'+ ~[\r\n]* '#'* ~[\r\n]* -> channel(HIDDEN);
EXCLM_COMMENT:		'!'+ ~[\r\n]* '!'* ~[\r\n]* -> channel(HIDDEN);
//SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

Simple_name:		SIMPLE_NAME;
//Residue_number:	Integer;
//Residue_name:		SIMPLE_NAME;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_' | '-' | '+' | '.' | '*' | '?' | '{' | '[';
fragment NAME_CHAR:	START_CHAR | '\'' | '"' | ',' | ';' | '#' | '%' | '|' | '/' | '}' | ']' | ':';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

CONTINUE:		'\\' [\r\n]+ -> skip;

SPACE:			[ \t]+ -> skip;
RETURN:			[\r\n]+;

fragment COMMENT_START_CHAR:	('#' | '!' | '\\' | '&' | '/' | '=');

//ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	(COMMENT_START_CHAR | COMMENT_START_CHAR '/'+ | COMMENT_START_CHAR '*'+ | COMMENT_START_CHAR '='+ | 'REMARK' 'S'?) ' '* RETURN -> channel(HIDDEN);
LINE_COMMENT:		(COMMENT_START_CHAR | COMMENT_START_CHAR '/'+ | COMMENT_START_CHAR '*'+ | COMMENT_START_CHAR '='+ | 'REMARK' 'S'?) ~[\r\n]* RETURN -> channel(HIDDEN);

mode EXT_TBL_MODE;

fragment START_CHAR_ET:	ALPHA_NUM | '_' | '-' | '+' | '.' | '*' | '?' | '{' | '[' | '/';
fragment NAME_CHAR_ET:	START_CHAR | '\'' | '"' | ',' | ';' | '#' | '%' | '|' | '/' | '}' | ']';

Res_ID_:		'RES_ID' -> popMode;

Label:			'Label';
Exp_par_fl:		'Exp Par Fl';
Peak_pick_fl:		'Peak-Pick Fl';
Cross_ref:		'#-Cross-Ref';

Simple_name_ET:		START_CHAR_ET NAME_CHAR_ET*;

SPACE_ET:		[ \t]+ -> skip;
RETURN_ET:		[\r\n]+;

mode MULTIPLE_NOTE_MODE;

Note:			NOTE;
Note_end:		')' -> popMode;

SPACE_MN:		[ \t\r\n]+ -> skip;
