##
# File: NmrDpValidationPk.py
# Date: 17-Aug-2026
#
# Updates:
##
""" NMR-STAR spectral peak list validation for NMR data validation.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.2"

import functools
from typing import Union

import pynmrstar

try:
    from wwpdb.utils.nmr.NmrDpConstant import (NUM_DIM_ITEMS,
                                               LOW_SEQ_COVERAGE,
                                               EMPTY_VALUE,
                                               MAX_DIM_NUM_OF_SPECTRA)
    from wwpdb.utils.nmr.AlignUtil import (alignPolymerSequence,
                                           assignPolymerSequence)
    from wwpdb.utils.nmr.CifToNmrStar import (has_key_value,
                                              get_first_sf_tag)
    from wwpdb.utils.nmr.NmrDpValidationBase import NmrDpValidationBase
    from wwpdb.utils.nmr.NmrDpRemediationBase import (CCA_ENT_ASM_ID,
                                                      CCA_ENTITY_ID,
                                                      CCA_COMP_IDX,
                                                      CCA_SEQ_ID,
                                                      CCA_COMP_ID,
                                                      CCA_AUTH_ASYM)
except ImportError:
    from nmr.NmrDpConstant import (NUM_DIM_ITEMS,
                                   LOW_SEQ_COVERAGE,
                                   EMPTY_VALUE,
                                   MAX_DIM_NUM_OF_SPECTRA)
    from nmr.AlignUtil import (alignPolymerSequence,
                               assignPolymerSequence)
    from nmr.CifToNmrStar import (has_key_value,
                                  get_first_sf_tag)
    from nmr.NmrDpValidationBase import NmrDpValidationBase
    from nmr.NmrDpRemediationBase import (CCA_ENT_ASM_ID,
                                          CCA_ENTITY_ID,
                                          CCA_COMP_IDX,
                                          CCA_SEQ_ID,
                                          CCA_COMP_ID,
                                          CCA_AUTH_ASYM)


class NmrDpValidationPk(NmrDpValidationBase):
    """ NMR-STAR spectral peak list validation for NMR data validation.
    """
    __slots__ = ()

    def validateStrPk(self, file_list_id: int, file_type: str, content_subtype: str, list_id: int,
                      sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                      sf_framecode: str, lp_category: str) -> bool:
        """ Validate spectral peak lists in NMR-STAR restraint files.
        """

        _num_dim = get_first_sf_tag(sf, NUM_DIM_ITEMS[file_type])

        try:
            num_dim = int(_num_dim)
        except (ValueError, TypeError):
            return False

        if num_dim not in range(1, MAX_DIM_NUM_OF_SPECTRA):
            return False

        max_dim = num_dim + 1

        lp_category = '_Peak_row_format' if content_subtype == 'spectral_peak' else '_Assigned_peak_chem_shift'

        try:

            loop = sf.get_loop(lp_category)

        except KeyError:
            return False

        input_source = self._reg.report.input_sources[file_list_id]
        input_source_dic = input_source.get()

        has_poly_seq_in_lp = has_key_value(input_source_dic, 'polymer_sequence_in_loop')

        if not has_poly_seq_in_lp:
            return False

        coord_atom_site = self._reg.caC['coord_atom_site']
        auth_to_star_seq = self._reg.caC['auth_to_star_seq']
        auth_to_star_seq_ann = self._reg.caC['auth_to_star_seq_ann']
        auth_atom_name_to_id = self._reg.caC['auth_atom_name_to_id']
        auth_atom_name_to_id_ext = self._reg.caC['auth_atom_name_to_id_ext']

        poly_seq_in_lp = input_source_dic['polymer_sequence_in_loop']

        seq_align = chain_assign = br_seq_align = br_chain_assign = np_seq_align = np_chain_assign = None

        if content_subtype in poly_seq_in_lp:
            _poly_seq_in_lp = next((_poly_seq_in_lp for _poly_seq_in_lp in poly_seq_in_lp[content_subtype]
                                    if _poly_seq_in_lp['sf_framecode'] == sf_framecode), None)

            if _poly_seq_in_lp is not None:
                poly_seq = _poly_seq_in_lp['polymer_sequence']

                seq_align, _ =\
                    alignPolymerSequence(self._reg.pA, self._reg.caC['polymer_sequence'], poly_seq, conservative=False)
                chain_assign, _ = assignPolymerSequence(self._reg.pA, self._reg.ccU, file_type,
                                                        self._reg.caC['polymer_sequence'], poly_seq, seq_align)

                if self._reg.caC['branched'] is not None:
                    br_seq_align, _ =\
                        alignPolymerSequence(self._reg.pA, self._reg.caC['branched'], poly_seq, conservative=False)
                    br_chain_assign, _ = assignPolymerSequence(self._reg.pA, self._reg.ccU, file_type,
                                                               self._reg.caC['branched'], poly_seq, br_seq_align)

                if self._reg.caC['non_polymer'] is not None:
                    np_seq_align, _ =\
                        alignPolymerSequence(self._reg.pA, self._reg.caC['non_polymer'], poly_seq, conservative=False)
                    np_chain_assign, _ = assignPolymerSequence(self._reg.pA, self._reg.ccU, file_type,
                                                               self._reg.caC['non_polymer'], poly_seq, np_seq_align)

        @functools.lru_cache()
        def get_auth_seq_scheme(chain_id, seq_id):
            auth_asym_id = auth_seq_id = None

            if seq_id is not None:

                if chain_assign is not None:
                    auth_asym_id = next((ca['ref_chain_id'] for ca in chain_assign if ca['test_chain_id'] == chain_id), None)
                    if auth_asym_id is not None:
                        sa = next((sa for sa in seq_align
                                   if sa['ref_chain_id'] == auth_asym_id and sa['test_chain_id'] == chain_id
                                   and seq_id in sa['test_seq_id'] and sa['sequence_coverage'] >= LOW_SEQ_COVERAGE), None)
                        if sa is not None:
                            _ref_seq_id_name = 'ref_auth_seq_id' if 'ref_auth_seq_id' in sa else 'ref_seq_id'
                            auth_seq_id = next((ref_seq_id for ref_seq_id, test_seq_id
                                                in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                                if test_seq_id == seq_id), None)

                if None in (auth_asym_id, auth_seq_id) and br_seq_align is not None:
                    auth_asym_id = next((ca['ref_chain_id'] for ca in br_chain_assign if ca['test_chain_id'] == chain_id), None)
                    if auth_asym_id is not None:
                        sa = next((sa for sa in br_seq_align
                                   if sa['ref_chain_id'] == auth_asym_id and sa['test_chain_id'] == chain_id
                                   and seq_id in sa['test_seq_id'] and sa['sequence_coverage'] >= LOW_SEQ_COVERAGE), None)
                        if sa is not None:
                            _ref_seq_id_name = 'ref_auth_seq_id' if 'ref_auth_seq_id' in sa else 'ref_seq_id'
                            auth_seq_id = next((ref_seq_id for ref_seq_id, test_seq_id
                                                in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                                if test_seq_id == seq_id), None)

                if None in (auth_asym_id, auth_seq_id) and np_seq_align is not None:
                    auth_asym_id = next((ca['ref_chain_id'] for ca in np_chain_assign if ca['test_chain_id'] == chain_id), None)
                    if auth_asym_id is not None:
                        sa = next((sa for sa in np_seq_align
                                   if sa['ref_chain_id'] == auth_asym_id and sa['test_chain_id'] == chain_id
                                   and seq_id in sa['test_seq_id'] and sa['sequence_coverage'] >= LOW_SEQ_COVERAGE), None)
                        if sa is not None:
                            _ref_seq_id_name = 'ref_auth_seq_id' if 'ref_auth_seq_id' in sa else 'ref_seq_id'
                            auth_seq_id = next((ref_seq_id for ref_seq_id, test_seq_id
                                                in zip(sa[_ref_seq_id_name], sa['test_seq_id'])
                                                if test_seq_id == seq_id), None)

            return auth_asym_id, auth_seq_id

        list_items = ['Details', 'Entry_ID', 'Spectral_peak_list_ID']

        if content_subtype == 'spectral_peak':

            core_items = ['Index_ID', 'ID', 'Volume', 'Volume_uncertainty', 'Height', 'Height_uncertainty']
            aux_items = [item for item in ['Figure_of_merit', 'Restraint'] if item in loop.tags]

            position_item_temps = ['Position_%s', 'Position_uncertainty_%s', 'Line_width_%s', 'Line_width_uncertainty_%s']

            position_items = []

            for dim in range(1, max_dim):
                for idx, position_item_temp in enumerate(position_item_temps):
                    position_item = position_item_temp % dim
                    if idx == 0:
                        position_items.append(position_item)
                    elif position_item in loop.tags:
                        position_items.append(position_item)

            assign_item_temps = ['Entity_assembly_ID_%s', 'Entity_ID_%s', 'Comp_index_ID_%s',
                                 'Seq_ID_%s', 'Comp_ID_%s', 'Atom_ID_%s']
            ambigutity_item_temps = ['Ambiguity_code_%s', 'Ambiguity_set_ID_%s']

            assign_items = []

            for dim in range(1, max_dim):
                for assign_item_temp in assign_item_temps:
                    assign_items.append(assign_item_temp % dim)
                for ambigutity_item_temp in ambigutity_item_temps:
                    ambigutity_item = ambigutity_item_temp % dim
                    if ambigutity_item in loop.tags:
                        assign_items.append(ambigutity_item)

            auth_assign_item_temps = ['Auth_asym_ID_%s', 'Auth_seq_ID_%s', 'Auth_comp_ID_%s', 'Auth_atom_ID_%s']

            auth_assign_items = []

            for dim in range(1, max_dim):
                for auth_assign_item_temp in auth_assign_item_temps:
                    auth_assign_items.append(auth_assign_item_temp % dim)

        else:

            core_items = ['Peak_ID', 'Spectral_dim_ID', 'Set_ID', 'Magnetization_linkage_ID', 'Val']
            aux_items = [item for item in ['Contribution_fractional_val', 'Figure_of_merit',
                                           'Assigned_chem_shift_list_ID', 'Atom_chem_shift_ID']
                         if item in loop.tags]

            assign_items = ['Entity_assembly_ID', 'Entity_ID', 'Comp_index_ID', 'Comp_ID', 'Atom_ID']
            ambigutity_items = ['Ambiguity_code', 'Ambiguity_set_ID']
            for ambiguity_item in ambigutity_items:
                if ambiguity_item in loop.tags:
                    assign_items.append(ambiguity_item)

            auth_assign_items = ['Auth_entity_ID', 'Auth_seq_ID', 'Auth_comp_ID', 'Auth_atom_ID']

        items = core_items
        if len(aux_items) > 0:
            items.extend(aux_items)
        if content_subtype == 'spectral_peak':
            items.extend(position_items)
        items.extend(assign_items)
        items.extend(auth_assign_items)
        items.extend(list_items)

        lp = pynmrstar.Loop.from_scratch(lp_category)

        tags = [f'{lp_category}.{item}' for item in items]

        lp.add_tag(tags)

        prefer_auth_atom_name = False

        if (self._reg.annotation_mode or self._reg.native_combined) and len(auth_atom_name_to_id) > 0:

            count_auth_name = count_auth_id = 0

            for row in loop:

                if content_subtype == 'spectral_peak':

                    for dim in range(1, max_dim):
                        has_auth_seq = valid_auth_seq = True
                        for auth_assign_item_temp in auth_assign_item_temps:
                            auth_assign_item = auth_assign_item_temp % dim
                            if auth_assign_item not in loop.tags:
                                has_auth_seq = valid_auth_seq = False
                                break
                        if has_auth_seq:
                            try:
                                auth_asym_id_ = row[loop.tags.index(auth_assign_item_temps[0] % dim)]
                                auth_seq_id_ = int(row[loop.tags.index(auth_assign_item_temps[1] % dim)])
                                comp_id = row[loop.tags.index(auth_assign_item_temps[2] % dim)]
                                atom_id = row[loop.tags.index(auth_assign_item_temps[3] % dim)]
                                seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                if seq_key not in auth_to_star_seq:
                                    comp_id =\
                                        next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                              if _auth_asym_id == auth_asym_id_ and _auth_seq_id == auth_seq_id_), comp_id)
                                    seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                    if seq_key not in auth_to_star_seq:
                                        valid_auth_seq = False
                            except (ValueError, TypeError):
                                has_auth_seq = valid_auth_seq = False

                        if valid_auth_seq:

                            if atom_id not in EMPTY_VALUE:

                                if comp_id in auth_atom_name_to_id:
                                    if atom_id in auth_atom_name_to_id[comp_id]:
                                        count_auth_name += 1
                                    if atom_id in auth_atom_name_to_id[comp_id].values():
                                        count_auth_id += 1

                        else:

                            chain_id = seq_id = comp_id = atom_id = auth_asym_id = auth_seq_id = None

                            for col, assign_item_temp in enumerate(assign_item_temps):
                                assign_item = assign_item_temp % dim
                                if assign_item not in loop.tags:
                                    continue
                                if col == 0:
                                    chain_id = row[loop.tags.index(assign_item)]
                                elif col == 1:
                                    continue
                                elif col == 2:
                                    try:
                                        seq_id = int(row[loop.tags.index(assign_item)])
                                    except (ValueError, TypeError):
                                        pass
                                elif col == 3:
                                    if seq_id is None:
                                        try:
                                            seq_id = int(row[loop.tags.index(assign_item)])
                                        except (ValueError, TypeError):
                                            pass
                                elif col == 4:
                                    comp_id = row[loop.tags.index(assign_item)]
                                    if comp_id not in EMPTY_VALUE:
                                        comp_id = comp_id.upper()
                                else:
                                    atom_id = row[loop.tags.index(assign_item)]

                            if None not in (chain_id, seq_id):
                                auth_asym_id, auth_seq_id = get_auth_seq_scheme(chain_id, seq_id)

                            if None not in (auth_asym_id, auth_seq_id):
                                seq_key = (auth_asym_id, auth_seq_id, comp_id)
                                if seq_key not in auth_to_star_seq:
                                    comp_id =\
                                        next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                              if _auth_asym_id == auth_asym_id and _auth_seq_id == auth_seq_id), comp_id)
                                    seq_key = (auth_asym_id, auth_seq_id, comp_id)
                                if seq_key in auth_to_star_seq:

                                    if atom_id not in EMPTY_VALUE:

                                        if comp_id in auth_atom_name_to_id:
                                            if atom_id in auth_atom_name_to_id[comp_id]:
                                                count_auth_name += 1
                                            if atom_id in auth_atom_name_to_id[comp_id].values():
                                                count_auth_id += 1

                else:

                    has_auth_seq = valid_auth_seq = True
                    for auth_assign_item in auth_assign_items:
                        if auth_assign_item not in loop.tags:
                            has_auth_seq = valid_auth_seq = False
                            break
                    if has_auth_seq:
                        try:
                            auth_asym_id_ = row[loop.tags.index(auth_assign_items[0])]
                            auth_seq_id_ = int(row[loop.tags.index(auth_assign_items[1])])
                            comp_id = row[loop.tags.index(auth_assign_items[2])]
                            atom_id = row[loop.tags.index(auth_assign_items[3])]
                            seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                            if seq_key not in auth_to_star_seq:
                                comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                if _auth_asym_id == auth_asym_id_ and _auth_seq_id == auth_seq_id_), comp_id)
                                seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                if seq_key not in auth_to_star_seq:
                                    valid_auth_seq = False
                        except (ValueError, TypeError):
                            has_auth_seq = valid_auth_seq = False

                    if valid_auth_seq:

                        if atom_id not in EMPTY_VALUE:

                            if comp_id in auth_atom_name_to_id:
                                if atom_id in auth_atom_name_to_id[comp_id]:
                                    count_auth_name += 1
                                if atom_id in auth_atom_name_to_id[comp_id].values():
                                    count_auth_id += 1

                    else:

                        chain_id = seq_id = comp_id = atom_id = auth_asym_id = auth_seq_id = None

                        for col, assign_item in enumerate(assign_items):
                            if assign_item not in loop.tags:
                                continue
                            if col == 0:
                                chain_id = row[loop.tags.index(assign_item)]
                            elif col == 1:
                                continue
                            elif col == 2:
                                try:
                                    seq_id = int(row[loop.tags.index(assign_item)])
                                except (ValueError, TypeError):
                                    pass
                            elif col == 3:
                                comp_id = row[loop.tags.index(assign_item)]
                                if comp_id not in EMPTY_VALUE:
                                    comp_id = comp_id.upper()
                            else:
                                atom_id = row[loop.tags.index(assign_item)]

                        if None not in (chain_id, seq_id):
                            auth_asym_id, auth_seq_id = get_auth_seq_scheme(chain_id, seq_id)

                        if None not in (auth_asym_id, auth_seq_id):
                            seq_key = (auth_asym_id, auth_seq_id, comp_id)
                            if seq_key not in auth_to_star_seq:
                                comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                if _auth_asym_id == auth_asym_id and _auth_seq_id == auth_seq_id), comp_id)
                                seq_key = (auth_asym_id, auth_seq_id, comp_id)
                            if seq_key in auth_to_star_seq:

                                if atom_id not in EMPTY_VALUE:

                                    if comp_id in auth_atom_name_to_id:
                                        if atom_id in auth_atom_name_to_id[comp_id]:
                                            count_auth_name += 1
                                        if atom_id in auth_atom_name_to_id[comp_id].values():
                                            count_auth_id += 1

            if count_auth_name + count_auth_id == 0:

                for row in loop:

                    if content_subtype == 'spectral_peak':

                        for dim in range(1, max_dim):
                            has_auth_seq = valid_auth_seq = True
                            for auth_assign_item_temp in auth_assign_item_temps:
                                auth_assign_item = auth_assign_item_temp % dim
                                if auth_assign_item not in loop.tags:
                                    has_auth_seq = valid_auth_seq = False
                                    break
                            if has_auth_seq:
                                try:
                                    auth_asym_id_ = row[loop.tags.index(auth_assign_item_temps[0] % dim)]
                                    auth_seq_id_ = int(row[loop.tags.index(auth_assign_item_temps[1] % dim)])
                                    comp_id = row[loop.tags.index(auth_assign_item_temps[2] % dim)]
                                    atom_id = row[loop.tags.index(auth_assign_item_temps[3] % dim)]
                                    seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                    if seq_key not in auth_to_star_seq_ann:
                                        valid_auth_seq = False
                                    else:
                                        _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                                        if _seq_key in coord_atom_site:  # DAOTHER-8817
                                            comp_id = coord_atom_site[_seq_key]['comp_id']
                                except (ValueError, TypeError):
                                    has_auth_seq = valid_auth_seq = False

                            if valid_auth_seq:

                                if atom_id not in EMPTY_VALUE:

                                    if comp_id in auth_atom_name_to_id:
                                        if atom_id in auth_atom_name_to_id[comp_id]:
                                            count_auth_name += 1
                                        if atom_id in auth_atom_name_to_id[comp_id].values():
                                            count_auth_id += 1

                            else:

                                chain_id = seq_id = comp_id = atom_id = auth_asym_id = auth_seq_id = None

                                for col, assign_item_temp in enumerate(assign_item_temps):
                                    assign_item = assign_item_temp % dim
                                    if assign_item not in loop.tags:
                                        continue
                                    if col == 0:
                                        chain_id = row[loop.tags.index(assign_item)]
                                    elif col == 1:
                                        continue
                                    elif col == 2:
                                        try:
                                            seq_id = int(row[loop.tags.index(assign_item)])
                                        except (ValueError, TypeError):
                                            pass
                                    elif col == 3:
                                        if seq_id is None:
                                            try:
                                                seq_id = int(row[loop.tags.index(assign_item)])
                                            except (ValueError, TypeError):
                                                pass
                                    elif col == 4:
                                        comp_id = row[loop.tags.index(assign_item)]
                                        if comp_id not in EMPTY_VALUE:
                                            comp_id = comp_id.upper()
                                    else:
                                        atom_id = row[loop.tags.index(assign_item)]

                                if None not in (chain_id, seq_id):
                                    auth_asym_id, auth_seq_id = get_auth_seq_scheme(chain_id, seq_id)

                                if None not in (auth_asym_id, auth_seq_id):
                                    seq_key = (auth_asym_id, auth_seq_id, comp_id)
                                    if seq_key in auth_to_star_seq_ann:
                                        _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                                        if _seq_key in coord_atom_site:  # DAOTHER-8817
                                            comp_id = coord_atom_site[_seq_key]['comp_id']

                                        if atom_id not in EMPTY_VALUE:

                                            if comp_id in auth_atom_name_to_id:
                                                if atom_id in auth_atom_name_to_id[comp_id]:
                                                    count_auth_name += 1
                                                if atom_id in auth_atom_name_to_id[comp_id].values():
                                                    count_auth_id += 1

                    else:

                        has_auth_seq = valid_auth_seq = True
                        for auth_assign_item in auth_assign_items:
                            if auth_assign_item not in loop.tags:
                                has_auth_seq = valid_auth_seq = False
                                break
                        if has_auth_seq:
                            try:
                                auth_asym_id_ = row[loop.tags.index(auth_assign_items[0])]
                                auth_seq_id_ = int(row[loop.tags.index(auth_assign_items[1])])
                                comp_id = row[loop.tags.index(auth_assign_items[2])]
                                atom_id = row[loop.tags.index(auth_assign_items[3])]
                                seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                if seq_key not in auth_to_star_seq:
                                    valid_auth_seq = False
                                else:
                                    _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                                    if _seq_key in coord_atom_site:  # DAOTHER-8817
                                        comp_id = coord_atom_site[_seq_key]['comp_id']
                            except (ValueError, TypeError):
                                has_auth_seq = valid_auth_seq = False

                        if valid_auth_seq:

                            if atom_id not in EMPTY_VALUE:

                                if comp_id in auth_atom_name_to_id:
                                    if atom_id in auth_atom_name_to_id[comp_id]:
                                        count_auth_name += 1
                                    if atom_id in auth_atom_name_to_id[comp_id].values():
                                        count_auth_id += 1

                        else:

                            chain_id = seq_id = comp_id = atom_id = auth_asym_id = auth_seq_id = None

                            for col, assign_item in enumerate(assign_items):
                                if assign_item not in loop.tags:
                                    continue
                                if col == 0:
                                    chain_id = row[loop.tags.index(assign_item)]
                                elif col == 1:
                                    continue
                                elif col == 2:
                                    try:
                                        seq_id = int(row[loop.tags.index(assign_item)])
                                    except (ValueError, TypeError):
                                        pass
                                elif col == 3:
                                    comp_id = row[loop.tags.index(assign_item)]
                                    if comp_id not in EMPTY_VALUE:
                                        comp_id = comp_id.upper()
                                else:
                                    atom_id = row[loop.tags.index(assign_item)]

                            if None not in (chain_id, seq_id):
                                auth_asym_id, auth_seq_id = get_auth_seq_scheme(chain_id, seq_id)

                            if None not in (auth_asym_id, auth_seq_id):
                                seq_key = (auth_asym_id, auth_seq_id, comp_id)
                                if seq_key in auth_to_star_seq_ann:
                                    _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                                    if _seq_key in coord_atom_site:  # DAOTHER-8817
                                        comp_id = coord_atom_site[_seq_key]['comp_id']

                                    if atom_id not in EMPTY_VALUE:

                                        if comp_id in auth_atom_name_to_id:
                                            if atom_id in auth_atom_name_to_id[comp_id]:
                                                count_auth_name += 1
                                            if atom_id in auth_atom_name_to_id[comp_id].values():
                                                count_auth_id += 1

            prefer_auth_atom_name = count_auth_name > count_auth_id

        index = 1

        for idx, row in enumerate(loop):

            _row = [None] * len(tags)

            for col, item in enumerate(loop.tags):
                if item in items:
                    _row[items.index(item)] = row[col]

            if content_subtype == 'spectral_peak':

                _row[0] = index

                for dim in range(1, max_dim):
                    has_auth_seq = valid_auth_seq = True
                    for auth_assign_item_temp in auth_assign_item_temps:
                        auth_assign_item = auth_assign_item_temp % dim
                        if auth_assign_item not in loop.tags:
                            has_auth_seq = valid_auth_seq = False
                            break
                    if has_auth_seq:
                        try:
                            auth_asym_id_ = row[loop.tags.index(auth_assign_item_temps[0] % dim)]
                            auth_seq_id_ = int(row[loop.tags.index(auth_assign_item_temps[1] % dim)])
                            comp_id = row[loop.tags.index(auth_assign_item_temps[2] % dim)]
                            atom_id = row[loop.tags.index(auth_assign_item_temps[3] % dim)]
                            seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                            if seq_key not in auth_to_star_seq:
                                if self._reg.annotation_mode:
                                    comp_id =\
                                        next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                              if _auth_asym_id == auth_asym_id_ and _auth_seq_id == auth_seq_id_), comp_id)
                                    seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                    if seq_key not in auth_to_star_seq:
                                        valid_auth_seq = False
                                elif seq_key not in auth_to_star_seq_ann:
                                    valid_auth_seq = False
                        except (ValueError, TypeError):
                            has_auth_seq = valid_auth_seq = False

                    if valid_auth_seq:
                        try:
                            entity_assembly_id, seq_id, entity_id, _ = auth_to_star_seq[seq_key]
                            _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                            if _seq_key in coord_atom_site:  # DAOTHER-8817
                                _coord_atom_site = coord_atom_site[_seq_key]
                                if 'chain_id' in _coord_atom_site:
                                    auth_asym_id = _coord_atom_site['chain_id']
                                comp_id = _coord_atom_site['comp_id']
                        except KeyError:
                            entity_assembly_id = seq_id = entity_id = None
                            if self._reg.annotation_mode:
                                auth_asym_id_ =\
                                    next((_auth_asym_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                          if _auth_seq_id == auth_seq_id_ and _auth_comp_id == comp_id), auth_asym_id_)
                                seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                if seq_key in auth_to_star_seq:
                                    row[loop.tags.index(auth_assign_item_temps[0] % dim)] = auth_asym_id
                                    entity_assembly_id, seq_id, entity_id, _ = auth_to_star_seq[seq_key]
                                else:
                                    auth_asym_id_, comp_id =\
                                        next(((_auth_asym_id, _auth_comp_id)
                                              for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                              if _auth_seq_id == auth_seq_id_), (auth_asym_id_, comp_id))
                                    seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                    if seq_key in auth_to_star_seq:
                                        row[loop.tags.index(auth_assign_item_temps[0] % dim)] = auth_asym_id
                                        entity_assembly_id, seq_id, entity_id, _ = auth_to_star_seq[seq_key]

                        if prefer_auth_atom_name:
                            _atom_id = atom_id
                            _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                            if _seq_key in coord_atom_site:
                                _coord_atom_site = coord_atom_site[_seq_key]
                                if comp_id in auth_atom_name_to_id and comp_id == _coord_atom_site['comp_id']\
                                   and _atom_id in auth_atom_name_to_id[comp_id]:
                                    if auth_atom_name_to_id[comp_id][_atom_id] in _coord_atom_site['atom_id']:
                                        atom_id = auth_atom_name_to_id[comp_id][_atom_id]
                                if 'alt_atom_id' in _coord_atom_site and _atom_id in _coord_atom_site['alt_atom_id']\
                                   and comp_id == _coord_atom_site['comp_id']:
                                    atom_id = _coord_atom_site['atom_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]
                                # DAOTHER-8751, 8817 (D_1300043061)
                                elif 'alt_comp_id' in _coord_atom_site and 'alt_atom_id' in _coord_atom_site\
                                     and _atom_id in _coord_atom_site['alt_atom_id']\
                                     and comp_id == _coord_atom_site['alt_comp_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]:  # noqa: E501, pylint: disable=line-too-long
                                    cca_row =\
                                        next((cca_row for cca_row in self._reg.chem_comp_asm_dat
                                              if cca_row[CCA_COMP_ID] == comp_id and cca_row[CCA_SEQ_ID] == _seq_key[0]
                                              and cca_row[CCA_AUTH_ASYM] == _seq_key[1]), None)
                                    if cca_row is not None:
                                        entity_assembly_id, entity_id, seq_id =\
                                            cca_row[CCA_ENT_ASM_ID], cca_row[CCA_ENTITY_ID], cca_row[CCA_COMP_IDX]
                                    if comp_id in auth_atom_name_to_id_ext and _atom_id in auth_atom_name_to_id_ext[comp_id]\
                                       and len(set(_coord_atom_site['alt_comp_id'])) > 1:
                                        atom_id = auth_atom_name_to_id_ext[comp_id][_atom_id]
                                    else:
                                        atom_id = _coord_atom_site['atom_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]
                                elif 'split_comp_id' in _coord_atom_site:
                                    for _comp_id in _coord_atom_site['split_comp_id']:
                                        if _comp_id == comp_id:
                                            continue
                                        __seq_key = (_seq_key[0], _seq_key[1], _comp_id)
                                        if __seq_key not in coord_atom_site:
                                            continue
                                        __coord_atom_site = coord_atom_site[__seq_key]
                                        if 'alt_comp_id' in __coord_atom_site and 'alt_atom_id' in __coord_atom_site\
                                           and _atom_id in __coord_atom_site['alt_atom_id']:
                                            comp_id = _comp_id
                                            cca_row =\
                                                next((cca_row for cca_row in self._reg.chem_comp_asm_dat
                                                      if cca_row[CCA_COMP_ID] == comp_id and cca_row[CCA_SEQ_ID] == _seq_key[0]
                                                      and cca_row[CCA_AUTH_ASYM] == _seq_key[1]), None)
                                            if cca_row is not None:
                                                entity_assembly_id, entity_id, seq_id =\
                                                    cca_row[CCA_ENT_ASM_ID], cca_row[CCA_ENTITY_ID], cca_row[CCA_COMP_IDX]
                                            atom_id = __coord_atom_site['atom_id'][__coord_atom_site['alt_atom_id'].index(_atom_id)]
                                            break
                                        if _atom_id in __coord_atom_site['atom_id']:
                                            comp_id = _comp_id
                                            cca_row =\
                                                next((cca_row for cca_row in self._reg.chem_comp_asm_dat
                                                      if cca_row[CCA_COMP_ID] == comp_id and cca_row[CCA_SEQ_ID] == _seq_key[0]
                                                      and cca_row[CCA_AUTH_ASYM] == _seq_key[1]), None)
                                            if cca_row is not None:
                                                entity_assembly_id, entity_id, seq_id =\
                                                    cca_row[CCA_ENT_ASM_ID], cca_row[CCA_ENTITY_ID], cca_row[CCA_COMP_IDX]
                                            break

                        for col, assign_item_temp in enumerate(assign_item_temps):
                            assign_item = assign_item_temp % dim
                            if col == 0:
                                _row[items.index(assign_item)] = entity_assembly_id
                            elif col == 1:
                                _row[items.index(assign_item)] = entity_id
                            elif col in (2, 3):
                                _row[items.index(assign_item)] = seq_id
                            elif col == 4:
                                _row[items.index(assign_item)] = comp_id
                            else:
                                _row[items.index(assign_item)] = atom_id

                    else:

                        chain_id = seq_id = comp_id = atom_id = auth_asym_id = auth_seq_id = None

                        for col, assign_item_temp in enumerate(assign_item_temps):
                            assign_item = assign_item_temp % dim
                            if assign_item not in loop.tags:
                                continue
                            if col == 0:
                                chain_id = row[loop.tags.index(assign_item)]
                            elif col == 1:
                                continue
                            elif col == 2:
                                try:
                                    seq_id = int(row[loop.tags.index(assign_item)])
                                except (ValueError, TypeError):
                                    pass
                            elif col == 3:
                                if seq_id is None:
                                    try:
                                        seq_id = int(row[loop.tags.index(assign_item)])
                                    except (ValueError, TypeError):
                                        pass
                            elif col == 4:
                                comp_id = row[loop.tags.index(assign_item)]
                                if comp_id not in EMPTY_VALUE:
                                    comp_id = comp_id.upper()
                            else:
                                atom_id = row[loop.tags.index(assign_item)]

                        if None not in (chain_id, seq_id):
                            auth_asym_id, auth_seq_id = get_auth_seq_scheme(chain_id, seq_id)

                        if None not in (auth_asym_id, auth_seq_id):
                            seq_key = (auth_asym_id, auth_seq_id, comp_id)
                            if self._reg.annotation_mode and seq_key not in auth_to_star_seq:
                                comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                if _auth_asym_id == auth_asym_id and _auth_seq_id == auth_seq_id), comp_id)
                                seq_key = (auth_asym_id, auth_seq_id, comp_id)
                            if seq_key in auth_to_star_seq:
                                entity_assembly_id, seq_id, entity_id, _ = auth_to_star_seq[seq_key]
                                _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                                if _seq_key in coord_atom_site:  # DAOTHER-8817
                                    _coord_atom_site = coord_atom_site[_seq_key]
                                    if 'chain_id' in _coord_atom_site:
                                        auth_asym_id = _coord_atom_site['chain_id']
                                    comp_id = _coord_atom_site['comp_id']

                                if prefer_auth_atom_name:
                                    _atom_id = atom_id
                                    _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                                    if _seq_key in coord_atom_site:
                                        _coord_atom_site = coord_atom_site[_seq_key]
                                        if comp_id in auth_atom_name_to_id and comp_id == _coord_atom_site['comp_id']\
                                           and _atom_id in auth_atom_name_to_id[comp_id]:
                                            if auth_atom_name_to_id[comp_id][_atom_id] in _coord_atom_site['atom_id']:
                                                atom_id = auth_atom_name_to_id[comp_id][_atom_id]
                                        if 'alt_atom_id' in _coord_atom_site and _atom_id in _coord_atom_site['alt_atom_id']\
                                           and comp_id == _coord_atom_site['comp_id']:
                                            atom_id = _coord_atom_site['atom_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]
                                        # DAOTHER-8751, 8817 (D_1300043061)
                                        elif 'alt_comp_id' in _coord_atom_site and 'alt_atom_id' in _coord_atom_site\
                                             and _atom_id in _coord_atom_site['alt_atom_id']\
                                             and comp_id == _coord_atom_site['alt_comp_id'][
                                                 _coord_atom_site['alt_atom_id'].index(_atom_id)]:
                                            cca_row =\
                                                next((cca_row for cca_row in self._reg.chem_comp_asm_dat
                                                      if cca_row[CCA_COMP_ID] == comp_id and cca_row[CCA_SEQ_ID] == _seq_key[0]
                                                      and cca_row[CCA_AUTH_ASYM] == _seq_key[1]), None)
                                            if cca_row is not None:
                                                entity_assembly_id, entity_id, seq_id =\
                                                    cca_row[CCA_ENT_ASM_ID], cca_row[CCA_ENTITY_ID], cca_row[CCA_COMP_IDX]
                                            if comp_id in auth_atom_name_to_id_ext\
                                               and _atom_id in auth_atom_name_to_id_ext[comp_id]\
                                               and len(set(_coord_atom_site['alt_comp_id'])) > 1:
                                                atom_id = auth_atom_name_to_id_ext[comp_id][_atom_id]
                                            else:
                                                atom_id = _coord_atom_site['atom_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]  # noqa: E501, pylint: disable=line-too-long
                                        elif 'split_comp_id' in _coord_atom_site:
                                            for _comp_id in _coord_atom_site['split_comp_id']:
                                                if _comp_id == comp_id:
                                                    continue
                                                __seq_key = (_seq_key[0], _seq_key[1], _comp_id)
                                                if __seq_key not in coord_atom_site:
                                                    continue
                                                __coord_atom_site = coord_atom_site[__seq_key]
                                                if 'alt_comp_id' in __coord_atom_site and 'alt_atom_id' in __coord_atom_site\
                                                   and _atom_id in __coord_atom_site['alt_atom_id']:
                                                    comp_id = _comp_id
                                                    cca_row =\
                                                        next((cca_row for cca_row in self._reg.chem_comp_asm_dat
                                                              if cca_row[CCA_COMP_ID] == comp_id
                                                              and cca_row[CCA_SEQ_ID] == _seq_key[0]
                                                              and cca_row[CCA_AUTH_ASYM] == _seq_key[1]), None)
                                                    if cca_row is not None:
                                                        entity_assembly_id, entity_id, seq_id =\
                                                            cca_row[CCA_ENT_ASM_ID], cca_row[CCA_ENTITY_ID], cca_row[CCA_COMP_IDX]
                                                    atom_id = __coord_atom_site['atom_id'][__coord_atom_site['alt_atom_id'].index(_atom_id)]  # noqa: E501, pylint: disable=line-too-long
                                                    break
                                                if _atom_id in __coord_atom_site['atom_id']:
                                                    comp_id = _comp_id
                                                    cca_row =\
                                                        next((cca_row for cca_row in self._reg.chem_comp_asm_dat
                                                              if cca_row[CCA_COMP_ID] == comp_id
                                                              and cca_row[CCA_SEQ_ID] == _seq_key[0]
                                                              and cca_row[CCA_AUTH_ASYM] == _seq_key[1]), None)
                                                    if cca_row is not None:
                                                        entity_assembly_id, entity_id, seq_id =\
                                                            cca_row[CCA_ENT_ASM_ID], cca_row[CCA_ENTITY_ID], cca_row[CCA_COMP_IDX]
                                                    break

                                for col, assign_item_temp in enumerate(assign_item_temps):
                                    assign_item = assign_item_temp % dim
                                    if col == 0:
                                        _row[items.index(assign_item)] = entity_assembly_id
                                    elif col == 1:
                                        _row[items.index(assign_item)] = entity_id
                                    elif col in (2, 3):
                                        _row[items.index(assign_item)] = seq_id
                                    elif col == 4:
                                        _row[items.index(assign_item)] = comp_id
                                    else:
                                        _row[items.index(assign_item)] = atom_id

                                for col, auth_assign_item_temp in enumerate(auth_assign_item_temps):
                                    auth_assign_item = auth_assign_item_temp % dim
                                    if col == 0:
                                        _row[items.index(auth_assign_item)] = auth_asym_id
                                    elif col == 1:
                                        _row[items.index(auth_assign_item)] = auth_seq_id
                                    elif col == 2:
                                        _row[items.index(auth_assign_item)] = comp_id
                                    else:
                                        _row[items.index(auth_assign_item)] = atom_id

            else:

                has_auth_seq = valid_auth_seq = True
                for auth_assign_item in auth_assign_items:
                    if auth_assign_item not in loop.tags:
                        has_auth_seq = valid_auth_seq = False
                        break
                if has_auth_seq:
                    try:
                        auth_asym_id_ = row[loop.tags.index(auth_assign_items[0])]
                        auth_seq_id_ = int(row[loop.tags.index(auth_assign_items[1])])
                        comp_id = row[loop.tags.index(auth_assign_items[2])]
                        atom_id = row[loop.tags.index(auth_assign_items[3])]
                        seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                        if seq_key not in auth_to_star_seq:
                            if self._reg.annotation_mode:
                                comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                if _auth_asym_id == auth_asym_id_ and _auth_seq_id == auth_seq_id_), comp_id)
                                seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                if seq_key not in auth_to_star_seq:
                                    valid_auth_seq = False
                            elif seq_key not in auth_to_star_seq_ann:
                                valid_auth_seq = False
                    except (ValueError, TypeError):
                        has_auth_seq = valid_auth_seq = False

                if valid_auth_seq:
                    try:
                        entity_assembly_id, seq_id, entity_id, _ = auth_to_star_seq[seq_key]
                        _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                        if _seq_key in coord_atom_site:  # DAOTHER-8817
                            _coord_atom_site = coord_atom_site[_seq_key]
                            if 'chain_id' in _coord_atom_site:
                                auth_asym_id = _coord_atom_site['chain_id']
                            comp_id = _coord_atom_site['comp_id']
                    except KeyError:
                        entity_assembly_id = seq_id = entity_id = None
                        if self._reg.annotation_mode:
                            auth_asym_id_ = next((_auth_asym_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                  if _auth_seq_id == auth_seq_id_ and _auth_comp_id == comp_id), auth_asym_id_)
                            seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                            if seq_key in auth_to_star_seq:
                                row[loop.tags.index(auth_assign_items[0])] = auth_asym_id_
                                entity_assembly_id, seq_id, entity_id, _ = auth_to_star_seq[seq_key]
                            else:
                                auth_asym_id_, comp_id = next(((_auth_asym_id, _auth_comp_id)
                                                               for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                                               if _auth_seq_id == auth_seq_id_), (auth_asym_id_, comp_id))
                                seq_key = (auth_asym_id_, auth_seq_id_, comp_id)
                                if seq_key in auth_to_star_seq:
                                    row[loop.tags.index(auth_assign_items[0])] = auth_asym_id_
                                    entity_assembly_id, seq_id, entity_id, _ = auth_to_star_seq[seq_key]

                    if prefer_auth_atom_name:
                        _atom_id = atom_id
                        _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                        if _seq_key in coord_atom_site:
                            _coord_atom_site = coord_atom_site[_seq_key]
                            if comp_id in auth_atom_name_to_id and comp_id == _coord_atom_site['comp_id']\
                               and _atom_id in auth_atom_name_to_id[comp_id]:
                                if auth_atom_name_to_id[comp_id][_atom_id] in _coord_atom_site['atom_id']:
                                    atom_id = auth_atom_name_to_id[comp_id][_atom_id]
                            if 'alt_atom_id' in _coord_atom_site and _atom_id in _coord_atom_site['alt_atom_id']\
                               and comp_id == _coord_atom_site['comp_id']:
                                atom_id = _coord_atom_site['atom_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]
                            # DAOTHER-8751, 8817 (D_1300043061)
                            elif 'alt_comp_id' in _coord_atom_site and 'alt_atom_id' in _coord_atom_site\
                                 and _atom_id in _coord_atom_site['alt_atom_id']\
                                 and comp_id == _coord_atom_site['alt_comp_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]:
                                cca_row = next((cca_row for cca_row in self._reg.chem_comp_asm_dat
                                                if cca_row[CCA_COMP_ID] == comp_id and cca_row[CCA_SEQ_ID] == _seq_key[0]
                                                and cca_row[CCA_AUTH_ASYM] == _seq_key[1]), None)
                                if cca_row is not None:
                                    entity_assembly_id, entity_id, seq_id =\
                                        cca_row[CCA_ENT_ASM_ID], cca_row[CCA_ENTITY_ID], cca_row[CCA_COMP_IDX]
                                if comp_id in auth_atom_name_to_id_ext and _atom_id in auth_atom_name_to_id_ext[comp_id]\
                                   and len(set(_coord_atom_site['alt_comp_id'])) > 1:
                                    atom_id = auth_atom_name_to_id_ext[comp_id][_atom_id]
                                else:
                                    atom_id = _coord_atom_site['atom_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]
                            elif 'split_comp_id' in _coord_atom_site:
                                for _comp_id in _coord_atom_site['split_comp_id']:
                                    if _comp_id == comp_id:
                                        continue
                                    __seq_key = (_seq_key[0], _seq_key[1], _comp_id)
                                    if __seq_key not in coord_atom_site:
                                        continue
                                    __coord_atom_site = coord_atom_site[__seq_key]
                                    if 'alt_comp_id' in __coord_atom_site and 'alt_atom_id' in __coord_atom_site\
                                       and _atom_id in __coord_atom_site['alt_atom_id']:
                                        comp_id = _comp_id
                                        cca_row = next((cca_row for cca_row in self._reg.chem_comp_asm_dat
                                                        if cca_row[CCA_COMP_ID] == comp_id and cca_row[CCA_SEQ_ID] == _seq_key[0]
                                                        and cca_row[CCA_AUTH_ASYM] == _seq_key[1]), None)
                                        if cca_row is not None:
                                            entity_assembly_id, entity_id, seq_id =\
                                                cca_row[CCA_ENT_ASM_ID], cca_row[CCA_ENTITY_ID], cca_row[CCA_COMP_IDX]
                                        atom_id = __coord_atom_site['atom_id'][__coord_atom_site['alt_atom_id'].index(_atom_id)]
                                        break
                                    if _atom_id in __coord_atom_site['atom_id']:
                                        comp_id = _comp_id
                                        cca_row = next((cca_row for cca_row in self._reg.chem_comp_asm_dat
                                                        if cca_row[CCA_COMP_ID] == comp_id and cca_row[CCA_SEQ_ID] == _seq_key[0]
                                                        and cca_row[CCA_AUTH_ASYM] == _seq_key[1]), None)
                                        if cca_row is not None:
                                            entity_assembly_id, entity_id, seq_id =\
                                                cca_row[CCA_ENT_ASM_ID], cca_row[CCA_ENTITY_ID], cca_row[CCA_COMP_IDX]
                                        break

                    for col, assign_item in enumerate(assign_items):
                        if col == 0:
                            _row[items.index(assign_item)] = entity_assembly_id
                        elif col == 1:
                            _row[items.index(assign_item)] = entity_id
                        elif col == 2:
                            _row[items.index(assign_item)] = seq_id
                        elif col == 3:
                            _row[items.index(assign_item)] = comp_id
                        else:
                            _row[items.index(assign_item)] = atom_id

                else:

                    chain_id = seq_id = comp_id = atom_id = auth_asym_id = auth_seq_id = None

                    for col, assign_item in enumerate(assign_items):
                        if assign_item not in loop.tags:
                            continue
                        if col == 0:
                            chain_id = row[loop.tags.index(assign_item)]
                        elif col == 1:
                            continue
                        elif col == 2:
                            try:
                                seq_id = int(row[loop.tags.index(assign_item)])
                            except (ValueError, TypeError):
                                pass
                        elif col == 3:
                            comp_id = row[loop.tags.index(assign_item)]
                            if comp_id not in EMPTY_VALUE:
                                comp_id = comp_id.upper()
                        else:
                            atom_id = row[loop.tags.index(assign_item)]

                    if None not in (chain_id, seq_id):
                        auth_asym_id, auth_seq_id = get_auth_seq_scheme(chain_id, seq_id)

                    if None not in (auth_asym_id, auth_seq_id):
                        seq_key = (auth_asym_id, auth_seq_id, comp_id)
                        if self._reg.annotation_mode and seq_key not in auth_to_star_seq:
                            comp_id = next((_auth_comp_id for _auth_asym_id, _auth_seq_id, _auth_comp_id in auth_to_star_seq
                                            if _auth_asym_id == auth_asym_id and _auth_seq_id == auth_seq_id), comp_id)
                            seq_key = (auth_asym_id, auth_seq_id, comp_id)
                        if seq_key in auth_to_star_seq:
                            entity_assembly_id, seq_id, entity_id, _ = auth_to_star_seq[seq_key]
                            _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                            if _seq_key in coord_atom_site:  # DAOTHER-8817
                                _coord_atom_site = coord_atom_site[_seq_key]
                                if 'chain_id' in _coord_atom_site:
                                    auth_asym_id = _coord_atom_site['chain_id']
                                comp_id = _coord_atom_site['comp_id']

                            if prefer_auth_atom_name:
                                _atom_id = atom_id
                                _seq_key = seq_key if seq_key in coord_atom_site else (seq_key[0], seq_key[1])
                                if _seq_key in coord_atom_site:
                                    _coord_atom_site = coord_atom_site[_seq_key]
                                    if comp_id in auth_atom_name_to_id and comp_id == _coord_atom_site['comp_id']\
                                       and _atom_id in auth_atom_name_to_id[comp_id]:
                                        if auth_atom_name_to_id[comp_id][_atom_id] in _coord_atom_site['atom_id']:
                                            atom_id = auth_atom_name_to_id[comp_id][_atom_id]
                                    if 'alt_atom_id' in _coord_atom_site and _atom_id in _coord_atom_site['alt_atom_id']\
                                       and comp_id == _coord_atom_site['comp_id']:
                                        atom_id = _coord_atom_site['atom_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]
                                    # DAOTHER-8751, 8817 (D_1300043061)
                                    elif 'alt_comp_id' in _coord_atom_site and 'alt_atom_id' in _coord_atom_site\
                                         and _atom_id in _coord_atom_site['alt_atom_id']\
                                         and comp_id == _coord_atom_site['alt_comp_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]:  # noqa: E501, pylint: disable=line-too-long
                                        cca_row = next((cca_row for cca_row in self._reg.chem_comp_asm_dat
                                                        if cca_row[CCA_COMP_ID] == comp_id and cca_row[CCA_SEQ_ID] == _seq_key[0]
                                                        and cca_row[CCA_AUTH_ASYM] == _seq_key[1]), None)
                                        if cca_row is not None:
                                            entity_assembly_id, entity_id, seq_id =\
                                                cca_row[CCA_ENT_ASM_ID], cca_row[CCA_ENTITY_ID], cca_row[CCA_COMP_IDX]
                                        if comp_id in auth_atom_name_to_id_ext and _atom_id in auth_atom_name_to_id_ext[comp_id]\
                                           and len(set(_coord_atom_site['alt_comp_id'])) > 1:
                                            atom_id = auth_atom_name_to_id_ext[comp_id][_atom_id]
                                        else:
                                            atom_id = _coord_atom_site['atom_id'][_coord_atom_site['alt_atom_id'].index(_atom_id)]
                                    elif 'split_comp_id' in _coord_atom_site:
                                        for _comp_id in _coord_atom_site['split_comp_id']:
                                            if _comp_id == comp_id:
                                                continue
                                            __seq_key = (_seq_key[0], _seq_key[1], _comp_id)
                                            if __seq_key not in coord_atom_site:
                                                continue
                                            __coord_atom_site = coord_atom_site[__seq_key]
                                            if 'alt_comp_id' in __coord_atom_site and 'alt_atom_id' in __coord_atom_site\
                                               and _atom_id in __coord_atom_site['alt_atom_id']:
                                                comp_id = _comp_id
                                                cca_row =\
                                                    next((cca_row for cca_row in self._reg.chem_comp_asm_dat
                                                          if cca_row[CCA_COMP_ID] == comp_id and cca_row[CCA_SEQ_ID] == _seq_key[0]
                                                          and cca_row[CCA_AUTH_ASYM] == _seq_key[1]), None)
                                                if cca_row is not None:
                                                    entity_assembly_id, entity_id, seq_id =\
                                                        cca_row[CCA_ENT_ASM_ID], cca_row[CCA_ENTITY_ID], cca_row[CCA_COMP_IDX]
                                                atom_id = __coord_atom_site['atom_id'][__coord_atom_site['alt_atom_id'].index(_atom_id)]  # noqa: E501, pylint: disable=line-too-long
                                                break
                                            if _atom_id in __coord_atom_site['atom_id']:
                                                comp_id = _comp_id
                                                cca_row =\
                                                    next((cca_row for cca_row in self._reg.chem_comp_asm_dat
                                                          if cca_row[CCA_COMP_ID] == comp_id and cca_row[CCA_SEQ_ID] == _seq_key[0]
                                                          and cca_row[CCA_AUTH_ASYM] == _seq_key[1]), None)
                                                if cca_row is not None:
                                                    entity_assembly_id, entity_id, seq_id =\
                                                        cca_row[CCA_ENT_ASM_ID], cca_row[CCA_ENTITY_ID], cca_row[CCA_COMP_IDX]
                                                break

                            for col, assign_item in enumerate(assign_items):
                                if col == 0:
                                    _row[items.index(assign_item)] = entity_assembly_id
                                elif col == 1:
                                    _row[items.index(assign_item)] = entity_id
                                elif col == 2:
                                    _row[items.index(assign_item)] = seq_id
                                elif col == 3:
                                    _row[items.index(assign_item)] = comp_id
                                else:
                                    _row[items.index(assign_item)] = atom_id

                            for col, auth_assign_item in enumerate(auth_assign_items):
                                if col == 0:
                                    _row[items.index(auth_assign_item)] = auth_asym_id
                                elif col == 1:
                                    _row[items.index(auth_assign_item)] = auth_seq_id
                                elif col == 2:
                                    _row[items.index(auth_assign_item)] = comp_id
                                else:
                                    _row[items.index(auth_assign_item)] = atom_id

            _row[-2] = self._reg.entry_id
            _row[-1] = list_id

            lp.add_data(_row)

            index += 1

        del sf[loop]

        sf.add_loop(lp)

        self._reg.c2S.set_entry_id(sf, self._reg.entry_id)
        self._reg.c2S.set_local_sf_id(sf, list_id)

        get_auth_seq_scheme.cache_clear()

        return True
