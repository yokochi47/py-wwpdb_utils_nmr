##
# File: NmrDpRemediationLegacyCs.py
# Date: 17-Aug-2026
#
# Updates:
##
""" Validation of legacy chemical shift files during NMR data remediation.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.3"

import copy
import os
from typing import Optional, Tuple

import pynmrstar

try:
    from wwpdb.utils.nmr.NmrDpConstant import (AC_FILE_PATH_LIST_KEY,
                                               SF_CATEGORIES,
                                               EMPTY_VALUE,
                                               SEQ_MISMATCH_WARNING_PAT,
                                               INCONSISTENT_RESTRAINT_WARNING_PAT)
    from wwpdb.utils.nmr.NmrDpMrSplitter import detect_encoding
    from wwpdb.utils.nmr.AlignUtil import getChemShiftFormatName
    from wwpdb.utils.nmr.CifToNmrStar import (has_key_value,
                                              get_first_sf_tag)
    from wwpdb.utils.nmr.mr.ParserListenerUtil import contentSubtypeOf
    from wwpdb.utils.nmr.cs.AriaCSReader import AriaCSReader
    from wwpdb.utils.nmr.cs.BareCSReader import BareCSReader
    from wwpdb.utils.nmr.cs.GarretCSReader import GarretCSReader
    from wwpdb.utils.nmr.cs.NmrPipeCSReader import NmrPipeCSReader
    from wwpdb.utils.nmr.cs.OliviaCSReader import OliviaCSReader
    from wwpdb.utils.nmr.cs.PippCSReader import PippCSReader
    from wwpdb.utils.nmr.cs.PpmCSReader import PpmCSReader
    from wwpdb.utils.nmr.cs.NmrStar2CSReader import NmrStar2CSReader
    from wwpdb.utils.nmr.cs.XeasyCSReader import XeasyCSReader
    from wwpdb.utils.nmr.NmrDpRemediationBase import NmrDpRemediationBase
except ImportError:
    from nmr.NmrDpConstant import (AC_FILE_PATH_LIST_KEY,
                                   SF_CATEGORIES,
                                   EMPTY_VALUE,
                                   SEQ_MISMATCH_WARNING_PAT,
                                   INCONSISTENT_RESTRAINT_WARNING_PAT)
    from nmr.NmrDpMrSplitter import detect_encoding
    from nmr.AlignUtil import getChemShiftFormatName
    from nmr.CifToNmrStar import (has_key_value,
                                  get_first_sf_tag)
    from nmr.mr.ParserListenerUtil import contentSubtypeOf
    from nmr.cs.AriaCSReader import AriaCSReader
    from nmr.cs.BareCSReader import BareCSReader
    from nmr.cs.GarretCSReader import GarretCSReader
    from nmr.cs.NmrPipeCSReader import NmrPipeCSReader
    from nmr.cs.OliviaCSReader import OliviaCSReader
    from nmr.cs.PippCSReader import PippCSReader
    from nmr.cs.PpmCSReader import PpmCSReader
    from nmr.cs.NmrStar2CSReader import NmrStar2CSReader
    from nmr.cs.XeasyCSReader import XeasyCSReader
    from nmr.NmrDpRemediationBase import NmrDpRemediationBase

# Reader dispatch for validateLegacyCs() and validateLegacyCsp(). Both run the
# same nine-format sequence over the same readers and labels; only the CSP mode
# flag and the reporting method name differ, so one table serves both.
_CS_READERS = {
    'ari': (AriaCSReader, 'ARIA'),
    'bar': (BareCSReader, 'Bare WSV/TSV/CSV or Sparky resonance list'),
    'gar': (GarretCSReader, 'GARRET'),
    'npi': (NmrPipeCSReader, 'NMRPIPE'),
    'oli': (OliviaCSReader, 'OLIVIA'),
    'pip': (PippCSReader, 'PIPP'),
    'ppm': (PpmCSReader, 'PPM'),
    'st2': (NmrStar2CSReader, 'NMR-STAR V2.1'),
    'xea': (XeasyCSReader, 'XEASY'),
}

LEGACY_CS_READERS = {f'nm-shi-{k}': v for k, v in _CS_READERS.items()}
# an XEASY PROT file may arrive as an auxiliary file
LEGACY_CS_READERS['nm-aux-xea'] = _CS_READERS['xea']

LEGACY_CSP_READERS = {f'nm-csp-{k}': v for k, v in _CS_READERS.items()}


class NmrDpRemediationLegacyCs(NmrDpRemediationBase):
    """ Validation of legacy chemical shift files during NMR data remediation.
    """
    __slots__ = ()

    def _parseLegacyCs(self, spec: tuple, file_path: str, file_name: str,
                       original_file_name: str, create_sf_dict: bool,
                       reserved_list_ids: dict, nmr_poly_seq, entity_assembly,
                       a_cs_format_name: str, deal_lexer_or_parser_error,
                       deal_warn_for_lazy_eval, csp_mode: bool = False, cs_loops=None
                       ) -> Tuple[bool, bool, Optional[object]]:
        """ Parse a legacy chemical shift file with the reader for a given file type,
            re-parsing once if the parser listener asks for it. Lexer errors are ignored
            throughout because these formats may be incomplete XML.
            @param spec: the (reader class, label) entry for the file type
            @param csp_mode: put the reader into chemical shift perturbation mode
            @return: (whether to skip this file, whether the initial parse yielded a
                     listener, the final listener). The second and third are reported
                     separately because the caller's processing was gated on the
                     *initial* parse, exactly as the per-format branches were.
        """
        reader_cls = spec[0]

        def new_reader(*trailing):
            reader = reader_cls(self._reg.verbose, self._reg.log,
                                nmr_poly_seq, entity_assembly,
                                self._reg.ccU, self._reg.csStat, self._reg.nefT,
                                *trailing)
            if csp_mode:
                reader.setCspMode(True)
                reader.setCsloops(cs_loops)
            return reader

        def parse_with(reader, list_id_counter):
            return reader.parse(file_path,
                                createSfDict=create_sf_dict, originalFileName=original_file_name,
                                listIdCounter=list_id_counter, reservedListIds=reserved_list_ids,
                                entryId=self._reg.entry_id)

        _list_id_counter = copy.copy(self._reg.list_id_counter)

        # ignore lexer error because of incomplete XML file format
        listener, parser_err_listener, _ = parse_with(new_reader(), self._reg.list_id_counter)

        if None not in (parser_err_listener, listener)\
           and parser_err_listener.getMessageList() is None:
            if deal_lexer_or_parser_error(a_cs_format_name, file_name, None, parser_err_listener):
                return True, False, None

        if listener is None:
            return False, False, None

        reasons = listener.getReasonsForReparsing()

        if reasons is not None:
            deal_warn_for_lazy_eval(file_name, listener)

            listener = parse_with(new_reader(reasons), _list_id_counter)[0]

        return False, True, listener

    def validateLegacyCs(self) -> bool:
        """ Validate data content of legacy NMR chemical shift files and merge them if possible.
        """

        if self._reg.combined_mode or not self._reg.conversion_server:
            return True

        if AC_FILE_PATH_LIST_KEY not in self._reg.inputParamDict:
            return True

        input_source = self._reg.report.input_sources[0]
        input_source_dic = input_source.get()

        has_poly_seq = has_key_value(input_source_dic, 'polymer_sequence')

        if not has_poly_seq:
            return False

        nmr_poly_seq = input_source_dic['polymer_sequence']
        entity_assembly = None

        file_type = 'nmr-star'
        content_subtype = 'chem_shift'

        sf_category = SF_CATEGORIES[file_type][content_subtype]

        _rlist_ids = []
        if len(self._reg.star_data) > 0 and isinstance(self._reg.star_data[0], pynmrstar.Entry):
            for idx, sf in enumerate(self._reg.star_data[0].get_saveframes_by_category(sf_category), start=1):
                list_id = get_first_sf_tag(sf, 'ID')
                _rlist_ids.append({'list_id': int(list_id) if list_id not in EMPTY_VALUE else idx,
                                   'data_file_name': get_first_sf_tag(sf, 'Data_file_name')})
            for sf in self._reg.star_data[0].get_saveframes_by_category('assembly'):
                try:
                    lp = sf.get_loop('_Entity_assembly')
                    has_pdb_chain_id = 'PDB_chain_ID' in lp.tags
                    if has_pdb_chain_id:
                        tags = ['ID', 'Entity_ID', 'PDB_chain_ID']
                        data = lp.get_tag(tags)
                        for row in data:
                            entity_assembly_id = row[0] if isinstance(row[0], str) else str(row[0])
                            entity_id = row[1] if isinstance(row[1], int) else int(row[1]) if row[1].isdigit() else None
                            pdb_chain_id = row[2].split(',')[0]
                            if entity_assembly is None:
                                entity_assembly = {}
                            entity_assembly[entity_assembly_id] = {'entity_id': entity_id, 'auth_asym_id': pdb_chain_id}
                    else:
                        tags = ['ID', 'Entity_ID']
                        data = lp.get_tag(tags)
                        for row in data:
                            entity_assembly_id = row[0] if isinstance(row[0], str) else str(row[0])
                            entity_id = row[1] if isinstance(row[1], int) else int(row[1]) if row[1].isdigit() else None
                            if entity_assembly is None:
                                entity_assembly = {}
                            entity_assembly[entity_assembly_id] = {'entity_id': entity_id, 'auth_asym_id': None}
                except KeyError:
                    pass

        if self._reg.caC is not None:
            nmr_poly_seq = copy.deepcopy(self._reg.caC['polymer_sequence'])
            if self._reg.caC['branched'] is not None:
                nmr_poly_seq.extend(self._reg.caC['branched'])
            if self._reg.caC['non_polymer'] is not None:
                nmr_poly_seq.extend(self._reg.caC['non_polymer'])
            entity_assembly = {}
            for item in self._reg.caC['entity_assembly']:
                _auth_asym_id = 'auth_asym_id' if 'fixed_auth_asym_id' not in item else 'fixed_auth_asym_id'
                entity_assembly[str(item['entity_assembly_id'])] =\
                    {'entity_id': item['entity_id'],
                     'auth_asym_id': item[_auth_asym_id].split(',')[0]}

        create_sf_dict = True

        if self._reg.list_id_counter is None:
            self._reg.list_id_counter = {}

        cs_sf_dict_holder = {}

        suspended_errors_for_lazy_eval = []

        def deal_lexer_or_parser_error(a_cs_format_name, file_name, lexer_err_listener, parser_err_listener):
            _err = ''
            if lexer_err_listener is not None:
                messageList = lexer_err_listener.getMessageList()

                if messageList is not None:
                    for description in messageList:
                        _err = f"[Syntax error as {a_cs_format_name} file] "\
                               f"line {description['line_number']}:{description['column_position']} {description['message']}\n"
                        if 'input' in description:
                            enc = detect_encoding(description['input'])
                            is_not_ascii = False
                            if enc is not None and enc != 'ascii':
                                _err += f"{description['input']}\n".encode().decode('ascii', 'backslashreplace')
                                is_not_ascii = True
                            else:
                                _err += f"{description['input']}\n"
                            _err += f"{description['marker']}\n"
                            if is_not_ascii:
                                _err += f"[Unexpected text encoding] Encoding used in the above line is {enc!r} "\
                                    "and must be 'ascii'.\n"

            if parser_err_listener is not None and len(_err) == 0:
                messageList = parser_err_listener.getMessageList()

                if messageList is not None:
                    for description in messageList:
                        _err += f"[Syntax error as {a_cs_format_name} file] "\
                                f"line {description['line_number']}:{description['column_position']} {description['message']}\n"
                        if 'input' in description:
                            _err += f"{description['input']}\n"
                            _err += f"{description['marker']}\n"

            if len(_err) == 0:
                return False

            err = f"The assigned chemical shift file {file_name!r} looks like {a_cs_format_name} file. "\
                "Please re-upload the assigned chemical shift file.\n"\
                "The following issues need to be fixed before re-upload.\n" + _err[:-1]

            self._reg.report.error.appendDescription('format_issue',
                                                     {'file_name': file_name, 'description': err})

            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCs() ++ Error  - {file_name} {err}\n")

            return True

        def consume_suspended_message():

            if len(suspended_errors_for_lazy_eval) > 0:
                for msg in suspended_errors_for_lazy_eval:
                    for k, v in msg.items():
                        self._reg.report.error.appendDescription(k, v)
                suspended_errors_for_lazy_eval.clear()

        def deal_shi_warn_message(file_name, listener, ignore_error):

            if listener.warningMessage is not None:

                for warn in listener.warningMessage:

                    msg_dict = {'file_name': file_name, 'description': warn, 'inheritable': True}
                    if INCONSISTENT_RESTRAINT_WARNING_PAT.match(warn):
                        g = INCONSISTENT_RESTRAINT_WARNING_PAT.search(warn).groups()
                        if g not in EMPTY_VALUE:
                            msg_dict['sf_framecode'] = g[1]
                            msg_dict['description'] = warn.replace(f', {g[1]}', '')

                    if warn.startswith('[Concatenated sequence]'):
                        self._reg.report.warning.appendDescription('concatenated_sequence', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCs() ++ Warning  - {warn}\n")

                    elif warn.startswith('[Sequence mismatch]'):
                        # consume_suspended_message()

                        self._reg.report.error.appendDescription('sequence_mismatch', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCs() ++ Error  - {warn}\n")

                    elif warn.startswith('[Atom not found]'):
                        self._reg.report.error.appendDescription('atom_not_found', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCs() ++ Error  - {warn}\n")

                    elif warn.startswith('[Invalid atom nomenclature]'):
                        consume_suspended_message()

                        self._reg.report.error.appendDescription('invalid_atom_nomenclature', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCs() ++ Error  - {warn}\n")

                    elif warn.startswith('[Invalid atom selection]') or warn.startswith('[Invalid data]'):
                        consume_suspended_message()

                        self._reg.report.error.appendDescription('invalid_data', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCs() ++ ValueError  - {warn}\n")

                    elif warn.startswith('[Sequence mismatch warning]'):
                        self._reg.report.warning.appendDescription('sequence_mismatch', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCs() ++ Warning  - {warn}\n")

                        if SEQ_MISMATCH_WARNING_PAT.match(warn):
                            g = SEQ_MISMATCH_WARNING_PAT.search(warn).groups()
                            d = {'auth_chain_id': g[2],
                                 'auth_seq_id': int(g[0]),
                                 'auth_comp_id': g[1]}
                            if d not in self._reg.nmr_ext_poly_seq:
                                self._reg.nmr_ext_poly_seq.append(d)

                    elif warn.startswith('[Missing data]'):
                        self._reg.report.warning.appendDescription('missing_data', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCs() ++ Warning  - {warn}\n")

                    elif warn.startswith('[Range value error]') and not self._reg.remediation_mode:
                        # consume_suspended_message()

                        self._reg.report.warning.appendDescription('anomalous_chemical_shift', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCs() ++ Warning  - {warn}\n")

                    elif warn.startswith('[Range value warning]')\
                            or (warn.startswith('[Range value error]') and self._reg.remediation_mode):
                        self._reg.report.warning.appendDescription('unusual_chemical_shift', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCs() ++ Warning  - {warn}\n")

                    elif not ignore_error:
                        self._reg.report.error.appendDescription('internal_error',
                                                                 f"+{self.__class_name__}.validateLegacyCs() "
                                                                 "++ KeyError  - " + warn)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCs() ++ KeyError  - {warn}\n")

        def deal_shi_warn_message_for_lazy_eval(file_name, listener):

            if listener.warningMessage is not None:

                def_sf_framecode = ''
                for warn in listener.warningMessage:

                    if INCONSISTENT_RESTRAINT_WARNING_PAT.match(warn):
                        g = INCONSISTENT_RESTRAINT_WARNING_PAT.search(warn).groups()
                        if g[1] not in EMPTY_VALUE:
                            def_sf_framecode = g[1]
                            break

                for warn in listener.warningMessage:

                    msg_dict = {'file_name': file_name, 'description': warn, 'inheritable': True}
                    if INCONSISTENT_RESTRAINT_WARNING_PAT.match(warn):
                        g = INCONSISTENT_RESTRAINT_WARNING_PAT.search(warn).groups()
                        msg_dict['sf_framecode'] = g[1] if g[1] not in EMPTY_VALUE else def_sf_framecode
                        msg_dict['description'] = warn.replace(f', {g[1]}', '')

                    if warn.startswith('[Sequence mismatch]'):
                        suspended_errors_for_lazy_eval.append({'sequence_mismatch': msg_dict})

                    elif warn.startswith('[Atom not found]'):
                        if not self._reg.remediation_mode or 'Macromolecules page' not in warn:
                            suspended_errors_for_lazy_eval.append({'atom_not_found': msg_dict})

                    # elif warn.startswith('[Hydrogen not instantiated]'):
                    #     if self._reg.remediation_mode:
                    #         pass
                    #     else:
                    #         suspended_errors_for_lazy_eval.append({'hydrogen_not_instantiated': msg_dict})

                    # elif warn.startswith('[Coordinate issue]'):
                    #     suspended_errors_for_lazy_eval.append({'coordinate_issue': msg_dict})

                    # elif warn.startswith('[Invalid atom nomenclature]'):
                    #     suspended_errors_for_lazy_eval.append({'invalid_atom_nomenclature': msg_dict})

                    elif warn.startswith('[Invalid atom selection]') or warn.startswith('[Invalid data]'):
                        suspended_errors_for_lazy_eval.append({'invalid_data': msg_dict})

                    # elif warn.startswith('[Range value error]') and not self._reg.remediation_mode:
                    #     suspended_errors_for_lazy_eval.append({'anomalous_data': msg_dict})

        fileListId = self._reg.file_path_list_len

        for acs in self._reg.inputParamDict[AC_FILE_PATH_LIST_KEY]:
            file_path = acs['file_name']

            input_source = self._reg.report.input_sources[fileListId]
            input_source_dic = input_source.get()

            file_type = input_source_dic['file_type']

            ignore_error = False if 'ignore_error' not in input_source_dic else input_source_dic['ignore_error']

            fileListId += 1

            if file_type is None or (not file_type.startswith('nm-shi-') and file_type != 'nm-aux-xea'):
                continue

            if self._reg.remediation_mode and os.path.exists(self.testPathWithSuffix(file_path, '-ignored', True)):
                continue

            file_path = self.testPathWithSuffix(file_path, '-corrected')

            file_name = input_source_dic['file_name']

            original_file_name = None
            if 'original_file_name' in input_source_dic:
                if input_source_dic['original_file_name'] is not None:
                    original_file_name = os.path.basename(input_source_dic['original_file_name'])
            if original_file_name in EMPTY_VALUE:
                original_file_name = file_name

            reserved_list_ids = None
            if len(_rlist_ids) > 0:
                rlist_ids = [item['list_id'] for item in _rlist_ids if item['data_file_name'] != original_file_name]
                if len(rlist_ids) > 0:
                    reserved_list_ids = {content_subtype: rlist_ids}

            _cs_format_name = getChemShiftFormatName(file_type)
            cs_format_name = _cs_format_name.split()[0]
            a_cs_format_name = ('an ' if cs_format_name[0] in ('AINMX') else 'a ') + _cs_format_name

            suspended_errors_for_lazy_eval.clear()

            spec = LEGACY_CS_READERS.get(file_type)

            if spec is not None:
                skip, parsed, listener = self._parseLegacyCs(
                    spec, file_path, file_name, original_file_name, create_sf_dict,
                    reserved_list_ids, nmr_poly_seq, entity_assembly, a_cs_format_name,
                    deal_lexer_or_parser_error, deal_shi_warn_message_for_lazy_eval)

                if skip:
                    continue

                if parsed:
                    deal_shi_warn_message(file_name, listener, ignore_error)

                    poly_seq = listener.getPolymerSequence()
                    if poly_seq is not None:
                        input_source.setItemValue('polymer_sequence', poly_seq)

                    if create_sf_dict:
                        if len(listener.getContentSubtype()) == 0 and not ignore_error:
                            label = spec[1]
                            err = f"Failed to validate assigned chemical shift file ({label}) {file_name!r}."

                            self._reg.report.error.appendDescription('internal_error',
                                                                     f"+{self.__class_name__}.validateLegacyCs() "
                                                                     "++ Error  - " + err)

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.validateLegacyCs() ++ Error  - {err}\n")

                        self._reg.list_id_counter, sf_dict = listener.getSfDict()
                        if sf_dict is not None:
                            for k, v in sf_dict.items():
                                content_subtype = contentSubtypeOf(k[0])
                                if content_subtype not in cs_sf_dict_holder:
                                    cs_sf_dict_holder[content_subtype] = []
                                for sf in v:
                                    if sf not in cs_sf_dict_holder[content_subtype]:
                                        cs_sf_dict_holder[content_subtype].append(sf)

        if content_subtype in cs_sf_dict_holder and len(self._reg.star_data) > 0\
           and isinstance(self._reg.star_data[0], pynmrstar.Entry):
            master_entry = self._reg.star_data[0]

            for sf in cs_sf_dict_holder[content_subtype]:

                data_file_name = get_first_sf_tag(sf['saveframe'], 'Data_file_name')

                if data_file_name not in EMPTY_VALUE:

                    _sf_list = master_entry.get_saveframes_by_tag_and_value('Data_file_name', data_file_name)

                    if len(_sf_list) == 1:

                        _sf = _sf_list[0]

                        try:

                            _lp = _sf.get_loop('_Atom_chem_shift')

                            del _sf[_lp]

                        except KeyError:
                            pass

                        _sf.add_loop(sf['loop'])

                    continue

                master_entry.add_saveframe(sf['saveframe'])

        return not self._reg.report.isError()

    def validateLegacyCsp(self) -> bool:
        """ Validate data content of legacy NMR chemical shift perturbation files and merge them if possible.
        """

        if not self._reg.combined_mode or not self._reg.conversion_server:
            return True

        if AC_FILE_PATH_LIST_KEY not in self._reg.inputParamDict:
            return True

        input_source = self._reg.report.input_sources[0]
        input_source_dic = input_source.get()

        has_poly_seq = has_key_value(input_source_dic, 'polymer_sequence')

        if not has_poly_seq:
            return False

        nmr_poly_seq = input_source_dic['polymer_sequence']
        entity_assembly = None

        file_type = 'nmr-star'
        content_subtype = 'csp_restraint'

        sf_category = SF_CATEGORIES[file_type][content_subtype]

        _rlist_ids = []
        if len(self._reg.star_data) > 0 and isinstance(self._reg.star_data[0], pynmrstar.Entry):
            for idx, sf in enumerate(self._reg.star_data[0].get_saveframes_by_category(sf_category), start=1):
                list_id = get_first_sf_tag(sf, 'ID')
                _rlist_ids.append({'list_id': int(list_id) if list_id not in EMPTY_VALUE else idx,
                                   'data_file_name': get_first_sf_tag(sf, 'Data_file_name')})
            for sf in self._reg.star_data[0].get_saveframes_by_category('assembly'):
                try:
                    lp = sf.get_loop('_Entity_assembly')
                    has_pdb_chain_id = 'PDB_chain_ID' in lp.tags
                    if has_pdb_chain_id:
                        tags = ['ID', 'Entity_ID', 'PDB_chain_ID']
                        data = lp.get_tag(tags)
                        for row in data:
                            entity_assembly_id = row[0] if isinstance(row[0], str) else str(row[0])
                            entity_id = row[1] if isinstance(row[1], int) else int(row[1]) if row[1].isdigit() else None
                            pdb_chain_id = row[2].split(',')[0]
                            if entity_assembly is None:
                                entity_assembly = {}
                            entity_assembly[entity_assembly_id] = {'entity_id': entity_id, 'auth_asym_id': pdb_chain_id}
                    else:
                        tags = ['ID', 'Entity_ID']
                        data = lp.get_tag(tags)
                        for row in data:
                            entity_assembly_id = row[0] if isinstance(row[0], str) else str(row[0])
                            entity_id = row[1] if isinstance(row[1], int) else int(row[1]) if row[1].isdigit() else None
                            if entity_assembly is None:
                                entity_assembly = {}
                            entity_assembly[entity_assembly_id] = {'entity_id': entity_id, 'auth_asym_id': None}
                except KeyError:
                    pass

        if self._reg.caC is not None:
            nmr_poly_seq = copy.deepcopy(self._reg.caC['polymer_sequence'])
            if self._reg.caC['branched'] is not None:
                nmr_poly_seq.extend(self._reg.caC['branched'])
            if self._reg.caC['non_polymer'] is not None:
                nmr_poly_seq.extend(self._reg.caC['non_polymer'])
            entity_assembly = {}
            for item in self._reg.caC['entity_assembly']:
                _auth_asym_id = 'auth_asym_id' if 'fixed_auth_asym_id' not in item else 'fixed_auth_asym_id'
                entity_assembly[str(item['entity_assembly_id'])] =\
                    {'entity_id': item['entity_id'],
                     'auth_asym_id': item[_auth_asym_id].split(',')[0]}

        create_sf_dict = True

        if self._reg.list_id_counter is None:
            self._reg.list_id_counter = {}

        cs_sf_dict_holder = {}

        suspended_errors_for_lazy_eval = []

        def deal_lexer_or_parser_error(a_cs_format_name, file_name, lexer_err_listener, parser_err_listener):
            _err = ''
            if lexer_err_listener is not None:
                messageList = lexer_err_listener.getMessageList()

                if messageList is not None:
                    for description in messageList:
                        _err = f"[Syntax error as {a_cs_format_name} file] "\
                               f"line {description['line_number']}:{description['column_position']} {description['message']}\n"
                        if 'input' in description:
                            enc = detect_encoding(description['input'])
                            is_not_ascii = False
                            if enc is not None and enc != 'ascii':
                                _err += f"{description['input']}\n".encode().decode('ascii', 'backslashreplace')
                                is_not_ascii = True
                            else:
                                _err += f"{description['input']}\n"
                            _err += f"{description['marker']}\n"
                            if is_not_ascii:
                                _err += f"[Unexpected text encoding] Encoding used in the above line is {enc!r} "\
                                    "and must be 'ascii'.\n"

            if parser_err_listener is not None and len(_err) == 0:
                messageList = parser_err_listener.getMessageList()

                if messageList is not None:
                    for description in messageList:
                        _err += f"[Syntax error as {a_cs_format_name} file] "\
                                f"line {description['line_number']}:{description['column_position']} {description['message']}\n"
                        if 'input' in description:
                            _err += f"{description['input']}\n"
                            _err += f"{description['marker']}\n"

            if len(_err) == 0:
                return False

            err = f"The assigned chemical shift file {file_name!r} looks like {a_cs_format_name} file. "\
                "Please re-upload the assigned chemical shift file.\n"\
                "The following issues need to be fixed before re-upload.\n" + _err[:-1]

            self._reg.report.error.appendDescription('format_issue',
                                                     {'file_name': file_name, 'description': err})

            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCsp() ++ Error  - {file_name} {err}\n")

            return True

        def consume_suspended_message():

            if len(suspended_errors_for_lazy_eval) > 0:
                for msg in suspended_errors_for_lazy_eval:
                    for k, v in msg.items():
                        self._reg.report.error.appendDescription(k, v)
                suspended_errors_for_lazy_eval.clear()

        def deal_shi_warn_message(file_name, listener, ignore_error):

            if listener.warningMessage is not None:

                for warn in listener.warningMessage:

                    msg_dict = {'file_name': file_name, 'description': warn, 'inheritable': True}
                    if INCONSISTENT_RESTRAINT_WARNING_PAT.match(warn):
                        g = INCONSISTENT_RESTRAINT_WARNING_PAT.search(warn).groups()
                        if g not in EMPTY_VALUE:
                            msg_dict['sf_framecode'] = g[1]
                            msg_dict['description'] = warn.replace(f', {g[1]}', '')

                    if warn.startswith('[Concatenated sequence]'):
                        self._reg.report.warning.appendDescription('concatenated_sequence', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCsp() ++ Warning  - {warn}\n")

                    elif warn.startswith('[Sequence mismatch]'):
                        # consume_suspended_message()

                        self._reg.report.error.appendDescription('sequence_mismatch', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCsp() ++ Error  - {warn}\n")

                    elif warn.startswith('[Atom not found]'):
                        self._reg.report.error.appendDescription('atom_not_found', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCsp() ++ Error  - {warn}\n")

                    elif warn.startswith('[Invalid atom nomenclature]'):
                        consume_suspended_message()

                        self._reg.report.error.appendDescription('invalid_atom_nomenclature', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCsp() ++ Error  - {warn}\n")

                    elif warn.startswith('[Invalid atom selection]') or warn.startswith('[Invalid data]'):
                        consume_suspended_message()

                        self._reg.report.error.appendDescription('invalid_data', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCsp() ++ ValueError  - {warn}\n")

                    elif warn.startswith('[Sequence mismatch warning]'):
                        self._reg.report.warning.appendDescription('sequence_mismatch', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCsp() ++ Warning  - {warn}\n")

                        if SEQ_MISMATCH_WARNING_PAT.match(warn):
                            g = SEQ_MISMATCH_WARNING_PAT.search(warn).groups()
                            d = {'auth_chain_id': g[2],
                                 'auth_seq_id': int(g[0]),
                                 'auth_comp_id': g[1]}
                            if d not in self._reg.nmr_ext_poly_seq:
                                self._reg.nmr_ext_poly_seq.append(d)

                    elif warn.startswith('[Missing data]'):
                        self._reg.report.warning.appendDescription('missing_data', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCsp() ++ Warning  - {warn}\n")

                    elif warn.startswith('[Range value error]') and not self._reg.remediation_mode:
                        # consume_suspended_message()

                        self._reg.report.warning.appendDescription('anomalous_chemical_shift', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCsp() ++ Warning  - {warn}\n")

                    elif warn.startswith('[Range value warning]')\
                            or (warn.startswith('[Range value error]') and self._reg.remediation_mode):
                        self._reg.report.warning.appendDescription('unusual_chemical_shift', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCsp() ++ Warning  - {warn}\n")

                    elif not ignore_error:
                        self._reg.report.error.appendDescription('internal_error',
                                                                 f"+{self.__class_name__}.validateLegacyCsp() "
                                                                 "++ KeyError  - " + warn)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateLegacyCsp() ++ KeyError  - {warn}\n")

        def deal_shi_warn_message_for_lazy_eval(file_name, listener):

            if listener.warningMessage is not None:

                def_sf_framecode = ''
                for warn in listener.warningMessage:

                    if INCONSISTENT_RESTRAINT_WARNING_PAT.match(warn):
                        g = INCONSISTENT_RESTRAINT_WARNING_PAT.search(warn).groups()
                        if g[1] not in EMPTY_VALUE:
                            def_sf_framecode = g[1]
                            break

                for warn in listener.warningMessage:

                    msg_dict = {'file_name': file_name, 'description': warn, 'inheritable': True}
                    if INCONSISTENT_RESTRAINT_WARNING_PAT.match(warn):
                        g = INCONSISTENT_RESTRAINT_WARNING_PAT.search(warn).groups()
                        msg_dict['sf_framecode'] = g[1] if g[1] not in EMPTY_VALUE else def_sf_framecode
                        msg_dict['description'] = warn.replace(f', {g[1]}', '')

                    if warn.startswith('[Sequence mismatch]'):
                        suspended_errors_for_lazy_eval.append({'sequence_mismatch': msg_dict})

                    elif warn.startswith('[Atom not found]'):
                        if not self._reg.remediation_mode or 'Macromolecules page' not in warn:
                            suspended_errors_for_lazy_eval.append({'atom_not_found': msg_dict})

                    # elif warn.startswith('[Hydrogen not instantiated]'):
                    #     if self._reg.remediation_mode:
                    #         pass
                    #     else:
                    #         suspended_errors_for_lazy_eval.append({'hydrogen_not_instantiated': msg_dict})

                    # elif warn.startswith('[Coordinate issue]'):
                    #     suspended_errors_for_lazy_eval.append({'coordinate_issue': msg_dict})

                    # elif warn.startswith('[Invalid atom nomenclature]'):
                    #     suspended_errors_for_lazy_eval.append({'invalid_atom_nomenclature': msg_dict})

                    elif warn.startswith('[Invalid atom selection]') or warn.startswith('[Invalid data]'):
                        suspended_errors_for_lazy_eval.append({'invalid_data': msg_dict})

                    # elif warn.startswith('[Range value error]') and not self._reg.remediation_mode:
                    #     suspended_errors_for_lazy_eval.append({'anomalous_data': msg_dict})

        csLoops = self._reg.lp_data['chem_shift']

        fileListId = self._reg.file_path_list_len

        for acs in self._reg.inputParamDict[AC_FILE_PATH_LIST_KEY]:
            file_path = acs['file_name']

            input_source = self._reg.report.input_sources[fileListId]
            input_source_dic = input_source.get()

            file_type = input_source_dic['file_type']

            ignore_error = False if 'ignore_error' not in input_source_dic else input_source_dic['ignore_error']

            fileListId += 1

            if file_type is None or not file_type.startswith('nm-csp-'):
                continue

            if self._reg.remediation_mode and os.path.exists(self.testPathWithSuffix(file_path, '-ignored', True)):
                continue

            file_path = self.testPathWithSuffix(file_path, '-corrected')

            file_name = input_source_dic['file_name']

            original_file_name = None
            if 'original_file_name' in input_source_dic:
                if input_source_dic['original_file_name'] is not None:
                    original_file_name = os.path.basename(input_source_dic['original_file_name'])
            if original_file_name in EMPTY_VALUE:
                original_file_name = file_name

            reserved_list_ids = None
            if len(_rlist_ids) > 0:
                rlist_ids = [item['list_id'] for item in _rlist_ids if item['data_file_name'] != original_file_name]
                if len(rlist_ids) > 0:
                    reserved_list_ids = {content_subtype: rlist_ids}

            _cs_format_name = getChemShiftFormatName(file_type)
            cs_format_name = _cs_format_name.split()[0]
            a_cs_format_name = ('an ' if cs_format_name[0] in ('AINMX') else 'a ') + _cs_format_name

            suspended_errors_for_lazy_eval.clear()

            spec = LEGACY_CSP_READERS.get(file_type)

            if spec is not None:
                skip, parsed, listener = self._parseLegacyCs(
                    spec, file_path, file_name, original_file_name, create_sf_dict,
                    reserved_list_ids, nmr_poly_seq, entity_assembly, a_cs_format_name,
                    deal_lexer_or_parser_error, deal_shi_warn_message_for_lazy_eval,
                    csp_mode=True, cs_loops=csLoops)

                if skip:
                    continue

                if parsed:
                    deal_shi_warn_message(file_name, listener, ignore_error)

                    poly_seq = listener.getPolymerSequence()
                    if poly_seq is not None:
                        input_source.setItemValue('polymer_sequence', poly_seq)

                    if create_sf_dict:
                        if len(listener.getContentSubtype()) == 0 and not ignore_error:
                            label = spec[1]
                            err = f"Failed to validate assigned chemical shift file ({label}) {file_name!r}."

                            self._reg.report.error.appendDescription('internal_error',
                                                                     f"+{self.__class_name__}.validateLegacyCsp() "
                                                                     "++ Error  - " + err)

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.validateLegacyCsp() ++ Error  - {err}\n")

                        self._reg.list_id_counter, sf_dict = listener.getSfDict()
                        if sf_dict is not None:
                            for k, v in sf_dict.items():
                                content_subtype = contentSubtypeOf(k[0])
                                if content_subtype not in cs_sf_dict_holder:
                                    cs_sf_dict_holder[content_subtype] = []
                                for sf in v:
                                    if sf not in cs_sf_dict_holder[content_subtype]:
                                        cs_sf_dict_holder[content_subtype].append(sf)

        if content_subtype in cs_sf_dict_holder and len(self._reg.star_data) > 0\
           and isinstance(self._reg.star_data[0], pynmrstar.Entry):
            master_entry = self._reg.star_data[0]

            for sf in cs_sf_dict_holder[content_subtype]:

                data_file_name = get_first_sf_tag(sf['saveframe'], 'Data_file_name')

                if data_file_name not in EMPTY_VALUE:

                    _sf_list = master_entry.get_saveframes_by_tag_and_value('Data_file_name', data_file_name)

                    if len(_sf_list) == 1:

                        _sf = _sf_list[0]

                        try:

                            _lp = _sf.get_loop('_Chem_shift_perturbation')

                            del _sf[_lp]

                        except KeyError:
                            pass

                        _sf.add_loop(sf['loop'])

                    continue

                master_entry.add_saveframe(sf['saveframe'])

        return not self._reg.report.isError()
