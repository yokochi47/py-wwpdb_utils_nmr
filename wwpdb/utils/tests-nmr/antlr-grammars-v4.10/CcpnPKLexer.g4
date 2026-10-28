/*
 Ccpn PK (Spectral peak list) lexer grammar for ANTLR v4.
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

lexer grammar CcpnPKLexer;

/* CCPN: Peak list format
 See also https://sites.google.com/site/ccpnwiki/home/documentation/ccpnmr-analysis/popup-reference/peaks-peak-lists
*/

Num:			'Number' -> pushMode(VARS_MODE);
Id:			'#' -> pushMode(VARS_MODE);
Assign_F1:		'Assign F1' -> pushMode(VARS_MODE);
Position_F1:		'Position F1' -> pushMode(VARS_MODE);
Shift_F1:		'Shift F1' -> pushMode(VARS_MODE);

Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC);
Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) ([Ee] ('+' | '-')? DECIMAL)?;
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

//SHARP_COMMENT:		'#'+ ~[\r\n]* '#'* ~[\r\n]* -> channel(HIDDEN);
EXCLM_COMMENT:		'!'+ ~[\r\n]* '!'* ~[\r\n]* -> channel(HIDDEN);
SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

Simple_name:		SIMPLE_NAME;
//Residue_number:	Integer;
//Residue_name:		SIMPLE_NAME;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;

Any_name:		~[ \t\r\n]+;

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_' | '-' | '+' | '.' | '*' | '?' | '(' | '{' | '[';
fragment NAME_CHAR:	START_CHAR | '\'' | '"' | ',' | ';' | '#' | '%' | '|' | '/' | ')' | '}' | ']';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

SPACE:			[ \t]+ -> skip;
RETURN:			[\r\n]+;

fragment COMMENT_START_CHAR:	('!' | '\\' | '&' | '/' | '*' | '=');

//ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	(COMMENT_START_CHAR | COMMENT_START_CHAR '/'+ | COMMENT_START_CHAR '*'+ | COMMENT_START_CHAR '='+ | 'REMARK' 'S'?) ' '* -> channel(HIDDEN);
LINE_COMMENT:		(COMMENT_START_CHAR | COMMENT_START_CHAR '/'+ | COMMENT_START_CHAR '*'+ | COMMENT_START_CHAR '='+ | 'REMARK' 'S'?) ~[\r\n]* -> channel(HIDDEN);

mode VARS_MODE;

Id_:			'#';

Position_F1_:		'Position F1';
Position_F2:		'Position F2';
Position_F3:		'Position F3';
Position_F4:		'Position F4';

Shift_F1_:		'Shift F1';
Shift_F2:		'Shift F2';
Shift_F3:		'Shift F3';
Shift_F4:		'Shift F4';

Assign_F1_:		'Assign F1';
Assign_F2:		'Assign F2';
Assign_F3:		'Assign F3';
Assign_F4:		'Assign F4';

Height:			'Height';
Volume:			'Volume';

Line_width_F1:		'Line Width F1 (Hz)';
Line_width_F2:		'Line Width F2 (Hz)';
Line_width_F3:		'Line Width F3 (Hz)';
Line_width_F4:		'Line Width F4 (Hz)';

Merit:			'Merit';

Details:		'Details';
Fit_method:		'Fit Method';
Vol_method:		'Vol. Method';

SPACE_VARS:		[ \t]+ -> skip;
RETURN_VARS:		[\r\n]+ -> popMode;

