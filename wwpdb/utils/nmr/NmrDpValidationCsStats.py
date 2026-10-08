##
# File: NmrDpValidationCsStats.py
# Date: 17-Aug-2026
#
# Updates:
##
""" Statistics of assigned chemical shifts for NMR data validation.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.2"

from typing import List, Optional, Union

import pynmrstar

try:
    from wwpdb.utils.nmr.NmrDpConstant import (LP_CATEGORIES,
                                               INDEX_TAGS,
                                               NUM_DIM_ITEMS,
                                               ITEM_NAMES_IN_CS_LOOP,
                                               LOW_SEQ_COVERAGE,
                                               EMPTY_VALUE,
                                               STD_MON_DICT,
                                               PROTON_BEGIN_CODE,
                                               MAX_DIM_NUM_OF_SPECTRA,
                                               MAX_ROWS_TO_PERFORM_REDUNDANCY_CHECK)
    from wwpdb.utils.nmr.AlignUtil import letterToDigit
    from wwpdb.utils.nmr.CifToNmrStar import (has_key_value,
                                              get_first_sf_tag)
    from wwpdb.utils.nmr.NmrVrptUtility import (predict_redox_state_of_cysteine,
                                                predict_cis_trans_peptide_of_proline,
                                                predict_tautomer_state_of_histidine,
                                                predict_rotamer_state_of_leucine,
                                                predict_rotamer_state_of_valine,
                                                predict_rotamer_state_of_isoleucine)
    from wwpdb.utils.nmr.NmrDpValidationBase import (NmrDpValidationBase,
                                                     get_atom_name_mapping)
except ImportError:
    from nmr.NmrDpConstant import (LP_CATEGORIES,
                                   INDEX_TAGS,
                                   NUM_DIM_ITEMS,
                                   ITEM_NAMES_IN_CS_LOOP,
                                   LOW_SEQ_COVERAGE,
                                   EMPTY_VALUE,
                                   STD_MON_DICT,
                                   PROTON_BEGIN_CODE,
                                   MAX_DIM_NUM_OF_SPECTRA,
                                   MAX_ROWS_TO_PERFORM_REDUNDANCY_CHECK)
    from nmr.AlignUtil import letterToDigit
    from nmr.CifToNmrStar import (has_key_value,
                                  get_first_sf_tag)
    from nmr.NmrVrptUtility import (predict_redox_state_of_cysteine,
                                    predict_cis_trans_peptide_of_proline,
                                    predict_tautomer_state_of_histidine,
                                    predict_rotamer_state_of_leucine,
                                    predict_rotamer_state_of_valine,
                                    predict_rotamer_state_of_isoleucine)
    from nmr.NmrDpValidationBase import (NmrDpValidationBase,
                                         get_atom_name_mapping)


class NmrDpValidationCsStats(NmrDpValidationBase):
    """ Statistics of assigned chemical shifts for NMR data validation.
    """
    __slots__ = ()

    def calculateStatsOfExptlData(self, file_list_id: int, file_name: str, file_type: str, content_subtype: str,
                                  sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                                  list_id: int, sf_framecode: str, lp_category: str, seq_align_dic: dict, asm: list) -> None:
        """ Calculate statistics of experimental data.
        """

        index_tag = INDEX_TAGS[file_type][content_subtype]

        _list_id = list_id
        if file_type == 'nmr-star' and self._reg.combined_mode:
            val = get_first_sf_tag(sf, 'ID')
            if isinstance(val, int):
                _list_id = val
            elif len(val) > 0:
                try:
                    _list_id = int(val)
                except ValueError:
                    return

        if content_subtype != 'poly_seq':
            lp_data = next((lp['data'] for lp in self._reg.lp_data[content_subtype]
                            if lp['sf_framecode'] == sf_framecode), None)
        else:
            lp_data = next((lp['data'] for lp in self._reg.aux_data[content_subtype]
                           if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode
                           and lp['category'] == lp_category), None)

        if lp_data is None or len(lp_data) == 0:

            if content_subtype == 'spectral_peak':

                ent = {'list_id': _list_id, 'sf_framecode': sf_framecode, 'number_of_rows': 0}

                try:

                    _num_dim = get_first_sf_tag(sf, NUM_DIM_ITEMS[file_type])
                    num_dim = int(_num_dim)

                    if num_dim not in range(1, MAX_DIM_NUM_OF_SPECTRA):
                        raise ValueError()

                except ValueError:  # raised error already at testIndexConsistency()
                    return

                self._calculateStatsOfSpectralPeak(file_list_id, sf_framecode, num_dim, lp_data, ent)

                has_err = self._reg.report.error.exists(file_name, sf_framecode)
                has_warn = self._reg.report.warning.exists(file_name, sf_framecode)

                original_file_name = get_first_sf_tag(sf, 'Data_file_name')
                if len(original_file_name) > 0:
                    has_err |= self._reg.report.error.exists(None, sf_framecode)
                    has_warn |= self._reg.report.warning.exists(None, sf_framecode)

                if has_err:
                    status = 'Error'
                    ent['error_descriptions'] =\
                        self._reg.report.error.getCombinedDescriptions(file_name, sf_framecode, original_file_name)
                    if has_warn:
                        ent['warning_descriptions'] =\
                            self._reg.report.warning.getCombinedDescriptions(file_name, sf_framecode, original_file_name)
                elif has_warn:
                    status = 'Warning'
                    ent['warning_descriptions'] =\
                        self._reg.report.warning.getCombinedDescriptions(file_name, sf_framecode, original_file_name)
                else:
                    status = 'OK'

                ent['status'] = status

                asm.append(ent)

            return

        ambig = False

        if file_type == 'nmr-star' and self._reg.star_data_type[0] == 'Entry':

            _sf_category = 'constraint_statistics'
            _lp_category = '_Constraint_file'

            try:

                tagNames = [t[0] for t in sf.tags]

                if 'Block_ID' in tagNames:
                    block_id = get_first_sf_tag(sf, 'Block_ID')

                    _sf = self._reg.star_data[0].get_saveframes_by_category(_sf_category)

                    _loop = _sf[0].get_loop(_lp_category)

                    _block_id_col = _loop.tags.index('Block_ID')
                    _constraint_type_col = _loop.tags.index('Constraint_type')
                    _constraint_subtype_col = _loop.tags.index('Constraint_subtype')
                    _constraint_subsubtype_col = _loop.tags.index('Constraint_subsubtype')

                    _row = next((_row for _row in _loop if _row[_block_id_col] == block_id), None)

                    if _row is not None:
                        _constraint_type = _row[_constraint_type_col]
                        _constraint_subtype = _row[_constraint_subtype_col]
                        _constraint_subsubtype = _row[_constraint_subsubtype_col]

                        if (_constraint_type == 'distance' and _constraint_subtype not in ('NOE', 'ROE'))\
                           or ('dihedral angle' in _constraint_type and _constraint_subtype == 'unknown'):
                            ambig = True

                        if _constraint_subsubtype not in EMPTY_VALUE and _constraint_subsubtype == 'ambi':
                            ambig = True

            except (IndexError, ValueError):
                pass

        sf_tag_data = next((t['data'] for t in self._reg.sf_tag_data[content_subtype]
                            if t['file_name'] == file_name and t['sf_framecode'] == sf_framecode), None)

        ent = {'list_id': _list_id, 'sf_framecode': sf_framecode, 'number_of_rows': len(lp_data)}

        if content_subtype in ('dist_restraint', 'dihed_restraint', 'rdc_restraint'):

            if len(sf_framecode) == 0:
                ent['exp_type'] = 'Unknown'
            else:
                ctype = get_first_sf_tag(sf, 'restraint_origin' if file_type == 'nef' else 'Constraint_type')
                if len(ctype) > 0:
                    ent['exp_type'] = ctype
                else:
                    ent['exp_type'] = 'Unknown'

        elif content_subtype.startswith('spectral_peak'):

            if len(sf_framecode) == 0:
                ent['exp_type'] = 'Unknown'
            else:
                ctype = get_first_sf_tag(sf, 'experiment_type' if file_type == 'nef' else 'Experiment_type')
                if len(ctype) > 0:
                    ent['exp_type'] = ctype
                else:
                    ent['exp_type'] = 'Unknown'

                if file_type == 'nmr-star':
                    exp_class = get_first_sf_tag(sf, 'Experiment_class')
                    if len(exp_class) > 0:
                        ent['exp_class'] = exp_class

        if content_subtype in ('chem_shift', 'dist_restraint', 'dihed_restraint', 'rdc_restraint',
                               'spectral_peak', 'spectral_peak_alt'):

            sa_name = f'nmr_poly_seq_vs_{content_subtype}'

            if has_key_value(seq_align_dic, sa_name):

                low_seq_coverage = ''

                seq_coverage = []

                for seq_align in seq_align_dic[sa_name]:

                    if seq_align['list_id'] == list_id:

                        sc = {}
                        sc['chain_id'] = seq_align['chain_id']
                        sc['length'] = seq_align['length']
                        sc['sequence_coverage'] = seq_align['sequence_coverage']

                        if seq_align['sequence_coverage'] < LOW_SEQ_COVERAGE and seq_align['length'] > 1 and not ambig:
                            if ('exp_type' not in ent)\
                               or (ent['exp_type'] not in ('disulfide bound', 'disulfide_bond',
                                                           'paramagnetic relaxation', 'pre', 'symmetry',
                                                           'J-couplings', 'jcoupling')):
                                low_seq_coverage += f"coverage {seq_align['sequence_coverage']} "\
                                    f"for chain_id {seq_align['chain_id']}, "\
                                    f"length {seq_align['length']}, "

                        seq_coverage.append(sc)

                if len(seq_coverage) > 0:

                    ent['sequence_coverage'] = seq_coverage

                    if len(low_seq_coverage) > 0 and not ambig:

                        warn = "Sequence coverage of NMR experimental data is relatively low ("\
                            + low_seq_coverage[:-2] + f") in {sf_framecode!r} saveframe."

                        self._reg.report.warning.appendDescription('insufficient_data',
                                                                   {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                    'category': lp_category, 'description': warn})

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.calculateStatsOfExptlData() ++ Warning  - {warn}\n")

                if content_subtype == 'chem_shift':

                    try:

                        item_names = ITEM_NAMES_IN_CS_LOOP[file_type]

                        anomalous_errs =\
                            self._reg.report.error.getValueListWithSf('anomalous_data', sf_framecode, key='Z_score')
                        anomalous_warns =\
                            self._reg.report.warning.getValueListWithSf('anomalous_data', sf_framecode, key='Z_score')
                        unusual_warns =\
                            self._reg.report.warning.getValueListWithSf('unusual_data', sf_framecode, key='Z_score')

                        cs_ann = []

                        if anomalous_errs is not None:

                            for a_err in anomalous_errs:
                                ann = {}
                                ann['level'] = 'anomalous'
                                ann['chain_id'] = a_err['row_location'][item_names['chain_id']]
                                ann['seq_id'] = int(a_err['row_location'][item_names['seq_id']])
                                ann['comp_id'] = a_err['row_location'][item_names['comp_id']]
                                ann['atom_id'] = a_err['row_location'][item_names['atom_id']]
                                ann['value'] = a_err['value']
                                ann['z_score'] = a_err['z_score']

                                comp_id = ann['comp_id']
                                atom_id = ann['atom_id'].split(' ')[0]

                                polypeptide_like = self._reg.csStat.peptideLike(comp_id)

                                if self._reg.csStat.hasSufficientStat(comp_id, polypeptide_like):
                                    non_rep_methyl_pros = self._reg.csStat.getNonRepMethylProtons(comp_id)

                                    if atom_id in non_rep_methyl_pros:
                                        continue

                                cs_ann.append(ann)

                        if anomalous_warns is not None:

                            for a_warn in anomalous_warns:
                                ann = {}
                                ann['level'] = 'anomalous'
                                ann['chain_id'] = a_warn['row_location'][item_names['chain_id']]
                                ann['seq_id'] = int(a_warn['row_location'][item_names['seq_id']])
                                ann['comp_id'] = a_warn['row_location'][item_names['comp_id']]
                                ann['atom_id'] = a_warn['row_location'][item_names['atom_id']]
                                ann['value'] = a_warn['value']
                                ann['z_score'] = a_warn['z_score']

                                comp_id = ann['comp_id']
                                atom_id = ann['atom_id'].split(' ')[0]

                                polypeptide_like = self._reg.csStat.peptideLike(comp_id)

                                if self._reg.csStat.hasSufficientStat(comp_id, polypeptide_like):
                                    non_rep_methyl_pros = self._reg.csStat.getNonRepMethylProtons(comp_id)

                                    if atom_id in non_rep_methyl_pros:
                                        continue

                                cs_ann.append(ann)

                        if unusual_warns is not None:

                            for u_warn in unusual_warns:
                                ann = {}
                                ann['level'] = 'unusual'
                                ann['chain_id'] = u_warn['row_location'][item_names['chain_id']]
                                ann['seq_id'] = int(u_warn['row_location'][item_names['seq_id']])
                                ann['comp_id'] = u_warn['row_location'][item_names['comp_id']]
                                ann['atom_id'] = u_warn['row_location'][item_names['atom_id']]
                                ann['value'] = u_warn['value']
                                ann['z_score'] = u_warn['z_score']

                                comp_id = ann['comp_id']
                                atom_id = ann['atom_id'].split(' ')[0]

                                polypeptide_like = self._reg.csStat.peptideLike(comp_id)

                                if self._reg.csStat.hasSufficientStat(comp_id, polypeptide_like):
                                    non_rep_methyl_pros = self._reg.csStat.getNonRepMethylProtons(comp_id)

                                    if atom_id in non_rep_methyl_pros:
                                        continue

                                cs_ann.append(ann)

                    except Exception as e:  # pylint: disable=broad-exception-caught

                        self._reg.report.error.appendDescription('internal_error',
                                                                 f"+{self.__class_name__}.calculateStatsOfExptlData() "
                                                                 "++ Error  - " + str(e))

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.calculateStatsOfExptlData() ++ Error  - {str(e)}\n")

                    self._calculateStatsOfAssignedChemShift(file_list_id, sf_framecode, lp_data, cs_ann, ent)

                elif content_subtype in ('dist_restraint', 'dihed_restraint', 'rdc_restraint')\
                        and len(lp_data) <= MAX_ROWS_TO_PERFORM_REDUNDANCY_CHECK:

                    conflict_id_set =\
                        self._reg.nefT.get_conflict_id_set(sf, lp_category,
                                                           self._reg.consist_key_items[file_type][content_subtype])[0]

                    conflict_warns = self._reg.report.warning.getValueListWithSf('conflicted_data', sf_framecode)
                    inconsist_warns = self._reg.report.warning.getValueListWithSf('inconsistent_data', sf_framecode)
                    redundant_warns = self._reg.report.warning.getValueListWithSf('redundant_data', sf_framecode)

                    inconsistent = set()
                    redundant = set()

                    if conflict_warns is not None:

                        for item in conflict_warns:
                            if 'row_locations' in item:
                                for index in item['row_locations'][index_tag]:
                                    inconsistent.add(int(index))

                    if inconsist_warns is not None:

                        for item in inconsist_warns:
                            if 'row_locations' in item:
                                for index in item['row_locations'][index_tag]:
                                    inconsistent.add(int(index))

                    if redundant_warns is not None:

                        for item in redundant_warns:
                            if 'row_locations' in item:
                                for index in item['row_locations'][index_tag]:
                                    redundant.add(int(index))

                    if content_subtype == 'dist_restraint':
                        self._calculateStatsOfDistanceRestraint(file_list_id, sf_framecode,
                                                                lp_data, conflict_id_set, inconsistent, redundant, ent)

                    elif content_subtype == 'dihed_restraint':
                        self._calculateStatsOfDihedralRestraint(file_list_id, sf_framecode,
                                                                lp_data, conflict_id_set, inconsistent, redundant, ent)

                    elif content_subtype == 'rdc_restraint':
                        self._calculateStatsOfRdcRestraint(file_list_id, sf_framecode,
                                                           lp_data, conflict_id_set, inconsistent, redundant, ent)

            if content_subtype.startswith('spectral_peak'):

                try:

                    _num_dim = get_first_sf_tag(sf, NUM_DIM_ITEMS[file_type])
                    num_dim = int(_num_dim)

                    if num_dim not in range(1, MAX_DIM_NUM_OF_SPECTRA):
                        raise ValueError()

                except ValueError:  # raised error already at testIndexConsistency()
                    return

                if content_subtype == 'spectral_peak':
                    self._calculateStatsOfSpectralPeak(file_list_id, sf_framecode, num_dim, lp_data, ent)
                elif content_subtype == 'spectral_peak_alt':
                    self._calculateStatsOfSpectralPeakAlt(file_list_id, sf_framecode, num_dim, lp_data, ent)

        elif content_subtype == 'poly_seq':
            self._calculateStatsOfCovalentBond(file_list_id, sf_framecode, lp_category, lp_data, ent)

        elif content_subtype == 'chem_shift_ref':
            ent['loop'] = lp_data
            ent['saveframe_tag'] = sf_tag_data

        has_err = self._reg.report.error.exists(file_name, sf_framecode)
        has_warn = self._reg.report.warning.exists(file_name, sf_framecode)

        original_file_name = get_first_sf_tag(sf, 'Data_file_name')
        if len(original_file_name) > 0:
            has_err |= self._reg.report.error.exists(None, sf_framecode)
            has_warn |= self._reg.report.warning.exists(None, sf_framecode)

        if has_err:
            status = 'Error'
            ent['error_descriptions'] =\
                self._reg.report.error.getCombinedDescriptions(file_name, sf_framecode, original_file_name)
            if has_warn:
                ent['warning_descriptions'] =\
                    self._reg.report.warning.getCombinedDescriptions(file_name, sf_framecode, original_file_name)
        elif has_warn:
            status = 'Warning'
            ent['warning_descriptions'] =\
                self._reg.report.warning.getCombinedDescriptions(file_name, sf_framecode, original_file_name)
        else:
            status = 'OK'

        ent['status'] = status

        asm.append(ent)

    def _calculateStatsOfAssignedChemShift(self, file_list_id: int, sf_framecode: str,
                                           lp_data: List[dict], cs_ann: List[dict], ent: dict) -> None:
        """ Calculate statistics of assigned chemical shifts.
        """

        input_source = self._reg.report.input_sources[file_list_id]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        item_names = ITEM_NAMES_IN_CS_LOOP[file_type]
        chain_id_name = item_names['chain_id']
        seq_id_name = item_names['seq_id']
        comp_id_name = item_names['comp_id']
        atom_id_name = item_names['atom_id']
        value_name = item_names['value']
        atom_type = item_names['atom_type']
        iso_number = item_names['isotope_number']
        alt_chain_id_name = item_names['alt_chain_id'] if file_type == 'nmr-star' else None
        chain_id_map = {}

        try:

            count = {}

            for row in lp_data:

                if row[atom_type] in EMPTY_VALUE or row[iso_number] in EMPTY_VALUE or row[value_name] in EMPTY_VALUE:
                    continue

                data_type = f'{row[iso_number]}{row[atom_type].lower()}_chemical_shifts'

                if data_type in count:
                    count[data_type] += 1
                else:
                    count[data_type] = 1

            if len(count) > 0:
                ent['number_of_assignments'] = count

            poly_seq = input_source_dic['polymer_sequence']

            if poly_seq is None:
                return

            if 'sequence_coverage' in ent:

                completeness = []

                for sc in ent['sequence_coverage']:

                    cc = {}

                    chain_id = sc['chain_id']

                    _chain_id = chain_id if file_type == 'nef' or self._reg.remediation_mode else str(letterToDigit(chain_id))

                    cc['chain_id'] = chain_id

                    # all atoms

                    all_c, excluded_comp_id, excluded_atom_id = [], [], []

                    h1_col = c13_col = n15_col = p31_col = -1

                    col = 0

                    for data_type in count:

                        atom_group = {}
                        atom_group['atom_group'] = f'all_{data_type}'
                        atom_group['number_of_assigned_shifts'] = 0
                        atom_group['number_of_target_shifts'] = 0
                        atom_group['completeness'] = 0.0

                        if data_type.startswith('1h'):
                            h1_col = col

                        elif data_type.startswith('13c'):
                            c13_col = col

                        elif data_type.startswith('15n'):
                            n15_col = col

                        elif data_type.startswith('31p'):
                            p31_col = col

                        all_c.append(atom_group)

                        col += 1

                    ps = next((ps for ps in poly_seq if ps['chain_id'] == chain_id), None)

                    if ps is not None:

                        for seq_id, comp_id in zip(ps['seq_id'], ps['comp_id']):

                            polypeptide_like = self._reg.csStat.peptideLike(comp_id)

                            if self._reg.csStat.hasSufficientStat(comp_id, polypeptide_like):

                                all_atoms = self._reg.csStat.getAllAtoms(comp_id, excl_minor_atom=True, primary=polypeptide_like)
                                non_excl_atoms = self._reg.csStat.getAllAtoms(comp_id, excl_minor_atom=False)
                                non_rep_methyl_pros = self._reg.csStat.getNonRepMethylProtons(comp_id)

                                for a in all_atoms:

                                    if h1_col != -1 and a not in non_rep_methyl_pros and a[0] in PROTON_BEGIN_CODE:
                                        all_c[h1_col]['number_of_target_shifts'] += 1

                                    elif c13_col != -1 and a.startswith('C'):
                                        all_c[c13_col]['number_of_target_shifts'] += 1

                                    elif n15_col != -1 and a.startswith('N'):
                                        all_c[n15_col]['number_of_target_shifts'] += 1

                                    elif p31_col != -1 and a.startswith('P'):
                                        all_c[p31_col]['number_of_target_shifts'] += 1

                                atom_set = set()

                                for row in lp_data:

                                    if row[chain_id_name] != _chain_id:
                                        if alt_chain_id_name is None or alt_chain_id_name not in row\
                                           or row[alt_chain_id_name] != _chain_id:
                                            continue
                                        _chain_id = chain_id_map[_chain_id] = row[chain_id_name]

                                    if row[seq_id_name] != seq_id or row[comp_id_name] != comp_id\
                                       or row[value_name] in EMPTY_VALUE:
                                        continue

                                    atom_id = row[atom_id_name]

                                    if None in (row[iso_number], row[atom_type]):
                                        continue

                                    data_type = str(row[iso_number]) + row[atom_type]

                                    if file_type == 'nef' or self.isNmrAtomName(comp_id, atom_id):
                                        atom_ids = self.getAtomIdList(comp_id, atom_id)

                                        if len(atom_ids) == 0:
                                            continue

                                        for a in atom_ids:

                                            if a in atom_set:
                                                continue

                                            atom_set.add(a)

                                            if a in all_atoms:

                                                if data_type == '1H' and h1_col != -1\
                                                   and a not in non_rep_methyl_pros and a[0] in PROTON_BEGIN_CODE:
                                                    all_c[h1_col]['number_of_assigned_shifts'] += 1

                                                elif data_type == '13C' and c13_col != -1:
                                                    all_c[c13_col]['number_of_assigned_shifts'] += 1

                                                elif data_type == '15N' and n15_col != -1:
                                                    all_c[n15_col]['number_of_assigned_shifts'] += 1

                                                elif data_type == '31P' and p31_col != -1:
                                                    all_c[p31_col]['number_of_assigned_shifts'] += 1

                                            elif a in non_excl_atoms:
                                                excluded_atom_id.append({'seq_id': seq_id, 'comp_id': comp_id,
                                                                         'atom_id': a, 'value': row[value_name]})

                                    else:

                                        if atom_id in atom_set:
                                            continue

                                        atom_set.add(atom_id)

                                        if atom_id in all_atoms:

                                            if data_type == '1H' and h1_col != -1\
                                               and atom_id not in non_rep_methyl_pros and atom_id[0] in PROTON_BEGIN_CODE:
                                                all_c[h1_col]['number_of_assigned_shifts'] += 1

                                            elif data_type == '13C' and c13_col != -1:
                                                all_c[c13_col]['number_of_assigned_shifts'] += 1

                                            elif data_type == '15N' and n15_col != -1:
                                                all_c[n15_col]['number_of_assigned_shifts'] += 1

                                            elif data_type == '31P' and p31_col != -1:
                                                all_c[p31_col]['number_of_assigned_shifts'] += 1

                                        elif atom_id in non_excl_atoms:
                                            excluded_atom_id.append({'seq_id': seq_id, 'comp_id': comp_id,
                                                                     'atom_id': atom_id, 'value': row[value_name]})

                            else:
                                excluded_comp_id.append({'seq_id': seq_id, 'comp_id': comp_id})

                        for c in all_c:
                            if c['number_of_target_shifts'] > 0:
                                c['completeness'] =\
                                    round(float(c['number_of_assigned_shifts']) / c['number_of_target_shifts'], 3)
                            else:
                                c['completeness'] = None

                    cc['completeness_of_all_assignments'] = all_c

                    cc['excluded_comp_id_in_statistics'] = excluded_comp_id if len(excluded_comp_id) > 0 else None
                    cc['excluded_atom_id_in_statistics'] = excluded_atom_id if len(excluded_atom_id) > 0 else None

                    # backbone atoms (bb)

                    bb_c = []

                    h1_col = c13_col = n15_col = p31_col = -1

                    col = 0

                    for data_type in count:

                        atom_group = {}
                        atom_group['atom_group'] = f'backbone_{data_type}'
                        atom_group['number_of_assigned_shifts'] = 0
                        atom_group['number_of_target_shifts'] = 0
                        atom_group['completeness'] = 0.0

                        if data_type.startswith('1h'):
                            h1_col = col

                        elif data_type.startswith('13c'):
                            c13_col = col

                        elif data_type.startswith('15n'):
                            n15_col = col

                        elif data_type.startswith('31p'):
                            p31_col = col

                        bb_c.append(atom_group)

                        col += 1

                    if ps is not None:

                        for seq_id, comp_id in zip(ps['seq_id'], ps['comp_id']):

                            polypeptide_like = self._reg.csStat.peptideLike(comp_id)

                            if self._reg.csStat.hasSufficientStat(comp_id, polypeptide_like):

                                bb_atoms = self._reg.csStat.getBackBoneAtoms(comp_id, excl_minor_atom=True)
                                non_rep_methyl_pros = self._reg.csStat.getNonRepMethylProtons(comp_id)

                                for a in bb_atoms:

                                    if h1_col != -1 and a not in non_rep_methyl_pros and a[0] in PROTON_BEGIN_CODE:
                                        bb_c[h1_col]['number_of_target_shifts'] += 1

                                    elif c13_col != -1 and a.startswith('C'):
                                        bb_c[c13_col]['number_of_target_shifts'] += 1

                                    elif n15_col != -1 and a.startswith('N'):
                                        bb_c[n15_col]['number_of_target_shifts'] += 1

                                    elif p31_col != -1 and a.startswith('P'):
                                        bb_c[p31_col]['number_of_target_shifts'] += 1

                                atom_set = set()

                                for row in lp_data:

                                    if row[chain_id_name] != _chain_id:
                                        if alt_chain_id_name is None or alt_chain_id_name not in row\
                                           or row[alt_chain_id_name] != _chain_id:
                                            continue
                                        _chain_id = chain_id_map[_chain_id] = row[chain_id_name]

                                    if row[seq_id_name] != seq_id or row[comp_id_name] != comp_id\
                                       or row[value_name] in EMPTY_VALUE:
                                        continue

                                    atom_id = row[atom_id_name]

                                    if None in (row[iso_number], row[atom_type]):
                                        continue

                                    data_type = str(row[iso_number]) + row[atom_type]

                                    if file_type == 'nef' or self.isNmrAtomName(comp_id, atom_id):
                                        atom_ids = self.getAtomIdList(comp_id, atom_id)

                                        if len(atom_ids) == 0:
                                            continue

                                        for a in atom_ids:

                                            if a in bb_atoms:

                                                if a in atom_set:
                                                    continue

                                                atom_set.add(a)

                                                if data_type == '1H' and h1_col != -1\
                                                   and a not in non_rep_methyl_pros and a[0] in PROTON_BEGIN_CODE:
                                                    bb_c[h1_col]['number_of_assigned_shifts'] += 1

                                                elif data_type == '13C' and c13_col != -1:
                                                    bb_c[c13_col]['number_of_assigned_shifts'] += 1

                                                elif data_type == '15N' and n15_col != -1:
                                                    bb_c[n15_col]['number_of_assigned_shifts'] += 1

                                                elif data_type == '31P' and p31_col != -1:
                                                    bb_c[p31_col]['number_of_assigned_shifts'] += 1

                                    elif atom_id in bb_atoms:

                                        if atom_id in atom_set:
                                            continue

                                        atom_set.add(atom_id)

                                        if data_type == '1H' and h1_col != -1\
                                           and atom_id not in non_rep_methyl_pros and atom_id[0] in PROTON_BEGIN_CODE:
                                            bb_c[h1_col]['number_of_assigned_shifts'] += 1

                                        elif data_type == '13C' and c13_col != -1:
                                            bb_c[c13_col]['number_of_assigned_shifts'] += 1

                                        elif data_type == '15N' and n15_col != -1:
                                            bb_c[n15_col]['number_of_assigned_shifts'] += 1

                                        elif data_type == '31P' and p31_col != -1:
                                            bb_c[p31_col]['number_of_assigned_shifts'] += 1

                        for c in bb_c:
                            if c['number_of_target_shifts'] > 0:
                                c['completeness'] =\
                                    round(float(c['number_of_assigned_shifts']) / c['number_of_target_shifts'], 3)
                            else:
                                c['completeness'] = None

                    if len(bb_c) > 0:
                        cc['completeness_of_backbone_assignments'] = bb_c

                    # sidechain atoms (sc)

                    sc_c = []

                    h1_col = c13_col = n15_col = p31_col = -1

                    col = 0

                    for data_type in count:

                        atom_group = {}
                        atom_group['atom_group'] = f'sidechain_{data_type}'
                        atom_group['number_of_assigned_shifts'] = 0
                        atom_group['number_of_target_shifts'] = 0
                        atom_group['completeness'] = 0.0

                        if data_type.startswith('1h'):
                            h1_col = col

                        elif data_type.startswith('13c'):
                            c13_col = col

                        elif data_type.startswith('15n'):
                            n15_col = col

                        elif data_type.startswith('31p'):
                            p31_col = col

                        sc_c.append(atom_group)

                        col += 1

                    if ps is not None:

                        for seq_id, comp_id in zip(ps['seq_id'], ps['comp_id']):

                            polypeptide_like = self._reg.csStat.peptideLike(comp_id)

                            if self._reg.csStat.hasSufficientStat(comp_id, polypeptide_like):

                                sc_atoms = self._reg.csStat.getSideChainAtoms(comp_id, excl_minor_atom=True)
                                non_rep_methyl_pros = self._reg.csStat.getNonRepMethylProtons(comp_id)

                                for a in sc_atoms:

                                    if h1_col != -1 and a not in non_rep_methyl_pros and a[0] in PROTON_BEGIN_CODE:
                                        sc_c[h1_col]['number_of_target_shifts'] += 1

                                    elif c13_col != -1 and a.startswith('C'):
                                        sc_c[c13_col]['number_of_target_shifts'] += 1

                                    elif n15_col != -1 and a.startswith('N'):
                                        sc_c[n15_col]['number_of_target_shifts'] += 1

                                    elif p31_col != -1 and a.startswith('P'):
                                        sc_c[p31_col]['number_of_target_shifts'] += 1

                                atom_set = set()

                                for row in lp_data:

                                    if row[chain_id_name] != _chain_id:
                                        if alt_chain_id_name is None or alt_chain_id_name not in row\
                                           or row[alt_chain_id_name] != _chain_id:
                                            continue
                                        _chain_id = chain_id_map[_chain_id] = row[chain_id_name]

                                    if row[seq_id_name] != seq_id or row[comp_id_name] != comp_id\
                                       or row[value_name] in EMPTY_VALUE:
                                        continue

                                    atom_id = row[atom_id_name]

                                    if None in (row[iso_number], row[atom_type]):
                                        continue

                                    data_type = str(row[iso_number]) + row[atom_type]

                                    if file_type == 'nef' or self.isNmrAtomName(comp_id, atom_id):
                                        atom_ids = self.getAtomIdList(comp_id, atom_id)

                                        if len(atom_ids) == 0:
                                            continue

                                        for a in atom_ids:

                                            if a in sc_atoms:

                                                if a in atom_set:
                                                    continue

                                                atom_set.add(a)

                                                if data_type == '1H' and h1_col != -1\
                                                   and a not in non_rep_methyl_pros and a[0] in PROTON_BEGIN_CODE:
                                                    sc_c[h1_col]['number_of_assigned_shifts'] += 1

                                                elif data_type == '13C' and c13_col != -1:
                                                    sc_c[c13_col]['number_of_assigned_shifts'] += 1

                                                elif data_type == '15N' and n15_col != -1:
                                                    sc_c[n15_col]['number_of_assigned_shifts'] += 1

                                                elif data_type == '31P' and p31_col != -1:
                                                    sc_c[p31_col]['number_of_assigned_shifts'] += 1

                                    elif atom_id in sc_atoms:

                                        if atom_id in atom_set:
                                            continue

                                        atom_set.add(atom_id)

                                        if data_type == '1H' and h1_col != -1\
                                           and atom_id not in non_rep_methyl_pros and atom_id[0] in PROTON_BEGIN_CODE:
                                            sc_c[h1_col]['number_of_assigned_shifts'] += 1

                                        elif data_type == '13C' and c13_col != -1:
                                            sc_c[c13_col]['number_of_assigned_shifts'] += 1

                                        elif data_type == '15N' and n15_col != -1:
                                            sc_c[n15_col]['number_of_assigned_shifts'] += 1

                                        elif data_type == '31P' and p31_col != -1:
                                            sc_c[p31_col]['number_of_assigned_shifts'] += 1

                        for c in sc_c:
                            if c['number_of_target_shifts'] > 0:
                                c['completeness'] =\
                                    round(float(c['number_of_assigned_shifts']) / c['number_of_target_shifts'], 3)
                            else:
                                c['completeness'] = None

                    if len(sc_c) > 0:
                        cc['completeness_of_sidechain_assignments'] = sc_c

                    # methyl group atoms (ch3)

                    ch3_c = []

                    h1_col = c13_col = -1

                    col = 0

                    for data_type in count:

                        atom_group = {}
                        atom_group['atom_group'] = f'methyl_{data_type}'
                        atom_group['number_of_assigned_shifts'] = 0
                        atom_group['number_of_target_shifts'] = 0
                        atom_group['completeness'] = 0.0

                        if data_type.startswith('1h'):
                            h1_col = col

                        elif data_type.startswith('13c'):
                            c13_col = col

                        else:
                            continue

                        ch3_c.append(atom_group)

                        col += 1

                    if ps is not None:

                        for seq_id, comp_id in zip(ps['seq_id'], ps['comp_id']):

                            polypeptide_like = self._reg.csStat.peptideLike(comp_id)

                            if self._reg.csStat.hasSufficientStat(comp_id, polypeptide_like):

                                ch3_atoms = self._reg.csStat.getMethylAtoms(comp_id)
                                non_rep_methyl_pros = self._reg.csStat.getNonRepMethylProtons(comp_id)

                                for a in ch3_atoms:

                                    if h1_col != -1 and a not in non_rep_methyl_pros and a[0] in PROTON_BEGIN_CODE:
                                        ch3_c[h1_col]['number_of_target_shifts'] += 1

                                    elif c13_col != -1 and a.startswith('C'):
                                        ch3_c[c13_col]['number_of_target_shifts'] += 1

                                atom_set = set()

                                for row in lp_data:

                                    if row[chain_id_name] != _chain_id:
                                        if alt_chain_id_name is None or alt_chain_id_name not in row\
                                           or row[alt_chain_id_name] != _chain_id:
                                            continue
                                        _chain_id = chain_id_map[_chain_id] = row[chain_id_name]

                                    if row[seq_id_name] != seq_id or row[comp_id_name] != comp_id\
                                       or row[value_name] in EMPTY_VALUE:
                                        continue

                                    atom_id = row[atom_id_name]

                                    if None in (row[iso_number], row[atom_type]):
                                        continue

                                    data_type = str(row[iso_number]) + row[atom_type]

                                    if file_type == 'nef' or self.isNmrAtomName(comp_id, atom_id):
                                        atom_ids = self.getAtomIdList(comp_id, atom_id)

                                        if len(atom_ids) == 0:
                                            continue

                                        for a in atom_ids:

                                            if a in ch3_atoms:

                                                if a in atom_set:
                                                    continue

                                                atom_set.add(a)

                                                if data_type == '1H' and h1_col != -1\
                                                   and a not in non_rep_methyl_pros and a[0] in PROTON_BEGIN_CODE:
                                                    ch3_c[h1_col]['number_of_assigned_shifts'] += 1

                                                elif data_type == '13C' and c13_col != -1:
                                                    ch3_c[c13_col]['number_of_assigned_shifts'] += 1

                                    elif atom_id in ch3_atoms:

                                        if atom_id in atom_set:
                                            continue

                                        atom_set.add(atom_id)

                                        if data_type == '1H' and h1_col != -1\
                                           and atom_id not in non_rep_methyl_pros and atom_id[0] in PROTON_BEGIN_CODE:
                                            ch3_c[h1_col]['number_of_assigned_shifts'] += 1

                                        elif data_type == '13C' and c13_col != -1:
                                            ch3_c[c13_col]['number_of_assigned_shifts'] += 1

                        for c in ch3_c:
                            if c['number_of_target_shifts'] > 0:
                                c['completeness'] =\
                                    round(float(c['number_of_assigned_shifts']) / c['number_of_target_shifts'], 3)
                            else:
                                c['completeness'] = None

                    if len(ch3_c) > 0:
                        cc['completeness_of_methyl_assignments'] = ch3_c

                    # aromatic atoms (aro)

                    aro_c = []

                    h1_col = c13_col = n15_col = -1

                    col = 0

                    for data_type in count:

                        atom_group = {}
                        atom_group['atom_group'] = f'aromatic_{data_type}'
                        atom_group['number_of_assigned_shifts'] = 0
                        atom_group['number_of_target_shifts'] = 0
                        atom_group['completeness'] = 0.0

                        if data_type.startswith('1h'):
                            h1_col = col

                        elif data_type.startswith('13c'):
                            c13_col = col

                        elif data_type.startswith('15n'):
                            n15_col = col

                        aro_c.append(atom_group)

                        col += 1

                    if ps is not None:

                        for seq_id, comp_id in zip(ps['seq_id'], ps['comp_id']):

                            polypeptide_like = self._reg.csStat.peptideLike(comp_id)

                            if self._reg.csStat.hasSufficientStat(comp_id, polypeptide_like):

                                aro_atoms = self._reg.csStat.getAromaticAtoms(comp_id,
                                                                              excl_minor_atom=True, primary=polypeptide_like)
                                non_rep_methyl_pros = self._reg.csStat.getNonRepMethylProtons(comp_id)

                                for a in aro_atoms:

                                    if h1_col != -1 and a not in non_rep_methyl_pros and a[0] in PROTON_BEGIN_CODE:
                                        aro_c[h1_col]['number_of_target_shifts'] += 1

                                    elif c13_col != -1 and a.startswith('C'):
                                        aro_c[c13_col]['number_of_target_shifts'] += 1

                                    elif n15_col != -1 and a.startswith('N'):
                                        aro_c[n15_col]['number_of_target_shifts'] += 1

                                atom_set = set()

                                for row in lp_data:

                                    if row[chain_id_name] != _chain_id:
                                        if alt_chain_id_name is None or alt_chain_id_name not in row\
                                           or row[alt_chain_id_name] != _chain_id:
                                            continue
                                        _chain_id = chain_id_map[_chain_id] = row[chain_id_name]

                                    if row[seq_id_name] != seq_id or row[comp_id_name] != comp_id\
                                       or row[value_name] in EMPTY_VALUE:
                                        continue

                                    atom_id = row[atom_id_name]

                                    if None in (row[iso_number], row[atom_type]):
                                        continue

                                    data_type = str(row[iso_number]) + row[atom_type]

                                    if file_type == 'nef' or self.isNmrAtomName(comp_id, atom_id):
                                        atom_ids = self.getAtomIdList(comp_id, atom_id)

                                        if len(atom_ids) == 0:
                                            continue

                                        for a in atom_ids:

                                            if a in aro_atoms:

                                                if a in atom_set:
                                                    continue

                                                atom_set.add(a)

                                                if data_type == '1H' and h1_col != -1\
                                                   and a not in non_rep_methyl_pros and a[0] in PROTON_BEGIN_CODE:
                                                    aro_c[h1_col]['number_of_assigned_shifts'] += 1

                                                elif data_type == '13C' and c13_col != -1:
                                                    aro_c[c13_col]['number_of_assigned_shifts'] += 1

                                                elif data_type == '15N' and n15_col != -1:
                                                    aro_c[n15_col]['number_of_assigned_shifts'] += 1

                                    elif atom_id in aro_atoms:

                                        if atom_id in atom_set:
                                            continue

                                        atom_set.add(atom_id)

                                        if data_type == '1H' and h1_col != -1\
                                           and atom_id not in non_rep_methyl_pros and atom_id[0] in PROTON_BEGIN_CODE:
                                            aro_c[h1_col]['number_of_assigned_shifts'] += 1

                                        elif data_type == '13C' and c13_col != -1:
                                            aro_c[c13_col]['number_of_assigned_shifts'] += 1

                                        elif data_type == '15N' and n15_col != -1:
                                            aro_c[n15_col]['number_of_assigned_shifts'] += 1

                        for c in aro_c:
                            if c['number_of_target_shifts'] > 0:
                                c['completeness'] =\
                                    round(float(c['number_of_assigned_shifts']) / c['number_of_target_shifts'], 3)
                            else:
                                c['completeness'] = None

                    if len(aro_c) > 0:
                        cc['completeness_of_aromatic_assignments'] = aro_c

                    completeness.append(cc)

                if len(completeness) > 0:
                    ent['completeness'] = completeness

            z_scores = {}

            for k in count:
                z_scores[k] = []

            max_val = min_val = 0.0

            for row in lp_data:

                if row[atom_type] in EMPTY_VALUE or row[iso_number] in EMPTY_VALUE or row[value_name] in EMPTY_VALUE:
                    continue

                data_type = f'{row[iso_number]}{row[atom_type].lower()}_chemical_shifts'

                chain_id = row[chain_id_name]
                seq_id = row[seq_id_name]
                comp_id = row[comp_id_name]
                atom_id = row[atom_id_name]
                value = row[value_name]

                _chain_id = chain_id if file_type == 'nef' or self._reg.remediation_mode else str(letterToDigit(chain_id))
                _chain_id = chain_id_map.get(_chain_id, _chain_id)

                if value in EMPTY_VALUE:
                    continue

                if file_type == 'nef' or self.isNmrAtomName(comp_id, atom_id):
                    _atom_id = self.getAtomIdList(comp_id, atom_id)

                    len_atom_id = len(_atom_id)

                    if len_atom_id == 0:
                        continue

                    if len_atom_id == 1 and atom_id == _atom_id[0]:
                        atom_id_ = atom_id

                    else:  # representative atom id
                        atom_id_ = _atom_id[0]

                else:
                    atom_id_ = atom_id

                has_cs_stat = False

                # non-standard residue
                if comp_id not in STD_MON_DICT:

                    neighbor_comp_ids = set(_row[comp_id_name] for _row in lp_data
                                            if _row[chain_id_name] == _chain_id
                                            and abs(_row[seq_id_name] - seq_id) < 4 and _row[seq_id_name] != seq_id)

                    polypeptide_like = False

                    for comp_id2 in neighbor_comp_ids:
                        polypeptide_like |= self._reg.csStat.peptideLike(comp_id2)

                    for cs_stat in self._reg.csStat.get(comp_id):

                        if cs_stat['atom_id'] == atom_id_ and cs_stat['count'] > 0:
                            avg_value = cs_stat['avg']
                            std_value = cs_stat['std']

                            has_cs_stat = True

                            break

                # standard residue
                else:

                    for cs_stat in self._reg.csStat.get(comp_id, self._reg.report.isDiamagnetic()):

                        if cs_stat['atom_id'] == atom_id_ and cs_stat['count'] > 0:
                            avg_value = cs_stat['avg']
                            std_value = cs_stat['std']

                            has_cs_stat = True

                            break

                if (not has_cs_stat) or None in (std_value, avg_value) or std_value <= 0.0:
                    continue

                z_score = (value - avg_value) / std_value

                if z_score > max_val:
                    max_val = z_score

                elif z_score < min_val:
                    min_val = z_score

                z_scores[data_type].append(z_score)

            target_scale = (max_val - min_val) / 20.0

            if target_scale <= 0.0:
                return

            scale = 1.0

            while scale < target_scale:
                scale *= 2.0

            while scale > target_scale:
                scale /= 2.0

            range_of_vals, count_of_vals = [], []

            v = 0.0
            while v < min_val:
                v += scale

            while v > min_val:
                v -= scale

            while v <= max_val:

                _count = count.copy()

                for k in count:
                    _count[k] = len([z for z in z_scores[k] if v <= z < v + scale])

                range_of_vals.append(v)
                count_of_vals.append(_count)

                v += scale

            transposed = {}

            for k in count:
                transposed[k] = []

                for count_of_val in count_of_vals:
                    transposed[k].append(count_of_val[k])

            if len(range_of_vals) > 1:
                ent['histogram'] = {'range_of_values': range_of_vals, 'number_of_values': transposed, 'annotations': cs_ann}

            if 'sequence_coverage' in ent:

                # prediction of redox state of CYS

                cys_redox_state = []

                for sc in ent['sequence_coverage']:

                    chain_id = sc['chain_id']

                    _chain_id = chain_id if file_type == 'nef' or self._reg.remediation_mode else str(letterToDigit(chain_id))
                    _chain_id = chain_id_map.get(_chain_id, _chain_id)

                    ps = next((ps for ps in poly_seq if ps['chain_id'] == chain_id), None)

                    if ps is not None:

                        for seq_id, comp_id in zip(ps['seq_id'], ps['comp_id']):

                            if comp_id not in ('CYS', 'DCY'):
                                continue

                            cys = {'chain_id': chain_id, 'seq_id': seq_id}

                            ca_chem_shift = cb_chem_shift = None

                            for row in lp_data:

                                atom_id = row[atom_id_name]

                                if row[chain_id_name] == _chain_id\
                                   and row[seq_id_name] == seq_id and row[comp_id_name] == comp_id:
                                    if atom_id == 'CA':
                                        ca_chem_shift = row[value_name]
                                    elif atom_id == 'CB':
                                        cb_chem_shift = row[value_name]

                                if None in (ca_chem_shift, cb_chem_shift):
                                    if row[chain_id_name] == _chain_id and row[seq_id_name] > seq_id:
                                        break
                                else:
                                    break

                            cys['ca_chem_shift'] = ca_chem_shift
                            cys['cb_chem_shift'] = cb_chem_shift

                            if cb_chem_shift is not None:
                                if cb_chem_shift < 32.0:
                                    cys['redox_state_pred'] = 'reduced'
                                elif cb_chem_shift > 35.0:
                                    cys['redox_state_pred'] = 'oxidized'
                                else:
                                    cys['redox_state_pred'] = 'ambiguous'
                            elif ca_chem_shift is not None:
                                cys['redox_state_pred'] = 'ambiguous'
                            else:
                                cys['redox_state_pred'] = 'unknown'

                            if cys['redox_state_pred'] == 'ambiguous':
                                oxi, red = predict_redox_state_of_cysteine(ca_chem_shift, cb_chem_shift)
                                if oxi < 0.001:
                                    cys['redox_state_pred'] = 'reduced'
                                elif red < 0.001:
                                    cys['redox_state_pred'] = 'oxidized'
                                else:
                                    cys['redox_state_pred'] = f"oxidized {oxi:.1%}, reduced {red:.1%}"

                            if self._hasCoordSeq(chain_id, seq_id):
                                cys['in_disulfide_bond'] = False
                                if has_key_value(input_source_dic, 'disulfide_bond'):
                                    if any(True for b in input_source_dic['disulfide_bond']
                                           if (b['chain_id_1'] == chain_id and b['seq_id_1'] == seq_id)
                                           or (b['chain_id_2'] == chain_id and b['seq_id_2'] == seq_id)):
                                        cys['in_disulfide_bond'] = True

                                cys['in_other_bond'] = False
                                if has_key_value(input_source_dic, 'other_bond'):
                                    if any(True for b in input_source_dic['other_bond']
                                           if (b['chain_id_1'] == chain_id and b['seq_id_1'] == seq_id)
                                           or (b['chain_id_2'] == chain_id and b['seq_id_2'] == seq_id)):
                                        cys['in_other_bond'] = True

                            cys_redox_state.append(cys)

                    if len(cys_redox_state) > 0:
                        ent['cys_redox_state'] = cys_redox_state

                # prediction of cis-trans peptide of PRO

                pro_cis_trans = []

                for sc in ent['sequence_coverage']:

                    chain_id = sc['chain_id']

                    _chain_id = chain_id if file_type == 'nef' or self._reg.remediation_mode else str(letterToDigit(chain_id))
                    _chain_id = chain_id_map.get(_chain_id, _chain_id)

                    ps = next((ps for ps in poly_seq if ps['chain_id'] == chain_id), None)

                    if ps is not None:

                        for seq_id, comp_id in zip(ps['seq_id'], ps['comp_id']):

                            if comp_id != 'PRO':
                                continue

                            pro = {'chain_id': chain_id, 'seq_id': seq_id}

                            cb_chem_shift = cg_chem_shift = None

                            for row in lp_data:

                                atom_id = row[atom_id_name]

                                if row[chain_id_name] == _chain_id\
                                   and row[seq_id_name] == seq_id and row[comp_id_name] == comp_id:
                                    if atom_id == 'CB':
                                        cb_chem_shift = row[value_name]
                                    elif atom_id == 'CG':
                                        cg_chem_shift = row[value_name]

                                if None in (cb_chem_shift, cg_chem_shift):
                                    if row[chain_id_name] == _chain_id and row[seq_id_name] > seq_id:
                                        break
                                else:
                                    break

                            pro['cb_chem_shift'] = cb_chem_shift
                            pro['cg_chem_shift'] = cg_chem_shift

                            if (cb_chem_shift is not None) and (cg_chem_shift is not None):
                                delta = cb_chem_shift - cg_chem_shift
                                if delta < 4.8:
                                    pro['cis_trans_pred'] = 'trans'
                                elif delta > 9.15:
                                    pro['cis_trans_pred'] = 'cis'
                                else:
                                    pro['cis_trans_pred'] = 'ambiguous'
                            elif (cb_chem_shift is not None) or (cg_chem_shift is not None):
                                pro['cis_trans_pred'] = 'ambiguous'
                            else:
                                pro['cis_trans_pred'] = 'unknown'

                            if pro['cis_trans_pred'] == 'ambiguous':
                                cis, trs = predict_cis_trans_peptide_of_proline(cb_chem_shift, cg_chem_shift)
                                if cis < 0.001:
                                    pro['cis_trans_pred'] = 'trans'
                                elif trs < 0.001:
                                    pro['cis_trans_pred'] = 'cis'
                                else:
                                    pro['cis_trans_pred'] = f"cis {cis:.1%}, trans {trs:.1%}"

                            if self._hasCoordSeq(chain_id, seq_id):
                                in_cis_peptide_bond = self.isProtCis(chain_id, seq_id)

                                pro['in_cis_peptide_bond'] = in_cis_peptide_bond

                                if pro['cis_trans_pred'] != 'unknown':

                                    if (in_cis_peptide_bond and pro['cis_trans_pred'] != 'cis')\
                                       or (not in_cis_peptide_bond and pro['cis_trans_pred'] != 'trans'):
                                        item = None
                                        if ',' in pro['cis_trans_pred']:
                                            if (in_cis_peptide_bond and cis > trs)\
                                               or (not in_cis_peptide_bond and trs > cis):
                                                pass
                                            else:
                                                item = 'unusual_chemical_shift'
                                        else:
                                            item = 'anomalous_chemical_shift'

                                        if item is not None:

                                            shifts = ''
                                            if cb_chem_shift is not None:
                                                shifts += f"CB {cb_chem_shift} ppm, "
                                            if cg_chem_shift is not None:
                                                shifts += f"CG {cg_chem_shift} ppm, "

                                            warn = f"{'cis' if in_cis_peptide_bond else 'trans'}-peptide bond of "\
                                                f"{chain_id}:{seq_id}:{comp_id} can not be verified with "\
                                                "the assigned chemical shift values "\
                                                f"({shifts}cis_trans_pred {pro['cis_trans_pred']})."

                                            self._reg.report.warning.appendDescription(item,
                                                                                       {'file_name': file_name,
                                                                                        'sf_framecode': sf_framecode,
                                                                                        'description': warn})

                                            if self._reg.verbose:
                                                self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfAssignedChemShift() "  # noqa: E501, pylint: disable=line-too-long
                                                                    f"++ Warning  - {warn}\n")

                            pro_cis_trans.append(pro)

                    if len(pro_cis_trans) > 0:
                        ent['pro_cis_trans'] = pro_cis_trans

                # prediction of tautomeric state of HIS

                his_tautomeric_state = []

                for sc in ent['sequence_coverage']:

                    chain_id = sc['chain_id']

                    _chain_id = chain_id if file_type == 'nef' or self._reg.remediation_mode else str(letterToDigit(chain_id))
                    _chain_id = chain_id_map.get(_chain_id, _chain_id)

                    ps = next((ps for ps in poly_seq if ps['chain_id'] == chain_id), None)

                    if ps is not None:

                        for seq_id, comp_id in zip(ps['seq_id'], ps['comp_id']):

                            if comp_id != 'HIS':
                                continue

                            his = {'chain_id': chain_id, 'seq_id': seq_id}

                            cg_chem_shift = cd2_chem_shift = nd1_chem_shift = ne2_chem_shift = None

                            for row in lp_data:

                                atom_id = row[atom_id_name]

                                if row[chain_id_name] == _chain_id\
                                   and row[seq_id_name] == seq_id and row[comp_id_name] == comp_id:
                                    if atom_id == 'CG':
                                        cg_chem_shift = row[value_name]
                                    elif atom_id == 'CD2':
                                        cd2_chem_shift = row[value_name]
                                    elif atom_id == 'ND1':
                                        nd1_chem_shift = row[value_name]
                                    elif atom_id == 'NE2':
                                        ne2_chem_shift = row[value_name]

                                if None in (cg_chem_shift, cd2_chem_shift, nd1_chem_shift, ne2_chem_shift):
                                    if row[chain_id_name] == _chain_id and row[seq_id_name] > seq_id:
                                        break
                                else:
                                    break

                            his['cg_chem_shift'] = cg_chem_shift
                            his['cd2_chem_shift'] = cd2_chem_shift
                            his['nd1_chem_shift'] = nd1_chem_shift
                            his['ne2_chem_shift'] = ne2_chem_shift

                            if (cg_chem_shift is not None) or (cd2_chem_shift is not None)\
                               or (nd1_chem_shift is not None) or (ne2_chem_shift is not None):
                                bip, tau, pi = predict_tautomer_state_of_histidine(cg_chem_shift, cd2_chem_shift,
                                                                                   nd1_chem_shift, ne2_chem_shift)
                                if tau < 0.001 and pi < 0.001:
                                    his['tautomeric_state_pred'] = 'biprotonated'
                                elif bip < 0.001 and pi < 0.001:
                                    his['tautomeric_state_pred'] = 'tau-tautomer'
                                elif bip < 0.001 and tau < 0.001:
                                    his['tautomeric_state_pred'] = 'pi-tautomer'
                                else:
                                    his['tautomeric_state_pred'] =\
                                        f"biprotonated {bip:.1%}, tau-tautomer {tau:.1%}, pi-tautomer {pi:.1%}"
                            else:
                                his['tautomeric_state_pred'] = 'unknown'

                            his['tautomeric_state'] = self.getTautomerOfHistidine(chain_id, seq_id)

                            if his['tautomeric_state_pred'] != 'unknown':
                                item = None
                                if his['tautomeric_state_pred'] != his['tautomeric_state'] and his['tautomeric_state'] != 'unknown':
                                    if ',' in his['tautomeric_state_pred']:
                                        if (his['tautomeric_state'] == 'biprotonated' and bip > tau and bip > pi)\
                                           or (his['tautomeric_state'] == 'tau-tautomer' and tau > bip and tau > pi)\
                                           or (his['tautomeric_state'] == 'pi-tautomer' and pi > bip and pi > tau):
                                            pass
                                        else:
                                            item = 'unusual_chemical_shift'
                                    else:
                                        item = 'anomalous_chemical_shift'

                                if item is not None:

                                    shifts = ''
                                    if cg_chem_shift is not None:
                                        shifts += f"CG {cg_chem_shift} ppm, "
                                    if cd2_chem_shift is not None:
                                        shifts += f"CD2 {cd2_chem_shift} ppm, "
                                    if nd1_chem_shift is not None:
                                        shifts += f"ND1 {nd1_chem_shift} ppm, "
                                    if ne2_chem_shift is not None:
                                        shifts += f"NE2 {ne2_chem_shift} ppm, "

                                    warn = f"Tautomeric state {his['tautomeric_state']} of {chain_id}:{seq_id}:{comp_id} "\
                                        "can not be verified with the assigned chemical shift values "\
                                        f"({shifts}tautomeric_state_pred {his['tautomeric_state_pred']})."

                                    self._reg.report.warning.appendDescription(item,
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'description': warn})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfAssignedChemShift() "
                                                            f"++ Warning  - {warn}\n")

                            his_tautomeric_state.append(his)

                if len(his_tautomeric_state) > 0:
                    ent['his_tautomeric_state'] = his_tautomeric_state

                # prediction of rotameric state of VAL/LEU/ILE

                ilv_comp_ids = ('VAL', 'LEU', 'ILE')

                ilv_rotameric_state = []

                for sc in ent['sequence_coverage']:

                    chain_id = sc['chain_id']

                    _chain_id = chain_id if file_type == 'nef' or self._reg.remediation_mode else str(letterToDigit(chain_id))
                    _chain_id = chain_id_map.get(_chain_id, _chain_id)

                    ps = next((ps for ps in poly_seq if ps['chain_id'] == chain_id), None)

                    if ps is not None:

                        for seq_id, comp_id in zip(ps['seq_id'], ps['comp_id']):

                            if comp_id not in ilv_comp_ids:
                                continue

                            ilv = {'chain_id': chain_id, 'seq_id': seq_id, 'comp_id': comp_id}

                            if comp_id == 'VAL':

                                cg1_chem_shift = cg2_chem_shift = None

                                for row in lp_data:

                                    atom_id = row[atom_id_name]

                                    if row[chain_id_name] == _chain_id\
                                       and row[seq_id_name] == seq_id and row[comp_id_name] == comp_id\
                                       and atom_id.startswith('CG'):

                                        _atom_id = atom_id

                                        if self.isNmrAtomName(comp_id, atom_id):
                                            _atom_id = self.getRepAtomId(comp_id, atom_id)

                                        if _atom_id == 'CG1':
                                            cg1_chem_shift = row[value_name]
                                        elif _atom_id == 'CG2':
                                            cg2_chem_shift = row[value_name]

                                    if None in (cg1_chem_shift, cg2_chem_shift):
                                        if row[chain_id_name] == _chain_id and row[seq_id_name] > seq_id:
                                            break
                                    else:
                                        break

                                ilv['cg1_chem_shift'] = cg1_chem_shift
                                ilv['cg2_chem_shift'] = cg2_chem_shift

                                if (cg1_chem_shift is not None) or (cg2_chem_shift is not None):
                                    gp, t, gm = predict_rotamer_state_of_valine(cg1_chem_shift, cg2_chem_shift)
                                    if t < 0.001 and gm < 0.001:
                                        ilv['rotameric_state_pred'] = 'gauche+'
                                    elif gm < 0.001 and gp < 0.001:
                                        ilv['rotameric_state_pred'] = 'trans'
                                    elif gp < 0.001 and t < 0.001:
                                        ilv['rotameric_state_pred'] = 'gauche-'
                                    else:
                                        ilv['rotameric_state_pred'] = f"gauche+ {gp:.1%}, trans {t:.1%}, gauche- {gm:.1%}"
                                else:
                                    ilv['rotameric_state_pred'] = 'unknown'

                                ilv['rotameric_state'] = self.getRotamerOfValine(chain_id, seq_id)

                                r = next(r for r in ilv['rotameric_state'] if r['name'] == 'chi1')
                                if 'unknown' in r:
                                    _rotameric_state = 'unknown'
                                else:
                                    _gp = r['gauche+']
                                    _t = r['trans']
                                    _gm = r['gauche-']
                                    if _gp > _t and _gp > _gm:
                                        _rotameric_state = 'gauche+'
                                    elif _t > _gm and _t > _gp:
                                        _rotameric_state = 'trans'
                                    elif _gm > _gp and _gm > _t:
                                        _rotameric_state = 'gauche-'
                                    else:
                                        _rotameric_state = 'unknown'

                                if ilv['rotameric_state_pred'] != 'unknown':
                                    item = None
                                    if _rotameric_state not in (ilv['rotameric_state_pred'], 'unknown'):
                                        if ',' in ilv['rotameric_state_pred']:
                                            if (_rotameric_state == 'gauche+' and gp > t and gp > gm)\
                                               or (_rotameric_state == 'trans' and t > gm and t > gp)\
                                               or (_rotameric_state == 'gauche-' and gm > gp and gm > t):
                                                pass
                                            else:
                                                item = 'unusual_chemical_shift'
                                        else:
                                            item = 'anomalous_chemical_shift'

                                    if item is not None:

                                        shifts = ''
                                        if cg1_chem_shift is not None:
                                            shifts += f"CG1 {cg1_chem_shift} ppm, "
                                        if cg2_chem_shift is not None:
                                            shifts += f"CG2 {cg2_chem_shift} ppm, "

                                        warn = f"Rotameric state {_rotameric_state} of {chain_id}:{seq_id}:{comp_id} "\
                                            "can not be verified with the assigned chemical shift values "\
                                            f"({shifts}rotameric_state_pred {ilv['rotameric_state_pred']})."

                                        self._reg.report.warning.appendDescription(item,
                                                                                   {'file_name': file_name,
                                                                                    'sf_framecode': sf_framecode,
                                                                                    'description': warn})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfAssignedChemShift() "
                                                                f"++ Warning  - {warn}\n")

                            elif comp_id == 'LEU':

                                cd1_chem_shift = cd2_chem_shift = None

                                for row in lp_data:

                                    atom_id = row[atom_id_name]

                                    if row[chain_id_name] == _chain_id\
                                       and row[seq_id_name] == seq_id and row[comp_id_name] == comp_id\
                                       and atom_id.startswith('CD'):

                                        _atom_id = atom_id

                                        if self.isNmrAtomName(comp_id, atom_id):
                                            _atom_id = self.getRepAtomId(comp_id, atom_id)

                                        if _atom_id == 'CD1':
                                            cd1_chem_shift = row[value_name]
                                        elif _atom_id == 'CD2':
                                            cd2_chem_shift = row[value_name]

                                    if None in (cd1_chem_shift, cd2_chem_shift):
                                        if row[chain_id_name] == _chain_id and row[seq_id_name] > seq_id:
                                            break
                                    else:
                                        break

                                ilv['cd1_chem_shift'] = cd1_chem_shift
                                ilv['cd2_chem_shift'] = cd2_chem_shift

                                if (cd1_chem_shift is not None) or (cd2_chem_shift is not None):
                                    gp, t, gm = predict_rotamer_state_of_leucine(cd1_chem_shift, cd2_chem_shift)
                                    if t < 0.001 and gm < 0.001:
                                        ilv['rotameric_state_pred'] = 'gauche+'
                                    elif gm < 0.001 and gp < 0.001:
                                        ilv['rotameric_state_pred'] = 'trans'
                                    elif gp < 0.001 and t < 0.001:
                                        ilv['rotameric_state_pred'] = 'gauche-'
                                    else:
                                        ilv['rotameric_state_pred'] = f"gauche+ {gp:.1%}, trans {t:.1%}, gauche- {gm:.1%}"
                                else:
                                    ilv['rotameric_state_pred'] = 'unknown'

                                ilv['rotameric_state'] = self.getRotamerOfLeucine(chain_id, seq_id)

                                r = next(r for r in ilv['rotameric_state'] if r['name'] == 'chi2')
                                if 'unknown' in r:
                                    _rotameric_state = 'unknown'
                                else:
                                    _gp = r['gauche+']
                                    _t = r['trans']
                                    _gm = r['gauche-']
                                    if _gp > _t and _gp > _gm:
                                        _rotameric_state = 'gauche+'
                                    elif _t > _gm and _t > _gp:
                                        _rotameric_state = 'trans'
                                    elif _gm > _gp and _gm > _t:
                                        _rotameric_state = 'gauche-'
                                    else:
                                        _rotameric_state = 'unknown'

                                if ilv['rotameric_state_pred'] != 'unknown':
                                    item = None
                                    if _rotameric_state not in (ilv['rotameric_state_pred'], 'unknown'):
                                        if ',' in ilv['rotameric_state_pred']:
                                            if (_rotameric_state == 'gauche+' and gp > t and gp > gm)\
                                               or (_rotameric_state == 'trans' and t > gm and t > gp)\
                                               or (_rotameric_state == 'gauche-' and gm > gp and gm > t):
                                                pass
                                            else:
                                                item = 'unusual_chemical_shift'
                                        else:
                                            item = 'anomalous_chemical_shift'

                                    if item is not None:

                                        shifts = ''
                                        if cd1_chem_shift is not None:
                                            shifts += f"CD1 {cd1_chem_shift} ppm, "
                                        if cd2_chem_shift is not None:
                                            shifts += f"CD2 {cd2_chem_shift} ppm, "

                                        warn = f"Rotameric state {_rotameric_state} of {chain_id}:{seq_id}:{comp_id} "\
                                            "can not be verified with the assigned chemical shift values "\
                                            f"({shifts}rotameric_state_pred {ilv['rotameric_state_pred']})."

                                        self._reg.report.warning.appendDescription(item,
                                                                                   {'file_name': file_name,
                                                                                    'sf_framecode': sf_framecode,
                                                                                    'description': warn})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfAssignedChemShift() "
                                                                f"++ Warning  - {warn}\n")

                            else:

                                cd1_chem_shift = None

                                for row in lp_data:

                                    atom_id = row[atom_id_name]

                                    if row[chain_id_name] == _chain_id\
                                       and row[seq_id_name] == seq_id and row[comp_id_name] == comp_id:
                                        if atom_id == 'CD1':
                                            cd1_chem_shift = row[value_name]

                                    if cd1_chem_shift is None:
                                        if row[chain_id_name] == _chain_id and row[seq_id_name] > seq_id:
                                            break
                                    else:
                                        break

                                ilv['cd1_chem_shift'] = cd1_chem_shift

                                if cd1_chem_shift is not None:
                                    gp, t, gm = predict_rotamer_state_of_isoleucine(cd1_chem_shift)
                                    if t < 0.001 and gm < 0.001:
                                        ilv['rotameric_state_pred'] = 'gauche+'
                                    elif gm < 0.001 and gp < 0.001:
                                        ilv['rotameric_state_pred'] = 'trans'
                                    elif gp < 0.001 and t < 0.001:
                                        ilv['rotameric_state_pred'] = 'gauche-'
                                    else:
                                        ilv['rotameric_state_pred'] = f"gauche+ {gp:.1%}, trans {t:.1%}, gauche- {gm:.1%}"
                                else:
                                    ilv['rotameric_state_pred'] = 'unknown'

                                ilv['rotameric_state'] = self.getRotamerOfIsoleucine(chain_id, seq_id)

                                r = next(r for r in ilv['rotameric_state'] if r['name'] == 'chi2')
                                if 'unknown' in r:
                                    _rotameric_state = 'unknown'
                                else:
                                    _gp = r['gauche+']
                                    _t = r['trans']
                                    _gm = r['gauche-']
                                    if _gp > _t and _gp > _gm:
                                        _rotameric_state = 'gauche+'
                                    elif _t > _gm and _t > _gp:
                                        _rotameric_state = 'trans'
                                    elif _gm > _gp and _gm > _t:
                                        _rotameric_state = 'gauche-'
                                    else:
                                        _rotameric_state = 'unknown'

                                if ilv['rotameric_state_pred'] != 'unknown':
                                    item = None
                                    if _rotameric_state not in (ilv['rotameric_state_pred'], 'unknown'):
                                        if ',' in ilv['rotameric_state_pred']:
                                            if (_rotameric_state == 'gauche+' and gp > t and gp > gm)\
                                               or (_rotameric_state == 'trans' and t > gm and t > gp)\
                                               or (_rotameric_state == 'gauche-' and gm > gp and gm > t):
                                                pass
                                            else:
                                                item = 'unusual_chemical_shift'
                                        else:
                                            item = 'anomalous_chemical_shift'

                                    if item is not None:

                                        shifts = ''
                                        if cd1_chem_shift is not None:
                                            shifts += f"CD1 {cd1_chem_shift} ppm, "

                                        warn = f"Rotameric state {_rotameric_state} of {chain_id}:{seq_id}:{comp_id} "\
                                            "can not be verified with the assigned chemical shift values "\
                                            f"({shifts}rotameric_state_pred {ilv['rotameric_state_pred']})."

                                        self._reg.report.warning.appendDescription(item,
                                                                                   {'file_name': file_name,
                                                                                    'sf_framecode': sf_framecode,
                                                                                    'description': warn})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfAssignedChemShift() "
                                                                f"++ Warning  - {warn}\n")

                            ilv_rotameric_state.append(ilv)

                if len(ilv_rotameric_state) > 0:
                    ent['ilv_rotameric_state'] = ilv_rotameric_state

                # random coil index

                rci_atom_ids = ('HA', 'HA1', 'HA2', 'HA3', 'H', 'HN', 'NH', 'C', 'CO', 'N', 'CA', 'CB')

                rci = []

                for sc in ent['sequence_coverage']:

                    chain_id = sc['chain_id']

                    _chain_id = chain_id if file_type == 'nef' or self._reg.remediation_mode else str(letterToDigit(chain_id))
                    _chain_id = chain_id_map.get(_chain_id, _chain_id)

                    ps = next((ps for ps in poly_seq if ps['chain_id'] == chain_id), None)

                    if ps is not None:

                        rci_residues, rci_assignments, seq_ids_wo_assign, oxidized_cys_seq_ids = [], [], [], []

                        for seq_id, comp_id in zip(ps['seq_id'], ps['comp_id']):

                            if comp_id not in EMPTY_VALUE:
                                if comp_id not in STD_MON_DICT:
                                    continue
                                if not self._reg.csStat.peptideLike(comp_id):
                                    continue
                                rci_residues.append([comp_id, seq_id])
                            else:
                                _comp_id = self._getCoordCompId(chain_id, seq_id)
                                if _comp_id is not None:
                                    if _comp_id not in STD_MON_DICT:
                                        continue
                                    if not self._reg.csStat.peptideLike(_comp_id):
                                        continue
                                    rci_residues.append([_comp_id, seq_id])
                                else:
                                    continue

                            has_bb_atoms = False

                            for row in lp_data:

                                if row[chain_id_name] != _chain_id\
                                   or row[seq_id_name] != seq_id or row[comp_id_name] != comp_id\
                                   or row[value_name] in EMPTY_VALUE:
                                    continue

                                atom_id = row[atom_id_name]

                                if file_type == 'nef' or self.isNmrAtomName(comp_id, atom_id):
                                    _atom_id = self.getAtomIdList(comp_id, atom_id)

                                    len_atom_id = len(_atom_id)

                                    if len_atom_id == 0:
                                        continue

                                    if len_atom_id == 1 and atom_id == _atom_id[0]:
                                        atom_id_ = atom_id

                                    else:  # representative atom id
                                        atom_id_ = _atom_id[0]

                                else:
                                    atom_id_ = atom_id

                                if atom_id_ not in rci_atom_ids:
                                    continue

                                rci_assignments.append([comp_id, seq_id, atom_id, row[atom_type], row[value_name]])

                                has_bb_atoms = True

                            if has_bb_atoms:

                                if comp_id in ('CYS', 'DCY'):

                                    ca_chem_shift = cb_chem_shift = None

                                    for row in lp_data:

                                        atom_id = row[atom_id_name]

                                        if row[chain_id_name] == _chain_id\
                                           and row[seq_id_name] == seq_id and row[comp_id_name] == comp_id:
                                            if atom_id == 'CA':
                                                ca_chem_shift = row[value_name]
                                            elif atom_id == 'CB':
                                                cb_chem_shift = row[value_name]

                                        if None in (ca_chem_shift, cb_chem_shift):
                                            if row[chain_id_name] == _chain_id and row[seq_id_name] > seq_id:
                                                break
                                        else:
                                            break

                                    ambig_redox_state = False

                                    if cb_chem_shift is not None:
                                        if cb_chem_shift < 32.0:
                                            pass
                                        elif cb_chem_shift > 35.0:
                                            oxidized_cys_seq_ids.append(seq_id)
                                        else:
                                            ambig_redox_state = True
                                    elif ca_chem_shift is not None:
                                        ambig_redox_state = True

                                    if ambig_redox_state:
                                        oxi, red = predict_redox_state_of_cysteine(ca_chem_shift, cb_chem_shift)
                                        if oxi < 0.001:
                                            pass
                                        elif red < 0.001 or oxi > 0.5:
                                            oxidized_cys_seq_ids.append(seq_id)

                            else:
                                seq_ids_wo_assign.append(seq_id)

                        if len(rci_assignments) > 0:
                            result = self._rci.calculate(rci_residues, rci_assignments, oxidized_cys_seq_ids, seq_ids_wo_assign)

                            if 'rci' in result and len(result['rci']) > 0:
                                result['chain_id'] = chain_id
                                result['comp_id'] = [res[0] for res in rci_residues]
                                struct_conf = self._extractCoordStructConf(chain_id, ps['seq_id'])
                                len_struct_conf = len(struct_conf)
                                result['struct_conf'] = []
                                for seq_id in result['seq_id']:
                                    pos = ps['seq_id'].index(seq_id)
                                    if pos < len_struct_conf:
                                        result['struct_conf'].append(struct_conf[pos])

                                cif_ps = self._reg.report.getModelPolymerSequenceWithNmrChainId(chain_id)

                                if cif_ps is not None and 'well_defined_region' in cif_ps and self._reg.caC is not None:
                                    chain_id = int(chain_id) if chain_id.isdigit() else letterToDigit(chain_id)
                                    auth_to_star_seq = self._reg.caC['auth_to_star_seq']
                                    coord_unobs_res = self._reg.caC['coord_unobs_res']
                                    dom = [None] * len(result['rci'])
                                    for idx, seq_id in enumerate(result['seq_id']):
                                        for r in cif_ps['well_defined_region']:
                                            seq_key = next((k for k, v in auth_to_star_seq.items()
                                                            if v[0] == chain_id and v[1] == seq_id), None)
                                            _seq_key = (seq_key[0], seq_key[1]) if seq_key is not None else None
                                            if _seq_key in coord_unobs_res:
                                                dom[idx] = -1
                                            elif _seq_key is not None:
                                                if _seq_key[1] in r['seq_id']:
                                                    dom[idx] = r['domain_id']
                                                    break
                                            elif dom[idx] is None:
                                                dom[idx] = -1
                                    result['domain_id'] = dom

                                    _score = 0.0
                                    dom_idx = -1

                                    for i, r in enumerate(cif_ps['well_defined_region']):
                                        try:
                                            score = r['percent_of_core'] / max(r['medoid_rmsd'], 1.0)
                                            if score > _score:
                                                _score = score
                                                dom_idx = i
                                        except Exception:  # pylint: disable=broad-exception-caught
                                            continue

                                    if dom_idx != -1:
                                        result['rmsd_in_well_defined_region'] =\
                                            cif_ps['well_defined_region'][dom_idx]['medoid_rmsd']

                                rci.append(result)

                if len(rci) > 0:
                    ent['random_coil_index'] = rci

            if file_type == 'nmr-star' and self._reg.star_data_type[file_list_id] == 'Entry':
                lp_category = LP_CATEGORIES[file_type]['chem_shift']
                sf = self._reg.star_data[file_list_id].get_saveframe_by_name(sf_framecode)
                lp = next(lp for lp in sf.loops if lp.category == lp_category)

                ent['atom_name_mapping'] = get_atom_name_mapping(lp, [['Comp_ID', 'Atom_ID', 'Original_PDB_atom_name']])

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.__calculateStatsOfAssignedChemShift() "
                                                     "++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfAssignedChemShift() "
                                    f"++ Error  - {str(e)}\n")

    def _hasCoordSeq(self, nmr_chain_id: str, nmr_seq_id: str) -> bool:
        """ Return whether a given sequence is in the coordinates.
            @return: True for corresponding sequence in the coordinates exists, False otherwise
        """

        cif_ps = self._reg.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return False

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self._reg.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return False

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            cif_seq_id = next((test_seq_id for ref_seq_id, test_seq_id
                               in zip(result['ref_seq_id'], result['test_seq_id'])
                               if ref_seq_id == nmr_seq_id), None)

            return cif_seq_id is not None

        return False

    def _getCoordCompId(self, nmr_chain_id: str, nmr_seq_id: int
                        ) -> Optional[str]:
        """ Return comp ID of coordinate file for a given NMR sequence.
        """

        cif_ps = self._reg.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return None

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self._reg.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return None

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id
                       and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            cif_seq_id = next((test_seq_id for ref_seq_id, test_seq_id
                               in zip(result['ref_seq_id'], result['test_seq_id'])
                               if ref_seq_id == nmr_seq_id), None)

            if cif_seq_id is None:
                return None

            return next((_comp_id for _seq_id, _comp_id
                         in zip(cif_ps['seq_id'], cif_ps['comp_id'])
                         if _seq_id == cif_seq_id), None)

        return None
