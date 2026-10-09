##
# File: NmrDpRemediationMerge.py
# Date: 17-Aug-2026
#
# Updates:
##
""" Merger of legacy NMR data into the combined NMR-STAR file.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.3"

import gc
import os
from datetime import datetime, timedelta
from operator import itemgetter

import pynmrstar

try:
    from wwpdb.utils.nmr.NmrDpConstant import (AR_FILE_PATH_LIST_KEY,
                                               NMR_CONTENT_SUBTYPES,
                                               READABLE_FILE_TYPE,
                                               SF_CATEGORIES,
                                               LP_CATEGORIES,
                                               SF_ALLOWED_TAGS,
                                               ITEM_NAMES_IN_DIST_LOOP,
                                               ITEM_NAMES_IN_RDC_LOOP,
                                               EMPTY_VALUE,
                                               PROTON_BEGIN_CODE,
                                               NMR_STAR_VERSION,
                                               INTNL_ANY_MR_FILE_NAME_PAT,
                                               PDB_MR_FILE_NAME_PAT,
                                               DIST_AMBIG_LOW,
                                               DIST_AMBIG_UP)
    from wwpdb.utils.nmr.AlignUtil import getPrettyJson
    from wwpdb.utils.nmr.CifToNmrStar import (get_first_sf_tag,
                                              set_sf_tag)
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (incListIdCounter,
                                                       retrieveOriginalFileName,
                                                       getPdbxNmrSoftwareName,
                                                       getSaveframe)
    from wwpdb.utils.nmr.NmrDpRemediationBase import NmrDpRemediationBase
except ImportError:
    from nmr.NmrDpConstant import (AR_FILE_PATH_LIST_KEY,
                                   NMR_CONTENT_SUBTYPES,
                                   READABLE_FILE_TYPE,
                                   SF_CATEGORIES,
                                   LP_CATEGORIES,
                                   SF_ALLOWED_TAGS,
                                   ITEM_NAMES_IN_DIST_LOOP,
                                   ITEM_NAMES_IN_RDC_LOOP,
                                   EMPTY_VALUE,
                                   PROTON_BEGIN_CODE,
                                   NMR_STAR_VERSION,
                                   INTNL_ANY_MR_FILE_NAME_PAT,
                                   PDB_MR_FILE_NAME_PAT,
                                   DIST_AMBIG_LOW,
                                   DIST_AMBIG_UP)
    from nmr.AlignUtil import getPrettyJson
    from nmr.CifToNmrStar import (get_first_sf_tag,
                                  set_sf_tag)
    from nmr.mr.ParserListenerUtil import (incListIdCounter,
                                           retrieveOriginalFileName,
                                           getPdbxNmrSoftwareName,
                                           getSaveframe)
    from nmr.NmrDpRemediationBase import NmrDpRemediationBase


class NmrDpRemediationMerge(NmrDpRemediationBase):
    """ Merger of legacy NMR data into the combined NMR-STAR file.
    """
    __slots__ = ()

    def mergeLegacyData(self) -> bool:
        """ Merge CS+MR+PK into next NMR combined data files.
        """

        if self._reg.combined_mode or not self._reg.remediation_mode or self._reg.dstPath is None:
            return False

        if len(self._reg.star_data) == 0 or not isinstance(self._reg.star_data[0], pynmrstar.Entry):
            return False

        master_entry = self._reg.star_data[0]

        sf_framecode = 'constraint_statistics'

        cst_sfs = master_entry.get_saveframes_by_category(sf_framecode)

        if len(cst_sfs) > 0:
            for cst_sf in reversed(cst_sfs):
                del master_entry[cst_sf]

        input_source = self._reg.report.input_sources[0]
        input_source_dic = input_source.get()

        original_file_name = input_source_dic['file_name']
        if 'original_file_name' in input_source_dic and input_source_dic['original_file_name'] is not None:
            original_file_name = os.path.basename(input_source_dic['original_file_name'])

        file_type = 'nmr-star'

        master_entry.entry_id = f'cs_{self._reg.entry_id.lower()}'

        self._reg.c2S.set_entry_id(master_entry, self._reg.entry_id)

        self._reg.c2S.normalize_str(master_entry)

        if self._reg.bmrb_only and self._reg.internal_mode and self._reg.bmrb_id is not None:
            master_entry.entry_id = self._reg.bmrb_id
        else:
            master_entry.entry_id = f'nef_{self._reg.entry_id.lower()}'

        self._reg.c2S.set_entry_id(master_entry, self._reg.entry_id)

        # remove _Audit loop if exists

        content_subtype = 'entry_info'

        sf_category = SF_CATEGORIES[file_type][content_subtype]
        lp_category = '_Audit'
        update_audit = False

        sf_list = master_entry.get_saveframes_by_category(sf_category)

        if self._reg.internal_mode:
            today = datetime.today()
            today_weekday = today.weekday()
            days_ahead = (4 - today_weekday) % 7
            this_friday = today + timedelta(days=days_ahead)

        try:

            sf = sf_list[0]

            try:

                loop = sf.get_loop(lp_category)

                if self._reg.internal_mode:

                    dat = loop.get_tag(['Revision_ID', 'Update_record'])

                    if any(True for row in dat if row[1] == 'Initial release'):
                        last_revision_id = int(dat[-1][0])

                        row = [None] * len(loop.tags)
                        row[loop.tags.index('Revision_ID')] = last_revision_id + 1
                        row[loop.tags.index('Creation_date')] = this_friday.strftime('%Y-%m-%d')
                        row[loop.tags.index('Update_record')] = 'Remediation'
                        row[loop.tags.index('Entry_ID')] = self._reg.entry_id

                        loop.add_data(row)

                        update_audit = True

                else:
                    del sf[loop]

            except KeyError:
                pass

        except IndexError:
            pass

        if len(sf_list) > 1:

            for sf in sf_list[1:]:

                try:

                    loop = sf.get_loop(lp_category)

                    if self._reg.internal_mode:

                        dat = loop.get_tag(['Revision_ID', 'Update_record'])

                        if any(True for row in dat if row[1] == 'Initial release'):
                            last_revision_id = int(dat[-1][0])

                            row = [None] * len(loop.tags)
                            row[loop.tags.index('Revision_ID')] = last_revision_id + 1
                            row[loop.tags.index('Creation_date')] = this_friday.strftime('%Y-%m-%d')
                            row[loop.tags.index('Update_record')] = 'Remediation'
                            row[loop.tags.index('Entry_ID')] = self._reg.entry_id

                            loop.add_data(row)

                            update_audit = True

                        sf_list[0].add_loop(loop)

                except KeyError:
                    pass

                del master_entry[sf]

        if self._reg.internal_mode and not self._reg.bmrb_only and not update_audit:

            sf_list = master_entry.get_saveframes_by_category(sf_category)

            try:

                sf = sf_list[0]

                try:

                    loop = sf.get_loop(lp_category)

                except KeyError:

                    lp = pynmrstar.Loop.from_scratch(lp_category)

                    items = ['Revision_ID', 'Creation_date', 'Update_record', 'Creation_method', 'Entry_ID']

                    tags = [f'{lp_category}.{item}' for item in items]

                    lp.add_tag(tags)

                    lp.add_data([1, this_friday.strftime('%Y-%m-%d'), 'Preliminary version', None, self._reg.entry_id])

                    sf.add_loop(lp)

            except IndexError:
                pass

        if self._reg.internal_mode and not self._reg.bmrb_only:

            nmr_star_version = get_first_sf_tag(sf_list[0], 'NMR_STAR_version')

            if len(nmr_star_version) == 0:
                set_sf_tag(sf_list[0], 'NMR_star_version', NMR_STAR_VERSION)

            sf_category = 'entry_interview'

            sf_list = master_entry.get_saveframes_by_category(sf_category)

            if len(sf_list) > 0:

                pdb_deposition = get_first_sf_tag(sf_list[0], 'PDB_deposition')
                if pdb_deposition == 'no':
                    set_sf_tag(sf_list[0], 'PDB_deposition', 'yes')

                view_mode = get_first_sf_tag(sf_list[0], 'View_mode')
                if len(view_mode) > 0 and view_mode != 'PDB/BMRB':
                    set_sf_tag(sf_list[0], 'View_mode', 'PDB/BMRB')

        # refresh _Constraint_stat_list saveframe

        cst_sf = pynmrstar.Saveframe.from_scratch(sf_framecode)
        cst_sf.set_tag_prefix('_Constraint_stat_list')
        cst_sf.add_tag('Sf_category', sf_framecode)
        cst_sf.add_tag('Sf_framecode', sf_framecode)
        cst_sf.add_tag('Entry_ID', self._reg.entry_id)
        cst_sf.add_tag('ID', 1)

        if self._reg.remediation_mode:

            if AR_FILE_PATH_LIST_KEY in self._reg.inputParamDict:

                fileListId = self._reg.file_path_list_len

                file_names = []

                for ar in self._reg.inputParamDict[AR_FILE_PATH_LIST_KEY]:

                    input_source = self._reg.report.input_sources[fileListId]
                    input_source_dic = input_source.get()

                    fileListId += 1

                    ar_file_type = input_source_dic['file_type']

                    if not ar_file_type.startswith('nm-res') or ar_file_type == 'nm-res-mr':
                        continue

                    if 'original_file_name' in ar and ar['original_file_name'] not in EMPTY_VALUE:
                        file_name = ar['original_file_name']
                    else:
                        file_name = input_source_dic['file_name']

                    file_names.append(retrieveOriginalFileName(file_name))

                if len(file_names) > 0:
                    cst_sf.add_tag('Data_file_name', ','.join(file_names))

        # statistics

        if self._reg.mr_sf_dict_holder is not None:

            content_subtype = 'dist_restraint'

            if content_subtype in self._reg.mr_sf_dict_holder:
                for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:
                    if 'NOE_dist_averaging_method' in sf_item:
                        cst_sf.add_tag('NOE_dist_averaging_method', sf_item['NOE_dist_averaging_method'])
                        break

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

                for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:

                    sf = sf_item['saveframe']
                    sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')

                    use_member_logic_code = sf_framecode.startswith('XPLOR') or sf_framecode.startswith('CNS')\
                        or sf_framecode.startswith('CHARMM')
                    if use_member_logic_code:
                        lp = sf_item['loop']
                        if 'Member_logic_code' not in lp.tags:
                            use_member_logic_code = False
                        else:
                            dat = lp.get_tag(['Member_logic_code'])
                            use_member_logic_code = any(True for row in dat if row not in EMPTY_VALUE)

                    if not use_member_logic_code:
                        self._reg.dpV.updateGenDistConstIdInMrStr(sf_item)

                    potential_type = get_first_sf_tag(sf, 'Potential_type')
                    if 'lower' in potential_type:
                        continue
                    constraint_type = get_first_sf_tag(sf, 'Constraint_type')
                    if 'NOE' in constraint_type:
                        # NOE_tot_num += sf_item['id']

                        lp = sf_item['loop']

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
                            upper_limit =\
                                float(row[upper_limit_col]) if upper_limit_col != -1 and row[upper_limit_col] not in EMPTY_VALUE\
                                else None

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

                for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:
                    sf = sf_item['saveframe']
                    potential_type = get_first_sf_tag(sf, 'Potential_type')
                    if 'lower' in potential_type:
                        continue
                    constraint_type = get_first_sf_tag(sf, 'Constraint_type')
                    if constraint_type in ('paramagnetic relaxation',
                                           'photo cidnp',
                                           'chemical shift perturbation',
                                           'mutation',
                                           'symmetry'):
                        NOE_other_tot_num += sf_item['id']

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

                for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:
                    if 'ROE_dist_averaging_method' in sf_item:
                        cst_sf.add_tag('ROE_dist_averaging_method', sf_item['ROE_dist_averaging_method'])
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

                for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:
                    sf = sf_item['saveframe']
                    potential_type = get_first_sf_tag(sf, 'Potential_type')
                    if 'lower' in potential_type:
                        continue
                    constraint_type = get_first_sf_tag(sf, 'Constraint_type')
                    if 'ROE' in constraint_type:
                        # ROE_tot_num += sf_item['id']

                        lp = sf_item['loop']

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
                            upper_limit =\
                                float(row[upper_limit_col]) if upper_limit_col != -1 and row[upper_limit_col] not in EMPTY_VALUE\
                                else None

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

            content_subtype = 'dihed_restraint'

            auth_to_entity_type = self._reg.caC['auth_to_entity_type']

            Dihedral_angle_tot_num = 0
            if content_subtype in self._reg.mr_sf_dict_holder:
                for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:
                    Dihedral_angle_tot_num += sf_item['id']

            if Dihedral_angle_tot_num > 0:
                cst_sf.add_tag('Dihedral_angle_tot_num', Dihedral_angle_tot_num)

            Protein_dihedral_angle_tot_num =\
                Protein_phi_angle_tot_num =\
                Protein_psi_angle_tot_num =\
                Protein_chi_one_angle_tot_num =\
                Protein_other_angle_tot_num = 0

            if content_subtype in self._reg.mr_sf_dict_holder:
                for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:
                    self._reg.dpV.updateTorsionAngleConstIdInMrStr(sf_item)

                    lp = sf_item['loop']

                    lp.sort_rows('ID')
                    lp.renumber_rows('Index_ID')

                    id_col = lp.tags.index('ID')
                    auth_asym_id_col = lp.tags.index('Auth_asym_ID_2')
                    auth_seq_id_col = lp.tags.index('Auth_seq_ID_2')
                    auth_comp_id_col = lp.tags.index('Auth_comp_ID_2')
                    angle_name_col = lp.tags.index('Torsion_angle_name')

                    _protein_angles = _other_angles = _protein_bb_angles = _protein_oth_angles = 0

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

                    if _protein_angles > _other_angles:
                        sf_item['constraint_type'] = 'protein dihedral angle'

                        sf = sf_item['saveframe']

                        if 'jcoup_restraint' not in self._reg.mr_sf_dict_holder:
                            set_sf_tag(sf, 'Constraint_type', 'backbone chemical shifts')

                        else:

                            _protein_jcoups = _protein_bb_jcoups = _protein_oth_jcoups = 0

                            for _sf_item in self._reg.mr_sf_dict_holder['jcoup_restraint']:

                                _lp = _sf_item['loop']

                                auth_asym_id_col = _lp.tags.index('Auth_asym_ID_2')
                                auth_seq_id_col = _lp.tags.index('Auth_seq_ID_2')
                                auth_comp_id_col = _lp.tags.index('Auth_comp_ID_2')
                                atom_id_1_col = _lp.tags.index('Atom_ID_1')
                                atom_id_4_col = _lp.tags.index('Atom_ID_4')

                                for _row in _lp:
                                    auth_asym_id = _row[auth_asym_id_col]
                                    try:
                                        auth_seq_id = int(_row[auth_seq_id_col])
                                    except (ValueError, TypeError):
                                        continue
                                    auth_comp_id = _row[auth_comp_id_col]
                                    atom_id_1 = _row[atom_id_1_col]
                                    atom_id_4 = _row[atom_id_4_col]

                                    seq_key = (auth_asym_id, auth_seq_id, auth_comp_id)

                                    if seq_key in auth_to_entity_type:
                                        entity_type = auth_to_entity_type[seq_key]

                                        if 'peptide' in entity_type:
                                            _protein_jcoups += 1
                                            if 'H' in (atom_id_1, atom_id_4):
                                                _protein_bb_jcoups += 1
                                            else:
                                                _protein_oth_jcoups += 1

                            if (_protein_bb_angles > 0 and _protein_oth_angles == 0
                                and _protein_bb_jcoups > 0 and _protein_oth_jcoups == 0)\
                               or (_protein_bb_angles > 0 and _protein_oth_angles > 0
                                   and _protein_bb_jcoups > 0 and _protein_oth_jcoups > 0)\
                               or (_protein_bb_angles == 0 and _protein_oth_angles > 0
                                   and _protein_bb_jcoups == 0 and _protein_oth_jcoups > 0):
                                set_sf_tag(sf, 'Constraint_type', 'J-couplings')

                            elif _protein_jcoups == 0:
                                set_sf_tag(sf, 'Constraint_type', 'backbone chemical shifts')

                            else:
                                set_sf_tag(sf, 'Constraint_type', 'unknown')

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

            if content_subtype in self._reg.mr_sf_dict_holder:
                for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:

                    lp = sf_item['loop']

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
                        sf_item['constraint_type'] = 'nucleic acid dihedral angle'

                        sf = sf_item['saveframe']

                        if 'jcoup_restraint' not in self._reg.mr_sf_dict_holder:
                            set_sf_tag(sf, 'Constraint_type', 'unknown')

                        else:

                            _na_jcoups = 0

                            for _sf_item in self._reg.mr_sf_dict_holder['jcoup_restraint']:

                                _lp = _sf_item['loop']

                                auth_asym_id_col = _lp.tags.index('Auth_asym_ID_2')
                                auth_seq_id_col = _lp.tags.index('Auth_seq_ID_2')
                                auth_comp_id_col = _lp.tags.index('Auth_comp_ID_2')

                                for _row in _lp:
                                    auth_asym_id = _row[auth_asym_id_col]
                                    try:
                                        auth_seq_id = int(_row[auth_seq_id_col])
                                    except (ValueError, TypeError):
                                        continue
                                    auth_comp_id = _row[auth_comp_id_col]

                                    seq_key = (auth_asym_id, auth_seq_id, auth_comp_id)

                                    if seq_key in auth_to_entity_type:
                                        entity_type = auth_to_entity_type[seq_key]

                                        if 'nucleotide' in entity_type:
                                            _na_jcoups += 1

                            set_sf_tag(sf, 'Constraint_type', 'J-couplings' if _na_jcoups > 0 else 'unknown')

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

            if content_subtype in self._reg.mr_sf_dict_holder:
                for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:

                    lp = sf_item['loop']

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
                        sf_item['constraint_type'] = 'carbohydrate dihedral angle'  # DAOTHER-9471

                        sf = sf_item['saveframe']

                        if 'jcoup_restraint' not in self._reg.mr_sf_dict_holder:
                            set_sf_tag(sf, 'Constraint_type', 'unknown')

                        else:

                            _br_jcoups = 0

                            for _sf_item in self._reg.mr_sf_dict_holder['jcoup_restraint']:

                                _lp = _sf_item['loop']

                                auth_asym_id_col = _lp.tags.index('Auth_asym_ID_2')
                                auth_seq_id_col = _lp.tags.index('Auth_seq_ID_2')
                                auth_comp_id_col = _lp.tags.index('Auth_comp_ID_2')

                                for _row in _lp:
                                    auth_asym_id = _row[auth_asym_id_col]
                                    try:
                                        auth_seq_id = int(_row[auth_seq_id_col])
                                    except (ValueError, TypeError):
                                        continue
                                    auth_comp_id = _row[auth_comp_id_col]

                                    seq_key = (auth_asym_id, auth_seq_id, auth_comp_id)

                                    if seq_key in auth_to_entity_type:
                                        entity_type = auth_to_entity_type[seq_key]

                                        if 'saccharide' in entity_type:
                                            _br_jcoups += 1

                            set_sf_tag(sf, 'Constraint_type', 'J-couplings' if _br_jcoups > 0 else 'unknown')

            content_subtype = 'rdc_restraint'

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

            if content_subtype in self._reg.mr_sf_dict_holder:
                for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:
                    lp = sf_item['loop']

                    # RDC_tot_num += sf_item['id']

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
                        try:
                            chain_id_1 = int(row[chain_id_1_col])
                            chain_id_2 = int(row[chain_id_2_col])
                            seq_id_1 = int(row[seq_id_1_col])
                            seq_id_2 = int(row[seq_id_2_col])
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

            content_subtype = 'dist_restraint'

            hbond_pairs = set()
            if content_subtype in self._reg.mr_sf_dict_holder:
                for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:
                    sf = sf_item['saveframe']
                    potential_type = get_first_sf_tag(sf, 'Potential_type')
                    if 'lower' in potential_type:
                        continue
                    constraint_type = get_first_sf_tag(sf, 'Constraint_type')
                    if constraint_type != 'hydrogen bond':
                        continue

                    lp = sf_item['loop']

                    item_names = ITEM_NAMES_IN_DIST_LOOP[file_type]
                    chain_id_1_col = lp.tags.index(item_names['chain_id_1'])
                    chain_id_2_col = lp.tags.index(item_names['chain_id_2'])
                    seq_id_1_col = lp.tags.index(item_names['seq_id_1'])
                    seq_id_2_col = lp.tags.index(item_names['seq_id_2'])
                    comp_id_1_col = lp.tags.index(item_names['comp_id_1'])
                    comp_id_2_col = lp.tags.index(item_names['comp_id_2'])
                    atom_id_1_col = lp.tags.index(item_names['atom_id_1'])
                    atom_id_2_col = lp.tags.index(item_names['atom_id_2'])

                    for row in lp:
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

                        if atom_id_1 in EMPTY_VALUE or atom_id_2 in EMPTY_VALUE:
                            continue

                        if atom_id_1[0] in PROTON_BEGIN_CODE:
                            if self._reg.ccU.updateChemCompDict(comp_id_1):
                                bonded_atom_id_1 = self._reg.ccU.getBondedAtoms(comp_id_1, atom_id_1)
                                if len(bonded_atom_id_1) == 0:
                                    continue
                                if any(True for _row in lp
                                       if (_row[chain_id_1_col] is not None and int(_row[chain_id_1_col]) == chain_id_1
                                           and _row[seq_id_1_col] is not None and int(_row[seq_id_1_col]) == seq_id_1
                                           and _row[atom_id_1_col] == bonded_atom_id_1[0])
                                       or (_row[chain_id_2_col] is not None and int(_row[chain_id_2_col]) == chain_id_1
                                           and _row[seq_id_2_col] is not None and int(_row[seq_id_2_col]) == seq_id_1
                                           and _row[atom_id_2_col] == bonded_atom_id_1[0])):
                                    continue
                        if atom_id_2[0] in PROTON_BEGIN_CODE:
                            if self._reg.ccU.updateChemCompDict(comp_id_2):
                                bonded_atom_id_2 = self._reg.ccU.getBondedAtoms(comp_id_2, atom_id_2)
                                if len(bonded_atom_id_2) == 0:
                                    continue
                                if any(True for _row in lp
                                       if (_row[chain_id_1_col] is not None and int(_row[chain_id_1_col]) == chain_id_2
                                           and _row[seq_id_1_col] is not None and int(_row[seq_id_1_col]) == seq_id_2
                                           and _row[atom_id_1_col] == bonded_atom_id_2[0])
                                       or (_row[chain_id_2_col] is not None and int(_row[chain_id_2_col]) == chain_id_2
                                           and _row[seq_id_2_col] is not None and int(_row[seq_id_2_col]) == seq_id_2
                                           and _row[atom_id_2_col] == bonded_atom_id_2[0])):
                                    continue
                        p1 = (chain_id_1, seq_id_1, atom_id_1)
                        p2 = (chain_id_2, seq_id_2, atom_id_2)
                        hbond_pair = sorted([p1, p2], key=itemgetter(0, 1, 2))
                        hbond_pairs.add(str(hbond_pair))

            H_bonds_constrained_tot_num = len(hbond_pairs)
            if H_bonds_constrained_tot_num > 0:
                cst_sf.add_tag('H_bonds_constrained_tot_num', H_bonds_constrained_tot_num)

            ssbond_pairs = set()
            if content_subtype in self._reg.mr_sf_dict_holder:
                for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:
                    sf = sf_item['saveframe']
                    potential_type = get_first_sf_tag(sf, 'Potential_type')
                    if 'lower' in potential_type:
                        continue
                    constraint_type = get_first_sf_tag(sf, 'Constraint_type')
                    if constraint_type != 'disulfide bond':
                        continue

                    lp = sf_item['loop']

                    item_names = ITEM_NAMES_IN_DIST_LOOP[file_type]
                    chain_id_1_col = lp.tags.index(item_names['chain_id_1'])
                    chain_id_2_col = lp.tags.index(item_names['chain_id_2'])
                    seq_id_1_col = lp.tags.index(item_names['seq_id_1'])
                    seq_id_2_col = lp.tags.index(item_names['seq_id_2'])
                    comp_id_1_col = lp.tags.index(item_names['comp_id_1'])
                    comp_id_2_col = lp.tags.index(item_names['comp_id_2'])
                    atom_id_1_col = lp.tags.index(item_names['atom_id_1'])
                    atom_id_2_col = lp.tags.index(item_names['atom_id_2'])

                    for row in lp:
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

                        if atom_id_1 in EMPTY_VALUE or atom_id_2 in EMPTY_VALUE:
                            continue

                        if atom_id_1[0] in PROTON_BEGIN_CODE:
                            if self._reg.ccU.updateChemCompDict(comp_id_1):
                                bonded_atom_id_1 = self._reg.ccU.getBondedAtoms(comp_id_1, atom_id_1)
                                if len(bonded_atom_id_1) == 0:
                                    continue
                                if any(True for _row in lp
                                       if (_row[chain_id_1_col] is not None and int(_row[chain_id_1_col]) == chain_id_1
                                           and _row[seq_id_1_col] is not None and int(_row[seq_id_1_col]) == seq_id_1
                                           and _row[atom_id_1_col] == bonded_atom_id_1[0])
                                       or (_row[chain_id_2_col] is not None and int(_row[chain_id_2_col]) == chain_id_1
                                           and _row[seq_id_2_col] is not None and int(_row[seq_id_2_col]) == seq_id_1
                                           and _row[atom_id_2_col] == bonded_atom_id_1[0])):
                                    continue
                        if atom_id_2[0] in PROTON_BEGIN_CODE:
                            if self._reg.ccU.updateChemCompDict(comp_id_2):
                                bonded_atom_id_2 = self._reg.ccU.getBondedAtoms(comp_id_2, atom_id_2)
                                if len(bonded_atom_id_2) == 0:
                                    continue
                                if any(True for _row in lp
                                       if (_row[chain_id_1_col] is not None and int(_row[chain_id_1_col]) == chain_id_2
                                           and _row[seq_id_1_col] is not None and int(_row[seq_id_1_col]) == seq_id_2
                                           and _row[atom_id_1_col] == bonded_atom_id_2[0])
                                       or (_row[chain_id_2_col] is not None and int(_row[chain_id_2_col]) == chain_id_2
                                           and _row[seq_id_2_col] is not None and int(_row[seq_id_2_col]) == seq_id_2
                                           and _row[atom_id_2_col] == bonded_atom_id_2[0])):
                                    continue
                        p1 = (chain_id_1, seq_id_1, atom_id_1)
                        p2 = (chain_id_2, seq_id_2, atom_id_2)
                        ssbond_pair = sorted([p1, p2], key=itemgetter(0, 1, 2))
                        ssbond_pairs.add(str(ssbond_pair))

            SS_bonds_constrained_tot_num = len(ssbond_pairs)
            if SS_bonds_constrained_tot_num > 0:
                cst_sf.add_tag('SS_bonds_constrained_tot_num', SS_bonds_constrained_tot_num)

            content_subtype = 'jcoup_restraint'

            Derived_coupling_const_tot_num = 0
            if content_subtype in self._reg.mr_sf_dict_holder:
                for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:
                    Derived_coupling_const_tot_num += sf_item['id']

            if Derived_coupling_const_tot_num > 0:
                cst_sf.add_tag('Derived_coupling_const_tot_num', Derived_coupling_const_tot_num)

            content_subtype = 'hvycs_restraint'

            Derived_CACB_chem_shift_tot_num = 0
            if content_subtype in self._reg.mr_sf_dict_holder:
                for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:
                    Derived_CACB_chem_shift_tot_num += sf_item['id']

            if Derived_CACB_chem_shift_tot_num > 0:
                cst_sf.add_tag('Derived_CACB_chem_shift_tot_num', Derived_CACB_chem_shift_tot_num)

            content_subtype = 'procs_restraint'

            Derived_1H_chem_shift_tot_num = 0
            if content_subtype in self._reg.mr_sf_dict_holder:
                for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:
                    Derived_1H_chem_shift_tot_num += sf_item['id']

            if Derived_1H_chem_shift_tot_num > 0:
                cst_sf.add_tag('Derived_1H_chem_shift_tot_num', Derived_1H_chem_shift_tot_num)

            content_subtype = 'dist_restraint'

            Derived_photo_cidnps_tot_num = 0
            if content_subtype in self._reg.mr_sf_dict_holder:
                for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:
                    sf = sf_item['saveframe']
                    potential_type = get_first_sf_tag(sf, 'Potential_type')
                    if 'lower' in potential_type:
                        continue
                    constraint_type = get_first_sf_tag(sf, 'Constraint_type')
                    if constraint_type != 'photo cidnp':
                        continue
                    Derived_photo_cidnps_tot_num += sf_item['id']

            if Derived_photo_cidnps_tot_num > 0:
                cst_sf.add_tag('Derived_photo_cidnps_tot_num', Derived_photo_cidnps_tot_num)

            Derived_paramag_relax_tot_num = 0
            if content_subtype in self._reg.mr_sf_dict_holder:
                for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:
                    sf = sf_item['saveframe']
                    potential_type = get_first_sf_tag(sf, 'Potential_type')
                    if 'lower' in potential_type:
                        continue
                    constraint_type = get_first_sf_tag(sf, 'Constraint_type')
                    if constraint_type != 'paramagnetic relaxation':
                        continue
                    Derived_paramag_relax_tot_num += sf_item['id']

            if Derived_paramag_relax_tot_num > 0:
                cst_sf.add_tag('Derived_paramag_relax_tot_num', Derived_paramag_relax_tot_num)

            content_subtype = 'other_restraint'

            if content_subtype in self._reg.mr_sf_dict_holder:
                Protein_other_tot_num = NA_other_tot_num = 0
                for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:
                    lp = sf_item['loop']
                    lp_tags = lp['tags']
                    lp_data = lp['data']

                    auth_asym_id_col = lp_tags.index('auth_asym_id') if 'auth_asym_id' in lp_tags\
                        else lp_tags.index('auth_asym_id_1') if 'auth_asym_id_1' in lp_tags\
                        else lp_tags.index('plane_1_auth_asym_id_1')
                    auth_seq_id_col = lp_tags.index('auth_seq_id') if 'auth_seq_id' in lp_tags\
                        else lp_tags.index('auth_seq_id_1') if 'auth_seq_id_1' in lp_tags\
                        else lp_tags.index('plane_1_auth_seq_id_1')
                    auth_comp_id_col = lp_tags.index('auth_comp_id') if 'auth_comp_id' in lp_tags\
                        else lp_tags.index('auth_comp_id_1') if 'auth_comp_id_1' in lp_tags\
                        else lp_tags.index('plane_1_auth_comp_id_1')

                    for row in lp_data:
                        auth_asym_id = row[auth_asym_id_col]
                        try:
                            auth_seq_id = int(row[auth_seq_id_col])
                        except (ValueError, TypeError):
                            continue
                        auth_comp_id = row[auth_comp_id_col]

                        seq_key = (auth_asym_id, auth_seq_id, auth_comp_id)

                        if seq_key in auth_to_entity_type:
                            entity_type = auth_to_entity_type[seq_key]

                            if 'peptide' in entity_type:
                                Protein_other_tot_num += 1
                            elif 'nucleotide' in entity_type:
                                NA_other_tot_num += 1

                if Protein_other_tot_num > 0:
                    cst_sf.add_tag('Protein_other_tot_num', Protein_other_tot_num)
                if NA_other_tot_num > 0:
                    cst_sf.add_tag('NA_other_tot_num', NA_other_tot_num)

        lp_category = '_Constraint_file'
        cf_loop = pynmrstar.Loop.from_scratch(lp_category)

        cf_key_items = [{'name': 'ID', 'type': 'int'},
                        {'name': 'Constraint_filename', 'type': 'str'},
                        {'name': 'Software_ID', 'type': 'int'},
                        {'name': 'Software_label', 'type': 'str'},
                        {'name': 'Software_name', 'type': 'str'},
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

        # inspect _Software saveframes to extend Software_ID in _Constraint_file loop

        defined_software = []
        software_dict = {}
        software_id = 0

        if 'software' in self._reg.sf_category_list:
            for sf in master_entry.get_saveframes_by_category('software'):
                _id = get_first_sf_tag(sf, 'ID')
                _name = get_first_sf_tag(sf, 'Name')
                _code = get_first_sf_tag(sf, 'Sf_framecode')
                defined_software.append(_name)
                if _id not in EMPTY_VALUE and _name not in EMPTY_VALUE \
                   and (isinstance(_id, int) or _id.isdigit())\
                   and _name not in software_dict:
                    _id_ = int(_id) if isinstance(_id, str) else _id
                    software_dict[_name] = (_id_, _code)
                    software_id = max(software_id, _id_)

        file_name_dict = {}
        file_id = block_id = 0

        for content_subtype in self._reg.mr_content_subtypes:
            if self._reg.mr_sf_dict_holder is not None and content_subtype in self._reg.mr_sf_dict_holder:
                for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:
                    row = [None] * len(tags)

                    sf = sf_item['saveframe']
                    file_name = get_first_sf_tag(sf, 'Data_file_name')
                    if file_name not in file_name_dict:
                        file_id += 1
                        file_name_dict[file_name] = file_id
                    row[0], row[1] = file_name_dict[file_name], file_name if len(file_name) > 0 else None
                    sf_allowed_tags = SF_ALLOWED_TAGS[file_type][content_subtype]
                    if 'Constraint_file_ID' in sf_allowed_tags:
                        sf.add_tag('Constraint_file_ID', file_name_dict[file_name], update=True)
                    _name = get_first_sf_tag(sf, 'Sf_framecode').split('_')[0]
                    _name_ = _name.upper()
                    if _name == _name_:
                        _name = getPdbxNmrSoftwareName(_name_)
                        if _name in software_dict:
                            row[2], row[3], row[4] =\
                                software_dict[_name][0], \
                                f'${software_dict[_name][1]}' if _name in defined_software else None, \
                                _name
                        else:
                            software_id += 1
                            _code = f'software_{software_id}'
                            row[2], row[3], row[4] =\
                                software_id, f'${_code}' if _name in defined_software else None, \
                                _name
                            software_dict[_name] = (software_id, _code)
                    if 'Block_ID' in sf_allowed_tags:
                        block_id += 1
                        _block_id = str(block_id)
                        sf.add_tag('Block_ID', _block_id, update=True)
                        row[5] = _block_id
                    constraint_type = sf_item['constraint_type']
                    if constraint_type == 'planarity':
                        try:
                            for item in sf_item['loop']['data']:
                                auth_comp_id = item[4]
                                peptide, nucleotide, _ = self._reg.csStat.getTypeOfCompId(auth_comp_id)
                                if peptide:
                                    constraint_type = 'protein peptide planarity'
                                    break
                                if nucleotide:
                                    constraint_type = 'nucleic acid base planarity'
                        except (KeyError, IndexError):
                            pass

                    if constraint_type == 'scalar J-coupling':  # DAOTHER-9471
                        constraint_type = 'coupling constant'
                    if constraint_type == 'angle database':  # DAOTHER-9471
                        constraint_type = 'protein dihedral angle'
                    if constraint_type == 'paramagnetic relaxation enhancement':  # DAOTHER-9471
                        constraint_type = 'line broadening'
                    constraint_subtype = (get_first_sf_tag(sf, 'Constraint_type') if content_subtype != 'other_restraint'
                                          else get_first_sf_tag(sf, 'Definition'))
                    if len(constraint_subtype) == 0:
                        constraint_subtype = None
                    if content_subtype == 'auto_relax_restraint'\
                       and get_first_sf_tag(sf, 'Common_relaxation_type_name') == 'paramagnetic relaxation enhancement':
                        constraint_subtype = 'PRE'
                    if sf_item['file_type'] == 'nm-res-sax':
                        constraint_subtype = 'SAXS'
                    if constraint_subtype is not None and constraint_subtype == 'RDC':
                        constraint_type = 'dipolar coupling'  # DAOTHER-9471
                    if constraint_type == 'scalar J-coupling':  # DAOTHER-9471
                        constraint_type, constraint_subtype = 'coupling constant', 'J-couplings'
                    if constraint_type in ('hydrogen bond', 'disulfide bond', 'diselenide bond'):  # DAOTHER-9471
                        constraint_type, constraint_subtype = 'distance', constraint_type
                    if constraint_type in ('carbon chemical shift', 'proton chemical shift'):  # DAOTHER-9471
                        constraint_type, constraint_subtype = 'chemical shift', f'{constraint_type}s'
                    if constraint_type == 'floating chiral stereo assignments':  # DAOTHER-9471
                        constraint_type, constraint_subtype = 'chemical shift', constraint_type
                    if constraint_type == 'NOESY peak volume':  # DAOTHER-9471
                        constraint_type, constraint_subtype = 'peak volume', 'NOE'
                    if constraint_type == 'radius of gyration':  # DAOTHER-9471
                        constraint_type, constraint_subtype = 'coordinate geometry', constraint_type
                    if constraint_type == 'small angle X-ray scattering':  # DAOTHER-9471
                        constraint_type, constraint_subtype = 'coordinate geometry', 'SAXS'

                    if constraint_subtype is not None:
                        if 'prochirality' in constraint_subtype:  # DAOTHER-9471
                            constraint_subtype = 'prochirality'
                        if 'NCS restraint' in constraint_subtype:  # DAOTHER-9471
                            constraint_subtype = 'symmetry'
                        if constraint_subtype == 'angle restraint':  # DAOTHER-9471
                            constraint_subtype = 'general angle'
                        if constraint_subtype == 'chemical shift perturbation':  # DAOTHER-9471
                            constraint_subtype = 'CSP'
                        if constraint_subtype == 'covalent bond linkage':  # DAOTHER-9471
                            constraint_subtype = 'covalent bond'
                        if constraint_subtype == 'paramagnetic relaxation':  # DAOTHER-9471
                            constraint_subtype = 'PRE'
                        if 'planality' in constraint_subtype:  # DAOTHER-9471
                            constraint_subtype = None
                        if 'radius of gyration' in constraint_subtype:  # DAOTHER-9471
                            constraint_type, constraint_subtype = 'coordinate geometry', constraint_type
                        if constraint_subtype == 'unknown':  # DAOTHER-9471
                            constraint_subtype = 'Not applicable'

                    constraint_subsubtype = sf_item.get('constraint_subsubtype')

                    try:
                        id_col = sf_item['loop'].tags.index('ID')
                        count = 0

                        prev_id = -1
                        for _row in sf_item['loop']:
                            _id = int(_row[id_col])
                            if _id == prev_id:
                                continue
                            prev_id = _id
                            count += 1

                        sf_item['id'] = count
                    except AttributeError:
                        pass

                    row[6], row[7], row[8], row[9] =\
                        constraint_type, constraint_subtype, constraint_subsubtype, sf_item['id']
                    row[10], row[11] = 1, self._reg.entry_id

                    cf_loop.add_data(row)

        ext_mr_sf_holder = []

        if AR_FILE_PATH_LIST_KEY in self._reg.inputParamDict:

            fileListId = self._reg.file_path_list_len

            for ar in self._reg.inputParamDict[AR_FILE_PATH_LIST_KEY]:
                file_path = ar['file_name']

                input_source = self._reg.report.input_sources[fileListId]
                input_source_dic = input_source.get()

                mr_file_type = input_source_dic['file_type']

                fileListId += 1

                if mr_file_type != 'nm-res-oth':
                    continue

                original_file_name = None
                if 'original_file_name' in input_source_dic:
                    if input_source_dic['original_file_name'] is not None:
                        original_file_name = os.path.basename(input_source_dic['original_file_name'])

                self._reg.list_id_counter = incListIdCounter(None, self._reg.list_id_counter)

                list_id = self._reg.list_id_counter['other_restraint']

                sf_framecode = f'NMR_restraints_not_interpreted_{list_id}'

                dir_path = os.path.dirname(file_path)

                details = data_format = None

                unknown_mr_desc = os.path.join(dir_path, '.entry_with_unknown_mr')
                if os.path.exists(unknown_mr_desc):
                    with open(unknown_mr_desc, 'r', encoding='utf-8') as ifh:
                        details = ifh.read().splitlines()
                        data_format = details[0].split(' ')[0]
                        if not data_format.isupper():
                            data_format = None
                        break

                sf = getSaveframe(None, sf_framecode, list_id, self._reg.entry_id, original_file_name,
                                  constraintType=details)

                file_id += 1
                sf.add_tag('Constraint_file_ID', file_id, update=True)

                block_id += 1
                _block_id = str(block_id)
                sf.add_tag('Block_ID', _block_id, update=True)

                row = [None] * len(tags)
                row[0], row[1], row[5] = file_id, original_file_name, _block_id

                if data_format is not None and data_format != 'UNKNOWN':
                    if data_format in software_dict:
                        row[2], row[3], row[4] =\
                            software_dict[data_format][0], \
                            f'${software_dict[data_format][1]}' if data_format in defined_software else None, \
                            data_format
                    else:
                        software_id += 1
                        _code = f'software_{software_id}'
                        row[2], row[3], row[4] =\
                            software_id, \
                            f'${_code}' if data_format in defined_software else None, \
                            data_format
                        software_dict[data_format] = (software_id, _code)

                sel_res_cif_file = self.testPathWithSuffix(os.path.join(dir_path, file_path), '-selected-as-res-cif', True)
                sel_res_oth_file = self.testPathWithSuffix(os.path.join(dir_path, file_path), '-selected-as-res-oth', True)

                if os.path.exists(sel_res_cif_file):
                    data_format = 'mmCIF'

                sf.add_tag('Text_data_format', data_format)

                with open(file_path, 'r', encoding='ascii', errors='ignore') as ifh:
                    sf.add_tag('Text_data', ifh.read())

                row[10], row[11] = 1, self._reg.entry_id

                # cf_loop.add_data(row)

                ext_mr_sf_holder.append(sf)

                if not os.path.exists(sel_res_cif_file) and not os.path.exists(sel_res_oth_file):

                    if self._reg.internal_mode:

                        err = f"Uninterpreted restraints are stored in {sf_framecode} saveframe as raw text format. "\
                            "@todo: It needs to be reviewed."

                        self._reg.report.error.appendDescription('internal_error',
                                                                 f"+{self.__class_name__}.mergeLegacyData() ++ Error  - {err}")

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.mergeLegacyData() ++ Error  - {err}\n")

                    else:

                        file_name = input_source_dic['file_name']
                        if file_name != original_file_name and original_file_name is not None:
                            file_name = f"{original_file_name} ({file_name})"

                        warn = f"We could not identify restraint file format of {file_name!r}. "\
                               "In order to add file format support in the future, "\
                               "the contents is temporarily stored as-is in the _Other_data_type_list.Text_data tag "\
                               "and will be converted during future data remediation "\
                               "if the data matches a known restraint format."

                        self._reg.report.warning.appendDescription('unsupported_mr_data',
                                                                   {'file_name': file_name, 'description': warn,
                                                                    'inheritable': True})

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.mergeLegacyData() ++ Warning  - {warn}\n")

        cst_sf.add_loop(cf_loop)

        if self._reg.orig_cst_sf is None:
            if len(cf_loop) > 0:
                master_entry.add_saveframe(cst_sf)
        else:
            _data_file_name = get_first_sf_tag(self._reg.orig_cst_sf, 'Data_file_name')
            replace_data_file_name = False
            if len(_data_file_name) > 0:
                replace_data_file_name = any(True for _file_name in _data_file_name.split(',')
                                             if INTNL_ANY_MR_FILE_NAME_PAT.match(_file_name)
                                             or PDB_MR_FILE_NAME_PAT.match(_file_name))
            for tag in cst_sf.tags:
                if tag[0] == 'Data_file_name' and not replace_data_file_name:
                    continue
                set_sf_tag(self._reg.orig_cst_sf, tag[0], tag[1])
            has_cf_loop = replace_cf_loop = False
            try:
                _cf_loop = self._reg.orig_cst_sf.get_loop('_Constraint_file')
                has_cf_loop = True
                if len(_cf_loop) != len(cf_loop) and len(cf_loop) > 0:
                    replace_cf_loop = True
                else:
                    tags = ['ID', 'Software_name', 'Block_ID',
                            'Constraint_type', 'Constraint_subtype', 'Constraint_subsubtype', 'Constraint_number']
                    _dat = _cf_loop.get_tag(tags)
                    dat = cf_loop.get_tag(tags)
                    for _row, row in zip(_dat, dat):
                        _row = [_col if isinstance(_col, str) else str(_col) for _col in _row]
                        row = [col if isinstance(col, str) else str(col) for col in row]
                        if _row != row:
                            replace_cf_loop = True
                            break
                    if not replace_cf_loop:
                        if all(_row[2] in EMPTY_VALUE for _row in _dat):
                            block_id_col = _cf_loop.tags.index('Block_ID')
                            for idx, _row in enumerate(_dat, start=1):
                                _cf_loop.data[idx][block_id_col] = idx
                        tags = ['Software_ID', 'Software_label', 'Software_name']
                        _dat = _cf_loop.get_tag(tags)
                        dat = cf_loop.get_tag(tags)
                        software_dict = {}
                        for row in dat:
                            if row[2] not in software_dict:
                                software_dict[row[2]] = (row[0], row[1])
                        software_id_col = _cf_loop.tags.index('Software_ID')
                        software_label_col = _cf_loop.tags.index('Software_label')
                        for idx, _row in enumerate(_dat):
                            if _row[2] in software_dict:
                                _cf_loop.data[idx][software_id_col] = software_dict[_row[2]][0]
                                _cf_loop.data[idx][software_label_col] = software_dict[_row[2]][1]
                        tags = ['Constraint_filename']
                        _dat = _cf_loop.get_tag(tags)
                        dat = cf_loop.get_tag(tags)
                        _filename_col = _cf_loop.tags.index('Constraint_filename')
                        filename_col = cf_loop.tags.index('Constraint_filename')
                        for idx, _row in enumerate(_dat):
                            if INTNL_ANY_MR_FILE_NAME_PAT.match(_row) or PDB_MR_FILE_NAME_PAT.match(_row):
                                _cf_loop.data[idx][_filename_col] = cf_loop.data[idx][filename_col]
            except KeyError:
                replace_cf_loop = True
            if replace_cf_loop:
                if has_cf_loop:
                    del self._reg.orig_cst_sf[_cf_loop]
                self._reg.orig_cst_sf.add_loop(cf_loop)

            master_entry.add_saveframe(self._reg.orig_cst_sf)

        # resolve CYANA distance subtype

        dat = cf_loop.get_tag(['Constraint_filename', 'Software_name', 'Block_ID',
                               'Constraint_type', 'Constraint_subtype', 'Constraint_subsubtype'])

        for dist_subtype in ['NOE', 'ROE', 'hydrogen bond', 'disulfide bond', 'diselenide bond']:
            cyana_subtype = {}
            for row in dat:
                if row[1] == 'CYANA' and row[3] == 'distance' and row[4] == dist_subtype and row[5] == 'simple':
                    if row[0] not in cyana_subtype or row[2] in EMPTY_VALUE:
                        cyana_subtype[row[0]] = []
                    cyana_subtype[row[0]].append(row[2] if isinstance(row[2], str) else str(row[2]))

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
                                if row[1] == 'CYANA' and row[3] == 'distance' and row[4] == dist_subtype and row[5] == 'simple'\
                                   and (row[2] if isinstance(row[2], str) else str(row[2])) == block_id:
                                    cf_loop.data[idx][cf_loop.tags.index('Constraint_subtype')] = f'{dist_subtype} (upper bound)'

        update_data_file_name = False
        data_file_name_map = {}
        removed_sf_names = []
        resolved_sf_name_prefixes = []

        for content_subtype in self._reg.mr_content_subtypes:
            if self._reg.mr_sf_dict_holder is not None and content_subtype in self._reg.mr_sf_dict_holder:
                if content_subtype != 'other_restraint':
                    lp_category = LP_CATEGORIES[file_type][content_subtype]
                    for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:
                        sf = sf_item['saveframe']
                        sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')

                        if content_subtype == 'fchiral_restraint':
                            set_sf_tag(sf, 'Stereo_assigned_count', sf_item['id'])

                        if 'XPLOR-NIH_' in sf_framecode or sf_framecode.startswith('CNS'):
                            if 'XPLOR-NIH' in sf_framecode:
                                alt_sf_framecode = f'XPLOR-NIH/CNS{sf_framecode[9:]}'
                            else:
                                alt_sf_framecode = f'XPLOR-NIH/{sf_framecode}'

                        else:
                            alt_sf_framecode = sf_framecode

                        if any(True for _sf in master_entry.frame_list if _sf.name in (sf_framecode, alt_sf_framecode)):

                            if self._reg.internal_mode or self._reg.bmrb_only:
                                _sf = next(_sf for _sf in master_entry.frame_list if _sf.name in (sf_framecode, alt_sf_framecode))
                                _data_file_name = get_first_sf_tag(_sf, 'Data_file_name')
                                data_file_name = get_first_sf_tag(sf, 'Data_file_name')
                                if len(_data_file_name) > 0 and _data_file_name != data_file_name and self._reg.internal_mode:
                                    data_file_name_map[data_file_name] = _data_file_name
                                    set_sf_tag(sf, 'Data_file_name', _data_file_name)
                                    update_data_file_name = True

                                    fileListId = self._reg.file_path_list_len

                                    for ar in self._reg.inputParamDict[AR_FILE_PATH_LIST_KEY]:

                                        input_source = self._reg.report.input_sources[fileListId]
                                        input_source_dic = input_source.get()

                                        fileListId += 1

                                        ar_file_type = input_source_dic['file_type']

                                        if not ar_file_type.startswith('nm-res') or ar_file_type == 'nm-res-mr':
                                            continue

                                        if 'original_file_name' in ar and ar['original_file_name'] not in EMPTY_VALUE:
                                            if ar['original_file_name'] == data_file_name:
                                                ar['original_file_name'] = _data_file_name
                                                update_data_file_name = True
                                                break

                                        elif os.path.basename(ar['file_name']) == data_file_name:
                                            ar['original_file_name'] = _data_file_name
                                            update_data_file_name = True
                                            break

                                if any(True for _sf in master_entry.frame_list if _sf.name == sf_framecode):
                                    master_entry.remove_saveframe(sf_framecode)
                                    removed_sf_names.append(sf_framecode)
                                else:
                                    master_entry.remove_saveframe(alt_sf_framecode)
                                    removed_sf_names.append(alt_sf_framecode)

                            else:

                                err = f"Couldn't add a saveframe with name {sf_framecode!r} "\
                                      f"since a saveframe with that name already exists in {original_file_name!r} file. "\
                                      f"Please remove {sf_framecode!r} saveframe "\
                                      f"and re-upload the {READABLE_FILE_TYPE[file_type]} file."

                                self._reg.report.error.appendDescription('format_issue',
                                                                         {'file_name': _data_file_name, 'description': err})

                                self._reg.log.write(f"+{self.__class_name__}.mergeLegacyData() ++ Error  - "
                                                    f"{_data_file_name} {err}\n")
                                continue

                        elif self._reg.internal_mode or self._reg.bmrb_only:

                            try:

                                data_file_name = get_first_sf_tag(sf, 'Data_file_name')
                                sf_framecode_prefix = '_'.join(sf_framecode.split('_')[:-1])
                                sf_framecode_suffix = int(sf_framecode[len(sf_framecode_prefix) + 1:])

                                if sf_framecode_prefix not in resolved_sf_name_prefixes\
                                   and any(True for _sf in master_entry.frame_list if _sf.name.startswith(sf_framecode_prefix)):
                                    resolved_sf_name_prefixes.append(sf_framecode_prefix)

                                    for sf_item_ in self._reg.mr_sf_dict_holder[content_subtype]:
                                        sf_ = sf_item_['saveframe']
                                        sf_framecode_ = get_first_sf_tag(sf_, 'Sf_framecode')

                                        if not sf_framecode_.startswith(sf_framecode_prefix):
                                            continue

                                        sf_framecode_suffix_ = int(sf_framecode_[len(sf_framecode_prefix) + 1:])

                                        if sf_framecode_suffix_ > sf_framecode_suffix:
                                            continue

                                        if 'XPLOR-NIH_' in sf_framecode_ or sf_framecode_.startswith('CNS'):
                                            if 'XPLOR-NIH' in sf_framecode_:
                                                alt_sf_framecode_ = f'XPLOR-NIH/CNS{sf_framecode_[9:]}'
                                            else:
                                                alt_sf_framecode_ = f'XPLOR-NIH/{sf_framecode_}'

                                        else:
                                            alt_sf_framecode_ = sf_framecode_

                                        if any(True for _sf in master_entry.frame_list
                                               if _sf.name in (sf_framecode_, alt_sf_framecode_)):
                                            continue

                                        for _sf in master_entry.frame_list:
                                            _sf_framecode_ = get_first_sf_tag(_sf, 'Sf_framecode')

                                            if _sf_framecode_ == sf_framecode_\
                                               or not _sf_framecode_.startswith(sf_framecode_prefix)\
                                               or _sf_framecode_ in removed_sf_names:
                                                continue

                                            _sf_framecode_suffix_ = int(_sf_framecode_[len(sf_framecode_prefix) + 1:])

                                            if _sf_framecode_suffix_ <= sf_framecode_suffix\
                                               and constraint_subtype == 'dist_restraint':
                                                continue

                                            _data_file_name = get_first_sf_tag(_sf, 'Data_file_name')
                                            if len(_data_file_name) > 0 and _data_file_name != data_file_name\
                                               and self._reg.internal_mode:
                                                data_file_name_map[data_file_name] = _data_file_name
                                                set_sf_tag(sf, 'Data_file_name', _data_file_name)
                                                update_data_file_name = True

                                                fileListId = self._reg.file_path_list_len

                                                for ar in self._reg.inputParamDict[AR_FILE_PATH_LIST_KEY]:

                                                    input_source = self._reg.report.input_sources[fileListId]
                                                    input_source_dic = input_source.get()

                                                    fileListId += 1

                                                    ar_file_type = input_source_dic['file_type']

                                                    if not ar_file_type.startswith('nm-res') or ar_file_type == 'nm-res-mr':
                                                        continue

                                                    if 'original_file_name' in ar and ar['original_file_name'] not in EMPTY_VALUE:
                                                        if ar['original_file_name'] == data_file_name:
                                                            ar['original_file_name'] = _data_file_name
                                                            update_data_file_name = True
                                                            break

                                                    elif os.path.basename(ar['file_name']) == data_file_name:
                                                        ar['original_file_name'] = _data_file_name
                                                        update_data_file_name = True
                                                        break

                                            master_entry.remove_saveframe(_sf.name)

                            except ValueError:
                                pass

                        master_entry.add_saveframe(sf)
                        removed_sf_names.append(sf_framecode)

                        _lp = next((lp for lp in self._reg.lp_data[content_subtype] if lp['sf_framecode'] == sf_framecode), None)
                        if _lp is not None:
                            self._reg.lp_data[content_subtype].remove(_lp)
                            data_file_name = get_first_sf_tag(sf, 'Data_file_name')
                            self._reg.dpV.testDataConsistencyInLoop(0, data_file_name, 'nmr-star', content_subtype,
                                                                    sf, sf_framecode, lp_category, sf_item['list_id'])

                else:
                    for sf_item in self._reg.mr_sf_dict_holder[content_subtype]:
                        sf = sf_item['saveframe']
                        sf_framecode = sf.get_tag('Sf_framecode')[0]

                        other_data = {'entry_id': self._reg.entry_id,
                                      'saveframes': [{'name': sf_framecode,
                                                      'category': 'undefined',
                                                      'tag_prefix': '?',
                                                      'tags': [['Sf_category', 'undefined'],
                                                               ['Sf_framecode', sf_framecode],
                                                               ['Definition', sf.get_tag('Definition')[0]],
                                                               ['Data_file_name', sf.get_tag('Data_file_name')[0]],
                                                               ['ID', sf.get_tag('ID')[0]],
                                                               ['Entry_ID', self._reg.entry_id]
                                                               ],
                                                      'loops': [{'category': 'unknown',
                                                                 'tags': sf_item['loop']['tags'],
                                                                 'data': sf_item['loop']['data']
                                                                 }]
                                                      }]
                                      }

                        sf.add_tag('Text_data_format', 'json')
                        sf.add_tag('Text_data', getPrettyJson(other_data))

                        if 'XPLOR-NIH_' in sf_framecode or sf_framecode.startswith('CNS'):
                            if 'XPLOR-NIH' in sf_framecode:
                                alt_sf_framecode = f'XPLOR-NIH/CNS{sf_framecode[9:]}'
                            else:
                                alt_sf_framecode = f'XPLOR-NIH/{sf_framecode}'

                        else:
                            alt_sf_framecode = sf_framecode

                        if any(True for _sf in master_entry.frame_list if _sf.name in (sf_framecode, alt_sf_framecode)):

                            if self._reg.internal_mode or self._reg.bmrb_only:
                                _sf = next(_sf for _sf in master_entry.frame_list if _sf.name in (sf_framecode, alt_sf_framecode))
                                _data_file_name = get_first_sf_tag(_sf, 'Data_file_name')
                                data_file_name = get_first_sf_tag(sf, 'Data_file_name')
                                if len(_data_file_name) > 0 and _data_file_name != data_file_name and self._reg.bmrb_only:
                                    data_file_name_map[data_file_name] = _data_file_name
                                    set_sf_tag(sf, 'Data_file_name', _data_file_name)
                                    update_data_file_name = True

                                    fileListId = self._reg.file_path_list_len

                                    for ar in self._reg.inputParamDict[AR_FILE_PATH_LIST_KEY]:

                                        input_source = self._reg.report.input_sources[fileListId]
                                        input_source_dic = input_source.get()

                                        fileListId += 1

                                        ar_file_type = input_source_dic['file_type']

                                        if not ar_file_type.startswith('nm-res') or ar_file_type == 'nm-res-mr':
                                            continue

                                        if 'original_file_name' in ar and ar['original_file_name'] not in EMPTY_VALUE:
                                            if ar['original_file_name'] == data_file_name:
                                                ar['original_file_name'] = _data_file_name
                                                update_data_file_name = True
                                                break

                                        elif os.path.basename(ar['file_name']) == data_file_name:
                                            ar['original_file_name'] = _data_file_name
                                            update_data_file_name = True
                                            break

                                if any(True for _sf in master_entry.frame_list if _sf.name == sf_framecode):
                                    master_entry.remove_saveframe(sf_framecode)
                                else:
                                    master_entry.remove_saveframe(alt_sf_framecode)

                            else:

                                err = f"Couldn't add a saveframe with name {sf_framecode!r} "\
                                      f"since a saveframe with that name already exists in {original_file_name!r} file. "\
                                      f"Please remove {sf_framecode!r} saveframe "\
                                      f"and re-upload the {READABLE_FILE_TYPE[file_type]} file."

                                self._reg.report.error.appendDescription('format_issue',
                                                                         {'file_name': _data_file_name, 'description': err})

                                self._reg.log.write(f"+{self.__class_name__}.mergeLegacyData() ++ Error  - "
                                                    f"{_data_file_name} {err}\n")
                                continue

                        master_entry.add_saveframe(sf)

        for sf in ext_mr_sf_holder:

            if self._reg.internal_mode and any(True for _sf in master_entry.frame_list if _sf.name == sf.name):
                continue

            master_entry.add_saveframe(sf)

        if update_data_file_name:

            for idx, row in enumerate(cf_loop):
                if row[1] in data_file_name_map:
                    cf_loop[idx][1] = data_file_name_map[row[1]]

            fileListId = self._reg.file_path_list_len

            file_names = []

            for ar in self._reg.inputParamDict[AR_FILE_PATH_LIST_KEY]:

                input_source = self._reg.report.input_sources[fileListId]
                input_source_dic = input_source.get()

                fileListId += 1

                ar_file_type = input_source_dic['file_type']

                if not ar_file_type.startswith('nm-res') or ar_file_type == 'nm-res-mr':
                    continue

                if 'original_file_name' in ar and ar['original_file_name'] not in EMPTY_VALUE:
                    file_name = ar['original_file_name']
                else:
                    file_name = input_source_dic['file_name']

                file_names.append(retrieveOriginalFileName(file_name))

            for content_subtype in self._reg.mr_sf_dict_holder:
                if content_subtype != 'other_restraint':
                    sf_category = SF_CATEGORIES[file_type][content_subtype]
                    for sf in master_entry.get_saveframes_by_category(sf_category):
                        data_file_name = get_first_sf_tag(sf, 'Data_file_name')
                        if data_file_name in EMPTY_VALUE:
                            continue
                        sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')
                        block_id = get_first_sf_tag(sf, "Block_ID")
                        data_file_name = retrieveOriginalFileName(data_file_name)
                        if data_file_name not in file_names:
                            file_names.append(data_file_name)
                        if block_id not in EMPTY_VALUE:
                            if isinstance(block_id, str) and block_id.isdigit():
                                pass
                            elif isinstance(block_id, int):
                                block_id = str(block_id)
                            else:
                                continue
                            dat = cf_loop.get_tag(['Constraint_filename', 'Software_name', 'Block_ID'])
                            for idx, row in enumerate(dat):
                                if row[2] != block_id or row[1] in EMPTY_VALUE or row[1] not in sf_framecode:
                                    continue
                                if row[0] != data_file_name:
                                    cf_loop.data[idx][cf_loop.tags.index('Constraint_filename')] = data_file_name

            if len(file_names) > 0:
                set_sf_tag(cst_sf, 'Data_file_name', ','.join(sorted(file_names)))

        self._mergeStrPk()

        # if self._reg.merge_any_pk_as_is:  # DAOTHER-7407 enabled until Phase 2 release
        self._mergeAnyPkAsIs()

        if self._reg.bmrb_only and self._reg.internal_mode:
            self.performBmrbJAnnTasks()

        try:

            content_subtype = 'entry_info'

            # update _Data_set/Datum loop

            sf_category = SF_CATEGORIES[file_type][content_subtype]

            self._reg.sf_category_list, self._reg.lp_category_list = self._reg.nefT.get_inventory_list(master_entry)

            has_entry_info = sf_category in self._reg.sf_category_list

            if has_entry_info:
                sf = master_entry.get_saveframes_by_category(sf_category)[0]

            else:
                sf_framecode = 'entry_information'

                sf = pynmrstar.Saveframe.from_scratch(sf_framecode)
                sf.set_tag_prefix('_Entry')
                sf.add_tag('Sf_category', sf_framecode)
                sf.add_tag('Sf_framecode', sf_framecode)
                sf.add_tag('ID', self._reg.entry_id)

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

            if not has_entry_info:
                master_entry.add_saveframe(sf)

        except IndexError as e:
            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.mergeLegacyData() ++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.mergeLegacyData() ++ Error  - {str(e)}\n")

        self._reg.list_id_counter = None
        self._reg.mr_sf_dict_holder = None
        self._reg.pk_sf_holder = None

        gc.collect(2)

        master_entry = self._reg.c2S.normalize_str(master_entry)

        master_entry.write_to_file(self._reg.dstPath,
                                   show_comments=(self._reg.bmrb_only and self._reg.internal_mode),
                                   skip_empty_loops=True, skip_empty_tags=False)

        # check inventory again

        self._reg.sf_category_list, self._reg.lp_category_list = self._reg.nefT.get_inventory_list(master_entry)

        lp_counts = {t: 0 for t in NMR_CONTENT_SUBTYPES}

        for lp_category in self._reg.lp_category_list:
            if lp_category in LP_CATEGORIES[file_type].values():
                lp_counts[[k for k, v in LP_CATEGORIES[file_type].items() if v == lp_category][0]] += 1

        mr_loops = 0

        for content_subtype in self._reg.mr_content_subtypes:
            if content_subtype in lp_counts:
                mr_loops += lp_counts[content_subtype]

        if mr_loops == 0 and not self._reg.validation_server and not self._reg.mr_has_valid_star_restraint:

            if 'other_data_types' not in self._reg.sf_category_list:

                mr_file_names = []

                for fileListId in range(self._reg.cs_file_path_list_len, self._reg.file_path_list_len):

                    input_source = self._reg.report.input_sources[fileListId]
                    input_source_dic = input_source.get()

                    file_type = input_source_dic['file_type']

                    if file_type != 'nmr-star':
                        continue

                    mr_file_names.append(input_source_dic['file_name'])

                if AR_FILE_PATH_LIST_KEY in self._reg.inputParamDict:

                    fileListId = self._reg.file_path_list_len

                    for ar in self._reg.inputParamDict[AR_FILE_PATH_LIST_KEY]:

                        input_source = self._reg.report.input_sources[fileListId]
                        input_source_dic = input_source.get()

                        file_type = input_source_dic['file_type']

                        fileListId += 1

                        if file_type == 'nm-res-mr':
                            continue

                        mr_file_names.append(input_source_dic['file_name'])

                if len(mr_file_names) > 0:

                    desc = 'uploaded restraint file'\
                        + (f's, {mr_file_names}, are' if len(mr_file_names) > 1 else f', {mr_file_names[0]!r}, is')\
                        + ' consistent with the coordinates'

                    err = "Deposition of restraints used for the structure determination is mandatory. "\
                        f"Please verify {desc} and re-upload valid restraint file(s)."

                    self._reg.report.error.appendDescription('missing_mandatory_content',
                                                             {'file_name': os.path.basename(self._reg.dstPath),
                                                              'description': err})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.mergeLegacyData() ++ Error  - {err}\n")

        return True

    def performBmrbJAnnTasks(self, enforce: bool = False) -> bool:
        """ Perform a series of BMRBj specific annotation tasks.
            @note: this method requires additional software packages,
                   network access to PubMed, NCBI Taxonomy, BMRB-API, BMRB ETS, etc
        """

        if self._reg.combined_mode or not self._reg.remediation_mode or (self._reg.dstPath is None and not enforce):
            return True

        if len(self._reg.star_data) == 0 or self._reg.star_data[0] is None:
            return False

        try:
            from wwpdb.utils.nmr.ann.BmrbJAnnTasks import BmrbJAnnTasks  # pylint: disable=import-outside-toplevel
        except ImportError:
            try:
                from nmr.ann.BmrbJAnnTasks import BmrbJAnnTasks  # pylint: disable=import-outside-toplevel
            except ImportError:
                return False

        ann = BmrbJAnnTasks(self._reg)

        return ann.perform(self._reg.star_data[0])
