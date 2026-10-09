##
# File: NmrDpValidationMr.py
# Date: 17-Aug-2026
#
# Updates:
##
""" NMR-STAR restraint validation for NMR data validation.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.3"

import copy
import functools
import itertools
from typing import Union

import pynmrstar

try:
    from wwpdb.utils.nmr.NmrDpConstant import (INDEX_TAGS,
                                               SF_ALLOWED_TAGS,
                                               LINKED_LP_CATEGORIES,
                                               ITEM_NAMES_IN_DIST_LOOP,
                                               ITEM_NAMES_IN_DIHED_LOOP,
                                               ITEM_NAMES_IN_RDC_LOOP,
                                               LOW_SEQ_COVERAGE,
                                               EMPTY_VALUE,
                                               PROTON_BEGIN_CODE,
                                               RDC_BB_PAIR_CODE,
                                               ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                               PERIPH_OFFSET_ATTEMPT,
                                               CONCAT_SEQ_ID_INS_CODE_PAT,
                                               NMR_STAR_LP_KEY_ITEMS,
                                               NMR_STAR_LP_DATA_ITEMS,
                                               NMR_STAR_LP_DATA_ITEMS_INS_CODE)
    from wwpdb.utils.nmr.AlignUtil import (alignPolymerSequence,
                                           assignPolymerSequence)
    from wwpdb.utils.nmr.CifToNmrStar import (has_key_value,
                                              get_first_sf_tag,
                                              set_sf_tag)
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (isIdenticalRestraint,
                                                       isAmbigAtomSelection,
                                                       getRestraintName,
                                                       incListIdCounter,
                                                       getSaveframe,
                                                       getLoop,
                                                       getRowForStrMr,
                                                       assignCoordPolymerSequenceWithChainId,
                                                       selectCoordAtoms,
                                                       getPotentialType,
                                                       getRdcCode)
    from wwpdb.utils.nmr.NmrDpValidationBase import NmrDpValidationBase
except ImportError:
    from nmr.NmrDpConstant import (INDEX_TAGS,
                                   SF_ALLOWED_TAGS,
                                   LINKED_LP_CATEGORIES,
                                   ITEM_NAMES_IN_DIST_LOOP,
                                   ITEM_NAMES_IN_DIHED_LOOP,
                                   ITEM_NAMES_IN_RDC_LOOP,
                                   LOW_SEQ_COVERAGE,
                                   EMPTY_VALUE,
                                   PROTON_BEGIN_CODE,
                                   RDC_BB_PAIR_CODE,
                                   ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                   PERIPH_OFFSET_ATTEMPT,
                                   CONCAT_SEQ_ID_INS_CODE_PAT,
                                   NMR_STAR_LP_KEY_ITEMS,
                                   NMR_STAR_LP_DATA_ITEMS,
                                   NMR_STAR_LP_DATA_ITEMS_INS_CODE)
    from nmr.AlignUtil import (alignPolymerSequence,
                               assignPolymerSequence)
    from nmr.CifToNmrStar import (has_key_value,
                                  get_first_sf_tag,
                                  set_sf_tag)
    from nmr.mr.ParserListenerUtil import (isIdenticalRestraint,
                                           isAmbigAtomSelection,
                                           getRestraintName,
                                           incListIdCounter,
                                           getSaveframe,
                                           getLoop,
                                           getRowForStrMr,
                                           assignCoordPolymerSequenceWithChainId,
                                           selectCoordAtoms,
                                           getPotentialType,
                                           getRdcCode)
    from nmr.NmrDpValidationBase import NmrDpValidationBase


class NmrDpValidationMr(NmrDpValidationBase):
    """ NMR-STAR restraint validation for NMR data validation.
    """
    __slots__ = ()

    def validateStrMr(self, file_list_id: int, file_type: str, original_file_name: str, content_subtype: str,
                      _sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                      sf_framecode: str, lp_category: str) -> bool:
        """ Validate data content of NMR-STAR restraint files.
        """

        self._reg.list_id_counter = incListIdCounter(content_subtype, self._reg.list_id_counter, reduced=False)

        list_id = self._reg.list_id_counter[content_subtype]

        restraint_name = getRestraintName(content_subtype)

        _sf_framecode = sf_framecode

        is_sf = True
        if len(sf_framecode) == 0:
            sf_framecode = restraint_name.replace(' ', '_').lower() + f'_{list_id}'
            is_sf = False

        sf = getSaveframe(content_subtype, sf_framecode, list_id, self._reg.entry_id, original_file_name,
                          reduced=False)

        # merge saveframe tags of the source saveframe
        if is_sf:

            origTagNames = [t[0] for t in _sf.tags]
            tagNames = [t[0] for t in sf.tags]

            for idx, origTagName in enumerate(origTagNames):
                if origTagName in SF_ALLOWED_TAGS[file_type][content_subtype]:
                    set_sf_tag(sf, origTagName, _sf.tags[idx][1])

        try:

            loop = _sf if self._reg.star_data_type[file_list_id] == 'Loop' else _sf.get_loop(lp_category)

            if not isinstance(loop, pynmrstar.Loop):
                loop = None

        except KeyError:
            loop = None

        _restraint_name = restraint_name.split()

        sf_item = {'file_type': file_type, 'saveframe': sf, 'list_id': list_id,
                   'id': 0, 'index_id': 0,
                   'constraint_type': ' '.join(_restraint_name[:-1])}

        if content_subtype == 'dist_restraint':
            sf_item['constraint_subsubtype'] = 'simple'

        if loop is not None:

            def get_idx_msg(idx):
                _index_tag = index_tag if index_tag is not None else 'ID'
                try:
                    _index_tag_col = loop.tags.index(_index_tag)
                    idx_msg = f"[Check row of {_index_tag} {loop.data[idx][_index_tag_col]}] "
                except ValueError:
                    _index_tag = 'ID'
                    try:
                        _index_tag_col = loop.tags.index(_index_tag)
                        idx_msg = f"[Check row of {_index_tag} {loop.data[idx][_index_tag_col]}] "
                    except ValueError:
                        _index_tag = 'Index_ID'
                        idx_msg = f"[Check row of {_index_tag} {idx + 1}] "
                return idx_msg

            def report_atom_sel_warn(idx, warn):
                idx_msg = get_idx_msg(idx)

                if warn.startswith('[Atom not found]'):
                    if not self._reg.remediation_mode or 'Macromolecules page' not in warn:
                        self._reg.report.error.appendDescription('atom_not_found',
                                                                 {'file_name': original_file_name,
                                                                  'sf_framecode': sf_framecode,
                                                                  'category': lp_category,
                                                                  'description': idx_msg + warn})

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateStrMr() "
                                                f"++ Error  - {idx_msg + warn}\n")

                elif warn.startswith('[Hydrogen not instantiated]'):
                    self._reg.report.warning.appendDescription('hydrogen_not_instantiated',
                                                               {'file_name': original_file_name,
                                                                'sf_framecode': sf_framecode,
                                                                'category': lp_category,
                                                                'description': idx_msg + warn})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.validateStrMr() "
                                            f"++ Warning  - {idx_msg + warn}\n")

                elif warn.startswith('[Invalid atom nomenclature]'):
                    self._reg.report.error.appendDescription('invalid_atom_nomenclature',
                                                             {'file_name': original_file_name,
                                                              'sf_framecode': sf_framecode,
                                                              'category': lp_category,
                                                              'description': idx_msg + warn})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.validateStrMr() "
                                            f"++ Error  - {idx_msg + warn}\n")

                elif warn.startswith('[Invalid atom selection]') or warn.startswith('[Invalid data]'):
                    self._reg.report.error.appendDescription('invalid_data',
                                                             {'file_name': original_file_name,
                                                              'sf_framecode': sf_framecode,
                                                              'category': lp_category,
                                                              'description': idx_msg + warn})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.validateStrMr() "
                                            f"++ ValueError  - {idx_msg + warn}\n")

            def emit_str_mr_rows(idx, atom_sels):
                if any(True for d in range(atom_dim_num) if atom_sels[d] is None or len(atom_sels[d]) == 0):
                    return

                sf_item['id'] += 1

                if content_subtype == 'dist_restraint':
                    Id = '.'
                    _Id = None
                    if id_col != -1:
                        Id = loop.data[idx][id_col]
                        try:
                            _Id = int(Id)
                        except ValueError:
                            Id = '.'
                    Id = sf_item['id'] if isinstance(Id, str) and Id == '.' else _Id
                    combinationId = '.'
                    if combination_id_col != -1:
                        combinationId = loop.data[idx][combination_id_col]
                        try:
                            int(combinationId)
                        except ValueError:
                            combinationId = '.'
                    memberId = '.'
                    if member_id_col != -1:
                        memberId = loop.data[idx][member_id_col]
                        try:
                            int(memberId)
                        except ValueError:
                            memberId = '.'
                    valid_atom_sels = atom_sels[0] is not None and atom_sels[1] is not None
                    if valid_atom_sels and len(atom_sels[0]) * len(atom_sels[1]) > 1\
                       and (isAmbigAtomSelection(atom_sels[0], self._reg.csStat)
                            or isAmbigAtomSelection(atom_sels[1], self._reg.csStat)):
                        memberId = 0
                    memberLogicCode = '.'
                    if member_logic_code_col != -1:
                        memberLogicCode = loop.data[idx][member_logic_code_col]
                        if memberLogicCode in EMPTY_VALUE:
                            memberLogicCode = '.'
                    memberLogicCode = 'OR' if valid_atom_sels and len(atom_sels[0]) * len(atom_sels[1]) > 1\
                        else memberLogicCode

                    if isinstance(memberId, int):
                        _atom1 = _atom2 = None

                    if valid_atom_sels:
                        for atom1, atom2 in itertools.product(atom_sels[0], atom_sels[1]):
                            if isIdenticalRestraint([atom1, atom2]):
                                continue
                            if isinstance(memberId, int):
                                if _atom1 is None or isAmbigAtomSelection([_atom1, atom1], self._reg.csStat)\
                                   or isAmbigAtomSelection([_atom2, atom2], self._reg.csStat):
                                    memberId += 1
                                    _atom1, _atom2 = atom1, atom2
                            sf_item['index_id'] += 1
                            _row = getRowForStrMr(content_subtype, Id, sf_item['index_id'],
                                                  memberId, memberLogicCode, list_id, self._reg.entry_id,
                                                  loop.tags, loop.data[idx],
                                                  auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                                  [atom1, atom2], self._reg.annotation_mode)
                            lp.add_data(_row)

                    elif atom_sels[0] is not None:
                        atom2 = None
                        for atom1 in atom_sels[0]:
                            sf_item['index_id'] += 1
                            _row = getRowForStrMr(content_subtype, Id, sf_item['index_id'],
                                                  memberId, memberLogicCode, list_id, self._reg.entry_id,
                                                  loop.tags, loop.data[idx],
                                                  auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                                  [atom1, atom2], self._reg.annotation_mode)
                            lp.add_data(_row)

                    elif atom_sels[1] is not None:
                        atom1 = None
                        for atom2 in atom_sels[1]:
                            sf_item['index_id'] += 1
                            _row = getRowForStrMr(content_subtype, Id, sf_item['index_id'],
                                                  memberId, memberLogicCode, list_id, self._reg.entry_id,
                                                  loop.tags, loop.data[idx],
                                                  auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                                  [atom1, atom2], self._reg.annotation_mode)
                            lp.add_data(_row)

                    else:
                        atom1 = atom2 = None
                        sf_item['index_id'] += 1
                        _row = getRowForStrMr(content_subtype, Id, sf_item['index_id'],
                                              memberId, memberLogicCode, list_id, self._reg.entry_id,
                                              loop.tags, loop.data[idx],
                                              auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                              [atom1, atom2], self._reg.annotation_mode)
                        lp.add_data(_row)

                else:

                    sf_item['index_id'] += 1
                    _row = getRowForStrMr(content_subtype, sf_item['id'], sf_item['index_id'],
                                          None, None, list_id, self._reg.entry_id,
                                          loop.tags, loop.data[idx],
                                          auth_to_star_seq, auth_to_orig_seq, auth_to_ins_code, offset_holder,
                                          atom_sels, self._reg.annotation_mode)
                    lp.add_data(_row)

            input_source = self._reg.report.input_sources[file_list_id]
            input_source_dic = input_source.get()

            has_poly_seq_in_lp = has_key_value(input_source_dic, 'polymer_sequence_in_loop')

            if has_poly_seq_in_lp and content_subtype != 'ph_param_data':
                poly_seq_in_lp = input_source_dic['polymer_sequence_in_loop']

                poly_seq = seq_align = chain_assign = br_seq_align = br_chain_assign = np_seq_align = np_chain_assign = None

                if has_poly_seq_in_lp and content_subtype in poly_seq_in_lp:
                    _poly_seq_in_lp = next((_poly_seq_in_lp for _poly_seq_in_lp in poly_seq_in_lp[content_subtype]
                                            if _poly_seq_in_lp['sf_framecode'] == _sf_framecode), None)

                    if _poly_seq_in_lp is not None:
                        list_id = _poly_seq_in_lp['list_id']
                        poly_seq = _poly_seq_in_lp['polymer_sequence']

                        seq_align, _ = alignPolymerSequence(self._reg.pA, self._reg.caC['polymer_sequence'],
                                                            poly_seq, conservative=False)
                        chain_assign, _ = assignPolymerSequence(self._reg.pA, self._reg.ccU, file_type,
                                                                self._reg.caC['polymer_sequence'], poly_seq,
                                                                seq_align)

                        if self._reg.caC['branched'] is not None:
                            br_seq_align, _ = alignPolymerSequence(self._reg.pA, self._reg.caC['branched'],
                                                                   poly_seq, conservative=False)
                            br_chain_assign, _ = assignPolymerSequence(self._reg.pA, self._reg.ccU, file_type,
                                                                       self._reg.caC['branched'], poly_seq,
                                                                       br_seq_align)

                        if self._reg.caC['non_polymer'] is not None:
                            np_seq_align, _ = alignPolymerSequence(self._reg.pA, self._reg.caC['non_polymer'],
                                                                   poly_seq, conservative=False)
                            np_chain_assign, _ = assignPolymerSequence(self._reg.pA, self._reg.ccU, file_type,
                                                                       self._reg.caC['non_polymer'], poly_seq,
                                                                       np_seq_align)

                def get_auth_seq_scheme(chain_id, seq_id):
                    auth_asym_id = auth_seq_id = None

                    if seq_id is not None:

                        if chain_assign is not None:
                            auth_asym_id = next((ca['ref_chain_id'] for ca in chain_assign
                                                 if ca['test_chain_id'] == chain_id), None)
                            if auth_asym_id is not None:
                                sa = next((sa for sa in seq_align
                                           if sa['ref_chain_id'] == auth_asym_id and sa['test_chain_id'] == chain_id
                                           and seq_id in sa['test_seq_id'] and sa['sequence_coverage'] >= LOW_SEQ_COVERAGE), None)
                                if sa is not None:
                                    _ref_seq_id_name = 'ref_auth_seq_id' if 'ref_auth_seq_id' in sa else 'ref_seq_id'
                                    auth_seq_id =\
                                        next((ref_seq_id for ref_seq_id, test_seq_id in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                              if test_seq_id == seq_id), None)

                        if None in (auth_asym_id, auth_seq_id) and br_seq_align is not None:
                            auth_asym_id = next((ca['ref_chain_id'] for ca in br_chain_assign
                                                 if ca['test_chain_id'] == chain_id), None)
                            if auth_asym_id is not None:
                                sa = next((sa for sa in br_seq_align
                                           if sa['ref_chain_id'] == auth_asym_id and sa['test_chain_id'] == chain_id
                                           and seq_id in sa['test_seq_id'] and sa['sequence_coverage'] >= LOW_SEQ_COVERAGE), None)
                                if sa is not None:
                                    _ref_seq_id_name = 'ref_auth_seq_id' if 'ref_auth_seq_id' in sa else 'ref_seq_id'
                                    auth_seq_id =\
                                        next((ref_seq_id for ref_seq_id, test_seq_id in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                              if test_seq_id == seq_id), None)

                        if None in (auth_asym_id, auth_seq_id) and np_seq_align is not None:
                            auth_asym_id = next((ca['ref_chain_id'] for ca in np_chain_assign
                                                 if ca['test_chain_id'] == chain_id), None)
                            if auth_asym_id is not None:
                                sa = next((sa for sa in np_seq_align
                                           if sa['ref_chain_id'] == auth_asym_id and sa['test_chain_id'] == chain_id
                                           and seq_id in sa['test_seq_id'] and sa['sequence_coverage'] >= LOW_SEQ_COVERAGE), None)
                                if sa is not None:
                                    _ref_seq_id_name = 'ref_auth_seq_id' if 'ref_auth_seq_id' in sa else 'ref_seq_id'
                                    auth_seq_id =\
                                        next((ref_seq_id for ref_seq_id, test_seq_id in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                              if test_seq_id == seq_id), None)

                    return auth_asym_id, auth_seq_id

                has_ins_code = False

                if poly_seq is not None:

                    for ps in poly_seq:

                        if has_ins_code:
                            break

                        auth_asym_id, _ = get_auth_seq_scheme(ps['chain_id'], ps['seq_id'][0])

                        if self._reg.caC['polymer_sequence'] is not None\
                           and any(True for cif_ps in self._reg.caC['polymer_sequence']
                                   if cif_ps['auth_chain_id'] == auth_asym_id and 'ins_code' in cif_ps):
                            has_ins_code = True

                        if self._reg.caC['branched'] is not None\
                           and any(True for cif_ps in self._reg.caC['branched']
                                   if cif_ps['auth_chain_id'] == auth_asym_id and 'ins_code' in cif_ps):
                            has_ins_code = True

                        if self._reg.caC['non_polymer'] is not None\
                           and any(True for cif_ps in self._reg.caC['non_polymer']
                                   if cif_ps['auth_chain_id'] == auth_asym_id and 'ins_code' in cif_ps):
                            has_ins_code = True

                lp = getLoop(content_subtype, reduced=False, hasInsCode=has_ins_code)

                sf.add_loop(lp)
                sf_item['loop'] = lp

                index_tag = INDEX_TAGS[file_type][content_subtype]
                id_col = loop.tags.index('ID') if 'ID' in loop.tags else -1
                combination_id_col = member_id_col = member_logic_code_col = upper_limit_col = -1
                auth_comp_id_1_col = auth_comp_id_2_col = torsion_angle_name_col = -1
                if content_subtype == 'dist_restraint':
                    if 'Combination_ID' in loop.tags:
                        combination_id_col = loop.tags.index('Combination_ID')
                    if 'Member_ID' in loop.tags:
                        member_id_col = loop.tags.index('Member_ID')
                    if 'Member_logic_code' in loop.tags:
                        member_logic_code_col = loop.tags.index('Member_logic_code')
                    if 'Distance_upper_bound_val' in loop.tags:
                        upper_limit_col = loop.tags.index('Distance_upper_bound_val')
                    if 'Auth_comp_ID_1' in loop.tags:
                        auth_comp_id_1_col = loop.tags.index('Auth_comp_ID_1')
                    if 'Auth_comp_ID_2' in loop.tags:
                        auth_comp_id_2_col = loop.tags.index('Auth_comp_ID_2')
                elif content_subtype == 'dihed_restraint':
                    if 'Torsion_angle_name' in loop.tags:
                        torsion_angle_name_col = loop.tags.index('Torsion_angle_name')

                key_items = [item['name'] for item in NMR_STAR_LP_KEY_ITEMS[content_subtype]]

                if content_subtype == 'ccr_dd_restraint' and 'Dipole_2_chem_comp_index_ID_2' in loop.tags:
                    key_items = copy.copy(key_items)
                    key_item = next((key_item for key_item in key_items if key_item['name'] == 'Dipole_2_comp_index_ID_2'), None)
                    if key_item is not None:
                        key_item['name'] = 'Dipole_2_chem_comp_index_ID_2'

                len_key_items = len(key_items)

                atom_dim_num = (len_key_items - 1) // 5  # 5 for entity_assembly_id, entity_id, comp_index_id, comp_id, atom_id tags

                if atom_dim_num == 0:
                    err = f"Unexpected key items {key_items} set for processing {lp_category} loop "\
                        f"in {sf_framecode} saveframe of {original_file_name} file."

                    self._reg.report.error.appendDescription('internal_error',
                                                             f"+{self.__class_name__}.validateStrMr() "
                                                             f"++ KeyError  - " + err)

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.validateStrMr() "
                                            f"++ KeyError  - {err}\n")

                    return False

                key_chain_id_names = [key_items[idx] for idx in range(1, len_key_items, 5)]
                key_entity_id_names = [key_items[idx] for idx in range(2, len_key_items, 5)]
                key_seq_id_names = [key_items[idx] for idx in range(3, len_key_items, 5)]
                key_comp_id_names = [key_items[idx] for idx in range(4, len_key_items, 5)]
                key_atom_id_names = [key_items[idx] for idx in range(5, len_key_items, 5)]

                key_tags = key_chain_id_names
                key_tags.extend(key_seq_id_names)
                key_tags.extend(key_comp_id_names)
                key_tags.extend(key_atom_id_names)

                auth_items = [auth_item['name'] for auth_item in NMR_STAR_LP_DATA_ITEMS[content_subtype]
                              if auth_item['name'].startswith('Auth') or 'auth' in auth_item['name']]

                auth_chain_id_names = [auth_item for auth_item in auth_items
                                       if 'asym' in auth_item or 'entity_assembly' in auth_item]
                auth_seq_id_names = [auth_item for auth_item in auth_items if 'seq' in auth_item]
                auth_comp_id_names = [auth_item for auth_item in auth_items if 'comp' in auth_item]
                auth_atom_id_names = [auth_item for auth_item in auth_items if 'atom' in auth_item and 'atom_name' not in auth_item]
                auth_atom_name_names = [auth_item for auth_item in auth_items if 'atom_name' in auth_item]

                auth_pdb_tags = auth_chain_id_names
                auth_pdb_tags.extend(auth_seq_id_names)
                auth_pdb_tags.extend(auth_comp_id_names)
                auth_pdb_tags.extend(auth_atom_id_names)

                coord_atom_site = self._reg.caC['coord_atom_site']
                auth_to_star_seq = self._reg.caC['auth_to_star_seq']
                auth_to_orig_seq = self._reg.caC['auth_to_orig_seq']
                auth_to_ins_code = self._reg.caC['auth_to_ins_code'] if has_ins_code else None
                auth_to_star_seq_ann = self._reg.caC['auth_to_star_seq_ann']
                auth_atom_name_to_id = self._reg.caC['auth_atom_name_to_id']

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self._reg.coord_atom_site_tags else 'ndb_model'

                # split concatenation of auth_seq_id and ins_code (DAOTHER-10418)
                if auth_to_ins_code is not None and len(auth_to_ins_code) > 0\
                   and set(auth_seq_id_names) & set(loop.tags) == set(auth_seq_id_names):
                    auth_dat = loop.get_tag(auth_seq_id_names)

                    if any(True for row in auth_dat if any(True for val in row if isinstance(val, str))):

                        auth_seq_id_cols = [loop.tags.index(auth_seq_id_name) for auth_seq_id_name in auth_seq_id_names]

                        ins_code_names = [auth_item['name'] for auth_item in NMR_STAR_LP_DATA_ITEMS_INS_CODE[content_subtype]
                                          if auth_item['name'].startswith('PDB_ins_code')]

                        for ins_code_name in ins_code_names:
                            if ins_code_name not in loop.tags:
                                loop.add_tag(ins_code_name, update_data=True)

                        ins_code_cols = [loop.tags.index(ins_code_name) for ins_code_name in ins_code_names]

                        for idx, row in enumerate(auth_dat):
                            for col, val in enumerate(row):
                                if isinstance(val, str) and CONCAT_SEQ_ID_INS_CODE_PAT.match(val):
                                    g = CONCAT_SEQ_ID_INS_CODE_PAT.search(val).groups()
                                    loop.data[idx][auth_seq_id_cols[col]] = g[0]
                                    if g[1] not in EMPTY_VALUE:
                                        loop.data[idx][ins_code_cols[col]] = g[1]

                offset_holder = {}

                has_key_seq = False

                if set(key_tags) & set(loop.tags) == set(key_tags):
                    dat = loop.get_tag(key_seq_id_names)
                    if len(dat) > 0:
                        has_key_seq = True
                        for row in dat:
                            try:
                                for d in range(atom_dim_num):
                                    int(row[d])
                            except (ValueError, TypeError):
                                has_key_seq = False
                                break

                has_auth_seq = valid_auth_seq = False

                if set(auth_pdb_tags) & set(loop.tags) == set(auth_pdb_tags):
                    auth_dat = loop.get_tag(auth_pdb_tags)
                    if len(auth_dat) > 0:
                        has_auth_seq = valid_auth_seq = True
                        if self._reg.annotation_mode:  # DAOTHER-10661
                            dat = loop.get_tag(auth_pdb_tags)
                            for row_ in dat:
                                for d in range(atom_dim_num):
                                    try:
                                        int(row_[atom_dim_num + d])
                                    except (ValueError, TypeError):
                                        has_auth_seq = valid_auth_seq = False
                                        break

                        else:
                            for row in auth_dat:
                                try:
                                    for d in range(atom_dim_num):
                                        seq_key = (row[d], int(row[atom_dim_num + d]), row[atom_dim_num * 2 + d])
                                        if seq_key not in auth_to_star_seq_ann:
                                            valid_auth_seq = False
                                            break
                                    if not valid_auth_seq:
                                        break
                                except (ValueError, TypeError):
                                    has_auth_seq = valid_auth_seq = False
                                    break

                if has_key_seq or has_auth_seq:

                    has_auth_atom_name = len(auth_atom_name_names) > 0\
                        and set(auth_atom_name_names) & set(loop.tags) == set(auth_atom_name_names)

                    if valid_auth_seq:

                        if has_auth_atom_name:
                            auth_pdb_tags.extend(auth_atom_name_names)

                        dat = loop.get_tag(auth_pdb_tags)

                        prefer_auth_atom_name = False

                        if (self._reg.annotation_mode or self._reg.native_combined) and len(auth_atom_name_to_id) > 0:

                            count_auth_name = count_auth_id = 0

                            for row_ in dat:

                                for d in range(atom_dim_num):
                                    chain_id = row_[d]
                                    seq_id = int(row_[atom_dim_num + d])
                                    comp_id = row_[atom_dim_num * 2 + d]
                                    atom_id = row_[atom_dim_num * 3 + d]

                                    seq_key = (chain_id, seq_id, comp_id)

                                    try:
                                        auth_to_star_seq[seq_key]  # pylint: disable=pointless-statement
                                    except KeyError:
                                        comp_id =\
                                            next((_auth_comp_id
                                                  for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                  if _auth_asym_id == chain_id and _auth_seq_id == seq_id), comp_id)

                                    if comp_id in auth_atom_name_to_id:
                                        if atom_id in auth_atom_name_to_id[comp_id]:
                                            count_auth_name += 1
                                        if atom_id in auth_atom_name_to_id[comp_id].values():
                                            count_auth_id += 1

                            if count_auth_name + count_auth_id == 0:

                                for row_ in dat:

                                    for d in range(atom_dim_num):
                                        chain_id = row_[d]
                                        seq_id = int(row_[atom_dim_num + d])
                                        comp_id = row_[atom_dim_num * 2 + d]
                                        atom_id = row_[atom_dim_num * 3 + d]

                                        seq_key = (chain_id, seq_id, comp_id)

                                        try:
                                            auth_to_star_seq_ann[seq_key]  # pylint: disable=pointless-statement
                                            _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                                            if _seq_key in coord_atom_site:  # DAOTHER-8817
                                                comp_id = coord_atom_site[_seq_key]['comp_id']
                                        except KeyError:
                                            continue

                                        if comp_id in auth_atom_name_to_id:
                                            if atom_id in auth_atom_name_to_id[comp_id]:
                                                count_auth_name += 1
                                            if atom_id in auth_atom_name_to_id[comp_id].values():
                                                count_auth_id += 1

                            prefer_auth_atom_name = count_auth_name > count_auth_id

                        for idx, row_ in enumerate(dat):
                            atom_sels = [None] * atom_dim_num

                            for d in range(atom_dim_num):
                                chain_id = auth_chain_id = row_[d]
                                seq_id = int(row_[atom_dim_num + d])
                                comp_id = row_[atom_dim_num * 2 + d]
                                atom_id = row_[atom_dim_num * 3 + d]

                                seq_key = (chain_id, seq_id, comp_id)

                                try:

                                    entity_assembly_id, comp_index_id, _, _ = auth_to_star_seq[seq_key]

                                    if self._reg.annotation_mode or self._reg.native_combined:
                                        _auth_asym_id, _auth_seq_id =\
                                            next(((k[0], k[1]) for k, v in auth_to_star_seq.items()
                                                  if v[0] == entity_assembly_id
                                                  and v[1] == comp_index_id and k[2] == comp_id), (None, None))
                                        if _auth_asym_id is not None:
                                            seq_key = (_auth_asym_id, _auth_seq_id, comp_id)
                                            if seq_key in auth_to_star_seq:
                                                chain_id, seq_id = _auth_asym_id, _auth_seq_id

                                except KeyError:
                                    if self._reg.annotation_mode or self._reg.native_combined:
                                        _auth_asym_id, _auth_seq_id =\
                                            next(((k[0], k[1]) for k, v in auth_to_star_seq.items()
                                                  if chain_id.isdigit() and v[0] == int(chain_id)
                                                  and v[1] == seq_id and k[2] == comp_id), (None, None))
                                        if _auth_asym_id is not None:
                                            seq_key = (_auth_asym_id, _auth_seq_id, comp_id)
                                            if seq_key in auth_to_star_seq:
                                                chain_id, seq_id = _auth_asym_id, _auth_seq_id
                                        else:
                                            chain_id =\
                                                next((_auth_asym_id
                                                      for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                      if _auth_seq_id == seq_id and _auth_comp_id == comp_id), chain_id)
                                            seq_key = (chain_id, seq_id, comp_id)
                                            if seq_key in auth_to_star_seq:
                                                row_[d] = chain_id
                                            else:
                                                chain_id, comp_id =\
                                                    next(((_auth_asym_id, _auth_comp_id)
                                                          for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                          if _auth_seq_id == seq_id), (chain_id, comp_id))
                                                seq_key = (chain_id, seq_id, comp_id)
                                                if seq_key in auth_to_star_seq:
                                                    row_[d] = chain_id
                                                    row_[atom_dim_num * 2 + d] = comp_id
                                        if seq_key not in auth_to_star_seq:
                                            comp_id = next((_auth_comp_id
                                                            for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                            if _auth_asym_id == chain_id and _auth_seq_id == seq_id), comp_id)
                                            _auth_seq_id = next((_auth_seq_id
                                                                 for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                                 if _auth_asym_id == chain_id and _auth_comp_id == comp_id), None)
                                            if _auth_seq_id is not None:
                                                seq_key = (chain_id, _auth_seq_id, comp_id)

                                if has_auth_atom_name:
                                    auth_atom_id = row_[atom_dim_num * 4 + d]
                                    if auth_atom_id in EMPTY_VALUE:
                                        auth_atom_id = atom_id
                                else:
                                    auth_atom_id = atom_id

                                _assign, warn = assignCoordPolymerSequenceWithChainId(self._reg.caC, self._reg.nefT,
                                                                                      chain_id, seq_id, comp_id, atom_id)

                                rescued = False

                                if warn is not None:

                                    idx_msg = get_idx_msg(idx)

                                    if warn.startswith('[Atom not found]'):
                                        if not self._reg.remediation_mode or 'Macromolecules page' not in warn:
                                            self._reg.report.error.appendDescription('atom_not_found',
                                                                                     {'file_name': original_file_name,
                                                                                      'sf_framecode': sf_framecode,
                                                                                      'category': lp_category,
                                                                                      'description': idx_msg + warn})

                                            if self._reg.verbose:
                                                self._reg.log.write(f"+{self.__class_name__}.validateStrMr() "
                                                                    f"++ Error  - {idx_msg + warn}\n")

                                    if content_subtype != 'dihed_restraint' or not self._reg.remediation_mode:
                                        continue

                                    if d not in (0, 3) or not warn.startswith('[Atom not found]'):
                                        _d = 1 if d == 0 else 2
                                        _chain_id = row_[_d]
                                        _seq_id = int(row_[atom_dim_num + _d])
                                        _comp_id = row_[atom_dim_num * 2 + _d]
                                        _atom_id = row_[atom_dim_num * 3 + _d]

                                        if chain_id != _chain_id or abs(seq_id - _seq_id) != 1:
                                            continue

                                        if not self._reg.ccU.updateChemCompDict(comp_id.upper()):
                                            continue

                                        cca = next((cca for cca in self._reg.ccU.lastAtomDictList
                                                    if cca['atom_id'] == atom_id.upper()), None)

                                        if cca is None:
                                            continue

                                        __assign, _warn =\
                                            assignCoordPolymerSequenceWithChainId(self._reg.caC, self._reg.nefT,
                                                                                  _chain_id, _seq_id, _comp_id, _atom_id)

                                        if len(__assign) != 1 or _warn is not None:
                                            continue

                                        chainId, cifSeqId, _, _ = __assign[0]
                                        cifSeqId -= _seq_id - seq_id

                                        atom_sels[d] = [{'chain_id': chainId,
                                                         'seq_id': cifSeqId,
                                                         'comp_id': comp_id.upper(),
                                                         'atom_id': atom_id.upper(),
                                                         'auth_atom_id': auth_atom_id}]
                                        warn = None

                                        rescued = True

                                if not rescued:
                                    enableWarning = True
                                    if content_subtype == 'dist_restraint':
                                        if (auth_comp_id_1_col != -1 and loop.data[idx][auth_comp_id_1_col] == 'HOH')\
                                           or (auth_comp_id_2_col != -1 and loop.data[idx][auth_comp_id_2_col] == 'HOH'):
                                            enableWarning = False
                                    elif content_subtype == 'dihed_restraint':
                                        if torsion_angle_name_col != -1 and loop.data[idx][torsion_angle_name_col] == 'PPA':
                                            enableWarning = False

                                    atom_sels[d], warn = selectCoordAtoms(self._reg.cR, self._reg.caC, self._reg.nefT, _assign,
                                                                          auth_chain_id, seq_id, comp_id, atom_id, auth_atom_id,
                                                                          allowAmbig=content_subtype in ('dist_restraint',
                                                                                                         'noepk_restraint'),
                                                                          enableWarning=enableWarning,
                                                                          preferAuthAtomName=prefer_auth_atom_name
                                                                          and comp_id in auth_atom_name_to_id,
                                                                          representativeModelId=self._reg.representative_model_id,
                                                                          representativeAltId=self._reg.representative_alt_id,
                                                                          modelNumName=model_num_name)

                                if warn is not None:

                                    report_atom_sel_warn(idx, warn)

                                    continue

                            emit_str_mr_rows(idx, atom_sels)

                    else:

                        if has_auth_atom_name:
                            key_tags.extend(auth_atom_name_names)

                        dat = loop.get_tag(key_tags)

                        prefer_auth_atom_name = False

                        if (self._reg.annotation_mode or self._reg.native_combined) and len(auth_atom_name_to_id) > 0:

                            count_auth_name = count_auth_id = 0

                            for row_ in dat:

                                for d in range(atom_dim_num):
                                    chain_id = row_[d]
                                    seq_id = int(row_[atom_dim_num + d])
                                    comp_id = row_[atom_dim_num * 2 + d]
                                    atom_id = row_[atom_dim_num * 3 + d]

                                    seq_key = (chain_id, seq_id, comp_id)

                                    try:

                                        entity_assembly_id, comp_index_id, _, _ = auth_to_star_seq[seq_key]

                                        _auth_asym_id, _auth_seq_id =\
                                            next(((k[0], k[1]) for k, v in auth_to_star_seq.items()
                                                  if v[0] == entity_assembly_id
                                                  and v[1] == comp_index_id and k[2] == comp_id), (None, None))
                                        if _auth_asym_id is not None:
                                            seq_key = (_auth_asym_id, _auth_seq_id, comp_id)
                                            if seq_key in auth_to_star_seq:
                                                chain_id, seq_id = _auth_asym_id, _auth_seq_id

                                    except KeyError:
                                        _auth_asym_id, _auth_seq_id =\
                                            next(((k[0], k[1]) for k, v in auth_to_star_seq.items()
                                                  if chain_id.isdigit() and v[0] == int(chain_id)
                                                  and v[1] == seq_id and k[2] == comp_id), (None, None))
                                        if _auth_asym_id is not None:
                                            seq_key = (_auth_asym_id, _auth_seq_id, comp_id)
                                            if seq_key in auth_to_star_seq:
                                                chain_id, seq_id = _auth_asym_id, _auth_seq_id
                                        else:
                                            chain_id = next((_auth_asym_id
                                                             for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                             if _auth_seq_id == seq_id and _auth_comp_id == comp_id), chain_id)
                                            seq_key = (chain_id, seq_id, comp_id)
                                            if seq_key in auth_to_star_seq:
                                                row_[d] = chain_id
                                            else:
                                                chain_id, comp_id =\
                                                    next(((_auth_asym_id, _auth_comp_id)
                                                          for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                          if _auth_seq_id == seq_id), (chain_id, comp_id))
                                                seq_key = (chain_id, seq_id, comp_id)
                                                if seq_key in auth_to_star_seq:
                                                    row_[d] = chain_id
                                                    row_[atom_dim_num * 2 + d] = comp_id
                                        if seq_key not in auth_to_star_seq:
                                            comp_id = next((_auth_comp_id
                                                            for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                            if _auth_asym_id == chain_id and _auth_seq_id == seq_id), comp_id)
                                            _auth_seq_id = next((_auth_seq_id
                                                                 for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                                 if _auth_asym_id == chain_id and _auth_comp_id == comp_id), None)
                                            if _auth_seq_id is not None:
                                                seq_key = (chain_id, _auth_seq_id, comp_id)

                                    if comp_id in auth_atom_name_to_id:
                                        if atom_id in auth_atom_name_to_id[comp_id]:
                                            count_auth_name += 1
                                        if atom_id in auth_atom_name_to_id[comp_id].values():
                                            count_auth_id += 1

                            if count_auth_name + count_auth_id == 0:

                                for row_ in dat:

                                    for d in range(atom_dim_num):
                                        chain_id = row_[d]
                                        seq_id = int(row_[atom_dim_num + d])
                                        comp_id = row_[atom_dim_num * 2 + d]
                                        atom_id = row_[atom_dim_num * 3 + d]

                                        seq_key = (chain_id, seq_id, comp_id)

                                        try:
                                            auth_to_star_seq_ann[seq_key]  # pylint: disable=pointless-statement
                                            _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                                            if _seq_key in coord_atom_site:  # DAOTHER-8817
                                                comp_id = coord_atom_site[_seq_key]['comp_id']
                                        except KeyError:
                                            continue

                                        if comp_id in auth_atom_name_to_id:
                                            if atom_id in auth_atom_name_to_id[comp_id]:
                                                count_auth_name += 1
                                            if atom_id in auth_atom_name_to_id[comp_id].values():
                                                count_auth_id += 1

                            prefer_auth_atom_name = count_auth_name > count_auth_id

                        for idx, row_ in enumerate(dat):
                            atom_sels = [None] * atom_dim_num

                            for d in range(atom_dim_num):
                                chain_id = auth_chain_id = row_[d]
                                seq_id = int(row_[atom_dim_num + d])
                                comp_id = row_[atom_dim_num * 2 + d]
                                atom_id = row_[atom_dim_num * 3 + d]

                                seq_key = (chain_id, seq_id, comp_id)

                                try:

                                    entity_assembly_id, comp_index_id, _, _ = auth_to_star_seq[seq_key]

                                    if self._reg.annotation_mode or self._reg.native_combined:
                                        _auth_asym_id, _auth_seq_id =\
                                            next(((k[0], k[1]) for k, v in auth_to_star_seq.items()
                                                  if v[0] == entity_assembly_id
                                                  and v[1] == comp_index_id and k[2] == comp_id), (None, None))
                                        if _auth_asym_id is not None:
                                            seq_key = (_auth_asym_id, _auth_seq_id, comp_id)
                                            if seq_key in auth_to_star_seq:
                                                chain_id, seq_id = _auth_asym_id, _auth_seq_id

                                except KeyError:
                                    if self._reg.annotation_mode or self._reg.native_combined:
                                        _auth_asym_id, _auth_seq_id =\
                                            next(((k[0], k[1]) for k, v in auth_to_star_seq.items()
                                                  if chain_id.isdigit() and v[0] == int(chain_id)
                                                  and v[1] == seq_id and k[2] == comp_id), (None, None))
                                        if _auth_asym_id is not None:
                                            seq_key = (_auth_asym_id, _auth_seq_id, comp_id)
                                            if seq_key in auth_to_star_seq:
                                                chain_id, seq_id = _auth_asym_id, _auth_seq_id
                                        else:
                                            chain_id = next((_auth_asym_id
                                                             for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                             if _auth_seq_id == seq_id and _auth_comp_id == comp_id), chain_id)
                                            seq_key = (chain_id, seq_id, comp_id)
                                            if seq_key in auth_to_star_seq:
                                                row_[d] = chain_id
                                            else:
                                                chain_id, comp_id =\
                                                    next(((_auth_asym_id, _auth_comp_id)
                                                          for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                          if _auth_seq_id == seq_id), (chain_id, comp_id))
                                                seq_key = (chain_id, seq_id, comp_id)
                                                if seq_key in auth_to_star_seq:
                                                    row_[d] = chain_id
                                                    row_[atom_dim_num * 2 + d] = comp_id
                                        if seq_key not in auth_to_star_seq:
                                            comp_id = next((_auth_comp_id
                                                            for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                            if _auth_asym_id == chain_id and _auth_seq_id == seq_id), comp_id)
                                            _auth_seq_id = next((_auth_seq_id
                                                                 for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                                 if _auth_asym_id == chain_id and _auth_comp_id == comp_id), None)
                                            if _auth_seq_id is not None:
                                                seq_key = (chain_id, _auth_seq_id, comp_id)

                                if has_auth_atom_name:
                                    auth_atom_id = row_[atom_dim_num * 4 + d]
                                    if auth_atom_id in EMPTY_VALUE:
                                        auth_atom_id = atom_id
                                else:
                                    auth_atom_id = atom_id

                                auth_asym_id = auth_seq_id = None

                                if chain_assign is not None:
                                    auth_asym_id = next((ca['ref_chain_id'] for ca in chain_assign
                                                         if ca['test_chain_id'] == chain_id), None)
                                    if auth_asym_id is not None:
                                        sa = next((sa for sa in seq_align
                                                   if sa['ref_chain_id'] == auth_asym_id and sa['test_chain_id'] == chain_id
                                                   and seq_id in sa['test_seq_id']), None)
                                        if sa is not None:
                                            _ref_seq_id_name = 'ref_auth_seq_id' if 'ref_auth_seq_id' in sa else 'ref_seq_id'
                                            auth_seq_id = next((ref_seq_id for ref_seq_id, test_seq_id
                                                                in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                                                if test_seq_id == seq_id), None)
                                            if auth_seq_id is None:
                                                for offset in range(1, PERIPH_OFFSET_ATTEMPT):
                                                    auth_seq_id = next((ref_seq_id for ref_seq_id, test_seq_id
                                                                        in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                                                        if test_seq_id == seq_id + offset), None)
                                                    if auth_seq_id is not None:
                                                        auth_seq_id -= offset
                                                        break
                                                    auth_seq_id = next((ref_seq_id for ref_seq_id, test_seq_id
                                                                        in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                                                        if test_seq_id == seq_id - offset), None)
                                                    if auth_seq_id is not None:
                                                        auth_seq_id += offset
                                                        break

                                if None in (auth_asym_id, auth_seq_id) and br_seq_align is not None:
                                    auth_asym_id = next((ca['ref_chain_id'] for ca in br_chain_assign
                                                         if ca['test_chain_id'] == chain_id), None)
                                    if auth_asym_id is not None:
                                        sa = next((sa for sa in br_seq_align
                                                   if sa['ref_chain_id'] == auth_asym_id and sa['test_chain_id'] == chain_id
                                                   and seq_id in sa['test_seq_id']), None)
                                        if sa is not None:
                                            _ref_seq_id_name = 'ref_auth_seq_id' if 'ref_auth_seq_id' in sa else 'ref_seq_id'
                                            auth_seq_id = next((ref_seq_id for ref_seq_id, test_seq_id
                                                                in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                                                if test_seq_id == seq_id), None)

                                if None in (auth_asym_id, auth_seq_id) and np_seq_align is not None:
                                    auth_asym_id = next((ca['ref_chain_id'] for ca in np_chain_assign
                                                         if ca['test_chain_id'] == chain_id), None)
                                    if auth_asym_id is not None:
                                        sa = next((sa for sa in np_seq_align
                                                   if sa['ref_chain_id'] == auth_asym_id and sa['test_chain_id'] == chain_id
                                                   and seq_id in sa['test_seq_id']), None)
                                        if sa is not None:
                                            _ref_seq_id_name = 'ref_auth_seq_id' if 'ref_auth_seq_id' in sa else 'ref_seq_id'
                                            auth_seq_id = next((ref_seq_id for ref_seq_id, test_seq_id
                                                                in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                                                if test_seq_id == seq_id), None)

                                if None in (auth_asym_id, auth_seq_id):
                                    if seq_key in auth_to_star_seq:
                                        auth_asym_id, auth_seq_id, _ = seq_key
                                    else:
                                        entity_id_name = key_entity_id_names[d]
                                        if entity_id_name not in loop.tags:
                                            continue
                                        try:
                                            entity_assembly_id = int(chain_id)
                                            entity_id = int(loop.data[idx][loop.tags.index(entity_id_name)])
                                        except ValueError:
                                            continue
                                        k = next((k for k, v in auth_to_star_seq.items()
                                                  if v[0] == entity_assembly_id and v[1] == seq_id and v[2] == entity_id), None)
                                        if k is None:
                                            continue
                                        auth_asym_id, auth_seq_id, _ = k

                                chain_id, seq_id = auth_asym_id, auth_seq_id

                                _assign, warn = assignCoordPolymerSequenceWithChainId(self._reg.caC, self._reg.nefT,
                                                                                      chain_id, seq_id, comp_id, atom_id)

                                if warn is not None:

                                    idx_msg = get_idx_msg(idx)

                                    if warn.startswith('[Atom not found]'):
                                        if not self._reg.remediation_mode or 'Macromolecules page' not in warn:
                                            self._reg.report.error.appendDescription('atom_not_found',
                                                                                     {'file_name': original_file_name,
                                                                                      'sf_framecode': sf_framecode,
                                                                                      'category': lp_category,
                                                                                      'description': idx_msg + warn})

                                            if self._reg.verbose:
                                                self._reg.log.write(f"+{self.__class_name__}.validateStrMr() "
                                                                    f"++ Error  - {idx_msg + warn}\n")

                                    continue

                                enableWarning = True
                                if content_subtype == 'dist_restraint':
                                    if (auth_comp_id_1_col != -1 and loop.data[idx][auth_comp_id_1_col] == 'HOH')\
                                       or (auth_comp_id_2_col != -1 and loop.data[idx][auth_comp_id_2_col] == 'HOH'):
                                        enableWarning = False
                                elif content_subtype == 'dihed_restraint':
                                    if torsion_angle_name_col != -1 and loop.data[idx][torsion_angle_name_col] == 'PPA':
                                        enableWarning = False

                                atom_sels[d], warn = selectCoordAtoms(self._reg.cR, self._reg.caC, self._reg.nefT, _assign,
                                                                      auth_chain_id, seq_id, comp_id, atom_id, auth_atom_id,
                                                                      allowAmbig=content_subtype in ('dist_restraint',
                                                                                                     'noepk_restraint'),
                                                                      enableWarning=enableWarning,
                                                                      preferAuthAtomName=prefer_auth_atom_name,
                                                                      representativeModelId=self._reg.representative_model_id,
                                                                      representativeAltId=self._reg.representative_alt_id,
                                                                      modelNumName=model_num_name)

                                if warn is not None:

                                    report_atom_sel_warn(idx, warn)

                                    continue

                            emit_str_mr_rows(idx, atom_sels)

                else:  # nothing to do because of insufficient sequence tags

                    del sf[lp]
                    lp = loop

                    sf.add_loop(lp)
                    sf_item['loop'] = lp

            elif content_subtype == 'ph_param_data':

                lp = getLoop(content_subtype, reduced=False, hasInsCode=False)

                sf.add_loop(lp)
                sf_item['loop'] = lp

                for row in loop:
                    sf_item['id'] += 1
                    sf_item['index_id'] += 1

                    _row = getRowForStrMr(content_subtype, sf_item['id'], sf_item['index_id'],
                                          None, None, list_id, self._reg.entry_id,
                                          loop.tags, row,
                                          {}, {}, {}, {},
                                          [None], self._reg.annotation_mode)
                    lp.add_data(_row)

            else:

                auth_to_star_seq = self._reg.caC['auth_to_star_seq']

                key_items = [item['name'] for item in NMR_STAR_LP_KEY_ITEMS[content_subtype]]

                if content_subtype == 'ccr_dd_restraint' and 'Dipole_2_chem_comp_index_ID_2' in loop.tags:
                    key_items = copy.copy(key_items)
                    key_item = next((key_item for key_item in key_items if key_item['name'] == 'Dipole_2_comp_index_ID_2'), None)
                    if key_item is not None:
                        key_item['name'] = 'Dipole_2_chem_comp_index_ID_2'

                len_key_items = len(key_items)

                atom_dim_num = (len_key_items - 1) // 5  # 5 for entity_assembly_id, entity_id, comp_index_id, comp_id, atom_id tags

                if atom_dim_num == 0:
                    err = f"Unexpected key items {key_items} set for processing {lp_category} loop "\
                        f"in {sf_framecode} saveframe of {original_file_name} file."

                    self._reg.report.error.appendDescription('internal_error',
                                                             f"+{self.__class_name__}.validateStrMr() "
                                                             f"++ KeyError  - " + err)

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.validateStrMr() "
                                            f"++ KeyError  - {err}\n")

                    return False

                prefer_auth_atom_name = True

                coord_atom_site = self._reg.caC['coord_atom_site']
                auth_to_orig_seq = self._reg.caC['auth_to_orig_seq']
                auth_to_ins_code = None

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self._reg.coord_atom_site_tags else 'ndb_model'

                offset_holder = {}

                index_tag = INDEX_TAGS[file_type][content_subtype]
                id_col = loop.tags.index('ID') if 'ID' in loop.tags else -1
                combination_id_col = member_id_col = member_logic_code_col = upper_limit_col = -1
                auth_comp_id_1_col = auth_comp_id_2_col = torsion_angle_name_col = -1
                if content_subtype == 'dist_restraint':
                    if 'Combination_ID' in loop.tags:
                        combination_id_col = loop.tags.index('Combination_ID')
                    if 'Member_ID' in loop.tags:
                        member_id_col = loop.tags.index('Member_ID')
                    if 'Member_logic_code' in loop.tags:
                        member_logic_code_col = loop.tags.index('Member_logic_code')
                    if 'Distance_upper_bound_val' in loop.tags:
                        upper_limit_col = loop.tags.index('Distance_upper_bound_val')
                    if 'Auth_comp_ID_1' in loop.tags:
                        auth_comp_id_1_col = loop.tags.index('Auth_comp_ID_1')
                    if 'Auth_comp_ID_2' in loop.tags:
                        auth_comp_id_2_col = loop.tags.index('Auth_comp_ID_2')
                elif content_subtype == 'dihed_restraint':
                    if 'Torsion_angle_name' in loop.tags:
                        torsion_angle_name_col = loop.tags.index('Torsion_angle_name')

                auth_items = [auth_item['name'] for auth_item in NMR_STAR_LP_DATA_ITEMS[content_subtype]
                              if auth_item['name'].startswith('Auth') or 'auth' in auth_item['name']]

                auth_chain_id_names = [auth_item for auth_item in auth_items
                                       if 'asym' in auth_item or 'entity_assembly' in auth_item]
                auth_seq_id_names = [auth_item for auth_item in auth_items if 'seq' in auth_item]
                auth_comp_id_names = [auth_item for auth_item in auth_items if 'comp' in auth_item]
                auth_atom_id_names = [auth_item for auth_item in auth_items if 'atom' in auth_item and 'atom_name' not in auth_item]

                has_auth_chain_tags = set(auth_chain_id_names) & set(loop.tags) == set(auth_chain_id_names)
                has_auth_seq_tags = set(auth_seq_id_names) & set(loop.tags) == set(auth_seq_id_names)
                has_auth_comp_tags = set(auth_comp_id_names) & set(loop.tags) == set(auth_comp_id_names)
                has_auth_atom_tags = set(auth_atom_id_names) & set(loop.tags) == set(auth_atom_id_names)

                if not has_auth_chain_tags and self._reg.caC['polymer_sequence'] is not None\
                   and len(self._reg.caC['polymer_sequence']) == 1:
                    auth_chain_id = self._reg.caC['polymer_sequence'][0]['auth_chain_id']
                    for auth_chain_id_name in auth_chain_id_names:
                        if auth_chain_id_name in loop.tags:
                            continue
                        loop.add_tag(auth_chain_id_name)
                        for row in loop:
                            row.append(auth_chain_id)
                    has_auth_chain_tags = True

                has_valid_comp_id = True
                if has_auth_chain_tags and has_auth_seq_tags and has_auth_atom_tags and not has_auth_comp_tags:
                    for d, auth_comp_id_name in enumerate(auth_comp_id_names):
                        if auth_comp_id_name in loop.tags:
                            tags = [auth_chain_id_names[d], auth_seq_id_names[d], auth_comp_id_names[d]]
                            for idx, row in enumerate(loop.get_tag(tags)):
                                if row[2] not in EMPTY_VALUE:
                                    continue
                                try:
                                    chain_id, seq_id = row[0], int(row[1])
                                    comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                    if _auth_asym_id == chain_id and _auth_seq_id == seq_id), None)
                                except (TypeError, ValueError):
                                    comp_id = None
                                    has_valid_comp_id = False
                                loop.data[idx][loop.tags.index(auth_comp_id_names[d])] = comp_id
                            continue
                        loop.add_tag(auth_comp_id_name)
                        tags = [auth_chain_id_names[d], auth_seq_id_names[d]]
                        for idx, row in enumerate(loop.get_tag(tags)):
                            try:
                                chain_id, seq_id = row[0], int(row[1])
                                comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                if _auth_asym_id == chain_id and _auth_seq_id == seq_id), None)
                            except (TypeError, ValueError):
                                comp_id = None
                            loop.data[idx].append(comp_id)
                            if comp_id is None:
                                has_valid_comp_id = False
                        has_auth_comp_tags = True

                if has_auth_chain_tags and has_auth_seq_tags and has_auth_atom_tags and has_auth_comp_tags and has_valid_comp_id:
                    is_valid = True

                    lp = getLoop(content_subtype, reduced=False)

                    sf.add_loop(lp)
                    sf_item['loop'] = lp

                    auth_items = []
                    for d in range(atom_dim_num):
                        auth_items.extend([auth_chain_id_names[d], auth_seq_id_names[d],
                                           auth_comp_id_names[d], auth_atom_id_names[d]])
                    for idx, row in enumerate(loop.get_tag(auth_items)):
                        atom_sels = [None] * atom_dim_num

                        for d in range(atom_dim_num):

                            try:

                                chain_id = auth_chain_id = row[d * 4]
                                seq_id = int(row[d * 4 + 1])
                                comp_id = row[d * 4 + 2]
                                atom_id = row[d * 4 + 3]

                                seq_key = (chain_id, seq_id, comp_id)

                                entity_assembly_id, comp_index_id, _, _ =\
                                    auth_to_star_seq[seq_key]

                                if self._reg.annotation_mode or self._reg.native_combined:
                                    _auth_asym_id, _auth_seq_id =\
                                        next(((k[0], k[1]) for k, v in auth_to_star_seq.items()
                                              if v[0] == entity_assembly_id and v[1] == comp_index_id
                                              and k[2] == comp_id), (None, None))
                                    if _auth_asym_id is not None:
                                        seq_key = (_auth_asym_id, _auth_seq_id, comp_id)
                                        if seq_key in auth_to_star_seq:
                                            chain_id, seq_id = _auth_asym_id, _auth_seq_id

                            except KeyError:
                                continue
                            except ValueError:
                                is_valid = False
                                continue

                            auth_atom_id = atom_id

                            auth_asym_id = auth_seq_id = None

                            if seq_key in auth_to_star_seq:
                                auth_asym_id, auth_seq_id, _ = seq_key
                            else:
                                k = next((k for k, v in auth_to_star_seq.items()
                                          if v[0] == entity_assembly_id and v[1] == seq_id and v[2] == entity_id), None)
                                if k is None:
                                    continue
                                auth_asym_id, auth_seq_id, _ = k

                            chain_id, seq_id = auth_asym_id, auth_seq_id

                            _assign, warn = assignCoordPolymerSequenceWithChainId(self._reg.caC, self._reg.nefT,
                                                                                  chain_id, seq_id, comp_id, atom_id)

                            if warn is not None:

                                idx_msg = get_idx_msg(idx)

                                if warn.startswith('[Atom not found]'):
                                    if not self._reg.remediation_mode or 'Macromolecules page' not in warn:
                                        self._reg.report.error.appendDescription('atom_not_found',
                                                                                 {'file_name': original_file_name,
                                                                                  'sf_framecode': sf_framecode,
                                                                                  'category': lp_category,
                                                                                  'description': idx_msg + warn})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.validateStrMr() "
                                                                f"++ Error  - {idx_msg + warn}\n")

                                continue

                            enableWarning = True
                            if content_subtype == 'dist_restraint':
                                if (auth_comp_id_1_col != -1 and loop.data[idx][auth_comp_id_1_col] == 'HOH')\
                                   or (auth_comp_id_2_col != -1 and loop.data[idx][auth_comp_id_2_col] == 'HOH'):
                                    enableWarning = False
                            elif content_subtype == 'dihed_restraint':
                                if torsion_angle_name_col != -1 and loop.data[idx][torsion_angle_name_col] == 'PPA':
                                    enableWarning = False

                            atom_sels[d], warn = selectCoordAtoms(self._reg.cR, self._reg.caC, self._reg.nefT,
                                                                  _assign, auth_chain_id, seq_id, comp_id, atom_id, auth_atom_id,
                                                                  allowAmbig=content_subtype in ('dist_restraint',
                                                                                                 'noepk_restraint'),
                                                                  enableWarning=enableWarning,
                                                                  preferAuthAtomName=prefer_auth_atom_name,
                                                                  representativeModelId=self._reg.representative_model_id,
                                                                  representativeAltId=self._reg.representative_alt_id,
                                                                  modelNumName=model_num_name)

                            if warn is not None:

                                report_atom_sel_warn(idx, warn)

                                continue

                        emit_str_mr_rows(idx, atom_sels)

                    if not is_valid:

                        lp = loop

                        sf_item['loop'] = lp

                else:  # nothing to do because of missing polymer sequence for this loop

                    lp = loop

                    sf_item['loop'] = lp

            if content_subtype == 'dist_restraint':

                sf_item['loop'] = lp

                use_member_logic_code = sf_item['file_type'] in ('nm-res-xpl', 'nm-res-cns', 'nm-res-cha')
                if use_member_logic_code:
                    lp = sf_item['loop']
                    if 'Member_logic_code' not in lp.tags:
                        use_member_logic_code = False
                    else:
                        dat = lp.get_tag(['Member_logic_code'])
                        use_member_logic_code = any(True for row in dat if row not in EMPTY_VALUE)

                if not use_member_logic_code:
                    if not self.updateGenDistConstIdInMrStr(sf_item):
                        err = "Atoms in distance restraints can not be properly identified. Please re-upload the NMR-STAR file."
                        self._reg.report.error.appendDescription('missing_mandatory_content',
                                                                 {'file_name': original_file_name,
                                                                  'sf_framecode': sf_framecode,
                                                                  'category': lp_category,
                                                                  'description': err})

                sf_item['constraint_type'] = 'distance'
                sf_item['constraint_subsubtype'] = 'simple'
                constraint_type = get_first_sf_tag(sf, 'Constraint_type')
                if len(constraint_type) > 0 and constraint_type not in EMPTY_VALUE:
                    sf_item['constraint_subtype'] = constraint_type

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
                has_potential_type = len(potential_type) > 0 and potential_type not in EMPTY_VALUE and potential_type != 'unknown'

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

                sf_item['id'] = count

                if has_or_code:

                    prev_id = -1
                    for row in lp:
                        if member_logic_code_col != -1 and row[member_logic_code_col] == 'OR':
                            _id = int(row[id_col])
                            if _id != prev_id:
                                _atom1 = {'chain_id': row[auth_asym_id_1_col],
                                          'seq_id':
                                          int(row[auth_seq_id_1_col]) if row[auth_seq_id_1_col] not in EMPTY_VALUE else None,
                                          'comp_id': row[comp_id_1_col],
                                          'atom_id': row[atom_id_1_col]}
                                _atom2 = {'chain_id': row[auth_asym_id_2_col],
                                          'seq_id':
                                          int(row[auth_seq_id_2_col]) if row[auth_seq_id_2_col] not in EMPTY_VALUE else None,
                                          'comp_id': row[comp_id_2_col],
                                          'atom_id': row[atom_id_2_col]}
                                prev_id = _id
                                continue
                            atom1 = {'chain_id': row[auth_asym_id_1_col],
                                     'seq_id': int(row[auth_seq_id_1_col]) if row[auth_seq_id_1_col] not in EMPTY_VALUE else None,
                                     'comp_id': row[comp_id_1_col],
                                     'atom_id': row[atom_id_1_col]}
                            atom2 = {'chain_id': row[auth_asym_id_2_col],
                                     'seq_id': int(row[auth_seq_id_2_col]) if row[auth_seq_id_2_col] not in EMPTY_VALUE else None,
                                     'comp_id': row[comp_id_2_col],
                                     'atom_id': row[atom_id_2_col]}
                            if isAmbigAtomSelection([_atom1, atom1], self._reg.csStat)\
                               or isAmbigAtomSelection([_atom2, atom2], self._reg.csStat):
                                sf_item['constraint_subsubtype'] = 'ambi'
                                break
                            _atom1, _atom2 = atom1, atom2

                    if sf_item['constraint_subsubtype'] == 'ambi':

                        if 'pre' in sf_framecode or 'paramag' in sf_framecode:
                            sf_item['constraint_subtype'] = 'paramagnetic relaxation'
                        if 'cidnp' in sf_framecode:
                            sf_item['constraint_subtype'] = 'photo cidnp'
                        if 'csp' in sf_framecode or 'perturb' in sf_framecode:
                            sf_item['constraint_subtype'] = 'chemical shift perturbation'
                        if 'mutat' in sf_framecode:
                            sf_item['constraint_subtype'] = 'mutation'
                        if 'protect' in sf_framecode:
                            sf_item['constraint_subtype'] = 'hydrogen exchange protection'
                        if 'symm' in sf_framecode:
                            sf_item['constraint_subtype'] = 'symmetry'

                        if 'pre' in original_file_name or 'paramag' in original_file_name:
                            sf_item['constraint_subtype'] = 'paramagnetic relaxation'
                        if 'cidnp' in original_file_name:
                            sf_item['constraint_subtype'] = 'photo cidnp'
                        if 'csp' in original_file_name or 'perturb' in original_file_name:
                            sf_item['constraint_subtype'] = 'chemical shift perturbation'
                        if 'mutat' in original_file_name:
                            sf_item['constraint_subtype'] = 'mutation'
                        if 'protect' in original_file_name:
                            sf_item['constraint_subtype'] = 'hydrogen exchange protection'
                        if 'symm' in original_file_name:
                            sf_item['constraint_subtype'] = 'symmetry'

                if sf_item['constraint_subsubtype'] == 'simple':

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
                                sf_item['constraint_subtype'] = 'ROE build-up'
                            else:
                                sf_item['constraint_subtype'] = 'NOE build-up'

                        elif 'not' in sf_framecode and 'seen' in sf_framecode:
                            sf_item['constraint_subtype'] = 'NOE not seen'

                        elif 'roe' in sf_framecode:
                            sf_item['constraint_subtype'] = 'ROE'

                        elif 'build' in original_file_name and 'up' in original_file_name:
                            if 'roe' in original_file_name:
                                sf_item['constraint_subtype'] = 'ROE build-up'
                            else:
                                sf_item['constraint_subtype'] = 'NOE build-up'

                        elif 'not' in original_file_name and 'seen' in original_file_name:
                            sf_item['constraint_subtype'] = 'NOE not seen'

                        elif 'roe' in original_file_name:
                            sf_item['constraint_subtype'] = 'ROE'

                        sf_item['constraint_subtype'] = 'NOE'

                    elif metal_coord and not disele_bond and not disulf_bond and not hydrog_bond:
                        sf_item['constraint_subtype'] = 'metal coordination'

                    elif not metal_coord and disele_bond and not disulf_bond and not hydrog_bond:
                        sf_item['constraint_subtype'] = 'diselenide bond'

                    elif not metal_coord and not disele_bond and disulf_bond and not hydrog_bond:
                        sf_item['constraint_subtype'] = 'disulfide bond'

                    elif not metal_coord and not disele_bond and not disulf_bond and hydrog_bond:
                        sf_item['constraint_subtype'] = 'hydrogen bond'

            elif content_subtype == 'dihed_restraint':
                self.updateTorsionAngleConstIdInMrStr(sf_item)

                auth_to_entity_type = self._reg.caC['auth_to_entity_type']

                sf_item['constraint_type'] = 'dihedral angle'

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
                try:
                    torsion_angle_name_col = lp.tags.index('Torsion_angle_name')
                except ValueError:
                    torsion_angle_name_col = -1

                potential_type = get_first_sf_tag(sf, 'Potential_type')
                has_potential_type = len(potential_type) > 0 and potential_type not in EMPTY_VALUE and potential_type != 'unknown'

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

                sf_item['id'] = count

                auth_asym_id_col = lp.tags.index('Auth_asym_ID_2')
                auth_seq_id_col = lp.tags.index('Auth_seq_ID_2')
                auth_comp_id_col = lp.tags.index('Auth_comp_ID_2')

                _protein_angles = _other_angles = 0

                prev_id = -1
                for row in lp:
                    _id = int(row[id_col])
                    if _id == prev_id:
                        continue
                    prev_id = _id
                    auth_asym_id = row[auth_asym_id_col]
                    auth_seq_id = int(row[auth_seq_id_col]) if row[auth_seq_id_col] not in EMPTY_VALUE else None
                    auth_comp_id = row[auth_comp_id_col]

                    seq_key = (auth_asym_id, auth_seq_id, auth_comp_id)

                    if seq_key in auth_to_entity_type:
                        entity_type = auth_to_entity_type[seq_key]

                        if 'peptide' in entity_type:
                            _protein_angles += 1
                        else:
                            _other_angles += 1

                if _protein_angles > _other_angles:
                    sf_item['constraint_type'] = 'protein dihedral angle'

                    tagNames = [t[0] for t in sf.tags]

                    if 'Constraint_type' not in tagNames:
                        sf_item['constraint_subtype'] = 'backbone chemical shifts'
                        sf.add_tag('Constraint_subtype', 'backbone chemical shifts')

                _na_angles = _other_angles = 0

                prev_id = -1
                for row in lp:
                    _id = int(row[id_col])
                    if _id == prev_id:
                        continue
                    prev_id = _id
                    auth_asym_id = row[auth_asym_id_col]
                    auth_seq_id = int(row[auth_seq_id_col]) if row[auth_seq_id_col] not in EMPTY_VALUE else None
                    auth_comp_id = row[auth_comp_id_col]

                    seq_key = (auth_asym_id, auth_seq_id, auth_comp_id)

                    if seq_key in auth_to_entity_type:
                        entity_type = auth_to_entity_type[seq_key]

                        if 'nucleotide' in entity_type:
                            _na_angles += 1
                        else:
                            _other_angles += 1

                if _na_angles > _other_angles:
                    sf_item['constraint_type'] = 'nucleic acid dihedral angle'

                    tagNames = [t[0] for t in sf.tags]

                    if 'Constraint_type' not in tagNames:
                        sf_item['constraint_subtype'] = 'unknown'
                        sf.add_tag('Constraint_type', 'unknown')

                _br_angles = _other_angles = 0

                prev_id = -1
                for row in lp:
                    _id = int(row[id_col])
                    if _id == prev_id:
                        continue
                    prev_id = _id
                    auth_asym_id = row[auth_asym_id_col]
                    auth_seq_id = int(row[auth_seq_id_col]) if row[auth_seq_id_col] not in EMPTY_VALUE else None
                    auth_comp_id = row[auth_comp_id_col]

                    seq_key = (auth_asym_id, auth_seq_id, auth_comp_id)

                    if seq_key in auth_to_entity_type:
                        entity_type = auth_to_entity_type[seq_key]

                        if 'saccharide' in entity_type:
                            _br_angles += 1
                        else:
                            _other_angles += 1

                if _br_angles > _other_angles:
                    sf_item['constraint_type'] = 'carbohydrate dihedral angle'  # DAOTHER-9471

                    tagNames = [t[0] for t in sf.tags]

                    if 'Constraint_type' not in tagNames:
                        sf_item['constraint_subtype'] = 'unknown'
                        sf.add_tag('Constraint_type', 'unknown')

            elif content_subtype == 'rdc_restraint':

                sf_item['constraint_type'] = 'dipolar coupling'  # DAOTHER-9471
                sf_item['constraint_subtype'] = 'RDC'

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

                chain_id_1_col = lp.tags.index(item_names['chain_id_1'])
                chain_id_2_col = lp.tags.index(item_names['chain_id_2'])
                seq_id_1_col = lp.tags.index(item_names['seq_id_1'])
                seq_id_2_col = lp.tags.index(item_names['seq_id_2'])
                comp_id_1_col = lp.tags.index(item_names['comp_id_1'])
                comp_id_2_col = lp.tags.index(item_names['comp_id_2'])
                atom_id_1_col = lp.tags.index(item_names['atom_id_1'])
                atom_id_2_col = lp.tags.index(item_names['atom_id_2'])

                potential_type = get_first_sf_tag(sf, 'Potential_type')
                has_potential_type = len(potential_type) > 0 and potential_type not in EMPTY_VALUE and potential_type != 'unknown'

                details = get_first_sf_tag(sf, 'Details')
                has_rdc_type = len(details) > 0 and details not in EMPTY_VALUE

                _potential_type = _rdc_type = None
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

                    if not has_rdc_type:
                        try:
                            atom1 = {'chain_id': row[chain_id_1_col],
                                     'seq_id': int(row[seq_id_1_col]),
                                     'comp_id': row[comp_id_1_col],
                                     'atom_id': row[atom_id_1_col]}
                            atom2 = {'chain_id': row[chain_id_2_col],
                                     'seq_id': int(row[seq_id_2_col]),
                                     'comp_id': row[comp_id_2_col],
                                     'atom_id': row[atom_id_2_col]}
                            if _rdc_type is None:
                                _rdc_type = getRdcCode([atom1, atom2])
                            else:
                                if getRdcCode([atom1, atom2]) != _rdc_type:
                                    has_rdc_type = True
                        except (ValueError, TypeError):
                            pass

                if not has_potential_type and _potential_type is not None:
                    set_sf_tag(sf, 'Potential_type', _potential_type)

                if not has_rdc_type and _rdc_type is not None:
                    set_sf_tag(sf, 'Details', _rdc_type)

                sf_item['id'] = count

            else:

                sf_item['id'] = len(lp)

            # merge other loops of the source saveframe
            if is_sf:

                for loop in _sf.loops:

                    if loop.category == lp_category:
                        continue

                    if loop.category in LINKED_LP_CATEGORIES[file_type][content_subtype]:
                        sf.add_loop(loop)

        self._reg.mr_sf_dict_holder[content_subtype].append(sf_item)

        return True

    def updateGenDistConstIdInMrStr(self, sf_item: dict) -> bool:
        """ Update _Gen_dist_constraint.ID in NMR-STAR restraint file.
        """

        loop = sf_item['loop']

        lp = pynmrstar.Loop.from_scratch(loop.category)

        lp.add_tag(loop.tags)

        id_col = loop.tags.index('ID')
        if 'Index_ID' not in loop.tags:
            tag = f'{loop.category}.Index_ID'
            for idx in range(len(loop)):
                loop.data[idx].append(idx + 1)
            loop.add_tag(tag)
            lp.add_tag(tag)
        if 'Member_ID' not in loop.tags:
            tag = f'{loop.category}.Member_ID'
            loop.add_tag(tag, update_data=True)
            lp.add_tag(tag)
        if 'Member_logic_code' not in loop.tags:
            tag = f'{loop.category}.Member_logic_code'
            loop.add_tag(tag, update_data=True)
            lp.add_tag(tag)

        index_id_col = loop.tags.index('Index_ID')
        member_id_col = loop.tags.index('Member_ID')
        member_logic_code_col = loop.tags.index('Member_logic_code')

        combination_id_col = loop.tags.index('Combination_ID') if 'Combination_ID' in loop.tags else -1

        chain_id_1_col = loop.tags.index('Auth_asym_ID_1')
        seq_id_1_col = loop.tags.index('Auth_seq_ID_1')
        comp_id_1_col = loop.tags.index('Auth_comp_ID_1')
        atom_id_1_col = loop.tags.index('Auth_atom_ID_1')

        ref_chain_id_1_col = loop.tags.index('Entity_assembly_ID_1')
        ref_seq_id_1_col = loop.tags.index('Comp_index_ID_1')
        ref_comp_id_1_col = loop.tags.index('Comp_ID_1')
        ref_atom_id_1_col = loop.tags.index('Atom_ID_1')

        chain_id_2_col = loop.tags.index('Auth_asym_ID_2')
        seq_id_2_col = loop.tags.index('Auth_seq_ID_2')
        comp_id_2_col = loop.tags.index('Auth_comp_ID_2')
        atom_id_2_col = loop.tags.index('Auth_atom_ID_2')

        ref_chain_id_2_col = loop.tags.index('Entity_assembly_ID_2')
        ref_seq_id_2_col = loop.tags.index('Comp_index_ID_2')
        ref_comp_id_2_col = loop.tags.index('Comp_ID_2')
        ref_atom_id_2_col = loop.tags.index('Atom_ID_2')

        target_val_col = loop.tags.index('Target_val') if 'Target_val' in loop.tags else -1
        target_val_err_col = loop.tags.index('Target_val_uncertainty') if 'Target_val_uncertainty' in loop.tags else -1
        lower_linear_limit_col = loop.tags.index('Lower_linear_limit') if 'Lower_linear_limit' in loop.tags else -1
        upper_linear_limit_col = loop.tags.index('Upper_linear_limit') if 'Upper_linear_limit' in loop.tags else -1
        lower_limit_col = loop.tags.index('Distance_lower_bound_val') if 'Distance_lower_bound_val' in loop.tags else -1
        upper_limit_col = loop.tags.index('Distance_upper_bound_val') if 'Distance_upper_bound_val' in loop.tags else -1
        weight_col = loop.tags.index('Weight') if 'Weight' in loop.tags else -1

        cs_loops = self._reg.lp_data['chem_shift']

        @functools.lru_cache()
        def get_cs_value(chain_id, seq_id, comp_id, atom_id):
            if cs_loops is None or len(cs_loops) == 0:
                return None

            if isinstance(chain_id, int):
                chain_id = str(chain_id)

            _atom_ids = self._reg.nefT.get_valid_star_atom(comp_id, atom_id, leave_unmatched=False)[0]

            for lp in cs_loops:
                row = next((row for row in lp['data']
                            if row['Entity_assembly_ID'] == chain_id and row['Comp_index_ID'] == seq_id
                            and row['Comp_ID'] == comp_id and row['Atom_ID'] in _atom_ids), None)

                if row is not None:
                    val = row['Val']
                    return val if val not in EMPTY_VALUE else None

            return None

        def concat_target_val(row):
            return (str(row[target_val_col]) if target_val_col != -1 else '')\
                + (str(row[target_val_err_col]) if target_val_err_col != -1 else '')\
                + (str(row[lower_linear_limit_col]) if lower_linear_limit_col != -1 else '')\
                + (str(row[upper_linear_limit_col]) if upper_linear_limit_col != -1 else '')\
                + (str(row[lower_limit_col]) if lower_limit_col != -1 else '')\
                + (str(row[upper_limit_col]) if upper_limit_col != -1 else '')\
                + (str(row[weight_col]) if weight_col != -1 else '')

        _rest_id = _member_logic_code = _cs_val1 = _cs_val2 = None
        _atom1, _atom2 = {}, {}
        _values = ''

        modified = has_member_id = False

        sf_item['id'] = 0

        for row in loop:
            _row = row

            sf_item['id'] += 1
            duplicated = False

            try:

                rest_id = row[id_col]
                try:
                    member_id = row[member_id_col]
                except IndexError:
                    member_id = None
                try:
                    member_logic_code = row[member_logic_code_col]
                except IndexError:
                    member_logic_code = None
                values = concat_target_val(row)

                try:
                    atom1 = {'chain_id': row[chain_id_1_col],
                             'seq_id': int(row[seq_id_1_col]),
                             'comp_id': row[comp_id_1_col],
                             'atom_id': row[atom_id_1_col],
                             'ref_chain_id': row[ref_chain_id_1_col],
                             'ref_seq_id': int(row[ref_seq_id_1_col]),
                             'ref_comp_id': row[ref_comp_id_1_col],
                             'ref_atom_id': row[ref_atom_id_1_col]}
                    cs_val1 = get_cs_value(atom1['ref_chain_id'], atom1['ref_seq_id'], atom1['ref_comp_id'], atom1['ref_atom_id'])
                except (ValueError, TypeError):
                    atom1 = {}
                    cs_val1 = None

                try:
                    atom2 = {'chain_id': row[chain_id_2_col],
                             'seq_id': int(row[seq_id_2_col]),
                             'comp_id': row[comp_id_2_col],
                             'atom_id': row[atom_id_2_col],
                             'ref_chain_id': row[ref_chain_id_2_col],
                             'ref_seq_id': int(row[ref_seq_id_2_col]),
                             'ref_comp_id': row[ref_comp_id_2_col],
                             'ref_atom_id': row[ref_atom_id_2_col]}
                    cs_val2 = get_cs_value(atom2['ref_chain_id'], atom2['ref_seq_id'], atom2['ref_comp_id'], atom2['ref_atom_id'])
                except (ValueError, TypeError):
                    atom2 = {}
                    cs_val2 = None

                if member_id not in EMPTY_VALUE:
                    has_member_id = True

                _atoms1 = [atom1, _atom1]
                _atoms2 = [atom2, _atom2]

                if _rest_id is None:
                    pass

                elif rest_id != _rest_id and len(atom1) > 0 and len(atom2) > 0:

                    if (member_id in EMPTY_VALUE or member_logic_code == 'OR'):

                        if atom1['atom_id'][0] in PROTON_BEGIN_CODE and atom2['atom_id'][0] in PROTON_BEGIN_CODE:

                            if values == _values:
                                ambig1 = isAmbigAtomSelection(_atoms1, self._reg.csStat)
                                ambig2 = isAmbigAtomSelection(_atoms2, self._reg.csStat)

                                if (not ambig1 and not ambig2)\
                                   or (atom1['ref_chain_id'] != atom2['ref_chain_id']
                                       and ((not ambig1 and len(_atom2) > 0
                                             and atom1['ref_chain_id'] != _atom2['ref_chain_id']
                                             and atom2['comp_id'] == _atom2['comp_id'])
                                            or (not ambig2 and len(_atom1) > 0
                                                and atom2['ref_chain_id'] != _atom1['ref_chain_id']
                                                and atom1['comp_id'] == _atom1['comp_id']))):

                                    diff_cs_val1 = cs_val1 is not None and _cs_val1 is not None and cs_val1 != _cs_val1
                                    diff_cs_val2 = cs_val2 is not None and _cs_val2 is not None and cs_val2 != _cs_val2

                                    if (not ambig1 and diff_cs_val1) or (not ambig2 and diff_cs_val2):
                                        pass

                                    else:

                                        try:

                                            _row[member_logic_code_col] = 'OR'

                                            if _member_logic_code in EMPTY_VALUE:
                                                lp.data[-1][member_logic_code_col] = 'OR'

                                        except IndexError:
                                            pass

                                        sf_item['id'] -= 1

                                        modified = True

                        elif values == _values and isIdenticalRestraint(_atoms1, self._reg.nefT)\
                                and isIdenticalRestraint(_atoms2, self._reg.nefT):
                            sf_item['id'] -= 1
                            duplicated = True

                elif member_logic_code != 'AND':

                    if not isAmbigAtomSelection(_atoms1, self._reg.csStat)\
                       and not isAmbigAtomSelection(_atoms2, self._reg.csStat):

                        if member_logic_code in EMPTY_VALUE:
                            modified = True

                        try:

                            _row[member_logic_code_col] = 'OR'

                            if _member_logic_code in EMPTY_VALUE:
                                lp.data[-1][member_logic_code_col] = 'OR'

                                modified = True

                        except IndexError:
                            pass

                    sf_item['id'] -= 1

                _rest_id, _member_logic_code, _atom1, _atom2, _values, _cs_val1, _cs_val2 =\
                    rest_id, member_logic_code, atom1, atom2, values, cs_val1, cs_val2

            except ValueError:
                _atom1, _atom2 = {}, {}

            if not self._reg.native_combined:  # DAOTHER-8855
                _row[id_col] = sf_item['id']
            if combination_id_col == -1 or (combination_id_col != -1 and _row[combination_id_col] in EMPTY_VALUE):
                try:
                    _row[member_id_col] = None
                except IndexError:
                    pass

            if duplicated:
                continue

            lp.add_data(_row)

        get_cs_value.cache_clear()

        if not modified and not has_member_id:
            return True

        member_id_dict = {}

        def update_member_id_dict(rows):
            if len(rows) < 2:
                return

            atom_sel1, atom_sel2 = [], []

            for row in rows:

                try:
                    atom1 = {'chain_id': row[chain_id_1_col],
                             'seq_id': int(row[seq_id_1_col]),
                             'comp_id': row[comp_id_1_col],
                             'atom_id': row[atom_id_1_col]}
                except (ValueError, TypeError):
                    atom1 = {}

                try:
                    atom2 = {'chain_id': row[chain_id_2_col],
                             'seq_id': int(row[seq_id_2_col]),
                             'comp_id': row[comp_id_2_col],
                             'atom_id': row[atom_id_2_col]}
                except (ValueError, TypeError):
                    atom2 = {}

                atom_sel1.append(atom1)
                atom_sel2.append(atom2)

            if isAmbigAtomSelection(atom_sel1, self._reg.csStat)\
               or isAmbigAtomSelection(atom_sel2, self._reg.csStat):
                for member_id, row in enumerate(rows, start=1):
                    try:
                        index_id = row[index_id_col]
                        member_id_dict[index_id] = member_id
                    except IndexError:
                        pass

        _row = _rest_id = None
        _union_rows = []

        for row in lp:
            rest_id = row[id_col]

            if _rest_id is not None and rest_id == _rest_id:
                if len(_union_rows) == 0:
                    _union_rows.append(_row)

                _union_rows.append(row)

            else:

                if len(_union_rows) > 0:
                    update_member_id_dict(_union_rows)

                _union_rows = []

            _row = row
            _rest_id = rest_id

        if len(_union_rows) > 0:
            update_member_id_dict(_union_rows)

        if len(member_id_dict) > 0:
            for row in lp:
                try:

                    index_id = row[index_id_col]
                    member_logic_code = row[member_logic_code_col]
                    if member_logic_code == 'AND':
                        continue

                    if index_id in member_id_dict:
                        row[member_id_col] = member_id_dict[index_id]

                except IndexError:
                    pass

        def concat_all_val(row):
            return str(row[chain_id_1_col]) + str(row[seq_id_1_col]) + str(row[comp_id_1_col]) + str(row[atom_id_1_col])\
                + str(row[chain_id_2_col]) + str(row[seq_id_2_col]) + str(row[comp_id_2_col]) + str(row[atom_id_2_col])\
                + concat_target_val(row)

        len_data = len(lp)

        try:

            for idx, row in enumerate(lp, start=1):
                if row[member_logic_code_col] != 'OR':
                    continue
                if idx - 2 > 0:
                    _row = lp.data[idx - 2]
                    if concat_all_val(row) == concat_all_val(_row):
                        row[member_logic_code_col] = '.'
                if idx < len_data:
                    _row = lp.data[idx]
                    if concat_all_val(row) == concat_all_val(_row):
                        row[member_logic_code_col] = '.'

        except IndexError:
            pass

        try:

            del sf_item['saveframe'][loop]

            sf_item['saveframe'].add_loop(lp)
            sf_item['loop'] = lp

            return True

        except ValueError:
            return False

    def updateTorsionAngleConstIdInMrStr(self, sf_item: dict) -> bool:  # pylint: disable=no-self-use
        """ Update _Torsion_angle_constraint.ID in NMR-STAR restraint file.
        """

        loop = sf_item['loop']

        lp = pynmrstar.Loop.from_scratch(loop.category)

        lp.add_tag(loop.tags)

        id_col = loop.tags.index('ID')
        if 'Index_ID' not in loop.tags:
            tag = f'{loop.category}.Index_ID'
            for idx in range(len(loop)):
                loop.data[idx].append(idx + 1)
            loop.add_tag(tag)
            lp.add_tag(tag)
        if 'Combination_ID' not in loop.tags:
            tag = f'{loop.category}.Combination_ID'
            loop.add_tag(tag, update_data=True)
            lp.add_tag(tag)

        index_id_col = loop.tags.index('Index_ID')
        combination_id_col = loop.tags.index('Combination_ID')

        chain_id_1_col = loop.tags.index('Auth_asym_ID_1')
        seq_id_1_col = loop.tags.index('Auth_seq_ID_1')
        atom_id_1_col = loop.tags.index('Auth_atom_ID_1')

        chain_id_2_col = loop.tags.index('Auth_asym_ID_2')
        seq_id_2_col = loop.tags.index('Auth_seq_ID_2')
        atom_id_2_col = loop.tags.index('Auth_atom_ID_2')

        chain_id_3_col = loop.tags.index('Auth_asym_ID_3')
        seq_id_3_col = loop.tags.index('Auth_seq_ID_3')
        atom_id_3_col = loop.tags.index('Auth_atom_ID_3')

        chain_id_4_col = loop.tags.index('Auth_asym_ID_4')
        seq_id_4_col = loop.tags.index('Auth_seq_ID_4')
        atom_id_4_col = loop.tags.index('Auth_atom_ID_4')

        target_val_col = loop.tags.index('Angle_target_val') if 'Angle_target_val' in loop.tags else -1
        target_val_err_col = loop.tags.index('Angle_target_val_err') if 'Angle_target_val_err' in loop.tags else -1
        lower_linear_limit_col = loop.tags.index('Angle_lower_linear_limit') if 'Angle_lower_linear_limit' in loop.tags else -1
        upper_linear_limit_col = loop.tags.index('Angle_upper_linear_limit') if 'Angle_upper_linear_limit' in loop.tags else -1
        lower_limit_col = loop.tags.index('Angle_lower_bound_val') if 'Angle_lower_bound_val' in loop.tags else -1
        upper_limit_col = loop.tags.index('Angle_upper_bound_val') if 'Angle_upper_bound_val' in loop.tags else -1
        weight_col = loop.tags.index('Weight') if 'Weight' in loop.tags else -1

        modified = False

        sf_item['id'] = 0
        sf_item['index_id'] = 0

        len_loop = len(loop)

        proc_row = [False] * len_loop

        for idx, row in enumerate(loop):

            if proc_row[idx]:
                continue

            _row = row

            sf_item['id'] += 1
            sf_item['index_id'] += 1

            try:
                combination_id = row[combination_id_col]
            except IndexError:
                combination_id = None

            if combination_id not in EMPTY_VALUE and str(combination_id) != '1':
                sf_item['id'] -= 1

            _row[id_col] = sf_item['id']
            try:
                _row[index_id_col] = sf_item['index_id']
            except IndexError:
                while index_id_col >= len(_row):
                    _row.append(None)
                _row[index_id_col] = sf_item['index_id']

            try:
                key = _row[chain_id_1_col] + str(_row[seq_id_1_col]) + _row[atom_id_1_col]\
                    + _row[chain_id_2_col] + str(_row[seq_id_2_col]) + _row[atom_id_2_col]\
                    + _row[chain_id_3_col] + str(_row[seq_id_3_col]) + _row[atom_id_3_col]\
                    + _row[chain_id_4_col] + str(_row[seq_id_4_col]) + _row[atom_id_4_col]
                values = (str(_row[target_val_col]) if target_val_col != -1 else '')\
                    + (str(_row[target_val_err_col]) if target_val_err_col != -1 else '')\
                    + (str(_row[lower_linear_limit_col]) if lower_linear_limit_col != -1 else '')\
                    + (str(_row[upper_linear_limit_col]) if upper_linear_limit_col != -1 else '')\
                    + (str(_row[lower_limit_col]) if lower_limit_col != -1 else '')\
                    + (str(_row[upper_limit_col]) if upper_limit_col != -1 else '')\
                    + (str(_row[weight_col]) if weight_col != -1 else '')
            except TypeError:
                return False

            if combination_id in EMPTY_VALUE and idx + 1 < len_loop:
                combination_id = 1

                for idx2 in range(idx + 1, len_loop):

                    if proc_row[idx2]:
                        continue

                    _row_ = loop.data[idx2]

                    try:
                        _key = _row_[chain_id_1_col] + str(_row_[seq_id_1_col]) + _row_[atom_id_1_col]\
                            + _row_[chain_id_2_col] + str(_row_[seq_id_2_col]) + _row_[atom_id_2_col]\
                            + _row_[chain_id_3_col] + str(_row_[seq_id_3_col]) + _row_[atom_id_3_col]\
                            + _row_[chain_id_4_col] + str(_row_[seq_id_4_col]) + _row_[atom_id_4_col]
                        _values = (str(_row_[target_val_col]) if target_val_col != -1 else '')\
                            + (str(_row_[target_val_err_col]) if target_val_err_col != -1 else '')\
                            + (str(_row_[lower_linear_limit_col]) if lower_linear_limit_col != -1 else '')\
                            + (str(_row_[upper_linear_limit_col]) if upper_linear_limit_col != -1 else '')\
                            + (str(_row_[lower_limit_col]) if lower_limit_col != -1 else '')\
                            + (str(_row_[upper_limit_col]) if upper_limit_col != -1 else '')\
                            + (str(_row_[weight_col]) if weight_col != -1 else '')
                    except TypeError:
                        return False

                    if key == _key:
                        modified = True

                        if values == _values:
                            proc_row[idx2] = True
                            continue

                        if combination_id == 1:
                            try:
                                _row[combination_id_col] = combination_id
                            except IndexError:
                                while combination_id_col >= len(_row):
                                    _row.append(None)
                                _row[combination_id_col] = combination_id
                            lp.add_data(_row)

                        sf_item['index_id'] += 1
                        combination_id += 1

                        _row_[id_col] = sf_item['id']
                        try:
                            _row_[index_id_col] = sf_item['index_id']
                        except IndexError:
                            while index_id_col >= len(_row_):
                                _row_.append(None)
                            _row_[index_id_col] = sf_item['index_id']
                        try:
                            _row_[combination_id_col] = combination_id
                        except IndexError:
                            while combination_id_col >= len(_row_):
                                _row_.append(None)
                            _row_[combination_id_col] = combination_id

                        lp.add_data(_row_)

                        proc_row[idx2] = True

                if combination_id == 1:
                    lp.add_data(_row)

            else:
                lp.add_data(_row)

        if not modified:
            return True

        try:

            del sf_item['saveframe'][loop]

            sf_item['saveframe'].add_loop(lp)
            sf_item['loop'] = lp

            return True

        except ValueError:
            return False

    def testRdcVector(self, file_name: str, file_type: str, content_subtype: str, sf_framecode: str, lp_category: str
                      ) -> None:
        """ Perform consistency test on RDC bond vectors.
        """

        item_names = ITEM_NAMES_IN_RDC_LOOP[file_type]
        index_tag = INDEX_TAGS[file_type][content_subtype]
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

            lp_data = next((lp['data'] for lp in self._reg.lp_data[content_subtype]
                            if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode), None)

            if lp_data is not None:

                for row in lp_data:
                    chain_id_1, chain_id_2, seq_id_1, seq_id_2, \
                        comp_id_1, comp_id_2, atom_id_1, atom_id_2 = ext_atom_names(row)

                    if atom_id_1 in EMPTY_VALUE or atom_id_2 in EMPTY_VALUE:
                        continue

                    if atom_id_1[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS\
                       or atom_id_2[0] not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS:

                        idx_msg = f"[Check row of {index_tag} {row[index_tag]}] " if index_tag in row else ''

                        err = f"{idx_msg}Non-magnetic susceptible spin appears in RDC vector; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                            f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2})."

                        self._reg.report.error.appendDescription('invalid_data',
                                                                 {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                  'category': lp_category, 'description': err})

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.testRdcVector() ++ Error  - {err}\n")

                    if chain_id_1 != chain_id_2:

                        if self._reg.exptl_method == 'SOLID-STATE NMR' and self._reg.symmetric is None:

                            src_id = self._reg.report.getInputSourceIdOfCoord()

                            if src_id >= 0:

                                cif_input_source = self._reg.report.input_sources[src_id]
                                cif_input_source_dic = cif_input_source.get()

                                has_cif_poly_seq = has_key_value(cif_input_source_dic, 'polymer_sequence')

                                if has_cif_poly_seq:

                                    cif_poly_seq = cif_input_source_dic['polymer_sequence']

                                    self._reg.symmetric = 'no'

                                    for ps in cif_poly_seq:

                                        if 'identical_auth_chain_id' in ps:

                                            if len(ps['identical_auth_chain_id']) + 1 > 2:
                                                self._reg.symmetric = 'yes'

                        idx_msg = f"[Check row of {index_tag} {row[index_tag]}] " if index_tag in row else ''

                        if self._reg.symmetric == 'no':

                            err = f"{idx_msg}Found inter-chain RDC vector; "\
                                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                                f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}) "\
                                f"in a loop {lp_category}."

                            self._reg.report.error.appendDescription('invalid_data',
                                                                     {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                      'category': lp_category, 'description': err})

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.testRdcVector() ++ Error  - {err}\n")

                        else:

                            err = f"{idx_msg}Found inter-chain RDC vector; "\
                                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                                f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}) "\
                                f"in a loop {lp_category}. "\
                                "However, it might be an artificial RDC constraint on solid-state NMR "\
                                "applied to symmetric samples such as fibrils.\n"

                            self._reg.report.warning.appendDescription('anomalous_rdc_vector',
                                                                       {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                        'category': lp_category, 'description': err})

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.testRdcVector() ++ Warning  - {err}\n")

                    elif abs(seq_id_1 - seq_id_2) > 1:

                        idx_msg = f"[Check row of {index_tag} {row[index_tag]}] " if index_tag in row else ''

                        err = f"{idx_msg}Found inter-residue RDC vector; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                            f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}) "\
                            f"in a loop {lp_category}."

                        self._reg.report.error.appendDescription('invalid_data',
                                                                 {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                  'category': lp_category, 'description': err})

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.testRdcVector() ++ Error  - {err}\n")

                    elif abs(seq_id_1 - seq_id_2) == 1:

                        if self._reg.csStat.peptideLike(comp_id_1) and self._reg.csStat.peptideLike(comp_id_2)\
                           and ((seq_id_1 < seq_id_2 and atom_id_1 == 'C' and atom_id_2 in RDC_BB_PAIR_CODE)
                                or (seq_id_1 > seq_id_2 and atom_id_1 in RDC_BB_PAIR_CODE and atom_id_2 == 'C')
                                or (seq_id_1 < seq_id_2 and atom_id_1.startswith('HA') and atom_id_2 == 'H')
                                or (seq_id_1 > seq_id_2 and atom_id_1 == 'H' and atom_id_2.startswith('HA'))):
                            pass

                        else:

                            idx_msg = f"[Check row of {index_tag} {row[index_tag]}] " if index_tag in row else ''

                            err = f"{idx_msg}Found inter-residue RDC vector; "\
                                f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                                f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2}) "\
                                f"in a loop {lp_category}."

                            self._reg.report.error.appendDescription('invalid_data',
                                                                     {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                      'category': lp_category, 'description': err})

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.testRdcVector() ++ Error  - {err}\n")

                    elif atom_id_1 == atom_id_2:

                        idx_msg = f"[Check row of {index_tag} {row[index_tag]}] " if index_tag in row else ''

                        err = f"{idx_msg}Found zero RDC vector; "\
                            f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                            f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2})."

                        self._reg.report.error.appendDescription('invalid_data',
                                                                 {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                  'category': lp_category, 'description': err})

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.testRdcVector() ++ Error  - {err}\n")

                    else:

                        if self._reg.ccU.updateChemCompDict(comp_id_1):  # matches with comp_id in CCD

                            if not self._reg.ccU.hasBond(comp_id_1, atom_id_1, atom_id_2):

                                if self._reg.nefT.validate_comp_atom(comp_id_1, atom_id_1)\
                                   and self._reg.nefT.validate_comp_atom(comp_id_2, atom_id_2):

                                    idx_msg = f"[Check row of {index_tag} {row[index_tag]}] " if index_tag in row else ''

                                    warn = f"{idx_msg}Found an RDC vector over multiple covalent bonds; "\
                                        f"({chain_id_1}:{seq_id_1}:{comp_id_1}:{atom_id_1}, "\
                                        f"{chain_id_2}:{seq_id_2}:{comp_id_2}:{atom_id_2})."

                                    self._reg.report.warning.appendDescription('unusual/rare_data',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': warn})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.testRdcVector() ++ Warning  - {warn}\n")

                                else:  # raised error already somewhere because of invalid atom nomenclature
                                    pass

                        else:  # raised warning already somewhere because of unknown comp_id
                            pass

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.testRdcVector() ++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.testRdcVector() ++ Error  - {str(e)}\n")
