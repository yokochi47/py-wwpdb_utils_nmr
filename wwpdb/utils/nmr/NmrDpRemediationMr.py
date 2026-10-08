##
# File: NmrDpRemediationMr.py
# Date: 17-Aug-2026
#
# Updates:
##
""" Remediation of NMR-STAR restraint loops.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.2"

from typing import Union

import numpy

import pynmrstar

try:
    from wwpdb.utils.nmr.NmrDpConstant import (SF_CATEGORIES,
                                               LP_CATEGORIES,
                                               ITEM_NAMES_IN_DIHED_LOOP,
                                               ITEM_NAMES_IN_RDC_LOOP,
                                               EMPTY_VALUE,
                                               MAX_DIM_NUM_OF_SPECTRA)
    from wwpdb.utils.nmr.NmrDpRemediationBase import NmrDpRemediationBase
except ImportError:
    from nmr.NmrDpConstant import (SF_CATEGORIES,
                                   LP_CATEGORIES,
                                   ITEM_NAMES_IN_DIHED_LOOP,
                                   ITEM_NAMES_IN_RDC_LOOP,
                                   EMPTY_VALUE,
                                   MAX_DIM_NUM_OF_SPECTRA)
    from nmr.NmrDpRemediationBase import NmrDpRemediationBase


class NmrDpRemediationMr(NmrDpRemediationBase):
    """ Remediation of NMR-STAR restraint loops.
    """
    __slots__ = ()

    def syncMrLoop(self) -> bool:
        """ Synchronize sequence scheme of restraint loop based on coordinates.
        """

        __errors = self._reg.report.getTotalErrors()

        for fileListId in range(self._reg.file_path_list_len):

            input_source = self._reg.report.input_sources[fileListId]
            input_source_dic = input_source.get()

            file_type = input_source_dic['file_type']

            if input_source_dic['content_subtype'] is None:
                continue

            for content_subtype in input_source_dic['content_subtype']:

                if content_subtype in ('entry_info', 'poly_seq', 'entity', 'chem_shift', 'chem_shift_ref'):
                    continue

                sf_category = SF_CATEGORIES[file_type][content_subtype]
                lp_category = LP_CATEGORIES[file_type][content_subtype]

                if file_type == 'nmr-star' and content_subtype == 'spectral_peak_alt':
                    lp_category = '_Assigned_peak_chem_shift'

                if self._reg.star_data_type[fileListId] == 'Loop':
                    sf = self._reg.star_data[fileListId]

                    self._syncMrLoop(fileListId, file_type, content_subtype, sf, lp_category)

                elif self._reg.star_data_type[fileListId] == 'Saveframe':
                    sf = self._reg.star_data[fileListId]

                    self._syncMrLoop(fileListId, file_type, content_subtype, sf, lp_category)

                else:

                    for sf in self._reg.star_data[fileListId].get_saveframes_by_category(sf_category):

                        if not any(True for loop in sf.loops if loop.category == lp_category):
                            continue

                        self._syncMrLoop(fileListId, file_type, content_subtype, sf, lp_category)

            return self._reg.report.getTotalErrors() == __errors

    def _syncMrLoop(self, file_list_id: int, file_type: str, content_subtype: str,
                    sf: Union[pynmrstar.Saveframe, pynmrstar.Loop], lp_category: str) -> None:
        """ Synchronize sequence scheme of restraint loop based on coordinates.
        """

        loop = sf if self._reg.star_data_type[file_list_id] == 'Loop' else sf.get_loop(lp_category)

        if file_type == 'nef':

            chain_id_name = 'chain_code'
            seq_id_name = 'sequence_code'

            if chain_id_name in loop.tags:
                tags = [chain_id_name, seq_id_name]
                dat = loop.get_tag(tags)
                for row in dat:
                    try:
                        seq_key = (row[0], int(row[1]))
                        if seq_key in self._reg.seq_id_map_for_remediation:
                            row[0], row[1] = self._reg.seq_id_map_for_remediation[seq_key]
                    except (ValueError, TypeError):
                        if row[0] in self._reg.chain_id_map_for_remediation:
                            row[0] = self._reg.chain_id_map_for_remediation[row[0]]

            else:
                for j in range(1, MAX_DIM_NUM_OF_SPECTRA):
                    chain_id_name = f'chain_code_{j}'
                    seq_id_name = f'sequence_code_{j}'
                    if chain_id_name not in loop.tags:
                        break
                    tags = [chain_id_name, seq_id_name]
                    dat = loop.get_tag(tags)
                    for row in dat:
                        try:
                            seq_key = (row[0], int(row[1]))
                            if seq_key in self._reg.seq_id_map_for_remediation:
                                row[0], row[1] = self._reg.seq_id_map_for_remediation[seq_key]
                        except (ValueError, TypeError):
                            if row[0] in self._reg.chain_id_map_for_remediation:
                                row[0] = self._reg.chain_id_map_for_remediation[row[0]]

        else:

            if content_subtype == 'ccr_d_csa_restraint':
                for interaction in ['Dipole', 'CSA']:
                    for j in range(1, 3):
                        chain_id_name = f'{interaction}_entity_assembly_ID_{j}'
                        seq_id_name = f'{interaction}_comp_index_ID_{j}'
                        alt_seq_id_name = f'{interaction}_seq_ID_{j}'
                        if alt_seq_id_name in loop.tags:
                            tags = [chain_id_name, seq_id_name, alt_seq_id_name]
                            dat = loop.get_tag(tags)
                            for row in dat:
                                try:
                                    seq_key = (row[0], int(row[1]))
                                    if seq_key in self._reg.seq_id_map_for_remediation:
                                        row[0], row[1] = self._reg.seq_id_map_for_remediation[seq_key]
                                        row[2] = row[1]
                                except (ValueError, TypeError):
                                    if row[0] in self._reg.chain_id_map_for_remediation:
                                        row[0] = self._reg.chain_id_map_for_remediation[row[0]]

                        else:
                            tags = [chain_id_name, seq_id_name]
                            dat = loop.get_tag(tags)
                            for row in dat:
                                try:
                                    seq_key = (row[0], int(row[1]))
                                    if seq_key in self._reg.seq_id_map_for_remediation:
                                        row[0], row[1] = self._reg.seq_id_map_for_remediation[seq_key]
                                except (ValueError, TypeError):
                                    if row[0] in self._reg.chain_id_map_for_remediation:
                                        row[0] = self._reg.chain_id_map_for_remediation[row[0]]

            elif content_subtype == 'ccr_dd_restraint':
                for interaction in ['Dipole_1', 'Dipole_2']:
                    for j in range(1, 3):
                        chain_id_name = f'{interaction}_entity_assembly_ID_{j}'
                        seq_id_name = f'{interaction}_comp_index_ID_{j}'
                        alt_seq_id_name = f'{interaction}_seq_ID_{j}'
                        if alt_seq_id_name in loop.tags:
                            tags = [chain_id_name, seq_id_name, alt_seq_id_name]
                            dat = loop.get_tag(tags)
                            for row in dat:
                                try:
                                    seq_key = (row[0], int(row[1]))
                                    if seq_key in self._reg.seq_id_map_for_remediation:
                                        row[0], row[1] = self._reg.seq_id_map_for_remediation[seq_key]
                                        row[2] = row[1]
                                except (ValueError, TypeError):
                                    if row[0] in self._reg.chain_id_map_for_remediation:
                                        row[0] = self._reg.chain_id_map_for_remediation[row[0]]

                        else:
                            tags = [chain_id_name, seq_id_name]
                            dat = loop.get_tag(tags)
                            for row in dat:
                                try:
                                    seq_key = (row[0], int(row[1]))
                                    if seq_key in self._reg.seq_id_map_for_remediation:
                                        row[0], row[1] = self._reg.seq_id_map_for_remediation[seq_key]
                                except (ValueError, TypeError):
                                    if row[0] in self._reg.chain_id_map_for_remediation:
                                        row[0] = self._reg.chain_id_map_for_remediation[row[0]]

            else:
                chain_id_name = 'Entity_assembly_ID'
                seq_id_name = 'Comp_index_ID'
                alt_seq_id_name = 'Seq_ID'

                if chain_id_name in loop.tags:
                    if alt_seq_id_name in loop.tags:
                        tags = [chain_id_name, seq_id_name, alt_seq_id_name]
                        dat = loop.get_tag(tags)
                        for row in dat:
                            try:
                                seq_key = (row[0], int(row[1]))
                                if seq_key in self._reg.seq_id_map_for_remediation:
                                    row[0], row[1] = self._reg.seq_id_map_for_remediation[seq_key]
                                    row[2] = row[1]
                            except (ValueError, TypeError):
                                if row[0] in self._reg.chain_id_map_for_remediation:
                                    row[0] = self._reg.chain_id_map_for_remediation[row[0]]

                    else:
                        tags = [chain_id_name, seq_id_name]
                        dat = loop.get_tag(tags)
                        for row in dat:
                            try:
                                seq_key = (row[0], int(row[1]))
                                if seq_key in self._reg.seq_id_map_for_remediation:
                                    row[0], row[1] = self._reg.seq_id_map_for_remediation[seq_key]
                            except (ValueError, TypeError):
                                if row[0] in self._reg.chain_id_map_for_remediation:
                                    row[0] = self._reg.chain_id_map_for_remediation[row[0]]

                else:
                    for j in range(1, MAX_DIM_NUM_OF_SPECTRA):
                        chain_id_name = f'Entity_assembly_ID_{j}'
                        seq_id_name = f'Comp_index_ID_{j}'
                        alt_seq_id_name = f'Seq_ID_{j}'
                        if chain_id_name not in loop.tags:
                            break
                        if alt_seq_id_name in loop.tags:
                            tags = [chain_id_name, seq_id_name, alt_seq_id_name]
                            dat = loop.get_tag(tags)
                            for row in dat:
                                try:
                                    seq_key = (row[0], int(row[1]))
                                    if seq_key in self._reg.seq_id_map_for_remediation:
                                        row[0], row[1] = self._reg.seq_id_map_for_remediation[seq_key]
                                        row[2] = row[1]
                                except (ValueError, TypeError):
                                    if row[0] in self._reg.chain_id_map_for_remediation:
                                        row[0] = self._reg.chain_id_map_for_remediation[row[0]]
                        else:
                            tags = [chain_id_name, seq_id_name]
                            dat = loop.get_tag(tags)
                            for row in dat:
                                try:
                                    seq_key = (row[0], int(row[1]))
                                    if seq_key in self._reg.seq_id_map_for_remediation:
                                        row[0], row[1] = self._reg.seq_id_map_for_remediation[seq_key]
                                except (ValueError, TypeError):
                                    if row[0] in self._reg.chain_id_map_for_remediation:
                                        row[0] = self._reg.chain_id_map_for_remediation[row[0]]

    def remediateDihedLoop(self, file_type: str, loop: pynmrstar.Loop) -> bool:  # pylint: disable=no-self-use
        """ Remediate dihedral angle target values in radian unit, if required.
        """

        modified = False

        item_names = ITEM_NAMES_IN_DIHED_LOOP[file_type]

        tags = [item_names['angle_type'], item_names['comp_id_2'],
                item_names['lower_limit'], item_names['target_value'], item_names['upper_limit']]

        if set(tags) & set(loop.tags) == set(tags):

            dat = loop.get_tag(tags)

            is_rad = False

            for idx, row in enumerate(dat):

                angle_type, comp_id, lower_limit, target_value, upper_limit =\
                    row[0], row[1], row[2], row[3], row[4]

                if angle_type not in ('PHI', 'PSI'):
                    continue

                if not self._reg.csStat.peptideLike(comp_id):
                    continue

                if target_value not in EMPTY_VALUE\
                   and lower_limit not in EMPTY_VALUE\
                   and upper_limit not in EMPTY_VALUE:
                    target_value = float(target_value)
                    lower_limit = float(lower_limit)
                    upper_limit = float(upper_limit)

                    if -3.12 < target_value < 3.12\
                       and 0.0 <= target_value - lower_limit < 1.0\
                       and 0.0 <= upper_limit - target_value < 1.0:
                        is_rad = True
                        break

            if is_rad:
                target_value_col = loop.tags.index(item_names['target_value'])
                lower_limit_col = loop.tags.index(item_names['lower_limit'])
                upper_limit_col = loop.tags.index(item_names['upper_limit'])
                lower_linear_limit_col = loop.tags.index(item_names['lower_linear_limit'])\
                    if item_names['lower_linear_limit'] in loop.tags else -1
                upper_linear_limit_col = loop.tags.index(item_names['upper_linear_limit'])\
                    if item_names['upper_linear_limit'] in loop.tags else -1

                for idx, row in enumerate(loop):
                    if row[target_value_col] not in EMPTY_VALUE:
                        loop.data[idx][target_value_col] = f'{numpy.degrees(float(row[target_value_col])):.3f}'
                    if row[lower_limit_col] not in EMPTY_VALUE:
                        loop.data[idx][lower_limit_col] = f'{numpy.degrees(float(row[lower_limit_col])):.3f}'
                    if row[upper_limit_col] not in EMPTY_VALUE:
                        loop.data[idx][upper_limit_col] = f'{numpy.degrees(float(row[upper_limit_col])):.3f}'
                    if lower_linear_limit_col != -1 and row[lower_linear_limit_col] not in EMPTY_VALUE:
                        loop.data[idx][lower_linear_limit_col] = f'{numpy.degrees(float(row[lower_linear_limit_col])):.3f}'
                    if upper_linear_limit_col != -1 and row[upper_linear_limit_col] not in EMPTY_VALUE:
                        loop.data[idx][upper_linear_limit_col] = f'{numpy.degrees(float(row[upper_linear_limit_col])):.3f}'

                modified = True

        return modified

    def remediateRdcLoop(self, file_type: str, loop: pynmrstar.Loop) -> bool:  # pylint: disable=no-self-use
        """ Remediate RDC target value due to the known OneDep bug, if required.
        """

        modified = False

        item_names = ITEM_NAMES_IN_RDC_LOOP[file_type]

        tags = [item_names['lower_limit'], item_names['target_value'], item_names['upper_limit']]

        if set(tags) & set(loop.tags) == set(tags):
            val_col = loop.tags.index(item_names['target_value'])

            dat = loop.get_tag(tags)

            for idx, row in enumerate(dat):

                if any(True for col in row if col in EMPTY_VALUE):
                    continue

                lower_limit, target_value, upper_limit = float(row[0]), float(row[1]), float(row[2])

                if abs((lower_limit + upper_limit) / 2.0 + target_value) < 0.01:
                    loop.data[idx][val_col] = str(-target_value)
                    modified = True

        return modified
