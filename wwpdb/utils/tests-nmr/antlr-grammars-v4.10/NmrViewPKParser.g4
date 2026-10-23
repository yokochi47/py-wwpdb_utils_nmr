/*
 NmrView PK (Spectral peak list) parser grammar for ANTLR v4.
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

parser grammar NmrViewPKParser;

options { tokenVocab=NmrViewPKLexer; }

nmrview_pk:
	RETURN?
	(
	data_label |
	peak_list_2d |
	peak_list_3d |
	peak_list_4d |
	peak_list_wo_eju_2d |
	peak_list_wo_eju_3d |
	peak_list_wo_eju_4d |
	RETURN
	)*
	EOF;

/* NMRView: Peak list format
 See also https://github.com/onemoonsci/nmrfxprocessordocs/blob/master/pages/02.viewer/08.refcmds/01.ref/docs.md
*/

data_label:
	Label Dataset Sw Sf Condition? SINGLE_NL_LA*
	labels SINGLE_NL_LA+
	Simple_name_LA* SINGLE_NL_LA+
	labels SINGLE_NL_LA+
	labels SINGLE_NL_LA+;

labels:
	label+;

peak_list_2d:
	L_name P_name W_name B_name E_name J_name U_name
	L_name P_name W_name B_name E_name J_name U_name
	Vol Int Stat Comment? Flag0 RETURN?
	peak_2d+;

peak_2d:
	Integer
	enclose_data number number number Simple_name jcoupling enclose_data
	enclose_data number number number Simple_name jcoupling enclose_data
	number number Integer enclose_data? Integer+ (RETURN | EOF);

peak_list_3d:
	L_name P_name W_name B_name E_name J_name U_name
	L_name P_name W_name B_name E_name J_name U_name
	L_name P_name W_name B_name E_name J_name U_name
	Vol Int Stat Comment? Flag0 RETURN?
	peak_3d+;

peak_3d:
	Integer
	enclose_data number number number Simple_name jcoupling enclose_data
	enclose_data number number number Simple_name jcoupling enclose_data
	enclose_data number number number Simple_name jcoupling enclose_data
	number number Integer enclose_data? Integer+ (RETURN | EOF);

peak_list_4d:
	L_name P_name W_name B_name E_name J_name U_name
	L_name P_name W_name B_name E_name J_name U_name
	L_name P_name W_name B_name E_name J_name U_name
	L_name P_name W_name B_name E_name J_name U_name
	Vol Int Stat Comment? Flag0 RETURN?
	peak_4d+;

peak_4d:
	Integer
	enclose_data number number number Simple_name jcoupling enclose_data
	enclose_data number number number Simple_name jcoupling enclose_data
	enclose_data number number number Simple_name jcoupling enclose_data
	enclose_data number number number Simple_name jcoupling enclose_data
	number number Integer enclose_data? Integer+ (RETURN | EOF);

peak_list_wo_eju_2d:
	L_name P_name W_name B_name
	L_name P_name W_name B_name
	Vol Int Stat Comment? Flag0 RETURN?
	peak_wo_eju_2d+;

peak_wo_eju_2d:
	Integer
	enclose_data number number number
	enclose_data number number number
	number number Integer enclose_data? Integer+ (RETURN | EOF);

peak_list_wo_eju_3d:
	L_name P_name W_name B_name
	L_name P_name W_name B_name
	L_name P_name W_name B_name
	Vol Int Stat Comment? Flag0 RETURN?
	peak_wo_eju_3d+;

peak_wo_eju_3d:
	Integer
	enclose_data number number number
	enclose_data number number number
	enclose_data number number number
	number number Integer enclose_data? Integer+ (RETURN | EOF);

peak_list_wo_eju_4d:
	L_name P_name W_name B_name
	L_name P_name W_name B_name
	L_name P_name W_name B_name
	L_name P_name W_name B_name
	Vol Int Stat Comment? Flag0 RETURN?
	peak_wo_eju_4d+;

peak_wo_eju_4d:
	Integer
	enclose_data number number number
	enclose_data number number number
	enclose_data number number number
	enclose_data number number number
	number number Integer enclose_data? Integer+ (RETURN | EOF);

label:
	Float_LA | Simple_name_LA | ENCLOSE_DATA_LA;

jcoupling:
	Float | Simple_name | enclose_data;

/* number expression in peak list */
number:	Real | Float | Integer | Simple_name;

/* enclose data */
enclose_data:	L_brace Any_name* R_brace;

