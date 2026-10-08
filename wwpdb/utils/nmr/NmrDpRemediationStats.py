##
# File: NmrDpRemediationStats.py
# Date: 17-Aug-2026
#
# Updates:
##
""" Constraint statistics of remediated NMR data.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.2"

import re

import pynmrstar

try:
    from wwpdb.utils.nmr.NmrDpConstant import (NMR_CONTENT_SUBTYPES,
                                               SF_CATEGORIES,
                                               LP_CATEGORIES,
                                               SF_ALLOWED_TAGS,
                                               ITEM_NAMES_IN_DIST_LOOP,
                                               ITEM_NAMES_IN_DIHED_LOOP,
                                               ITEM_NAMES_IN_RDC_LOOP,
                                               EMPTY_VALUE,
                                               PROTON_BEGIN_CODE,
                                               DIST_AMBIG_LOW,
                                               DIST_AMBIG_UP)
    from wwpdb.utils.nmr.CifToNmrStar import (has_key_value,
                                              get_first_sf_tag,
                                              set_sf_tag)
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (isAmbigAtomSelection,
                                                       getRestraintName,
                                                       getPotentialType)
    from wwpdb.utils.nmr.NmrDpRemediationBase import NmrDpRemediationBase
except ImportError:
    from nmr.NmrDpConstant import (NMR_CONTENT_SUBTYPES,
                                   SF_CATEGORIES,
                                   LP_CATEGORIES,
                                   SF_ALLOWED_TAGS,
                                   ITEM_NAMES_IN_DIST_LOOP,
                                   ITEM_NAMES_IN_DIHED_LOOP,
                                   ITEM_NAMES_IN_RDC_LOOP,
                                   EMPTY_VALUE,
                                   PROTON_BEGIN_CODE,
                                   DIST_AMBIG_LOW,
                                   DIST_AMBIG_UP)
    from nmr.CifToNmrStar import (has_key_value,
                                  get_first_sf_tag,
                                  set_sf_tag)
    from nmr.mr.ParserListenerUtil import (isAmbigAtomSelection,
                                           getRestraintName,
                                           getPotentialType)
    from nmr.NmrDpRemediationBase import NmrDpRemediationBase


class NmrDpRemediationStats(NmrDpRemediationBase):
    """ Constraint statistics of remediated NMR data.
    """
    __slots__ = ()

    def updateConstraintStats(self) -> bool:
        """ Update _Constraint_stat_list saveframe.
        """

        if (not self._reg.combined_mode and not self._reg.remediation_mode)\
           or self._reg.dstPath is None\
           or self._reg.release_mode\
           or not self._reg.cifChecked:
            return True

        input_source = self._reg.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        if file_type == 'nef':
            return True

        if len(self._reg.star_data) == 0 or not isinstance(self._reg.star_data[0], pynmrstar.Entry):
            return False

        master_entry = self._reg.star_data[0]

        if 'constraint_statistics' in self._reg.sf_category_list and self._reg.list_id_counter is not None:
            return False

        if self._reg.bmrb_only and self._reg.internal_mode and self._reg.bmrb_id is not None:
            master_entry.entry_id = self._reg.bmrb_id
        else:
            master_entry.entry_id = f'nef_{self._reg.entry_id.lower()}'

        self._reg.c2S.set_entry_id(master_entry, self._reg.entry_id)

        # refresh _Constraint_stat_list saveframe

        sf_framecode = 'constraint_statistics'

        cst_sfs = master_entry.get_saveframes_by_category(sf_framecode)

        if len(cst_sfs) > 0:

            if self._reg.list_id_counter is None:
                master_entry.remove_saveframe(sf_framecode)

            else:

                lp_category = '_Constraint_file'

                key_items = [{'name': 'ID', 'type': 'int'},
                             {'name': 'Constraint_filename', 'type': 'str'},
                             {'name': 'Block_ID', 'type': 'int'},
                             ]
                data_items = [{'name': 'Constraint_type', 'type': 'str', 'mandatory': True},
                              {'name': 'Constraint_subtype', 'type': 'str'},
                              {'name': 'Constraint_subsubtype', 'type': 'str',
                               'enum': ('ambi', 'simple')},
                              {'name': 'Constraint_number', 'type': 'int'},
                              {'name': 'Constraint_stat_list_ID', 'type': 'int', 'mandatory': True,
                               'default': '1', 'default-from': 'parent'},
                              {'name': 'Entry_ID', 'type': 'str', 'mandatory': False}
                              ]

                allowed_tags = ['ID', 'Constraint_filename', 'Software_ID', 'Software_label', 'Software_name',
                                'Block_ID', 'Constraint_type', 'Constraint_subtype', 'Constraint_subsubtype', 'Constraint_number',
                                'Sf_ID', 'Entry_ID', 'Constraint_stat_list_ID']

                try:

                    for parent_pointer, cst_sf in enumerate(cst_sfs, start=1):

                        self._reg.nefT.check_data(cst_sf, lp_category, key_items, data_items,
                                                  allowed_tags, None, parent_pointer=parent_pointer,
                                                  enforce_allowed_tags=(file_type == 'nmr-star'),
                                                  excl_missing_data=self._reg.excl_missing_data)

                    return True

                except Exception:  # pylint: disable=broad-exception-caught
                    for cst_sf in reversed(cst_sfs):
                        del master_entry[cst_sf]

        self._reg.sf_category_list, self._reg.lp_category_list = self._reg.nefT.get_inventory_list(master_entry)

        # initialize loop counter
        lp_counts = {t: 0 for t in NMR_CONTENT_SUBTYPES}

        # increment loop counter of each content subtype
        for lp_category in self._reg.lp_category_list:
            if lp_category in LP_CATEGORIES[file_type].values():
                lp_counts[[k for k, v in LP_CATEGORIES[file_type].items() if v == lp_category][0]] += 1

        content_subtypes = {k: lp_counts[k] for k in lp_counts if lp_counts[k] > 0}

        input_source.setItemValue('content_subtype', content_subtypes)

        sf_item = {}

        cst_sf = pynmrstar.Saveframe.from_scratch(sf_framecode)
        cst_sf.set_tag_prefix('_Constraint_stat_list')
        cst_sf.add_tag('Sf_category', sf_framecode)
        cst_sf.add_tag('Sf_framecode', sf_framecode)
        cst_sf.add_tag('Entry_ID', self._reg.entry_id)
        cst_sf.add_tag('ID', 1)
        if self._reg.srcName is not None:
            cst_sf.add_tag('Data_file_name', self._reg.srcName)

        if has_key_value(input_source_dic, 'content_subtype'):

            for content_subtype in input_source_dic['content_subtype']:

                if content_subtype == 'dist_restraint':

                    sf_category = SF_CATEGORIES[file_type][content_subtype]
                    lp_category = LP_CATEGORIES[file_type][content_subtype]

                    for sf in master_entry.get_saveframes_by_category(sf_category):
                        avr_method = get_first_sf_tag(sf, 'NOE_dist_averaging_method')
                        if len(avr_method) > 0 and avr_method not in EMPTY_VALUE:
                            cst_sf.add_tag('NOE_dist_averaging_method', avr_method)
                            break

                    for sf in master_entry.get_saveframes_by_category(sf_category):
                        sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')
                        if sf_framecode not in sf_item:
                            sf_item[sf_framecode] = {'constraint_type': 'distance', 'constraint_subsubtype': 'simple'}
                            constraint_type = get_first_sf_tag(sf, 'Constraint_type')
                            if len(constraint_type) > 0 and constraint_type not in EMPTY_VALUE:
                                sf_item[sf_framecode]['constraint_subtype'] = constraint_type

                        lp = sf.get_loop(lp_category)

                        item_names = ITEM_NAMES_IN_DIST_LOOP[file_type]
                        id_col = lp.tags.index('ID')
                        member_logic_code_col = lp.tags.index('Member_logic_code') if 'Member_logic_code' in lp.tags else -1
                        auth_asym_id_1_col = lp.tags.index('Auth_asym_ID_1')
                        auth_seq_id_1_col = lp.tags.index('Auth_seq_ID_1')
                        auth_asym_id_2_col = lp.tags.index('Auth_asym_ID_2')
                        auth_seq_id_2_col = lp.tags.index('Auth_seq_ID_2')
                        comp_id_1_col = lp.tags.index(item_names['comp_id_1'])
                        comp_id_2_col = lp.tags.index(item_names['comp_id_2'])
                        atom_id_1_col = lp.tags.index(item_names['atom_id_1'])
                        atom_id_2_col = lp.tags.index(item_names['atom_id_2'])

                        try:
                            target_value_col = lp.tags.index(item_names['target_value'])
                        except ValueError:
                            target_value_col = -1
                        try:
                            lower_limit_col = lp.tags.index(item_names['lower_limit'])
                        except ValueError:
                            lower_limit_col = -1
                        try:
                            upper_limit_col = lp.tags.index(item_names['upper_limit'])
                        except ValueError:
                            upper_limit_col = -1
                        try:
                            lower_linear_limit_col = lp.tags.index(item_names['lower_linear_limit'])
                        except ValueError:
                            lower_linear_limit_col = -1
                        try:
                            upper_linear_limit_col = lp.tags.index(item_names['upper_linear_limit'])
                        except ValueError:
                            upper_linear_limit_col = -1

                        has_or_code = False

                        potential_type = get_first_sf_tag(sf, 'Potential_type')
                        has_potential_type = len(potential_type) > 0 and potential_type not in EMPTY_VALUE\
                            and potential_type != 'unknown'

                        _potential_type = None
                        count = 0

                        prev_id = -1
                        for row in lp:
                            _id = int(row[id_col])
                            if _id == prev_id:
                                if member_logic_code_col != -1 and row[member_logic_code_col] == 'OR':
                                    has_or_code = True
                                continue
                            prev_id = _id
                            count += 1
                            if not has_potential_type:
                                dst_func = {}
                                if target_value_col != -1 and row[target_value_col] not in EMPTY_VALUE:
                                    dst_func['target_value'] = float(row[target_value_col])
                                if lower_limit_col != -1 and row[lower_limit_col] not in EMPTY_VALUE:
                                    dst_func['lower_limit'] = float(row[lower_limit_col])
                                if upper_limit_col != -1 and row[upper_limit_col] not in EMPTY_VALUE:
                                    dst_func['upper_limit'] = float(row[upper_limit_col])
                                if lower_linear_limit_col != -1 and row[lower_linear_limit_col] not in EMPTY_VALUE:
                                    dst_func['lower_linear_limit'] = float(row[lower_linear_limit_col])
                                if upper_linear_limit_col != -1 and row[upper_linear_limit_col] not in EMPTY_VALUE:
                                    dst_func['upper_linear_limit'] = float(row[upper_linear_limit_col])
                                if _potential_type is None:
                                    _potential_type = getPotentialType(file_type, 'dist', dst_func)
                                else:
                                    if getPotentialType(file_type, 'dist', dst_func) != _potential_type:
                                        has_potential_type = True

                        if not has_potential_type and _potential_type is not None:
                            set_sf_tag(sf, 'Potential_type', _potential_type)

                        sf_item[sf_framecode]['id'] = count

                        if has_or_code:

                            def get_auth_seq_id(val):
                                if val in EMPTY_VALUE:
                                    return None
                                if isinstance(val, int):
                                    return val
                                if val.isdigit():
                                    return int(val)
                                return int(re.findall(r'\d+', val)[0])

                            prev_id = -1
                            for row in lp:
                                if member_logic_code_col != -1 and row[member_logic_code_col] == 'OR':
                                    _id = int(row[id_col])
                                    if _id != prev_id:
                                        _atom1 = {'chain_id': row[auth_asym_id_1_col],
                                                  'seq_id': get_auth_seq_id(row[auth_seq_id_1_col]),
                                                  'comp_id': row[comp_id_1_col],
                                                  'atom_id': row[atom_id_1_col]}
                                        _atom2 = {'chain_id': row[auth_asym_id_2_col],
                                                  'seq_id': get_auth_seq_id(row[auth_seq_id_2_col]),
                                                  'comp_id': row[comp_id_2_col],
                                                  'atom_id': row[atom_id_2_col]}
                                        prev_id = _id
                                        continue
                                    atom1 = {'chain_id': row[auth_asym_id_1_col],
                                             'seq_id': get_auth_seq_id(row[auth_seq_id_1_col]),
                                             'comp_id': row[comp_id_1_col],
                                             'atom_id': row[atom_id_1_col]}
                                    atom2 = {'chain_id': row[auth_asym_id_2_col],
                                             'seq_id': get_auth_seq_id(row[auth_seq_id_2_col]),
                                             'comp_id': row[comp_id_2_col],
                                             'atom_id': row[atom_id_2_col]}
                                    if isAmbigAtomSelection([_atom1, atom1], self._reg.csStat)\
                                       or isAmbigAtomSelection([_atom2, atom2], self._reg.csStat):
                                        sf_item[sf_framecode]['constraint_subsubtype'] = 'ambi'
                                        break
                                    _atom1, _atom2 = atom1, atom2

                            if sf_item[sf_framecode]['constraint_subsubtype'] == 'ambi':

                                if 'pre' in sf_framecode or 'paramag' in sf_framecode:
                                    sf_item[sf_framecode]['constraint_subtype'] = 'paramagnetic relaxation'
                                if 'cidnp' in sf_framecode:
                                    sf_item[sf_framecode]['constraint_subtype'] = 'photo cidnp'
                                if 'csp' in sf_framecode or 'perturb' in sf_framecode:
                                    sf_item[sf_framecode]['constraint_subtype'] = 'chemical shift perturbation'
                                if 'mutat' in sf_framecode:
                                    sf_item[sf_framecode]['constraint_subtype'] = 'mutation'
                                if 'protect' in sf_framecode:
                                    sf_item[sf_framecode]['constraint_subtype'] = 'hydrogen exchange protection'
                                if 'symm' in sf_framecode:
                                    sf_item[sf_framecode]['constraint_subtype'] = 'symmetry'

                        if sf_item[sf_framecode]['constraint_subsubtype'] == 'simple':

                            metal_coord = disele_bond = disulf_bond = hydrog_bond = False

                            for row in lp:
                                comp_id_1 = row[comp_id_1_col]
                                comp_id_2 = row[comp_id_2_col]
                                atom_id_1 = row[atom_id_1_col]
                                atom_id_2 = row[atom_id_2_col]

                                if atom_id_1 in EMPTY_VALUE or atom_id_2 in EMPTY_VALUE:
                                    continue

                                atom_id_1_ = atom_id_1[0]
                                atom_id_2_ = atom_id_2[0]
                                if comp_id_1 == atom_id_1 or comp_id_2 == atom_id_2:
                                    metal_coord = True
                                elif 'SE' in (atom_id_1, atom_id_2):
                                    disele_bond = True
                                elif 'SG' in (atom_id_1, atom_id_2):
                                    disulf_bond = True
                                elif (atom_id_1_ == 'F' and atom_id_2_ in PROTON_BEGIN_CODE)\
                                        or (atom_id_2_ == 'F' and atom_id_1_ in PROTON_BEGIN_CODE):
                                    hydrog_bond = True
                                elif (atom_id_1_ == 'F' and atom_id_2_ == 'F') or (atom_id_2_ == 'F' and atom_id_1_ == 'F'):
                                    hydrog_bond = True
                                elif (atom_id_1_ == 'O' and atom_id_2_ in PROTON_BEGIN_CODE)\
                                        or (atom_id_2_ == 'O' and atom_id_1_ in PROTON_BEGIN_CODE):
                                    hydrog_bond = True
                                elif (atom_id_1_ == 'O' and atom_id_2_ == 'N') or (atom_id_2_ == 'O' and atom_id_1_ == 'N'):
                                    hydrog_bond = True
                                elif (atom_id_1_ == 'O' and atom_id_2_ == 'O') or (atom_id_2_ == 'O' and atom_id_1_ == 'O'):
                                    hydrog_bond = True
                                elif (atom_id_1_ == 'N' and atom_id_2_ in PROTON_BEGIN_CODE)\
                                        or (atom_id_2_ == 'N' and atom_id_1_ in PROTON_BEGIN_CODE):
                                    hydrog_bond = True
                                elif (atom_id_1_ == 'N' and atom_id_2_ == 'N') or (atom_id_2_ == 'N' and atom_id_1_ == 'N'):
                                    hydrog_bond = True

                            if not metal_coord and not disele_bond and not disulf_bond and not hydrog_bond:
                                if 'build' in sf_framecode and 'up' in sf_framecode:
                                    if 'roe' in sf_framecode:
                                        sf_item[sf_framecode]['constraint_subtype'] = 'ROE build-up'
                                    else:
                                        sf_item[sf_framecode]['constraint_subtype'] = 'NOE build-up'

                                elif 'not' in sf_framecode and 'seen' in sf_framecode:
                                    sf_item[sf_framecode]['constraint_subtype'] = 'NOE not seen'

                                elif 'roe' in sf_framecode:
                                    sf_item[sf_framecode]['constraint_subtype'] = 'ROE'

                                sf_item[sf_framecode]['constraint_subtype'] = 'NOE'

                            elif metal_coord and not disele_bond and not disulf_bond and not hydrog_bond:
                                sf_item[sf_framecode]['constraint_subtype'] = 'metal coordination'

                            elif not metal_coord and disele_bond and not disulf_bond and not hydrog_bond:
                                sf_item[sf_framecode]['constraint_subtype'] = 'diselenide bond'

                            elif not metal_coord and not disele_bond and disulf_bond and not hydrog_bond:
                                sf_item[sf_framecode]['constraint_subtype'] = 'disulfide bond'

                            elif not metal_coord and not disele_bond and not disulf_bond and hydrog_bond:
                                sf_item[sf_framecode]['constraint_subtype'] = 'hydrogen bond'

                    NOE_tot_num =\
                        NOE_intraresidue_tot_num =\
                        NOE_sequential_tot_num =\
                        NOE_medium_range_tot_num =\
                        NOE_long_range_tot_num =\
                        NOE_unique_tot_num =\
                        NOE_intraresidue_unique_tot_num =\
                        NOE_sequential_unique_tot_num =\
                        NOE_medium_range_unique_tot_num =\
                        NOE_long_range_unique_tot_num =\
                        NOE_unamb_intramol_tot_num =\
                        NOE_unamb_intermol_tot_num =\
                        NOE_ambig_intramol_tot_num =\
                        NOE_ambig_intermol_tot_num =\
                        NOE_interentity_tot_num =\
                        NOE_other_tot_num = 0

                    for sf in master_entry.get_saveframes_by_category(sf_category):
                        sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')
                        potential_type = get_first_sf_tag(sf, 'Potential_type')
                        if 'lower' in potential_type:
                            continue
                        if 'constraint_subtype' in sf_item[sf_framecode] and 'NOE' in sf_item[sf_framecode]['constraint_subtype']:
                            # NOE_tot_num += sf_item[sf_framecode]['id']

                            lp = sf.get_loop(lp_category)

                            item_names = ITEM_NAMES_IN_DIST_LOOP[file_type]
                            id_col = lp.tags.index('ID')
                            chain_id_1_col = lp.tags.index(item_names['chain_id_1'])
                            chain_id_2_col = lp.tags.index(item_names['chain_id_2'])
                            seq_id_1_col = lp.tags.index(item_names['seq_id_1'])
                            seq_id_2_col = lp.tags.index(item_names['seq_id_2'])
                            comp_id_1_col = lp.tags.index(item_names['comp_id_1'])
                            comp_id_2_col = lp.tags.index(item_names['comp_id_2'])
                            atom_id_1_col = lp.tags.index(item_names['atom_id_1'])
                            atom_id_2_col = lp.tags.index(item_names['atom_id_2'])
                            # try:
                            #     member_logic_code_col = lp.tags.index(item_names['member_logic_code'])
                            # except ValueError:
                            #     member_logic_code_col = -1
                            try:
                                combination_id_col = lp.tags.index(item_names['combination_id'])
                            except ValueError:
                                combination_id_col = -1
                            try:
                                upper_limit_col = lp.tags.index(item_names['upper_limit'])
                            except ValueError:
                                upper_limit_col = -1

                            prev_id = -1

                            for row in lp:
                                _id = int(row[id_col])
                                # member_logic_code = row[member_logic_code_col] if member_logic_code_col != -1 else None
                                try:
                                    chain_id_1 = int(row[chain_id_1_col])
                                    chain_id_2 = int(row[chain_id_2_col])
                                    seq_id_1 = int(row[seq_id_1_col])
                                    seq_id_2 = int(row[seq_id_2_col])
                                except (ValueError, TypeError):
                                    continue
                                comp_id_1 = row[comp_id_1_col]
                                comp_id_2 = row[comp_id_2_col]
                                atom_id_1 = row[atom_id_1_col]
                                atom_id_2 = row[atom_id_2_col]

                                if atom_id_1 in EMPTY_VALUE or atom_id_2 in EMPTY_VALUE or _id == prev_id:
                                    continue

                                prev_id = _id

                                combination_id = row[combination_id_col] if combination_id_col != -1 else None
                                upper_limit = float(row[upper_limit_col])\
                                    if upper_limit_col != -1 and row[upper_limit_col] not in EMPTY_VALUE else None

                                offset = abs(seq_id_1 - seq_id_2)
                                ambig = upper_limit is not None and (upper_limit <= DIST_AMBIG_LOW or upper_limit >= DIST_AMBIG_UP)
                                uniq = combination_id in EMPTY_VALUE and not ambig

                                NOE_tot_num += 1

                                if uniq:
                                    NOE_unique_tot_num += 1

                                if chain_id_1 == chain_id_2:
                                    if uniq:
                                        NOE_unamb_intramol_tot_num += 1
                                    else:
                                        NOE_ambig_intramol_tot_num += 1
                                    if offset == 0:
                                        NOE_intraresidue_tot_num += 1
                                        if uniq:
                                            NOE_intraresidue_unique_tot_num += 1
                                    elif offset == 1:
                                        NOE_sequential_tot_num += 1
                                        if uniq:
                                            NOE_sequential_unique_tot_num += 1
                                    elif offset < 5:
                                        NOE_medium_range_tot_num += 1
                                        if uniq:
                                            NOE_medium_range_unique_tot_num += 1
                                    else:
                                        NOE_long_range_tot_num += 1
                                        if uniq:
                                            NOE_long_range_unique_tot_num += 1
                                else:
                                    NOE_interentity_tot_num += 1
                                    if uniq:
                                        NOE_unamb_intermol_tot_num += 1
                                    else:
                                        NOE_ambig_intermol_tot_num += 1

                    for sf in master_entry.get_saveframes_by_category(sf_category):
                        sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')
                        potential_type = get_first_sf_tag(sf, 'Potential_type')
                        if 'lower' in potential_type:
                            continue
                        constraint_type = get_first_sf_tag(sf, 'Constraint_type')
                        if constraint_type in ('paramagnetic relaxation',
                                               'photo cidnp',
                                               'chemical shift perturbation',
                                               'mutation',
                                               'symmetry'):
                            NOE_other_tot_num += sf_item[sf_framecode]['id']

                    if NOE_tot_num > 0:
                        cst_sf.add_tag('NOE_tot_num', NOE_tot_num)
                        cst_sf.add_tag('NOE_intraresidue_tot_num', NOE_intraresidue_tot_num)
                        cst_sf.add_tag('NOE_sequential_tot_num', NOE_sequential_tot_num)
                        cst_sf.add_tag('NOE_medium_range_tot_num', NOE_medium_range_tot_num)
                        cst_sf.add_tag('NOE_long_range_tot_num', NOE_long_range_tot_num)
                        cst_sf.add_tag('NOE_unique_tot_num', NOE_unique_tot_num)
                        cst_sf.add_tag('NOE_intraresidue_unique_tot_num', NOE_intraresidue_unique_tot_num)
                        cst_sf.add_tag('NOE_sequential_unique_tot_num', NOE_sequential_unique_tot_num)
                        cst_sf.add_tag('NOE_medium_range_unique_tot_num', NOE_medium_range_unique_tot_num)
                        cst_sf.add_tag('NOE_long_range_unique_tot_num', NOE_long_range_unique_tot_num)
                        cst_sf.add_tag('NOE_unamb_intramol_tot_num', NOE_unamb_intramol_tot_num)
                        cst_sf.add_tag('NOE_unamb_intermol_tot_num', NOE_unamb_intermol_tot_num)
                        cst_sf.add_tag('NOE_ambig_intramol_tot_num', NOE_ambig_intramol_tot_num)
                        cst_sf.add_tag('NOE_ambig_intermol_tot_num', NOE_ambig_intermol_tot_num)
                        cst_sf.add_tag('NOE_interentity_tot_num', NOE_interentity_tot_num)
                        cst_sf.add_tag('NOE_other_tot_num', NOE_other_tot_num)

                    for sf in master_entry.get_saveframes_by_category(sf_category):
                        avr_method = get_first_sf_tag(sf, 'ROE_dist_averaging_method')
                        if len(avr_method) > 0 or avr_method not in EMPTY_VALUE:
                            cst_sf.add_tag('ROE_dist_averaging_method', avr_method)
                            break

                    ROE_tot_num =\
                        ROE_intraresidue_tot_num =\
                        ROE_sequential_tot_num =\
                        ROE_medium_range_tot_num =\
                        ROE_long_range_tot_num =\
                        ROE_unambig_intramol_tot_num =\
                        ROE_unambig_intermol_tot_num =\
                        ROE_ambig_intramol_tot_num =\
                        ROE_ambig_intermol_tot_num =\
                        ROE_other_tot_num = 0

                    for sf in master_entry.get_saveframes_by_category(sf_category):
                        sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')
                        potential_type = get_first_sf_tag(sf, 'Potential_type')
                        if 'lower' in potential_type:
                            continue
                        if 'constraint_subtype' in sf_item[sf_framecode] and 'ROE' in sf_item[sf_framecode]['constraint_subtype']:
                            # ROE_tot_num += sf_item[sf_framecode]['id']

                            lp = sf.get_loop(lp_category)

                            item_names = ITEM_NAMES_IN_DIST_LOOP[file_type]
                            id_col = lp.tags.index('ID')
                            chain_id_1_col = lp.tags.index(item_names['chain_id_1'])
                            chain_id_2_col = lp.tags.index(item_names['chain_id_2'])
                            seq_id_1_col = lp.tags.index(item_names['seq_id_1'])
                            seq_id_2_col = lp.tags.index(item_names['seq_id_2'])
                            comp_id_1_col = lp.tags.index(item_names['comp_id_1'])
                            comp_id_2_col = lp.tags.index(item_names['comp_id_2'])
                            atom_id_1_col = lp.tags.index(item_names['atom_id_1'])
                            atom_id_2_col = lp.tags.index(item_names['atom_id_2'])
                            # try:
                            #     member_logic_code_col = lp.tags.index(item_names['member_logic_code'])
                            # except ValueError:
                            #     member_logic_code_col = -1
                            try:
                                combination_id_col = lp.tags.index(item_names['combination_id'])
                            except ValueError:
                                combination_id_col = -1
                            try:
                                upper_limit_col = lp.tags.index(item_names['upper_limit'])
                            except ValueError:
                                upper_limit_col = -1

                            prev_id = -1

                            for row in lp:
                                _id = int(row[id_col])
                                # member_logic_code = row[member_logic_code_col] if member_logic_code_col != -1 else None
                                try:
                                    chain_id_1 = int(row[chain_id_1_col])
                                    chain_id_2 = int(row[chain_id_2_col])
                                    seq_id_1 = int(row[seq_id_1_col])
                                    seq_id_2 = int(row[seq_id_2_col])
                                except (ValueError, TypeError):
                                    continue
                                comp_id_1 = row[comp_id_1_col]
                                comp_id_2 = row[comp_id_2_col]
                                atom_id_1 = row[atom_id_1_col]
                                atom_id_2 = row[atom_id_2_col]

                                if atom_id_1 in EMPTY_VALUE or atom_id_2 in EMPTY_VALUE or _id == prev_id:
                                    continue

                                prev_id = _id

                                combination_id = row[combination_id_col] if combination_id_col != -1 else None
                                upper_limit = float(row[upper_limit_col])\
                                    if upper_limit_col != -1 and row[upper_limit_col] not in EMPTY_VALUE else None

                                offset = abs(seq_id_1 - seq_id_2)
                                ambig = upper_limit is not None and (upper_limit <= DIST_AMBIG_LOW or upper_limit >= DIST_AMBIG_UP)
                                uniq = combination_id in EMPTY_VALUE and not ambig

                                ROE_tot_num += 1

                                if chain_id_1 == chain_id_2:
                                    if uniq:
                                        ROE_unambig_intramol_tot_num += 1
                                    else:
                                        ROE_ambig_intramol_tot_num += 1
                                    if offset == 0:
                                        ROE_intraresidue_tot_num += 1
                                    elif offset == 1:
                                        ROE_sequential_tot_num += 1
                                    elif offset < 5:
                                        ROE_medium_range_tot_num += 1
                                    else:
                                        ROE_long_range_tot_num += 1
                                else:
                                    ROE_other_tot_num += 1
                                    if uniq:
                                        ROE_unambig_intermol_tot_num += 1
                                    else:
                                        ROE_ambig_intermol_tot_num += 1

                    if ROE_tot_num > 0:
                        cst_sf.add_tag('ROE_tot_num', ROE_tot_num)
                        cst_sf.add_tag('ROE_intraresidue_tot_num', ROE_intraresidue_tot_num)
                        cst_sf.add_tag('ROE_sequential_tot_num', ROE_sequential_tot_num)
                        cst_sf.add_tag('ROE_medium_range_tot_num', ROE_medium_range_tot_num)
                        cst_sf.add_tag('ROE_long_range_tot_num', ROE_long_range_tot_num)
                        cst_sf.add_tag('ROE_unambig_intramol_tot_num', ROE_unambig_intramol_tot_num)
                        cst_sf.add_tag('ROE_unambig_intermol_tot_num', ROE_unambig_intermol_tot_num)
                        cst_sf.add_tag('ROE_ambig_intramol_tot_num', ROE_ambig_intramol_tot_num)
                        cst_sf.add_tag('ROE_ambig_intermol_tot_num', ROE_ambig_intermol_tot_num)
                        cst_sf.add_tag('ROE_other_tot_num', ROE_other_tot_num)

                elif content_subtype == 'dihed_restraint':

                    sf_category = SF_CATEGORIES[file_type][content_subtype]
                    lp_category = LP_CATEGORIES[file_type][content_subtype]

                    auth_to_entity_type = self._reg.caC['auth_to_entity_type']

                    Dihedral_angle_tot_num = 0
                    for sf in master_entry.get_saveframes_by_category(sf_category):
                        sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')
                        if sf_framecode not in sf_item:
                            sf_item[sf_framecode] = {'constraint_type': 'dihedral angle'}

                        lp = sf.get_loop(lp_category)

                        item_names = ITEM_NAMES_IN_DIHED_LOOP[file_type]
                        id_col = lp.tags.index('ID')
                        try:
                            target_value_col = lp.tags.index(item_names['target_value'])
                        except ValueError:
                            target_value_col = -1
                        try:
                            lower_limit_col = lp.tags.index(item_names['lower_limit'])
                        except ValueError:
                            lower_limit_col = -1
                        try:
                            upper_limit_col = lp.tags.index(item_names['upper_limit'])
                        except ValueError:
                            upper_limit_col = -1
                        try:
                            lower_linear_limit_col = lp.tags.index(item_names['lower_linear_limit'])
                        except ValueError:
                            lower_linear_limit_col = -1
                        try:
                            upper_linear_limit_col = lp.tags.index(item_names['upper_linear_limit'])
                        except ValueError:
                            upper_linear_limit_col = -1

                        potential_type = get_first_sf_tag(sf, 'Potential_type')
                        has_potential_type = len(potential_type) > 0 and potential_type not in EMPTY_VALUE\
                            and potential_type != 'unknown'

                        _potential_type = None
                        count = 0

                        prev_id = -1
                        for row in lp:
                            _id = int(row[id_col])
                            if _id == prev_id:
                                continue
                            prev_id = _id
                            count += 1
                            if not has_potential_type:
                                dst_func = {}
                                if target_value_col != -1 and row[target_value_col] not in EMPTY_VALUE:
                                    dst_func['target_value'] = float(row[target_value_col])
                                if lower_limit_col != -1 and row[lower_limit_col] not in EMPTY_VALUE:
                                    dst_func['lower_limit'] = float(row[lower_limit_col])
                                if upper_limit_col != -1 and row[upper_limit_col] not in EMPTY_VALUE:
                                    dst_func['upper_limit'] = float(row[upper_limit_col])
                                if lower_linear_limit_col != -1 and row[lower_linear_limit_col] not in EMPTY_VALUE:
                                    dst_func['lower_linear_limit'] = float(row[lower_linear_limit_col])
                                if upper_linear_limit_col != -1 and row[upper_linear_limit_col] not in EMPTY_VALUE:
                                    dst_func['upper_linear_limit'] = float(row[upper_linear_limit_col])
                                if _potential_type is None:
                                    _potential_type = getPotentialType(file_type, 'dihed', dst_func)
                                else:
                                    if getPotentialType(file_type, 'dihed', dst_func) != _potential_type:
                                        has_potential_type = True

                        if not has_potential_type and _potential_type is not None:
                            set_sf_tag(sf, 'Potential_type', _potential_type)

                        sf_item[sf_framecode]['id'] = count
                        Dihedral_angle_tot_num += count

                    if Dihedral_angle_tot_num > 0:
                        cst_sf.add_tag('Dihedral_angle_tot_num', Dihedral_angle_tot_num)

                    Protein_dihedral_angle_tot_num =\
                        Protein_phi_angle_tot_num =\
                        Protein_psi_angle_tot_num =\
                        Protein_chi_one_angle_tot_num =\
                        Protein_other_angle_tot_num = 0

                    for sf in master_entry.get_saveframes_by_category(sf_category):
                        sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')

                        lp = sf.get_loop(lp_category)

                        id_col = lp.tags.index('ID')
                        auth_asym_id_col = lp.tags.index('Auth_asym_ID_2')
                        auth_seq_id_col = lp.tags.index('Auth_seq_ID_2')
                        auth_comp_id_col = lp.tags.index('Auth_comp_ID_2')
                        angle_name_col = lp.tags.index('Torsion_angle_name')

                        _protein_angles = _other_angles = 0
                        _protein_bb_angles = _protein_oth_angles = 0

                        prev_id = -1
                        for row in lp:
                            _id = int(row[id_col])
                            if _id == prev_id:
                                continue
                            prev_id = _id
                            auth_asym_id = row[auth_asym_id_col]
                            try:
                                auth_seq_id = int(row[auth_seq_id_col]) if row[auth_seq_id_col] not in EMPTY_VALUE else None
                            except (ValueError, TypeError):
                                continue
                            auth_comp_id = row[auth_comp_id_col]
                            angle_name = row[angle_name_col]
                            if angle_name is None:
                                continue

                            seq_key = (auth_asym_id, auth_seq_id, auth_comp_id)

                            if seq_key in auth_to_entity_type:
                                entity_type = auth_to_entity_type[seq_key]

                                if 'peptide' in entity_type:
                                    Protein_dihedral_angle_tot_num += 1
                                    _protein_angles += 1
                                    if angle_name == 'PHI':
                                        Protein_phi_angle_tot_num += 1
                                        _protein_bb_angles += 1
                                    elif angle_name == 'PSI':
                                        Protein_psi_angle_tot_num += 1
                                        _protein_bb_angles += 1
                                    elif angle_name == 'CHI1':
                                        Protein_chi_one_angle_tot_num += 1
                                        _protein_oth_angles += 1
                                    else:
                                        Protein_other_angle_tot_num += 1
                                        _protein_oth_angles += 1
                                else:
                                    _other_angles += 1

                        if _protein_angles > _other_angles == 0:
                            sf_item[sf_framecode]['constraint_type'] = 'protein dihedral angle'

                            tagNames = [t[0] for t in sf.tags]

                            if 'Constraint_type' not in tagNames:
                                sf_item[sf_framecode]['constraint_subtype'] = 'backbone chemical shifts'
                                sf.add_tag('Constraint_subtype', 'backbone chemical shifts')

                    if Protein_dihedral_angle_tot_num > 0:
                        cst_sf.add_tag('Protein_dihedral_angle_tot_num', Protein_dihedral_angle_tot_num)
                        cst_sf.add_tag('Protein_phi_angle_tot_num', Protein_phi_angle_tot_num)
                        cst_sf.add_tag('Protein_psi_angle_tot_num', Protein_psi_angle_tot_num)
                        cst_sf.add_tag('Protein_chi_one_angle_tot_num', Protein_chi_one_angle_tot_num)
                        cst_sf.add_tag('Protein_other_angle_tot_num', Protein_other_angle_tot_num)

                    NA_dihedral_angle_tot_num =\
                        NA_alpha_angle_tot_num =\
                        NA_beta_angle_tot_num =\
                        NA_gamma_angle_tot_num =\
                        NA_delta_angle_tot_num =\
                        NA_epsilon_angle_tot_num =\
                        NA_chi_angle_tot_num =\
                        NA_other_angle_tot_num =\
                        NA_amb_dihedral_angle_tot_num = 0

                    for sf in master_entry.get_saveframes_by_category(sf_category):
                        sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')

                        lp = sf.get_loop(lp_category)

                        id_col = lp.tags.index('ID')
                        auth_asym_id_col = lp.tags.index('Auth_asym_ID_2')
                        auth_seq_id_col = lp.tags.index('Auth_seq_ID_2')
                        auth_comp_id_col = lp.tags.index('Auth_comp_ID_2')
                        angle_name_col = lp.tags.index('Torsion_angle_name')

                        _na_angles = _other_angles = 0

                        prev_id = -1
                        for row in lp:
                            _id = int(row[id_col])
                            if _id == prev_id:
                                continue
                            prev_id = _id
                            auth_asym_id = row[auth_asym_id_col]
                            try:
                                auth_seq_id = int(row[auth_seq_id_col]) if row[auth_seq_id_col] not in EMPTY_VALUE else None
                            except (ValueError, TypeError):
                                continue
                            auth_comp_id = row[auth_comp_id_col]
                            angle_name = row[angle_name_col]
                            if angle_name is None:
                                continue

                            seq_key = (auth_asym_id, auth_seq_id, auth_comp_id)

                            if seq_key in auth_to_entity_type:
                                entity_type = auth_to_entity_type[seq_key]

                                if 'nucleotide' in entity_type:
                                    NA_dihedral_angle_tot_num += 1
                                    _na_angles += 1
                                    if angle_name == 'ALPHA':
                                        NA_alpha_angle_tot_num += 1
                                    elif angle_name == 'BETA':
                                        NA_beta_angle_tot_num += 1
                                    elif angle_name == 'GAMMA':
                                        NA_gamma_angle_tot_num += 1
                                    elif angle_name == 'DELTA':
                                        NA_delta_angle_tot_num += 1
                                    elif angle_name == 'EPSILON':
                                        NA_epsilon_angle_tot_num += 1
                                    elif angle_name == 'CHI':
                                        NA_chi_angle_tot_num += 1
                                    elif angle_name == 'PPA':
                                        NA_amb_dihedral_angle_tot_num += 1
                                    else:
                                        NA_other_angle_tot_num += 1
                                else:
                                    _other_angles += 1

                        if _na_angles > _other_angles:
                            sf_item[sf_framecode]['constraint_type'] = 'nucleic acid dihedral angle'

                            tagNames = [t[0] for t in sf.tags]

                            if 'Constraint_type' not in tagNames:
                                sf_item[sf_framecode]['constraint_subtype'] = 'unknown'
                                sf.add_tag('Constraint_type', 'unknown')

                    if NA_dihedral_angle_tot_num > 0:
                        cst_sf.add_tag('NA_dihedral_angle_tot_num', NA_dihedral_angle_tot_num)
                        cst_sf.add_tag('NA_alpha_angle_tot_num', NA_alpha_angle_tot_num)
                        cst_sf.add_tag('NA_beta_angle_tot_num', NA_beta_angle_tot_num)
                        cst_sf.add_tag('NA_gamma_angle_tot_num', NA_gamma_angle_tot_num)
                        cst_sf.add_tag('NA_delta_angle_tot_num', NA_delta_angle_tot_num)
                        cst_sf.add_tag('NA_epsilon_angle_tot_num', NA_epsilon_angle_tot_num)
                        cst_sf.add_tag('NA_chi_angle_tot_num', NA_chi_angle_tot_num)
                        cst_sf.add_tag('NA_other_angle_tot_num', NA_other_angle_tot_num)
                        cst_sf.add_tag('NA_amb_dihedral_angle_tot_num', NA_amb_dihedral_angle_tot_num)

                    for sf in master_entry.get_saveframes_by_category(sf_category):
                        sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')

                        lp = sf.get_loop(lp_category)

                        id_col = lp.tags.index('ID')
                        auth_asym_id_col = lp.tags.index('Auth_asym_ID_2')
                        auth_seq_id_col = lp.tags.index('Auth_seq_ID_2')
                        auth_comp_id_col = lp.tags.index('Auth_comp_ID_2')
                        angle_name_col = lp.tags.index('Torsion_angle_name')

                        _br_angles = _other_angles = 0

                        prev_id = -1
                        for row in lp:
                            _id = int(row[id_col])
                            if _id == prev_id:
                                continue
                            prev_id = _id
                            auth_asym_id = row[auth_asym_id_col]
                            try:
                                auth_seq_id = int(row[auth_seq_id_col]) if row[auth_seq_id_col] not in EMPTY_VALUE else None
                            except (ValueError, TypeError):
                                continue
                            auth_comp_id = row[auth_comp_id_col]
                            angle_name = row[angle_name_col]
                            if angle_name is None:
                                continue

                            seq_key = (auth_asym_id, auth_seq_id, auth_comp_id)

                            if seq_key in auth_to_entity_type:
                                entity_type = auth_to_entity_type[seq_key]

                                if 'saccharide' in entity_type:
                                    _br_angles += 1
                                else:
                                    _other_angles += 1

                        if _br_angles > _other_angles:
                            sf_item[sf_framecode]['constraint_type'] = 'carbohydrate dihedral angle'  # DAOTHER-9471

                            tagNames = [t[0] for t in sf.tags]

                            if 'Constraint_type' not in tagNames:
                                sf_item[sf_framecode]['constraint_subtype'] = 'unknown'
                                sf.add_tag('Constraint_type', 'unknown')

                elif content_subtype == 'rdc_restraint':

                    sf_category = SF_CATEGORIES[file_type][content_subtype]
                    lp_category = LP_CATEGORIES[file_type][content_subtype]

                    for sf in master_entry.get_saveframes_by_category(sf_category):
                        sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')
                        if sf_framecode not in sf_item:
                            # DAOTHER-9471
                            sf_item[sf_framecode] = {'constraint_type': 'dipolar coupling', 'constraint_subtype': 'RDC'}

                        lp = sf.get_loop(lp_category)

                        item_names = ITEM_NAMES_IN_RDC_LOOP[file_type]
                        id_col = lp.tags.index('ID')
                        try:
                            target_value_col = lp.tags.index(item_names['target_value'])
                        except ValueError:
                            target_value_col = -1
                        try:
                            lower_limit_col = lp.tags.index(item_names['lower_limit'])
                        except ValueError:
                            lower_limit_col = -1
                        try:
                            upper_limit_col = lp.tags.index(item_names['upper_limit'])
                        except ValueError:
                            upper_limit_col = -1
                        try:
                            lower_linear_limit_col = lp.tags.index(item_names['lower_linear_limit'])
                        except ValueError:
                            lower_linear_limit_col = -1
                        try:
                            upper_linear_limit_col = lp.tags.index(item_names['upper_linear_limit'])
                        except ValueError:
                            upper_linear_limit_col = -1

                        potential_type = get_first_sf_tag(sf, 'Potential_type')
                        has_potential_type = len(potential_type) > 0 and potential_type not in EMPTY_VALUE\
                            and potential_type != 'unknown'

                        _potential_type = None
                        count = 0

                        prev_id = -1
                        for row in lp:
                            _id = int(row[id_col])
                            if _id == prev_id:
                                continue
                            prev_id = _id
                            count += 1
                            if not has_potential_type:
                                dst_func = {}
                                if target_value_col != -1 and row[target_value_col] not in EMPTY_VALUE:
                                    dst_func['target_value'] = float(row[target_value_col])
                                if lower_limit_col != -1 and row[lower_limit_col] not in EMPTY_VALUE:
                                    dst_func['lower_limit'] = float(row[lower_limit_col])
                                if upper_limit_col != -1 and row[upper_limit_col] not in EMPTY_VALUE:
                                    dst_func['upper_limit'] = float(row[upper_limit_col])
                                if lower_linear_limit_col != -1 and row[lower_linear_limit_col] not in EMPTY_VALUE:
                                    dst_func['lower_linear_limit'] = float(row[lower_linear_limit_col])
                                if upper_linear_limit_col != -1 and row[upper_linear_limit_col] not in EMPTY_VALUE:
                                    dst_func['upper_linear_limit'] = float(row[upper_linear_limit_col])
                                if _potential_type is None:
                                    _potential_type = getPotentialType(file_type, 'rdc', dst_func)
                                else:
                                    if getPotentialType(file_type, 'rdc', dst_func) != _potential_type:
                                        has_potential_type = True

                        if not has_potential_type and _potential_type is not None:
                            set_sf_tag(sf, 'Potential_type', _potential_type)

                        sf_item[sf_framecode]['id'] = count

                    RDC_tot_num =\
                        RDC_HH_tot_num =\
                        RDC_HNC_tot_num =\
                        RDC_NH_tot_num =\
                        RDC_CC_tot_num =\
                        RDC_CN_i_1_tot_num =\
                        RDC_CAHA_tot_num =\
                        RDC_HNHA_tot_num =\
                        RDC_HNHA_i_1_tot_num =\
                        RDC_CAC_tot_num =\
                        RDC_CAN_tot_num =\
                        RDC_other_tot_num =\
                        RDC_intraresidue_tot_num =\
                        RDC_sequential_tot_num =\
                        RDC_medium_range_tot_num =\
                        RDC_long_range_tot_num =\
                        RDC_unambig_intramol_tot_num =\
                        RDC_unambig_intermol_tot_num =\
                        RDC_ambig_intramol_tot_num =\
                        RDC_ambig_intermol_tot_num =\
                        RDC_intermol_tot_num = 0

                    for sf in master_entry.get_saveframes_by_category(sf_category):
                        sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')

                        lp = sf.get_loop(lp_category)

                        # RDC_tot_num += sf_item[sf_framecode]['id']

                        item_names = ITEM_NAMES_IN_RDC_LOOP[file_type]
                        id_col = lp.tags.index('ID')
                        chain_id_1_col = lp.tags.index(item_names['chain_id_1'])
                        chain_id_2_col = lp.tags.index(item_names['chain_id_2'])
                        seq_id_1_col = lp.tags.index(item_names['seq_id_1'])
                        seq_id_2_col = lp.tags.index(item_names['seq_id_2'])
                        comp_id_1_col = lp.tags.index(item_names['comp_id_1'])
                        atom_id_1_col = lp.tags.index(item_names['atom_id_1'])
                        atom_id_2_col = lp.tags.index(item_names['atom_id_2'])
                        try:
                            combination_id_col = lp.tags.index(item_names['combination_id'])
                        except ValueError:
                            combination_id_col = -1

                        prev_id = -1
                        for row in lp:
                            _id = int(row[id_col])
                            if _id == prev_id:
                                continue
                            prev_id = _id
                            chain_id_1 = row[chain_id_1_col]
                            chain_id_2 = row[chain_id_2_col]
                            try:
                                seq_id_1 = int(row[seq_id_1_col]) if row[seq_id_1_col] not in EMPTY_VALUE else None
                                seq_id_2 = int(row[seq_id_2_col]) if row[seq_id_2_col] not in EMPTY_VALUE else None
                            except (ValueError, TypeError):
                                continue
                            comp_id_1 = row[comp_id_1_col]
                            atom_id_1 = row[atom_id_1_col]
                            atom_id_2 = row[atom_id_2_col]

                            if atom_id_1 in EMPTY_VALUE or atom_id_2 in EMPTY_VALUE:
                                continue

                            combination_id = row[combination_id_col] if combination_id_col != -1 else None

                            vector = {atom_id_1, atom_id_2}
                            offset = abs(seq_id_1 - seq_id_2)

                            RDC_tot_num += 1

                            if chain_id_1 == chain_id_2:
                                if vector == {'H', 'C'} and offset == 1:
                                    RDC_HNC_tot_num += 1
                                elif vector == {'H', 'N'} and offset == 0:
                                    RDC_NH_tot_num += 1
                                elif vector == {'C', 'N'} and offset == 1:
                                    RDC_CN_i_1_tot_num += 1
                                elif vector == {'CA', 'HA'} and offset == 0:
                                    RDC_CAHA_tot_num += 1
                                elif vector == {'H', 'HA'} and offset == 0:
                                    RDC_HNHA_tot_num += 1
                                elif vector == {'H', 'HA'} and offset == 1:
                                    RDC_HNHA_i_1_tot_num += 1
                                elif vector == {'CA', 'C'} and offset == 0:
                                    RDC_CAC_tot_num += 1
                                elif vector == {'CA', 'N'} and offset == 0:
                                    RDC_CAN_tot_num += 1
                                elif atom_id_1[0] == atom_id_2[0]:
                                    if atom_id_1[0] in PROTON_BEGIN_CODE:
                                        RDC_HH_tot_num += 1
                                    elif atom_id_1[0] == 'C':
                                        RDC_CC_tot_num += 1
                                    else:
                                        RDC_other_tot_num += 1
                                elif offset == 0 and comp_id_1 == 'TRP' and vector == {'HE1', 'NE1'}:
                                    RDC_NH_tot_num += 1
                                elif offset == 0 and comp_id_1 == 'ARG' and vector == {'HE', 'NE'}:
                                    RDC_NH_tot_num += 1
                                else:
                                    RDC_other_tot_num += 1

                            if chain_id_1 == chain_id_2:
                                if offset == 0:
                                    RDC_intraresidue_tot_num += 1
                                elif offset == 1:
                                    RDC_sequential_tot_num += 1
                                elif offset < 5:
                                    RDC_medium_range_tot_num += 1
                                else:
                                    RDC_long_range_tot_num += 1
                                if combination_id in EMPTY_VALUE:
                                    RDC_unambig_intramol_tot_num += 1
                                else:
                                    RDC_ambig_intramol_tot_num += 1

                            else:
                                RDC_intermol_tot_num += 1
                                if combination_id in EMPTY_VALUE:
                                    RDC_unambig_intermol_tot_num += 1
                                else:
                                    RDC_ambig_intermol_tot_num += 1

                    if RDC_tot_num > 0:
                        cst_sf.add_tag('RDC_tot_num', RDC_tot_num)
                        cst_sf.add_tag('RDC_HH_tot_num', RDC_HH_tot_num)
                        cst_sf.add_tag('RDC_HNC_tot_num', RDC_HNC_tot_num)
                        cst_sf.add_tag('RDC_NH_tot_num', RDC_NH_tot_num)
                        cst_sf.add_tag('RDC_CC_tot_num', RDC_CC_tot_num)
                        cst_sf.add_tag('RDC_CN_i_1_tot_num', RDC_CN_i_1_tot_num)
                        cst_sf.add_tag('RDC_CAHA_tot_num', RDC_CAHA_tot_num)
                        cst_sf.add_tag('RDC_HNHA_tot_num', RDC_HNHA_tot_num)
                        cst_sf.add_tag('RDC_HNHA_i_1_tot_num', RDC_HNHA_i_1_tot_num)
                        cst_sf.add_tag('RDC_CAC_tot_num', RDC_CAC_tot_num)
                        cst_sf.add_tag('RDC_CAN_tot_num', RDC_CAN_tot_num)
                        cst_sf.add_tag('RDC_other_tot_num', RDC_other_tot_num)
                        cst_sf.add_tag('RDC_intraresidue_tot_num', RDC_intraresidue_tot_num)
                        cst_sf.add_tag('RDC_sequential_tot_num', RDC_sequential_tot_num)
                        cst_sf.add_tag('RDC_medium_range_tot_num', RDC_medium_range_tot_num)
                        cst_sf.add_tag('RDC_long_range_tot_num', RDC_long_range_tot_num)
                        cst_sf.add_tag('RDC_unambig_intramol_tot_num', RDC_unambig_intramol_tot_num)
                        cst_sf.add_tag('RDC_unambig_intermol_tot_num', RDC_unambig_intermol_tot_num)
                        cst_sf.add_tag('RDC_ambig_intramol_tot_num', RDC_ambig_intramol_tot_num)
                        cst_sf.add_tag('RDC_ambig_intermol_tot_num', RDC_ambig_intermol_tot_num)
                        cst_sf.add_tag('RDC_intermol_tot_num', RDC_intermol_tot_num)

                elif content_subtype in self._reg.mr_content_subtypes:

                    sf_category = SF_CATEGORIES[file_type][content_subtype]
                    lp_category = LP_CATEGORIES[file_type][content_subtype]

                    restraint_name = getRestraintName(content_subtype)
                    _restraint_name = restraint_name.split()

                    for sf in master_entry.get_saveframes_by_category(sf_category):
                        sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')
                        if sf_framecode not in sf_item:
                            sf_item[sf_framecode] = {'constraint_type': ' '.join(_restraint_name[:-1])}

                            lp = sf.get_loop(lp_category)

                            id_col = lp.tags.index('ID')

                            count = 0

                            prev_id = -1
                            for row in lp:
                                _id = int(row[id_col])
                                if _id == prev_id:
                                    continue
                                prev_id = _id
                                count += 1

                            sf_item[sf_framecode]['id'] = count

        content_subtype = 'dist_restraint'

        sf_category = SF_CATEGORIES[file_type][content_subtype]

        H_bonds_constrained_tot_num = 0
        for sf in master_entry.get_saveframes_by_category(sf_category):
            sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')
            try:
                if 'constraint_subtype' in sf_item[sf_framecode]\
                   and sf_item[sf_framecode]['constraint_subtype'] == 'hydrogen bond':
                    H_bonds_constrained_tot_num += sf_item[sf_framecode]['id']
            except KeyError:
                pass

        if H_bonds_constrained_tot_num > 0:
            cst_sf.add_tag('H_bonds_constrained_tot_num', H_bonds_constrained_tot_num)

        SS_bonds_constrained_tot_num = 0
        for sf in master_entry.get_saveframes_by_category(sf_category):
            sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')
            try:
                if 'constraint_subtype' in sf_item[sf_framecode]\
                   and sf_item[sf_framecode]['constraint_subtype'] == 'disulfide bond':
                    SS_bonds_constrained_tot_num += sf_item[sf_framecode]['id']
            except KeyError:
                pass

        if SS_bonds_constrained_tot_num > 0:
            cst_sf.add_tag('SS_bonds_constrained_tot_num', SS_bonds_constrained_tot_num)

        Derived_photo_cidnps_tot_num = 0
        for sf in master_entry.get_saveframes_by_category(sf_category):
            sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')
            try:
                if 'constraint_subtype' in sf_item[sf_framecode]\
                   and sf_item[sf_framecode]['constraint_subtype'] == 'photo cidnp':
                    Derived_photo_cidnps_tot_num += sf_item[sf_framecode]['id']
            except KeyError:
                pass

        if Derived_photo_cidnps_tot_num > 0:
            cst_sf.add_tag('Derived_photo_cidnps_tot_num', Derived_photo_cidnps_tot_num)

        Derived_paramag_relax_tot_num = 0
        for sf in master_entry.get_saveframes_by_category(sf_category):
            sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')
            try:
                if 'constraint_subtype' in sf_item[sf_framecode]\
                   and sf_item[sf_framecode]['constraint_subtype'] == 'paramagnetic relaxation':
                    Derived_paramag_relax_tot_num += sf_item[sf_framecode]['id']
            except KeyError:
                pass

        if Derived_paramag_relax_tot_num > 0:
            cst_sf.add_tag('Derived_paramag_relax_tot_num', Derived_paramag_relax_tot_num)

        lp_category = '_Constraint_file'

        cf_loop = pynmrstar.Loop.from_scratch(lp_category)

        cf_key_items = [{'name': 'ID', 'type': 'int'},
                        {'name': 'Constraint_filename', 'type': 'str'},
                        # {'name': 'Software_ID', 'type': 'int'},
                        # {'name': 'Software_label', 'type': 'str'},
                        # {'name': 'Software_name', 'type': 'str'},
                        {'name': 'Block_ID', 'type': 'int'},
                        {'name': 'Constraint_type', 'type': 'enum',
                         'enum': ('distance', 'dipolar coupling', 'protein dihedral angle', 'nucleic acid dihedral angle',
                                  'coupling constant', 'chemical shift', 'other angle', 'chemical shift anisotropy',
                                  'hydrogen exchange', 'line broadening', 'pseudocontact shift', 'intervector projection angle',
                                  'protein peptide planarity', 'protein other kinds of constraints',
                                  'nucleic acid base planarity', 'nucleic acid other kinds of constraints',
                                  'carbohydrate dihedral angle')},
                        {'name': 'Constraint_subtype', 'type': 'enum',
                         'enum': ('Not applicable', 'NOE', 'NOE buildup', 'NOE not seen', 'general distance',
                                  'alignment tensor', 'chirality', 'prochirality', 'disulfide bond', 'hydrogen bond',
                                  'symmetry', 'ROE', 'peptide', 'ring', 'PRE')},
                        {'name': 'Constraint_subsubtype', 'type': 'enum',
                         'enum': ('ambi', 'simple')}
                        ]
        cf_data_items = [{'name': 'Constraint_number', 'type': 'int'},
                         {'name': 'Constraint_stat_list_ID', 'type': 'int', 'mandatory': True,
                          'default': '1', 'default-from': 'parent'},
                         {'name': 'Entry_ID', 'type': 'str', 'mandatory': False}
                         ]

        tags = [f"{lp_category}.{_item['name']}" for _item in cf_key_items]
        tags.extend([f"{lp_category}.{_item['name']}" for _item in cf_data_items])

        cf_loop.add_tag(tags)

        if has_key_value(input_source_dic, 'content_subtype'):

            block_id = 0

            for content_subtype in self._reg.mr_content_subtypes:
                if content_subtype in input_source_dic['content_subtype']:
                    sf_category = SF_CATEGORIES[file_type][content_subtype]

                    for sf in master_entry.get_saveframes_by_category(sf_category):
                        sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')

                        row = [None] * len(tags)

                        row[0], row[1] = 1, self._reg.srcName
                        sf_allowed_tags = SF_ALLOWED_TAGS[file_type][content_subtype]
                        if 'Constraint_file_ID' in sf_allowed_tags:
                            set_sf_tag(sf, 'Constraint_file_ID', 1)
                        if 'Block_ID' in sf_allowed_tags:
                            block_id += 1
                            _block_id = str(block_id)
                            set_sf_tag(sf, 'Block_ID', _block_id)
                            row[2] = _block_id
                        constraint_type = sf_item[sf_framecode]['constraint_type']
                        constraint_subtype = get_first_sf_tag(sf, 'Constraint_type')\
                            if content_subtype != 'other_restraint' else get_first_sf_tag(sf, 'Definition')
                        if len(constraint_subtype) == 0 or constraint_subtype in EMPTY_VALUE:
                            constraint_subtype = sf_item[sf_framecode]['constraint_subtype']\
                                if 'constraint_subtype' in sf_item[sf_framecode] else None
                        if constraint_subtype is not None and constraint_subtype == 'RDC':  # DAOTHER-9471
                            constraint_type = 'dipolar coupling'

                        constraint_subsubtype = sf_item[sf_framecode]['constraint_subsubtype']\
                            if 'constraint_subsubtype' in sf_item[sf_framecode] else None
                        row[3], row[4], row[5], row[6] =\
                            constraint_type, constraint_subtype, constraint_subsubtype, sf_item[sf_framecode]['id']
                        row[7], row[8] = 1, self._reg.entry_id

                        cf_loop.add_data(row)

            cst_sf.add_loop(cf_loop)

            if len(cf_loop) > 0:
                master_entry.add_saveframe(cst_sf)

        # resolve CYANA distance subtype

        tags = ['Constraint_filename', 'Block_ID', 'Constraint_type', 'Constraint_subtype', 'Constraint_subsubtype']

        if set(tags) & set(cf_loop.tags) != set(tags):
            dat = cf_loop.get_tag(tags)

            for dist_subtype in ['NOE', 'ROE', 'hydrogen bond', 'disulfide bond', 'diselenide bond']:
                cyana_subtype = {}
                for row in dat:
                    if row[2] == 'distance' and row[3] == dist_subtype and row[4] == 'simple':
                        if row[0] not in cyana_subtype:
                            cyana_subtype[row[0]] = []
                        cyana_subtype[row[0]].append(row[1] if isinstance(row[1], str) else str(row[1]))

                if any(True for v in cyana_subtype.values() if len(v) > 1):
                    for v in cyana_subtype.values():
                        if len(v) < 2:
                            continue
                        cyana_potential_type = {}
                        for block_id in v:
                            for sf in master_entry.get_saveframes_by_category('general_distance_constraints'):
                                _block_id = get_first_sf_tag(sf, 'Block_ID')
                                if _block_id in EMPTY_VALUE:
                                    continue
                                if isinstance(_block_id, int):
                                    _block_id = str(_block_id)
                                if _block_id == block_id:
                                    cyana_potential_type[get_first_sf_tag(sf, 'Potential_type').split('-')[0]] = block_id
                        if len(cyana_potential_type) > 1:
                            if 'upper' in cyana_potential_type:
                                block_id = cyana_potential_type['upper']
                                for idx, row in enumerate(dat):
                                    if row[2] == 'distance' and row[3] == dist_subtype and row[4] == 'simple'\
                                       and (row[1] if isinstance(row[1], str) else str(row[1])) == block_id:
                                        cf_loop.data[idx][cf_loop.tags.index('Constraint_subtype')] =\
                                            f'{dist_subtype} (upper bound)'

        # update _Data_set/Datum loop

        try:

            content_subtype = 'entry_info'

            sf_category = SF_CATEGORIES[file_type][content_subtype]

            sf = master_entry.get_saveframes_by_category(sf_category)[0]

            # update _Data_set loop

            lp_category = '_Data_set'

            loop = next((loop for loop in sf.loops if loop.category == lp_category), None)

            if loop is not None:
                del sf[loop]

            lp = pynmrstar.Loop.from_scratch(lp_category)

            items = ['Type', 'Count', 'Entry_ID']

            tags = [f'{lp_category}.{item}' for item in items]

            lp.add_tag(tags)

            for content_subtype in self._reg.nmr_rep_content_subtypes:
                sf_category = SF_CATEGORIES[file_type][content_subtype]

                if sf_category.endswith('constraints'):  # ignore non-quantitative data set
                    continue

                count = sum(1 for sf in master_entry.frame_list if sf.category == sf_category)

                if count > 0:
                    row = [sf_category, count, self._reg.entry_id]
                    lp.add_data(row)
                    lp.data.sort()

            lp.sort_rows('Type')

            sf.add_loop(lp)

            # update _Datum loop

            lp_category = '_Datum'

            loop = next((loop for loop in sf.loops if loop.category == lp_category), None)

            if loop is not None:
                del sf[loop]

            lp = pynmrstar.Loop.from_scratch(lp_category)

            tags = [f'{lp_category}.{item}' for item in items]

            lp.add_tag(tags)

            datum_counter = self._reg.dpV.getDatumCounter(master_entry)

            for k, v in datum_counter.items():
                row = [k, v, self._reg.entry_id]
                lp.add_data(row)

            sf.add_loop(lp)

        except IndexError:
            pass

        master_entry = self._reg.c2S.normalize_str(master_entry)

        master_entry.write_to_file(self._reg.dstPath,
                                   show_comments=(self._reg.bmrb_only and self._reg.internal_mode),
                                   skip_empty_loops=True, skip_empty_tags=False)

        return True
