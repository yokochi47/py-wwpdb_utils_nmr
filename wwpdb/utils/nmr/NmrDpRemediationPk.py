##
# File: NmrDpRemediationPk.py
# Date: 17-Aug-2026
#
# Updates:
##
""" Remediation of spectral peak lists of NMR data.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.3"

import copy
import os
from operator import itemgetter
from typing import List, Optional, Tuple

import pynmrstar

try:
    from wwpdb.utils.nmr.NmrDpConstant import (MR_FILE_PATH_LIST_KEY,
                                               AR_FILE_PATH_LIST_KEY,
                                               PK_CONTENT_SUBTYPES,
                                               SF_CATEGORIES,
                                               SF_TAG_PREFIXES,
                                               EMPTY_VALUE,
                                               SEQ_MISMATCH_WARNING_PAT)
    from wwpdb.utils.nmr.NmrDpMrSplitter import (get_peak_list_format,
                                                 get_number_of_dimensions_of_peak_list)
    from wwpdb.utils.nmr.AlignUtil import (getScoreOfSeqAlign,
                                           updatePolySeqRst,
                                           sortPolySeqRst,
                                           alignPolymerSequence,
                                           assignPolymerSequence,
                                           trimSequenceAlignment)
    from wwpdb.utils.nmr.CifToNmrStar import (get_first_sf_tag,
                                              set_sf_tag)
    from wwpdb.utils.nmr.mr.ParserListenerUtil import contentSubtypeOf
    from wwpdb.utils.nmr.pk.AriaPKReader import AriaPKReader
    from wwpdb.utils.nmr.pk.BarePKReader import BarePKReader
    from wwpdb.utils.nmr.pk.CcpnPKReader import CcpnPKReader
    from wwpdb.utils.nmr.pk.OliviaPKReader import OliviaPKReader
    from wwpdb.utils.nmr.pk.NmrPipePKReader import NmrPipePKReader
    from wwpdb.utils.nmr.pk.PonderosaPKReader import PonderosaPKReader
    from wwpdb.utils.nmr.pk.NmrViewPKReader import NmrViewPKReader
    from wwpdb.utils.nmr.pk.SparkyPKReader import SparkyPKReader
    from wwpdb.utils.nmr.pk.SparkySPKReader import SparkySPKReader
    from wwpdb.utils.nmr.pk.TopSpinPKReader import TopSpinPKReader
    from wwpdb.utils.nmr.pk.VnmrPKReader import VnmrPKReader
    from wwpdb.utils.nmr.pk.XeasyPKReader import XeasyPKReader
    from wwpdb.utils.nmr.pk.XwinNmrPKReader import XwinNmrPKReader
    from wwpdb.utils.nmr.NmrDpRemediationBase import (NmrDpRemediationBase,
                                                      get_chem_shift_format)
except ImportError:
    from nmr.NmrDpConstant import (MR_FILE_PATH_LIST_KEY,
                                   AR_FILE_PATH_LIST_KEY,
                                   PK_CONTENT_SUBTYPES,
                                   SF_CATEGORIES,
                                   SF_TAG_PREFIXES,
                                   EMPTY_VALUE,
                                   SEQ_MISMATCH_WARNING_PAT)
    from nmr.NmrDpMrSplitter import (get_peak_list_format,
                                     get_number_of_dimensions_of_peak_list)
    from nmr.AlignUtil import (getScoreOfSeqAlign,
                               updatePolySeqRst,
                               sortPolySeqRst,
                               alignPolymerSequence,
                               assignPolymerSequence,
                               trimSequenceAlignment)
    from nmr.CifToNmrStar import (get_first_sf_tag,
                                  set_sf_tag)
    from nmr.mr.ParserListenerUtil import contentSubtypeOf
    from nmr.pk.AriaPKReader import AriaPKReader
    from nmr.pk.BarePKReader import BarePKReader
    from nmr.pk.CcpnPKReader import CcpnPKReader
    from nmr.pk.OliviaPKReader import OliviaPKReader
    from nmr.pk.NmrPipePKReader import NmrPipePKReader
    from nmr.pk.PonderosaPKReader import PonderosaPKReader
    from nmr.pk.NmrViewPKReader import NmrViewPKReader
    from nmr.pk.SparkyPKReader import SparkyPKReader
    from nmr.pk.SparkySPKReader import SparkySPKReader
    from nmr.pk.TopSpinPKReader import TopSpinPKReader
    from nmr.pk.VnmrPKReader import VnmrPKReader
    from nmr.pk.XeasyPKReader import XeasyPKReader
    from nmr.pk.XwinNmrPKReader import XwinNmrPKReader
    from nmr.NmrDpRemediationBase import (NmrDpRemediationBase,
                                          get_chem_shift_format)


# Reader dispatch for remediateRawTextPk(), one entry per raw text peak list
# file type. 'reader' and 'label' are required; the remaining keys record the
# only genuine per-format deviations from the common parse/re-parse sequence:
#
#   extra_args             extra positional arguments appended after nefT
#                          (XEASY takes an additional None)
#   cs_loops               whether parse() is given csLoops (default True)
#   reparse_needs_warning  whether re-parsing additionally requires the
#                          listener to have emitted warning messages
PK_READERS = {
    'nm-pea-ari': {'reader': AriaPKReader, 'label': 'ARIA'},
    'nm-pea-bar': {'reader': BarePKReader, 'label': 'Bare WSV/TSV'},
    'nm-pea-ccp': {'reader': CcpnPKReader, 'label': 'CCPN'},
    'nm-pea-oli': {'reader': OliviaPKReader, 'label': 'OLIVIA'},
    'nm-pea-pip': {'reader': NmrPipePKReader, 'label': 'NMRPIPE'},
    'nm-pea-pon': {'reader': PonderosaPKReader, 'label': 'PONDEROSA'},
    'nm-pea-spa': {'reader': SparkyPKReader, 'label': 'SPARKY'},
    'nm-pea-sps': {'reader': SparkySPKReader, 'label': 'SPARKY'},
    'nm-pea-top': {'reader': TopSpinPKReader, 'label': 'TOPSPIN',
                   'cs_loops': False},
    'nm-pea-vie': {'reader': NmrViewPKReader, 'label': 'NMRVIEW'},
    'nm-pea-vnm': {'reader': VnmrPKReader, 'label': 'VNMR'},
    'nm-pea-xea': {'reader': XeasyPKReader, 'label': 'XEASY',
                   'extra_args': (None,), 'reparse_needs_warning': True},
    'nm-pea-xwi': {'reader': XwinNmrPKReader, 'label': 'XWINNMR',
                   'cs_loops': False},
}


class NmrDpRemediationPk(NmrDpRemediationBase):
    """ Remediation of spectral peak lists of NMR data.
    """
    __slots__ = ()

    def _parseRawTextPk(self, spec: dict, data_file_name: str, text_data: str,
                        reserved_list_ids: List[int], deal_warn_for_lazy_eval
                        ) -> Tuple[bool, Optional[object]]:
        """ Parse raw text spectral peak list data with the reader for a given file type,
            re-parsing once if the parser listener asks for it.
            @param spec: the PK_READERS entry for the file type
            @param deal_warn_for_lazy_eval: callback invoked before re-parsing
            @return: (whether the initial parse yielded a listener, the final listener).
                     The two are reported separately because the caller's processing is
                     gated on the initial parse, exactly as the per-format branches were.
        """
        reader_cls = spec['reader']
        extra_args = spec.get('extra_args', ())

        def new_reader(*trailing):
            reader = reader_cls(self._reg.verbose, self._reg.log,
                                self._reg.representative_model_id,
                                self._reg.representative_alt_id,
                                self._reg.mr_atom_name_mapping,
                                self._reg.cR, self._reg.caC,
                                self._reg.ccU, self._reg.csStat, self._reg.nefT,
                                *extra_args, *trailing)
            reader.enforcePeakRowFormat(self._reg.enforce_peak_row_format)
            reader.setInternalMode(self._reg.internal_mode)
            return reader

        def parse_with(reader, list_id_counter):
            kwargs = {'listIdCounter': list_id_counter,
                      'reservedListIds': reserved_list_ids,
                      'entryId': self._reg.entry_id}
            if spec.get('cs_loops', True):
                kwargs['csLoops'] = self._reg.lp_data['chem_shift']
            return reader.parse(text_data, self._reg.cifPath, isFilePath=False,
                                createSfDict=True, originalFileName=data_file_name,
                                **kwargs)[0]

        _list_id_counter = copy.copy(self._reg.list_id_counter)

        listener = parse_with(new_reader(), self._reg.list_id_counter)

        if listener is None:
            return False, None

        reasons = listener.getReasonsForReparsing()

        reparse = reasons is not None
        if reparse and spec.get('reparse_needs_warning', False):
            reparse = listener.warningMessage is not None and len(listener.warningMessage) > 0

        if reparse:
            deal_warn_for_lazy_eval(data_file_name, listener)

            listener = parse_with(new_reader(reasons), _list_id_counter)

        return True, listener

    def remediateRawTextPk(self, src_sf: pynmrstar.Saveframe, file_type: str, data_file_name: str, text_data: str,
                           reserved_list_ids: List[int]) -> bool:
        """ Remediate raw text data in saveframe of spectral peak list (for NMR data remediation upgrade to Phase 2).
        """

        __errors = self._reg.report.getTotalErrors()

        input_source = self._reg.report.input_sources[0]

        content_subtype = 'spectral_peak'

        sf_framecode = get_first_sf_tag(src_sf, 'Sf_framecode')

        poly_seq_set = []

        if self._reg.list_id_counter is None:
            self._reg.list_id_counter = {}

        pk_sf_dict_holder = {}

        proc_nmr_ext_poly_seq = False

        if self._reg.nmr_ext_poly_seq is None and not self._reg.bmrb_only or not self._reg.internal_mode:
            proc_nmr_ext_poly_seq = True

            self._reg.nmr_ext_poly_seq = []

            input_source_dic = input_source.get()

            nmr_poly_seq = input_source_dic['polymer_sequence']
            cif_poly_seq = self._reg.caC['polymer_sequence']

            seq_align, _ = alignPolymerSequence(self._reg.pA, cif_poly_seq, nmr_poly_seq)
            chain_assign, _ = assignPolymerSequence(self._reg.pA, self._reg.ccU, 'nmr-star',
                                                    cif_poly_seq, nmr_poly_seq, seq_align)

            if chain_assign is not None:

                for ca in chain_assign:
                    ref_chain_id = ca['ref_chain_id']
                    test_chain_id = ca['test_chain_id']

                    sa = next(sa for sa in seq_align
                              if sa['ref_chain_id'] == ref_chain_id
                              and sa['test_chain_id'] == test_chain_id)

                    if sa['conflict'] > 0 or sa['unmapped'] == 0:
                        continue

                    ps1 = next(ps for ps in nmr_poly_seq if ps['chain_id'] == test_chain_id)
                    ps2 = next(ps for ps in cif_poly_seq if ps['auth_chain_id'] == ref_chain_id)

                    self._reg.pA.clear()
                    self._reg.pA.setReferenceSequence(ps1['comp_id'], f'REF{test_chain_id}')
                    self._reg.pA.addTestSequence(ps2['comp_id'], test_chain_id)
                    self._reg.pA.doAlign()

                    myAlign = self._reg.pA.getAlignment(test_chain_id)

                    length = len(myAlign)

                    _matched, unmapped, conflict, offset_1, offset_2 = getScoreOfSeqAlign(myAlign)

                    if conflict == 0 and unmapped > 0:

                        nmr_seq_ids, cif_auth_seq_ids = [], []

                        for i in range(length):
                            if str(myAlign[i][0]) != '.' and i < len(ps1['seq_id']):
                                nmr_seq_ids.append(ps1['seq_id'][i])
                            else:
                                nmr_seq_ids.append(None)

                        for i in range(length):
                            if str(myAlign[i][1]) != '.' and i < len(ps2['seq_id']):
                                cif_auth_seq_ids.append(ps2['auth_seq_id'][i])
                            else:
                                cif_auth_seq_ids.append(None)

                        for i in range(length):
                            nmr_comp_id, cif_comp_id = str(myAlign[i][0]), str(myAlign[i][1])

                            if nmr_comp_id == cif_comp_id:
                                continue

                            if cif_comp_id == '.' and nmr_comp_id != '.':
                                nmr_seq_id = nmr_seq_ids[i] - offset_1 if nmr_seq_ids[i] is not None else None
                                if nmr_seq_id is not None:
                                    offset = None
                                    for _offset in range(1, 20):
                                        if i + _offset < length:
                                            _myPr = myAlign[i + _offset]
                                            if _myPr[0] == _myPr[1]:
                                                offset = _offset
                                                break
                                        if i - _offset >= 0:
                                            _myPr = myAlign[i - _offset]
                                            if _myPr[0] == _myPr[1]:
                                                offset = -_offset
                                                break

                                    if offset is not None and cif_auth_seq_ids[i + offset] is not None:
                                        cif_auth_seq_id = cif_auth_seq_ids[i + offset] - offset - offset_2
                                        self._reg.nmr_ext_poly_seq.append({'auth_chain_id': ps2['auth_chain_id'],
                                                                           'auth_seq_id': cif_auth_seq_id,
                                                                           'auth_comp_id': nmr_comp_id})

        suspended_errors_for_lazy_eval = []

        def consume_suspended_message():

            if len(suspended_errors_for_lazy_eval) > 0:
                for msg in suspended_errors_for_lazy_eval:
                    for k, v in msg.items():
                        self._reg.report.error.appendDescription(k, v)
                suspended_errors_for_lazy_eval.clear()

        def deal_pea_warn_message(file_name, listener):

            if listener.warningMessage is not None:

                for warn in listener.warningMessage:

                    msg_dict = {'file_name': file_name, 'sf_framecode': sf_framecode, 'description': warn, 'inheritable': True}

                    if warn.startswith('[Concatenated sequence]'):
                        self._reg.report.warning.appendDescription('concatenated_sequence', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.remediateRawTextPk() ++ Warning  - {warn}\n")

                    elif warn.startswith('[Sequence mismatch]'):
                        # consume_suspended_message()

                        self._reg.report.error.appendDescription('sequence_mismatch', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.remediateRawTextPk() ++ Error  - {warn}\n")

                    elif warn.startswith('[Atom not found]'):
                        if not self._reg.remediation_mode or 'Macromolecules page' not in warn:
                            consume_suspended_message()

                            self._reg.report.warning.appendDescription('assigned_peak_atom_not_found', msg_dict)

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.remediateRawTextPk() ++ Warning  - {warn}\n")
                        else:
                            self._reg.report.warning.appendDescription('sequence_mismatch', msg_dict)

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.remediateRawTextPk() ++ Warning  - {warn}\n")

                    elif warn.startswith('[Hydrogen not instantiated]'):
                        if self._reg.remediation_mode:
                            pass
                        else:
                            consume_suspended_message()

                        self._reg.report.warning.appendDescription('hydrogen_not_instantiated', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.remediateRawTextPk() ++ Warning  - {warn}\n")

                    elif warn.startswith('[Coordinate issue]'):
                        # consume_suspended_message()

                        self._reg.report.warning.appendDescription('coordinate_issue', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.remediateRawTextPk() ++ Warning  - {warn}\n")

                    elif warn.startswith('[Invalid atom nomenclature]'):
                        consume_suspended_message()

                        # DAOTHER-8905: change warning level from 'invalid_atom_nomenclature' error
                        # to 'atom_nomenclature_mismatch' warning
                        # because we accept atom nomenclature provided by depositor for peak list
                        self._reg.report.warning.appendDescription('atom_nomenclature_mismatch', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.remediateRawTextPk() ++ Warning  - {warn}\n")

                    elif warn.startswith('[Invalid atom selection]') or warn.startswith('[Invalid data]'):
                        # consume_suspended_message()

                        self._reg.report.warning.appendDescription('inconsistent_peak_list', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.remediateRawTextPk() ++ Warning  - {warn}\n")

                    elif warn.startswith('[Sequence mismatch warning]'):
                        self._reg.report.warning.appendDescription('sequence_mismatch', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.remediateRawTextPk() ++ Warning  - {warn}\n")

                        if SEQ_MISMATCH_WARNING_PAT.match(warn):
                            g = SEQ_MISMATCH_WARNING_PAT.search(warn).groups()
                            d = {'auth_chain_id': g[2],
                                 'auth_seq_id': int(g[0]),
                                 'auth_comp_id': g[1]}
                            if d not in self._reg.nmr_ext_poly_seq:
                                self._reg.nmr_ext_poly_seq.append(d)

                    elif warn.startswith('[Inconsistent peak assignment]'):
                        self._reg.report.warning.appendDescription('inconsistent_peak_list', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.remediateRawTextPk() ++ Warning  - {warn}\n")

                    elif warn.startswith('[Conflicted peak assignment]'):
                        self._reg.report.warning.appendDescription('conflicted_peak_list', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.remediateRawTextPk() ++ Warning  - {warn}\n")

                    elif warn.startswith('[Missing data]'):
                        if (self._reg.remediation_mode or self._reg.internal_mode) and not self._reg.conversion_server:
                            pass
                        else:
                            self._reg.report.error.appendDescription('missing_mandatory_item', msg_dict)

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.remediateRawTextPk() ++ Error  - {warn}\n")

                    elif warn.startswith('[Range value error]') and not self._reg.remediation_mode:
                        # consume_suspended_message()

                        self._reg.report.error.appendDescription('anomalous_data', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.remediateRawTextPk() ++ ValueError  - {warn}\n")

                    elif warn.startswith('[Range value warning]')\
                            or (warn.startswith('[Range value error]') and self._reg.remediation_mode):
                        self._reg.report.warning.appendDescription('inconsistent_peak_list', msg_dict)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.remediateRawTextPk() ++ Warning  - {warn}\n")

                    else:
                        self._reg.report.error.appendDescription('internal_error',
                                                                 f"+{self.__class_name__}.remediateRawTextPk() "
                                                                 "++ KeyError  - " + warn)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.remediateRawTextPk() ++ KeyError  - {warn}\n")

        def deal_pea_warn_message_for_lazy_eval(file_name, listener):

            if listener.warningMessage is not None:

                for warn in listener.warningMessage:

                    msg_dict = {'file_name': file_name, 'sf_framecode': sf_framecode, 'description': warn, 'inheritable': True}

                    if warn.startswith('[Sequence mismatch]'):
                        suspended_errors_for_lazy_eval.append({'sequence_mismatch': msg_dict})

                    # elif warn.startswith('[Atom not found]'):
                    #     if not self._reg.remediation_mode or 'Macromolecules page' not in warn:
                    #         suspended_errors_for_lazy_eval.append({'atom_not_found': msg_dict})

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

        spec = PK_READERS.get(file_type)

        if spec is not None:
            parsed, listener = self._parseRawTextPk(spec, data_file_name, text_data,
                                                    reserved_list_ids,
                                                    deal_pea_warn_message_for_lazy_eval)

            if parsed:
                deal_pea_warn_message(data_file_name, listener)

                poly_seq = listener.getPolymerSequence()
                if poly_seq is not None:
                    input_source.setItemValue('polymer_sequence', poly_seq)
                    poly_seq_set.append(poly_seq)

                seq_align = listener.getSequenceAlignment()
                if seq_align is not None:
                    self._reg.report.sequence_alignment.setItemValue(f'model_poly_seq_vs_{content_subtype}', seq_align)

                if len(listener.getContentSubtype()) == 0:
                    err = f"Failed to validate spectral peak list file ({spec['label']}) {data_file_name!r}."

                    self._reg.report.error.appendDescription('internal_error',
                                                             f"+{self.__class_name__}.remediateRawTextPk() ++ Error  - " + err)

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.remediateRawTextPk() ++ Error  - {err}\n")

                self._reg.list_id_counter, sf_dict = listener.getSfDict()
                if sf_dict is not None:
                    for k, v in sf_dict.items():
                        content_subtype = contentSubtypeOf(k[0])
                        if content_subtype not in pk_sf_dict_holder:
                            pk_sf_dict_holder[content_subtype] = []
                        for sf in v:
                            if sf not in pk_sf_dict_holder[content_subtype]:
                                pk_sf_dict_holder[content_subtype].append(sf)

        if content_subtype in pk_sf_dict_holder:

            master_entry = self._reg.star_data[0]

            master_entry.remove_saveframe(sf_framecode)

            for sf in pk_sf_dict_holder[content_subtype]:

                cs_list = get_first_sf_tag(sf['saveframe'], 'Chemical_shift_list')

                if cs_list in EMPTY_VALUE:
                    sf_category = SF_CATEGORIES['nmr-star']['chem_shift']
                    cs_sf_list = master_entry.get_saveframes_by_category(sf_category)
                    if len(cs_sf_list) == 1:
                        set_sf_tag(sf['saveframe'], 'Chemical_shift_list', get_first_sf_tag(cs_sf_list[0], 'Sf_framecode'))

                master_entry.add_saveframe(sf['saveframe'])

        if len(poly_seq_set) > 1:

            poly_seq_rst = None
            for idx, poly_seq in enumerate(poly_seq_set):
                if idx == 0:
                    poly_seq_rst = poly_seq
                    continue
                for ps in poly_seq:
                    chain_id = ps['chain_id']
                    for seq_id, comp_id in zip(ps['seq_id'], ps['comp_id']):
                        updatePolySeqRst(poly_seq_rst, chain_id, seq_id, comp_id)

            poly_seq_model = self._reg.caC['polymer_sequence']

            sortPolySeqRst(poly_seq_rst)

            file_type = 'nm-pea-any'

            seq_align, _ = alignPolymerSequence(self._reg.pA, poly_seq_model, poly_seq_rst, conservative=False)
            chain_assign, _ = assignPolymerSequence(self._reg.pA, self._reg.ccU, file_type,
                                                    poly_seq_model, poly_seq_rst, seq_align)

            if chain_assign is not None:

                if len(poly_seq_model) == len(poly_seq_rst):

                    chain_mapping = {}

                    for ca in chain_assign:
                        ref_chain_id = ca['ref_chain_id']
                        test_chain_id = ca['test_chain_id']

                        if ref_chain_id != test_chain_id:
                            chain_mapping[test_chain_id] = ref_chain_id

                    if len(chain_mapping) == len(poly_seq_model):

                        for ps in poly_seq_rst:
                            if ps['chain_id'] in chain_mapping:
                                ps['chain_id'] = chain_mapping[ps['chain_id']]

                        seq_align, _ = alignPolymerSequence(self._reg.pA, poly_seq_model, poly_seq_rst, conservative=False)
                        chain_assign, _ = assignPolymerSequence(self._reg.pA, self._reg.ccU, file_type,
                                                                poly_seq_model, poly_seq_rst, seq_align)

                    trimSequenceAlignment(seq_align, chain_assign)

            input_source.setItemValue('polymer_sequence', poly_seq_rst)

            self._reg.report.sequence_alignment.setItemValue(f'model_poly_seq_vs_{content_subtype}', seq_align)

        if proc_nmr_ext_poly_seq and len(self._reg.nmr_ext_poly_seq) > 0:
            entity_assembly = self._reg.caC['entity_assembly']
            auth_chain_ids = list(set(d['auth_chain_id'] for d in self._reg.nmr_ext_poly_seq))
            for auth_chain_id in auth_chain_ids:
                try:
                    item = next(item for item in entity_assembly if auth_chain_id in item['auth_asym_id'].split(','))
                except StopIteration:
                    continue
                if item['entity_type'] == 'polymer':
                    poly_type = item['entity_poly_type']
                    if poly_type.startswith('polypeptide'):
                        unknown_residue = 'UNK'
                    elif any(True for comp_id in item['comp_id_set'] if comp_id in ('DA', 'DC', 'DG', 'DT'))\
                            and any(True for comp_id in item['comp_id_set'] if comp_id in ('A', 'C', 'G', 'U')):
                        unknown_residue = 'DN'
                    elif poly_type == 'polydeoxyribonucleotide':
                        unknown_residue = 'DN'
                    elif poly_type == 'polyribonucleotide':
                        unknown_residue = 'N'
                    else:
                        continue
                    ps = next(ps for ps in self._reg.caC['polymer_sequence'] if ps['auth_chain_id'] == auth_chain_id)
                    auth_seq_ids = [d['auth_seq_id'] for d in self._reg.nmr_ext_poly_seq if d['auth_chain_id'] == auth_chain_id]
                    auth_seq_ids.extend(list(filter(None, ps['auth_seq_id'])))
                    min_auth_seq_id = min(auth_seq_ids)
                    max_auth_seq_id = max(auth_seq_ids)
                    for auth_seq_id in range(min_auth_seq_id, max_auth_seq_id + 1):
                        if auth_seq_id not in ps['auth_seq_id']\
                           and not any(True for d in self._reg.nmr_ext_poly_seq
                                       if d['auth_chain_id'] == auth_chain_id and d['auth_seq_id'] == auth_seq_id):
                            self._reg.nmr_ext_poly_seq.append({'auth_chain_id': auth_chain_id,
                                                               'auth_seq_id': auth_seq_id,
                                                               'auth_comp_id': unknown_residue})

            self._reg.nmr_ext_poly_seq = sorted(self._reg.nmr_ext_poly_seq, key=itemgetter('auth_chain_id', 'auth_seq_id'))

        return self._reg.report.getTotalErrors() == __errors

    def remediateSpectralPeakListSaveframe(self, star_data: pynmrstar.Entry) -> None:
        """ Remediate spectral peak list saveframe
        """

        if not self._reg.bmrb_only:
            return

        sf_category = 'spectral_peak_list'

        sf_name_map = {}
        for idx, sf in enumerate(star_data.get_saveframes_by_category(sf_category), start=1):
            tagNames = [t[0] for t in sf.tags]
            if 'Text_data' in tagNames and get_first_sf_tag(sf, 'Text_data') in EMPTY_VALUE:
                # sf.remove_tag('Text_data')
                if 'Text_data_format' in tagNames:
                    set_sf_tag(sf, 'Text_data_format', '.')
                    # sf.remove_tag('Text_data_format')
            sf_id = get_first_sf_tag(sf, 'ID')
            if isinstance(sf_id, str):
                sf_id = int(sf_id) if len(sf_id) > 0 else idx
            sf_name_map[sf.name] = sf_id

        if not all(sf_name.split('_')[-1] == str(sf_id) for sf_name, sf_id in sf_name_map.items()):
            for sf in star_data.get_saveframes_by_category(sf_category):
                prefix_sf_name = '_'.join(sf.name.split('_')[:-1])
                sf.name = f'{prefix_sf_name}_{sf_name_map[sf.name]}'
                set_sf_tag(sf, 'Sf_framecode', sf.name)

        truncated = False
        for sf in star_data.get_saveframes_by_category(sf_category):

            lp_category = '_Peak_row_format'

            try:

                sf.get_loop(lp_category)
                continue

            except KeyError:

                lp_category = '_Peak_char'

                try:

                    sf.get_loop(lp_category)
                    continue

                except KeyError:
                    pass

            if get_first_sf_tag(sf, 'Text_data') in EMPTY_VALUE:
                star_data.remove_saveframe(sf.name)
                truncated = True

        if truncated:

            total_peak_lists = len(star_data.get_saveframes_by_category(sf_category))

            if total_peak_lists == 0:

                sf_category = 'entry_interview'

                if sf_category in self._reg.sf_category_list:

                    int_sf = star_data.get_saveframes_by_category(sf_category)[0]

                    set_sf_tag(int_sf, 'Spectral_peak_lists', '.')

            sf_category = 'entry_information'

            if sf_category in self._reg.sf_category_list:

                inf_sf = star_data.get_saveframes_by_category(sf_category)[0]

                lp_category = '_Data_set'

                try:

                    lp = inf_sf.get_loop(lp_category)

                    type_col = lp.tags.index('Type')
                    count_col = lp.tags.index('Count')

                    for idx, row in enumerate(lp):

                        if row[type_col] != 'spectral_peak_list':
                            continue

                        if total_peak_lists == 0:
                            del lp.data[idx]

                        else:
                            lp.data[idx][count_col] = total_peak_lists

                        break

                except KeyError:
                    pass

    def _mergeStrPk(self) -> bool:
        """ Merge spectral peak lists in NMR-STAR restraint files.
        """

        if self._reg.combined_mode:
            return True

        if MR_FILE_PATH_LIST_KEY not in self._reg.inputParamDict:
            return True

        if not self._reg.cifChecked:
            return False

        if self._reg.pk_sf_holder is None:
            self._reg.pk_sf_holder = []

        list_id = len(self._reg.pk_sf_holder) + 1

        master_entry = self._reg.star_data[0]

        for fileListId in range(self._reg.cs_file_path_list_len, self._reg.file_path_list_len):

            input_source = self._reg.report.input_sources[fileListId]
            input_source_dic = input_source.get()

            file_type = input_source_dic['file_type']
            content_subtype = input_source_dic['content_subtype']

            if file_type != 'nmr-star':
                continue

            if input_source_dic['content_subtype'] is None:
                continue

            for content_subtype in PK_CONTENT_SUBTYPES:

                if content_subtype not in input_source_dic['content_subtype']:
                    continue

                sf_category = SF_CATEGORIES[file_type][content_subtype]

                if self._reg.bmrb_only and self._reg.internal_mode and self._reg.nmr_cif_sf_category_list is not None:
                    if sf_category in self._reg.nmr_cif_sf_category_list:
                        continue

                if self._reg.star_data_type[fileListId] == 'Loop':
                    pass

                elif self._reg.star_data_type[fileListId] == 'Saveframe':
                    sf = self._reg.star_data[fileListId]

                    self._reg.c2S.set_entry_id(sf, self._reg.entry_id)
                    self._reg.c2S.set_local_sf_id(sf, list_id)

                    master_entry.add_saveframe(sf)

                    self._reg.pk_sf_holder.append({'file_type': 'nmr-star', 'saveframe': sf})

                    list_id += 1

                else:

                    for sf in self._reg.star_data[fileListId].get_saveframes_by_category(sf_category):

                        self._reg.c2S.set_entry_id(sf, self._reg.entry_id)
                        self._reg.c2S.set_local_sf_id(sf, list_id)

                        master_entry.add_saveframe(sf)

                        self._reg.pk_sf_holder.append({'file_type': 'nmr-star', 'saveframe': sf})

                        list_id += 1

        return True

    def _mergeAnyPkAsIs(self) -> bool:
        """ Merge spectral peak list file(s) in any plain text format (file type: nm-pea-any) into a single NMR-STAR file as-is.
        """

        if self._reg.combined_mode:
            return True

        if AR_FILE_PATH_LIST_KEY not in self._reg.inputParamDict:
            return True

        if self._reg.pk_sf_holder is None:
            self._reg.pk_sf_holder = []

        fileListId = self._reg.file_path_list_len

        list_id = len(self._reg.pk_sf_holder) + 1

        master_entry = self._reg.star_data[0]

        for ar in self._reg.inputParamDict[AR_FILE_PATH_LIST_KEY]:

            input_source = self._reg.report.input_sources[fileListId]
            input_source_dic = input_source.get()

            file_name = input_source_dic['file_name']
            file_type = input_source_dic['file_type']

            fileListId += 1

            if file_type != 'nm-pea-any':
                continue

            original_file_name = None
            if 'original_file_name' in input_source_dic:
                if input_source_dic['original_file_name'] is not None:
                    original_file_name = os.path.basename(input_source_dic['original_file_name'])

            file_path = ar['file_name']

            try:

                with open(file_path, 'r', encoding='utf-8') as ifh:
                    ifh.read()

            except UnicodeDecodeError:  # catch exception due to binary format (DAOTHER-9425)
                continue

            if get_chem_shift_format(file_path) is not None:

                err = "The spectral peak list file includes assigned chemical shifts."

                self._reg.report.error.appendDescription('content_mismatch',
                                                         {'file_name': file_name, 'description': err})

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.__mergeAnyPkAsIs() ++ Error  - {err}\n")

                continue

            content_subtype = 'spectral_peak'

            sf_category = SF_CATEGORIES['nmr-star'][content_subtype]
            sf_framecode = f'spectral_peak_list_{list_id}'

            if self._reg.bmrb_only and self._reg.internal_mode and self._reg.nmr_cif_sf_category_list is not None:
                if sf_category in self._reg.nmr_cif_sf_category_list:
                    continue

            try:

                sf = master_entry.get_saveframe_by_name(sf_framecode)
                text_data = get_first_sf_tag(sf, 'Text_data')

                if any(True for loop in sf.loops if loop.category in ('_Peak_row_format', '_Peak_general_char'))\
                        or text_data not in EMPTY_VALUE:

                    list_id += 1

                    continue

                file_format = get_peak_list_format(file_path, False)
                dimensions = get_number_of_dimensions_of_peak_list(file_path, file_format)

                set_sf_tag(sf, 'Number_of_spectral_dimensions', dimensions)

                _sf_id = _sf_framecode = None
                _sf_category = SF_CATEGORIES['nmr-star']['chem_shift']
                if len(master_entry.get_saveframes_by_category(_sf_category)) == 1:
                    _sf = master_entry.get_saveframes_by_category(_sf_category)[0]
                    _sf_id = get_first_sf_tag(_sf, 'ID')
                    _sf_framecode = f"${get_first_sf_tag(_sf, 'Sf_framecode')}"

                set_sf_tag(sf, 'Assigned_chem_shift_list_ID', _sf_id)
                set_sf_tag(sf, 'Assigned_chem_shift_list_label', _sf_framecode)

                set_sf_tag(sf, 'Text_data_format', file_format if file_format is not None else 'unknown')

                with open(file_path, 'r', encoding='ascii', errors='ignore') as ifh:
                    set_sf_tag(sf, 'Text_data', ifh.read())

                list_id += 1

            except KeyError:

                sf = pynmrstar.Saveframe.from_scratch(sf_framecode, SF_TAG_PREFIXES['nmr-star'][content_subtype])
                sf.add_tag('Sf_category', sf_category)
                sf.add_tag('Sf_framecode', sf_framecode)
                sf.add_tag('Entry_ID', self._reg.entry_id)
                sf.add_tag('ID', list_id)
                sf.add_tag('Data_file_name', original_file_name if original_file_name is not None else file_name)

                _sf_id = _sf_framecode = None
                _sf_category = 'sample'
                if len(master_entry.get_saveframes_by_category(_sf_category)) == 1:
                    _sf = master_entry.get_saveframes_by_category(_sf_category)[0]
                    _sf_id = get_first_sf_tag(_sf, 'ID')
                    _sf_framecode = f"${get_first_sf_tag(_sf, 'Sf_framecode')}"

                sf.add_tag('Sample_ID', _sf_id)
                sf.add_tag('Sample_label', _sf_framecode)

                _sf_id = _sf_framecode = None
                _sf_category = 'sample_conditions'
                if len(master_entry.get_saveframes_by_category(_sf_category)) == 1:
                    _sf = master_entry.get_saveframes_by_category(_sf_category)[0]
                    _sf_id = get_first_sf_tag(_sf, 'ID')
                    _sf_framecode = f"${get_first_sf_tag(_sf, 'Sf_framecode')}"

                sf.add_tag('Sample_condition_list_ID', _sf_id)
                sf.add_tag('Sample_condition_list_label', _sf_framecode)

                sf.add_tag('Experiment_ID', None)
                sf.add_tag('Experiment_name', None)
                sf.add_tag('Experiment_class', None)
                sf.add_tag('Experiment_type', None)

                file_format = get_peak_list_format(file_path, False)
                dimensions = get_number_of_dimensions_of_peak_list(file_path, file_format)

                sf.add_tag('Number_of_spectral_dimensions', dimensions)

                cs_list = get_first_sf_tag(sf, 'Chemical_shift_list')

                if cs_list in EMPTY_VALUE:
                    sf_category = SF_CATEGORIES['nmr-star']['chem_shift']
                    cs_sf_list = master_entry.get_saveframes_by_category(sf_category)
                    if len(cs_sf_list) == 1:
                        set_sf_tag(sf, 'Chemical_shift_list', get_first_sf_tag(cs_sf_list[0], 'Sf_framecode'))

                _sf_id = _sf_framecode = None
                _sf_category = SF_CATEGORIES['nmr-star']['chem_shift']
                if len(master_entry.get_saveframes_by_category(_sf_category)) == 1:
                    _sf = master_entry.get_saveframes_by_category(_sf_category)[0]
                    _sf_id = get_first_sf_tag(_sf, 'ID')
                    _sf_framecode = f"${get_first_sf_tag(_sf, 'Sf_framecode')}"

                sf.add_tag('Assigned_chem_shift_list_ID', _sf_id)
                sf.add_tag('Assigned_chem_shift_list_label', _sf_framecode)

                sf.add_tag('Details', None)
                sf.add_tag('Text_data_format', file_format if file_format is not None else 'unknown')

                with open(file_path, 'r', encoding='ascii', errors='ignore') as ifh:
                    sf.add_tag('Text_data', ifh.read())

                master_entry.add_saveframe(sf)

                self._reg.pk_sf_holder.append({'file_type': file_type, 'saveframe': sf})

                list_id += 1

        return True
