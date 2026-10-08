##
# File: NmrDpRemediationBase.py
# Date: 17-Aug-2026
#
# Updates:
##
""" Base class for NMR data remediation.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.2"

from typing import Optional, Union

import pynmrstar

try:
    from wwpdb.utils.nmr.NmrDpConstant import (SF_CATEGORIES,
                                               LP_CATEGORIES,
                                               MR_MAX_SPACER_LINES,
                                               NUM_DIM_ITEMS,
                                               SF_ALLOWED_TAGS,
                                               AUX_LP_CATEGORIES,
                                               EMPTY_VALUE,
                                               MAX_DIM_NUM_OF_SPECTRA,
                                               COMMENT_PAT)
    from wwpdb.utils.nmr.NmrDpRegistry import (NmrDpRegistry,
                                               test_path_with_suffix)
    from wwpdb.utils.nmr.CifToNmrStar import get_first_sf_tag
except ImportError:
    from nmr.NmrDpConstant import (SF_CATEGORIES,
                                   LP_CATEGORIES,
                                   MR_MAX_SPACER_LINES,
                                   NUM_DIM_ITEMS,
                                   SF_ALLOWED_TAGS,
                                   AUX_LP_CATEGORIES,
                                   EMPTY_VALUE,
                                   MAX_DIM_NUM_OF_SPECTRA,
                                   COMMENT_PAT)
    from nmr.NmrDpRegistry import (NmrDpRegistry,
                                   test_path_with_suffix)
    from nmr.CifToNmrStar import get_first_sf_tag


# Column positions of self.__reg.chem_comp_asm_dat
CCA_TAGS = ('Entity_assembly_ID',
            'Entity_ID',
            'Comp_index_ID',
            'Seq_ID',
            'Comp_ID',
            'Auth_asym_ID',
            'Auth_seq_ID')

# positions within CCA_TAGS
CCA_ENT_ASM_ID = 0  # Entity_assembly_ID
CCA_ENTITY_ID = 1  # Entity_ID
CCA_COMP_IDX = 2  # Comp_index_ID
CCA_SEQ_ID = 3  # Seq_ID
CCA_COMP_ID = 4  # Comp_ID
CCA_AUTH_ASYM = 5  # Auth_asym_ID
CCA_AUTH_SEQ = 6  # Auth_seq_ID


def get_chem_shift_format(fPath: str
                          ) -> Optional[str]:
    """ Return chemical shift format for an input file.
    """

    with open(fPath, 'r', encoding='utf-8', errors='ignore') as ifh:

        for idx, line in enumerate(ifh):

            if line.isspace() or COMMENT_PAT.match(line):
                continue

            file_type = get_chem_shift_format_from_string(line)

            if file_type is not None or idx >= MR_MAX_SPACER_LINES:
                return file_type

    return None


def get_chem_shift_format_from_string(string: str
                                      ) -> Optional[str]:
    """ Return chemical shift format for a given input.
    """

    if '<!DOCTYPE chemical_shift_list SYSTEM' in string or '<chemical_shift_list>' in string:
        return 'nm-shi-ari'

    if 'VARS' in string and 'RESID ' in string and 'RESNAME ' in string and 'ATOMNAME ' in string and 'SHIFT' in string:
        return 'nm-shi-npi'

    if 'SHIFT_FL_FRMT' in string and 'RES_SIAD' in string:
        return 'nm-shi-pip'

    if 'TYPEDEF SEQUENCE' in string or 'TYPEDEF ASS_TBL_' in string:
        return 'nm-shi-oli'

    return None


class NmrDpRemediationBase:
    """ Base class for NMR data remediation.
    """
    __slots__ = ('__class_name__',
                 '__version__',
                 '_reg',
                 '_paramag')

    def __init__(self, registry: NmrDpRegistry) -> None:
        self.__class_name__ = self.__class__.__name__
        self.__version__ = __version__

        self._reg = registry

        self._paramag = False

    def testPathWithSuffix(self, src_path: str, suffix: str, defer_check: bool = False) -> str:
        """ Return basename(src_path) + suffix file path in either current workspace or default workspace if possible.
        """
        return test_path_with_suffix(self._reg, src_path, suffix, defer_check)

    def cleanUpSf(self) -> bool:
        """ Clean-up third-party saveframes.
        """

        __errors = self._reg.report.getTotalErrors()

        for fileListId in range(self._reg.file_path_list_len):

            if fileListId >= len(self._reg.star_data):
                break

            input_source = self._reg.report.input_sources[fileListId]
            input_source_dic = input_source.get()

            file_type = input_source_dic['file_type']
            category_order = self._reg.c2S.category_order if file_type == 'nmr-star' else self._reg.c2S.category_order_nef

            if self._reg.star_data_type[fileListId] == 'Entry':

                for sf in reversed(self._reg.star_data[fileListId].frame_list):

                    if sf.tag_prefix not in category_order:
                        del self._reg.star_data[fileListId][sf]

            if input_source_dic['content_subtype'] is None:
                continue

            for content_subtype in input_source_dic['content_subtype']:

                sf_category = SF_CATEGORIES[file_type][content_subtype]

                if self._reg.star_data_type[fileListId] == 'Loop':
                    pass

                elif self._reg.star_data_type[fileListId] == 'Saveframe':
                    sf = self._reg.star_data[fileListId]

                    self._cleanUpSf(file_type, content_subtype, sf)

                else:

                    for sf in self._reg.star_data[fileListId].get_saveframes_by_category(sf_category):

                        self._cleanUpSf(file_type, content_subtype, sf)

        return self._reg.report.getTotalErrors() == __errors

    def _cleanUpSf(self, file_type: str, content_subtype: str,  # pylint: disable=no-self-use
                   sf: Union[pynmrstar.Saveframe, pynmrstar.Loop]) -> None:
        """ Clean-up third-party saveframes.
        """

        tags_to_be_removed = [t[0] for t in sf.tags if t[0] not in SF_ALLOWED_TAGS[file_type][content_subtype]]

        if len(tags_to_be_removed) == 0:
            return

        sf.remove_tag(tags_to_be_removed)

    def removeUnusedPdbInsCode(self, file_list_id: int, content_subtype: str,
                               sf: Union[pynmrstar.Saveframe, pynmrstar.Loop], lp_category: str) -> bool:
        """ Remove unused PDB_ind_code tags from loops.
        """

        loop = sf if self._reg.star_data_type[file_list_id] == 'Loop' else sf.get_loop(lp_category)

        if loop is None:
            return False

        if content_subtype == 'chem_shift':
            tags = ['PDB_ins_code']
        elif content_subtype in ('dist_restraint', 'rdc_restraint'):
            tags = ['PDB_ins_code_1', 'PDB_ins_code_2']
        elif content_subtype == 'dihed_restraint':
            tags = ['PDB_ins_code_1', 'PDB_ins_code_2', 'PDB_ins_code_3', 'PDB_ins_code_4']
        else:
            return False

        if set(tags) & set(loop.tags) != set(tags):
            return False

        try:

            dat = loop.get_tag(tags)

            for row in dat:
                if row is not None and len(row) > 0:
                    for col in row:
                        if col is not None and col not in EMPTY_VALUE:
                            return False

            loop.remove_tag(tags)

            return True

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.removeUnusedPdbInsCode() ++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.removeUnusedPdbInsCode() ++ Error  - {str(e)}\n")

        return False

    def fixChainIdInLoop(self, file_list_id: int, file_type: str, content_subtype: str, sf_framecode: str,
                         chain_id: str, _chain_id: str) -> None:
        """ Fix chain ID of interesting loop.
        """

        sf_category = SF_CATEGORIES[file_type][content_subtype]
        lp_category = LP_CATEGORIES[file_type][content_subtype]

        if file_type == 'nmr-star' and content_subtype == 'spectral_peak_alt':
            lp_category = '_Assigned_peak_chem_shift'

        if self._reg.star_data_type[file_list_id] == 'Loop':
            sf = self._reg.star_data[file_list_id]

            if sf_framecode == '':
                self._fixChainIdInLoop(file_list_id, file_type, content_subtype, sf, lp_category, chain_id, _chain_id)

        elif self._reg.star_data_type[file_list_id] == 'Saveframe':
            sf = self._reg.star_data[file_list_id]

            if get_first_sf_tag(sf, 'sf_framecode') == sf_framecode:
                self._fixChainIdInLoop(file_list_id, file_type, content_subtype, sf, lp_category, chain_id, _chain_id)

        else:

            for sf in self._reg.star_data[file_list_id].get_saveframes_by_category(sf_category):

                if get_first_sf_tag(sf, 'sf_framecode') != sf_framecode:
                    continue

                if not any(True for loop in sf.loops if loop.category == lp_category):
                    continue

                self._fixChainIdInLoop(file_list_id, file_type, content_subtype, sf, lp_category, chain_id, _chain_id)

    def _fixChainIdInLoop(self, file_list_id: int, file_type: str, content_subtype: str,
                          sf: Union[pynmrstar.Saveframe, pynmrstar.Loop], lp_category: str,
                          chain_id: str, _chain_id: str) -> None:
        """ Fix chain ID of interesting loop.
        """

        uniq_chain_ids = self._reg.report.getChainIdsForSameEntity() is None

        chain_id_name = 'chain_code' if file_type == 'nef' else 'Entity_assembly_ID'
        entity_id_name = None if file_type == 'nef' else 'Entity_ID'

        max_dim = 2

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

            except ValueError:  # raised error already at __testIndexConsistency()
                return

            max_dim = num_dim + 1

        loop = sf if self._reg.star_data_type[file_list_id] == 'Loop' else sf.get_loop(lp_category)

        if max_dim == 2:

            chain_id_col = loop.tags.index(chain_id_name) if chain_id_name in loop.tags else -1
            entity_id_col = -1
            if entity_id_name is not None:
                entity_id_col = loop.tags.index(entity_id_name) if entity_id_name in loop.tags else -1

            if chain_id_col == -1:
                return

            for row in loop:

                if row[chain_id_col] != chain_id:
                    continue

                row[chain_id_col] = _chain_id

                if uniq_chain_ids and entity_id_col != -1:
                    row[entity_id_col] = _chain_id

        else:

            for i in range(1, max_dim):

                _chain_id_name = f'{chain_id_name}_{i}'
                _entity_id_name = None if entity_id_name is None else f'{entity_id_name}_{i}'

                chain_id_col = loop.tags.index(_chain_id_name) if _chain_id_name in loop.tags else -1
                entity_id_col = -1
                if _entity_id_name is not None:
                    entity_id_col = loop.tags.index(_entity_id_name) if _entity_id_name in loop.tags else -1

                if chain_id_col == -1:
                    continue

                for row in loop:

                    if row[chain_id_col] != chain_id:
                        continue

                    row[chain_id_col] = _chain_id

                    if uniq_chain_ids and entity_id_col != -1:
                        row[entity_id_col] = _chain_id

    def fixSeqIdInLoop(self, file_list_id: int, file_type: str, content_subtype: str, sf_framecode: str,
                       chain_id: str, seq_id_conv_dict: dict) -> None:
        """ Fix sequence ID of interesting loop.
        """

        sf_category = SF_CATEGORIES[file_type][content_subtype]
        lp_category = LP_CATEGORIES[file_type][content_subtype]

        if file_type == 'nmr-star' and content_subtype == 'spectral_peak_alt':
            lp_category = '_Assigned_peak_chem_shift'

        if self._reg.star_data_type[file_list_id] == 'Loop':
            sf = self._reg.star_data[file_list_id]

            if sf_framecode == '':
                self._fixSeqIdInLoop(file_list_id, file_type, content_subtype, sf, lp_category, chain_id, seq_id_conv_dict)

        elif self._reg.star_data_type[file_list_id] == 'Saveframe':
            sf = self._reg.star_data[file_list_id]

            if get_first_sf_tag(sf, 'sf_framecode') == sf_framecode:
                self._fixSeqIdInLoop(file_list_id, file_type, content_subtype, sf, lp_category, chain_id, seq_id_conv_dict)

        else:

            for sf in self._reg.star_data[file_list_id].get_saveframes_by_category(sf_category):

                if get_first_sf_tag(sf, 'sf_framecode') != sf_framecode:
                    continue

                if not any(True for loop in sf.loops if loop.category == lp_category):
                    continue

                self._fixSeqIdInLoop(file_list_id, file_type, content_subtype, sf, lp_category, chain_id, seq_id_conv_dict)

    def _fixSeqIdInLoop(self, file_list_id: int, file_type: str, content_subtype: str,
                        sf: Union[pynmrstar.Saveframe, pynmrstar.Loop], lp_category: str,
                        chain_id: str, seq_id_conv_dict: dict) -> None:
        """ Fix sequence ID of interesting loop.
        """

        chain_id_name = 'chain_code' if file_type == 'nef' else 'Entity_assembly_ID'
        seq_id_name = 'sequence_code' if file_type == 'nef' else 'Comp_index_ID'
        seq_id_alt_name = None if file_type == 'nef' else 'Seq_ID'

        max_dim = 2

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

            except ValueError:  # raised error already at __testIndexConsistency()
                return

            max_dim = num_dim + 1

        loop = sf if self._reg.star_data_type[file_list_id] == 'Loop' else sf.get_loop(lp_category)

        if max_dim == 2:

            chain_id_col = loop.tags.index(chain_id_name) if chain_id_name in loop.tags else -1
            seq_id_col = loop.tags.index(seq_id_name) if seq_id_name in loop.tags else -1
            seq_id_alt_col = -1
            if seq_id_alt_name is not None:
                seq_id_alt_col = loop.tags.index(seq_id_alt_name) if seq_id_alt_name in loop.tags else -1

            if -1 in (chain_id_col, seq_id_col):
                return

            for row in loop:

                if row[chain_id_col] != chain_id:
                    continue

                seq_id = row[seq_id_col]

                if seq_id in seq_id_conv_dict:
                    row[seq_id_col] = seq_id_conv_dict[seq_id]

                if seq_id_alt_col == -1:
                    continue

                seq_id_alt = row[seq_id_alt_col]

                if seq_id_alt in seq_id_conv_dict:
                    row[seq_id_alt_col] = seq_id_conv_dict[seq_id_alt]

        else:

            for i in range(1, max_dim):

                _chain_id_name = f'{chain_id_name}_{i}'
                _seq_id_name = f'{seq_id_name}_{i}'

                chain_id_col = loop.tags.index(_chain_id_name) if _chain_id_name in loop.tags else -1
                seq_id_col = loop.tags.index(_seq_id_name) if _seq_id_name in loop.tags else -1
                seq_id_alt_col = -1
                if seq_id_alt_name is not None:
                    _seq_id_alt_name = f'{seq_id_alt_name}_{i}'
                    seq_id_alt_col = loop.tags.index(_seq_id_alt_name) if _seq_id_alt_name in loop.tags else -1

                if -1 in (chain_id_col, seq_id_col):
                    continue

                for row in loop:

                    if row[chain_id_col] != chain_id:
                        continue

                    seq_id = row[seq_id_col]

                    if seq_id in seq_id_conv_dict:
                        row[seq_id_col] = seq_id_conv_dict[seq_id]

                    if seq_id_alt_col == -1:
                        continue

                    seq_id_alt = row[seq_id_alt_col]

                    if seq_id_alt in seq_id_conv_dict:
                        row[seq_id_alt_col] = seq_id_conv_dict[seq_id_alt]

    def fixCompIdInLoop(self, file_list_id: int, file_type: str, content_subtype: str, sf_framecode: str,
                        chain_id: str, seq_id: int, comp_id_conv_dict: dict) -> None:
        """ Fix comp ID of interesting loop.
        """

        sf_category = SF_CATEGORIES[file_type][content_subtype]
        lp_category = LP_CATEGORIES[file_type][content_subtype]

        if file_type == 'nmr-star' and content_subtype == 'spectral_peak_alt':
            lp_category = '_Assigned_peak_chem_shift'

        if self._reg.star_data_type[file_list_id] == 'Loop':
            sf = self._reg.star_data[file_list_id]

            if sf_framecode == '':
                self._fixCompIdInLoop(file_list_id, file_type, content_subtype,
                                      sf, lp_category, chain_id, seq_id, comp_id_conv_dict)

        elif self._reg.star_data_type[file_list_id] == 'Saveframe':
            sf = self._reg.star_data[file_list_id]

            if get_first_sf_tag(sf, 'sf_framecode') == sf_framecode:
                self._fixCompIdInLoop(file_list_id, file_type, content_subtype,
                                      sf, lp_category, chain_id, seq_id, comp_id_conv_dict)

        else:

            for sf in self._reg.star_data[file_list_id].get_saveframes_by_category(sf_category):

                if get_first_sf_tag(sf, 'sf_framecode') != sf_framecode:
                    continue

                if not any(True for loop in sf.loops if loop.category == lp_category):
                    continue

                self._fixCompIdInLoop(file_list_id, file_type, content_subtype,
                                      sf, lp_category, chain_id, seq_id, comp_id_conv_dict)

    def _fixCompIdInLoop(self, file_list_id: int, file_type: str, content_subtype: str,
                         sf: Union[pynmrstar.Saveframe, pynmrstar.Loop], lp_category: str,
                         chain_id: str, seq_id: int, comp_id_conv_dict: dict) -> bool:
        """ Fix sequence ID of interesting loop.
        """

        chain_id_name = 'chain_code' if file_type == 'nef' else 'Entity_assembly_ID'
        seq_id_name = 'sequence_code' if file_type == 'nef' else 'Comp_index_ID'
        comp_id_name = 'residue_name' if file_type == 'nef' else 'Comp_ID'

        max_dim = 2

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

            except ValueError:  # raised error already at __testIndexConsistency()
                return

            max_dim = num_dim + 1

        loop = sf if self._reg.star_data_type[file_list_id] == 'Loop' else sf.get_loop(lp_category)

        if max_dim == 2:

            chain_id_col = loop.tags.index(chain_id_name) if chain_id_name in loop.tags else -1
            seq_id_col = loop.tags.index(seq_id_name) if seq_id_name in loop.tags else -1
            comp_id_col = loop.tags.index(comp_id_name) if comp_id_name in loop.tags else -1

            if -1 in (chain_id_col, seq_id_col, comp_id_col):
                return

            for row in loop:

                if row[chain_id_col] != chain_id:
                    continue

                _seq_id = row[seq_id_col]

                if _seq_id in EMPTY_VALUE or int(_seq_id) != seq_id:
                    continue

                comp_id = row[comp_id_col]

                if comp_id in comp_id_conv_dict:
                    row[comp_id_col] = comp_id_conv_dict[comp_id]

        else:

            for i in range(1, max_dim):

                _chain_id_name = f'{chain_id_name}_{i}'
                _seq_id_name = f'{seq_id_name}_{i}'
                _comp_id_name = f'{comp_id_name}_{i}'

                chain_id_col = loop.tags.index(_chain_id_name) if _chain_id_name in loop.tags else -1
                seq_id_col = loop.tags.index(_seq_id_name) if _seq_id_name in loop.tags else -1
                comp_id_col = loop.tags.index(_comp_id_name) if _comp_id_name in loop.tags else -1

                if -1 in (chain_id_col, seq_id_col, comp_id_col):
                    continue

                for row in loop:

                    if row[chain_id_col] != chain_id:
                        continue

                    _seq_id = row[seq_id_col]

                    if _seq_id in EMPTY_VALUE or int(_seq_id) != seq_id:
                        continue

                    comp_id = row[comp_id_col]

                    if comp_id in comp_id_conv_dict:
                        row[comp_id_col] = comp_id_conv_dict[comp_id]

    def fixAtomNomenclature(self, comp_id: str, atom_id_conv_dict: dict) -> None:
        """ Fix atom nomenclature.
        """

        for fileListId in range(self._reg.file_path_list_len):

            input_source = self._reg.report.input_sources[fileListId]
            input_source_dic = input_source.get()

            file_type = input_source_dic['file_type']

            if input_source_dic['content_subtype'] is None:
                continue

            for content_subtype in input_source_dic['content_subtype']:

                if content_subtype == ['entry_info', 'entity', 'chem_shift_ref']:
                    continue

                sf_category = SF_CATEGORIES[file_type][content_subtype]
                lp_category = LP_CATEGORIES[file_type][content_subtype]

                if content_subtype == 'poly_seq':
                    lp_category = AUX_LP_CATEGORIES[file_type][content_subtype][0]

                if file_type == 'nmr-star' and content_subtype == 'spectral_peak_alt':
                    lp_category = '_Assigned_peak_chem_shift'

                if self._reg.star_data_type[fileListId] == 'Loop':
                    sf = self._reg.star_data[fileListId]

                    self._fixAtomNomenclature(fileListId, file_type, content_subtype,
                                              sf, lp_category, comp_id, atom_id_conv_dict)

                elif self._reg.star_data_type[fileListId] == 'Saveframe':
                    sf = self._reg.star_data[fileListId]

                    self._fixAtomNomenclature(fileListId, file_type, content_subtype,
                                              sf, lp_category, comp_id, atom_id_conv_dict)

                else:

                    for sf in self._reg.star_data[fileListId].get_saveframes_by_category(sf_category):

                        if not any(True for loop in sf.loops if loop.category == lp_category):
                            continue

                        self._fixAtomNomenclature(fileListId, file_type, content_subtype,
                                                  sf, lp_category, comp_id, atom_id_conv_dict)

    def _fixAtomNomenclature(self, file_list_id: int, file_type: str, content_subtype: str,
                             sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                             lp_category: str, comp_id: str, atom_id_conv_dict: dict) -> None:
        """ Fix atom nomenclature.
        """

        comp_id_name = 'residue_name' if file_type == 'nef' else 'Comp_ID'
        atom_id_name = 'atom_name' if file_type == 'nef' else 'Atom_ID'

        max_dim = 2

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
                return

            max_dim = num_dim + 1

        loop = sf if self._reg.star_data_type[file_list_id] == 'Loop' else sf.get_loop(lp_category)

        if max_dim == 2:

            comp_id_col = loop.tags.index(comp_id_name) if comp_id_name in loop.tags else -1
            atom_id_col = loop.tags.index(atom_id_name) if atom_id_name in loop.tags else -1

            if -1 in (comp_id_col, atom_id_col):
                return

            for row in loop:

                _comp_id = row[comp_id_col].upper()

                if _comp_id != comp_id:
                    continue

                atom_id = row[atom_id_col]

                if atom_id in atom_id_conv_dict:
                    row[atom_id_col] = atom_id_conv_dict[atom_id]

        else:

            for j in range(1, max_dim):

                _comp_id_name = f'{comp_id_name}_{j}'
                _atom_id_name = f'{atom_id_name}_{j}'

                comp_id_col = loop.tags.index(_comp_id_name) if _comp_id_name in loop.tags else -1
                atom_id_col = loop.tags.index(_atom_id_name) if _atom_id_name in loop.tags else -1

                if -1 in (comp_id_col, atom_id_col):
                    continue

                for row in loop:

                    _comp_id = row[comp_id_col].upper()

                    if _comp_id != comp_id:
                        continue

                    atom_id = row[atom_id_col]

                    if atom_id in atom_id_conv_dict:
                        row[atom_id_col] = atom_id_conv_dict[atom_id]
