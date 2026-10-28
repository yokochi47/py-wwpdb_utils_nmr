/*
 Sparky PK (Spectral peak list) lexer grammar for ANTLR v4.
 Copyright 2024 Masashi Yokochi

you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

lexer grammar SparkyPKLexer;

Assignment:		'Assignment' 's'? -> pushMode(LABEL_MODE);
W1:			'w1' -> pushMode(LABEL_MODE);

Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC);
Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) ([Ee] ('+' | '-')? DECIMAL)?;
Real_vol:		('+' | '-')? (DECIMAL | DEC_DOT_DEC) ([Ee] ('+' | '-')? DECIMAL)? ' ' [a-z-][a-z-];
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL) | ('.' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

SHARP_COMMENT:		'#'+ ~[\r\n]* '#'* ~[\r\n]* -> channel(HIDDEN);
EXCLM_COMMENT:		'!'+ ~[\r\n]* '!'* ~[\r\n]* -> channel(HIDDEN);
SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

fragment ASS_EACH_AXIS:	SIMPLE_NAME ([:;&/,.()] SIMPLE_NAME [&"]*)*;

Assignment_2d_ex:	ASS_EACH_AXIS '-' ASS_EACH_AXIS;
Assignment_3d_ex:	ASS_EACH_AXIS '-' ASS_EACH_AXIS '-' ASS_EACH_AXIS;
Assignment_4d_ex:	ASS_EACH_AXIS '-' ASS_EACH_AXIS '-' ASS_EACH_AXIS '-' ASS_EACH_AXIS;

Note_2d_ex:		Assignment_2d_ex ('/' Assignment_2d_ex)* '(' ALPHA_NUM+ '=' Float ')';
Note_3d_ex:		Assignment_3d_ex ('/' Assignment_3d_ex)* '(' ALPHA_NUM+ '=' Float ')';
Note_4d_ex:		Assignment_4d_ex ('/' Assignment_4d_ex)* '(' ALPHA_NUM+ '=' Float ')';
Note_ex:		ASS_EACH_AXIS ('/' ASS_EACH_AXIS)* ('(' ALPHA_NUM+ '=' Float ')')?;

Simple_name:		SIMPLE_NAME;
//Residue_number:	Integer;
//Residue_name:		SIMPLE_NAME;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;

fragment ALPHA:		[A-Za-z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_' | '+' | '.' | '*' | '?';
fragment NAME_CHAR:	START_CHAR | '\'' | '"' | ',' | ';' | '#' | '%' | '|';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

SPACE:			[ \t]+ -> skip;
RETURN:			[\r\n]+;

fragment COMMENT_START_CHAR:	('!' | ';' | '\\' | '&' | '/' | '*' | '=');

ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	('#' | COMMENT_START_CHAR | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK' 'S'?) ' '* -> channel(HIDDEN);
LINE_COMMENT:		(('#' (' ' | ALPHA_NUM)) | COMMENT_START_CHAR | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK' 'S'?) ~[\r\n]* -> channel(HIDDEN);

mode LABEL_MODE;

W1_Hz_LA:		'w1 (' [Hh] 'z)';
W2_Hz_LA:		'w2 (' [Hh] 'z)';
W3_Hz_LA:		'w3 (' [Hh] 'z)';
W4_Hz_LA:		'w4 (' [Hh] 'z)';

Lw1_Hz_LA:		[Ll] 'w1 (' [Hh] 'z)';
Lw2_Hz_LA:		[Ll] 'w2 (' [Hh] 'z)';
Lw3_Hz_LA:		[Ll] 'w3 (' [Hh] 'z)';
Lw4_Hz_LA:		[Ll] 'w4 (' [Hh] 'z)';

W1_LA:			'w1';
W2_LA:			'w2';
W3_LA:			'w3';
W4_LA:			'w4';

Dev_w1_LA:		[Dd] 'ev w1';
Dev_w2_LA:		[Dd] 'ev w2';
Dev_w3_LA:		[Dd] 'ev w3';
Dev_w4_LA:		[Dd] 'ev w4';

Dummy_H_LA:		'Fit Height' 's'?;
Height_LA:		('Data '? 'Height' 's'? | 'Data');
Volume_LA:		'Volume';
Dummy_Rms_LA:		'Fit RMS %';
S_N_LA:			[Ss] '/' [Nn];
Atom1_LA:		'Atom1' | 'ATOM1';
Atom2_LA:		'Atom2' | 'ATOM2';
Atom3_LA:		'Atom3' | 'ATOM3';
Atom4_LA:		'Atom4' | 'ATOM4';
Distance_LA:		'Distance' | 'DISTANCE';
Note_LA:		'Note' | 'NOTE';

SPACE_LA:		[ \t]+ -> skip;
RETURN_LA:		[\r\n]+ -> popMode;

