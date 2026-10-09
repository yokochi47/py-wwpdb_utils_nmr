##
# File: NmrDpValidationMrStats.py
# Date: 17-Aug-2026
#
# Updates:
# 19-Aug-2026  M. Yokochi - optimize _getTypeOfDistanceRestraint() by indexing inter-chain restraints by their
#                           sequence/composition pair instead of scanning the whole loop per row
##
""" Statistics of restraints and spectral peak lists for NMR data validation.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.3"

import collections
import copy
import itertools
from typing import Callable, List, Optional, Set

try:
    from wwpdb.utils.nmr.NmrDpConstant import (LP_CATEGORIES,
                                               INCONSIST_OVER_CONFLICTED,
                                               R_CONFLICTED_DIST_RESTRAINT,
                                               R_INCONSISTENT_DIST_RESTRAINT,
                                               INDEX_TAGS,
                                               WEIGHT_TAGS,
                                               CONSIST_ID_TAGS,
                                               POTENTIAL_ITEMS,
                                               AUX_LP_CATEGORIES,
                                               ITEM_NAMES_IN_CS_LOOP,
                                               ITEM_NAMES_IN_PK_LOOP,
                                               ITEM_NAMES_IN_DIST_LOOP,
                                               ITEM_NAMES_IN_DIHED_LOOP,
                                               ITEM_NAMES_IN_RDC_LOOP,
                                               EMPTY_VALUE,
                                               PROTON_BEGIN_CODE,
                                               ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                               ANGLE_UNCERT_MAX,
                                               RDC_UNCERT_MAX,
                                               DIST_AMBIG_LOW,
                                               DIST_AMBIG_UP,
                                               C_CARBONYL_CENTER_MAX,
                                               C_CARBONYL_CENTER_MIN,
                                               C_AROMATIC_CENTER_MAX,
                                               C_AROMATIC_CENTER_MIN_TOR,
                                               C_ALIPHATIC_CENTER_MAX,
                                               C_ALIPHATIC_CENTER_MIN,
                                               C_METHYL_CENTER_MAX,
                                               C_METHYL_CENTER_MIN)
    from wwpdb.utils.nmr.CifToNmrStar import has_key_value
    from wwpdb.utils.nmr.mr.ParserListenerUtil import isAmbigAtomSelection
    from wwpdb.utils.nmr.NmrDpValidationBase import (NmrDpValidationBase,
                                                     is_non_metal_element,
                                                     is_like_planality_boundary,
                                                     get_atom_name_mapping)
except ImportError:
    from nmr.NmrDpConstant import (LP_CATEGORIES,
                                   INCONSIST_OVER_CONFLICTED,
                                   R_CONFLICTED_DIST_RESTRAINT,
                                   R_INCONSISTENT_DIST_RESTRAINT,
                                   INDEX_TAGS,
                                   WEIGHT_TAGS,
                                   CONSIST_ID_TAGS,
                                   POTENTIAL_ITEMS,
                                   AUX_LP_CATEGORIES,
                                   ITEM_NAMES_IN_CS_LOOP,
                                   ITEM_NAMES_IN_PK_LOOP,
                                   ITEM_NAMES_IN_DIST_LOOP,
                                   ITEM_NAMES_IN_DIHED_LOOP,
                                   ITEM_NAMES_IN_RDC_LOOP,
                                   EMPTY_VALUE,
                                   PROTON_BEGIN_CODE,
                                   ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                   ANGLE_UNCERT_MAX,
                                   RDC_UNCERT_MAX,
                                   DIST_AMBIG_LOW,
                                   DIST_AMBIG_UP,
                                   C_CARBONYL_CENTER_MAX,
                                   C_CARBONYL_CENTER_MIN,
                                   C_AROMATIC_CENTER_MAX,
                                   C_AROMATIC_CENTER_MIN_TOR,
                                   C_ALIPHATIC_CENTER_MAX,
                                   C_ALIPHATIC_CENTER_MIN,
                                   C_METHYL_CENTER_MAX,
                                   C_METHYL_CENTER_MIN)
    from nmr.CifToNmrStar import has_key_value
    from nmr.mr.ParserListenerUtil import isAmbigAtomSelection
    from nmr.NmrDpValidationBase import (NmrDpValidationBase,
                                         is_non_metal_element,
                                         is_like_planality_boundary,
                                         get_atom_name_mapping)


class NmrDpValidationMrStats(NmrDpValidationBase):
    """ Statistics of restraints and spectral peak lists for NMR data validation.
    """
    __slots__ = ()

    def _calculateStatsOfDistanceRestraint(self, file_list_id: int, sf_framecode: str, lp_data: List[dict],
                                           conflict_id_set: Optional[List[int]], inconsistent: Set[int],
                                           redundant: Set[int], ent: dict) -> None:
        """ Calculate statistics of distance restraints.
        """

        input_source = self._reg.report.input_sources[file_list_id]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        content_subtype = 'dist_restraint'

        index_tag = INDEX_TAGS[file_type][content_subtype]
        item_names = ITEM_NAMES_IN_DIST_LOOP[file_type]
        combination_id_name = item_names['combination_id']
        chain_id_1_name = item_names['chain_id_1']
        chain_id_2_name = item_names['chain_id_2']
        seq_id_1_name = item_names['seq_id_1']
        seq_id_2_name = item_names['seq_id_2']
        comp_id_1_name = item_names['comp_id_1']
        comp_id_2_name = item_names['comp_id_2']
        atom_id_1_name = item_names['atom_id_1']
        atom_id_2_name = item_names['atom_id_2']
        member_id_name = item_names['member_id'] if file_type == 'nmr-star' else None
        member_logic_code_name = item_names['member_logic_code'] if file_type == 'nmr-star' else None
        target_value_name = item_names['target_value']
        if 'target_value_alt' in item_names and target_value_name not in lp_data[0].keys():
            target_value_name = item_names['target_value_alt']
        lower_limit_name = item_names['lower_limit']
        upper_limit_name = item_names['upper_limit']
        lower_linear_limit_name = item_names['lower_linear_limit']
        upper_linear_limit_name = item_names['upper_linear_limit']
        weight_name = WEIGHT_TAGS[file_type][content_subtype]
        id_tag = CONSIST_ID_TAGS[file_type][content_subtype]

        def ext_atom_names(row):
            return (row[chain_id_1_name], row[chain_id_2_name],
                    row[seq_id_1_name], row[seq_id_2_name],
                    row[comp_id_1_name], row[comp_id_2_name],
                    row[atom_id_1_name], row[atom_id_2_name])

        symmetry_index = None

        def get_symmetry_index():
            """ Return row ids of inter-chain restraints grouped by their sequence/composition pair.
                Built on first use so that loops never reaching the symmetry test are not touched.
            """

            nonlocal symmetry_index

            if symmetry_index is None:
                symmetry_index = {}
                for _idx, _row in enumerate(lp_data):
                    _chain_id_1 = _row[chain_id_1_name]
                    _chain_id_2 = _row[chain_id_2_name]
                    if _chain_id_1 == _chain_id_2:
                        continue
                    _key = (_row[seq_id_1_name], _row[comp_id_1_name],
                            _row[seq_id_2_name], _row[comp_id_2_name])
                    if _key in symmetry_index:
                        symmetry_index[_key].append((_idx, _chain_id_1, _chain_id_2))
                    else:
                        symmetry_index[_key] = [(_idx, _chain_id_1, _chain_id_2)]

            return symmetry_index

        def get_est_value_range(row):
            target_value = row.get(target_value_name)
            upper_limit = lower_limit = None

            if target_value is None:

                if has_key_value(row, lower_limit_name)\
                        and has_key_value(row, upper_limit_name):
                    target_value = (row[lower_limit_name] + row[upper_limit_name]) / 2.0
                    upper_limit = row[lower_limit_name]
                    lower_limit = row[upper_limit_name]

                elif has_key_value(row, lower_linear_limit_name)\
                        and has_key_value(row, upper_linear_limit_name):
                    target_value = (row[lower_linear_limit_name] + row[upper_linear_limit_name]) / 2.0

                elif has_key_value(row, upper_linear_limit_name):
                    target_value = row[upper_linear_limit_name]
                    upper_limit = target_value

                elif has_key_value(row, upper_limit_name):
                    target_value = row[upper_limit_name]
                    upper_limit = target_value

                elif has_key_value(row, lower_linear_limit_name):
                    target_value = row[lower_linear_limit_name]
                    lower_limit = target_value

                elif has_key_value(row, lower_limit_name):
                    target_value = row[lower_limit_name]
                    lower_limit = target_value

            return target_value, upper_limit, lower_limit

        def get_est_target_value(row):
            value = row.get(target_value_name)

            if value is None:

                if has_key_value(row, lower_limit_name)\
                        and has_key_value(row, upper_limit_name):
                    value = (row[lower_limit_name] + row[upper_limit_name]) / 2.0

                elif has_key_value(row, lower_linear_limit_name)\
                        and has_key_value(row, upper_linear_limit_name):
                    value = (row[lower_linear_limit_name] + row[upper_linear_limit_name]) / 2.0

                elif has_key_value(row, upper_linear_limit_name):
                    value = row[upper_linear_limit_name]

                elif has_key_value(row, upper_limit_name):
                    value = row[upper_limit_name]

                elif has_key_value(row, lower_linear_limit_name):
                    value = row[lower_linear_limit_name]

                elif has_key_value(row, lower_limit_name):
                    value = row[lower_limit_name]

            return value

        len_lp_data = len(lp_data)

        try:

            max_val = -100.0
            min_val = 100.0

            count, comb_count, inco_count, redu_count, weights, potential_types =\
                {}, {}, {}, {}, {}, {}

            set_id = set()

            count_per_residue, count_on_map, count_on_asym_map = [], [], []

            has_inter_chain_constraint = False

            poly_seq = input_source_dic['polymer_sequence']

            if poly_seq is not None:

                for ps in poly_seq:
                    struct_conf = self._extractCoordStructConf(ps['chain_id'], ps['seq_id'])
                    count_per_residue.append({'chain_id': ps['chain_id'], 'seq_id': ps['seq_id'], 'comp_id': ps['comp_id'],
                                              'struct_conf': struct_conf})
                    count_on_map.append({'chain_id': ps['chain_id'], 'seq_id': ps['seq_id'], 'comp_id': ps['comp_id'],
                                         'struct_conf': struct_conf})

                if len(poly_seq) > 1:
                    for ps1, ps2 in itertools.combinations(poly_seq, 2):
                        count_on_asym_map.append({'chain_id_1': ps1['chain_id'], 'chain_id_2': ps2['chain_id'],
                                                  'seq_id_1': ps1['seq_id'], 'seq_id_2': ps2['seq_id'],
                                                  'comp_id_1': ps1['comp_id'], 'comp_id_2': ps2['comp_id'],
                                                  'struct_conf_1': self._extractCoordStructConf(ps1['chain_id'], ps1['seq_id']),
                                                  'struct_conf_2': self._extractCoordStructConf(ps2['chain_id'], ps2['seq_id'])})

            _rest_id = -1
            _atom1 = _atom2 = None

            for idx, row in enumerate(lp_data):
                index = row.get(index_tag)
                combination_id = row.get(combination_id_name)
                member_id = row.get(member_id_name) if file_type == 'nmr-star' else None
                member_logic_code = row.get(member_logic_code_name) if file_type == 'nmr-star' else None

                chain_id_1, chain_id_2, seq_id_1, seq_id_2, \
                    comp_id_1, comp_id_2, atom_id_1, atom_id_2 = ext_atom_names(row)

                if 'HOH' in (comp_id_1, comp_id_2):
                    continue

                weight = row.get(weight_name)

                rest_id = row[id_tag]
                set_id.add(rest_id)

                if (member_logic_code is not None and member_logic_code == 'OR') or rest_id == _rest_id:
                    atom1 = {'chain_id': chain_id_1,
                             'seq_id': int(seq_id_1) if seq_id_1 not in EMPTY_VALUE else None,
                             'comp_id': comp_id_1,
                             'atom_id': atom_id_1}
                    atom2 = {'chain_id': chain_id_2,
                             'seq_id': int(seq_id_2) if seq_id_2 not in EMPTY_VALUE else None,
                             'comp_id': comp_id_2,
                             'atom_id': atom_id_2}
                    if None not in (_atom1, _atom2):
                        if not isAmbigAtomSelection([_atom1, atom1], self._reg.csStat)\
                           and not isAmbigAtomSelection([_atom2, atom2], self._reg.csStat):
                            _rest_id, _atom1, _atom2 = rest_id, atom1, atom2
                            continue
                    _atom1, _atom2 = atom1, atom2

                _rest_id = rest_id

                target_value, upper_limit, lower_limit = get_est_value_range(row)

                if target_value is None:
                    continue

                max_val = max(max_val, target_value)
                min_val = min(min_val, target_value)

                data_type = self._getTypeOfDistanceRestraint(file_type, idx, target_value, upper_limit, lower_limit,
                                                             member_id, chain_id_1, seq_id_1, comp_id_1, atom_id_1,
                                                             chain_id_2, seq_id_2, comp_id_2, atom_id_2,
                                                             get_symmetry_index)

                if 'hydrogen_bonds' in data_type and ('too close!' in data_type or 'too far!' in data_type):

                    values = ''
                    if has_key_value(row, target_value_name):
                        values += f"{target_value_name} {row[target_value_name]}, "
                    if has_key_value(row, lower_limit_name):
                        values += f"{lower_limit_name} {row[lower_limit_name]}, "
                    if has_key_value(row, upper_limit_name):
                        values += f"{upper_limit_name} {row[upper_limit_name]}, "
                    if has_key_value(row, lower_linear_limit_name):
                        values += f"{lower_linear_limit_name} {row[lower_linear_limit_name]}, "
                    if has_key_value(row, upper_linear_limit_name):
                        values += f"{upper_linear_limit_name} {row[upper_linear_limit_name]}, "

                    warn = "Hydrogen bond constraint "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}) "\
                        f"is too {'close each other' if 'close' in data_type else 'far apart'} ({values[:-2]})."

                    self._reg.report.warning.appendDescription('unusual_data',
                                                               {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                'description': warn})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfDistanceRestraint() ++ Warning  - {warn}\n")

                elif 'disulfide_bonds' in data_type and ('too close!' in data_type or 'too far!' in data_type):

                    values = ''
                    if has_key_value(row, target_value_name):
                        values += f"{target_value_name} {row[target_value_name]}, "
                    if has_key_value(row, lower_limit_name):
                        values += f"{lower_limit_name} {row[lower_limit_name]}, "
                    if has_key_value(row, upper_limit_name):
                        values += f"{upper_limit_name} {row[upper_limit_name]}, "
                    if has_key_value(row, lower_linear_limit_name):
                        values += f"{lower_linear_limit_name} {row[lower_linear_limit_name]}, "
                    if has_key_value(row, upper_linear_limit_name):
                        values += f"{upper_linear_limit_name} {row[upper_linear_limit_name]}, "

                    warn = "Disulfide bond constraint "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}) "\
                        f"is too {'close each other' if 'close' in data_type else 'far apart'} ({values[:-2]})."

                    self._reg.report.warning.appendDescription('unusual_data',
                                                               {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                'description': warn})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfDistanceRestraint() ++ Warning  - {warn}\n")

                elif 'diselenide_bonds' in data_type and ('too close!' in data_type or 'too far!' in data_type):

                    values = ''
                    if has_key_value(row, target_value_name):
                        values += f"{target_value_name} {row[target_value_name]}, "
                    if has_key_value(row, lower_limit_name):
                        values += f"{lower_limit_name} {row[lower_limit_name]}, "
                    if has_key_value(row, upper_limit_name):
                        values += f"{upper_limit_name} {row[upper_limit_name]}, "
                    if has_key_value(row, lower_linear_limit_name):
                        values += f"{lower_linear_limit_name} {row[lower_linear_limit_name]}, "
                    if has_key_value(row, upper_linear_limit_name):
                        values += f"{upper_linear_limit_name} {row[upper_linear_limit_name]}, "

                    warn = "Diselenide bond constraint "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}) "\
                        f"is too {'close each other' if 'close' in data_type else 'far apart'} ({values[:-2]})."

                    self._reg.report.warning.appendDescription('unusual_data',
                                                               {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                'description': warn})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfDistanceRestraint() ++ Warning  - {warn}\n")

                elif 'other_bonds' in data_type and ('too close!' in data_type or 'too far!' in data_type):

                    values = ''
                    if has_key_value(row, target_value_name):
                        values += f"{target_value_name} {row[target_value_name]}, "
                    if has_key_value(row, lower_limit_name):
                        values += f"{lower_limit_name} {row[lower_limit_name]}, "
                    if has_key_value(row, upper_limit_name):
                        values += f"{upper_limit_name} {row[upper_limit_name]}, "
                    if has_key_value(row, lower_linear_limit_name):
                        values += f"{lower_linear_limit_name} {row[lower_linear_limit_name]}, "
                    if has_key_value(row, upper_linear_limit_name):
                        values += f"{upper_linear_limit_name} {row[upper_linear_limit_name]}, "

                    warn = "Other bond constraint "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}) "\
                        f"is too {'close each other' if 'close' in data_type else 'far apart'} ({values[:-2]})."

                    self._reg.report.warning.appendDescription('unusual_data',
                                                               {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                'description': warn})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfDistanceRestraint() ++ Warning  - {warn}\n")

                if data_type in count:
                    count[data_type] += 1
                else:
                    count[data_type] = 1

                if (combination_id is not None) and (combination_id not in EMPTY_VALUE):
                    if data_type in comb_count:
                        comb_count[data_type] += 1
                    else:
                        comb_count[data_type] = 1

                if index is not None:

                    if index in inconsistent:
                        if data_type in inco_count:
                            inco_count[data_type] += 1
                        else:
                            inco_count[data_type] = 1

                    if index in redundant:
                        if data_type in redu_count:
                            redu_count[data_type] += 1
                        else:
                            redu_count[data_type] = 1

                # detect weight

                if weight is not None:
                    if data_type not in weights:
                        weights[data_type] = []
                    weights[data_type].append(weight)

                # detect potential type

                lower_limit = row.get(lower_limit_name)
                upper_limit = row.get(upper_limit_name)
                lower_linear_limit = row.get(lower_linear_limit_name)
                upper_linear_limit = row.get(upper_linear_limit_name)

                if (lower_limit is not None) and (upper_limit is not None)\
                        and lower_linear_limit is None and upper_linear_limit is None:
                    potential_type = 'square-well-parabolic'
                elif (lower_limit is not None) and (upper_limit is not None)\
                        and (lower_linear_limit is not None) and (upper_linear_limit is not None):
                    potential_type = 'square-well-parabolic-linear'
                elif lower_limit is None and (upper_limit is not None)\
                        and lower_linear_limit is None and upper_linear_limit is None:
                    potential_type = 'upper-bound-parabolic'
                elif (lower_limit is not None) and upper_limit is None\
                        and lower_linear_limit is None and upper_linear_limit is None:
                    potential_type = 'lower-bound-parabolic'
                elif lower_limit is None and (upper_limit is not None)\
                        and lower_linear_limit is None and (upper_linear_limit is not None):
                    potential_type = 'upper-bound-parabolic-linear'
                elif (lower_limit is not None) and upper_limit is None\
                        and (lower_linear_limit is not None) and upper_linear_limit is None:
                    potential_type = 'lower-bound-parabolic-linear'
                elif (target_value is not None) and lower_limit is None and upper_limit is None\
                        and lower_linear_limit is None and upper_linear_limit is None:
                    potential_type = 'log-harmonic'
                else:
                    potential_type = 'undefined'

                if potential_type is not None:
                    if data_type not in potential_types:
                        potential_types[data_type] = []
                    potential_types[data_type].append(potential_type)

                if poly_seq is not None:

                    # count per residue

                    for c in count_per_residue:
                        if data_type not in c:
                            c[data_type] = [0] * len(c['seq_id'])
                        if c['chain_id'] == chain_id_1 and seq_id_1 in c['seq_id']:
                            c[data_type][c['seq_id'].index(seq_id_1)] += 1
                        if c['chain_id'] == chain_id_2 and seq_id_2 in c['seq_id']:
                            c[data_type][c['seq_id'].index(seq_id_2)] += 1

                    # count on map

                    if chain_id_1 == chain_id_2:

                        for c in count_on_map:
                            if data_type not in c:
                                c[data_type] = []
                            if c['chain_id'] == chain_id_1:
                                try:
                                    b = next(b for b in c[data_type] if b['seq_id_1'] == seq_id_1 and b['seq_id_2'] == seq_id_2)
                                    b['total'] += 1
                                except StopIteration:
                                    if seq_id_1 in c['seq_id'] and seq_id_2 in c['seq_id']:
                                        c[data_type].append({'seq_id_1': seq_id_1, 'seq_id_2': seq_id_2, 'total': 1})

                    else:

                        for c in count_on_asym_map:
                            if data_type not in c:
                                c[data_type] = []
                            if c['chain_id_1'] == chain_id_1 and c['chain_id_2'] == chain_id_2:
                                try:
                                    b = next(b for b in c[data_type] if b['seq_id_1'] == seq_id_1 and b['seq_id_2'] == seq_id_2)
                                    b['total'] += 1
                                except StopIteration:
                                    if seq_id_1 in c['seq_id_1'] and seq_id_2 in c['seq_id_2']:
                                        c[data_type].append({'seq_id_1': seq_id_1, 'seq_id_2': seq_id_2, 'total': 1})
                            elif c['chain_id_1'] == chain_id_2 and c['chain_id_2'] == chain_id_1:
                                try:
                                    b = next(b for b in c[data_type] if b['seq_id_1'] == seq_id_2 and b['seq_id_2'] == seq_id_1)
                                    b['total'] += 1
                                except StopIteration:
                                    if seq_id_1 in c['seq_id_1'] and seq_id_2 in c['seq_id_2']:
                                        c[data_type].append({'seq_id_1': seq_id_2, 'seq_id_2': seq_id_1, 'total': 1})
                            if not has_inter_chain_constraint and len(c[data_type]) > 0:
                                has_inter_chain_constraint = True

            if len(count) == 0:
                return

            ent['number_of_constraints'] = count
            ent['number_of_constraint_sets'] = len(set_id)
            if len(comb_count) > 0:
                ent['number_of_combined_constraints'] = comb_count
            if len(inco_count) > 0:
                ent['number_of_inconsistent_constraints'] = inco_count
            if len(redu_count) > 0:
                ent['number_of_redundant_constraints'] = redu_count
            if poly_seq is not None:
                ent['constraints_per_residue'] = count_per_residue
                ent['constraints_on_contact_map'] = count_on_map
            if has_inter_chain_constraint:
                ent['constraints_on_asym_contact_map'] = count_on_asym_map
            ent['range'] = {'max_value': round(max_val, 2), 'min_value': round(min_val, 2)}
            if len(weights) > 0:
                _weights = {}
                for k, v in weights.items():
                    _weights[k] = collections.Counter(v).most_common()
                ent['weight_of_constraints'] = _weights
            if len(potential_types) > 0:
                _potential_types = {}
                for k, v in potential_types.items():
                    _potential_types[k] = collections.Counter(v).most_common()
                ent['potential_type_of_constraints'] = _potential_types

            target_scale = (max_val - min_val) / 10.0

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
                    _count[k] = 0

                for idx, row in enumerate(lp_data):
                    member_id = row.get(member_id_name) if file_type == 'nmr-star' else None

                    chain_id_1, chain_id_2, seq_id_1, seq_id_2, \
                        comp_id_1, comp_id_2, atom_id_1, atom_id_2 = ext_atom_names(row)

                    target_value, upper_limit, lower_limit = get_est_value_range(row)

                    if target_value is None or target_value < v or target_value >= v + scale:
                        continue

                    data_type = self._getTypeOfDistanceRestraint(file_type, idx, target_value, upper_limit, lower_limit,
                                                                 member_id, chain_id_1, seq_id_1, comp_id_1, atom_id_1,
                                                                 chain_id_2, seq_id_2, comp_id_2, atom_id_2,
                                                                 get_symmetry_index)

                    if data_type in _count:
                        _count[data_type] += 1
                    else:
                        _count[data_type] = 1

                range_of_vals.append(v)
                count_of_vals.append(_count)

                v += scale

            transposed = {}

            for k in count:
                transposed[k] = []

                for count_of_val in count_of_vals:
                    transposed[k].append(count_of_val[k])

            if len(range_of_vals) > 1:
                ent['histogram'] = {'range_of_values': range_of_vals, 'number_of_values': transposed}

            if conflict_id_set is not None:

                # max_inclusive = DIST_UNCERT_MAX

                max_val = min_val = 0.0

                dist_ann = []

                for id_set in conflict_id_set:
                    len_id_set = len(id_set)

                    if len_id_set < 2:
                        continue

                    for i in range(len_id_set - 1):

                        for j in range(i + 1, len_id_set):
                            if id_set[j] >= len_lp_data:
                                continue
                            row_1 = lp_data[id_set[i]]
                            row_2 = lp_data[id_set[j]]

                            target_value_1 = get_est_target_value(row_1)
                            target_value_2 = get_est_target_value(row_2)

                            if None in (target_value_1, target_value_2):
                                continue

                            if target_value_1 == target_value_2:
                                continue

                            discrepancy = abs(target_value_1 - target_value_2) / abs(target_value_1 + target_value_2) * 100.0

                            max_val = max(max_val, discrepancy)

                            if discrepancy >= R_INCONSISTENT_DIST_RESTRAINT * 100.0:
                                ann = {}
                                ann['level'] = 'conflicted' if discrepancy >= R_CONFLICTED_DIST_RESTRAINT * 100.0\
                                    else 'inconsistent'
                                ann['chain_id_1'] = row_1[chain_id_1_name]
                                ann['seq_id_1'] = row_1[seq_id_1_name]
                                ann['comp_id_1'] = row_1[comp_id_1_name]
                                ann['atom_id_1'] = row_1[atom_id_1_name]
                                if row_1[chain_id_1_name] != row_2[chain_id_2_name]:
                                    ann['chain_id_2'] = row_2[chain_id_2_name]
                                    ann['seq_id_2'] = row_2[seq_id_2_name]
                                    ann['comp_id_2'] = row_2[comp_id_2_name]
                                elif row_1[seq_id_1_name] != row_2[seq_id_2_name]:
                                    ann['seq_id_2'] = row_2[seq_id_2_name]
                                    ann['comp_id_2'] = row_2[comp_id_2_name]
                                ann['atom_id_2'] = row_2[atom_id_2_name]
                                ann['discrepancy'] = round(discrepancy, 1)

                                dist_ann.append(ann)

                if max_val > 0.0:
                    target_scale = (max_val - min_val) / 10.0

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
                            _count[k] = 0

                        for id_set in conflict_id_set:
                            len_id_set = len(id_set)

                            if len_id_set < 2:
                                continue

                            redundant = True

                            for i in range(len_id_set - 1):

                                for j in range(i + 1, len_id_set):
                                    row_id_1 = id_set[i]
                                    row_id_2 = id_set[j]
                                    if row_id_2 >= len_lp_data:
                                        continue
                                    row_1 = lp_data[row_id_1]
                                    row_2 = lp_data[row_id_2]

                                    target_value_1 = get_est_target_value(row_1)
                                    target_value_2 = get_est_target_value(row_2)

                                    if target_value_1 is None and target_value_2 is None:
                                        continue

                                    if None in (target_value_1, target_value_2):
                                        redundant = False
                                        continue

                                    if target_value_1 == target_value_2:
                                        continue

                                    redundant = False

                                    discrepancy =\
                                        abs(target_value_1 - target_value_2) / abs(target_value_1 + target_value_2) * 100.0

                                    if discrepancy < v or discrepancy >= v + scale:
                                        continue

                                    target_value = get_est_target_value(row_1)

                                    if target_value is None:
                                        continue

                                    member_id = row_1.get(member_id_name) if file_type == 'nmr-star' else None

                                    chain_id_1, chain_id_2, seq_id_1, seq_id_2, \
                                        comp_id_1, comp_id_2, atom_id_1, atom_id_2 = ext_atom_names(row_1)

                                    data_type = self._getTypeOfDistanceRestraint(file_type, row_id_1,
                                                                                 target_value, upper_limit, lower_limit,
                                                                                 member_id,
                                                                                 chain_id_1, seq_id_1, comp_id_1, atom_id_1,
                                                                                 chain_id_2, seq_id_2, comp_id_2, atom_id_2,
                                                                                 get_symmetry_index)

                                    if data_type in _count:
                                        _count[data_type] += 1
                                    else:
                                        _count[data_type] = 1

                            if 0.0 <= v < scale and redundant:

                                target_value, upper_limit, lower_limit = get_est_value_range(row_1)

                                if target_value is None:
                                    continue

                                member_id = row_1.get(member_id_name) if file_type == 'nmr-star' else None

                                chain_id_1, chain_id_2, seq_id_1, seq_id_2, \
                                    comp_id_1, comp_id_2, atom_id_1, atom_id_2 = ext_atom_names(row_1)

                                data_type = self._getTypeOfDistanceRestraint(file_type, row_id_1,
                                                                             target_value, upper_limit, lower_limit,
                                                                             member_id,
                                                                             chain_id_1, seq_id_1, comp_id_1, atom_id_1,
                                                                             chain_id_2, seq_id_2, comp_id_2, atom_id_2,
                                                                             get_symmetry_index)

                                if data_type in _count:
                                    _count[data_type] += 1
                                else:
                                    _count[data_type] = 1

                        range_of_vals.append(v)
                        count_of_vals.append(_count)

                        v += scale

                    transposed = {}

                    for k in count:
                        transposed[k] = []

                        for count_of_val in count_of_vals:
                            transposed[k].append(count_of_val[k])

                    if len(range_of_vals) > 1:
                        ent['histogram_of_discrepancy'] = {'range_of_values': range_of_vals,
                                                           'number_of_values': transposed,
                                                           'annotations': dist_ann}

            if file_type == 'nmr-star' and self._reg.star_data_type[file_list_id] == 'Entry':
                lp_category = LP_CATEGORIES[file_type][content_subtype]
                sf = self._reg.star_data[file_list_id].get_saveframe_by_name(sf_framecode)
                lp = next(lp for lp in sf.loops if lp.category == lp_category)

                ent['atom_name_mapping'] = get_atom_name_mapping(lp, [['Comp_ID_1', 'Atom_ID_1', 'Auth_atom_name_1'],
                                                                      ['Comp_ID_2', 'Atom_ID_2', 'Auth_atom_name_2']])

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.__calculateStatsOfDistanceRestraint() "
                                                     "++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfDistanceRestraint() "
                                    f"++ Error  - {str(e)}\n")

    def _calculateStatsOfCovalentBond(self, file_list_id: int, sf_framecode: str, lp_category: str, lp_data: List[dict], ent: dict
                                      ) -> None:
        """ Calculate statistics of covalent bonds.
        """

        input_source = self._reg.report.input_sources[file_list_id]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        item_names = ITEM_NAMES_IN_DIST_LOOP[file_type]
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

            count = {}

            count_on_map, count_on_asym_map = [], []

            has_inter_chain_constraint = False

            poly_seq = input_source_dic['polymer_sequence']

            if poly_seq is not None:

                for ps in poly_seq:
                    struct_conf = self._extractCoordStructConf(ps['chain_id'], ps['seq_id'])
                    count_on_map.append({'chain_id': ps['chain_id'], 'seq_id': ps['seq_id'], 'comp_id': ps['comp_id'],
                                         'struct_conf': struct_conf})

                if len(poly_seq) > 1:
                    for ps1, ps2 in itertools.combinations(poly_seq, 2):
                        count_on_asym_map.append({'chain_id_1': ps1['chain_id'], 'chain_id_2': ps2['chain_id'],
                                                  'seq_id_1': ps1['seq_id'], 'seq_id_2': ps2['seq_id'],
                                                  'comp_id_1': ps1['comp_id'], 'comp_id_2': ps2['comp_id'],
                                                  'struct_conf_1': self._extractCoordStructConf(ps1['chain_id'], ps1['seq_id']),
                                                  'struct_conf_2': self._extractCoordStructConf(ps2['chain_id'], ps2['seq_id'])})

            for idx, row in enumerate(lp_data):
                chain_id_1, chain_id_2, seq_id_1, seq_id_2, \
                    comp_id_1, comp_id_2, atom_id_1, atom_id_2 = ext_atom_names(row)

                bond = self.getNmrBondLength(chain_id_1, seq_id_1, atom_id_1, chain_id_2, seq_id_2, atom_id_2)

                if bond is None:
                    continue

                dist = next((b['distance'] for b in bond if b['model_id'] == self._reg.representative_model_id), None)

                if dist is None:
                    dist = bond[0]['distance']

                data_type = self._getTypeOfCovalentBond(file_type, lp_data, idx, dist,
                                                        chain_id_1, seq_id_1, comp_id_1, atom_id_1,
                                                        chain_id_2, seq_id_2, comp_id_2, atom_id_2)

                if 'hydrogen_bonds' in data_type and ('too close!' in data_type or 'too far!' in data_type):

                    warn = "Hydrogen bond constraint "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}) "\
                        f"is too {'close each other' if 'close' in data_type else 'far apart'} ({dist}Å)."

                    self._reg.report.warning.appendDescription('unusual_data',
                                                               {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                'category': lp_category, 'description': warn})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfCovalentBond() ++ Warning  - {warn}\n")

                elif 'disulfide_bonds' in data_type and ('too close!' in data_type or 'too far!' in data_type):

                    warn = "Disulfide bond constraint "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}) "\
                        f"is too {'close each other' if 'close' in data_type else 'far apart'} ({dist}Å)."

                    self._reg.report.warning.appendDescription('unusual_data',
                                                               {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                'category': lp_category, 'description': warn})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfCovalentBond() ++ Warning  - {warn}\n")

                elif 'diselenide_bonds' in data_type and ('too close!' in data_type or 'too far!' in data_type):

                    warn = "Diselenide bond constraint "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}) "\
                        f"is too {'close each other' if 'close' in data_type else 'far apart'} ({dist}Å)."

                    self._reg.report.warning.appendDescription('unusual_data',
                                                               {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                'category': lp_category, 'description': warn})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfCovalentBond() ++ Warning  - {warn}\n")

                elif 'other_bonds' in data_type and ('too close!' in data_type or 'too far!' in data_type):

                    warn = "Other bond constraint "\
                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, {chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}) "\
                        f"is too {'close each other' if 'close' in data_type else 'far apart'} ({dist}Å)."

                    self._reg.report.warning.appendDescription('unusual_data',
                                                               {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                'category': lp_category, 'description': warn})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfCovalentBond() ++ Warning  - {warn}\n")

                if data_type in count:
                    count[data_type] += 1
                else:
                    count[data_type] = 1

                if poly_seq is not None:

                    # count on map

                    if chain_id_1 == chain_id_2:

                        for c in count_on_map:
                            if data_type not in c:
                                c[data_type] = []
                            if c['chain_id'] == chain_id_1:
                                try:
                                    b = next(b for b in c[data_type] if b['seq_id_1'] == seq_id_1 and b['seq_id_2'] == seq_id_2)
                                    b['total'] += 1
                                except StopIteration:
                                    if seq_id_1 in c['seq_id'] and seq_id_2 in c['seq_id']:
                                        c[data_type].append({'seq_id_1': seq_id_1, 'seq_id_2': seq_id_2, 'total': 1})

                    else:

                        for c in count_on_asym_map:
                            if data_type not in c:
                                c[data_type] = []
                            if c['chain_id_1'] == chain_id_1 and c['chain_id_2'] == chain_id_2:
                                try:
                                    b = next(b for b in c[data_type] if b['seq_id_1'] == seq_id_1 and b['seq_id_2'] == seq_id_2)
                                    b['total'] += 1
                                except StopIteration:
                                    if seq_id_1 in c['seq_id_1'] and seq_id_2 in c['seq_id_2']:
                                        c[data_type].append({'seq_id_1': seq_id_1, 'seq_id_2': seq_id_2, 'total': 1})
                            elif c['chain_id_1'] == chain_id_2 and c['chain_id_2'] == chain_id_1:
                                try:
                                    b = next(b for b in c[data_type] if b['seq_id_1'] == seq_id_2 and b['seq_id_2'] == seq_id_1)
                                    b['total'] += 1
                                except StopIteration:
                                    if seq_id_1 in c['seq_id_1'] and seq_id_2 in c['seq_id_2']:
                                        c[data_type].append({'seq_id_1': seq_id_2, 'seq_id_2': seq_id_1, 'total': 1})
                            if not has_inter_chain_constraint and len(c[data_type]) > 0:
                                has_inter_chain_constraint = True

            if len(count) == 0:
                return

            ent['number_of_constraints'] = count
            if poly_seq is not None:
                ent['constraints_on_contact_map'] = count_on_map
            if has_inter_chain_constraint:
                ent['constraints_on_asym_contact_map'] = count_on_asym_map

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.__calculateStatsOfCovalentBond() "
                                                     "++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfCovalentBond() ++ Error  - {str(e)}\n")

    def _getTypeOfDistanceRestraint(self, file_type: str, row_id: int,
                                    target_value: float, upper_limit: float, lower_limit: float, member_id: Optional[int],
                                    chain_id_1: str, seq_id_1: int, comp_id_1: str, atom_id_1: str,
                                    chain_id_2: str, seq_id_2: int, comp_id_2: str, atom_id_2: str,
                                    get_symmetry_index: Callable[[], dict]) -> str:
        """ Return type of distance restraint.
        """

        hydrogen_bond_type = disulfide_bond_type = diselenide_bond_type = other_bond_type = None

        hydrogen_bond = disulfide_bond = diselenide_bond = other_bond = symmetry = False

        if chain_id_1 != chain_id_2 or seq_id_1 != seq_id_2:

            atom_id_1_ = atom_id_1[0]
            atom_id_2_ = atom_id_2[0]

            if upper_limit is not None:
                target_value -= 0.4

            if lower_limit is not None:
                target_value += 0.4

            balanced = (upper_limit is None and lower_limit is None)\
                or (upper_limit is not None and lower_limit is not None)\
                or (upper_limit is not None and upper_limit == 0.0)\
                or (lower_limit is not None and lower_limit == 0.0)

            delta_minus = 0.1 if upper_limit is not None and lower_limit is not None else 0.0

            ambig = member_id is not None or (upper_limit is not None
                                              and (upper_limit <= DIST_AMBIG_LOW or upper_limit >= DIST_AMBIG_UP))

            if not ambig:

                if (atom_id_1_ == 'F' and atom_id_2_ in PROTON_BEGIN_CODE)\
                   or (atom_id_2_ == 'F' and atom_id_1_ in PROTON_BEGIN_CODE):

                    if 1.2 - delta_minus <= target_value <= 1.5:
                        hydrogen_bond_type = 'F...H-x'
                        hydrogen_bond = True
                    elif target_value < 1.2 - delta_minus:
                        hydrogen_bond_type = 'F...H-x (too close!)'
                        hydrogen_bond = True
                    elif target_value <= 2.0:
                        hydrogen_bond_type = 'F...H-x (too far!)'
                        hydrogen_bond = True

                elif (atom_id_1_ == 'F' and atom_id_2_ == 'F') or (atom_id_2_ == 'F' and atom_id_1_ == 'F'):

                    if 2.2 - delta_minus <= target_value <= 2.5:
                        hydrogen_bond_type = 'F...h-F'
                        hydrogen_bond = True
                    elif target_value < 2.2 - delta_minus:
                        hydrogen_bond_type = 'F...h-F (too close!)'
                        hydrogen_bond = True
                    elif target_value <= 3.0:
                        hydrogen_bond_type = 'F...h-F (too far!)'
                        hydrogen_bond = True

                elif (atom_id_1_ == 'O' and atom_id_2_ in PROTON_BEGIN_CODE)\
                        or (atom_id_2_ == 'O' and atom_id_1_ in PROTON_BEGIN_CODE):

                    if 1.5 - delta_minus <= target_value <= 2.5:
                        hydrogen_bond_type = 'O...H-x'
                        hydrogen_bond = True
                    elif target_value < 1.5 - delta_minus:
                        hydrogen_bond_type = 'O...H-x (too close!)'
                        hydrogen_bond = True
                    elif target_value <= 4.0:
                        hydrogen_bond_type = 'O...H-x (too far!)'
                        hydrogen_bond = True

                elif (atom_id_1_ == 'O' and atom_id_2_ == 'N') or (atom_id_2_ == 'O' and atom_id_1_ == 'N'):

                    if 2.5 - delta_minus <= target_value <= 3.5:
                        hydrogen_bond_type = 'O...h-N'
                        hydrogen_bond = True
                    elif target_value < 2.5 - delta_minus:
                        hydrogen_bond_type = 'O...h-N (too close!)'
                        hydrogen_bond = True
                    elif target_value <= 5.0:
                        hydrogen_bond_type = 'O...h-N (too far!)'
                        hydrogen_bond = True

                elif (atom_id_1_ == 'O' and atom_id_2_ == 'O') or (atom_id_2_ == 'O' and atom_id_1_ == 'O'):

                    if 2.5 - delta_minus <= target_value <= 3.5:
                        hydrogen_bond_type = 'O...h-O'
                        hydrogen_bond = True
                    elif target_value < 2.5 - delta_minus:
                        hydrogen_bond_type = 'O...h-O (too close!)'
                        hydrogen_bond = True
                    elif target_value <= 5.0:
                        hydrogen_bond_type = 'O...h-O (too far!)'
                        hydrogen_bond = True

                elif (atom_id_1_ == 'N' and atom_id_2_ in PROTON_BEGIN_CODE)\
                        or (atom_id_2_ == 'N' and atom_id_1_ in PROTON_BEGIN_CODE):

                    if 1.5 - delta_minus <= target_value <= 2.5:
                        hydrogen_bond_type = 'N...H-x'
                        hydrogen_bond = True
                    elif target_value < 1.5 - delta_minus:
                        hydrogen_bond_type = 'N...H-x (too close!)'
                        hydrogen_bond = True
                    elif target_value <= 4.0:
                        hydrogen_bond_type = 'N...H-x (too far!)'
                        hydrogen_bond = True

                elif (atom_id_1_ == 'N' and atom_id_2_ == 'N') or (atom_id_2_ == 'N' and atom_id_1_ == 'N'):

                    if 2.5 - delta_minus <= target_value <= 3.5:
                        hydrogen_bond_type = 'N...h_N'
                        hydrogen_bond = True
                    elif target_value < 2.5 - delta_minus:
                        hydrogen_bond_type = 'N...h_N (too close!)'
                        hydrogen_bond = True
                    elif target_value <= 5.0:
                        hydrogen_bond_type = 'N...h_N (too far!)'
                        hydrogen_bond = True

                elif atom_id_1_ == 'S' and atom_id_2_ == 'S' and not atom_id_1.startswith('SE') and not atom_id_2.startswith('SE'):

                    if 1.9 - delta_minus <= target_value <= 2.3:
                        disulfide_bond_type = 'S...S'
                        disulfide_bond = True
                    elif target_value < 1.9 - delta_minus:
                        disulfide_bond_type = 'S...S (too close!)'
                        disulfide_bond = True
                    elif target_value <= 3.6:
                        disulfide_bond_type = 'S...S (too far!)'
                        disulfide_bond = True

                elif atom_id_1.startswith('SE') and atom_id_2.startswith('SE'):

                    if 2.1 - delta_minus <= target_value <= 2.6:
                        diselenide_bond_type = 'Se...Se'
                        diselenide_bond = True
                    elif target_value < 2.1 - delta_minus:
                        diselenide_bond_type = 'Se...Se (too close!)'
                        diselenide_bond = True
                    elif target_value <= 4.2:
                        diselenide_bond_type = 'Se...Se (too far!)'
                        diselenide_bond = True

                elif (atom_id_1_ == 'N' and not is_non_metal_element(comp_id_2, atom_id_2))\
                        or (atom_id_2_ == 'N' and not is_non_metal_element(comp_id_1, atom_id_1)):

                    metal = atom_id_2 if is_non_metal_element(comp_id_1, atom_id_1) else atom_id_1
                    metal = metal.title()

                    if 1.9 - delta_minus <= target_value <= 2.1 or not balanced:
                        other_bond_type = f'N...{metal}'
                        other_bond = True
                    elif target_value < 1.9 - delta_minus:
                        other_bond_type = f'N...{metal} (too close!)'
                        other_bond = True
                    elif target_value <= 3.2:
                        other_bond_type = f'N...{metal} (too far!)'
                        other_bond = True

                elif (atom_id_1_ == 'O' and not is_non_metal_element(comp_id_2, atom_id_2))\
                        or (atom_id_2_ == 'O' and not is_non_metal_element(comp_id_1, atom_id_1)):

                    metal = atom_id_2 if is_non_metal_element(comp_id_1, atom_id_1) else atom_id_1
                    metal = metal.title()

                    if 2.0 - delta_minus <= target_value <= 2.2 or not balanced:
                        other_bond_type = f'O...{metal}'
                        other_bond = True
                    elif target_value < 2.0 - delta_minus:
                        other_bond_type = f'O...{metal} (too close!)'
                        other_bond = True
                    elif target_value <= 3.4:
                        other_bond_type = f'O...{metal} (too far!)'
                        other_bond = True

                elif (atom_id_1_ == 'P' and not is_non_metal_element(comp_id_2, atom_id_2))\
                        or (atom_id_2_ == 'P' and not is_non_metal_element(comp_id_1, atom_id_1)):

                    metal = atom_id_2 if is_non_metal_element(comp_id_1, atom_id_1) else atom_id_1
                    metal = metal.title()

                    if 2.1 - delta_minus <= target_value <= 2.5 or not balanced:
                        other_bond_type = f'P...{metal}'
                        other_bond = True
                    elif target_value < 2.1 - delta_minus:
                        other_bond_type = f'P...{metal} (too close!)'
                        other_bond = True
                    elif target_value <= 4.0:
                        other_bond_type = f'P...{metal} (too far!)'
                        other_bond = True

                elif (atom_id_1_ == 'S' and not atom_id_1.startswith('SE')
                      and not is_non_metal_element(comp_id_2, atom_id_2))\
                        or (atom_id_2_ == 'S' and not atom_id_2.startswith('SE')
                            and not is_non_metal_element(comp_id_1, atom_id_1)):

                    metal = atom_id_2 if is_non_metal_element(comp_id_1, atom_id_1) else atom_id_1
                    metal = metal.title()

                    if 2.2 - delta_minus <= target_value <= 2.6 or not balanced:
                        other_bond_type = f'S...{metal}'
                        other_bond = True
                    elif target_value < 2.2 - delta_minus:
                        other_bond_type = f'S...{metal} (too close!)'
                        other_bond = True
                    elif target_value <= 4.2:
                        other_bond_type = f'S...{metal} (too far!)'
                        other_bond = True

                elif (atom_id_1.startswith('SE') and not is_non_metal_element(comp_id_2, atom_id_2))\
                        or (atom_id_2.startswith('SE') and not is_non_metal_element(comp_id_1, atom_id_1)):

                    metal = atom_id_2 if is_non_metal_element(comp_id_1, atom_id_1) else atom_id_1
                    metal = metal.title()

                    if 2.3 - delta_minus <= target_value <= 2.7 or not balanced:
                        other_bond_type = f'Se...{metal}'
                        other_bond = True
                    elif target_value < 2.3 - delta_minus:
                        other_bond_type = f'Se...{metal} (too close!)'
                        other_bond = True
                    elif target_value <= 4.4:
                        other_bond_type = f'Se...{metal} (too far!)'
                        other_bond = True

                elif chain_id_1 != chain_id_2:

                    _symmetry_index = get_symmetry_index()

                    for _key in ((seq_id_1, comp_id_1, seq_id_2, comp_id_2),
                                 (seq_id_2, comp_id_2, seq_id_1, comp_id_1)):

                        for idx, _chain_id_1, _chain_id_2 in _symmetry_index.get(_key, ()):
                            if idx != row_id and _chain_id_1 != chain_id_1 and _chain_id_2 != chain_id_2:
                                symmetry = True
                                break

                        if symmetry:
                            break

        range_of_seq = abs(seq_id_1 - seq_id_2)

        if hydrogen_bond:
            if chain_id_1 != chain_id_2:
                data_type = 'inter-chain_hydrogen_bonds'
            elif range_of_seq > 5:
                data_type = 'long_range_hydrogen_bonds'
            else:
                data_type = 'hydrogen_bonds'
            data_type += f'_{hydrogen_bond_type}'
        elif disulfide_bond:
            if chain_id_1 != chain_id_2:
                data_type = 'inter-chain_disulfide_bonds'
            elif range_of_seq > 5:
                data_type = 'long_range_disulfide_bonds'
            else:
                data_type = 'disulfide_bonds'
            data_type += f'_{disulfide_bond_type}'
        elif diselenide_bond:
            if chain_id_1 != chain_id_2:
                data_type = 'inter-chain_diselenide_bonds'
            elif range_of_seq > 5:
                data_type = 'long_range_diselenide_bonds'
            else:
                data_type = 'diselenide_bonds'
            data_type += f'_{diselenide_bond_type}'
        elif other_bond:
            if chain_id_1 != chain_id_2:
                data_type = 'inter-chain_other_bonds'
            elif range_of_seq > 5:
                data_type = 'long_range_other_bonds'
            else:
                data_type = 'other_bonds'
            data_type += f'_{other_bond_type}'
        elif symmetry:
            data_type = 'symmetric_constraints'
        elif chain_id_1 != chain_id_2:
            data_type = 'inter-chain_constraints'
        elif range_of_seq == 0:
            data_type = 'intra-residue_constraints'
        elif range_of_seq < 5:

            if file_type == 'nef' or (self.isNmrAtomName(comp_id_1, atom_id_1)
                                      or self.isNmrAtomName(comp_id_2, atom_id_2)):
                _atom_id_1 = self.getAtomIdList(comp_id_1, atom_id_1)
                _atom_id_2 = self.getAtomIdList(comp_id_2, atom_id_2)

                if len(_atom_id_1) > 0 and len(_atom_id_2) > 0:
                    is_sc_atom_1 = _atom_id_1[0] in self._reg.csStat.getSideChainAtoms(comp_id_1, incl_nstd_bb_atom=True)
                    is_sc_atom_2 = _atom_id_2[0] in self._reg.csStat.getSideChainAtoms(comp_id_2, incl_nstd_bb_atom=True)

                    if is_sc_atom_1:
                        is_bb_atom_1 = False
                    else:
                        is_bb_atom_1 = _atom_id_1[0] in self._reg.csStat.getBackBoneAtoms(comp_id_1, incl_nstd_bb_atom=True)

                    if is_sc_atom_2:
                        is_bb_atom_2 = False
                    else:
                        is_bb_atom_2 = _atom_id_2[0] in self._reg.csStat.getBackBoneAtoms(comp_id_2, incl_nstd_bb_atom=True)

                else:
                    is_bb_atom_1 = is_bb_atom_2 = is_sc_atom_1 = is_sc_atom_2 = False

            else:
                is_sc_atom_1 = atom_id_1 in self._reg.csStat.getSideChainAtoms(comp_id_1, incl_nstd_bb_atom=True)
                is_sc_atom_2 = atom_id_2 in self._reg.csStat.getSideChainAtoms(comp_id_2, incl_nstd_bb_atom=True)

                if is_sc_atom_1:
                    is_bb_atom_1 = False
                else:
                    is_bb_atom_1 = atom_id_1 in self._reg.csStat.getBackBoneAtoms(comp_id_1, incl_nstd_bb_atom=True)

                if is_sc_atom_2:
                    is_bb_atom_2 = False
                else:
                    is_bb_atom_2 = atom_id_2 in self._reg.csStat.getBackBoneAtoms(comp_id_2, incl_nstd_bb_atom=True)

            is_bb_bb = is_bb_atom_1 and is_bb_atom_2
            is_bb_sc = (is_bb_atom_1 and is_sc_atom_2) or (is_sc_atom_1 and is_bb_atom_2)
            is_sc_sc = is_sc_atom_1 and is_sc_atom_2

            if range_of_seq == 1:
                data_type = 'sequential_constraints'
            else:
                data_type = 'medium_range_constraints'

            if is_bb_bb:
                data_type += '_backbone-backbone'
            elif is_bb_sc:
                data_type += '_backbone-sidechain'
            elif is_sc_sc:
                data_type += '_sidechain-sidechain'
        else:
            data_type = 'long_range_constraints'

        return data_type

    def _getTypeOfCovalentBond(self, file_type: str, lp_data: List[dict], row_id: int, target_value: float,
                               chain_id_1: str, seq_id_1: int, comp_id_1: str, atom_id_1: str,
                               chain_id_2: str, seq_id_2: int, comp_id_2: str, atom_id_2: str) -> str:
        """ Return type of covalent bond.
        """

        item_names = ITEM_NAMES_IN_DIST_LOOP[file_type]
        chain_id_1_name = item_names['chain_id_1']
        chain_id_2_name = item_names['chain_id_2']
        seq_id_1_name = item_names['seq_id_1']
        seq_id_2_name = item_names['seq_id_2']
        comp_id_1_name = item_names['comp_id_1']
        comp_id_2_name = item_names['comp_id_2']

        def ext_comp_names(row):
            return (row[chain_id_1_name], row[chain_id_2_name],
                    row[seq_id_1_name], row[seq_id_2_name],
                    row[comp_id_1_name], row[comp_id_2_name])

        hydrogen_bond_type = disulfide_bond_type = diselenide_bond_type = other_bond_type = None

        hydrogen_bond = disulfide_bond = diselenide_bond = other_bond = symmetry = False

        if chain_id_1 != chain_id_2 or seq_id_1 != seq_id_2:

            atom_id_1_ = atom_id_1[0]
            atom_id_2_ = atom_id_2[0]

            if (atom_id_1_ == 'F' and atom_id_2_ in PROTON_BEGIN_CODE) or (atom_id_2_ == 'F' and atom_id_1_ in PROTON_BEGIN_CODE):

                if 1.2 <= target_value <= 1.5:
                    hydrogen_bond_type = 'F...H-x'
                    hydrogen_bond = True
                elif target_value < 1.2:
                    hydrogen_bond_type = 'F...H-x (too close!)'
                    hydrogen_bond = True
                elif target_value <= 2.0:
                    hydrogen_bond_type = 'F...H-x (too far!)'
                    hydrogen_bond = True

            elif (atom_id_1_ == 'F' and atom_id_2_ == 'F') or (atom_id_2_ == 'F' and atom_id_1_ == 'F'):

                if 2.2 <= target_value <= 2.5:
                    hydrogen_bond_type = 'F...h-F'
                    hydrogen_bond = True
                elif target_value < 2.2:
                    hydrogen_bond_type = 'F...h-F (too close!)'
                    hydrogen_bond = True
                elif target_value <= 3.0:
                    hydrogen_bond_type = 'F...h-F (too far!)'
                    hydrogen_bond = True

            elif (atom_id_1_ == 'O' and atom_id_2_ in PROTON_BEGIN_CODE) or (atom_id_2_ == 'O' and atom_id_1_ in PROTON_BEGIN_CODE):

                if 1.5 <= target_value <= 2.5:
                    hydrogen_bond_type = 'O...H-x'
                    hydrogen_bond = True
                elif target_value < 1.5:
                    hydrogen_bond_type = 'O...H-x (too close!)'
                    hydrogen_bond = True
                elif target_value <= 4.0:
                    hydrogen_bond_type = 'O...H-x (too far!)'
                    hydrogen_bond = True

            elif (atom_id_1_ == 'O' and atom_id_2_ == 'N') or (atom_id_2_ == 'O' and atom_id_1_ == 'N'):

                if 2.5 <= target_value <= 3.5:
                    hydrogen_bond_type = 'O...h-N'
                    hydrogen_bond = True
                elif target_value < 2.5:
                    hydrogen_bond_type = 'O...h-N (too close!)'
                    hydrogen_bond = True
                elif target_value <= 5.0:
                    hydrogen_bond_type = 'O...h-N (too far!)'
                    hydrogen_bond = True

            elif (atom_id_1_ == 'O' and atom_id_2_ == 'O') or (atom_id_2_ == 'O' and atom_id_1_ == 'O'):

                if 2.5 <= target_value <= 3.5:
                    hydrogen_bond_type = 'O...h-O'
                    hydrogen_bond = True
                elif target_value < 2.5:
                    hydrogen_bond_type = 'O...h-O (too close!)'
                    hydrogen_bond = True
                elif target_value <= 5.0:
                    hydrogen_bond_type = 'O...h-O (too far!)'
                    hydrogen_bond = True

            elif (atom_id_1_ == 'N' and atom_id_2_ in PROTON_BEGIN_CODE) or (atom_id_2_ == 'N' and atom_id_1_ in PROTON_BEGIN_CODE):

                if 1.5 <= target_value <= 2.5:
                    hydrogen_bond_type = 'N...H-x'
                    hydrogen_bond = True
                elif target_value < 1.5:
                    hydrogen_bond_type = 'N...H-x (too close!)'
                    hydrogen_bond = True
                elif target_value <= 4.0:
                    hydrogen_bond_type = 'N...H-x (too far!)'
                    hydrogen_bond = True

            elif (atom_id_1_ == 'N' and atom_id_2_ == 'N') or (atom_id_2_ == 'N' and atom_id_1_ == 'N'):

                if 2.5 <= target_value <= 3.5:
                    hydrogen_bond_type = 'N...h_N'
                    hydrogen_bond = True
                elif target_value < 2.5:
                    hydrogen_bond_type = 'N...h_N (too close!)'
                    hydrogen_bond = True
                elif target_value <= 5.0:
                    hydrogen_bond_type = 'N...h_N (too far!)'
                    hydrogen_bond = True

            elif atom_id_1_ == 'S' and atom_id_2_ == 'S' and not atom_id_1.startswith('SE') and not atom_id_2.startswith('SE'):

                if 1.9 <= target_value <= 2.3:
                    disulfide_bond_type = 'S...S'
                    disulfide_bond = True
                elif target_value < 1.9:
                    disulfide_bond_type = 'S...S (too close!)'
                    disulfide_bond = True
                elif target_value <= 3.6:
                    disulfide_bond_type = 'S...S (too far!)'
                    disulfide_bond = True

            elif atom_id_1.startswith('SE') and atom_id_2.startswith('SE'):

                if 2.1 <= target_value <= 2.6:
                    diselenide_bond_type = 'Se...Se'
                    diselenide_bond = True
                elif target_value < 2.1:
                    diselenide_bond_type = 'Se...Se (too close!)'
                    diselenide_bond = True
                elif target_value <= 4.2:
                    diselenide_bond_type = 'Se...Se (too far!)'
                    diselenide_bond = True

            elif (atom_id_1_ == 'N' and not is_non_metal_element(comp_id_2, atom_id_2))\
                    or (atom_id_2_ == 'N' and not is_non_metal_element(comp_id_1, atom_id_1)):

                metal = atom_id_2 if is_non_metal_element(comp_id_1, atom_id_1) else atom_id_1
                metal = metal.title()

                if 1.9 <= target_value <= 2.1:
                    other_bond_type = f'N...{metal}'
                    other_bond = True
                elif target_value < 1.9:
                    other_bond_type = f'N...{metal} (too close!)'
                    other_bond = True
                elif target_value <= 3.2:
                    other_bond_type = f'N...{metal} (too far!)'
                    other_bond = True

            elif (atom_id_1_ == 'O' and not is_non_metal_element(comp_id_2, atom_id_2))\
                    or (atom_id_2_ == 'O' and not is_non_metal_element(comp_id_1, atom_id_1)):

                metal = atom_id_2 if is_non_metal_element(comp_id_1, atom_id_1) else atom_id_1
                metal = metal.title()

                if 2.0 <= target_value <= 2.2:
                    other_bond_type = f'O...{metal}'
                    other_bond = True
                elif target_value < 2.0:
                    other_bond_type = f'O...{metal} (too close!)'
                    other_bond = True
                elif target_value <= 3.4:
                    other_bond_type = f'O...{metal} (too far!)'
                    other_bond = True

            elif (atom_id_1_ == 'P' and not is_non_metal_element(comp_id_2, atom_id_2))\
                    or (atom_id_2_ == 'P' and not is_non_metal_element(comp_id_1, atom_id_1)):

                metal = atom_id_2 if is_non_metal_element(comp_id_1, atom_id_1) else atom_id_1
                metal = metal.title()

                if 2.1 <= target_value <= 2.5:
                    other_bond_type = f'P...{metal}'
                    other_bond = True
                elif target_value < 2.1:
                    other_bond_type = f'P...{metal} (too close!)'
                    other_bond = True
                elif target_value <= 4.0:
                    other_bond_type = f'P...{metal} (too far!)'
                    other_bond = True

            elif (atom_id_1_ == 'S' and not atom_id_1.startswith('SE') and not is_non_metal_element(comp_id_2, atom_id_2))\
                    or (atom_id_2_ == 'S' and not atom_id_2.startswith('SE') and not is_non_metal_element(comp_id_1, atom_id_1)):

                metal = atom_id_2 if is_non_metal_element(comp_id_1, atom_id_1) else atom_id_1
                metal = metal.title()

                if 2.2 <= target_value <= 2.6:
                    other_bond_type = f'S...{metal}'
                    other_bond = True
                elif target_value < 2.2:
                    other_bond_type = f'S...{metal} (too close!)'
                    other_bond = True
                elif target_value <= 4.2:
                    other_bond_type = f'S...{metal} (too far!)'
                    other_bond = True

            elif (atom_id_1.startswith('SE') and not is_non_metal_element(comp_id_2, atom_id_2))\
                    or (atom_id_2.startswith('SE') and not is_non_metal_element(comp_id_1, atom_id_1)):

                metal = atom_id_2 if is_non_metal_element(comp_id_1, atom_id_1) else atom_id_1
                metal = metal.title()

                if 2.3 <= target_value <= 2.7:
                    other_bond_type = f'Se...{metal}'
                    other_bond = True
                elif target_value < 2.3:
                    other_bond_type = f'Se...{metal} (too close!)'
                    other_bond = True
                elif target_value <= 4.4:
                    other_bond_type = f'Se...{metal} (too far!)'
                    other_bond = True

            elif chain_id_1 != chain_id_2:

                for idx, row in enumerate(lp_data):

                    if idx == row_id:
                        continue

                    _chain_id_1, _chain_id_2, _seq_id_1, _seq_id_2, \
                        _comp_id_1, _comp_id_2 = ext_comp_names(row)

                    if _chain_id_1 != _chain_id_2 and _chain_id_1 != chain_id_1 and _chain_id_2 != chain_id_2:

                        if seq_id_1 == _seq_id_1 and comp_id_1 == _comp_id_1\
                           and seq_id_2 == _seq_id_2 and comp_id_2 == _comp_id_2:
                            symmetry = True
                            break

                        if seq_id_1 == _seq_id_2 and comp_id_1 == _comp_id_2\
                           and seq_id_2 == _seq_id_1 and comp_id_2 == _comp_id_1:
                            symmetry = True
                            break

        range_of_seq = abs(seq_id_1 - seq_id_2)

        if hydrogen_bond:
            if chain_id_1 != chain_id_2:
                data_type = 'inter-chain_hydrogen_bonds'
            elif range_of_seq > 5:
                data_type = 'long_range_hydrogen_bonds'
            else:
                data_type = 'hydrogen_bonds'
            data_type += f'_{hydrogen_bond_type}'
        elif disulfide_bond:
            if chain_id_1 != chain_id_2:
                data_type = 'inter-chain_disulfide_bonds'
            elif range_of_seq > 5:
                data_type = 'long_range_disulfide_bonds'
            else:
                data_type = 'disulfide_bonds'
            data_type += f'_{disulfide_bond_type}'
        elif diselenide_bond:
            if chain_id_1 != chain_id_2:
                data_type = 'inter-chain_diselenide_bonds'
            elif range_of_seq > 5:
                data_type = 'long_range_diselenide_bonds'
            else:
                data_type = 'diselenide_bonds'
            data_type += f'_{diselenide_bond_type}'
        elif other_bond:
            if chain_id_1 != chain_id_2:
                data_type = 'inter-chain_other_bonds'
            elif range_of_seq > 5:
                data_type = 'long_range_other_bonds'
            else:
                data_type = 'other_bonds'
            data_type += f'_{other_bond_type}'
        elif symmetry:
            data_type = 'symmetric_constraints'
        elif chain_id_1 != chain_id_2:
            data_type = 'inter-chain_constraints'
        elif range_of_seq == 0:
            data_type = 'intra-residue_constraints'
        elif range_of_seq < 5:

            if file_type == 'nef' or (self.isNmrAtomName(comp_id_1, atom_id_1)
                                      or self.isNmrAtomName(comp_id_2, atom_id_2)):
                _atom_id_1 = self.getAtomIdList(comp_id_1, atom_id_1)
                _atom_id_2 = self.getAtomIdList(comp_id_2, atom_id_2)

                if len(_atom_id_1) > 0 and len(_atom_id_2) > 0:
                    is_sc_atom_1 = _atom_id_1[0] in self._reg.csStat.getSideChainAtoms(comp_id_1, incl_nstd_bb_atom=True)
                    is_sc_atom_2 = _atom_id_2[0] in self._reg.csStat.getSideChainAtoms(comp_id_2, incl_nstd_bb_atom=True)

                    if is_sc_atom_1:
                        is_bb_atom_1 = False
                    else:
                        is_bb_atom_1 = _atom_id_1[0] in self._reg.csStat.getBackBoneAtoms(comp_id_1, incl_nstd_bb_atom=True)

                    if is_sc_atom_2:
                        is_bb_atom_2 = False
                    else:
                        is_bb_atom_2 = _atom_id_2[0] in self._reg.csStat.getBackBoneAtoms(comp_id_2, incl_nstd_bb_atom=True)

                else:
                    is_bb_atom_1 = is_bb_atom_2 = is_sc_atom_1 = is_sc_atom_2 = False

            else:
                is_sc_atom_1 = atom_id_1 in self._reg.csStat.getSideChainAtoms(comp_id_1, incl_nstd_bb_atom=True)
                is_sc_atom_2 = atom_id_2 in self._reg.csStat.getSideChainAtoms(comp_id_2, incl_nstd_bb_atom=True)

                if is_sc_atom_1:
                    is_bb_atom_1 = False
                else:
                    is_bb_atom_1 = atom_id_1 in self._reg.csStat.getBackBoneAtoms(comp_id_1, incl_nstd_bb_atom=True)

                if is_sc_atom_2:
                    is_bb_atom_2 = False
                else:
                    is_bb_atom_2 = atom_id_2 in self._reg.csStat.getBackBoneAtoms(comp_id_2, incl_nstd_bb_atom=True)

            is_bb_bb = is_bb_atom_1 and is_bb_atom_2
            is_bb_sc = (is_bb_atom_1 and is_sc_atom_2) or (is_sc_atom_1 and is_bb_atom_2)
            is_sc_sc = is_sc_atom_1 and is_sc_atom_2

            if range_of_seq == 1:
                data_type = 'sequential_constraints'
            else:
                data_type = 'medium_range_constraints'

            if is_bb_bb:
                data_type += '_backbone-backbone'
            elif is_bb_sc:
                data_type += '_backbone-sidechain'
            elif is_sc_sc:
                data_type += '_sidechain-sidechain'
        else:
            data_type = 'long_range_constraints'

        return data_type

    def _calculateStatsOfDihedralRestraint(self, file_list_id: int, sf_framecode: str, lp_data: List[dict],
                                           conflict_id_set: Optional[List[int]], inconsistent: Set[int],
                                           redundant: Set[int], ent: dict) -> None:
        """ Calculate statistics of dihedral angle restraints.
        """

        input_source = self._reg.report.input_sources[file_list_id]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        content_subtype = 'dihed_restraint'

        index_tag = INDEX_TAGS[file_type][content_subtype]
        item_names = POTENTIAL_ITEMS[file_type][content_subtype]
        target_value_name = item_names['target_value']
        lower_limit_name = item_names['lower_limit']
        upper_limit_name = item_names['upper_limit']
        lower_linear_limit_name = item_names['lower_linear_limit']
        upper_linear_limit_name = item_names['upper_linear_limit']

        def get_est_target_value(row):
            value = row.get(target_value_name)

            if value is None:

                if has_key_value(row, lower_limit_name)\
                        and has_key_value(row, upper_limit_name):
                    value = (row[lower_limit_name] + row[upper_limit_name]) / 2.0

                elif has_key_value(row, lower_linear_limit_name)\
                        and has_key_value(row, upper_linear_limit_name):
                    value = (row[lower_linear_limit_name] + row[upper_linear_limit_name]) / 2.0

                elif has_key_value(row, upper_linear_limit_name):
                    value = row[upper_linear_limit_name]

                elif has_key_value(row, upper_limit_name):
                    value = row[upper_limit_name]

                elif has_key_value(row, lower_linear_limit_name):
                    value = row[lower_linear_limit_name]

                elif has_key_value(row, lower_limit_name):
                    value = row[lower_limit_name]

            return value

        dh_item_names = ITEM_NAMES_IN_DIHED_LOOP[file_type]
        combination_id_name = dh_item_names['combination_id']
        chain_id_1_name = dh_item_names['chain_id_1']
        chain_id_2_name = dh_item_names['chain_id_2']
        chain_id_3_name = dh_item_names['chain_id_3']
        chain_id_4_name = dh_item_names['chain_id_4']
        seq_id_1_name = dh_item_names['seq_id_1']
        seq_id_2_name = dh_item_names['seq_id_2']
        seq_id_3_name = dh_item_names['seq_id_3']
        seq_id_4_name = dh_item_names['seq_id_4']
        comp_id_1_name = dh_item_names['comp_id_1']
        comp_id_2_name = dh_item_names['comp_id_2']
        comp_id_3_name = dh_item_names['comp_id_3']
        comp_id_4_name = dh_item_names['comp_id_4']
        atom_id_1_name = dh_item_names['atom_id_1']
        atom_id_2_name = dh_item_names['atom_id_2']
        atom_id_3_name = dh_item_names['atom_id_3']
        atom_id_4_name = dh_item_names['atom_id_4']
        angle_type_name = dh_item_names['angle_type']
        weight_name = WEIGHT_TAGS[file_type][content_subtype]
        id_tag = CONSIST_ID_TAGS[file_type][content_subtype]

        def ext_atoms(row):
            return ({'chain_id': row[chain_id_1_name], 'seq_id': row[seq_id_1_name],
                     'comp_id': row[comp_id_1_name], 'atom_id': row[atom_id_1_name]},
                    {'chain_id': row[chain_id_2_name], 'seq_id': row[seq_id_2_name],
                     'comp_id': row[comp_id_2_name], 'atom_id': row[atom_id_2_name]},
                    {'chain_id': row[chain_id_3_name], 'seq_id': row[seq_id_3_name],
                     'comp_id': row[comp_id_3_name], 'atom_id': row[atom_id_3_name]},
                    {'chain_id': row[chain_id_4_name], 'seq_id': row[seq_id_4_name],
                     'comp_id': row[comp_id_4_name], 'atom_id': row[atom_id_4_name]})

        try:

            count, comb_count, inco_count, redu_count, polymer_types, weights, potential_types =\
                {}, {}, {}, {}, {}, {}, {}

            set_id = set()

            phi_list, psi_list, chi1_list, chi2_list, value_per_residue = [], [], [], [], []

            poly_seq = input_source_dic['polymer_sequence']

            if poly_seq is not None:

                for ps in poly_seq:
                    struct_conf = self._extractCoordStructConf(ps['chain_id'], ps['seq_id'])
                    value_per_residue.append({'chain_id': ps['chain_id'], 'seq_id': ps['seq_id'], 'comp_id': ps['comp_id'],
                                              'struct_conf': struct_conf})

            for row in lp_data:
                index = row.get(index_tag)
                combination_id = row.get(combination_id_name)

                target_value = row.get(target_value_name)

                if target_value is None:

                    if has_key_value(row, lower_limit_name)\
                            and has_key_value(row, upper_limit_name):
                        target_value = (row[lower_limit_name] + row[upper_limit_name]) / 2.0

                    elif has_key_value(row, lower_linear_limit_name)\
                            and has_key_value(row, upper_linear_limit_name):
                        target_value = (row[lower_linear_limit_name] + row[upper_linear_limit_name]) / 2.0

                    else:
                        continue

                target_value = round(target_value, 1)

                while target_value > 180.0:
                    target_value -= 360.0
                while target_value < -180.0:
                    target_value += 360.0

                if has_key_value(row, lower_limit_name)\
                        and has_key_value(row, upper_limit_name):
                    lower_limit = row[lower_limit_name]
                    upper_limit = row[upper_limit_name]

                    while lower_limit - target_value > 180.0:
                        lower_limit -= 360.0
                    while lower_limit - target_value < -180.0:
                        lower_limit += 360.0

                    while upper_limit - target_value > 180.0:
                        upper_limit -= 360.0
                    while upper_limit - target_value < -180.0:
                        upper_limit += 360.0

                elif has_key_value(row, lower_linear_limit_name)\
                        and has_key_value(row, upper_linear_limit_name):
                    lower_limit = row[lower_linear_limit_name]
                    upper_limit = row[upper_linear_limit_name]

                    while lower_limit - target_value > 180.0:
                        lower_limit -= 360.0
                    while lower_limit - target_value < -180.0:
                        lower_limit += 360.0

                    while upper_limit - target_value > 180.0:
                        upper_limit -= 360.0
                    while upper_limit - target_value < -180.0:
                        upper_limit += 360.0

                else:
                    lower_limit = upper_limit = None

                data_type = row[angle_type_name]

                if data_type == 'PPA':
                    continue

                atom1, atom2, atom3, atom4 = ext_atoms(row)

                weight = row.get(weight_name)
                set_id.add(row[id_tag])

                peptide, nucleotide, carbohydrate = self._reg.csStat.getTypeOfCompId(atom2['comp_id'])
                plane_like = is_like_planality_boundary(row, lower_limit_name, upper_limit_name)

                data_type =\
                    self.getTypeOfDihedralRestraint(data_type, peptide, nucleotide, carbohydrate,
                                                    [atom1, atom2, atom3, atom4], plane_like)

                if data_type in count:
                    count[data_type] += 1
                else:
                    count[data_type] = 1

                if (combination_id is not None) and (combination_id not in EMPTY_VALUE):
                    if data_type in comb_count:
                        comb_count[data_type] += 1
                    else:
                        comb_count[data_type] = 1

                if index is not None:

                    if index in inconsistent:
                        if data_type in inco_count:
                            inco_count[data_type] += 1
                        else:
                            inco_count[data_type] = 1

                    if index in redundant:
                        if data_type in redu_count:
                            redu_count[data_type] += 1
                        else:
                            redu_count[data_type] = 1

                if peptide:
                    if 'protein' in polymer_types:
                        polymer_types['protein'] += 1
                    else:
                        polymer_types['protein'] = 1

                if nucleotide:
                    if 'nucleic_acid' in polymer_types:
                        polymer_types['nucleic_acid'] += 1
                    else:
                        polymer_types['nucleic_acid'] = 1

                if carbohydrate:
                    if 'carbohydrate' in polymer_types:
                        polymer_types['carbohydrate'] += 1
                    else:
                        polymer_types['carbohydrate'] = 1

                if not peptide and not nucleotide and not carbohydrate:
                    if 'other' in polymer_types:
                        polymer_types['other'] += 1
                    else:
                        polymer_types['other'] = 1

                chain_id = atom1['chain_id']
                seq_ids = [atom1['seq_id'], atom2['seq_id'], atom3['seq_id'], atom4['seq_id']]
                comp_ids = [atom1['comp_id'], atom2['comp_id'], atom3['comp_id'], atom4['comp_id']]
                seq_id_common = collections.Counter(seq_ids).most_common()
                comp_id_common = collections.Counter(comp_ids).most_common()

                if data_type.startswith('phi_'):
                    phi = {}
                    phi['chain_id'] = chain_id
                    phi['seq_id'] = seq_id_common[0][0]
                    phi['comp_id'] = comp_id_common[0][0]
                    phi['value'] = target_value
                    phi['error'] = None if None in (lower_limit, upper_limit) else [lower_limit, upper_limit]
                    phi_list.append(phi)

                elif data_type.startswith('psi_'):
                    psi = {}
                    psi['chain_id'] = chain_id
                    psi['seq_id'] = seq_id_common[0][0]
                    psi['comp_id'] = comp_id_common[0][0]
                    psi['value'] = target_value
                    psi['error'] = None if None in (lower_limit, upper_limit) else [lower_limit, upper_limit]
                    psi_list.append(psi)

                elif data_type.startswith('chi1_'):
                    chi1 = {}
                    chi1['chain_id'] = chain_id
                    chi1['seq_id'] = seq_ids[0]
                    chi1['comp_id'] = comp_ids[0]
                    chi1['value'] = target_value
                    chi1['error'] = None if None in (lower_limit, upper_limit) else [lower_limit, upper_limit]
                    chi1_list.append(chi1)

                elif data_type.startswith('chi2_'):
                    chi2 = {}
                    chi2['chain_id'] = chain_id
                    chi2['seq_id'] = seq_ids[0]
                    chi2['comp_id'] = comp_ids[0]
                    chi2['value'] = target_value
                    chi2['error'] = None if None in (lower_limit, upper_limit) else [lower_limit, upper_limit]
                    chi2_list.append(chi2)

                # detect weight

                if weight is not None:
                    if data_type not in weights:
                        weights[data_type] = []
                    weights[data_type].append(weight)

                # detect potential type

                lower_limit = row.get(lower_limit_name)
                upper_limit = row.get(upper_limit_name)
                lower_linear_limit = row.get(lower_linear_limit_name)
                upper_linear_limit = row.get(upper_linear_limit_name)

                if (lower_limit is not None) and (upper_limit is not None)\
                        and lower_linear_limit is None and upper_linear_limit is None:
                    potential_type = 'square-well-parabolic'
                elif (lower_limit is not None) and (upper_limit is not None)\
                        and (lower_linear_limit is not None) and (upper_linear_limit is not None):
                    potential_type = 'square-well-parabolic-linear'
                elif lower_limit is None and (upper_limit is not None)\
                        and lower_linear_limit is None and upper_linear_limit is None:
                    potential_type = 'upper-bound-parabolic'
                elif (lower_limit is not None) and upper_limit is None\
                        and lower_linear_limit is None and upper_linear_limit is None:
                    potential_type = 'lower-bound-parabolic'
                elif lower_limit is None and (upper_limit is not None)\
                        and lower_linear_limit is None and (upper_linear_limit is not None):
                    potential_type = 'upper-bound-parabolic-linear'
                elif (lower_limit is not None) and upper_limit is None\
                        and (lower_linear_limit is not None) and upper_linear_limit is None:
                    potential_type = 'lower-bound-parabolic-linear'
                elif (target_value is not None) and lower_limit is None and upper_limit is None\
                        and lower_linear_limit is None and upper_linear_limit is None:
                    potential_type = 'parabolic'
                else:
                    potential_type = 'undefined'

                if potential_type is not None:
                    if data_type not in potential_types:
                        potential_types[data_type] = []
                    potential_types[data_type].append(potential_type)

                if poly_seq is not None:

                    # value per residue

                    for c in value_per_residue:
                        if data_type not in c:
                            c[data_type] = [None] * len(c['seq_id'])
                        if c['chain_id'] == chain_id and target_value is not None and seq_id_common[0][0] in c['seq_id']:
                            b = c['seq_id'].index(seq_id_common[0][0])
                            if c[data_type][b] is None:
                                c[data_type][b] = float(target_value)
                            else:
                                j = 2
                                while True:
                                    _data_type = f'{data_type}_{j}'
                                    if _data_type not in c:
                                        c[_data_type] = [None] * len(c['seq_id'])
                                    if c[_data_type][b] is None:
                                        c[_data_type][b] = float(target_value)
                                        break
                                    j += 1

            if len(count) > 0:
                ent['number_of_constraints'] = count
                ent['number_of_constraint_sets'] = len(set_id)
                if len(comb_count) > 0:
                    ent['number_of_combined_constraints'] = comb_count
                if len(inco_count) > 0:
                    ent['number_of_inconsistent_constraints'] = inco_count
                if len(redu_count) > 0:
                    ent['number_of_redundant_constraints'] = redu_count
                ent['constraints_per_polymer_type'] = polymer_types
                if poly_seq is not None:
                    ent['constraints_per_residue'] = value_per_residue
                if len(weights) > 0:
                    _weights = {}
                    for k, v in weights.items():
                        _weights[k] = collections.Counter(v).most_common()
                    ent['weight_of_constraints'] = _weights
                if len(potential_types) > 0:
                    _potential_types = {}
                    for k, v in potential_types.items():
                        _potential_types[k] = collections.Counter(v).most_common()
                    ent['potential_type_of_constraints'] = _potential_types

            if 'phi_angle_constraints' in count and 'psi_angle_constraints' in count:

                phi_psi_value, phi_psi_error = {}, {}

                for phi in phi_list:

                    comp_id = phi['comp_id']

                    for psi in [psi for psi in psi_list if psi['chain_id'] == phi['chain_id'] and psi['seq_id'] == phi['seq_id']]:

                        if comp_id not in phi_psi_value:
                            phi_psi_value[comp_id] = []

                        phi_psi_value[comp_id].append([phi['value'], psi['value'],
                                                       f"{phi['chain_id']}:{phi['seq_id']}:{phi['comp_id']}"])

                        if (phi['error'] is not None) or (psi['error'] is not None):

                            if comp_id not in phi_psi_error:
                                phi_psi_error[comp_id] = []

                            phi_psi_error[comp_id].append([phi['value'], psi['value'],
                                                           None if phi['error'] is None else phi['error'][0],
                                                           None if phi['error'] is None else phi['error'][1],
                                                           None if psi['error'] is None else psi['error'][0],
                                                           None if psi['error'] is None else psi['error'][1]])

                if len(phi_psi_value) > 0:

                    phi_psi_plot = {}

                    phi_psi_plot['values'] = phi_psi_value

                    if len(phi_psi_error) > 0:
                        phi_psi_plot['errors'] = phi_psi_error

                    ent['phi_psi_plot'] = phi_psi_plot

            if 'chi1_angle_constraints' in count and 'chi2_angle_constraints' in count:

                chi1_chi2_value, chi1_chi2_error = {}, {}

                for chi1 in chi1_list:

                    comp_id = chi1['comp_id']

                    for chi2 in [chi2 for chi2 in chi2_list
                                 if chi2['chain_id'] == chi1['chain_id'] and chi2['seq_id'] == chi1['seq_id']]:

                        if comp_id not in chi1_chi2_value:
                            chi1_chi2_value[comp_id] = []

                        chi1_chi2_value[comp_id].append([chi1['value'], chi2['value'],
                                                         f"{chi1['chain_id']}:{chi1['seq_id']}:{chi1['comp_id']}"])

                        if (chi1['error'] is not None) or (chi2['error'] is not None):

                            if comp_id not in chi1_chi2_error:
                                chi1_chi2_error[comp_id] = []

                            chi1_chi2_error[comp_id].append([chi1['value'], chi2['value'],
                                                            None if chi1['error'] is None else chi1['error'][0],
                                                            None if chi1['error'] is None else chi1['error'][1],
                                                            None if chi2['error'] is None else chi2['error'][0],
                                                            None if chi2['error'] is None else chi2['error'][1]])

                if len(chi1_chi2_value) > 0:

                    chi1_chi2_plot = {}

                    chi1_chi2_plot['values'] = chi1_chi2_value

                    if len(chi1_chi2_error) > 0:
                        chi1_chi2_plot['errors'] = chi1_chi2_error

                    ent['chi1_chi2_plot'] = chi1_chi2_plot

            if conflict_id_set is not None:

                max_inclusive = ANGLE_UNCERT_MAX

                max_val = min_val = 0.0

                dihed_ann = []

                for id_set in conflict_id_set:
                    len_id_set = len(id_set)

                    if len_id_set < 2:
                        continue

                    for i in range(len_id_set - 1):

                        for j in range(i + 1, len_id_set):
                            row_1 = lp_data[id_set[i]]
                            row_2 = lp_data[id_set[j]]

                            target_value_1 = get_est_target_value(row_1)
                            target_value_2 = get_est_target_value(row_2)

                            if None in (target_value_1, target_value_2):
                                continue

                            while target_value_1 > 180.0:
                                target_value_1 -= 360.0
                            while target_value_1 < -180.0:
                                target_value_1 += 360.0

                            while target_value_2 > 180.0:
                                target_value_2 -= 360.0
                            while target_value_2 < -180.0:
                                target_value_2 += 360.0

                            if target_value_1 == target_value_2:
                                continue

                            discrepancy = abs(target_value_1 - target_value_2)

                            if discrepancy > 180.0:
                                if target_value_1 < target_value_2:
                                    discrepancy = abs(target_value_1 - (target_value_2 - 360.0))
                                if target_value_1 > target_value_2:
                                    discrepancy = abs(target_value_1 - (target_value_2 + 360.0))

                            atom1, atom2, atom3, atom4 = ext_atoms(row_1)

                            data_type = row_1[angle_type_name]

                            peptide, nucleotide, carbohydrate = self._reg.csStat.getTypeOfCompId(atom2['comp_id'])
                            plane_like = is_like_planality_boundary(row_1, lower_limit_name, upper_limit_name)

                            data_type = self.getTypeOfDihedralRestraint(data_type, peptide, nucleotide, carbohydrate,
                                                                        [atom1, atom2, atom3, atom4], plane_like)[0]

                            if data_type.startswith('phi') or data_type.startswith('psi') or data_type.startswith('omega'):

                                max_val = max(max_val, discrepancy)

                                if discrepancy > max_inclusive * INCONSIST_OVER_CONFLICTED:
                                    ann = {}
                                    ann['level'] = 'conflicted' if discrepancy > max_inclusive else 'inconsistent'
                                    ann['chain_id'] = atom2['chain_id']
                                    ann['seq_id'] = atom2['seq_id']
                                    ann['comp_id'] = atom2['comp_id']
                                    ann['atom_id_1'] = atom1['atom_id']
                                    ann['atom_id_2'] = atom2['atom_id']
                                    ann['atom_id_3'] = atom3['atom_id']
                                    ann['atom_id_4'] = atom4['atom_id']
                                    ann['discrepancy'] = round(discrepancy, 1)

                                    dihed_ann.append(ann)

                if max_val > 0.0:
                    target_scale = (max_val - min_val) / 10.0

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
                            _count[k] = 0

                        for id_set in conflict_id_set:
                            len_id_set = len(id_set)

                            if len_id_set < 2:
                                continue

                            redundant = True

                            for i in range(len_id_set - 1):

                                for j in range(i + 1, len_id_set):
                                    row_1 = lp_data[id_set[i]]
                                    row_2 = lp_data[id_set[j]]

                                    target_value_1 = get_est_target_value(row_1)
                                    target_value_2 = get_est_target_value(row_2)

                                    if target_value_1 is None and target_value_2 is None:
                                        continue

                                    if None in (target_value_1, target_value_2):
                                        redundant = False
                                        continue

                                    while target_value_1 > 180.0:
                                        target_value_1 -= 360.0
                                    while target_value_1 < -180.0:
                                        target_value_1 += 360.0

                                    while target_value_2 > 180.0:
                                        target_value_2 -= 360.0
                                    while target_value_2 < -180.0:
                                        target_value_2 += 360.0

                                    if target_value_1 == target_value_2:
                                        continue

                                    redundant = False

                                    discrepancy = abs(target_value_1 - target_value_2)

                                    if discrepancy < v or discrepancy >= v + scale:
                                        continue

                                    atom1, atom2, atom3, atom4 = ext_atoms(row_1)

                                    peptide, nucleotide, carbohydrate = self._reg.csStat.getTypeOfCompId(atom2['comp_id'])
                                    plane_like = is_like_planality_boundary(row_1, lower_limit_name, upper_limit_name)

                                    data_type = self.getTypeOfDihedralRestraint(data_type, peptide, nucleotide, carbohydrate,
                                                                                [atom1, atom2, atom3, atom4], plane_like)[0]

                                    if data_type in _count:
                                        _count[data_type] += 1
                                    else:
                                        _count[data_type] = 1

                            if 0.0 <= v < scale and redundant:

                                atom1, atom2, atom3, atom4 = ext_atoms(row_1)

                                peptide, nucleotide, carbohydrate = self._reg.csStat.getTypeOfCompId(atom2['comp_id'])
                                plane_like = is_like_planality_boundary(row_1, lower_limit_name, upper_limit_name)

                                data_type = self.getTypeOfDihedralRestraint(data_type, peptide, nucleotide, carbohydrate,
                                                                            [atom1, atom2, atom3, atom4], plane_like)[0]

                                if data_type in _count:
                                    _count[data_type] += 1
                                else:
                                    _count[data_type] = 1

                        range_of_vals.append(v)
                        count_of_vals.append(_count)

                        v += scale

                    transposed = {}

                    for k in count:
                        transposed[k] = []

                        for count_of_val in count_of_vals:
                            transposed[k].append(count_of_val[k])

                    if len(range_of_vals) > 1:
                        ent['histogram_of_discrepancy'] = {'range_of_values': range_of_vals,
                                                           'number_of_values': transposed,
                                                           'annotations': dihed_ann}

            if file_type == 'nmr-star' and self._reg.star_data_type[file_list_id] == 'Entry':
                lp_category = LP_CATEGORIES[file_type][content_subtype]
                sf = self._reg.star_data[file_list_id].get_saveframe_by_name(sf_framecode)
                lp = next(lp for lp in sf.loops if lp.category == lp_category)

                ent['atom_name_mapping'] = get_atom_name_mapping(lp, [['Comp_ID_1', 'Atom_ID_1', 'Auth_atom_name_1'],
                                                                      ['Comp_ID_2', 'Atom_ID_2', 'Auth_atom_name_2'],
                                                                      ['Comp_ID_3', 'Atom_ID_3', 'Auth_atom_name_3'],
                                                                      ['Comp_ID_4', 'Atom_ID_4', 'Auth_atom_name_4']])

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.__calculateStatsOfDihedralRestraint() "
                                                     "++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfDihedralRestraint() "
                                    f"++ Error  - {str(e)}\n")

    def _calculateStatsOfRdcRestraint(self, file_list_id: int, sf_framecode: str, lp_data: List[dict],
                                      conflict_id_set: List[int], inconsistent: Set[int], redundant: Set[int], ent: dict
                                      ) -> None:
        """ Calculate statistics of RDC restraints.
        """

        input_source = self._reg.report.input_sources[file_list_id]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        content_subtype = 'rdc_restraint'

        index_tag = INDEX_TAGS[file_type][content_subtype]
        item_names = POTENTIAL_ITEMS[file_type][content_subtype]
        target_value_name = item_names['target_value']
        if 'target_value_alt' in item_names and target_value_name not in lp_data[0].keys():
            target_value_name = item_names['target_value_alt']
        lower_limit_name = item_names['lower_limit']
        upper_limit_name = item_names['upper_limit']
        lower_linear_limit_name = item_names['lower_linear_limit']
        upper_linear_limit_name = item_names['upper_linear_limit']

        def get_est_target_value(row):
            value = row.get(target_value_name)

            if value is None:

                if has_key_value(row, lower_limit_name)\
                        and has_key_value(row, upper_limit_name):
                    value = (row[lower_limit_name] + row[upper_limit_name]) / 2.0

                elif has_key_value(row, lower_linear_limit_name)\
                        and has_key_value(row, upper_linear_limit_name):
                    value = (row[lower_linear_limit_name] + row[upper_linear_limit_name]) / 2.0

                elif has_key_value(row, upper_linear_limit_name):
                    value = row[upper_linear_limit_name]

                elif has_key_value(row, upper_limit_name):
                    value = row[upper_limit_name]

                elif has_key_value(row, lower_linear_limit_name):
                    value = row[lower_linear_limit_name]

                elif has_key_value(row, lower_limit_name):
                    value = row[lower_limit_name]

            return value

        try:

            max_val = min_val = 0.0

            max_val_ = -100.0
            min_val_ = 100.0

            for row in lp_data:
                target_value = get_est_target_value(row)

                if target_value is None:
                    continue

                max_val = max(max_val, target_value)
                min_val = min(min_val, target_value)

                max_val_ = max(max_val_, target_value)
                min_val_ = min(min_val_, target_value)

            item_names = ITEM_NAMES_IN_RDC_LOOP[file_type]
            combination_id_name = item_names['combination_id']
            chain_id_1_name = item_names['chain_id_1']
            seq_id_1_name = item_names['seq_id_1']
            comp_id_1_name = item_names['comp_id_1']
            atom_id_1_name = item_names['atom_id_1']
            atom_id_2_name = item_names['atom_id_2']
            weight_name = WEIGHT_TAGS[file_type][content_subtype]
            id_tag = CONSIST_ID_TAGS[file_type][content_subtype]

            def ext_atom_names(row):
                return (row[chain_id_1_name], row[seq_id_1_name],
                        row[atom_id_1_name], row[atom_id_2_name])

            count, comb_count, inco_count, redu_count, weights, potential_types =\
                {}, {}, {}, {}, {}, {}

            set_id = set()

            value_per_residue = []

            poly_seq = input_source_dic['polymer_sequence']

            if poly_seq is not None:

                for ps in poly_seq:
                    struct_conf = self._extractCoordStructConf(ps['chain_id'], ps['seq_id'])
                    value_per_residue.append({'chain_id': ps['chain_id'], 'seq_id': ps['seq_id'], 'comp_id': ps['comp_id'],
                                              'struct_conf': struct_conf})

            for row in lp_data:
                index = row.get(index_tag)
                combination_id = row.get(combination_id_name)

                chain_id_1, seq_id_1, atom_id_1, atom_id_2 = ext_atom_names(row)

                weight = row.get(weight_name)
                set_id.add(row[id_tag])

                data_type = self._getTypeOfRdcRestraint(atom_id_1, atom_id_2)

                if data_type in count:
                    count[data_type] += 1
                else:
                    count[data_type] = 1

                if (combination_id is not None) and (combination_id not in EMPTY_VALUE):
                    if data_type in comb_count:
                        comb_count[data_type] += 1
                    else:
                        comb_count[data_type] = 1

                if index is not None:

                    if index in inconsistent:
                        if data_type in inco_count:
                            inco_count[data_type] += 1
                        else:
                            inco_count[data_type] = 1

                    if index in redundant:
                        if data_type in redu_count:
                            redu_count[data_type] += 1
                        else:
                            redu_count[data_type] = 1

                # detect weight

                if weight is not None:
                    if data_type not in weights:
                        weights[data_type] = []
                    weights[data_type].append(weight)

                # detect potential type

                targe_value = row.get(target_value_name)
                lower_limit = row.get(lower_limit_name)
                upper_limit = row.get(upper_limit_name)
                lower_linear_limit = row.get(lower_linear_limit_name)
                upper_linear_limit = row.get(upper_linear_limit_name)

                if (lower_limit is not None) and (upper_limit is not None)\
                        and lower_linear_limit is None and upper_linear_limit is None:
                    potential_type = 'square-well-parabolic'
                elif (lower_limit is not None) and (upper_limit is not None)\
                        and (lower_linear_limit is not None) and (upper_linear_limit is not None):
                    potential_type = 'square-well-parabolic-linear'
                elif lower_limit is None and (upper_limit is not None)\
                        and lower_linear_limit is None and upper_linear_limit is None:
                    potential_type = 'upper-bound-parabolic'
                elif (lower_limit is not None) and upper_limit is None\
                        and lower_linear_limit is None and upper_linear_limit is None:
                    potential_type = 'lower-bound-parabolic'
                elif lower_limit is None and (upper_limit is not None)\
                        and lower_linear_limit is None and (upper_linear_limit is not None):
                    potential_type = 'upper-bound-parabolic-linear'
                elif (lower_limit is not None) and upper_limit is None\
                        and (lower_linear_limit is not None) and upper_linear_limit is None:
                    potential_type = 'lower-bound-parabolic-linear'
                elif (target_value is not None) and lower_limit is None and upper_limit is None\
                        and lower_linear_limit is None and upper_linear_limit is None:
                    potential_type = 'parabolic'
                else:
                    potential_type = 'undefined'

                if potential_type is not None:
                    if data_type not in potential_types:
                        potential_types[data_type] = []
                    potential_types[data_type].append(potential_type)

                if poly_seq is not None:

                    # value per residue

                    for c in value_per_residue:
                        if data_type not in c:
                            c[data_type] = [None] * len(c['seq_id'])
                        if c['chain_id'] == chain_id_1 and targe_value is not None and seq_id_1 in c['seq_id']:
                            b = c['seq_id'].index(seq_id_1)
                            if c[data_type][b] is None:
                                c[data_type][b] = float(targe_value)
                            else:
                                j = 2
                                while True:
                                    _data_type = f'{data_type}_{j}'
                                    if _data_type not in c:
                                        c[_data_type] = [None] * len(c['seq_id'])
                                    if c[_data_type][b] is None:
                                        c[_data_type][b] = float(target_value)
                                        break
                                    j += 1

            if len(count) == 0:
                return

            ent['number_of_constraints'] = count
            ent['number_of_constraint_sets'] = len(set_id)
            if len(comb_count) > 0:
                ent['number_of_combined_constraints'] = comb_count
            if len(inco_count) > 0:
                ent['number_of_inconsistent_constraints'] = inco_count
            if len(redu_count) > 0:
                ent['number_of_redundant_constraints'] = redu_count
            if poly_seq is not None:
                ent['constraints_per_residue'] = value_per_residue
            ent['range'] = {'max_value': round(max_val_, 2), 'min_value': round(min_val_, 2)}
            if len(weights) > 0:
                _weights = {}
                for k, v in weights.items():
                    _weights[k] = collections.Counter(v).most_common()
                ent['weight_of_constraints'] = _weights
            if len(potential_types) > 0:
                _potential_types = {}
                for k, v in potential_types.items():
                    _potential_types[k] = collections.Counter(v).most_common()
                ent['potential_type_of_constraints'] = _potential_types

            target_scale = (max_val - min_val) / 12.0

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
                    _count[k] = 0

                for row in lp_data:
                    target_value = get_est_target_value(row)

                    if targe_value is None or target_value < v or target_value >= v + scale:
                        continue

                    atom_id_1 = row[atom_id_1_name]
                    atom_id_2 = row[atom_id_2_name]

                    data_type = self._getTypeOfRdcRestraint(atom_id_1, atom_id_2)

                    if data_type in _count:
                        _count[data_type] += 1
                    else:
                        _count[data_type] = 1

                range_of_vals.append(v)
                count_of_vals.append(_count)

                v += scale

            transposed = {}

            for k in count:
                transposed[k] = []

                for count_of_val in count_of_vals:
                    transposed[k].append(count_of_val[k])

            if len(range_of_vals) > 1:
                ent['histogram'] = {'range_of_values': range_of_vals, 'number_of_values': transposed}

            if conflict_id_set is not None:

                max_inclusive = RDC_UNCERT_MAX

                max_val = min_val = 0.0

                rdc_ann = []

                for id_set in conflict_id_set:
                    len_id_set = len(id_set)

                    if len_id_set < 2:
                        continue

                    for i in range(len_id_set - 1):

                        for j in range(i + 1, len_id_set):
                            row_1 = lp_data[id_set[i]]
                            row_2 = lp_data[id_set[j]]

                            target_value_1 = get_est_target_value(row_1)
                            target_value_2 = get_est_target_value(row_2)

                            if None in (target_value_1, target_value_2):
                                continue

                            if target_value_1 == target_value_2:
                                continue

                            discrepancy = abs(target_value_1 - target_value_2)

                            max_val = max(max_val, discrepancy)

                            if discrepancy > max_inclusive * INCONSIST_OVER_CONFLICTED:
                                ann = {}
                                ann['level'] = 'conflicted' if discrepancy > max_inclusive else 'inconsistent'
                                ann['chain_id'] = row_1[chain_id_1_name]
                                ann['seq_id'] = row_1[seq_id_1_name]
                                ann['comp_id'] = row_1[comp_id_1_name]
                                ann['atom_id_1'] = row_1[atom_id_1_name]
                                ann['atom_id_2'] = row_1[atom_id_2_name]
                                ann['discrepancy'] = round(discrepancy, 1)

                                rdc_ann.append(ann)

                if max_val > 0.0:
                    target_scale = (max_val - min_val) / 10.0

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
                            _count[k] = 0

                        for id_set in conflict_id_set:
                            len_id_set = len(id_set)

                            if len_id_set < 2:
                                continue

                            redundant = True

                            for i in range(len_id_set - 1):

                                for j in range(i + 1, len_id_set):
                                    row_1 = lp_data[id_set[i]]
                                    row_2 = lp_data[id_set[j]]

                                    target_value_1 = get_est_target_value(row_1)
                                    target_value_2 = get_est_target_value(row_2)

                                    if target_value_1 is None and target_value_2 is None:
                                        continue

                                    if None in (target_value_1, target_value_2):
                                        redundant = False
                                        continue

                                    if target_value_1 == target_value_2:
                                        continue

                                    redundant = False

                                    discrepancy = abs(target_value_1 - target_value_2)

                                    if discrepancy < v or discrepancy >= v + scale:
                                        continue

                                    atom_id_1 = row_1[atom_id_1_name]
                                    atom_id_2 = row_1[atom_id_2_name]

                                    data_type = self._getTypeOfRdcRestraint(atom_id_1, atom_id_2)

                                    _count[data_type] += 1

                            if 0.0 <= v < scale and redundant:

                                atom_id_1 = row_1[atom_id_1_name]
                                atom_id_2 = row_1[atom_id_2_name]

                                data_type = self._getTypeOfRdcRestraint(atom_id_1, atom_id_2)

                                _count[data_type] += 1

                        range_of_vals.append(v)
                        count_of_vals.append(_count)

                        v += scale

                    transposed = {}

                    for k in count:
                        transposed[k] = []

                        for count_of_val in count_of_vals:
                            transposed[k].append(count_of_val[k])

                    if len(range_of_vals) > 1:
                        ent['histogram_of_discrepancy'] = {'range_of_values': range_of_vals,
                                                           'number_of_values': transposed,
                                                           'annotations': rdc_ann}

            if file_type == 'nmr-star' and self._reg.star_data_type[file_list_id] == 'Entry':
                lp_category = LP_CATEGORIES[file_type][content_subtype]
                sf = self._reg.star_data[file_list_id].get_saveframe_by_name(sf_framecode)
                lp = next(lp for lp in sf.loops if lp.category == lp_category)

                ent['atom_name_mapping'] = get_atom_name_mapping(lp, [['Comp_ID_1', 'Atom_ID_1', 'Auth_atom_name_1'],
                                                                      ['Comp_ID_2', 'Atom_ID_2', 'Auth_atom_name_2']])

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.__calculateStatsOfRdcRestraint() "
                                                     "++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfRdcRestraint() ++ Error  - {str(e)}\n")

    def _getTypeOfRdcRestraint(self, atom_id_1: str, atom_id_2: str) -> str:  # pylint: disable=no-self-use
        """ Return type of RDC restraint.
        """

        try:
            iso_number_1 = ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS[atom_id_1[0]][0]
            iso_number_2 = ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS[atom_id_2[0]][0]
        except KeyError:
            pass

        if iso_number_1 < iso_number_2:
            vector_type = f'{atom_id_1}-{atom_id_2}'
        elif iso_number_2 < iso_number_1:
            vector_type = f'{atom_id_2}-{atom_id_1}'
        else:
            sorted_atom_ids = sorted([atom_id_1, atom_id_2])
            vector_type = f'{sorted_atom_ids[0]}-{sorted_atom_ids[1]}'

        return f'{vector_type}_bond_vectors'

    def _calculateStatsOfSpectralPeak(self, file_list_id: int, sf_framecode: str,
                                      num_dim: int, lp_data: Optional[List[dict]], ent: dict) -> None:
        """ Calculate statistics of spectral peaks.
        """

        input_source = self._reg.report.input_sources[file_list_id]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        content_subtype = 'spectral_peak'

        max_dim = num_dim + 1

        item_names = []
        for dim in range(1, max_dim):
            _d = {}
            for k, v in ITEM_NAMES_IN_PK_LOOP[file_type].items():
                if '%s' in v:
                    v = v % dim
                _d[k] = v
            item_names.append(_d)

        chain_id_names, seq_id_names, comp_id_names, atom_id_names = [], [], [], []

        try:

            ent['number_of_spectral_dimensions'] = num_dim
            ent['spectral_dim'] = []
            ent['spectral_dim_transfer'] = []

            aux_data = next((lp['data'] for lp in self._reg.aux_data[content_subtype]
                             if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode
                             and lp['category'] == AUX_LP_CATEGORIES[file_type][content_subtype][1]), None)

            mag_link = []

            if aux_data is not None:
                for sp_dim_trans in aux_data:
                    if file_type == 'nef':
                        if sp_dim_trans['transfer_type'] == 'onebond':
                            # or sp_dim_trans['transfer_type'].startswith('j')
                            # or sp_dim_trans['transfer_type'].startswith('relayed'):
                            dim_1 = sp_dim_trans['dimension_1']
                            dim_2 = sp_dim_trans['dimension_2']
                            mag_link.append((dim_1, dim_2))
                        ent['spectral_dim_transfer'].append({'id_1': sp_dim_trans['dimension_1'],
                                                             'id_2': sp_dim_trans['dimension_2'],
                                                             'indirect': sp_dim_trans.get('is_indirect'),
                                                             'type': sp_dim_trans.get('transfer_type')})
                    else:
                        if sp_dim_trans['Type'] == 'onebond':
                            # or sp_dim_trans['Type'].startswith('j') or sp_dim_trans['Type'].startswith('relayed'):
                            dim_1 = sp_dim_trans['Spectral_dim_ID_1']
                            dim_2 = sp_dim_trans['Spectral_dim_ID_2']
                            mag_link.append((dim_1, dim_2))
                        ent['spectral_dim_transfer'].append({'id_1': sp_dim_trans['Spectral_dim_ID_1'],
                                                             'id_2': sp_dim_trans['Spectral_dim_ID_2'],
                                                             'indirect': sp_dim_trans.get('Indirect'),
                                                             'type': sp_dim_trans.get('Type')})

            aux_data = next((lp['data'] for lp in self._reg.aux_data[content_subtype]
                             if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode
                             and lp['category'] == AUX_LP_CATEGORIES[file_type][content_subtype][0]), None)

            if aux_data is not None:
                for i in range(1, max_dim):
                    for sp_dim in aux_data:
                        sp_freq = center_point = under_sampling_type = encoding_code = encoded_src_dim_id = mag_link_id = None
                        if file_type == 'nef':
                            if sp_dim['dimension_id'] != i:
                                continue
                            axis_code = sp_dim['axis_code']
                            atom_type = ''.join(j for j in axis_code if not j.isdigit())
                            atom_isotope_number = int(''.join(j for j in axis_code if j.isdigit()))
                            axis_unit = 'Hz' if 'axis_unit' not in sp_dim else sp_dim['axis_unit']
                            first_point = sp_dim.get('value_first_point')
                            sp_width = sp_dim.get('spectral_width')
                            if 'spectrometer_frequency' in sp_dim:
                                sp_freq = sp_dim['spectrometer_frequency']
                            if 'folding' in sp_dim:
                                under_sampling_type = sp_dim['folding']
                        else:
                            if sp_dim['ID'] != i:
                                continue
                            axis_code = sp_dim['Axis_code']
                            atom_type = sp_dim.get('Atom_type')
                            if atom_type in EMPTY_VALUE:
                                atom_type = ''.join(j for j in axis_code if not j.isdigit())
                            atom_isotope_number = sp_dim.get('Atom_isotope_number')
                            if atom_isotope_number in EMPTY_VALUE:
                                if atom_type not in EMPTY_VALUE and atom_type[0] in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS:
                                    atom_isotope_number = ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS[atom_type[0]][0]
                                else:
                                    try:
                                        atom_isotope_number = int(''.join(j for j in axis_code if j.isdigit()))
                                    except ValueError:
                                        pass
                            axis_unit = 'Hz' if 'Sweep_width_units' not in sp_dim else sp_dim['Sweep_width_units']
                            first_point = sp_dim.get('Value_first_point')
                            sp_width = sp_dim.get('Sweep_width')
                            if 'Spectrometer_frequency' in sp_dim:
                                sp_freq = sp_dim['Spectrometer_frequency']
                            if 'Under_sampling_type' in sp_dim:
                                under_sampling_type = sp_dim['Under_sampling_type']
                            if 'Center_frequency_offset' in sp_dim:
                                center_point = sp_dim['Center_frequency_offset']
                                if center_point in EMPTY_VALUE:
                                    center_point = None
                            if 'Encoding_code' in sp_dim:
                                encoding_code = sp_dim['Encoding_code']
                                if encoding_code in EMPTY_VALUE:
                                    encoding_code = None
                            if 'Encoded_reduced_dimension_ID' in sp_dim:
                                encoded_src_dim_id = sp_dim['Encoded_reduced_dimension_ID']
                                if encoded_src_dim_id in EMPTY_VALUE:
                                    encoded_src_dim_id = None
                            if 'Magnetization_linkage_ID' in sp_dim:
                                mag_link_id = sp_dim['Magnetization_linkage_ID']
                                if mag_link_id in EMPTY_VALUE:
                                    mag_link_id = None

                        if sp_freq is not None and sp_freq in EMPTY_VALUE:
                            sp_freq = None

                        if center_point is None:
                            center_point = None if None in (first_point, sp_width) else (first_point - sp_width / 2.0)

                        if under_sampling_type is not None and under_sampling_type in EMPTY_VALUE:
                            under_sampling_type = None

                        if under_sampling_type is not None and under_sampling_type in ('circular', 'mirror', 'none', 'fold'):
                            if under_sampling_type in ('circular', 'fold'):
                                under_sampling_type = 'folded'
                            elif under_sampling_type == 'mirror':
                                under_sampling_type = 'aliased'
                            else:
                                under_sampling_type = 'not observed'

                        if mag_link_id is None:
                            for pair in mag_link:
                                if i in (pair[0], pair[1]):
                                    mag_link_id = mag_link.index(pair) + 1
                                    break

                        spectral_dim = {'id': i, 'atom_type': atom_type, 'atom_isotope_number': atom_isotope_number,
                                        'sweep_width': copy.copy(sp_width), 'sweep_width_units': axis_unit,
                                        'center_frequency_offset': None if center_point is None else round(center_point, 8),
                                        'under_sampling_type': under_sampling_type, 'encoding_code': encoding_code,
                                        'encoded_source_dimension_id': encoded_src_dim_id, 'magnetization_linkage_id': mag_link_id}

                        if axis_unit == 'Hz' and None not in (sp_freq, first_point, center_point, sp_width):
                            first_point /= sp_freq
                            center_point /= sp_freq
                            sp_width /= sp_freq

                        last_point = None if None in (first_point, sp_width) else (first_point - sp_width)

                        if None in (center_point, last_point):
                            spectral_region = atom_type
                        elif atom_type == 'H':
                            if mag_link_id is None:
                                spectral_region = 'H'
                            else:
                                dim_1, dim_2 = mag_link[mag_link_id - 1]
                                hvy_dim = dim_1 if i == dim_2 else dim_2

                                for _sp_dim in aux_data:
                                    if file_type == 'nef':
                                        if _sp_dim['dimension_id'] != hvy_dim:
                                            continue
                                        _axis_code = _sp_dim['axis_code']
                                        _atom_type = ''.join(j for j in _axis_code if not j.isdigit())
                                    else:
                                        if _sp_dim['ID'] != hvy_dim:
                                            continue
                                        _axis_code = _sp_dim['Axis_code']
                                        _atom_type = _sp_dim.get('Atom_type')
                                        if _atom_type in EMPTY_VALUE:
                                            _atom_type = ''.join(j for j in _axis_code if not j.isdigit())

                                    if _atom_type == 'C':
                                        _center_point = None
                                        if file_type == 'nef':
                                            _axis_unit = _sp_dim.get('axis_unit', 'Hz')
                                            _first_point = _sp_dim.get('value_first_point')
                                            _sp_width = None if 'axis_unit' not in _sp_dim else _sp_dim.get('spectral_width')
                                            if 'spectrometer_frequency' in _sp_dim:
                                                _sp_freq = _sp_dim['spectrometer_frequency']
                                        else:
                                            _axis_unit = _sp_dim.get('Sweep_width_units', 'Hz')
                                            _first_point = _sp_dim.get('Value_first_point')
                                            _sp_width = None if 'Sweep_width_units' not in _sp_dim else _sp_dim.get('Sweep_width')
                                            if 'Spectrometer_frequency' in _sp_dim:
                                                _sp_freq = _sp_dim['Spectrometer_frequency']
                                            if 'Center_frequency_offset' in _sp_dim:
                                                _center_point = _sp_dim['Center_frequency_offset']
                                                if _center_point in EMPTY_VALUE:
                                                    _center_point = None

                                        if _sp_freq is not None and _sp_freq in EMPTY_VALUE:
                                            _sp_freq = None

                                        if _center_point is None:
                                            _center_point = None if None in (_first_point, _sp_width)\
                                                else (_first_point - _sp_width / 2.0)

                                        if _axis_unit == 'Hz' and None not in (_sp_freq, _first_point, _center_point, _sp_width):
                                            _first_point /= _sp_freq
                                            _center_point /= _sp_freq
                                            _sp_width /= _sp_freq

                                        _last_point = None if None in (_first_point, _sp_width) else (_first_point - _sp_width)

                                        if None in (_center_point, _last_point):
                                            spectral_region = 'H'
                                        elif C_AROMATIC_CENTER_MIN_TOR < _center_point <= C_AROMATIC_CENTER_MAX\
                                                and _sp_width < 60.0:
                                            spectral_region = 'H-aromatic'
                                        elif C_METHYL_CENTER_MIN < _center_point <= C_METHYL_CENTER_MAX\
                                                and _sp_width < 30.0:
                                            spectral_region = 'H-methyl'
                                        elif C_ALIPHATIC_CENTER_MIN < _center_point <= C_ALIPHATIC_CENTER_MAX\
                                                and _sp_width < 90.0:
                                            spectral_region = 'H-aliphatic'
                                        else:
                                            spectral_region = 'H'

                                    elif _atom_type == 'N':
                                        spectral_region = 'HN'
                                    else:
                                        spectral_region = 'H'
                                    break
                        elif atom_type == 'C':
                            if mag_link_id is None and C_CARBONYL_CENTER_MIN <= center_point <= C_CARBONYL_CENTER_MAX:
                                spectral_region = 'CO'
                            elif C_AROMATIC_CENTER_MIN_TOR < center_point <= C_AROMATIC_CENTER_MAX and sp_width < 60.0:
                                spectral_region = 'C-aromatic'
                            elif C_METHYL_CENTER_MIN < center_point <= C_METHYL_CENTER_MAX and sp_width < 30.0:
                                spectral_region = 'C-methyl'
                            elif C_ALIPHATIC_CENTER_MIN < center_point <= C_ALIPHATIC_CENTER_MAX and sp_width < 90.0:
                                spectral_region = 'C-aliphatic'
                            else:
                                spectral_region = 'C'
                        else:
                            spectral_region = atom_type

                        spectral_dim['spectral_region'] = spectral_region

                        ent['spectral_dim'].append(spectral_dim)

                        break

            if lp_data is not None:

                count = {'assigned_spectral_peaks': 0, 'unassigned_spectral_peaks': 0}

                for j in range(num_dim):
                    chain_id_names.append(item_names[j]['chain_id'])
                    seq_id_names.append(item_names[j]['seq_id'])
                    comp_id_names.append(item_names[j]['comp_id'])
                    atom_id_names.append(item_names[j]['atom_id'])

                for row in lp_data:

                    has_assignment = True

                    for j in range(num_dim):

                        if not (chain_id_names[j] in row and seq_id_names[j] in row
                                and comp_id_names[j] in row and atom_id_names[j] in row):
                            has_assignment = False
                            break

                        chain_id = row[chain_id_names[j]]
                        seq_id = row[seq_id_names[j]]
                        comp_id = row[comp_id_names[j]]
                        atom_id = row[atom_id_names[j]]

                        if chain_id in EMPTY_VALUE or seq_id in EMPTY_VALUE or comp_id in EMPTY_VALUE or atom_id in EMPTY_VALUE:
                            has_assignment = False
                            break

                    if has_assignment:
                        count['assigned_spectral_peaks'] += 1
                    else:
                        count['unassigned_spectral_peaks'] += 1

                ent['number_of_spectral_peaks'] = count

            if file_type == 'nmr-star' and self._reg.star_data_type[file_list_id] == 'Entry':
                lp_category = LP_CATEGORIES[file_type][content_subtype]
                sf = self._reg.star_data[file_list_id].get_saveframe_by_name(sf_framecode)

                try:

                    lp = next(lp for lp in sf.loops if lp.category == lp_category)

                    list_of_tags = []
                    for dim in range(1, max_dim):
                        list_of_tags.append([f'Comp_ID_{dim}', f'Atom_ID_{dim}', f'Auth_atom_ID_{dim}'])

                    ent['atom_name_mapping'] = get_atom_name_mapping(lp, list_of_tags)

                except StopIteration:

                    lp_category = '_Assigned_peak_chem_shift'
                    lp = next((lp for lp in sf.loops if lp.category == lp_category), None)

                    if lp is not None:
                        ent['atom_name_mapping'] = get_atom_name_mapping(lp, [['Comp_ID', 'Atom_ID', 'Auth_atom_ID']])

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.__calculateStatsOfSpectralPeak() "
                                                     "++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfSpectralPeak() ++ Error  - {str(e)}\n")

    def _calculateStatsOfSpectralPeakAlt(self, file_list_id: int, sf_framecode: str, num_dim: int, lp_data: List[dict], ent: dict
                                         ) -> None:
        """ Calculate statistics of spectral peaks.
        """

        input_source = self._reg.report.input_sources[file_list_id]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        if file_type == 'nef':
            return

        content_subtype = 'spectral_peak_alt'

        max_dim = num_dim + 1

        item_names = ITEM_NAMES_IN_CS_LOOP[file_type]
        chain_id_name = item_names['chain_id']
        seq_id_name = item_names['seq_id']
        comp_id_name = item_names['comp_id']
        atom_id_name = item_names['atom_id']

        try:

            ent['number_of_spectral_dimensions'] = num_dim
            ent['spectral_dim'] = []
            ent['spectral_dim_transfer'] = []

            aux_data = next((lp['data'] for lp in self._reg.aux_data[content_subtype]
                             if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode
                             and lp['category'] == AUX_LP_CATEGORIES[file_type][content_subtype][1]), None)

            mag_link = []

            if aux_data is not None:
                for sp_dim_trans in aux_data:
                    if sp_dim_trans['Type'] == 'onebond':
                        # or sp_dim_trans['Type'].startswith('j') or sp_dim_trans['Type'].startswith('relayed'):
                        dim_1 = sp_dim_trans['Spectral_dim_ID_1']
                        dim_2 = sp_dim_trans['Spectral_dim_ID_2']
                        mag_link.append((dim_1, dim_2))
                    ent['spectral_dim_transfer'].append({'id_1': sp_dim_trans['Spectral_dim_ID_1'],
                                                         'id_2': sp_dim_trans['Spectral_dim_ID_2'],
                                                         'indirect': sp_dim_trans.get('Indirect'),
                                                         'type': sp_dim_trans.get('Type')})

            aux_data = next((lp['data'] for lp in self._reg.aux_data[content_subtype]
                             if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode
                             and lp['category'] == AUX_LP_CATEGORIES[file_type][content_subtype][0]), None)

            if aux_data is not None:
                for i in range(1, max_dim):
                    for sp_dim in aux_data:
                        sp_freq = center_point = under_sampling_type = encoding_code = encoded_src_dim_id = mag_link_id = None
                        if sp_dim['ID'] != i:
                            continue
                        axis_code = sp_dim['Axis_code']
                        atom_type = sp_dim.get('Atom_type')
                        if atom_type in EMPTY_VALUE:
                            atom_type = ''.join(j for j in axis_code if not j.isdigit())
                        atom_isotope_number = sp_dim.get('Atom_isotope_number')
                        if atom_isotope_number in EMPTY_VALUE:
                            if atom_type not in EMPTY_VALUE and atom_type[0] in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS:
                                atom_isotope_number = ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS[atom_type[0]][0]
                            else:
                                try:
                                    atom_isotope_number = int(''.join(j for j in axis_code if j.isdigit()))
                                except ValueError:
                                    pass
                        axis_unit = 'Hz' if 'Sweep_width_units' not in sp_dim else sp_dim['Sweep_width_units']
                        first_point = sp_dim.get('Value_first_point')
                        sp_width = sp_dim.get('Sweep_width')
                        if 'Spectrometer_frequency' in sp_dim:
                            sp_freq = sp_dim['Spectrometer_frequency']
                        if 'Under_sampling_type' in sp_dim:
                            under_sampling_type = sp_dim['Under_sampling_type']
                        if 'Center_frequency_offset' in sp_dim:
                            center_point = sp_dim['Center_frequency_offset']
                            if center_point in EMPTY_VALUE:
                                center_point = None
                        if 'Encoding_code' in sp_dim:
                            encoding_code = sp_dim['Encoding_code']
                            if encoding_code in EMPTY_VALUE:
                                encoding_code = None
                        if 'Encoded_reduced_dimension_ID' in sp_dim:
                            encoded_src_dim_id = sp_dim['Encoded_reduced_dimension_ID']
                            if encoded_src_dim_id in EMPTY_VALUE:
                                encoded_src_dim_id = None
                        if 'Magnetization_linkage_ID' in sp_dim:
                            mag_link_id = sp_dim['Magnetization_linkage_ID']
                            if mag_link_id in EMPTY_VALUE:
                                mag_link_id = None

                        if sp_freq is not None and sp_freq in EMPTY_VALUE:
                            sp_freq = None

                        if center_point is None:
                            center_point = None if None in (first_point, sp_width) else (first_point - sp_width / 2.0)

                        if under_sampling_type is not None and under_sampling_type in EMPTY_VALUE:
                            under_sampling_type = None

                        if under_sampling_type is not None and under_sampling_type in ('circular', 'mirror', 'none', 'fold'):
                            if under_sampling_type in ('circular', 'fold'):
                                under_sampling_type = 'folded'
                            elif under_sampling_type == 'mirror':
                                under_sampling_type = 'aliased'
                            else:
                                under_sampling_type = 'not observed'

                        if mag_link_id is None:
                            for pair in mag_link:
                                if i in (pair[0], pair[1]):
                                    mag_link_id = mag_link.index(pair) + 1
                                    break

                        spectral_dim = {'id': i, 'atom_type': atom_type, 'atom_isotope_number': atom_isotope_number,
                                        'sweep_width': copy.copy(sp_width), 'sweep_width_units': axis_unit,
                                        'center_frequency_offset': None if center_point is None else round(center_point, 8),
                                        'under_sampling_type': under_sampling_type, 'encoding_code': encoding_code,
                                        'encoded_source_dimension_id': encoded_src_dim_id, 'magnetization_linkage_id': mag_link_id}

                        if axis_unit == 'Hz' and None not in (sp_freq, first_point, center_point, sp_width):
                            first_point /= sp_freq
                            center_point /= sp_freq
                            sp_width /= sp_freq

                        last_point = None if None in (first_point, sp_width) else (first_point - sp_width)

                        if None in (center_point, last_point):
                            spectral_region = atom_type
                        elif atom_type == 'H':
                            if mag_link_id is None:
                                spectral_region = 'H'
                            else:
                                dim_1, dim_2 = mag_link[mag_link_id - 1]
                                hvy_dim = dim_1 if i == dim_2 else dim_2

                                for _sp_dim in aux_data:
                                    if _sp_dim['ID'] != hvy_dim:
                                        continue
                                    _axis_code = _sp_dim['Axis_code']
                                    _atom_type = _sp_dim.get('Atom_type')
                                    if _atom_type in EMPTY_VALUE:
                                        _atom_type = ''.join(j for j in _axis_code if not j.isdigit())

                                    if _atom_type == 'C':
                                        _center_point = None
                                        _axis_unit = _sp_dim.get('Sweep_width_units', 'Hz')
                                        _first_point = _sp_dim.get('Value_first_point')
                                        _sp_width = None if 'Sweep_width_units' not in _sp_dim else _sp_dim.get('Sweep_width')
                                        if 'Spectrometer_frequency' in _sp_dim:
                                            _sp_freq = _sp_dim['Spectrometer_frequency']
                                        if 'Center_frequency_offset' in _sp_dim:
                                            _center_point = _sp_dim['Center_frequency_offset']
                                            if _center_point in EMPTY_VALUE:
                                                _center_point = None

                                        if _sp_freq is not None and _sp_freq in EMPTY_VALUE:
                                            _sp_freq = None

                                        if _center_point is None:
                                            _center_point = None if None in (_first_point, _sp_width)\
                                                else (_first_point - _sp_width / 2.0)

                                        if _axis_unit == 'Hz' and None not in (_sp_freq, _first_point, _center_point, _sp_width):
                                            _first_point /= _sp_freq
                                            _center_point /= _sp_freq
                                            _sp_width /= _sp_freq

                                        _last_point = None if None in (_first_point, _sp_width) else (_first_point - _sp_width)

                                        if None in (_center_point, _last_point):
                                            spectral_region = 'H'
                                        elif C_AROMATIC_CENTER_MIN_TOR < _center_point <= C_AROMATIC_CENTER_MAX\
                                                and _sp_width < 60.0:
                                            spectral_region = 'H-aromatic'
                                        elif C_METHYL_CENTER_MIN < _center_point <= C_METHYL_CENTER_MAX\
                                                and _sp_width < 30.0:
                                            spectral_region = 'H-methyl'
                                        elif C_ALIPHATIC_CENTER_MIN < _center_point <= C_ALIPHATIC_CENTER_MAX\
                                                and _sp_width < 90.0:
                                            spectral_region = 'H-aliphatic'
                                        else:
                                            spectral_region = 'H'

                                    elif _atom_type == 'N':
                                        spectral_region = 'HN'
                                    else:
                                        spectral_region = 'H'
                                    break
                        elif atom_type == 'C':
                            if mag_link_id is None and C_CARBONYL_CENTER_MIN <= center_point <= C_CARBONYL_CENTER_MAX:
                                spectral_region = 'CO'
                            elif C_AROMATIC_CENTER_MIN_TOR < center_point <= C_AROMATIC_CENTER_MAX and sp_width < 60.0:
                                spectral_region = 'C-aromatic'
                            elif C_METHYL_CENTER_MIN < center_point <= C_METHYL_CENTER_MAX and sp_width < 30.0:
                                spectral_region = 'C-methyl'
                            elif C_ALIPHATIC_CENTER_MIN < center_point <= C_ALIPHATIC_CENTER_MAX and sp_width < 90.0:
                                spectral_region = 'C-aliphatic'
                            else:
                                spectral_region = 'C'
                        else:
                            spectral_region = atom_type

                        spectral_dim['spectral_region'] = spectral_region

                        ent['spectral_dim'].append(spectral_dim)

                        break

            count = {'assigned_spectral_peaks': 0, 'unassigned_spectral_peaks': 0}

            aux_data = next((lp['data'] for lp in self._reg.aux_data[content_subtype]
                             if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode
                             and lp['category'] == '_Assigned_peak_chem_shift'), None)

            pk_id_name = 'Peak_ID'
            dim_id_name = 'Spectral_dim_ID'

            pk_id_set = set()

            for row in lp_data:

                has_assignment = aux_data is not None

                pk_id = row['ID']

                if pk_id in pk_id_set:
                    continue

                if has_assignment:

                    for j in range(num_dim):

                        try:
                            k = next(k for k in aux_data if k[pk_id_name] == pk_id and int(k[dim_id_name]) - 1 == j)
                        except StopIteration:
                            has_assignment = False
                            break

                        if not (chain_id_name in k and seq_id_name in k and comp_id_name in k and atom_id_name in k):
                            has_assignment = False
                            break

                        chain_id = k[chain_id_name]
                        seq_id = k[seq_id_name]
                        comp_id = k[comp_id_name]
                        atom_id = k[atom_id_name]

                        if chain_id in EMPTY_VALUE or seq_id in EMPTY_VALUE or comp_id in EMPTY_VALUE or atom_id in EMPTY_VALUE:
                            has_assignment = False
                            break

                pk_id_set.add(pk_id)

                if has_assignment:
                    count['assigned_spectral_peaks'] += 1
                else:
                    count['unassigned_spectral_peaks'] += 1

            ent['number_of_spectral_peaks'] = count

            if file_type == 'nmr-star' and self._reg.star_data_type[file_list_id] == 'Entry':
                lp_category = '_Assigned_peak_chem_shift'
                sf = self._reg.star_data[file_list_id].get_saveframe_by_name(sf_framecode)
                lp = next((lp for lp in sf.loops if lp.category == lp_category), None)

                if lp is not None:
                    ent['atom_name_mapping'] = get_atom_name_mapping(lp, [['Comp_ID', 'Atom_ID', 'Auth_atom_ID']])

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.__calculateStatsOfSpectralPeakAlt() "
                                                     "++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.__calculateStatsOfSpectralPeakAlt() "
                                    f"++ Error  - {str(e)}\n")
