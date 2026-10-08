##
# File: NmrDpRemediationPolySeq.py
# Date: 17-Aug-2026
#
# Updates:
##
""" Remediation of the polymer sequence and the entity saveframe of NMR data.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.2"

import copy
import re
from typing import Optional, Tuple

import pynmrstar

try:
    from wwpdb.utils.nmr.NmrDpConstant import (SF_CATEGORIES,
                                               LP_CATEGORIES,
                                               INDEX_TAGS,
                                               DATA_ITEMS,
                                               SF_TAG_PREFIXES,
                                               AUX_LP_CATEGORIES,
                                               EMPTY_VALUE,
                                               STD_MON_DICT,
                                               UNKNOWN_RESIDUE,
                                               PARAMAGNETIC_ELEMENTS)
    from wwpdb.utils.nmr.AlignUtil import (getOneLetterCodeCanSequence,
                                           getOneLetterCodeSequence)
    from wwpdb.utils.nmr.CifToNmrStar import (get_first_sf_tag,
                                              set_sf_tag)
    from wwpdb.utils.nmr.NmrVrptUtility import write_as_pickle
    from wwpdb.utils.nmr.NmrDpRemediationBase import (NmrDpRemediationBase,
                                                      CCA_TAGS)
except ImportError:
    from nmr.NmrDpConstant import (SF_CATEGORIES,
                                   LP_CATEGORIES,
                                   INDEX_TAGS,
                                   DATA_ITEMS,
                                   SF_TAG_PREFIXES,
                                   AUX_LP_CATEGORIES,
                                   EMPTY_VALUE,
                                   STD_MON_DICT,
                                   UNKNOWN_RESIDUE,
                                   PARAMAGNETIC_ELEMENTS)
    from nmr.AlignUtil import (getOneLetterCodeCanSequence,
                               getOneLetterCodeSequence)
    from nmr.CifToNmrStar import (get_first_sf_tag,
                                  set_sf_tag)
    from nmr.NmrVrptUtility import write_as_pickle
    from nmr.NmrDpRemediationBase import (NmrDpRemediationBase,
                                          CCA_TAGS)


class NmrDpRemediationPolySeq(NmrDpRemediationBase):
    """ Remediation of the polymer sequence and the entity saveframe of NMR data.
    """
    __slots__ = ()

    def updatePolymerSequence(self) -> Tuple[bool, Optional[pynmrstar.Saveframe]]:
        """ Update polymer sequence.
        """

        input_source = self._reg.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        master_entry = self._reg.star_data[0]

        content_subtype = 'poly_seq'

        sf_category = SF_CATEGORIES[file_type][content_subtype]
        lp_category = LP_CATEGORIES[file_type][content_subtype]

        key_items = self._reg.key_items[file_type][content_subtype]
        data_items = DATA_ITEMS[file_type][content_subtype]

        orig_lp_data = None

        has_res_var_dat = has_nef_index = has_entry_id = False

        sf_framecode = 'assembly'

        for sf in master_entry.get_saveframes_by_category(sf_category):
            sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')

            try:

                _lp_category = '_Entity_assembly'

                _loop = sf.get_loop(_lp_category)

                tags = ['Conformational_isomer', 'Details']

                dat = _loop.get_tag(tags)

                for row in dat:
                    if row[0] == 'yes' and 'Conformational isomer' in row[1]:
                        return False, None

            except KeyError:
                pass

            orig_lp_data = next((lp['data'] for lp in self._reg.lp_data[content_subtype]
                                 if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode), None)

            if orig_lp_data is None:

                try:

                    orig_lp_data = self._reg.nefT.check_data(sf, lp_category, key_items, data_items, None, None, None,
                                                             enforce_allowed_tags=(file_type == 'nmr-star'),
                                                             excl_missing_data=self._reg.excl_missing_data)[0]

                except Exception:  # pylint: disable=broad-exception-caught
                    pass

            if orig_lp_data is not None and len(orig_lp_data) > 0:

                if file_type == 'nef':
                    if 'residue_variant' in orig_lp_data[0]:
                        if any(True for _row in orig_lp_data if _row['residue_variant'] not in EMPTY_VALUE):
                            has_res_var_dat = True

                else:
                    if 'Auth_variant_ID' in orig_lp_data[0]:
                        if any(True for _row in orig_lp_data if _row['Auth_variant_ID'] not in EMPTY_VALUE):
                            has_res_var_dat = True

                    if 'NEF_index' in orig_lp_data[0]:
                        if any(True for _row in orig_lp_data if _row['NEF_index'] not in EMPTY_VALUE):
                            has_nef_index = True

                    if 'Entry_ID' in orig_lp_data[0]:
                        has_entry_id = True

            elif not self._reg.has_star_entity and not self._reg.update_poly_seq and file_type == 'nef':  # DAOTHER-6694, 8751
                return False, None

        orig_asm_sf = None

        try:
            orig_asm_sf = master_entry.get_saveframes_by_category(sf_category)[0]
        except IndexError:
            pass

        entity_assembly = self._reg.caC['entity_assembly']

        if entity_assembly is None:
            return False, None

        components_ex_water = 0
        for item in entity_assembly:
            if isinstance(item['entity_copies'], int):
                components_ex_water += item['entity_copies']

        ligand_total = sum(len(item['label_asym_id'].split(',')
                               if 'fixed_label_asym_id' not in item else item['fixed_label_asym_id'].split(','))
                           for item in entity_assembly
                           if item['entity_type'] == 'non-polymer' and 'ION' not in item['entity_desc'])
        ion_total = sum(len(item['label_asym_id'].split(',')
                            if 'fixed_label_asym_id' not in item else item['fixed_label_asym_id'].split(','))
                        for item in entity_assembly
                        if item['entity_type'] == 'non-polymer' and 'ION' in item['entity_desc'])

        self._reg.sail_flag = False

        if self._reg.cR.hasItem('struct_keywords', 'text'):
            struct_keywords = self._reg.cR.getDictList('struct_keywords')
            text = struct_keywords[0]['text'].lower()
            if 'sail' in text or 'stereo-array isotope labeling' in text:
                self._reg.sail_flag = True

        if self._reg.cR.hasItem('pdbx_nmr_exptl_sample', 'isotopic_labeling'):
            exptl_sample = self._reg.cR.getDictList('pdbx_nmr_exptl_sample')
            for item in exptl_sample:
                text = item['isotopic_labeling'].lower()
                if 'sail' in text or 'stereo-array isotope labeling' in text:
                    self._reg.sail_flag = True
                    break

        chem_comp = self._reg.cR.getDictList('chem_comp')

        self._paramag = len(chem_comp) > 0\
            and any(True for cc in chem_comp if cc['type'] == 'non-poly' and cc['id'] in PARAMAGNETIC_ELEMENTS)

        has_cys = any(True for cc in chem_comp
                      if ((cc['type'] == 'L-peptide linking' and cc['id'] == 'CYS')
                          or (cc['type'] == 'D-peptide linking' and cc['id'] == 'DCY')))
        if has_cys:
            cys_total = 0
            for ps in self._reg.caC['polymer_sequence']:
                cys_total += ps['comp_id'].count('CYS') + ps['comp_id'].count('DCY')
            disul_cys = other_cys = 0
            if self._reg.cR.hasCategory('struct_conn'):
                bonds = self._reg.cR.getDictList('struct_conn')
                for bond in bonds:
                    auth_comp_id_1 = bond['ptnr1_auth_comp_id']
                    atom_id_1 = bond['ptnr1_label_atom_id']
                    auth_comp_id_2 = bond['ptnr2_auth_comp_id']
                    atom_id_2 = bond['ptnr2_label_atom_id']

                    if auth_comp_id_1 in ('CYS', 'DCY') and atom_id_1 == 'SG':
                        if auth_comp_id_2 in ('CYS', 'DCY') and atom_id_2 == 'SG':
                            disul_cys += 1
                        else:
                            other_cys += 1

                    if auth_comp_id_2 in ('CYS', 'DCY') and atom_id_2 == 'SG':
                        if auth_comp_id_1 in ('CYS', 'DCY') and atom_id_1 == 'SG':
                            disul_cys += 1
                        else:
                            other_cys += 1

            free_cys = cys_total - disul_cys - other_cys

            if free_cys > 0:
                if free_cys == cys_total:
                    thiol_state = 'all free'
                elif disul_cys > 0 and other_cys > 0:
                    thiol_state = 'free disulfide and other bound'
                elif other_cys == 0:
                    thiol_state = 'free and disulfide bound'
                else:
                    thiol_state = 'free and other bound'
            else:
                if disul_cys > 0 and other_cys > 0:
                    thiol_state = 'disulfide and other bound'
                elif other_cys == 0:
                    thiol_state = 'all disulfide bound'
                else:
                    thiol_state = 'all other bound'
        else:
            thiol_state = 'not present'

        formula_weight = 0.0
        for item in entity_assembly:
            fw = item['entity_fw']
            num = item['entity_copies']
            if isinstance(fw, float) and isinstance(num, int):
                formula_weight += fw * num
            else:
                formula_weight = '.'
                break

        ec_numbers = []
        for item in entity_assembly:
            if 'entity_ec' in item and item['entity_ec'] not in EMPTY_VALUE and item['entity_ec'] not in ec_numbers:
                ec_numbers.append(item['entity_ec'])
        if len(ec_numbers) == 0:
            ec_number = '.'
        else:
            ec_number = ','.join(ec_numbers)

        details = ''
        for item in entity_assembly:
            if 'entity_details' not in item:
                continue
            _details = item['entity_details'].strip().rstrip('\n')
            if _details in EMPTY_VALUE or _details + '\n' in details:
                continue
            if len(details.strip()) > 0:
                details += _details + '\n'
        if len(details) == 0:
            details = '.'
        else:
            details = details[:-1]
            if len(details) == 0:
                details = '.'

        asm_sf = pynmrstar.Saveframe.from_scratch(sf_framecode)
        asm_sf.set_tag_prefix(SF_TAG_PREFIXES[file_type][content_subtype])

        if file_type == 'nef':
            asm_sf.add_tag('sf_category', SF_CATEGORIES[file_type][content_subtype])
            asm_sf.add_tag('sf_framecode', sf_framecode)

        else:
            asm_sf.add_tag('Sf_category', SF_CATEGORIES[file_type][content_subtype])
            asm_sf.add_tag('Sf_framecode', sf_framecode)
            asm_sf.add_tag('Entry_ID', self._reg.entry_id)
            asm_sf.add_tag('ID', 1)
            assembly_name = self._reg.assembly_name
            if assembly_name in EMPTY_VALUE and self._reg.cR.hasItem('struct', 'pdbx_descriptor'):
                struct = self._reg.cR.getDictList('struct')
                assembly_name = struct[0]['pdbx_descriptor']
            asm_sf.add_tag('Name', assembly_name)
            asm_sf.add_tag('BMRB_code', None)
            asm_sf.add_tag('Number_of_components', components_ex_water if components_ex_water > 0 else None)
            asm_sf.add_tag('Organic_ligands', ligand_total if ligand_total > 0 else None)
            asm_sf.add_tag('Metal_ions', ion_total if ion_total > 0 else None)
            asm_sf.add_tag('Non_standard_bonds', None)  # filled 'yes' if the assembly contains non-standard bonds
            asm_sf.add_tag('Ambiguous_conformational_states', None)
            asm_sf.add_tag('Ambiguous_chem_comp_sites', None)
            asm_sf.add_tag('Molecules_in_chemical_exchange', None)  # filled 'yes' if conformational isomers exist
            asm_sf.add_tag('Paramagnetic', 'yes' if self._paramag else 'no')
            asm_sf.add_tag('Thiol_state', thiol_state)
            asm_sf.add_tag('Molecular_mass', f'{formula_weight:.3f}' if isinstance(formula_weight, float) else None)
            asm_sf.add_tag('Enzyme_commission_number', ec_number)
            asm_sf.add_tag('Details', details)
            asm_sf.add_tag('DB_query_date', None)
            asm_sf.add_tag('DB_query_revised_last_date', None)

        entity_type_of = {item['entity_id']: item['entity_type'] for item in entity_assembly}
        entity_total = {entity_id: len([item for item in entity_assembly if item['entity_id'] == entity_id])
                        for entity_id in entity_type_of.keys()}
        entity_count = {entity_id: 0 for entity_id in entity_type_of.keys()}

        if file_type == 'nmr-star':

            # refresh _Entity_assembly loop

            lp_category = '_Entity_assembly'

            ea_loop = pynmrstar.Loop.from_scratch(lp_category)

            ea_key_items = [{'name': 'ID', 'type': 'positive-int'},
                            {'name': 'Entity_assembly_name', 'type': 'str'},
                            {'name': 'Entity_ID', 'type': 'positive-int', 'default': '1'},
                            {'name': 'Entity_label', 'type': 'str'},
                            ]
            ea_data_items = [{'name': 'Asym_ID', 'type': 'str', 'mandatory': False},  # label_asym_id
                             {'name': 'PDB_chain_ID', 'type': 'str', 'mandatory': False},  # auth_asym_id
                             {'name': 'Experimental_data_reported', 'type': 'enum', 'mandatory': False,
                              'enum': ('no', 'yes')},
                             {'name': 'Physical_state', 'type': 'enum', 'mandatory': False,
                              'enum': ('native', 'denatured', 'molten globule', 'unfolded',
                                       'intrinsically disordered', 'partially disordered', 'na')},
                             {'name': 'Conformational_isomer', 'type': 'enum', 'mandatory': False,
                              'enum': ('no', 'yes')},
                             {'name': 'Chemical_exchange_state', 'type': 'enum', 'mandatory': False,
                              'enum': ('no', 'yes')},
                             {'name': 'Magnetic_equivalence_group_code', 'type': 'str', 'mandatory': False},
                             {'name': 'Role', 'type': 'str', 'mandatory': False},
                             {'name': 'Details', 'type': 'str', 'default': '.', 'mandatory': False},
                             {'name': 'Assembly_ID', 'type': 'pointer-index', 'mandatory': False,
                              'default': '1', 'default-from': 'parent'},
                             {'name': 'Entry_ID', 'type': 'str', 'mandatory': False}
                             ]

            tags = [f"{lp_category}.{_item['name']}" for _item in ea_key_items]
            tags.extend([f"{lp_category}.{_item['name']}" for _item in ea_data_items])

            ea_loop.add_tag(tags)

            for item in entity_assembly:
                entity_id = item['entity_id']
                entity_type = item['entity_type']
                entity_count[entity_id] += 1

                row = [None] * len(tags)

                row[0] = item['entity_assembly_id']
                row[1] = (f'entity_{entity_id}' + ('' if entity_total[entity_id] == 1 else f'_{entity_count[entity_id]}'))\
                    if entity_type not in ('non-polymer', 'water')\
                    else f"entity_{item['comp_id']}" + ('' if entity_total[entity_id] == 1 else f'_{entity_count[entity_id]}')
                item['entity_assembly_name'] = row[1]
                row[2] = item['entity_id']
                row[3] = f'$entity_{entity_id}' if entity_type not in ('non-polymer', 'water') else f"$entity_{item['comp_id']}"
                _label_asym_id = 'label_asym_id' if 'fixed_label_asym_id' not in item else 'fixed_label_asym_id'
                _auth_asym_id = 'auth_asym_id' if 'fixed_auth_asym_id' not in item else 'fixed_auth_asym_id'
                row[4] = item[_label_asym_id]
                row[5] = item[_auth_asym_id]
                if len(self._reg.label_asym_id_with_exptl_data) > 0:
                    if any(True for label_asym_id in item[_label_asym_id].split(',')
                           if label_asym_id in self._reg.label_asym_id_with_exptl_data):
                        row[6] = 'yes'
                # Physical_state
                # Conformational_isomer
                if len(self._reg.auth_asym_ids_with_chem_exch) > 0:
                    if any(True for auth_asym_id in item[_auth_asym_id].split(',')
                           if auth_asym_id in self._reg.auth_asym_ids_with_chem_exch.keys()):
                        row[8] = row[9] = 'yes'
                if entity_total[entity_id] > 0 and entity_type == 'polymer' and len(self._reg.label_asym_id_with_exptl_data) > 0:
                    equiv_entity_assemblies = [_item for _item in entity_assembly if _item['entity_id'] == entity_id]
                    _item = next((_item for _item in equiv_entity_assemblies
                                  if any(True for label_asym_id in _item[_label_asym_id].split(',')
                                         if label_asym_id in self._reg.label_asym_id_with_exptl_data)), None)
                    if _item is not None:
                        group_id = sorted(sorted(set(_item[_label_asym_id].split(','))), key=len)[0]
                        if any(True for __item in equiv_entity_assemblies
                               if not any(True for label_asym_id in __item[_label_asym_id].split(',')
                                          if label_asym_id in self._reg.label_asym_id_with_exptl_data)):
                            if _item == item or row[6] is None or row[6] == 'no':
                                row[10] = group_id
                row[11], row[12] = item['entity_role'], item['entity_details']
                row[13], row[14] = 1, self._reg.entry_id

                if len(self._reg.auth_asym_ids_with_chem_exch) > 0:
                    auth_asym_id = row[5]
                    if auth_asym_id in self._reg.auth_asym_ids_with_chem_exch.keys():
                        conformational_states = len(self._reg.auth_asym_ids_with_chem_exch[auth_asym_id]) + 1
                        beg_model_id = 1
                        end_model_id = self._reg.total_models // conformational_states
                        seq_ids = [k for k, v in self._reg.auth_seq_ids_with_chem_exch.items()
                                   if v['chain_id'] == auth_asym_id]
                        if len(seq_ids) > 0:
                            row[12] = f'Conformational isomer 1, PDB_model_num range: {beg_model_id}-{end_model_id}, '\
                                f'original sequence number range: {min(seq_ids)}-{max(seq_ids)}'
                            set_sf_tag(asm_sf, 'Molecules_in_chemical_exchange', 'yes')

                ea_loop.add_data(row)

            if len(self._reg.auth_asym_ids_with_chem_exch) > 0:
                _entity_assembly_id = ea_loop.data[-1][0]
                for idx, item in enumerate(entity_assembly):
                    entity_type = item['entity_type']
                    if entity_type in ('non-polymer', 'water'):
                        continue
                    auth_asym_id = item['auth_asym_id']
                    if auth_asym_id in self._reg.auth_asym_ids_with_chem_exch.keys():
                        for offset, _auth_asym_id in enumerate(self._reg.auth_asym_ids_with_chem_exch[auth_asym_id], start=2):
                            row = ea_loop.data[idx]
                            _row = copy.copy(row)
                            _entity_assembly_id += 1
                            _row[0] = _entity_assembly_id
                            _row[1] = f'entity_{entity_id}_{offset}'
                            _row[5] = _auth_asym_id
                            conformational_states = len(self._reg.auth_asym_ids_with_chem_exch[auth_asym_id]) + 1
                            model_ids_per_state = self._reg.total_models // conformational_states
                            beg_model_id = 1 + model_ids_per_state * (offset - 1)
                            end_model_id = model_ids_per_state * offset
                            seq_ids = [k for k, v in self._reg.auth_seq_ids_with_chem_exch.items()
                                       if v['chain_id'] == _auth_asym_id]
                            if len(seq_ids) > 0:
                                _row[12] = f'Conformational isomer {offset}, PDB_model_num range: {beg_model_id}-{end_model_id}, '\
                                    f'original sequence number range: {min(seq_ids)}-{max(seq_ids)}'

                            ea_loop.add_data(_row)

            asm_sf.add_loop(ea_loop)

        # refresh _nef_sequence or _Chem_comp_assembly loop

        lp_category = LP_CATEGORIES[file_type][content_subtype]

        loop = pynmrstar.Loop.from_scratch(lp_category)

        has_index_tag = INDEX_TAGS[file_type][content_subtype] is not None

        if has_index_tag:
            loop.add_tag(f'{lp_category}.{INDEX_TAGS[file_type][content_subtype]}')

        for key_item in key_items:
            loop.add_tag(f"{lp_category}.{key_item['name']}")

        for data_item in data_items:
            data_name = data_item['name']
            if data_name != 'NEF_index' or (data_name == 'NEF_index' and has_nef_index):
                loop.add_tag(f'{lp_category}.{data_name}')

        if has_entry_id:
            loop.add_tag(f'{lp_category}.Entry_ID')

        cif_poly_seq = self._reg.caC['polymer_sequence']
        entity_assembly = self._reg.caC['entity_assembly']
        auth_to_star_seq = self._reg.caC['auth_to_star_seq']
        auth_to_orig_seq = self._reg.caC['auth_to_orig_seq']
        asym_to_orig_seq = {}
        if self._reg.caC is not None:
            if 'asym_to_orig_seq' in self._reg.caC:
                asym_to_orig_seq = self._reg.caC['asym_to_orig_seq']
            else:
                for _k, _v in auth_to_orig_seq.items():
                    auth_asym_id = _k[0]
                    if auth_asym_id not in asym_to_orig_seq:
                        asym_to_orig_seq[auth_asym_id] = {}
                    asym_to_orig_seq[auth_asym_id][(_k[1], _k[2])] = _v
                self._reg.caC['asym_to_orig_seq'] = asym_to_orig_seq
                if self._reg.asmChkCachePath is not None:
                    write_as_pickle(self._reg.caC, self._reg.asmChkCachePath)

        # DAOTHER-9644: sort by Entity_assembly_ID and Comp_index_ID due to inserted sequence for truncated loop
        _auth_to_star_seq = dict(sorted(auth_to_star_seq.items(), key=lambda item: item[1]))

        entity_type_of = {item['entity_id']: item['entity_type'] for item in entity_assembly}

        seq_keys = set()

        nef_index = 1
        _entity_assembly_id = index = 0

        if file_type == 'nef':

            idx_col = loop.tags.index('index')
            chain_id_col = loop.tags.index('chain_code')
            seq_id_col = loop.tags.index('sequence_code')
            comp_id_col = loop.tags.index('residue_name')
            seq_link_col = loop.tags.index('linking')
            auth_var_id_col = loop.tags.index('residue_variant')
            cis_res_col = loop.tags.index('cis_peptide')

            for k, v in _auth_to_star_seq.items():
                auth_asym_id, auth_seq_id, comp_id = k
                entity_assembly_id, seq_id, entity_id, genuine = v

                if auth_seq_id is None or not genuine:
                    continue

                seq_key = (entity_assembly_id, seq_id)

                if seq_key in seq_keys:
                    continue

                if entity_assembly_id != _entity_assembly_id:
                    _entity_assembly_id = entity_assembly_id
                    index = 1

                seq_keys.add(seq_key)

                if self._reg.nmr_ext_poly_seq is not None and len(self._reg.nmr_ext_poly_seq) > 0\
                   and any(True for d in self._reg.nmr_ext_poly_seq
                           if d['auth_chain_id'] == auth_asym_id and d['auth_seq_id'] < auth_seq_id):
                    for d in self._reg.nmr_ext_poly_seq:
                        if d['auth_chain_id'] == auth_asym_id and d['auth_seq_id'] < auth_seq_id and 'touch' not in d:
                            _auth_seq_id, _auth_comp_id = d['auth_seq_id'], d['auth_comp_id']
                            _seq_key = (entity_assembly_id, _auth_seq_id)
                            # 2l1f, DAOTHER-9694
                            if _seq_key in seq_keys or _auth_comp_id in EMPTY_VALUE or not _auth_comp_id[0].isalnum():
                                continue
                            seq_keys.add(_seq_key)
                            row = [None] * len(loop.tags)
                            row[chain_id_col], row[seq_id_col], row[comp_id_col], row[idx_col] =\
                                auth_asym_id, _auth_seq_id, _auth_comp_id, nef_index
                            row[seq_link_col] = 'start' if index == 1\
                                else 'middle' if _auth_comp_id not in UNKNOWN_RESIDUE\
                                else 'dummy'

                            loop.add_data(row)

                            d['touch'] = True

                            nef_index += 1
                            index += 1

                if auth_asym_id in asym_to_orig_seq:
                    auth_comp_id = next((_v[1] for _k, _v in asym_to_orig_seq[auth_asym_id].items()
                                         if _k == (auth_seq_id, comp_id)), comp_id)
                else:
                    auth_comp_id = comp_id

                row = [None] * len(loop.tags)

                row[chain_id_col], row[seq_id_col] = auth_asym_id, auth_seq_id

                entity_type = entity_type_of[entity_id]

                row[comp_id_col] = auth_comp_id

                if entity_type == 'polymer':
                    ps = next(ps for ps in cif_poly_seq if ps['auth_chain_id'] == auth_asym_id)
                    nmr_ps = self._reg.report.getNmrPolymerSequenceWithModelChainId(auth_asym_id,
                                                                                    label_scheme=False)
                    if nmr_ps is None and 'identical_auth_chain_id' in ps:
                        nmr_ps = self._reg.report.getNmrPolymerSequenceWithModelChainId(ps['identical_auth_chain_id'][0],
                                                                                        label_scheme=False)

                    if nmr_ps is not None:
                        try:
                            j = ps['auth_seq_id'].index(auth_seq_id)
                            label_seq_id = ps['seq_id'][j]
                            length = len(ps['seq_id'])
                            cyclic = self._reg.dpV.isCyclicPolymer(nmr_ps['chain_id'])
                            if cyclic and label_seq_id in (1, length):
                                row[seq_link_col] = 'cyclic'
                            elif label_seq_id == 1 and length == 1:
                                row[seq_link_col] = 'single'
                            elif index == 1:
                                row[seq_link_col] = 'start'
                            elif j == length - 1:
                                row[seq_link_col] = 'end'
                            elif label_seq_id - 1 == ps['seq_id'][j - 1] and label_seq_id + 1 == ps['seq_id'][j + 1]:
                                row[seq_link_col] = 'middle'
                            elif label_seq_id == 1:
                                row[seq_link_col] = 'middle'
                            else:
                                row[seq_link_col] = 'break'

                            entity_poly_type = next((item['entity_poly_type'] for item in entity_assembly
                                                     if item['entity_id'] == entity_id and item['entity_type'] == 'polymer'), None)
                            if entity_poly_type is not None and entity_poly_type.startswith('polypeptide'):
                                if self._reg.dpV.isProtCis(nmr_ps['chain_id'], seq_id):
                                    row[cis_res_col] = 'true'
                                elif auth_comp_id in ('PRO', 'GLY'):
                                    row[cis_res_col] = 'false'
                                else:
                                    row[cis_res_col] = '.'
                        except ValueError:
                            pass

                row[idx_col] = nef_index

                if auth_var_id_col != -1 and has_res_var_dat:
                    orig_row = next((_row for _row in orig_lp_data
                                     if _row['chain_code'] == auth_asym_id
                                     and _row['sequence_code'] == auth_seq_id
                                     and _row['residue_name'] == auth_comp_id), None)
                    if orig_row is not None:
                        row[auth_var_id_col] = orig_row['residue_variant']

                if auth_comp_id not in EMPTY_VALUE:
                    loop.add_data(row)

                nef_index += 1
                index += 1

                if row[seq_link_col] == 'end' and self._reg.nmr_ext_poly_seq is not None and len(self._reg.nmr_ext_poly_seq) > 0\
                   and any(True for d in self._reg.nmr_ext_poly_seq
                           if d['auth_chain_id'] == auth_asym_id and d['auth_seq_id'] > auth_seq_id):
                    for d in self._reg.nmr_ext_poly_seq:
                        if d['auth_chain_id'] == auth_asym_id and d['auth_seq_id'] > auth_seq_id and 'touch' not in d:
                            if loop.data[-1][seq_link_col] == 'end':
                                loop.data[-1][seq_link_col] = 'middle'
                            _auth_seq_id, _auth_comp_id = d['auth_seq_id'], d['auth_comp_id']
                            _seq_key = (entity_assembly_id, _auth_seq_id)
                            # 2l1f, DAOTHER-9694:
                            if _seq_key in seq_keys or _auth_comp_id in EMPTY_VALUE or not _auth_comp_id[0].isalnum():
                                continue
                            seq_keys.add(_seq_key)
                            row = [None] * len(loop.tags)
                            row[chain_id_col], row[seq_id_col], row[comp_id_col], row[idx_col] =\
                                auth_asym_id, _auth_seq_id, _auth_comp_id, nef_index
                            row[seq_link_col] = 'end' if _auth_comp_id not in UNKNOWN_RESIDUE else 'dummy'

                            loop.add_data(row)

                            d['touch'] = True

                            nef_index += 1

            if len(self._reg.auth_asym_ids_with_chem_exch) > 0:
                for item in entity_assembly:
                    entity_type = item['entity_type']
                    if entity_type in ('non-polymer', 'water'):
                        continue
                    auth_asym_id = item['auth_asym_id']
                    if auth_asym_id in self._reg.auth_asym_ids_with_chem_exch.keys():
                        for _auth_asym_id in self._reg.auth_asym_ids_with_chem_exch[auth_asym_id]:
                            for row in loop:
                                if row[chain_id_col] == auth_asym_id:
                                    _row = copy.copy(row)
                                    _row[chain_id_col] = _auth_asym_id
                                    _row[idx_col] = nef_index

                                    loop.add_data(_row)

                                    nef_index += 1

            asm_sf.add_loop(loop)

            if self._reg.nmr_ext_poly_seq is not None and len(self._reg.nmr_ext_poly_seq) > 0:
                for d in self._reg.nmr_ext_poly_seq:
                    if 'touch' in d:
                        del d['touch']

            # refresh _nef_covalent_links loop

            if self._reg.cR.hasCategory('struct_conn'):

                lp_category = '_nef_covalent_links'

                b_loop = pynmrstar.Loop.from_scratch(lp_category)

                b_key_items = [{'name': 'chain_code_1', 'type': 'str'},
                               {'name': 'sequence_code_1', 'type': 'int'},
                               {'name': 'residue_name_1', 'type': 'str'},
                               {'name': 'atom_name_1', 'type': 'str'},
                               {'name': 'chain_code_2', 'type': 'str'},
                               {'name': 'sequence_code_2', 'type': 'int'},
                               {'name': 'residue_name_2', 'type': 'str'},
                               {'name': 'atom_name_2', 'type': 'str'}
                               ]

                tags = [f"{lp_category}.{_item['name']}" for _item in b_key_items]

                b_loop.add_tag(tags)

                bonds = self._reg.cR.getDictList('struct_conn')

                for bond in bonds:
                    bond_type = bond['conn_type_id']
                    auth_asym_id_1 = bond['ptnr1_auth_asym_id']
                    auth_seq_id_1 = bond['ptnr1_auth_seq_id']
                    auth_comp_id_1 = bond['ptnr1_auth_comp_id']
                    atom_id_1 = bond['ptnr1_label_atom_id']
                    auth_asym_id_2 = bond['ptnr2_auth_asym_id']
                    auth_seq_id_2 = bond['ptnr2_auth_seq_id']
                    auth_comp_id_2 = bond['ptnr2_auth_comp_id']
                    atom_id_2 = bond['ptnr2_label_atom_id']

                    if bond_type == 'covale':
                        pass
                    elif bond_type.startswith('covale_'):  # 'covale_base', 'covale_phosphate', 'covale_sugar'
                        pass
                    elif bond_type == 'disulf':
                        pass
                    elif bond_type == 'hydrog':
                        continue
                    elif bond_type == 'metalc':
                        pass
                    elif bond_type == 'mismat':
                        continue
                    elif bond_type == 'modres':
                        continue
                    elif bond_type == 'saltbr':
                        continue

                    row = [None] * len(tags)

                    try:

                        seq_key_1 = (auth_asym_id_1, int(auth_seq_id_1), auth_comp_id_1)

                        if seq_key_1 in auth_to_star_seq:
                            row[0], row[1], row[2], row[3] = auth_asym_id_1, auth_seq_id_1, auth_comp_id_1, atom_id_1

                    except ValueError:
                        pass

                    try:

                        seq_key_2 = (auth_asym_id_2, int(auth_seq_id_2), auth_comp_id_2)

                        if seq_key_2 in auth_to_star_seq:
                            row[4], row[5], row[6], row[7] = auth_asym_id_2, auth_seq_id_2, auth_comp_id_2, atom_id_2

                    except ValueError:
                        pass

                    if None not in (row[0], row[4]):
                        b_loop.add_data(row)

                if len(b_loop) > 0:
                    asm_sf.add_loop(b_loop)

        else:

            chain_id_col = loop.tags.index('Entity_assembly_ID')
            ent_id_col = loop.tags.index('Entity_ID')
            seq_id_col = loop.tags.index('Comp_index_ID')
            alt_seq_id_col = loop.tags.index('Seq_ID')
            comp_id_col = loop.tags.index('Comp_ID')
            auth_asym_id_col = loop.tags.index('Auth_asym_ID')
            auth_seq_id_col = loop.tags.index('Auth_seq_ID')
            auth_comp_id_col = loop.tags.index('Auth_comp_ID')
            seq_link_col = loop.tags.index('Sequence_linking')
            cis_res_col = loop.tags.index('Cis_residue')
            asm_id_col = loop.tags.index('Assembly_ID')
            idx_col = loop.tags.index('NEF_index') if 'NEF_index' in loop.tags else -1
            auth_var_id_col = loop.tags.index('Auth_variant_ID') if 'Auth_variant_ID' in loop.tags else -1
            entry_id_col = loop.tags.index('Entry_ID') if 'Entry_ID' in loop.tags else -1

            for k, v in _auth_to_star_seq.items():
                auth_asym_id, auth_seq_id, comp_id = k
                entity_assembly_id, seq_id, entity_id, genuine = v

                if auth_seq_id is None or not genuine:
                    continue

                seq_key = (entity_assembly_id, seq_id)

                if seq_key in seq_keys:
                    continue

                if entity_assembly_id != _entity_assembly_id:
                    _entity_assembly_id = entity_assembly_id
                    index = 1

                seq_keys.add(seq_key)

                if self._reg.nmr_ext_poly_seq is not None and len(self._reg.nmr_ext_poly_seq) > 0\
                   and any(True for d in self._reg.nmr_ext_poly_seq
                           if d['auth_chain_id'] == auth_asym_id and d['auth_seq_id'] < auth_seq_id):
                    for d in self._reg.nmr_ext_poly_seq:
                        if d['auth_chain_id'] == auth_asym_id and d['auth_seq_id'] < auth_seq_id and 'touch' not in d:
                            _offset = seq_id - auth_seq_id
                            _auth_seq_id, _auth_comp_id = d['auth_seq_id'], d['auth_comp_id']
                            _seq_id = _auth_seq_id + _offset
                            _seq_key = (entity_assembly_id, _seq_id)
                            # 2l1f, DAOTHER-9694
                            if _seq_key in seq_keys or _auth_comp_id in EMPTY_VALUE or not _auth_comp_id[0].isalnum():
                                continue
                            seq_keys.add(_seq_key)
                            row = [None] * len(loop.tags)
                            row[chain_id_col], row[ent_id_col], row[seq_id_col], row[alt_seq_id_col] =\
                                entity_assembly_id, entity_id, _seq_id, _seq_id
                            row[comp_id_col], row[auth_asym_id_col], row[auth_seq_id_col], row[auth_comp_id_col] =\
                                _auth_comp_id, auth_asym_id, _auth_seq_id, _auth_comp_id
                            row[seq_link_col] = 'start' if index == 1\
                                else 'middle' if _auth_comp_id not in UNKNOWN_RESIDUE\
                                else 'dummy'
                            row[asm_id_col] = 1
                            if idx_col != -1:
                                row[idx_col] = nef_index
                            if entry_id_col != -1:
                                row[entry_id_col] = self._reg.entry_id

                            loop.add_data(row)

                            d['touch'] = True

                            nef_index += 1
                            index += 1

                if auth_asym_id in asym_to_orig_seq:
                    auth_comp_id = next((_v[1] for _k, _v in asym_to_orig_seq[auth_asym_id].items()
                                         if _k == (auth_seq_id, comp_id)), comp_id)
                else:
                    auth_comp_id = comp_id

                row = [None] * len(loop.tags)

                row[chain_id_col], row[ent_id_col] = entity_assembly_id, entity_id
                row[seq_id_col] = row[alt_seq_id_col] = seq_id
                seq_keys.add((entity_assembly_id, seq_id))

                entity_type = entity_type_of[entity_id]

                row[comp_id_col], row[auth_asym_id_col], row[auth_seq_id_col], row[auth_comp_id_col] =\
                    auth_comp_id, auth_asym_id, auth_seq_id, auth_comp_id

                if entity_type == 'polymer':
                    ps = next(ps for ps in cif_poly_seq if ps['auth_chain_id'] == auth_asym_id)
                    nmr_ps = self._reg.report.getNmrPolymerSequenceWithModelChainId(auth_asym_id,
                                                                                    label_scheme=False)
                    if nmr_ps is None and 'identical_auth_chain_id' in ps:
                        nmr_ps = self._reg.report.getNmrPolymerSequenceWithModelChainId(ps['identical_auth_chain_id'][0],
                                                                                        label_scheme=False)

                    if nmr_ps is not None:
                        try:
                            j = ps['auth_seq_id'].index(auth_seq_id)
                            label_seq_id = ps['seq_id'][j]
                            if label_seq_id is not None:
                                try:
                                    length = len(ps['seq_id'])
                                    cyclic = self._reg.dpV.isCyclicPolymer(nmr_ps['chain_id'])
                                    if cyclic and label_seq_id in (1, length):
                                        row[seq_link_col] = 'cyclic'
                                    elif label_seq_id == 1 and length == 1:
                                        row[seq_link_col] = 'single'
                                    elif index == 1:
                                        row[seq_link_col] = 'start'
                                    elif j == length - 1:
                                        row[seq_link_col] = 'end'
                                    elif label_seq_id - 1 == ps['seq_id'][j - 1] and label_seq_id + 1 == ps['seq_id'][j + 1]:
                                        row[seq_link_col] = 'middle'
                                    elif label_seq_id == 1:
                                        row[seq_link_col] = 'middle'
                                    else:
                                        row[seq_link_col] = 'break'
                                except IndexError:
                                    pass

                            entity_poly_type = next((item['entity_poly_type'] for item in entity_assembly
                                                     if item['entity_id'] == entity_id and item['entity_type'] == 'polymer'), None)
                            if entity_poly_type is not None and entity_poly_type.startswith('polypeptide'):
                                if self._reg.dpV.isProtCis(nmr_ps['chain_id'], seq_id):
                                    row[cis_res_col] = 'yes'
                                elif auth_comp_id in ('PRO', 'GLY'):
                                    row[cis_res_col] = 'no'
                                else:
                                    row[cis_res_col] = '.'
                        except ValueError:
                            pass

                row[asm_id_col] = 1

                if idx_col != -1:
                    row[idx_col] = nef_index

                if auth_var_id_col != -1 and has_res_var_dat:
                    orig_row = next((_row for _row in orig_lp_data
                                     if _row['Entity_assembly_ID'] == str(entity_assembly_id)
                                     and _row['Comp_index_ID'] == seq_id
                                     and _row['Comp_ID'] == auth_comp_id), None)
                    if orig_row is not None:
                        row[auth_var_id_col] = orig_row['Auth_variant_ID']

                if entry_id_col != -1:
                    row[entry_id_col] = self._reg.entry_id

                if comp_id not in EMPTY_VALUE:
                    loop.add_data(row)

                nef_index += 1
                index += 1

                if row[seq_link_col] == 'end' and self._reg.nmr_ext_poly_seq is not None and len(self._reg.nmr_ext_poly_seq) > 0\
                   and any(True for d in self._reg.nmr_ext_poly_seq
                           if d['auth_chain_id'] == auth_asym_id and d['auth_seq_id'] > auth_seq_id):
                    for d in self._reg.nmr_ext_poly_seq:
                        if d['auth_chain_id'] == auth_asym_id and d['auth_seq_id'] > auth_seq_id and 'touch' not in d:
                            if loop.data[-1][seq_link_col] == 'end':
                                loop.data[-1][seq_link_col] = 'middle'
                            _offset = seq_id - auth_seq_id
                            _auth_seq_id, _auth_comp_id = d['auth_seq_id'], d['auth_comp_id']
                            _seq_id = _auth_seq_id + _offset
                            _seq_key = (entity_assembly_id, _seq_id)
                            # 2l1f, DAOTHER-9694:
                            if _seq_key in seq_keys or _auth_comp_id in EMPTY_VALUE or not _auth_comp_id[0].isalnum():
                                continue
                            seq_keys.add(_seq_key)
                            row = [None] * len(loop.tags)
                            row[chain_id_col], row[ent_id_col], row[seq_id_col], row[alt_seq_id_col] =\
                                entity_assembly_id, entity_id, _seq_id, _seq_id
                            row[comp_id_col], row[auth_asym_id_col], row[auth_seq_id_col], row[auth_comp_id_col] =\
                                _auth_comp_id, auth_asym_id, _auth_seq_id, _auth_comp_id
                            row[seq_link_col] = 'end' if _auth_comp_id not in UNKNOWN_RESIDUE else 'dummy'
                            row[asm_id_col] = 1
                            if idx_col != -1:
                                row[idx_col] = nef_index
                            if entry_id_col != -1:
                                row[entry_id_col] = self._reg.entry_id

                            loop.add_data(row)

                            d['touch'] = True

                            nef_index += 1

            if len(self._reg.auth_asym_ids_with_chem_exch) > 0:
                _entity_assembly_id = loop.data[-1][chain_id_col]
                for item in entity_assembly:
                    entity_type = item['entity_type']
                    if entity_type in ('non-polymer', 'water'):
                        continue
                    entity_id = item['entity_id']
                    auth_asym_id = item['auth_asym_id']
                    if auth_asym_id in self._reg.auth_asym_ids_with_chem_exch.keys():
                        for _auth_asym_id in self._reg.auth_asym_ids_with_chem_exch[auth_asym_id]:
                            _entity_assembly_id += 1
                            for row in loop:
                                if row[ent_id_col] == entity_id and row[auth_asym_id_col] == auth_asym_id:
                                    _row = copy.copy(row)
                                    _row[chain_id_col] = _entity_assembly_id
                                    _row[auth_asym_id_col] = _auth_asym_id

                                    if idx_col != -1:
                                        _row[idx_col] = nef_index

                                    loop.add_data(_row)

                                    nef_index += 1

            asm_sf.add_loop(loop)

            if self._reg.nmr_ext_poly_seq is not None and len(self._reg.nmr_ext_poly_seq) > 0:
                for d in self._reg.nmr_ext_poly_seq:
                    if 'touch' in d:
                        del d['touch']

            self._reg.chem_comp_asm_dat = loop.get_tag(list(CCA_TAGS))

            # refresh _Bond loop

            if self._reg.cR.hasCategory('struct_conn'):

                lp_category = '_Bond'

                b_loop = pynmrstar.Loop.from_scratch(lp_category)

                b_key_items = [{'name': 'ID', 'type': 'positive-int'},
                               {'name': 'Type', 'type': 'enum',
                                'enum': ('amide', 'covalent', 'directed', 'disulfide', 'ester', 'ether',
                                         'hydrogen', 'metal coordination', 'peptide', 'thioether', 'oxime',
                                         'thioester', 'phosphoester', 'phosphodiester', 'diselenide', 'na')},
                               {'name': 'Value_order', 'type': 'enum',
                                'enum': ('sing', 'doub', 'trip', 'quad', 'arom', 'poly', 'delo', 'pi', 'directed')},
                               {'name': 'Entity_assembly_ID_1', 'type': 'positive-int-as-str'},
                               {'name': 'Entity_assembly_name_1', 'type': 'str'},
                               {'name': 'Entity_ID_1', 'type': 'positive-int'},
                               {'name': 'Comp_ID_1', 'type': 'str'},
                               {'name': 'Comp_index_ID_1', 'type': 'int'},
                               {'name': 'Seq_ID_1', 'type': 'int'},
                               {'name': 'Atom_ID_1', 'type': 'str'},
                               {'name': 'Entity_assembly_ID_2', 'type': 'positive-int-as-str'},
                               {'name': 'Entity_assembly_name_2', 'type': 'str'},
                               {'name': 'Entity_ID_2', 'type': 'positive-int'},
                               {'name': 'Comp_ID_2', 'type': 'str'},
                               {'name': 'Comp_index_ID_2', 'type': 'int'},
                               {'name': 'Seq_ID_2', 'type': 'int'},
                               {'name': 'Atom_ID_2', 'type': 'str'},
                               ]
                b_data_items = [{'name': 'Auth_asym_ID_1', 'type': 'str', 'mandaory': False},
                                {'name': 'Auth_seq_ID_1', 'type': 'int', 'mandatory': False},
                                {'name': 'Auth_comp_ID_1', 'type': 'str', 'mandatory': False},
                                {'name': 'Auth_atom_ID_1', 'type': 'str', 'mandatory': False},
                                {'name': 'Auth_asym_ID_2', 'type': 'str', 'mandaory': False},
                                {'name': 'Auth_seq_ID_2', 'type': 'int', 'mandatory': False},
                                {'name': 'Auth_comp_ID_2', 'type': 'str', 'mandatory': False},
                                {'name': 'Auth_atom_ID_2', 'type': 'str', 'mandatory': False},
                                {'name': 'Assembly_ID', 'type': 'pointer-index', 'mandatory': False,
                                 'default': '1', 'default-from': 'parent'},
                                {'name': 'Entry_ID', 'type': 'str', 'mandatory': False}
                                ]

                tags = [f"{lp_category}.{_item['name']}" for _item in b_key_items]
                tags.extend([f"{lp_category}.{_item['name']}" for _item in b_data_items])

                b_loop.add_tag(tags)

                bonds = self._reg.cR.getDictList('struct_conn')

                index = 1

                non_std_bond = False

                for bond in bonds:

                    try:

                        bond_type = bond['conn_type_id']
                        auth_asym_id_1 = bond['ptnr1_auth_asym_id']
                        auth_seq_id_1 = int(bond['ptnr1_auth_seq_id'])
                        auth_comp_id_1 = bond['ptnr1_auth_comp_id']
                        atom_id_1 = bond['ptnr1_label_atom_id']
                        auth_asym_id_2 = bond['ptnr2_auth_asym_id']
                        auth_seq_id_2 = int(bond['ptnr2_auth_seq_id'])
                        auth_comp_id_2 = bond['ptnr2_auth_comp_id']
                        atom_id_2 = bond['ptnr2_label_atom_id']

                    except ValueError:
                        continue

                    row = [None] * len(tags)

                    row[0] = index

                    if bond_type == 'covale':
                        row[1], row[2] = 'covalent', 'sing'
                        non_std_bond = True
                    elif bond_type.startswith('covale_'):  # 'covale_base', 'covale_phosphate', 'covale_sugar'
                        row[1] = 'covalent'
                        non_std_bond = True
                    elif bond_type == 'disulf':
                        row[1], row[2] = 'disulfide', 'sing'
                    elif bond_type == 'hydrog':
                        row[1], row[2] = 'hydrogen', 'sing'
                        continue
                    elif bond_type == 'metalc':
                        row[1], row[2] = 'metal coordination', 'sing'
                        non_std_bond = True
                    elif bond_type == 'mismat':
                        row[1] = 'na'
                        non_std_bond = True
                        continue
                    elif bond_type == 'modres':
                        row[1] = 'na'
                        non_std_bond = True
                        continue
                    elif bond_type == 'saltbr':
                        row[1] = 'na'
                        continue

                    seq_key_1 = (auth_asym_id_1, auth_seq_id_1, auth_comp_id_1)

                    entity_id_1 = entity_id_2 = None

                    if seq_key_1 in auth_to_star_seq:
                        entity_assembly_id_1, seq_id_1, entity_id_1, _ = auth_to_star_seq[seq_key_1]
                        entity_assembly_name_1 = next((item['entity_assembly_name'] for item in entity_assembly
                                                       if item['entity_assembly_id'] == entity_assembly_id_1), None)
                        row[3], row[4], row[5], row[6], row[7], row[8], row[9] =\
                            entity_assembly_id_1, entity_assembly_name_1, entity_id_1, auth_comp_id_1, seq_id_1, seq_id_1, atom_id_1

                        row[17], row[18], row[19], row[20] =\
                            auth_asym_id_1, auth_seq_id_1, auth_comp_id_1, atom_id_1

                    seq_key_2 = (auth_asym_id_2, auth_seq_id_2, auth_comp_id_2)

                    if seq_key_2 in auth_to_star_seq:
                        entity_assembly_id_2, seq_id_2, entity_id_2, _ = auth_to_star_seq[seq_key_2]
                        entity_assembly_name_2 = next((item['entity_assembly_name'] for item in entity_assembly
                                                       if item['entity_assembly_id'] == entity_assembly_id_2), None)
                        row[10], row[11], row[12], row[13], row[14], row[15], row[16] =\
                            entity_assembly_id_2, entity_assembly_name_2, entity_id_2, auth_comp_id_2, seq_id_2, seq_id_2, atom_id_2

                        row[21], row[22], row[23], row[24] =\
                            auth_asym_id_2, auth_seq_id_2, auth_comp_id_2, atom_id_2

                    if entity_id_1 is not None and entity_id_2 is not None and entity_id_1 == entity_id_2:
                        entity_poly_type = next((item['entity_poly_type'] for item in entity_assembly
                                                 if item['entity_id'] == entity_id_1 and item['entity_type'] == 'polymer'), None)
                        if entity_poly_type is not None and entity_poly_type.startswith('polypeptide')\
                           and {atom_id_1, atom_id_2} == {'C', 'N'} and abs(auth_seq_id_1 - auth_seq_id_2) > 1:
                            row[1], row[2] = 'peptide', "sing"

                    row[25], row[26] = 1, self._reg.entry_id

                    b_loop.add_data(row)

                    index += 1

                if index > 1:
                    asm_sf.add_loop(b_loop)

                if non_std_bond:
                    set_sf_tag(asm_sf, 'Non_standard_bonds', 'yes')

                bonds_w_leaving = [bond for bond in bonds
                                   if ('pdbx_leaving_atom_flag' in bond and bond['pdbx_leaving_atom_flag'] in ('both', 'one'))
                                   or (bond['ptnr1_label_comp_id'] in ('CYS', 'DCS') and bond['ptnr1_label_atom_id'] == 'SG')
                                   or (bond['ptnr2_label_comp_id'] in ('CYS', 'DCS') and bond['ptnr2_label_atom_id'] == 'SG')
                                   or (bond['ptnr1_label_comp_id'] == 'HIS' and bond['ptnr1_label_atom_id'] in ('ND1', 'NE2'))
                                   or (bond['ptnr2_label_comp_id'] == 'HIS' and bond['ptnr2_label_atom_id'] in ('ND1', 'NE2'))]

                if len(bonds_w_leaving) > 0:

                    def get_auth_seq_id(val):
                        if isinstance(val, int):
                            return val
                        if val in EMPTY_VALUE:
                            return None
                        if val.isdigit():
                            return int(val)
                        return int(re.findall(r'\d+', val)[0])

                    # _Entity_deleted_atom loop

                    lp_category = '_Entity_deleted_atom'

                    eda_loop = pynmrstar.Loop.from_scratch(lp_category)

                    eda_key_items = [{'name': 'ID', 'type': 'positive-int'},
                                     {'name': 'Entity_assembly_ID', 'type': 'positive-int-as-str'},
                                     {'name': 'Comp_index_ID', 'type': 'int'},
                                     {'name': 'Seq_ID', 'type': 'int'},
                                     {'name': 'Comp_ID', 'type': 'str'},
                                     {'name': 'Atom_ID', 'type': 'str'}
                                     ]
                    eda_data_items = [{'name': 'Auth_entity_assembly_ID', 'type': 'positive-int-as-str'},
                                      {'name': 'Auth_seq_ID', 'type': 'int'},
                                      {'name': 'Auth_comp_ID', 'type': 'str'},
                                      {'name': 'Auth_atom_ID', 'type': 'str'},
                                      {'name': 'Assembly_ID', 'type': 'pointer-index', 'mandatory': False,
                                       'default': '1', 'default-from': 'parent'},
                                      {'name': 'Entry_ID', 'type': 'str', 'mandatory': False}
                                      ]

                    tags = [f"{lp_category}.{_item['name']}" for _item in eda_key_items]
                    tags.extend([f"{lp_category}.{_item['name']}" for _item in eda_data_items])

                    eda_loop.add_tag(tags)

                    index = 1

                    for bond in bonds_w_leaving:

                        leaving_flag = bond.get('pdbx_leaving_atom_flag', '')

                        if leaving_flag in ('one', 'both'):
                            leaving_atom_id = None

                            comp_id = bond['ptnr1_label_comp_id']
                            atom_id = bond['ptnr1_label_atom_id']
                            auth_asym_id = bond['ptnr1_auth_asym_id']
                            auth_seq_id = get_auth_seq_id(bond['ptnr1_auth_seq_id'])

                            if auth_seq_id is None:
                                continue

                            if self._reg.ccU.updateChemCompDict(comp_id):
                                for b in self._reg.ccU.lastBondDictList:
                                    if atom_id in (b['atom_id_1'], b['atom_id_2']):
                                        _atom_id = b['atom_id_1'] if b['atom_id_1'] != atom_id\
                                            else b['atom_id_2']
                                        if any(True for a in self._reg.ccU.lastAtomDictList
                                               if _atom_id == a['atom_id'] and a['leaving_atom_flag'] == 'Y'):
                                            leaving_atom_id = _atom_id
                                            break

                                if leaving_atom_id is not None:

                                    seq_key = (auth_asym_id, auth_seq_id, comp_id)

                                    if seq_key in auth_to_star_seq:
                                        if auth_asym_id in asym_to_orig_seq:
                                            auth_comp_id = next((_v[1] for _k, _v in asym_to_orig_seq[auth_asym_id].items()
                                                                 if _k == (seq_key[1], comp_id)), comp_id)
                                        else:
                                            auth_comp_id = comp_id

                                        row = [None] * len(tags)

                                        row[0] = index

                                        entity_assembly_id, seq_id, _, _ = auth_to_star_seq[seq_key]

                                        row[1], row[4], row[5] =\
                                            entity_assembly_id, auth_comp_id, leaving_atom_id
                                        row[2] = row[3] = seq_id

                                        row[6], row[7], row[8], row[9] =\
                                            auth_asym_id, auth_seq_id, auth_comp_id, leaving_atom_id

                                        row[10], row[11] = 1, self._reg.entry_id

                                        eda_loop.add_data(row)

                                        index += 1

                            if leaving_flag == 'both' or leaving_atom_id is None:
                                leaving_atom_id = None

                                comp_id = bond['ptnr2_label_comp_id']
                                atom_id = bond['ptnr2_label_atom_id']
                                auth_asym_id = bond['ptnr2_auth_asym_id']
                                auth_seq_id = get_auth_seq_id(bond['ptnr2_auth_seq_id'])

                                if auth_seq_id is None:
                                    continue

                                if self._reg.ccU.updateChemCompDict(comp_id):
                                    for b in self._reg.ccU.lastBondDictList:
                                        if atom_id in (b['atom_id_1'], b['atom_id_2']):
                                            _atom_id = b['atom_id_1'] if b['atom_id_1'] != atom_id\
                                                else b['atom_id_2']
                                            if any(True for a in self._reg.ccU.lastAtomDictList
                                                   if _atom_id == a['atom_id']
                                                   and a['leaving_atom_flag'] == 'Y'):
                                                leaving_atom_id = _atom_id
                                                break

                                    if leaving_atom_id is not None:

                                        seq_key = (auth_asym_id, auth_seq_id, comp_id)

                                        if seq_key in auth_to_star_seq:
                                            if auth_asym_id in asym_to_orig_seq:
                                                auth_comp_id = next((_v[1] for _k, _v in asym_to_orig_seq[auth_asym_id].items()
                                                                     if _k == (seq_key[1], comp_id)), comp_id)
                                            else:
                                                auth_comp_id = comp_id

                                            row = [None] * len(tags)

                                            row[0] = index

                                            entity_assembly_id, seq_id, _, _ = auth_to_star_seq[seq_key]

                                            row[1], row[4], row[5] =\
                                                entity_assembly_id, auth_comp_id, leaving_atom_id
                                            row[2] = row[3] = seq_id

                                            row[6], row[7], row[8], row[9] =\
                                                auth_asym_id, auth_seq_id, auth_comp_id, leaving_atom_id

                                            row[10], row[11] = 1, self._reg.entry_id

                                            eda_loop.add_data(row)

                                            index += 1

                        else:

                            if bond['ptnr1_label_comp_id'] in ('CYS', 'DCS') and bond['ptnr1_label_atom_id'] == 'SG':
                                comp_id = bond['ptnr1_label_comp_id']
                                atom_id = 'SG'
                                auth_asym_id = bond['ptnr1_auth_asym_id']
                                auth_seq_id = get_auth_seq_id(bond['ptnr1_auth_seq_id'])

                                if auth_seq_id is None:
                                    continue

                                leaving_atom_id = 'HG'

                                seq_key = (auth_asym_id, auth_seq_id, comp_id)

                                if seq_key in auth_to_star_seq:
                                    auth_comp_id = next((_v[1] for _k, _v in asym_to_orig_seq[auth_asym_id].items()
                                                         if _k == (seq_key[1], comp_id)), comp_id)

                                    row = [None] * len(tags)

                                    row[0] = index

                                    entity_assembly_id, seq_id, _, _ = auth_to_star_seq[seq_key]

                                    row[1], row[4], row[5] =\
                                        entity_assembly_id, auth_comp_id, leaving_atom_id
                                    row[2] = row[3] = seq_id

                                    row[6], row[7], row[8], row[9] =\
                                        auth_asym_id, auth_seq_id, auth_comp_id, leaving_atom_id

                                    row[10], row[11] = 1, self._reg.entry_id

                                    eda_loop.add_data(row)

                                    index += 1

                            elif bond['ptnr1_label_comp_id'] == 'HIS' and bond['ptnr1_label_atom_id'] in ('ND1', 'NE2'):
                                comp_id = 'HIS'
                                atom_id = bond['ptnr1_label_atom_id']
                                auth_asym_id = bond['ptnr1_auth_asym_id']
                                auth_seq_id = get_auth_seq_id(bond['ptnr1_auth_seq_id'])

                                if auth_seq_id is None:
                                    continue

                                leaving_atom_id = 'HD1' if atom_id == 'ND1' else 'HE2'

                                seq_key = (auth_asym_id, auth_seq_id, comp_id)

                                if seq_key in auth_to_star_seq:
                                    if auth_asym_id in asym_to_orig_seq:
                                        auth_comp_id = next((_v[1] for _k, _v in asym_to_orig_seq[auth_asym_id].items()
                                                             if _k == (seq_key[1], comp_id)), comp_id)
                                    else:
                                        auth_comp_id = comp_id

                                    row = [None] * len(tags)

                                    row[0] = index

                                    entity_assembly_id, seq_id, _, _ = auth_to_star_seq[seq_key]

                                    row[1], row[4], row[5] =\
                                        entity_assembly_id, auth_comp_id, leaving_atom_id
                                    row[2] = row[3] = seq_id

                                    row[6], row[7], row[8], row[9] =\
                                        auth_asym_id, auth_seq_id, auth_comp_id, leaving_atom_id

                                    row[10], row[11] = 1, self._reg.entry_id

                                    eda_loop.add_data(row)

                                    index += 1

                            if bond['ptnr2_label_comp_id'] in ('CYS', 'DCS') and bond['ptnr2_label_atom_id'] == 'SG':
                                comp_id = bond['ptnr2_label_comp_id']
                                atom_id = 'SG'
                                auth_asym_id = bond['ptnr2_auth_asym_id']
                                auth_seq_id = get_auth_seq_id(bond['ptnr2_auth_seq_id'])

                                if auth_seq_id is None:
                                    continue

                                leaving_atom_id = 'HG'

                                seq_key = (auth_asym_id, auth_seq_id, comp_id)

                                if seq_key in auth_to_star_seq:
                                    if auth_asym_id in asym_to_orig_seq:
                                        auth_comp_id = next((_v[1] for _k, _v in asym_to_orig_seq[auth_asym_id].items()
                                                             if _k == (seq_key[1], comp_id)), comp_id)
                                    else:
                                        auth_comp_id = comp_id

                                    row = [None] * len(tags)

                                    row[0] = index

                                    entity_assembly_id, seq_id, _, _ = auth_to_star_seq[seq_key]

                                    row[1], row[4], row[5] =\
                                        entity_assembly_id, auth_comp_id, leaving_atom_id
                                    row[2] = row[3] = seq_id

                                    row[6], row[7], row[8], row[9] =\
                                        auth_asym_id, auth_seq_id, auth_comp_id, leaving_atom_id

                                    row[10], row[11] = 1, self._reg.entry_id

                                    eda_loop.add_data(row)

                                    index += 1

                            elif bond['ptnr2_label_comp_id'] == 'HIS' and bond['ptnr2_label_atom_id'] in ('ND1', 'NE2'):
                                comp_id = 'HIS'
                                atom_id = bond['ptnr2_label_atom_id']
                                auth_asym_id = bond['ptnr2_auth_asym_id']
                                auth_seq_id = get_auth_seq_id(bond['ptnr2_auth_seq_id'])

                                if auth_seq_id is None:
                                    continue

                                leaving_atom_id = 'HD1' if atom_id == 'ND1' else 'HE2'

                                seq_key = (auth_asym_id, auth_seq_id, comp_id)

                                if seq_key in auth_to_star_seq:
                                    if auth_asym_id in asym_to_orig_seq:
                                        auth_comp_id = next((_v[1] for _k, _v in asym_to_orig_seq[auth_asym_id].items()
                                                             if _k == (seq_key[1], comp_id)), comp_id)
                                    else:
                                        auth_comp_id = comp_id

                                    row = [None] * len(tags)

                                    row[0] = index

                                    entity_assembly_id, seq_id, _, _ = auth_to_star_seq[seq_key]

                                    row[1], row[4], row[5] =\
                                        entity_assembly_id, auth_comp_id, leaving_atom_id
                                    row[2] = row[3] = seq_id

                                    row[6], row[7], row[8], row[9] =\
                                        auth_asym_id, auth_seq_id, auth_comp_id, leaving_atom_id

                                    row[10], row[11] = 1, self._reg.entry_id

                                    eda_loop.add_data(row)

                                    index += 1

                    asm_sf.add_loop(eda_loop)

        if orig_asm_sf is not None:

            # append extra categories

            if self._reg.retain_original and file_type == 'nmr-star':

                for loop in orig_asm_sf.loops:

                    if loop.category == LP_CATEGORIES[file_type][content_subtype]:
                        continue

                    if loop.category in AUX_LP_CATEGORIES[file_type][content_subtype]:
                        continue

                    asm_sf.add_loop(loop)

            del master_entry[orig_asm_sf]

        for sf in master_entry.frame_list:
            if sf.name == sf_framecode:
                master_entry.remove_saveframe(sf.name)
                break

        master_entry.add_saveframe(asm_sf)

        return True, asm_sf

    def updateEntitySaveframe(self) -> bool:
        """ Update entity saveframe(s).
        """

        input_source = self._reg.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        master_entry = self._reg.star_data[0]

        cif_poly_seq = self._reg.caC['polymer_sequence']
        entity_assembly = self._reg.caC['entity_assembly']

        # refresh _Entity saveframe

        content_subtype = 'entity'

        ent_sfs = master_entry.get_saveframes_by_category(SF_CATEGORIES[file_type][content_subtype])

        for sf in reversed(ent_sfs):
            master_entry.remove_saveframe(sf.name)

        entity_ids = []

        for item in entity_assembly:
            entity_id = item['entity_id']

            if entity_id in entity_ids:
                continue

            entity_ids.append(entity_id)

            entity_type = item['entity_type']

            sf_framecode = f'entity_{entity_id}' if entity_type not in ('non-polymer', 'water') else f"entity_{item['comp_id']}"

            ent_sf = pynmrstar.Saveframe.from_scratch(sf_framecode)
            ent_sf.set_tag_prefix(SF_TAG_PREFIXES[file_type][content_subtype])
            ent_sf.add_tag('Sf_category', SF_CATEGORIES[file_type][content_subtype])
            ent_sf.add_tag('Sf_framecode', sf_framecode)
            ent_sf.add_tag('Entry_ID', self._reg.entry_id)
            ent_sf.add_tag('ID', entity_id)
            ent_sf.add_tag('BMRB_code', None if entity_type not in ('non-polymer', 'water') else item['comp_id'])
            ent_sf.add_tag('Name', item['entity_desc'])
            ent_sf.add_tag('Type', entity_type)

            if entity_type == 'polymer':
                poly_type = item['entity_poly_type']
                if poly_type.startswith('polypeptide'):
                    common_type = 'protein'
                elif any(True for comp_id in item['comp_id_set'] if comp_id in ('DA', 'DC', 'DG', 'DT'))\
                        and any(True for comp_id in item['comp_id_set'] if comp_id in ('A', 'C', 'G', 'U')):
                    common_type = 'DNA/RNA hybrid'
                elif poly_type == 'polydeoxyribonucleotide':
                    common_type = 'DNA'
                elif poly_type == 'polyribonucleotide':
                    common_type = 'RNA'
                else:
                    common_type = None
            elif entity_type == 'branched':
                common_type = 'polysaccharide'
            else:
                common_type = None
            ent_sf.add_tag('Polymer_common_type', common_type)

            if entity_type == 'polymer':
                poly_type = item['entity_poly_type']
                if poly_type.startswith('polypeptide'):
                    _poly_type = poly_type

                    if self._reg.cR.hasCategory('struct_conn'):
                        auth_asym_ids = item['auth_asym_id'].split(',')

                        bonds = self._reg.cR.getDictList('struct_conn')

                        for bond in bonds:

                            try:

                                auth_asym_id_1 = bond['ptnr1_auth_asym_id']
                                auth_seq_id_1 = int(bond['ptnr1_auth_seq_id'])
                                atom_id_1 = bond['ptnr1_label_atom_id']
                                auth_asym_id_2 = bond['ptnr2_auth_asym_id']
                                auth_seq_id_2 = int(bond['ptnr2_auth_seq_id'])
                                atom_id_2 = bond['ptnr2_label_atom_id']

                                if auth_asym_id_1 == auth_asym_id_2 and auth_asym_id_1 in auth_asym_ids\
                                   and {atom_id_1, atom_id_2} == {'C', 'N'} and abs(auth_seq_id_1 - auth_seq_id_2) > 1:
                                    _poly_type = 'cyclic-pseudo-peptide'

                            except ValueError:
                                continue

                elif any(True for comp_id in item['comp_id_set'] if comp_id in ('DA', 'DC', 'DG', 'DT'))\
                        and any(True for comp_id in item['comp_id_set'] if comp_id in ('A', 'C', 'G', 'U')):
                    _poly_type = 'polydeoxyribonucleotide/polyribonucleotide hybrid'
                else:
                    _poly_type = poly_type
            elif entity_type == 'branched':
                _poly_type = item['entity_poly_type']
            else:
                _poly_type = None

            ent_sf.add_tag('Polymer_type', _poly_type)
            ent_sf.add_tag('Polymer_type_details', None)

            auth_asym_ids = []
            for _item in entity_assembly:
                if _item['entity_id'] != entity_id:
                    continue
                if _item['auth_asym_id'] in auth_asym_ids:
                    continue
                auth_asym_ids.append(_item['auth_asym_id'])
            auth_asym_id_list = ','.join(auth_asym_ids)
            if len(auth_asym_id_list) > 12 and ',' in auth_asym_id_list:
                last_asym_id = f",..,{auth_asym_id_list.rsplit(',', maxsplit=1)[-1]}"
                max_len = 11 - len(last_asym_id)
                while True:
                    if auth_asym_id_list[max_len] == ',':
                        break
                    max_len -= 1
                auth_asym_id_list = auth_asym_id_list[:max_len] + last_asym_id
            ent_sf.add_tag('Polymer_strand_ID', auth_asym_id_list)

            one_letter_code_can = one_letter_code = None
            nmr_ext_monomers = 0
            nmr_ext_fw = 0.0
            if entity_type == 'polymer':
                one_letter_code_can = item['one_letter_code_can']
                one_letter_code = item['one_letter_code']
                if self._reg.nmr_ext_poly_seq is not None and len(self._reg.nmr_ext_poly_seq) > 0\
                   and any(True for d in self._reg.nmr_ext_poly_seq if d['auth_chain_id'] in auth_asym_ids):
                    ps = next(ps for ps in cif_poly_seq if ps['auth_chain_id'] in auth_asym_ids)
                    auth_seq_ids = list(filter(None, ps['auth_seq_id']))
                    min_auth_seq_id = min(auth_seq_ids)
                    max_auth_seq_id = max(auth_seq_ids)
                    comp_ids = []
                    for d in self._reg.nmr_ext_poly_seq:
                        if d['auth_chain_id'] in auth_asym_ids:
                            if d['auth_seq_id'] < min_auth_seq_id:
                                comp_ids.append(d['auth_comp_id'])
                                nmr_ext_monomers += 1
                                nmr_ext_fw += self._reg.ccU.getEffectiveFormulaWeight(d['auth_comp_id'])
                    comp_ids.extend(ps['comp_id'])
                    for d in self._reg.nmr_ext_poly_seq:
                        if d['auth_chain_id'] in auth_asym_ids:
                            if d['auth_seq_id'] > max_auth_seq_id:
                                comp_ids.append(d['auth_comp_id'])
                                nmr_ext_monomers += 1
                                nmr_ext_fw += self._reg.ccU.getEffectiveFormulaWeight(d['auth_comp_id'])
                    one_letter_code_can = getOneLetterCodeCanSequence(comp_ids)
                    one_letter_code = getOneLetterCodeSequence(comp_ids)

            ent_sf.add_tag('Polymer_seq_one_letter_code_can', None if entity_type != 'polymer' else one_letter_code_can)
            ent_sf.add_tag('Polymer_seq_one_letter_code', None if entity_type != 'polymer' else one_letter_code)
            ent_sf.add_tag('Target_identifier', None if entity_type != 'polymer' else item['target_identifier'])
            ent_sf.add_tag('Polymer_author_defined_seq', None)
            ent_sf.add_tag('Polymer_author_seq_details', None)
            ent_sf.add_tag('Ambiguous_conformational_states', None)
            ent_sf.add_tag('Ambiguous_chem_comp_sites', None)
            ent_sf.add_tag('Nstd_monomer', None if entity_type != 'polymer' else item['nstd_monomer'])
            ent_sf.add_tag('Nstd_chirality', None if entity_type != 'polymer' else item['nstd_chirality'])
            ent_sf.add_tag('Nstd_linkage', None if entity_type != 'polymer' else item['nstd_linkage'])
            ent_sf.add_tag('Nonpolymer_comp_ID', None if entity_type not in ('non-polymer', 'water') else item['comp_id'])
            ent_sf.add_tag('Nonpolymer_comp_label', None if entity_type != 'non-polymer' else f"$chem_comp_{item['comp_id']}")
            ent_sf.add_tag('Number_of_monomers',
                           None if entity_type in ('non-polymer', 'water') else item['num_of_monomers'] + nmr_ext_monomers)
            ent_sf.add_tag('Number_of_nonpolymer_components', None if entity_type not in ('non-polymer', 'water') else 1)
            ent_sf.add_tag('Paramagnetic',
                           'no' if not self._paramag or entity_type not in ('non-polymer', 'water')
                           or item['comp_id'] not in PARAMAGNETIC_ELEMENTS else 'yes')

            _label_asym_id = 'label_asym_id' if 'fixed_label_asym_id' not in item else 'fixed_label_asym_id'

            cys_total = 0
            label_asym_ids = set(item[_label_asym_id].split(','))
            for chain_id in label_asym_ids:
                if entity_type == 'polymer':
                    ps = next(ps for ps in cif_poly_seq if ps['chain_id'] == chain_id)
                    cys_total += ps['comp_id'].count('CYS') + ps['comp_id'].count('DCY')

            if cys_total > 0:
                disul_cys = other_cys = 0
                if self._reg.cR.hasCategory('struct_conn'):
                    bonds = self._reg.cR.getDictList('struct_conn')
                    for bond in bonds:
                        label_asym_id_1 = bond['ptnr1_label_asym_id']
                        auth_comp_id_1 = bond['ptnr1_auth_comp_id']
                        label_asym_id_2 = bond['ptnr2_label_asym_id']
                        atom_id_1 = bond['ptnr1_label_atom_id']
                        auth_comp_id_2 = bond['ptnr2_auth_comp_id']
                        atom_id_2 = bond['ptnr2_label_atom_id']

                        if label_asym_id_1 in label_asym_ids and auth_comp_id_1 in ('CYS', 'DCY') and atom_id_1 == 'SG':
                            if auth_comp_id_2 in ('CYS', 'DCY') and atom_id_2 == 'SG':
                                disul_cys += 1
                            else:
                                other_cys += 1

                        if label_asym_id_2 in label_asym_ids and auth_comp_id_2 in ('CYS', 'DCY') and atom_id_2 == 'SG':
                            if auth_comp_id_1 in ('CYS', 'DCY') and atom_id_1 == 'SG':
                                disul_cys += 1
                            else:
                                other_cys += 1

                free_cys = cys_total - disul_cys - other_cys

                if free_cys > 0:
                    if free_cys == cys_total:
                        thiol_state = 'all free'
                    elif disul_cys > 0 and other_cys > 0:
                        thiol_state = 'free disulfide and other bound'
                    elif other_cys == 0:
                        thiol_state = 'free and disulfide bound'
                    else:
                        thiol_state = 'free and other bound'
                else:
                    if disul_cys > 0 and other_cys > 0:
                        thiol_state = 'disulfide and other bound'
                    elif other_cys == 0:
                        thiol_state = 'all disulfide bound'
                    else:
                        thiol_state = 'all other bound'
            else:
                thiol_state = 'not present'
            ent_sf.add_tag('Thiol_state', thiol_state)
            ent_sf.add_tag('Src_method', item['entity_src_method'])
            ent_sf.add_tag('Parent_entity_ID', None if entity_type != 'polymer' else item['entity_parent'])
            ent_sf.add_tag('Fragment', None if entity_type != 'polymer' else item['entity_fragment'])
            ent_sf.add_tag('Mutation', None if entity_type != 'polymer' else item['entity_mutation'])
            ent_sf.add_tag('EC_number', None if entity_type != 'polymer' else item['entity_ec'])
            ent_sf.add_tag('Calc_isoelectric_point', None)
            ent_sf.add_tag('Formula_weight',
                           item['entity_fw'] if nmr_ext_monomers == 0 else round(item['entity_fw'] + nmr_ext_fw, 3))
            ent_sf.add_tag('Formula_weight_exptl', None)
            ent_sf.add_tag('Formula_weight_exptl_meth', None)
            ent_sf.add_tag('Details', item['entity_details'])
            ent_sf.add_tag('DB_query_date', None)
            ent_sf.add_tag('DB_query_revised_last_date', None)

            # refresh _Entity_common_name loop

            if self._reg.cR.hasCategory('entity_name_com'):
                lp_category = '_Entity_common_name'
                ecn_loop = pynmrstar.Loop.from_scratch(lp_category)

                ecn_key_items = [{'name': 'Name', 'type': 'str'},
                                 {'name': 'Type', 'type': 'enum',
                                  'enum': ('common', 'abbreviation', 'synonym')}
                                 ]
                ecn_data_items = [{'name': 'Entity_ID', 'type': 'pointer-index', 'mandatory': True,
                                   'default': '1', 'default-from': 'parent'},
                                  {'name': 'Entry_ID', 'type': 'str', 'mandatory': False}
                                  ]

                tags = [f"{lp_category}.{_item['name']}" for _item in ecn_key_items]
                tags.extend([f"{lp_category}.{_item['name']}" for _item in ecn_data_items])

                ecn_loop.add_tag(tags)

                ent_name_coms = self._reg.cR.getDictList('entity_name_com')
                for ent_name_com in ent_name_coms:
                    if int(ent_name_com['entity_id']) == entity_id:
                        row = [None] * len(tags)

                        row[0], row[1], row[2], row[3] =\
                            ent_name_com['name'], 'common', entity_id, self._reg.entry_id

                        ecn_loop.add_data(row)

                if not ecn_loop.empty:
                    ent_sf.add_loop(ecn_loop)

            # refresh _Entity_systematic_name loop

            if self._reg.cR.hasCategory('entity_name_sys'):
                lp_category = '_Entity_systematic_name'
                esn_loop = pynmrstar.Loop.from_scratch(lp_category)

                esn_key_items = [{'name': 'Name', 'type': 'str'},
                                 {'name': 'Naming_system', 'type': 'enum',
                                  'enum': ('IUPAC', 'CAS name', 'CAS registry number', 'BMRB',
                                           'Three letter code', 'Pfam', 'Swiss-Prot', 'EC', 'NCBI')}
                                 ]
                esn_data_items = [{'name': 'Entity_ID', 'type': 'pointer-index', 'mandatory': True,
                                   'default': '1', 'default-from': 'parent'},
                                  {'name': 'Entry_ID', 'type': 'str', 'mandatory': False}
                                  ]

                tags = [f"{lp_category}.{_item['name']}" for _item in esn_key_items]
                tags.extend([f"{lp_category}.{_item['name']}" for _item in esn_data_items])

                esn_loop.add_tag(tags)

                ent_name_syss = self._reg.cR.getDictList('entity_name_sys')
                for ent_name_sys in ent_name_syss:
                    if int(ent_name_sys['entity_id']) == entity_id:
                        row = [None] * len(tags)

                        row[0], row[1], row[2], row[3] =\
                            ent_name_sys['name'], ent_name_sys.get('system'), entity_id, self._reg.entry_id

                        esn_loop.add_data(row)

                if not esn_loop.empty:
                    ent_sf.add_loop(esn_loop)

            # refresh _Entity_keyword loop

            if self._reg.cR.hasCategory('entity_keywords'):
                lp_category = '_Entity_keyword'
                ek_loop = pynmrstar.Loop.from_scratch(lp_category)

                ek_key_items = [{'name': 'Keyword', 'type': 'str'}
                                ]
                ek_data_items = [{'name': 'Entity_ID', 'type': 'pointer-index', 'mandatory': True,
                                  'default': '1', 'default-from': 'parent'},
                                 {'name': 'Entry_ID', 'type': 'str', 'mandatory': False}
                                 ]

                tags = [f"{lp_category}.{_item['name']}" for _item in ek_key_items]
                tags.extend([f"{lp_category}.{_item['name']}" for _item in ek_data_items])

                ek_loop.add_tag(tags)

                ent_keys = self._reg.cR.getDictList('entity_keywords')
                for ent_key in ent_keys:
                    if int(ent_key['entity_id']) == entity_id and 'text' in ent_key and ent_key['text'] not in EMPTY_VALUE:
                        row = [None] * len(tags)

                        row[0], row[1], row[2] =\
                            ent_key['text'], entity_id, self._reg.entry_id

                        ek_loop.add_data(row)

                if not ek_loop.empty:
                    ent_sf.add_loop(ek_loop)

            # refresh _Entity_comp_index loop

            lp_category = '_Entity_comp_index'
            eci_loop = pynmrstar.Loop.from_scratch(lp_category)

            eci_key_items = [{'name': 'ID', 'type': 'positive-int'},
                             {'name': 'Auth_seq_ID', 'type': 'int'},
                             {'name': 'Comp_ID', 'type': 'str'}
                             ]
            eci_data_items = [{'name': 'Comp_label', 'type': 'str'},
                              {'name': 'Entity_ID', 'type': 'pointer-index', 'mandatory': True,
                               'default': '1', 'default-from': 'parent'},
                              {'name': 'Entry_ID', 'type': 'str', 'mandatory': False}
                              ]

            tags = [f"{lp_category}.{_item['name']}" for _item in eci_key_items]
            tags.extend([f"{lp_category}.{_item['name']}" for _item in eci_data_items])

            eci_loop.add_tag(tags)

            index = 1

            label_asym_ids = []
            for chain_id in item['label_asym_id'].split(','):
                if chain_id not in label_asym_ids:
                    label_asym_ids.append(chain_id)

            if entity_type == 'non-polymer':
                for _item in entity_assembly:
                    if entity_id != _item['entity_id'] or _item == item:
                        continue
                    for chain_id in _item['label_asym_id'].split(','):
                        if chain_id not in label_asym_ids:
                            label_asym_ids.append(chain_id)

            min_auth_seq_id = max_auth_seq_id = max_seq_id = -1

            for chain_id in label_asym_ids:
                if entity_type == 'polymer':
                    ps = next(ps for ps in cif_poly_seq if ps['chain_id'] == chain_id)
                    auth_seq_ids = list(filter(None, ps['auth_seq_id']))
                    seq_ids = list(filter(None, ps['seq_id']))
                    min_auth_seq_id = min(auth_seq_ids)
                    max_auth_seq_id = max(auth_seq_ids)
                    max_seq_id = max(seq_ids)
                elif entity_type == 'branched':
                    ps = next(ps for ps in self._reg.caC['branched'] if ps['chain_id'] == chain_id)
                else:
                    ps = next(ps for ps in self._reg.caC['non_polymer'] if ps['chain_id'] == chain_id)

                seq_keys = set()

                for auth_seq_id, seq_id, comp_id in zip(ps['auth_seq_id'], ps['seq_id'],
                                                        ps['auth_comp_id'] if 'auth_comp_id' in ps else ps['comp_id']):
                    seq_key = (ps['auth_chain_id'], seq_id)

                    if seq_key in seq_keys:
                        continue

                    if entity_type in ('non-polymer', 'water'):
                        if comp_id != item['comp_id']:
                            continue
                        auth_seq_id = seq_id

                    if entity_type == 'polymer' and self._reg.nmr_ext_poly_seq is not None\
                       and len(self._reg.nmr_ext_poly_seq) > 0\
                       and any(True for d in self._reg.nmr_ext_poly_seq if d['auth_chain_id'] == ps['auth_chain_id']
                               and d['auth_seq_id'] < min_auth_seq_id):
                        for d in self._reg.nmr_ext_poly_seq:
                            auth_asym_id = ps['auth_chain_id']
                            _auth_seq_id = ps['auth_seq_id'][ps['seq_id'].index(seq_id)]
                            if d['auth_chain_id'] == auth_asym_id and d['auth_seq_id'] < _auth_seq_id:
                                _offset = seq_id - _auth_seq_id
                                _seq_id = d['auth_seq_id'] + _offset
                                _seq_key = (auth_asym_id, _seq_id)
                                if _seq_key in seq_keys:
                                    continue
                                seq_keys.add(_seq_key)
                                row = [None] * len(tags)
                                row[0], row[1], row[2] = _seq_id, d['auth_seq_id'], d['auth_comp_id']
                                if d['auth_comp_id'] not in STD_MON_DICT and d['auth_comp_id'] != 'HOH':
                                    row[3] = f"$chem_comp_{d['auth_comp_id']}"
                                row[4], row[5] = entity_id, self._reg.entry_id

                                eci_loop.add_data(row)

                    row = [None] * len(tags)

                    seq_keys.add(seq_key)

                    row[0], row[1], row[2] = seq_id if entity_type == 'polymer' else index, auth_seq_id, comp_id

                    if comp_id not in STD_MON_DICT and comp_id != 'HOH':
                        row[3] = f"$chem_comp_{comp_id}"

                    row[4], row[5] = entity_id, self._reg.entry_id

                    if comp_id not in EMPTY_VALUE:
                        eci_loop.add_data(row)

                    index += 1

            if entity_type == 'polymer' and self._reg.nmr_ext_poly_seq is not None and len(self._reg.nmr_ext_poly_seq) > 0\
               and any(True for d in self._reg.nmr_ext_poly_seq if d['auth_chain_id'] == ps['auth_chain_id']
                       and d['auth_seq_id'] > max_auth_seq_id):
                _offset = max_seq_id - max_auth_seq_id
                for d in self._reg.nmr_ext_poly_seq:
                    auth_asym_id = ps['auth_chain_id']
                    if d['auth_chain_id'] == auth_asym_id and d['auth_seq_id'] > max_auth_seq_id:
                        _seq_id = d['auth_seq_id'] + _offset
                        row = [None] * len(tags)
                        row[0], row[1], row[2] = _seq_id, d['auth_seq_id'], d['auth_comp_id']
                        if d['auth_comp_id'] not in STD_MON_DICT and d['auth_comp_id'] != 'HOH':
                            row[3] = f"$chem_comp_{d['auth_comp_id']}"
                        row[4], row[5] = entity_id, self._reg.entry_id

                        eci_loop.add_data(row)

            ent_sf.add_loop(eci_loop)

            # refresh _Entity_poly_seq loop

            if entity_type not in ('non-polymer', 'water'):
                lp_category = '_Entity_poly_seq'
                eps_loop = pynmrstar.Loop.from_scratch(lp_category)

                eps_key_items = [{'name': 'Hetero', 'type': 'str'},
                                 {'name': 'Mon_ID', 'type': 'str'},
                                 {'name': 'Num', 'type': 'int'},
                                 {'name': 'Comp_index_ID', 'type': 'int'}
                                 ]
                eps_data_items = [{'name': 'Entity_ID', 'type': 'pointer-index', 'mandatory': True,
                                   'default': '1', 'default-from': 'parent'},
                                  {'name': 'Entry_ID', 'type': 'str', 'mandatory': False}
                                  ]

                tags = [f"{lp_category}.{_item['name']}" for _item in eps_key_items]
                tags.extend([f"{lp_category}.{_item['name']}" for _item in eps_data_items])

                eps_loop.add_tag(tags)

                seq_keys = set()

                label_asym_ids = list(set(item['label_asym_id'].split(',')))
                for chain_id in sorted(sorted(label_asym_ids), key=len):
                    if entity_type == 'polymer':
                        ps = next(ps for ps in cif_poly_seq if ps['chain_id'] == chain_id)
                        auth_seq_ids = list(filter(None, ps['auth_seq_id']))
                        seq_ids = list(filter(None, ps['seq_id']))
                        min_auth_seq_id = min(auth_seq_ids)
                        max_auth_seq_id = max(auth_seq_ids)
                        max_seq_id = max(seq_ids)
                    else:  # 'branched':
                        ps = next(ps for ps in self._reg.caC['branched'] if ps['chain_id'] == chain_id)

                    for seq_id, comp_id in zip(ps['seq_id'], ps['auth_comp_id'] if 'auth_comp_id' in ps else ps['comp_id']):
                        seq_key = (ps['auth_chain_id'], seq_id)

                        if seq_key in seq_keys:
                            continue

                        if entity_type in ('non-polymer', 'water'):
                            if comp_id != item['comp_id']:
                                continue

                        if entity_type == 'polymer' and self._reg.nmr_ext_poly_seq is not None\
                           and len(self._reg.nmr_ext_poly_seq) > 0\
                           and any(True for d in self._reg.nmr_ext_poly_seq if d['auth_chain_id'] == ps['auth_chain_id']
                                   and d['auth_seq_id'] < min_auth_seq_id):
                            for d in self._reg.nmr_ext_poly_seq:
                                auth_asym_id = ps['auth_chain_id']
                                auth_seq_id = ps['auth_seq_id'][ps['seq_id'].index(seq_id)]
                                if d['auth_chain_id'] == auth_asym_id and d['auth_seq_id'] < auth_seq_id:
                                    _offset = seq_id - auth_seq_id
                                    _seq_id = d['auth_seq_id'] + _offset
                                    _seq_key = (auth_asym_id, _seq_id)
                                    if _seq_key in seq_keys:
                                        continue
                                    seq_keys.add(_seq_key)
                                    row = [None] * len(tags)
                                    row[1], row[2], row[3], row[4], row[5] =\
                                        d['auth_comp_id'], _seq_id, _seq_id, entity_id, self._reg.entry_id

                                    eps_loop.add_data(row)

                        row = [None] * len(tags)

                        seq_keys.add(seq_key)

                        row[1], row[4], row[5] = comp_id, entity_id, self._reg.entry_id
                        row[2] = row[3] = seq_id

                        if comp_id not in EMPTY_VALUE:
                            eps_loop.add_data(row)

                    if entity_type == 'polymer' and self._reg.nmr_ext_poly_seq is not None\
                       and len(self._reg.nmr_ext_poly_seq) > 0\
                       and any(True for d in self._reg.nmr_ext_poly_seq if d['auth_chain_id'] == ps['auth_chain_id']
                               and d['auth_seq_id'] > max_auth_seq_id):
                        _offset = max_seq_id - max_auth_seq_id
                        for d in self._reg.nmr_ext_poly_seq:
                            auth_asym_id = ps['auth_chain_id']
                            if d['auth_chain_id'] == auth_asym_id and d['auth_seq_id'] > max_auth_seq_id:
                                _seq_id = d['auth_seq_id'] + _offset
                                row = [None] * len(tags)
                                row[1], row[2], row[3], row[4], row[5] =\
                                    d['auth_comp_id'], _seq_id, _seq_id, entity_id, self._reg.entry_id

                                eps_loop.add_data(row)

                ent_sf.add_loop(eps_loop)

            master_entry.add_saveframe(ent_sf)
