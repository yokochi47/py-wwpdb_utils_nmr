##
# File: NmrDpValidationCoordChk.py
# Date: 17-Aug-2026
#
# Updates:
##
""" Cross-check of NMR data against the coordinates for NMR data validation.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.3"

import copy
from typing import List, Optional, Tuple, Union

import pynmrstar

try:
    from wwpdb.utils.nmr.NmrDpConstant import (SF_CATEGORIES,
                                               LP_CATEGORIES,
                                               CUTOFF_BOND_LENGTH,
                                               INDEX_TAGS,
                                               PK_KEY_ITEMS,
                                               DATA_ITEMS,
                                               NUM_DIM_ITEMS,
                                               AUX_ALLOWED_TAGS,
                                               ITEM_NAMES_IN_CS_LOOP,
                                               ITEM_NAMES_IN_PK_LOOP,
                                               ITEM_NAMES_IN_RDC_LOOP,
                                               LOW_SEQ_COVERAGE,
                                               EMPTY_VALUE,
                                               STD_MON_DICT,
                                               PROTON_BEGIN_CODE,
                                               AMINO_PROTON_CODE,
                                               MAX_DIM_NUM_OF_SPECTRA,
                                               PERIPH_OFFSET_ATTEMPT)
    from wwpdb.utils.nmr.CifToNmrStar import (has_key_value,
                                              get_first_sf_tag)
    from wwpdb.utils.nmr.NmrVrptUtility import predict_redox_state_of_cysteine
    from wwpdb.utils.nmr.NmrDpValidationBase import NmrDpValidationBase
except ImportError:
    from nmr.NmrDpConstant import (SF_CATEGORIES,
                                   LP_CATEGORIES,
                                   CUTOFF_BOND_LENGTH,
                                   INDEX_TAGS,
                                   PK_KEY_ITEMS,
                                   DATA_ITEMS,
                                   NUM_DIM_ITEMS,
                                   AUX_ALLOWED_TAGS,
                                   ITEM_NAMES_IN_CS_LOOP,
                                   ITEM_NAMES_IN_PK_LOOP,
                                   ITEM_NAMES_IN_RDC_LOOP,
                                   LOW_SEQ_COVERAGE,
                                   EMPTY_VALUE,
                                   STD_MON_DICT,
                                   PROTON_BEGIN_CODE,
                                   AMINO_PROTON_CODE,
                                   MAX_DIM_NUM_OF_SPECTRA,
                                   PERIPH_OFFSET_ATTEMPT)
    from nmr.CifToNmrStar import (has_key_value,
                                  get_first_sf_tag)
    from nmr.NmrVrptUtility import predict_redox_state_of_cysteine
    from nmr.NmrDpValidationBase import NmrDpValidationBase


class NmrDpValidationCoordChk(NmrDpValidationBase):
    """ Cross-check of NMR data against the coordinates for NMR data validation.
    """
    __slots__ = ()

    def mapCoordDisulfideBond2Nmr(self, bond_list) -> bool:
        """ Map disulfide bond of coordinate file to NMR data.
        """

        is_done = False

        for fileListId in range(self._reg.file_path_list_len):

            input_source = self._reg.report.input_sources[fileListId]
            input_source_dic = input_source.get()

            file_name = input_source_dic['file_name']
            file_type = input_source_dic['file_type']

            polymer_sequence = input_source_dic['polymer_sequence']

            if polymer_sequence is None:
                continue

            seq_align_dic = self._reg.report.sequence_alignment.get()

            content_subtype = 'chem_shift'

            if not has_key_value(input_source_dic['content_subtype'], content_subtype):
                continue

            if not has_key_value(seq_align_dic, 'model_poly_seq_vs_nmr_poly_seq'):
                continue

            sf_category = SF_CATEGORIES[file_type][content_subtype]
            lp_category = LP_CATEGORIES[file_type][content_subtype]

            asm = []

            for bond in bond_list:

                cif_chain_id_1 = bond['chain_id_1']
                cif_seq_id_1 = bond['seq_id_1']
                cif_chain_id_2 = bond['chain_id_2']
                cif_seq_id_2 = bond['seq_id_2']

                ps1 = self._reg.report.getNmrPolymerSequenceWithModelChainId(cif_chain_id_1)

                if ps1 is None:
                    continue

                nmr_chain_id_1 = ps1['chain_id']

                result = next((seq_align for seq_align in seq_align_dic['model_poly_seq_vs_nmr_poly_seq']
                               if seq_align['ref_chain_id'] == cif_chain_id_1
                               and seq_align['test_chain_id'] == nmr_chain_id_1), None)

                if result is None:
                    continue

                nmr_seq_id_1 = next((test_seq_id for ref_seq_id, test_seq_id
                                     in zip(result['ref_seq_id'], result['test_seq_id'])
                                     if ref_seq_id == cif_seq_id_1), None)

                if nmr_seq_id_1 is None:
                    continue

                nmr_comp_id_1 = next((comp_id for seq_id, comp_id
                                      in zip(ps1['seq_id'], ps1['comp_id'])
                                      if seq_id == nmr_seq_id_1), None)

                if nmr_comp_id_1 is None:
                    continue

                ps2 = self._reg.report.getNmrPolymerSequenceWithModelChainId(cif_chain_id_2)

                if ps2 is None:
                    continue

                nmr_chain_id_2 = ps2['chain_id']

                result = next((seq_align for seq_align in seq_align_dic['model_poly_seq_vs_nmr_poly_seq']
                               if seq_align['ref_chain_id'] == cif_chain_id_2
                               and seq_align['test_chain_id'] == nmr_chain_id_2), None)

                if result is None:
                    continue

                nmr_seq_id_2 = next((test_seq_id for ref_seq_id, test_seq_id
                                     in zip(result['ref_seq_id'], result['test_seq_id'])
                                     if ref_seq_id == cif_seq_id_2), None)

                if nmr_seq_id_2 is None:
                    continue

                nmr_comp_id_2 = next((comp_id for seq_id, comp_id
                                      in zip(ps2['seq_id'], ps2['comp_id'])
                                      if seq_id == nmr_seq_id_2), None)

                if nmr_comp_id_2 is None:
                    continue

                disulf = {}
                disulf['chain_id_1'] = nmr_chain_id_1
                disulf['seq_id_1'] = nmr_seq_id_1
                disulf['comp_id_1'] = nmr_comp_id_1
                disulf['atom_id_1'] = bond['atom_id_1']
                disulf['chain_id_2'] = nmr_chain_id_2
                disulf['seq_id_2'] = nmr_seq_id_2
                disulf['comp_id_2'] = nmr_comp_id_2
                disulf['atom_id_2'] = bond['atom_id_2']
                disulf['distance_value'] = bond['distance_value']
                disulf['warning_description_1'] = None
                disulf['warning_description_2'] = None

                if self._reg.star_data_type[fileListId] == 'Loop':
                    sf = self._reg.star_data[fileListId]
                    sf_framecode = ''

                    ca_chem_shift_1, cb_chem_shift_1, ca_chem_shift_2, cb_chem_shift_2 =\
                        self._mapCoordBond2Nmr(file_name, file_type, content_subtype,
                                               sf, sf_framecode, lp_category,
                                               nmr_chain_id_1, nmr_seq_id_1, nmr_comp_id_1,
                                               nmr_chain_id_2, nmr_seq_id_2, nmr_comp_id_2)

                elif self._reg.star_data_type[fileListId] == 'Saveframe':
                    sf = self._reg.star_data[fileListId]
                    sf_framecode = get_first_sf_tag(sf, 'sf_framecode')

                    ca_chem_shift_1, cb_chem_shift_1, ca_chem_shift_2, cb_chem_shift_2 =\
                        self._mapCoordBond2Nmr(file_name, file_type, content_subtype,
                                               sf, sf_framecode, lp_category,
                                               nmr_chain_id_1, nmr_seq_id_1, nmr_comp_id_1,
                                               nmr_chain_id_2, nmr_seq_id_2, nmr_comp_id_2)
                else:

                    for sf in self._reg.star_data[fileListId].get_saveframes_by_category(sf_category):
                        sf_framecode = get_first_sf_tag(sf, 'sf_framecode')

                        if not any(True for loop in sf.loops if loop.category == lp_category):
                            continue

                        ca_chem_shift_1, cb_chem_shift_1, ca_chem_shift_2, cb_chem_shift_2 =\
                            self._mapCoordBond2Nmr(file_name, file_type, content_subtype,
                                                   sf, sf_framecode, lp_category,
                                                   nmr_chain_id_1, nmr_seq_id_1, nmr_comp_id_1,
                                                   nmr_chain_id_2, nmr_seq_id_2, nmr_comp_id_2)

                        if None in (ca_chem_shift_1, cb_chem_shift_1, ca_chem_shift_2, cb_chem_shift_2):
                            pass
                        else:
                            break

                disulf['ca_chem_shift_1'] = ca_chem_shift_1
                disulf['cb_chem_shift_1'] = cb_chem_shift_1
                disulf['ca_chem_shift_2'] = ca_chem_shift_2
                disulf['cb_chem_shift_2'] = cb_chem_shift_2

                if cb_chem_shift_1 is not None:
                    if cb_chem_shift_1 < 32.0:
                        disulf['redox_state_pred_1'] = 'reduced'
                    elif cb_chem_shift_1 > 35.0:
                        disulf['redox_state_pred_1'] = 'oxidized'
                    elif cb_chem_shift_2 is not None:
                        if cb_chem_shift_2 < 32.0:
                            disulf['redox_state_pred_1'] = 'reduced'
                        elif cb_chem_shift_2 > 35.0:
                            disulf['redox_state_pred_1'] = 'oxidized'
                        else:
                            disulf['redox_state_pred_1'] = 'ambiguous'
                    else:
                        disulf['redox_state_pred_1'] = 'ambiguous'
                else:
                    disulf['redox_state_pred_1'] = 'unknown'

                if cb_chem_shift_2 is not None:
                    if cb_chem_shift_2 < 32.0:
                        disulf['redox_state_pred_2'] = 'reduced'
                    elif cb_chem_shift_2 > 35.0:
                        disulf['redox_state_pred_2'] = 'oxidized'
                    elif cb_chem_shift_1 is not None:
                        if cb_chem_shift_1 < 32.0:
                            disulf['redox_state_pred_2'] = 'reduced'
                        elif cb_chem_shift_1 > 35.0:
                            disulf['redox_state_pred_2'] = 'oxidized'
                        else:
                            disulf['redox_state_pred_2'] = 'ambiguous'
                    else:
                        disulf['redox_state_pred_2'] = 'ambiguous'
                else:
                    disulf['redox_state_pred_2'] = 'unknown'

                if disulf['redox_state_pred_1'] == 'ambiguous' and ((ca_chem_shift_1 is not None) or (cb_chem_shift_1 is not None)):
                    oxi, red = predict_redox_state_of_cysteine(ca_chem_shift_1, cb_chem_shift_1)
                    disulf['redox_state_pred_1'] = f"oxidized {oxi:.1%}, reduced {red:.1%}"

                if disulf['redox_state_pred_2'] == 'ambiguous' and ((ca_chem_shift_2 is not None) or (cb_chem_shift_2 is not None)):
                    oxi, red = predict_redox_state_of_cysteine(ca_chem_shift_2, cb_chem_shift_2)
                    disulf['redox_state_pred_2'] = f"oxidized {oxi:.1%}, reduced {red:.1%}"

                if disulf['redox_state_pred_1'] != 'oxidized' and disulf['redox_state_pred_1'] != 'unknown':

                    warn = "Disulfide bond "\
                        f"({nmr_chain_id_1}:{nmr_seq_id_1}:{nmr_comp_id_1} - {nmr_chain_id_2}:{nmr_seq_id_2}:{nmr_comp_id_2}) "\
                        "can not be verified with the assigned chemical shift values "\
                        f"({nmr_chain_id_1}:{nmr_seq_id_1}:{nmr_comp_id_1}:CA {ca_chem_shift_1} ppm, "\
                        f"{nmr_chain_id_1}:{nmr_seq_id_1}:{nmr_comp_id_1}:CB {cb_chem_shift_1} ppm, "\
                        f"redox_state_pred {disulf['redox_state_pred_1']})."

                    item = 'anomalous_chemical_shift' if disulf['redox_state_pred_1'] == 'reduced' else 'unusual_chemical_shift'

                    self._reg.report.warning.appendDescription(item,
                                                               {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                'description': warn})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.mapCoordDisulfideBond2Nmr() ++ Warning  - {warn}\n")

                    disulf['warning_description_1'] = f'{item}: {warn}'

                if disulf['redox_state_pred_2'] != 'oxidized' and disulf['redox_state_pred_2'] != 'unknown':

                    warn = "Disulfide bond "\
                        f"({nmr_chain_id_1}:{nmr_seq_id_1}:{nmr_comp_id_1} - {nmr_chain_id_2}:{nmr_seq_id_2}:{nmr_comp_id_2}) "\
                        "can not be verified with the assigned chemical shift values "\
                        f"({nmr_chain_id_2}:{nmr_seq_id_2}:{nmr_comp_id_2}:CA {ca_chem_shift_2} ppm, "\
                        f"{nmr_chain_id_2}:{nmr_seq_id_2}:{nmr_comp_id_2}:CB {cb_chem_shift_2} ppm, "\
                        f"redox_state_pred {disulf['redox_state_pred_2']})."

                    item = 'anomalous_chemical_shift' if disulf['redox_state_pred_2'] == 'reduced' else 'unusual_chemical_shift'

                    self._reg.report.warning.appendDescription(item,
                                                               {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                'description': warn})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.mapCoordDisulfideBond2Nmr() ++ Warning  - {warn}\n")

                    disulf['warning_description_2'] = f'{item}: {warn}'

                asm.append(disulf)

            if len(asm) > 0:
                input_source.setItemValue('disulfide_bond', asm)
                is_done = True

        return is_done

    def _mapCoordBond2Nmr(self, file_name: str, file_type: str, content_subtype: str,
                          sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                          sf_framecode: str, lp_category: str,
                          nmr_chain_id_1: str, nmr_seq_id_1: int, nmr_comp_id_1: str,
                          nmr_chain_id_2: str, nmr_seq_id_2: int, nmr_comp_id_2: str
                          ) -> Tuple[Optional[float], Optional[float], Optional[float], Optional[float]]:
        """ Map a bond of coordinate file to NMR data.
        """

        ca_chem_shift_1 = cb_chem_shift_1 = ca_chem_shift_2 = cb_chem_shift_2 = None

        key_items = self._reg.key_items[file_type][content_subtype]
        data_items = DATA_ITEMS[file_type][content_subtype]

        item_names = ITEM_NAMES_IN_CS_LOOP[file_type]
        chain_id_name = item_names['chain_id']
        seq_id_name = item_names['seq_id']
        comp_id_name = item_names['comp_id']
        atom_id_name = item_names['atom_id']
        value_name = item_names['value']

        if not self._reg.report.error.exists(file_name, sf_framecode):

            lp_data = next((lp['data'] for lp in self._reg.lp_data[content_subtype]
                            if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode), None)

            if lp_data is None:

                try:

                    lp_data = self._reg.nefT.check_data(sf, lp_category, key_items, data_items, None, None, None,
                                                        enforce_allowed_tags=(file_type == 'nmr-star'),
                                                        excl_missing_data=self._reg.excl_missing_data)[0]

                    self._reg.lp_data[content_subtype].append({'file_name': file_name, 'sf_framecode': sf_framecode,
                                                               'data': lp_data})

                except Exception:  # pylint: disable=broad-exception-caught
                    pass

            if lp_data is not None:

                for row in lp_data:
                    chain_id = row[chain_id_name]
                    seq_id = row[seq_id_name]
                    comp_id = row[comp_id_name]
                    atom_id = row[atom_id_name]

                    if chain_id == nmr_chain_id_1 and seq_id == nmr_seq_id_1 and comp_id == nmr_comp_id_1:
                        if atom_id == 'CA' and ca_chem_shift_1 is None:
                            ca_chem_shift_1 = row[value_name]
                        elif atom_id == 'CB' and cb_chem_shift_1 is None:
                            cb_chem_shift_1 = row[value_name]

                    elif chain_id == nmr_chain_id_2 and seq_id == nmr_seq_id_2 and comp_id == nmr_comp_id_2:
                        if atom_id == 'CA' and ca_chem_shift_2 is None:
                            ca_chem_shift_2 = row[value_name]
                        elif atom_id == 'CB' and cb_chem_shift_2 is None:
                            cb_chem_shift_2 = row[value_name]

                    if None in (ca_chem_shift_1, cb_chem_shift_1, ca_chem_shift_2, cb_chem_shift_2):
                        pass
                    else:
                        break

        return ca_chem_shift_1, cb_chem_shift_1, ca_chem_shift_2, cb_chem_shift_2

    def mapCoordOtherBond2Nmr(self, bond_list: List[dict]) -> bool:
        """ Map other bond (neither disulfide nor covalent bond) of coordinate file to NMR data.
        """

        is_done = False

        for fileListId in range(self._reg.file_path_list_len):

            input_source = self._reg.report.input_sources[fileListId]
            input_source_dic = input_source.get()

            file_name = input_source_dic['file_name']
            file_type = input_source_dic['file_type']

            polymer_sequence = input_source_dic['polymer_sequence']

            if polymer_sequence is None:
                continue

            seq_align_dic = self._reg.report.sequence_alignment.get()

            content_subtype = 'chem_shift'

            if not has_key_value(input_source_dic['content_subtype'], content_subtype):
                continue

            if not has_key_value(seq_align_dic, 'model_poly_seq_vs_nmr_poly_seq'):
                continue

            sf_category = SF_CATEGORIES[file_type][content_subtype]
            lp_category = LP_CATEGORIES[file_type][content_subtype]

            asm = []

            for bond in bond_list:

                cif_chain_id_1 = bond['chain_id_1']
                cif_seq_id_1 = bond['seq_id_1']
                cif_chain_id_2 = bond['chain_id_2']
                cif_seq_id_2 = bond['seq_id_2']

                ps1 = self._reg.report.getNmrPolymerSequenceWithModelChainId(cif_chain_id_1)

                if ps1 is None:
                    continue

                nmr_chain_id_1 = ps1['chain_id']

                result = next((seq_align for seq_align in seq_align_dic['model_poly_seq_vs_nmr_poly_seq']
                               if seq_align['ref_chain_id'] == cif_chain_id_1
                               and seq_align['test_chain_id'] == nmr_chain_id_1), None)

                if result is None:
                    continue

                nmr_seq_id_1 = next((test_seq_id for ref_seq_id, test_seq_id
                                     in zip(result['ref_seq_id'], result['test_seq_id'])
                                     if ref_seq_id == cif_seq_id_1), None)

                if nmr_seq_id_1 is None:
                    continue

                nmr_comp_id_1 = next((comp_id for seq_id, comp_id
                                      in zip(ps1['seq_id'], ps1['comp_id'])
                                      if seq_id == nmr_seq_id_1), None)

                if nmr_comp_id_1 is None:
                    continue

                ps2 = self._reg.report.getNmrPolymerSequenceWithModelChainId(cif_chain_id_2)

                if ps2 is None:
                    continue

                nmr_chain_id_2 = ps2['chain_id']

                result = next((seq_align for seq_align in seq_align_dic['model_poly_seq_vs_nmr_poly_seq']
                               if seq_align['ref_chain_id'] == cif_chain_id_2
                               and seq_align['test_chain_id'] == nmr_chain_id_2), None)

                if result is None:
                    continue

                nmr_seq_id_2 = next((test_seq_id for ref_seq_id, test_seq_id
                                     in zip(result['ref_seq_id'], result['test_seq_id'])
                                     if ref_seq_id == cif_seq_id_2), None)

                if nmr_seq_id_2 is None:
                    continue

                nmr_comp_id_2 = next((comp_id for seq_id, comp_id
                                      in zip(ps2['seq_id'], ps2['comp_id'])
                                      if seq_id == nmr_seq_id_2), None)

                if nmr_comp_id_2 is None:
                    continue

                other = {}
                other['chain_id_1'] = nmr_chain_id_1
                other['seq_id_1'] = nmr_seq_id_1
                other['comp_id_1'] = nmr_comp_id_1
                other['atom_id_1'] = bond['atom_id_1']
                other['chain_id_2'] = nmr_chain_id_2
                other['seq_id_2'] = nmr_seq_id_2
                other['comp_id_2'] = nmr_comp_id_2
                other['atom_id_2'] = bond['atom_id_2']
                other['distance_value'] = bond['distance_value']
                other['warning_description_1'] = None
                other['warning_description_2'] = None

                if self._reg.star_data_type[fileListId] == 'Loop':
                    sf = self._reg.star_data[fileListId]
                    sf_framecode = ''

                    ca_chem_shift_1, cb_chem_shift_1, ca_chem_shift_2, cb_chem_shift_2 =\
                        self._mapCoordBond2Nmr(file_name, file_type, content_subtype,
                                               sf, sf_framecode, lp_category,
                                               nmr_chain_id_1, nmr_seq_id_1, nmr_comp_id_1,
                                               nmr_chain_id_2, nmr_seq_id_2, nmr_comp_id_2)

                elif self._reg.star_data_type[fileListId] == 'Saveframe':
                    sf = self._reg.star_data[fileListId]
                    sf_framecode = get_first_sf_tag(sf, 'sf_framecode')

                    ca_chem_shift_1, cb_chem_shift_1, ca_chem_shift_2, cb_chem_shift_2 =\
                        self._mapCoordBond2Nmr(file_name, file_type, content_subtype,
                                               sf, sf_framecode, lp_category,
                                               nmr_chain_id_1, nmr_seq_id_1, nmr_comp_id_1,
                                               nmr_chain_id_2, nmr_seq_id_2, nmr_comp_id_2)

                else:

                    for sf in self._reg.star_data[fileListId].get_saveframes_by_category(sf_category):
                        sf_framecode = get_first_sf_tag(sf, 'sf_framecode')

                        if not any(True for loop in sf.loops if loop.category == lp_category):
                            continue

                        ca_chem_shift_1, cb_chem_shift_1, ca_chem_shift_2, cb_chem_shift_2 =\
                            self._mapCoordBond2Nmr(file_name, file_type, content_subtype,
                                                   sf, sf_framecode, lp_category,
                                                   nmr_chain_id_1, nmr_seq_id_1, nmr_comp_id_1,
                                                   nmr_chain_id_2, nmr_seq_id_2, nmr_comp_id_2)

                        if None in (ca_chem_shift_1, cb_chem_shift_1, ca_chem_shift_2, cb_chem_shift_2):
                            pass
                        else:
                            break

                other['ca_chem_shift_1'] = ca_chem_shift_1
                other['cb_chem_shift_1'] = cb_chem_shift_1
                other['ca_chem_shift_2'] = ca_chem_shift_2
                other['cb_chem_shift_2'] = cb_chem_shift_2

                if cb_chem_shift_1 is not None:
                    if cb_chem_shift_1 < 32.0:
                        other['redox_state_pred_1'] = 'reduced'
                    elif cb_chem_shift_1 > 35.0:
                        other['redox_state_pred_1'] = 'oxidized'
                    elif cb_chem_shift_2 is not None:
                        if cb_chem_shift_2 < 32.0:
                            other['redox_state_pred_1'] = 'reduced'
                        elif cb_chem_shift_2 > 35.0:
                            other['redox_state_pred_1'] = 'oxidized'
                        else:
                            other['redox_state_pred_1'] = 'ambiguous'
                    else:
                        other['redox_state_pred_1'] = 'ambiguous'
                else:
                    other['redox_state_pred_1'] = 'unknown'

                if cb_chem_shift_2 is not None:
                    if cb_chem_shift_2 < 32.0:
                        other['redox_state_pred_2'] = 'reduced'
                    elif cb_chem_shift_2 > 35.0:
                        other['redox_state_pred_2'] = 'oxidized'
                    elif cb_chem_shift_1 is not None:
                        if cb_chem_shift_1 < 32.0:
                            other['redox_state_pred_2'] = 'reduced'
                        elif cb_chem_shift_1 > 35.0:
                            other['redox_state_pred_2'] = 'oxidized'
                        else:
                            other['redox_state_pred_2'] = 'ambiguous'
                    else:
                        other['redox_state_pred_2'] = 'ambiguous'
                else:
                    other['redox_state_pred_2'] = 'unknown'

                if other['redox_state_pred_1'] == 'ambiguous' and ((ca_chem_shift_1 is not None) or (cb_chem_shift_1 is not None)):
                    oxi, red = predict_redox_state_of_cysteine(ca_chem_shift_1, cb_chem_shift_1)
                    other['redox_state_pred_1'] = f"oxidized {oxi:.1%}, reduced {red:.1%}"

                if other['redox_state_pred_2'] == 'ambiguous' and ((ca_chem_shift_2 is not None) or (cb_chem_shift_2 is not None)):
                    oxi, red = predict_redox_state_of_cysteine(ca_chem_shift_2, cb_chem_shift_2)
                    other['redox_state_pred_2'] = f"oxidized {oxi:.1%}, reduced {red:.1%}"

                if other['redox_state_pred_1'] != 'oxidized' and other['redox_state_pred_1'] != 'unknown':

                    warn = "Other bond "\
                        f"({nmr_chain_id_1}:{nmr_seq_id_1}:{nmr_comp_id_1} - {nmr_chain_id_2}:{nmr_seq_id_2}:{nmr_comp_id_2}) "\
                        "can not be verified with the assigned chemical shift values "\
                        f"({nmr_chain_id_1}:{nmr_seq_id_1}:{nmr_comp_id_1}:CA {ca_chem_shift_1} ppm, "\
                        f"{nmr_chain_id_1}:{nmr_seq_id_1}:{nmr_comp_id_1}:CB {cb_chem_shift_1} ppm, "\
                        f"redox_state_pred {other['redox_state_pred_1']})."

                    item = 'anomalous_chemical_shift' if other['redox_state_pred_1'] == 'reduced' else 'unusual_chemical_shift'

                    self._reg.report.warning.appendDescription(item,
                                                               {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                'description': warn})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.mapCoordOtherBond2Nmr() ++ Warning  - {warn}\n")

                    other['warning_description_1'] = f'{item}: {warn}'

                if other['redox_state_pred_2'] != 'oxidized' and other['redox_state_pred_2'] != 'unknown':

                    warn = "Other bond "\
                        f"({nmr_chain_id_1}:{nmr_seq_id_1}:{nmr_comp_id_1} - {nmr_chain_id_2}:{nmr_seq_id_2}:{nmr_comp_id_2}) "\
                        "can not be verified with the assigned chemical shift values "\
                        f"({nmr_chain_id_2}:{nmr_seq_id_2}:{nmr_comp_id_2}:CA {ca_chem_shift_2} ppm, "\
                        f"{nmr_chain_id_2}:{nmr_seq_id_2}:{nmr_comp_id_2}:CB {cb_chem_shift_2} ppm, "\
                        f"redox_state_pred {other['redox_state_pred_2']})."

                    item = 'anomalous_chemical_shift' if other['redox_state_pred_2'] == 'reduced' else 'unusual_chemical_shift'

                    self._reg.report.warning.appendDescription(item,
                                                               {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                'description': warn})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.mapCoordOtherBond2Nmr() ++ Warning  - {warn}\n")

                    other['warning_description_2'] = f'{item}: {warn}'

                asm.append(other)

            if len(asm) > 0:
                input_source.setItemValue('other_bond', asm)
                is_done = True

        return is_done

    def testCoordCovalentBond(self, file_name: str, file_type: str, content_subtype: str, sf_framecode: str, lp_category: str
                              ) -> None:
        """ Perform consistency test on covalent bonds.
        """

        item_names = ITEM_NAMES_IN_RDC_LOOP[file_type]
        chain_id_1_name = item_names['chain_id_1']
        chain_id_2_name = item_names['chain_id_2']
        seq_id_1_name = item_names['seq_id_1']
        seq_id_2_name = item_names['seq_id_2']
        comp_id_1_name = item_names['comp_id_1']
        comp_id_2_name = item_names['comp_id_2']
        atom_id_1_name = item_names['atom_id_1']
        atom_id_2_name = item_names['atom_id_2']

        def ext_atom_names(row):
            return (row[chain_id_1_name], row[chain_id_2_name],
                    row[seq_id_1_name], row[seq_id_2_name],
                    row[comp_id_1_name], row[comp_id_2_name],
                    row[atom_id_1_name], row[atom_id_2_name])

        try:

            aux_data = next((lp['data'] for lp in self._reg.aux_data[content_subtype]
                             if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode
                             and lp['category'] == lp_category), None)

            if aux_data is not None:

                for row in aux_data:
                    chain_id_1, chain_id_2, seq_id_1, seq_id_2, \
                        comp_id_1, comp_id_2, atom_id_1, atom_id_2 = ext_atom_names(row)

                    bond = self.getNmrBondLength(chain_id_1, seq_id_1, atom_id_1, chain_id_2, seq_id_2, atom_id_2)

                    if bond is None:
                        continue

                    broken_bond = [b for b in bond if b['distance'] > CUTOFF_BOND_LENGTH]

                    if len(broken_bond) == 0:
                        continue

                    length_list = ''
                    for bb in broken_bond:
                        length_list += f"{bb['distance']} (model_id {bb['model_id']}), "

                    warn = "Covalent bond ("\
                        + self.getReducedAtomNotation(chain_id_1_name, chain_id_1, seq_id_1_name, seq_id_1,
                                                      comp_id_1_name, comp_id_1, atom_id_1_name, atom_id_1)\
                        + " - "\
                        + self.getReducedAtomNotation(chain_id_2_name, chain_id_2, seq_id_2_name, seq_id_2,
                                                      comp_id_2_name, comp_id_2, atom_id_2_name, atom_id_2)\
                        + f") is out of acceptable range, {length_list[:-2]}Å."

                    self._reg.report.warning.appendDescription('anomalous_bond_length',
                                                               {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                'category': lp_category, 'description': warn})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.testCoordCovalentBond() ++ Warning  - {warn}\n")

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.testCoordCovalentBond() ++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.testCoordCovalentBond() ++ Error  - {str(e)}\n")

    def testResidueVariant(self, file_name: str, file_type: str, content_subtype: str,
                           sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                           sf_framecode: str, lp_category: str, cif_poly_seq: List[dict], nmr2ca: dict) -> None:
        """ Perform consistency test on residue variants.
        """

        item_names = ITEM_NAMES_IN_CS_LOOP[file_type]
        chain_id_name = item_names['chain_id']
        seq_id_name = item_names['seq_id']
        comp_id_name = item_names['comp_id']
        atom_id_name = item_names['atom_id']
        variant_name = 'residue_variant' if file_type == 'nef' else item_names['atom_id']

        key_items = self._reg.aux_key_items[file_type][content_subtype][lp_category]
        data_items = self._reg.aux_data_items[file_type][content_subtype][lp_category]
        allowed_tags = AUX_ALLOWED_TAGS[file_type][content_subtype][lp_category]

        try:

            aux_data = self._reg.nefT.check_data(sf, lp_category, key_items, data_items,
                                                 allowed_tags, None, None,
                                                 enforce_allowed_tags=(file_type == 'nmr-star'),
                                                 excl_missing_data=self._reg.excl_missing_data)[0]

            if aux_data is not None:

                for row in aux_data:
                    chain_id = row[chain_id_name]
                    seq_id = row[seq_id_name]
                    comp_id = row[comp_id_name]
                    variant = row[variant_name]

                    if chain_id not in nmr2ca:
                        continue

                    ca = next((ca['seq_align'] for ca in nmr2ca[chain_id]
                               if ('seq_unmap' not in ca or (seq_id not in ca['seq_unmap']))), None)  # DAOTHER-7465

                    if ca is None:
                        continue

                    cif_chain_id = ca['test_chain_id']

                    cif_seq_id = next((test_seq_id for ref_seq_id, test_seq_id
                                       in zip(ca['ref_seq_id'], ca['test_seq_id']) if ref_seq_id == seq_id), None)

                    if cif_seq_id is None:
                        continue

                    cif_ps = next(ps for ps in cif_poly_seq if ps['chain_id'] == cif_chain_id)

                    cif_comp_id = next((_comp_id for _seq_id, _comp_id
                                        in zip(cif_ps['seq_id'], cif_ps['comp_id']) if _seq_id == cif_seq_id), None)

                    if cif_comp_id is None:
                        continue

                    seq_key = (cif_chain_id, cif_seq_id)

                    if seq_key in self._reg.caC['coord_unobs_res']:  # DAOTHER-7665
                        continue

                    coord_atom_site_ = self._reg.caC['coord_atom_site'].get(seq_key)

                    self._reg.ccU.updateChemCompDict(comp_id)

                    if file_type == 'nef':

                        if variant in EMPTY_VALUE:
                            continue

                        for _variant in variant.split(','):
                            _variant_ = _variant.strip(' ')

                            if _variant_[0] not in ('-', '+'):

                                warn = f"Residue variant {_variant_!r} should start with "\
                                    "either '-' or '+' symbol according to the NEF specification."

                                self._reg.report.warning.appendDescription('atom_nomenclature_mismatch',
                                                                           {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                            'category': lp_category, 'description': warn})

                                if self._reg.verbose:
                                    self._reg.log.write(f"+{self.__class_name__}.textResidueVariant() ++ Warning  - {warn}\n")

                                continue

                            atom_id = _variant_[1:]

                            if file_type == 'nef' or self.isNmrAtomName(comp_id, atom_id):
                                _atom_id, _, details = self._getAtomIdListWithAmbigCode(comp_id, atom_id)

                                len_atom_id = len(_atom_id)

                                if len_atom_id == 0:
                                    continue

                                if len_atom_id == 1 and atom_id == _atom_id[0]:
                                    atom_id_ = atom_id
                                    atom_name = atom_id

                                    if details is not None:
                                        atom_name += f", where {details.rstrip('.')}"

                                else:
                                    atom_name = f'{atom_id} (e.g. '

                                    for atom_id_ in _atom_id:
                                        atom_name += f'{atom_id_} '

                                    atom_name = f'{atom_name.rstrip()})'

                                    # representative atom id
                                    atom_id_ = _atom_id[0]

                            else:
                                atom_id_ = atom_id
                                atom_name = atom_id

                            if _variant_[0] == '-':

                                if self._reg.ccU.lastStatus:  # matches with comp_id in CCD

                                    if not self._reg.nefT.validate_comp_atom(comp_id, atom_id_):

                                        warn = "Atom ("\
                                            + self.getReducedAtomNotation(chain_id_name, chain_id, seq_id_name, seq_id,
                                                                          comp_id_name, comp_id, atom_id_name, atom_name)\
                                            + f", {variant_name} {_variant_!r}) did not match with "\
                                            "chemical component dictionary (CCD)."

                                        self._reg.report.warning.appendDescription('atom_nomenclature_mismatch',
                                                                                   {'file_name': file_name,
                                                                                    'sf_framecode': sf_framecode,
                                                                                    'category': lp_category, 'description': warn})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.textResidueVariant() "
                                                                f"++ Warning  - {warn}\n")

                                if coord_atom_site_ is not None and coord_atom_site_['comp_id'] == cif_comp_id\
                                   and (atom_id_ in coord_atom_site_['atom_id']
                                        or ('auth_atom_id' in coord_atom_site_ and atom_id_ in coord_atom_site_['auth_atom_id']))\
                                   and lp_category != '_Entity_deleted_atom':

                                    err = "Atom ("\
                                        + self.getReducedAtomNotation(chain_id_name, chain_id, seq_id_name, seq_id,
                                                                      comp_id_name, comp_id, atom_id_name, atom_name)\
                                        + f", {variant_name} {_variant_!r}) is unexpectedly incorporated in the coordinates."

                                    self._reg.report.error.appendDescription('invalid_atom_nomenclature',
                                                                             {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                              'category': lp_category, 'description': err})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.testResidueVariant() ++ Error  - {err}\n")

                            else:

                                if coord_atom_site_ is not None and coord_atom_site_['comp_id'] == cif_comp_id\
                                   and (atom_id_ not in coord_atom_site_['atom_id']
                                        and (('auth_atom_id' in coord_atom_site_
                                              and atom_id_ not in coord_atom_site_['auth_atom_id'])
                                             or 'auth_atom_id' not in coord_atom_site_)):

                                    err = "Atom ("\
                                        + self.getReducedAtomNotation(chain_id_name, chain_id, seq_id_name, seq_id,
                                                                      comp_id_name, comp_id, atom_id_name, atom_name)\
                                        + f") which is a {variant_name} {_variant_!r} is not present in the coordinates."

                                    checked = False
                                    if atom_id_[0] in PROTON_BEGIN_CODE:
                                        cca = next((cca for cca in self._reg.ccU.lastAtomDictList
                                                    if cca['atom_id'] == atom_id_), None)
                                        bonded_to = self._reg.ccU.getBondedAtoms(comp_id, atom_id_)
                                        peptide_like = self._reg.csStat.peptideLike(comp_id)
                                        if cca is not None and len(bonded_to) > 0:
                                            if coord_atom_site_ is not None and bonded_to[0] in coord_atom_site_['atom_id']\
                                               and (cca['leaving_atom_flag'] != 'Y'
                                                    or (peptide_like
                                                        and cca['n_terminal_atom_flag'] == 'N'
                                                        and cca['c_terminal_atom_flag'] == 'N')):
                                                checked = True
                                                err = "Atom ("\
                                                    + self.getReducedAtomNotation(chain_id_name, chain_id, seq_id_name, seq_id,
                                                                                  comp_id_name, comp_id, atom_id_name, atom_name)\
                                                    + f") which is a {variant_name} {_variant_!r} is not properly instantiated "\
                                                    "in the coordinates. Please re-upload the model file."

                                    if self._reg.remediation_mode and checked:
                                        continue

                                    if content_subtype.startswith('spectral_peak'):

                                        self._reg.report.warning.appendDescription('hydrogen_not_instantiated' if checked
                                                                                   else 'assigned_peak_atom_not_found',
                                                                                   {'file_name': file_name,
                                                                                    'sf_framecode': sf_framecode,
                                                                                    'category': lp_category, 'description': err})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.testResidueVariant() "
                                                                f"++ Warning  - {err}\n")

                                    else:

                                        self._reg.report.error.appendDescription('hydrogen_not_instantiated' if checked
                                                                                 else 'atom_not_found',
                                                                                 {'file_name': file_name,
                                                                                  'sf_framecode': sf_framecode,
                                                                                  'category': lp_category, 'description': err})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.testResidueVariant() ++ Error  - {err}\n")

                    else:

                        atom_id = variant

                        if file_type == 'nef' or self.isNmrAtomName(comp_id, atom_id):
                            _atom_id, _, details = self._getAtomIdListWithAmbigCode(comp_id, atom_id)

                            len_atom_id = len(_atom_id)

                            if len_atom_id == 0:
                                continue

                            if len_atom_id == 1 and atom_id == _atom_id[0]:
                                atom_id_ = atom_id
                                atom_name = atom_id

                                if details is not None:
                                    atom_name += f", where {details.rstrip('.')}"

                            else:
                                atom_name = f'{atom_id} (e.g. '

                                for atom_id_ in _atom_id:
                                    atom_name += f'{atom_id_} '

                                atom_name = f'{atom_name.rstrip()})'

                                # representative atom id
                                atom_id_ = _atom_id[0]

                        else:
                            atom_id_ = atom_id
                            atom_name = atom_id

                            if self._reg.ccU.lastStatus:  # matches with comp_id in CCD

                                if not self._reg.nefT.validate_comp_atom(comp_id, atom_id_):

                                    warn = "Atom ("\
                                        + self.getReducedAtomNotation(chain_id_name, chain_id, seq_id_name, seq_id,
                                                                      comp_id_name, comp_id, atom_id_name, atom_name)\
                                        + ") did not match with chemical component dictionary (CCD)."

                                    self._reg.report.warning.appendDescription('atom_nomenclature_mismatch',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': warn})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.textResidueVariant() ++ Warning  - {warn}\n")

                            if coord_atom_site_ is not None and coord_atom_site_['comp_id'] == cif_comp_id\
                               and (atom_id_ in coord_atom_site_['atom_id']
                                    and (('auth_atom_id' in coord_atom_site_ and atom_id_ in coord_atom_site_['auth_atom_id'])
                                         or 'auth_atom_id' not in coord_atom_site_))\
                               and lp_category != '_Entity_deleted_atom':

                                err = "Atom ("\
                                    + self.getReducedAtomNotation(chain_id_name, chain_id, seq_id_name, seq_id,
                                                                  comp_id_name, comp_id, atom_id_name, atom_name)\
                                    + ") is unexpectedly incorporated in the coordinates."

                                self._reg.report.error.appendDescription('invalid_atom_nomenclature',
                                                                         {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                          'category': lp_category, 'description': err})

                                if self._reg.verbose:
                                    self._reg.log.write(f"+{self.__class_name__}.testResidueVariant() ++ Error  - {err}\n")

        except LookupError as e:

            item = 'format_issue' if 'Unauthorized' in str(e) else 'missing_mandatory_item'

            self._reg.report.error.appendDescription(item,
                                                     {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                      'category': lp_category, 'description': str(e).strip("'")})

            self._reg.log.write(f"+{self.__class_name__}.testResidueVariant() ++ LookupError  - "
                                f"{file_name} {sf_framecode} {lp_category} {str(e)}\n")

        except ValueError as e:

            self._reg.report.error.appendDescription('invalid_data',
                                                     {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                      'category': lp_category, 'description': str(e).strip("'")})

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.testResidueVariant() ++ ValueError  - {str(e)}\n")

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.testResidueVariant() ++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.testResidueVariant() ++ Error  - {str(e)}\n")

    def testCoordAtomIdConsistency(self, file_list_id: int, file_name: str, file_type: str, content_subtype: str,
                                   sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                                   list_id: int, sf_framecode: str, lp_category: str, cif_poly_seq: List[dict],
                                   seq_align_dic: dict, nmr2ca: dict, ref_chain_id: str) -> bool:
        """ Perform consistency test on atom names of coordinate file.
        """

        modified = False

        index_tag = INDEX_TAGS[file_type][content_subtype] if content_subtype != 'poly_seq' else None

        if file_type == 'nef' or not self._reg.nonblk_bad_nterm:

            if content_subtype != 'poly_seq':
                lp_data = next((lp['data'] for lp in self._reg.lp_data[content_subtype]
                                if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode), None)
            else:
                lp_data = next((lp['data'] for lp in self._reg.aux_data[content_subtype]
                                if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode
                                and lp['category'] == lp_category), None)

        else:

            if content_subtype == 'spectral_peak':

                try:

                    _num_dim = get_first_sf_tag(sf, NUM_DIM_ITEMS[file_type])
                    num_dim = int(_num_dim)

                    if num_dim not in range(1, MAX_DIM_NUM_OF_SPECTRA):
                        raise ValueError()

                except ValueError:  # raised error already at testIndexConsistency()
                    return False

                max_dim = num_dim + 1

                key_items = []
                for dim in range(1, max_dim):
                    for k in PK_KEY_ITEMS[file_type]:
                        if k['type'] == 'float':  # position
                            _k = copy.copy(k)
                            if '%s' in k['name']:
                                _k['name'] = k['name'] % dim
                            key_items.append(_k)
                for k in PK_KEY_ITEMS[file_type]:
                    if k['type'] == 'positive-int':  # peak_id
                        key_items.append(k)

                data_items = []
                for d in DATA_ITEMS[file_type][content_subtype]:
                    data_items.append(d)
                for dim in range(1, max_dim):
                    for d in self._reg.pk_data_items[file_type]:
                        _d = copy.copy(d)
                        if '%s' in d['name']:
                            _d['name'] = d['name'] % dim
                        if 'default-from' in d and '%s' in d['default-from']:  # DAOTHER-7421
                            _d['default-from'] = d['default-from'] % dim
                        data_items.append(_d)

            else:

                if content_subtype != 'poly_seq':
                    key_items = self._reg.key_items[file_type][content_subtype]
                    data_items = DATA_ITEMS[file_type][content_subtype]
                else:
                    key_items = self._reg.aux_key_items[file_type][content_subtype][lp_category]
                    data_items = self._reg.aux_data_items[file_type][content_subtype][lp_category]

            try:

                lp_data = self._reg.nefT.check_data(sf, lp_category, key_items, data_items, None, None, None,
                                                    enforce_allowed_tags=(file_type == 'nmr-star'),
                                                    excl_missing_data=self._reg.excl_missing_data)[0]

            except Exception:  # pylint: disable=broad-exception-caught
                return False

        if lp_data is None:
            return False

        has_seq_align = False

        sa_name = f'nmr_poly_seq_vs_{content_subtype}'

        if has_key_value(seq_align_dic, sa_name):

            for seq_align in seq_align_dic[sa_name]:

                if seq_align['list_id'] == list_id:
                    has_seq_align = True
                    break

        if not has_seq_align and content_subtype != 'poly_seq':
            return False

        auth_to_star_seq = self._reg.caC['auth_to_star_seq']
        auth_to_label_seq = self._reg.caC['auth_to_label_seq']
        auth_to_orig_seq = self._reg.caC['auth_to_orig_seq']
        label_to_auth_seq = self._reg.caC['label_to_auth_seq']
        coord_atom_site = self._reg.caC['coord_atom_site']
        coord_unobs_res = self._reg.caC['coord_unobs_res']
        coord_unobs_atom = self._reg.caC['coord_unobs_atom'] if 'coord_unobs_atom' in self._reg.caC else {}

        if auth_to_star_seq is None:
            return False

        item_names = []

        if content_subtype == 'chem_shift':
            max_dim = 2

            item_names.append(ITEM_NAMES_IN_CS_LOOP[file_type])

        else:

            if content_subtype in ('poly_seq', 'dist_restraint', 'rdc_restraint'):
                max_dim = 3

            elif content_subtype == 'dihed_restraint':
                max_dim = 5

            elif content_subtype == 'spectral_peak':

                try:

                    _num_dim = get_first_sf_tag(sf, NUM_DIM_ITEMS[file_type])
                    num_dim = int(_num_dim)

                    if num_dim not in range(1, MAX_DIM_NUM_OF_SPECTRA):
                        raise ValueError()

                except ValueError:  # raised error already at testIndexConsistency()
                    return False

                max_dim = num_dim + 1

            else:
                return False

            for j in range(1, max_dim):
                _item_names = {}
                for k, v in ITEM_NAMES_IN_PK_LOOP[file_type].items():
                    if '%s' in v:
                        v = v % j
                    _item_names[k] = v
                item_names.append(_item_names)

        num_dim = max_dim - 1

        chain_id_names, seq_id_names, comp_id_names, atom_id_names = [], [], [], []
        if file_type == 'nmr-star':
            alt_seq_id_names = []

        for j in range(num_dim):
            chain_id_names.append(item_names[j]['chain_id'])
            seq_id_names.append(item_names[j]['seq_id'])
            comp_id_names.append(item_names[j]['comp_id'])
            atom_id_names.append(item_names[j]['atom_id'])
            if file_type == 'nmr-star':
                alt_seq_id_names.append(item_names[j]['alt_seq_id'])

        details_col = -1

        if file_type == 'nmr-star':

            loop = sf if self._reg.star_data_type[file_list_id] == 'Loop' else sf.get_loop(lp_category)

            if 'Details' in loop.tags:
                details_col = loop.tags.index('Details')

        def get_coord_atom_site_of(chain_id, seq_id, comp_id):

            if (chain_id, seq_id, comp_id) in auth_to_star_seq:
                seq_key = (chain_id, seq_id)

                if seq_key in coord_unobs_res:  # DAOTHER-7665
                    return True, None, None

                if seq_key not in coord_atom_site:
                    return True, None, None

                # 2lit: 1:104:LYS (nmr), A:99:LYS (model) overlaps A:104:HEC (model)
                # if seq_key not in auth_to_label_seq:
                #     return True, None, None

                coord_atom_site_ = coord_atom_site[seq_key]

                cif_comp_id = coord_atom_site_['comp_id']

                if comp_id == cif_comp_id:
                    return True, seq_key, coord_atom_site_

                _seq_key = (chain_id, seq_id, comp_id)

                if _seq_key in auth_to_orig_seq:
                    _seq_key_ = auth_to_orig_seq[_seq_key]

                    seq_key = (chain_id, _seq_key_[0])

                    if seq_key in coord_atom_site:
                        _coord_atom_site_ = coord_atom_site[seq_key]

                        if _coord_atom_site_['comp_id'] == comp_id:
                            return True, seq_key, _coord_atom_site_

            if (chain_id, seq_id) in label_to_auth_seq:
                _chain_id, _seq_id = label_to_auth_seq[(chain_id, seq_id)]

                if (_chain_id, _seq_id, comp_id) in auth_to_star_seq:
                    seq_key = (_chain_id, _seq_id)

                    if seq_key in coord_unobs_res:  # DAOTHER-7665
                        return True, None, None

                    if seq_key not in coord_atom_site:
                        return True, None, None

                    # 2lit: 1:104:LYS (nmr), A:99:LYS (model) overlaps A:104:HEC (model)
                    # if seq_key not in auth_to_label_seq:
                    #     return True, None, None

                    coord_atom_site_ = coord_atom_site[seq_key]

                    cif_comp_id = coord_atom_site_['comp_id']

                    if comp_id == cif_comp_id:
                        return True, seq_key, coord_atom_site_

            return False, None, None

        offset = {}

        for idx, row in enumerate(lp_data):

            for j in range(num_dim):
                try:
                    chain_id = row[chain_id_names[j]]
                    seq_id = alt_seq_id = row[seq_id_names[j]]
                    comp_id = row[comp_id_names[j]]
                    atom_id = row[atom_id_names[j]]
                    if file_type == 'nmr-star' and alt_seq_id_names[j] in row:
                        alt_seq_id = row[alt_seq_id_names[j]]
                except KeyError:
                    continue

                if content_subtype.startswith('spectral_peak')\
                   and (chain_id in EMPTY_VALUE or seq_id in EMPTY_VALUE or comp_id in EMPTY_VALUE or atom_id in EMPTY_VALUE):
                    continue

                if chain_id not in nmr2ca:
                    continue

                ca = next((ca['seq_align'] for ca in nmr2ca[chain_id]
                           if ('seq_unmap' not in ca or (seq_id not in ca['seq_unmap']))), None)  # DAOTHER-7465

                if ca is None:
                    continue

                cif_chain_id = ca['test_chain_id']

                cif_seq_id = next((test_seq_id for ref_seq_id, test_seq_id
                                   in zip(ca['ref_seq_id'], ca['test_auth_seq_id' if 'test_auth_seq_id' in ca else 'test_seq_id'])
                                   if ref_seq_id == seq_id), None)

                if cif_seq_id is None and ca['sequence_coverage'] >= LOW_SEQ_COVERAGE:
                    continue

                cif_ps = next(ps for ps in cif_poly_seq if ps['chain_id'] == cif_chain_id)

                if 'auth_chain_id' in cif_ps:
                    cif_chain_id = cif_ps['auth_chain_id']

                if ca['sequence_coverage'] < LOW_SEQ_COVERAGE:  # DAOTHER-8751, issue #2

                    if 'auth_seq_id' in cif_ps:
                        cif_seq_id, cif_comp_id = next(((_seq_id, _comp_id) for _auth_seq_id, _seq_id, _comp_id
                                                        in zip(cif_ps['auth_seq_id'], cif_ps['seq_id'], cif_ps['comp_id'])
                                                        if _auth_seq_id == seq_id), (None, None))
                    else:
                        cif_seq_id, cif_comp_id = next(((_seq_id, _comp_id) for _seq_id, _comp_id
                                                        in zip(cif_ps['seq_id'], cif_ps['comp_id'])
                                                        if _seq_id == seq_id), (None, None))

                    if None in (cif_seq_id, cif_comp_id):
                        continue

                else:

                    cif_comp_id = next((_comp_id for _seq_id, _comp_id
                                        in zip(cif_ps['auth_seq_id' if 'auth_seq_id' in cif_ps else 'seq_id'], cif_ps['comp_id'])
                                        if _seq_id == cif_seq_id), None)

                    if cif_comp_id is None:
                        continue

                    if cif_comp_id != comp_id and seq_id != cif_seq_id:
                        cif_comp_id = next((_comp_id for _seq_id, _comp_id
                                            in zip(cif_ps['auth_seq_id' if 'auth_seq_id' in cif_ps else 'seq_id'],
                                                   cif_ps['comp_id'])
                                            if _seq_id == seq_id), None)

                        if cif_comp_id is None:
                            continue

                        if cif_comp_id == comp_id:
                            cif_seq_id = seq_id

                if ca['sequence_coverage'] < LOW_SEQ_COVERAGE:

                    if 'auth_seq_id' in cif_ps:
                        cif_comp_id = next((_comp_id for _seq_id, _comp_id
                                            in zip(cif_ps['auth_seq_id'], cif_ps['comp_id'])
                                            if _seq_id == seq_id), None)
                    else:
                        cif_comp_id = next((_comp_id for _seq_id, _comp_id
                                            in zip(cif_ps['seq_id'], cif_ps['comp_id'])
                                            if _seq_id == seq_id), None)

                    if cif_comp_id is None:
                        continue

                if file_type == 'nef' or self.isNmrAtomName(comp_id, atom_id):
                    _atom_id, _, details = self._getAtomIdListWithAmbigCode(comp_id, atom_id)

                    len_atom_id = len(_atom_id)

                    if len_atom_id == 0:
                        continue

                    if len_atom_id == 1 and atom_id == _atom_id[0]:
                        atom_id_ = atom_id
                        atom_name = atom_id

                        if details is not None:
                            atom_name += f", where {details.rstrip('.')}"

                    else:
                        atom_name = f'{atom_id} (e.g. '

                        for atom_id_ in _atom_id:
                            atom_name += f'{atom_id_} '

                        atom_name = f'{atom_name.rstrip()})'

                        # representative atom id
                        atom_id_ = _atom_id[0]

                else:
                    atom_id_ = atom_id
                    atom_name = atom_id

                if len(auth_to_star_seq) == 0:
                    continue

                found, seq_key, coord_atom_site_ = get_coord_atom_site_of(cif_chain_id, cif_seq_id, comp_id)

                if found:

                    if seq_key is None:
                        continue

                    if seq_key in auth_to_label_seq:

                        offset[chain_id] = seq_key[1] - seq_id

                        cif_chain_id, cif_seq_id = auth_to_label_seq[seq_key]
                        cif_comp_id = comp_id

                        _seq_key = (seq_key[0], seq_key[1]) if len(seq_key) > 2 else seq_key

                        if _seq_key in coord_unobs_res:  # DAOTHER-7665
                            continue

                else:

                    if chain_id in offset:
                        _, seq_key, coord_atom_site_ = get_coord_atom_site_of(cif_chain_id, cif_seq_id + offset[chain_id], comp_id)

                        if seq_key is not None:
                            _seq_key = (seq_key[0], seq_key[1]) if len(seq_key) > 2 else seq_key

                            if _seq_key in coord_unobs_res:
                                continue

                    elif seq_key is not None:
                        seq_key = (cif_chain_id, cif_seq_id)

                        if seq_key in coord_unobs_res:  # DAOTHER-7665
                            continue

                        coord_atom_site_ = coord_atom_site.get(seq_key)

                    else:

                        for _offset in range(1, PERIPH_OFFSET_ATTEMPT):
                            if (cif_chain_id, cif_seq_id + _offset) in label_to_auth_seq:
                                _, _cif_seq_id = label_to_auth_seq[(cif_chain_id, cif_seq_id + _offset)]
                                if (cif_chain_id, _cif_seq_id) in auth_to_label_seq:
                                    cif_seq_id = _cif_seq_id - _offset

                                    seq_key = (cif_chain_id, cif_seq_id)
                                    break

                        if seq_key is not None:
                            _seq_key = (seq_key[0], seq_key[1]) if len(seq_key) > 2 else seq_key

                            if _seq_key in coord_unobs_res:  # DAOTHER-7665
                                continue

                    if file_type == 'nmr-star' and seq_id != alt_seq_id:

                        if coord_atom_site_ is None or coord_atom_site_['comp_id'] != cif_comp_id\
                           or (atom_id_ not in coord_atom_site_['atom_id']
                               and (('auth_atom_id' in coord_atom_site_ and atom_id_ not in coord_atom_site_['auth_atom_id'])
                                    or 'auth_atom_id' not in coord_atom_site_)):

                            cif_seq_id = next((test_seq_id for ref_seq_id, test_seq_id
                                               in zip(ca['ref_seq_id'], ca['test_auth_seq_id'])
                                               if ref_seq_id == alt_seq_id), None)

                            if cif_seq_id is None:
                                continue

                            cif_ps = next(ps for ps in cif_poly_seq if ps['chain_id'] == cif_chain_id)

                            cif_comp_id = next((_comp_id for _seq_id, _comp_id
                                                in zip(cif_ps['seq_id'], cif_ps['comp_id'])
                                                if _seq_id == cif_seq_id), None)

                            if cif_comp_id is None:
                                continue

                            seq_key = (cif_chain_id, cif_seq_id)

                            if seq_key in coord_unobs_res:  # DAOTHER-7665
                                continue

                            coord_atom_site_ = coord_atom_site.get(seq_key)

                if coord_atom_site_ is None and file_type == 'nmr-star':

                    if max_dim == 2:
                        auth_asym_id_name = 'Auth_asym_ID'
                        auth_seq_id_name = 'Auth_seq_ID'
                    else:
                        auth_asym_id_name = f'Auth_asym_ID_{j + 1}'
                        auth_seq_id_name = f'Auth_seq_ID_{j + 1}'

                    if auth_asym_id_name in row and auth_seq_id_name in row\
                       and row[auth_asym_id_name] not in EMPTY_VALUE\
                       and row[auth_seq_id_name] not in EMPTY_VALUE\
                       and (isinstance(row[auth_seq_id_name], int) or row[auth_seq_id_name].isdigit()):
                        cif_chain_id = row[auth_asym_id_name]
                        cif_seq_id = row[auth_seq_id_name]
                        if isinstance(cif_seq_id, str):
                            cif_seq_id = int(cif_seq_id)

                        _, seq_key, coord_atom_site_ = get_coord_atom_site_of(cif_chain_id, cif_seq_id, comp_id)

                        if coord_atom_site_ is not None:
                            cif_comp_id = coord_atom_site_['comp_id']

                if coord_atom_site_ is None or coord_atom_site_['comp_id'] != cif_comp_id\
                   or (atom_id_ not in coord_atom_site_['atom_id']
                       and (('auth_atom_id' in coord_atom_site_ and atom_id_ not in coord_atom_site_['auth_atom_id'])
                            or 'auth_atom_id' not in coord_atom_site_)):

                    idx_msg = ''
                    if index_tag is not None and index_tag in row:
                        idx_msg = f"[Check row of {index_tag} {row[index_tag]}] "

                    err = f"{idx_msg}Atom ("\
                        + self.getReducedAtomNotation(chain_id_names[j], chain_id, seq_id_names[j], seq_id,
                                                      comp_id_names[j], comp_id, atom_id_names[j], atom_name)\
                        + ") is not present in the coordinates."

                    cyclic = self.isCyclicPolymer(ref_chain_id)

                    if self._reg.nonblk_bad_nterm\
                       and (seq_id == 1 or cif_seq_id == 1 or ((seq_key[0], seq_key[1] - 1) if seq_key is not None
                                                               else (cif_chain_id, cif_seq_id - 1)) in coord_unobs_res)\
                       and atom_id_ in AMINO_PROTON_CODE\
                       and (cyclic or comp_id == 'PRO'
                            or (atom_id_ in PROTON_BEGIN_CODE
                                or (coord_atom_site_ is not None and 'auth_atom_id' not in coord_atom_site_))):  # DAOTHER-7665

                        err += " However, it is acceptable if corresponding atom name, H1, is given during biocuration "

                        if cyclic:
                            err += "because of a cyclic-peptide."
                        elif comp_id == 'PRO':
                            err += "because polymer sequence starts with the Proline residue."
                        else:  # DAOTHER-7665
                            err += "because polymer sequence starts with the residue in the coordinates."

                        self._reg.report.warning.appendDescription('auth_atom_nomenclature_mismatch',
                                                                   {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                    'category': lp_category, 'description': err})

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.testCoordAtomIdConsistency() "
                                                f"++ Warning  - {err}\n")

                        if cyclic and self._reg.bmrb_only and self._reg.leave_intl_note\
                           and file_type == 'nmr-star' and seq_id == 1 and details_col != -1:
                            _details = loop.data[idx][details_col]
                            details = f"{chain_id}:{seq_id}:{comp_id}:{atom_name} is not present in the coordinates. "\
                                "However, it is acceptable if an appropriate atom name, H1, is given because of a cyclic-peptide.\n"
                            if _details in EMPTY_VALUE or (details not in _details):
                                if _details in EMPTY_VALUE:
                                    loop.data[idx][details_col] = details
                                else:
                                    loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                modified = True

                    elif self._reg.nonblk_bad_nterm\
                            and (seq_id == 1 or cif_seq_id == 1
                                 or ((seq_key[0], seq_key[1] - 1)
                                     if seq_key is not None else (cif_chain_id, cif_seq_id - 1)) in coord_unobs_res)\
                            and atom_id_ == 'P':
                        continue

                    elif ca['conflict'] == 0:  # no conflict in sequence alignment

                        if comp_id in STD_MON_DICT:

                            checked = coord_issue = False
                            if atom_id_[0] in PROTON_BEGIN_CODE:
                                self._reg.ccU.updateChemCompDict(comp_id)
                                cca = next((cca for cca in self._reg.ccU.lastAtomDictList if cca['atom_id'] == atom_id_), None)
                                bonded_to = self._reg.ccU.getBondedAtoms(comp_id, atom_id_)
                                peptide_like = self._reg.csStat.peptideLike(comp_id)
                                if cca is not None and len(bonded_to) > 0:
                                    if coord_atom_site_ is not None and bonded_to[0] in coord_atom_site_['atom_id']\
                                       and (cca['leaving_atom_flag'] != 'Y'
                                            or (peptide_like
                                                and cca['n_terminal_atom_flag'] == 'N'
                                                and cca['c_terminal_atom_flag'] == 'N')):
                                        checked = True
                                        err = f"{idx_msg}Atom ("\
                                            + self.getReducedAtomNotation(chain_id_names[j], chain_id, seq_id_names[j], seq_id,
                                                                          comp_id_names[j], comp_id, atom_id_names[j], atom_name)\
                                            + ") is not properly instantiated in the coordinates. Please re-upload the model file."

                            if (self._reg.remediation_mode or self._reg.combined_mode) and checked:
                                continue

                            if not checked and err.endswith("not present in the coordinates."):

                                if atom_id_[0] in PROTON_BEGIN_CODE:
                                    bonded_to = self._reg.ccU.getBondedAtoms(comp_id, atom_id_)
                                    if len(bonded_to) > 0 and coord_atom_site_ is not None\
                                       and bonded_to[0] not in coord_atom_site_['atom_id']:
                                        err += " Additionally, the attached atom ("\
                                            + self.getReducedAtomNotation(chain_id_names[j], chain_id, seq_id_names[j], seq_id,
                                                                          comp_id_names[j], comp_id,
                                                                          atom_id_names[j], bonded_to[0])\
                                            + ") is not instantiated in the coordinates. Please re-upload the model file."
                                        coord_issue = True

                                elif 'coord_unobs_atom' in self._reg.caC:
                                    _seq_key = (seq_key[0], seq_key[1]) if seq_key is not None and len(seq_key) > 2 else seq_key

                                    if _seq_key in coord_unobs_atom and atom_id_ in coord_unobs_atom[_seq_key]['atom_ids']:
                                        coord_issue = True

                            _atom_id, _, _ = self._getAtomIdListWithAmbigCode(comp_id, f'{atom_id_}%')

                            if content_subtype.startswith('spectral_peak')\
                               or (len(_atom_id) > 0 and coord_atom_site_ is not None
                                   and _atom_id[0] in coord_atom_site_['atom_id']):

                                if len(_atom_id) > 0 and coord_atom_site_ is not None\
                                   and _atom_id[0] in coord_atom_site_['atom_id']:
                                    item = 'atom_nomenclature_mismatch'
                                elif content_subtype.startswith('spectral_peak'):
                                    item = 'hydrogen_not_instantiated' if checked\
                                        else 'coordinate_issue' if coord_issue else 'assigned_peak_atom_not_found'
                                else:
                                    item = 'hydrogen_not_instantiated' if checked\
                                        else 'coordinate_issue' if coord_issue else 'atom_nomenclature_mismatch'

                                self._reg.report.warning.appendDescription(item,
                                                                           {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                            'category': lp_category, 'description': err})

                                if self._reg.verbose:
                                    self._reg.log.write(f"+{self.__class_name__}.testCoordAtomIdConsistency() "
                                                        f"++ Warning  - {err}\n")

                            else:

                                item = 'hydrogen_not_instantiated' if checked\
                                    else 'coordinate_issue' if coord_issue else 'atom_not_found'

                                if self._reg.internal_mode and item in ('hydrogen_not_instantiated', 'coordinate_issue'):

                                    self._reg.report.warning.appendDescription(item,
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': err})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.testCoordAtomIdConsistency() "
                                                            f"++ Warning  - {err}\n")

                                else:

                                    if item == 'atom_not_found' and self._reg.internal_mode\
                                       and file_type == 'nmr-star' and details_col != -1:
                                        _details = loop.data[idx][details_col]
                                        if _details == 'UNMAPPED':
                                            continue

                                    if item == 'atom_not_found' and self._reg.op == 'nmr-str-replace-cs' and file_list_id > 0:
                                        item = 'atom_nomenclature_mismatch'

                                        self._reg.report.warning.appendDescription(item,
                                                                                   {'file_name': file_name,
                                                                                    'sf_framecode': sf_framecode,
                                                                                    'category': lp_category, 'description': err})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.testCoordAtomIdConsistency() "
                                                                f"++ Warning  - {err}\n")

                                        continue

                                    self._reg.report.error.appendDescription(item,
                                                                             {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                              'category': lp_category, 'description': err})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.testCoordAtomIdConsistency() "
                                                            f"++ Error  - {err}\n")

                        else:

                            if self._reg.combined_mode and self._reg.remediation_mode\
                               and self._reg.ccU.updateChemCompDict(comp_id):
                                cca = next((cca for cca in self._reg.ccU.lastAtomDictList if cca['atom_id'] == atom_id_), None)
                                bonded_to = self._reg.ccU.getBondedAtoms(comp_id, atom_id_)
                                peptide_like = self._reg.csStat.peptideLike(comp_id)
                                if cca is not None and len(bonded_to) > 0:
                                    if coord_atom_site_ is not None and bonded_to[0] in coord_atom_site_['atom_id']\
                                       and (cca['leaving_atom_flag'] != 'Y'
                                            or (peptide_like
                                                and cca['n_terminal_atom_flag'] == 'N'
                                                and cca['c_terminal_atom_flag'] == 'N')):
                                        err = f"{idx_msg}Atom ("\
                                            + self.getReducedAtomNotation(chain_id_names[j], chain_id, seq_id_names[j], seq_id,
                                                                          comp_id_names[j], comp_id, atom_id_names[j], atom_name)\
                                            + ") is not properly instantiated in the coordinates. Please re-upload the model file."

                                        self._reg.report.warning.appendDescription('hydrogen_not_instantiated',
                                                                                   {'file_name': file_name,
                                                                                    'sf_framecode': sf_framecode,
                                                                                    'category': lp_category, 'description': err})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.testCoordAtomIdConsistency() "
                                                                f"++ Warning  - {err}\n")

                                        continue

                            self._reg.report.warning.appendDescription('atom_nomenclature_mismatch',
                                                                       {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                        'category': lp_category, 'description': err})

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.testCoordAtomIdConsistency() "
                                                    f"++ Warning  - {err}\n")

        return modified
