##
# File: NmrDpRemediationCs.py
# Date: 17-Aug-2026
#
# Updates:
##
""" Auxiliary remediation of the assigned chemical shift loop of NMR data.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.3"

import copy
from operator import itemgetter
from typing import Union

import pynmrstar

try:
    from wwpdb.utils.nmr.NmrDpConstant import (SF_CATEGORIES,
                                               LP_CATEGORIES,
                                               DATA_ITEMS,
                                               ALLOWED_TAGS,
                                               ITEM_NAMES_IN_CS_LOOP,
                                               EMPTY_VALUE)
    from wwpdb.utils.nmr.AlignUtil import (letterToDigit,
                                           fillBlankCompIdWithOffset,
                                           getScoreOfSeqAlign)
    from wwpdb.utils.nmr.CifToNmrStar import (has_key_value,
                                              get_first_sf_tag)
    from wwpdb.utils.nmr.NmrDpRemediationBase import NmrDpRemediationBase
except ImportError:
    from nmr.NmrDpConstant import (SF_CATEGORIES,
                                   LP_CATEGORIES,
                                   DATA_ITEMS,
                                   ALLOWED_TAGS,
                                   ITEM_NAMES_IN_CS_LOOP,
                                   EMPTY_VALUE)
    from nmr.AlignUtil import (letterToDigit,
                               fillBlankCompIdWithOffset,
                               getScoreOfSeqAlign)
    from nmr.CifToNmrStar import (has_key_value,
                                  get_first_sf_tag)
    from nmr.NmrDpRemediationBase import NmrDpRemediationBase


class NmrDpRemediationCs(NmrDpRemediationBase):
    """ Auxiliary remediation of the assigned chemical shift loop of NMR data.
    """
    __slots__ = ()

    def updateCompIdInCsLoop(self, file_list_id: int, cif_ps: dict, nmr_ps: dict) -> bool:
        """ Update residue name in CS loop to follow CCD replacement.
        """

        if len(cif_ps['seq_id']) != len(nmr_ps['seq_id']) or cif_ps['comp_id'] == nmr_ps['comp_id']:
            return False

        input_source = self._reg.report.input_sources[file_list_id]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        if file_type == 'nef' or file_list_id >= len(self._reg.star_data) or self._reg.star_data[file_list_id] is None:
            return False

        if input_source_dic['content_subtype'] is None:
            return False

        content_subtype = 'chem_shift'

        if content_subtype not in input_source_dic['content_subtype']:
            return False

        has_poly_seq = has_key_value(input_source_dic, 'polymer_sequence')
        has_poly_seq_in_lp = has_key_value(input_source_dic, 'polymer_sequence_in_loop')

        if (not has_poly_seq) or (not has_poly_seq_in_lp):
            return False

        poly_seq_in_lp = input_source_dic['polymer_sequence_in_loop']

        if content_subtype not in poly_seq_in_lp:
            return False

        sf_category = SF_CATEGORIES[file_type][content_subtype]
        lp_category = LP_CATEGORIES[file_type][content_subtype]

        _poly_seq_in_lp = poly_seq_in_lp[content_subtype]

        modified = False

        list_id = 1

        if self._reg.star_data_type[file_list_id] == 'Loop':
            sf = self._reg.star_data[file_list_id]

            try:
                poly_seq = next(poly_seq['polymer_sequence'] for poly_seq in _poly_seq_in_lp if poly_seq['list_id'] == list_id)
                next(ps for ps in poly_seq if ps['chain_id'] == nmr_ps['chain_id'])
            except StopIteration:
                return False

            allow_chain_id_mismatch = len(poly_seq) == 1

            modified |= self._updateCompIdInCsLoop(file_list_id, sf, lp_category, cif_ps, nmr_ps, allow_chain_id_mismatch)

        elif self._reg.star_data_type[file_list_id] == 'Saveframe':
            sf = self._reg.star_data[file_list_id]

            try:
                poly_seq = next(poly_seq['polymer_sequence'] for poly_seq in _poly_seq_in_lp if poly_seq['list_id'] == list_id)
                next(ps for ps in poly_seq if ps['chain_id'] == nmr_ps['chain_id'])
            except StopIteration:
                return False

            allow_chain_id_mismatch = len(poly_seq) == 1

            modified |= self._updateCompIdInCsLoop(file_list_id, sf, lp_category, cif_ps, nmr_ps, allow_chain_id_mismatch)

        else:

            for list_id, sf in enumerate(self._reg.star_data[file_list_id].get_saveframes_by_category(sf_category), start=1):

                if not any(True for loop in sf.loops if loop.category == lp_category):
                    continue

                try:
                    poly_seq = next(poly_seq['polymer_sequence'] for poly_seq in _poly_seq_in_lp if poly_seq['list_id'] == list_id)
                    next(ps for ps in poly_seq if ps['chain_id'] == nmr_ps['chain_id'])
                except StopIteration:
                    continue

                allow_chain_id_mismatch = len(poly_seq) == 1

                modified |= self._updateCompIdInCsLoop(file_list_id, sf, lp_category, cif_ps, nmr_ps, allow_chain_id_mismatch)

        return modified

    def _updateCompIdInCsLoop(self, file_list_id: int,
                              sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                              lp_category: str, cif_ps: dict, nmr_ps: dict, allow_chain_id_mismatch: bool) -> bool:
        """ Update residue name in CS loop to follow CCD replacement.
        """

        loop = sf if self._reg.star_data_type[file_list_id] == 'Loop' else sf.get_loop(lp_category)

        chain_id_col = loop.tags.index('Entity_assembly_ID')
        seq_id_col = loop.tags.index('Comp_index_ID')
        comp_id_col = loop.tags.index('Comp_ID')
        auth_comp_id_col = loop.tags.index('Auth_comp_ID') if 'Auth_comp_ID' in loop.tags else -1

        nmr_chain_id = nmr_ps['chain_id']

        comp_id_map = {nmr_seq_id: cif_comp_id
                       for cif_comp_id, nmr_seq_id, nmr_comp_id
                       in zip(cif_ps['comp_id'], nmr_ps['seq_id'], nmr_ps['comp_id'])
                       if cif_comp_id != nmr_comp_id}

        modified = False

        for row in loop:
            if (not allow_chain_id_mismatch and row[chain_id_col] != nmr_chain_id) or row[seq_id_col] in EMPTY_VALUE:
                continue

            try:
                nmr_seq_id = row[seq_id_col] if isinstance(row[seq_id_col], int) else int(row[seq_id_col])
            except ValueError:
                continue

            if nmr_seq_id not in comp_id_map:
                continue

            cif_comp_id = comp_id_map[nmr_seq_id]

            row[comp_id_col] = cif_comp_id

            if auth_comp_id_col != -1:
                row[auth_comp_id_col] = cif_comp_id

            modified = True

        return modified

    def resolveUnmappedAuthSequenceInCsLoop(self, file_list_id: int, cif_ps: dict, nmr_ps: dict) -> bool:
        """ Resolve unmapped author sequence in CS loop based on sequence alignment.
        """

        input_source = self._reg.report.input_sources[file_list_id]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        if file_type == 'nef' or file_list_id >= len(self._reg.star_data) or self._reg.star_data[file_list_id] is None:
            return False

        if input_source_dic['content_subtype'] is None:
            return False

        content_subtype = 'chem_shift'

        if content_subtype not in input_source_dic['content_subtype']:
            return False

        has_poly_seq = has_key_value(input_source_dic, 'polymer_sequence')
        has_poly_seq_in_lp = has_key_value(input_source_dic, 'polymer_sequence_in_loop')

        if (not has_poly_seq) or (not has_poly_seq_in_lp):
            return False

        poly_seq_in_lp = input_source_dic['polymer_sequence_in_loop']

        if content_subtype not in poly_seq_in_lp:
            return False

        sf_category = SF_CATEGORIES[file_type][content_subtype]
        lp_category = LP_CATEGORIES[file_type][content_subtype]

        _poly_seq_in_lp = poly_seq_in_lp[content_subtype]

        modified = False

        list_id = 1

        if self._reg.star_data_type[file_list_id] == 'Loop':
            sf = self._reg.star_data[file_list_id]

            try:
                poly_seq = next(poly_seq['polymer_sequence'] for poly_seq in _poly_seq_in_lp if poly_seq['list_id'] == list_id)
                next(ps for ps in poly_seq if ps['chain_id'] == nmr_ps['chain_id'])
            except StopIteration:
                return False

            allow_chain_id_mismatch = len(poly_seq) == 1

            modified |= self._resolveUnmappedAuthSequenceInCsLoop(file_list_id,
                                                                  sf, lp_category, cif_ps, nmr_ps, allow_chain_id_mismatch)

        elif self._reg.star_data_type[file_list_id] == 'Saveframe':
            sf = self._reg.star_data[file_list_id]

            try:
                poly_seq = next(poly_seq['polymer_sequence'] for poly_seq in _poly_seq_in_lp if poly_seq['list_id'] == list_id)
                next(ps for ps in poly_seq if ps['chain_id'] == nmr_ps['chain_id'])
            except StopIteration:
                return False

            allow_chain_id_mismatch = len(poly_seq) == 1

            modified |= self._resolveUnmappedAuthSequenceInCsLoop(file_list_id,
                                                                  sf, lp_category, cif_ps, nmr_ps, allow_chain_id_mismatch)

        else:

            for list_id, sf in enumerate(self._reg.star_data[file_list_id].get_saveframes_by_category(sf_category), start=1):

                if not any(True for loop in sf.loops if loop.category == lp_category):
                    continue

                try:
                    poly_seq = next(poly_seq['polymer_sequence'] for poly_seq in _poly_seq_in_lp if poly_seq['list_id'] == list_id)
                    next(ps for ps in poly_seq if ps['chain_id'] == nmr_ps['chain_id'])
                except StopIteration:
                    continue

                allow_chain_id_mismatch = len(poly_seq) == 1

                modified |= self._resolveUnmappedAuthSequenceInCsLoop(file_list_id,
                                                                      sf, lp_category, cif_ps, nmr_ps, allow_chain_id_mismatch)

        return modified

    def _resolveUnmappedAuthSequenceInCsLoop(self, file_list_id: int,
                                             sf: Union[pynmrstar.Saveframe, pynmrstar.Loop], lp_category: str,
                                             cif_ps: dict, nmr_ps: dict, allow_chain_id_mismatch: bool
                                             ) -> bool:
        """ Resolve unmapped author sequence in CS loop based on sequence alignment.
        """

        loop = sf if self._reg.star_data_type[file_list_id] == 'Loop' else sf.get_loop(lp_category)

        chain_id_col = loop.tags.index('Entity_assembly_ID')
        seq_id_col = loop.tags.index('Comp_index_ID')
        auth_chain_id_col = loop.tags.index('Auth_asym_ID') if 'Auth_asym_ID' in loop.tags else -1
        auth_seq_id_col = loop.tags.index('Auth_seq_ID') if 'Auth_seq_ID' in loop.tags else -1

        if auth_chain_id_col == -1:
            return False

        chain_id = cif_ps['chain_id']

        self._reg.pA.clear()
        self._reg.pA.setReferenceSequence(cif_ps['comp_id'], f'REF{chain_id}')
        self._reg.pA.addTestSequence(nmr_ps['comp_id'], chain_id)
        self._reg.pA.doAlign()

        myAlign = self._reg.pA.getAlignment(chain_id)

        length = len(myAlign)

        if length == 0:
            return False

        _matched, unmapped, conflict, offset_1, offset_2 = getScoreOfSeqAlign(myAlign)

        if length == unmapped + conflict or conflict > 0:
            return False

        _cif_ps = cif_ps if offset_1 == 0 else fillBlankCompIdWithOffset(cif_ps, offset_1)
        _nmr_ps = nmr_ps if offset_2 == 0 else fillBlankCompIdWithOffset(nmr_ps, offset_2)

        nmr_chain_id = nmr_ps['chain_id']

        modified = False

        for row in loop:
            if (not allow_chain_id_mismatch and row[chain_id_col] != nmr_chain_id) or row[seq_id_col] in EMPTY_VALUE:
                continue

            try:
                nmr_seq_id = row[seq_id_col] if isinstance(row[seq_id_col], int) else int(row[seq_id_col])
            except ValueError:
                continue

            if nmr_seq_id not in nmr_ps['seq_id']:
                continue

            if row[auth_chain_id_col] in EMPTY_VALUE or row[auth_chain_id_col] == 'UNMAPPED':
                row[auth_chain_id_col] = cif_ps['auth_chain_id' if 'auth_chain_id' in cif_ps else 'chain_id']
                if auth_seq_id_col != -1:
                    try:
                        str(next(_cif_seq_id for _cif_seq_id, _nmr_seq_id
                                 in zip(_cif_ps['auth_seq_id' if 'auth_seq_id' in _cif_ps else 'seq_id'],
                                        _nmr_ps['seq_id'])
                                 if _nmr_seq_id == nmr_seq_id))
                    except StopIteration:  # D_1300044764
                        return False

        for row in loop:
            if (not allow_chain_id_mismatch and row[chain_id_col] != nmr_chain_id) or row[seq_id_col] in EMPTY_VALUE:
                continue

            try:
                nmr_seq_id = row[seq_id_col] if isinstance(row[seq_id_col], int) else int(row[seq_id_col])
            except ValueError:
                continue

            if nmr_seq_id not in nmr_ps['seq_id']:
                continue

            if row[auth_chain_id_col] in EMPTY_VALUE or row[auth_chain_id_col] == 'UNMAPPED':
                row[auth_chain_id_col] = cif_ps['auth_chain_id' if 'auth_chain_id' in cif_ps else 'chain_id']
                if auth_seq_id_col != -1:
                    row[auth_seq_id_col] =\
                        str(next(_cif_seq_id for _cif_seq_id, _nmr_seq_id
                                 in zip(_cif_ps['auth_seq_id' if 'auth_seq_id' in _cif_ps else 'seq_id'],
                                        _nmr_ps['seq_id'])
                                 if _nmr_seq_id == nmr_seq_id))

                modified = True

        return modified

    def sortCsLoop(self) -> bool:
        """ Sort assigned chemical shift loop if required.
        """

        if not self._reg.combined_mode:
            return True

        input_source = self._reg.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        if input_source_dic['content_subtype'] is None:
            return False

        content_subtype = 'chem_shift'

        if content_subtype not in input_source_dic['content_subtype']:
            return False

        sf_category = SF_CATEGORIES[file_type][content_subtype]
        lp_category = LP_CATEGORIES[file_type][content_subtype]

        key_items = self._reg.key_items[file_type][content_subtype]
        data_items = DATA_ITEMS[file_type][content_subtype]
        allowed_tags = ALLOWED_TAGS[file_type][content_subtype]

        item_names = ITEM_NAMES_IN_CS_LOOP[file_type]
        chain_id_name = item_names['chain_id']
        seq_id_name = item_names['seq_id']
        iso_number_name = item_names['isotope_number']
        atom_id_name = item_names['atom_id']
        idx_name = 'ID'

        # modified = False

        for sf in self._reg.star_data[0].get_saveframes_by_category(sf_category):
            sf_framecode = get_first_sf_tag(sf, 'sf_framecode')

            if self._reg.report.error.exists(file_name, sf_framecode):
                continue

            try:

                lp_data = next((lp['data'] for lp in self._reg.lp_data[content_subtype]
                                if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode), None)

                if lp_data is None:
                    lp_data = self._reg.nefT.check_data(sf, lp_category, key_items, data_items, allowed_tags, None, None,
                                                        enforce_allowed_tags=(file_type == 'nmr-star'),
                                                        excl_missing_data=self._reg.excl_missing_data)[0]

                    self._reg.lp_data[content_subtype].append({'file_name': file_name, 'sf_framecode': sf_framecode,
                                                               'category': lp_category, 'data': lp_data})

                _key_items = copy.copy(key_items)
                _key_items.append({'name': idx_name, 'type': 'positive-int'})

                _lp_data = self._reg.nefT.check_data(sf, lp_category, _key_items, data_items, allowed_tags, None, None,
                                                     enforce_allowed_tags=(file_type == 'nmr-star'),
                                                     excl_missing_data=self._reg.excl_missing_data)[0]

            except Exception:  # pylint: disable=broad-exception-caught
                continue

            atoms = []

            chain_ids = set()

            for row in _lp_data:
                chain_ids.add(row[chain_id_name])

            min_seq_ids = {c: 0 for c in chain_ids}

            for row in _lp_data:
                chain_id = row[chain_id_name]
                seq_id = row[seq_id_name]

                if seq_id < min_seq_ids[chain_id]:
                    min_seq_ids[chain_id] = seq_id

            for row in _lp_data:
                chain_id = row[chain_id_name]
                seq_id = row[seq_id_name]
                iso_number = row[iso_number_name]
                atom_id = row[atom_id_name]
                idx = row[idx_name]

                atoms.append((chain_id if isinstance(chain_id, int)
                              else int(chain_id) if chain_id.isdigit()
                              else letterToDigit(chain_id),
                              seq_id - min_seq_ids[chain_id],
                              iso_number, atom_id, idx))

            sorted_atoms = sorted(atoms, key=itemgetter(0, 1, 2, 3))

            sorted_idx = [atom[4] for atom in sorted_atoms]

            if sorted_idx != list(range(1, len(_lp_data) + 1)):

                loop = sf.get_loop(lp_category)

                lp = pynmrstar.Loop.from_scratch(lp_category)

                lp.add_tag(loop.tags)

                dat = [int(idx) for idx in loop.get_tag([idx_name])]

                idx_col = lp.tags.index(idx_name)

                for new_idx, old_idx in enumerate(sorted_idx, start=1):
                    row = loop.data[dat.index(old_idx)]
                    row[idx_col] = new_idx

                    lp.add_data(row)

                del sf[loop]

                sf.add_loop(lp)

        return True
