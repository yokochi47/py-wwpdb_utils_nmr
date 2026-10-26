/*
 BIOSYM MR (Magnetic Restraint) lexer grammar for ANTLR v4.10 or later
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

lexer grammar BiosymMRLexer;

options { caseInsensitive=true; }

Integer:		('+' | '-')? DECIMAL;
Float:			('+' | '-')? (DECIMAL | DEC_DOT_DEC);
Float_DecimalComma:	('+' | '-')? DEC_COM_DEC;
Real:			('+' | '-')? (DECIMAL | DEC_DOT_DEC) ('E' ('+' | '-')? DECIMAL)?;
fragment DEC_DOT_DEC:	(DECIMAL '.' DECIMAL) | ('.' DECIMAL);
fragment DEC_COM_DEC:	(DECIMAL ',' DECIMAL) | (',' DECIMAL);
fragment DEC_DIGIT:	[0-9];
fragment DECIMAL:	DEC_DIGIT+;

SHARP_COMMENT:		'#'+ ~[\r\n]* '#'* ~[\r\n]* -> channel(HIDDEN);
EXCLM_COMMENT:		'!'+ ~[\r\n]* '!'* ~[\r\n]* -> channel(HIDDEN);
SMCLN_COMMENT:		';'+ ~[\r\n]* ';'* ~[\r\n]* -> channel(HIDDEN);

Chiral_code:		'R' | 'S';
Atom_selection:		DECIMAL ':' SIMPLE_NAME '_' ALPHA? DECIMAL ALPHA? ':' SIMPLE_NAME;
//Simple_name:		SIMPLE_NAME;
//Residue_number:	Integer;
//Residue_name:		SIMPLE_NAME;
//Atom_name:		ALPHA_NUM ATM_NAME_CHAR*;

fragment ALPHA:		[A-Z];
fragment ALPHA_NUM:	ALPHA | DEC_DIGIT;
fragment START_CHAR:	ALPHA_NUM | '_';
fragment NAME_CHAR:	START_CHAR | '\'' | '-' | '+' | '.' | '"' | '*' | '#' | '|' | ',';
//fragment ATM_NAME_CHAR:	ALPHA_NUM | '\'';
fragment SIMPLE_NAME:	START_CHAR NAME_CHAR*;

Ordinal:		DECIMAL '.';

/* Insight II distance restraint */
Restraint:		'restraint' -> pushMode(INSIGHT_II_MODE);

SPACE:			[ \t\r\n]+ -> skip;
ENCLOSE_COMMENT:	'{' (ENCLOSE_COMMENT | .)*? '}' -> channel(HIDDEN);
SECTION_COMMENT:	('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK' 'S'?) ' '* [\r\n]+ -> channel(HIDDEN);
LINE_COMMENT:		('#' | '!' | ';' | '\\' | '&' | '/' '/'+ | '*' '*'+ | '-' '-'+ | '+' '+'+ | '=' '='+ | 'REMARK' 'S'?) ~[\r\n]* -> channel(HIDDEN);

mode INSIGHT_II_MODE;

fragment NAME_CHAR_II:	START_CHAR | '\'' | '-' | '+' | '.' | '"' | '*' | '#' | ':' | '|';
fragment SIMPLE_NAME_II:	START_CHAR NAME_CHAR_II*;

Double_quote_string:	'"' SIMPLE_NAME_II '"';

Create:			'create';
Function:		'function';
Target:			'target';

Distance:		'distance';
Quadratic:		'quadratic';
Flat_bottomed:		'flatBottomed';

Relative:		'relative';

SPACE_II:		[ \t]+ -> skip;

RETURN_II:		[\r\n]+ -> popMode;

