##
# File: NmrDpValidationBase.py
# Date: 17-Aug-2026
#
# Updates:
##
""" Base class for NMR data validation.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.2"

import copy
import itertools
from operator import itemgetter
from typing import List, Optional, Tuple

import numpy

import pynmrstar

try:
    from wwpdb.utils.nmr.NmrDpConstant import (SF_CATEGORIES,
                                               LP_CATEGORIES,
                                               EMPTY_VALUE,
                                               STD_MON_DICT,
                                               NON_METAL_ELEMENTS,
                                               THRESHOLD_FOR_CIRCULAR_SHIFT,
                                               PLANE_LIKE_LOWER_LIMIT,
                                               PLANE_LIKE_UPPER_LIMIT,
                                               DEFAULT_DATUM_COUNTER)
    from wwpdb.utils.nmr.NmrDpRegistry import (NmrDpRegistry,
                                               get_next_path,
                                               test_path_with_suffix)
    from wwpdb.utils.nmr.CifToNmrStar import (has_key_value,
                                              get_first_sf_tag)
    from wwpdb.utils.nmr.NmrVrptUtility import (to_np_array,
                                                distance,
                                                dihedral_angle)
    from wwpdb.utils.nmr.mr.ParserListenerUtil import getTypeOfDihedralRestraint
    from wwpdb.utils.nmr.rci.RCI import RCI
except ImportError:
    from nmr.NmrDpConstant import (SF_CATEGORIES,
                                   LP_CATEGORIES,
                                   EMPTY_VALUE,
                                   STD_MON_DICT,
                                   NON_METAL_ELEMENTS,
                                   THRESHOLD_FOR_CIRCULAR_SHIFT,
                                   PLANE_LIKE_LOWER_LIMIT,
                                   PLANE_LIKE_UPPER_LIMIT,
                                   DEFAULT_DATUM_COUNTER)
    from nmr.NmrDpRegistry import (NmrDpRegistry,
                                   get_next_path,
                                   test_path_with_suffix)
    from nmr.CifToNmrStar import (has_key_value,
                                  get_first_sf_tag)
    from nmr.NmrVrptUtility import (to_np_array,
                                    distance,
                                    dihedral_angle)
    from nmr.mr.ParserListenerUtil import getTypeOfDihedralRestraint
    from nmr.rci.RCI import RCI


def is_non_metal_element(comp_id: str, atom_id: str) -> bool:
    """ Return whether a given atom_id is non metal element.
        @return: True for non metal element, False otherwise
    """

    if comp_id == atom_id:
        return False

    return any(True for elem in NON_METAL_ELEMENTS if atom_id.startswith(elem))


def is_like_planality_boundary(row: dict, lower_limit_name: str, upper_limit_name: str) -> bool:
    """ Return whether boundary conditions like planality restraint.
    """

    try:

        upper_limit = float(row[upper_limit_name])
        lower_limit = float(row[lower_limit_name])

        _array = numpy.array([upper_limit, lower_limit], dtype=float)

        shift = None
        if numpy.nanmin(_array) >= THRESHOLD_FOR_CIRCULAR_SHIFT:
            shift = -(numpy.nanmax(_array) // 360) * 360
        elif numpy.nanmax(_array) <= -THRESHOLD_FOR_CIRCULAR_SHIFT:
            shift = -(numpy.nanmin(_array) // 360) * 360
        if shift is not None:
            upper_limit += shift
            lower_limit += shift

        return PLANE_LIKE_LOWER_LIMIT <= lower_limit < 0.0 < upper_limit <= PLANE_LIKE_UPPER_LIMIT\
            or PLANE_LIKE_LOWER_LIMIT <= lower_limit - 180.0 < 0.0 < upper_limit - 180.0 <= PLANE_LIKE_UPPER_LIMIT\
            or PLANE_LIKE_LOWER_LIMIT <= lower_limit - 360.0 < 0.0 < upper_limit - 360.0 <= PLANE_LIKE_UPPER_LIMIT

    except (ValueError, TypeError):
        return False


def get_atom_name_mapping(lp: pynmrstar.Loop, list_of_tags: List[List[str]]
                          ) -> Optional[List[dict]]:
    """ Return atom name mapping history for each comp_id.
        Each tag should be an array of 'comp_id', 'atom_id', and 'atom_name'.
    """

    mapping, identity_mapping = [], []
    list_of_dat = [None] * len(list_of_tags)

    for idx, tags in enumerate(list_of_tags):
        if set(tags) & set(lp.tags) == set(tags):
            list_of_dat[idx] = lp.get_tag(tags)
            for row in list_of_dat[idx]:
                if row[0] in EMPTY_VALUE or row[1] in EMPTY_VALUE or row[2] in EMPTY_VALUE or row[1] != row[2]:
                    continue
                key = (row[0], row[2])
                if key not in identity_mapping:
                    identity_mapping.append(key)

    for dat in list_of_dat:
        if dat is None:
            continue
        for row in dat:
            if row[0] in EMPTY_VALUE or row[1] in EMPTY_VALUE or row[2] in EMPTY_VALUE or row[1] == row[2]:
                continue
            comp_id = row[0]
            atom_id = row[1]
            atom_name = row[2]

            if not any(m['comp_id'] == comp_id for m in mapping):
                mapping.append({'comp_id': comp_id, 'history': []})

            history = next(m['history'] for m in mapping if m['comp_id'] == comp_id)

            if not any(True for h in history if h['atom_name'] == atom_name):
                history.append({'atom_name': atom_name, 'atom_id': [atom_name] if (comp_id, atom_name) in identity_mapping else []})

            h = next(h for h in history if h['atom_name'] == atom_name)
            if atom_id not in h['atom_id']:
                h['atom_id'].append(atom_id)

    if len(mapping) == 0:
        mapping = None

    else:
        for m in mapping:
            for h in m['history']:
                h['atom_id'] = sorted(h['atom_id'])
            m['history'] = sorted(m['history'], key=itemgetter('atom_name'))
        mapping = sorted(mapping, key=lambda x: (len(x['comp_id']), x['comp_id']))

    return mapping


class NmrDpValidationBase:
    """ Base class for NMR data validation.
    """
    __slots__ = ('__class_name__',
                 '__version__',
                 '_reg',
                 '_rci')

    def __init__(self, registry: NmrDpRegistry) -> None:
        self.__class_name__ = self.__class__.__name__
        self.__version__ = __version__

        self._reg = registry

        # RCI
        self._rci = RCI(False, self._reg.log)

    def getNextPath(self, src_path: str, suffix: str = '~') -> str:
        """ Return candidate next file path.
        """
        return get_next_path(self._reg, src_path, suffix)

    def testPathWithSuffix(self, src_path: str, suffix: str, defer_check: bool = False) -> str:
        """ Return basename(src_path) + suffix file path in either current workspace or default workspace if possible.
        """
        return test_path_with_suffix(self._reg, src_path, suffix, defer_check)

    def getChemCompNameAndStatusOf(self, comp_id: str
                                   ) -> Tuple[bool, Optional[str], Optional[str]]:
        """ Return _chem_comp.name and release status of a given CCD ID, if possible.
        """

        cc_name = cc_rel_status = processing_site = None

        if len(self._reg.star_data_type) > 0 and self._reg.star_data_type[0] == 'Entry'\
           and 'chem_comp' in self._reg.sf_category_list:
            chem_comp_sf = next((sf for sf in self._reg.star_data[0].frame_list if sf.name == f'chem_comp_{comp_id}'), None)

            if chem_comp_sf is not None:
                cc_name = get_first_sf_tag(chem_comp_sf, 'Name')
                if cc_name in EMPTY_VALUE:
                    cc_name = None
                processing_site = get_first_sf_tag(chem_comp_sf, 'Processing_site')
                if processing_site in EMPTY_VALUE:
                    processing_site = None

        if self._reg.ccU.updateChemCompDict(comp_id):  # matches with comp_id in CCD
            is_valid = True

            if cc_name is None:
                cc_name = self._reg.ccU.lastChemCompDict['name']

            if processing_site is not None and processing_site.startswith('BMRB'):
                is_valid = False
                cc_name += f', processing site {processing_site}'
            else:
                cc_rel_status = self._reg.ccU.lastChemCompDict['release_status']

        else:
            is_valid = False

        return is_valid, cc_name, cc_rel_status

    def isNmrAtomName(self, comp_id: str, atom_id: str) -> bool:
        """ Return whether a given atom_id uses NMR conventional atom name.
        """

        return ((atom_id in ('HN', 'CO') and self._reg.csStat.peptideLike(comp_id))
                or atom_id.startswith('Q') or atom_id.startswith('M')
                or atom_id.endswith('%') or atom_id.endswith('#')
                or self._reg.csStat.getMaxAmbigCodeWoSetId(comp_id, atom_id) == 0)

    def getAtomIdListInXplor(self, comp_id: str, atom_id: str
                             ) -> List[str]:
        """ Return atom ID list in IUPAC atom nomenclature for a given atom_id in XPLOR atom nomenclature.
        """

        atom_list, _, details = self._reg.nefT.get_valid_star_atom_in_xplor(comp_id, atom_id)

        return atom_list if details is None else []

    def getAtomIdListInXplorForLigandRemap(self, comp_id: str, atom_id: str, coord_atom_site: dict
                                           ) -> List[str]:
        """ Return atom ID list in IUPAC atom nomenclature for a given atom_id in XPLOR atom nomenclature
            in reference to coordinates' alternative atom IDs. (DAOTHER-9286)
        """

        return self._reg.nefT.get_valid_star_atom_in_xplor_for_ligand_remap(comp_id, atom_id, coord_atom_site)[0]

    def getRepAtomId(self, comp_id: str, atom_id: str) -> str:
        """ Return a representative atom ID in IUPAC atom nomenclature for a given atom_id.
        """

        _atom_id = self._reg.nefT.get_valid_star_atom(comp_id, atom_id, leave_unmatched=False)[0]

        return atom_id if len(_atom_id) == 0 else _atom_id[0]

    def getAtomIdList(self, comp_id: str, atom_id: str
                      ) -> List[str]:
        """ Return atom ID list in IUPAC atom nomenclature for a given atom_id.
        """

        return self._reg.nefT.get_valid_star_atom(comp_id, atom_id, leave_unmatched=False)[0]

    def _getAtomIdListWithAmbigCode(self, comp_id: str, atom_id: str, leave_unmatched: bool = True
                                    ) -> Tuple[List[str], Optional[int], Optional[str]]:
        """ Return lists of atom ID, ambiguity_code, details in IUPAC atom nomenclature for a given conventional NMR atom name.
            @see: NefTranslator.get_valid_star_atom()
        """

        return self._reg.nefT.get_valid_star_atom(comp_id, atom_id, leave_unmatched=leave_unmatched)

    def getReducedAtomNotation(self, chain_id_name: str, chain_id: str, seq_id_name: str, seq_id: int,
                               comp_id_name: str, comp_id: str, atom_id_name: str, atom_id: str) -> str:
        """ Return reduced form of atom notation.
        """

        if self._reg.reduced_atom_notation:
            return f"{chain_id}:{seq_id}:{comp_id}:{atom_id}"

        return f"{chain_id_name} {chain_id}, {seq_id_name} {seq_id}, {comp_id_name} {comp_id}, {atom_id_name} {atom_id}"

    def _getReducedAtomNotations(self, key_items: List[dict], row_data: dict) -> str:
        """ Return reduced form of series of atom notations.
        """

        msg = ''

        if self._reg.reduced_atom_notation:
            j = 0
            for k in key_items:
                msg += f"{row_data[k['name']]}:"
                j += 1
                if j % 4 == 0:
                    msg = msg[:-1] + ' - '
            return msg[:-3]

        for k in key_items:
            msg += k['name'] + f" {row_data[k['name']]}, "

        return msg[:-2]

    def getTypeOfDihedralRestraint(self, data_type: str,  # pylint: disable=no-self-use
                                   peptide: bool, nucleotide: bool, carbohydrate: bool,
                                   atoms: List[dict], plane_like: bool) -> str:
        """ Return type of dihedral angle restraint.
        """

        if data_type in EMPTY_VALUE:
            data_type = getTypeOfDihedralRestraint(peptide, nucleotide, carbohydrate,
                                                   atoms, plane_like)

            if data_type in EMPTY_VALUE or data_type.startswith('pseudo'):
                data_type = 'undefined'
            else:
                data_type = data_type.lower()

        else:
            data_type = data_type.lower()

        if not data_type.endswith('_angle_constraints'):
            data_type += '_angle_constraints'

        return data_type

    def equalsToRepCompId(self, comp_id: str, ref_comp_id: str) -> bool:
        """ Return whether given representative comp IDs are equal.
            @return: True for representative comp IDs are matched, False otherwise
        """

        if comp_id in EMPTY_VALUE or ref_comp_id in EMPTY_VALUE:
            return False

        if '_' in comp_id:
            comp_id = comp_id.split('_')[0]

        elif comp_id not in STD_MON_DICT and self._reg.ccU.updateChemCompDict(comp_id):
            if 'parent_comp_id' in self._reg.ccU.lastChemCompDict:  # matches with comp_id in CCD
                if self._reg.ccU.lastChemCompDict['parent_comp_id'] not in EMPTY_VALUE:
                    comp_id = self._reg.ccU.lastChemCompDict['parent_comp_id']
                    if comp_id in ('A', 'C', 'G', 'T', 'I', 'U') and len(ref_comp_id) == 2 and ref_comp_id.startswith('D'):
                        comp_id = f'D{comp_id}'
                    elif ref_comp_id in ('A', 'C', 'G', 'T', 'I', 'U') and len(comp_id) == 2 and comp_id.startswith('D'):
                        comp_id = comp_id[1]

        if '_' in ref_comp_id:
            ref_comp_id = ref_comp_id.split('_')[0]

        elif ref_comp_id not in STD_MON_DICT and self._reg.ccU.updateChemCompDict(ref_comp_id):
            if 'parent_comp_id' in self._reg.ccU.lastChemCompDict:  # matches with comp_id in CCD
                if self._reg.ccU.lastChemCompDict['parent_comp_id'] not in EMPTY_VALUE:
                    ref_comp_id = self._reg.ccU.lastChemCompDict['parent_comp_id']
                    if ref_comp_id in ('A', 'C', 'G', 'T', 'I', 'U') and len(comp_id) == 2 and comp_id.startswith('D'):
                        ref_comp_id = f'D{ref_comp_id}'
                    elif comp_id in ('A', 'C', 'G', 'T', 'I', 'U') and len(ref_comp_id) == 2 and ref_comp_id.startswith('D'):
                        ref_comp_id = ref_comp_id[1]

        return comp_id == ref_comp_id

    def getNmrBondLength(self, nmr_chain_id_1: str, nmr_seq_id_1: int, nmr_atom_id_1: str,
                         nmr_chain_id_2: str, nmr_seq_id_2: int, nmr_atom_id_2: str
                         ) -> Optional[List[dict]]:
        """ Return the bond length of given two NMR atoms.
            @return: the bond length
        """

        intra_chain = nmr_chain_id_1 == nmr_chain_id_2

        s_1 = self._reg.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id_1)

        if s_1 is None:
            return None

        s_2 = s_1 if intra_chain else self._reg.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id_2)

        if s_2 is None:
            return None

        cif_chain_id_1 = s_1['chain_id']
        cif_chain_id_2 = cif_chain_id_1 if intra_chain else s_2['chain_id']

        seq_align_dic = self._reg.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return None

        seq_key = (nmr_chain_id_1, nmr_seq_id_1, nmr_atom_id_1, nmr_chain_id_2, nmr_seq_id_2, nmr_atom_id_2)

        if seq_key in self._reg.cpC['bond_length']:
            return self._reg.cpC['bond_length'][seq_key]

        result_1 = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                         if seq_align['ref_chain_id'] == nmr_chain_id_1 and seq_align['test_chain_id'] == cif_chain_id_1), None)
        result_2 = result_1 if intra_chain else next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                                                      if seq_align['ref_chain_id'] == nmr_chain_id_2
                                                      and seq_align['test_chain_id'] == cif_chain_id_2), None)

        if None not in (result_1, result_2):

            cif_seq_id_1 = next((test_seq_id for ref_seq_id, test_seq_id
                                 in zip(result_1['ref_seq_id'], result_1['test_seq_id']) if ref_seq_id == nmr_seq_id_1), None)

            if cif_seq_id_1 is None:
                self._reg.cpC['bond_length'][seq_key] = None
                return None

            cif_seq_id_2 = next((test_seq_id for ref_seq_id, test_seq_id
                                 in zip(result_2['ref_seq_id'], result_2['test_seq_id']) if ref_seq_id == nmr_seq_id_2), None)

            if cif_seq_id_2 is None:
                self._reg.cpC['bond_length'][seq_key] = None
                return None

            bond = self.getCoordBondLength(cif_chain_id_1, cif_seq_id_1, nmr_atom_id_1, cif_chain_id_2, cif_seq_id_2, nmr_atom_id_2)

            if bond is not None:
                self._reg.cpC['bond_length'][seq_key] = bond

                return bond

        self._reg.cpC['bond_length'][seq_key] = None

        return None

    def getCoordBondLength(self, cif_chain_id_1: str, cif_seq_id_1: int, cif_atom_id_1: str,
                           cif_chain_id_2: str, cif_seq_id_2: int, cif_atom_id_2: str,
                           label_scheme: bool = True
                           ) -> Optional[List[dict]]:
        """ Return the bond length of given two CIF atoms.
            @return: the bond length
        """

        if not self._reg.cifChecked:
            return None

        try:

            model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self._reg.coord_atom_site_tags else 'ndb_model'

            data_items = [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                          {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                          {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                          {'name': model_num_name, 'type': 'int', 'alt_name': 'model_id'}
                          ]

            atom_site_1 = self._reg.cR.getDictListWithFilter('atom_site',
                                                             data_items,
                                                             [{'name': 'label_asym_id' if label_scheme else 'auth_asym_id',
                                                               'type': 'str', 'value': cif_chain_id_1},
                                                              {'name': 'label_seq_id' if label_scheme else 'auth_seq_id',
                                                               'type': 'int', 'value': cif_seq_id_1},
                                                              {'name': 'label_atom_id' if label_scheme else 'auth_atom_id',
                                                               'type': 'str', 'value': cif_atom_id_1},
                                                              {'name': 'label_alt_id', 'type': 'enum',
                                                               'enum': (self._reg.representative_alt_id,)}
                                                              ])

            atom_site_2 = self._reg.cR.getDictListWithFilter('atom_site',
                                                             data_items,
                                                             [{'name': 'label_asym_id' if label_scheme else 'auth_asym_id',
                                                               'type': 'str', 'value': cif_chain_id_2},
                                                              {'name': 'label_seq_id' if label_scheme else 'auth_seq_id',
                                                               'type': 'int', 'value': cif_seq_id_2},
                                                              {'name': 'label_atom_id' if label_scheme else 'auth_atom_id',
                                                               'type': 'str', 'value': cif_atom_id_2},
                                                              {'name': 'label_alt_id', 'type': 'enum',
                                                               'enum': (self._reg.representative_alt_id,)}
                                                              ])

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.getCoordBondLength() ++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.getCoordBondLength() ++ Error  - {str(e)}\n")

            return None

        model_ids = set(a['model_id'] for a in atom_site_1) | set(a['model_id'] for a in atom_site_2)

        bond = []

        for model_id in model_ids:
            a_1 = next((a for a in atom_site_1 if a['model_id'] == model_id), None)
            a_2 = next((a for a in atom_site_2 if a['model_id'] == model_id), None)

            if None in (a_1, a_2):
                continue

            bond.append({'model_id': model_id, 'distance': round(distance(to_np_array(a_1), to_np_array(a_2)), 3)})

        if len(bond) > 0:
            return bond

        return None

    def _extractCoordStructConf(self, nmr_chain_id: str, nmr_seq_ids: List[int]
                                ) -> List[Optional[str]]:
        """ Extract conformational annotations of coordinate file.
        """

        if nmr_chain_id in self._reg.nmr_struct_conf:
            return self._reg.nmr_struct_conf[nmr_chain_id]

        nmr_struct_conf = [None] * len(nmr_seq_ids)

        cif_ps = self._reg.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return nmr_struct_conf

        cif_chain_id = cif_ps['chain_id']

        if 'struct_conf' not in cif_ps:
            return nmr_struct_conf

        seq_align_dic = self._reg.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return nmr_struct_conf

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id
                       and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            for nmr_seq_id in nmr_seq_ids:

                cif_seq_id = next((test_seq_id for ref_seq_id, test_seq_id
                                   in zip(result['ref_seq_id'], result['test_seq_id'])
                                   if ref_seq_id == nmr_seq_id), None)

                if cif_seq_id is None:
                    continue

                if cif_seq_id not in cif_ps['seq_id']:
                    continue

                nmr_struct_conf[nmr_seq_ids.index(nmr_seq_id)] = cif_ps['struct_conf'][cif_ps['seq_id'].index(cif_seq_id)]

        self._reg.nmr_struct_conf[nmr_chain_id] = nmr_struct_conf

        return nmr_struct_conf

    def isConsistentSequence(self) -> bool:
        """ Perform sequence consistency test among extracted polymer sequences.
            @return: True for valid sequence, False otherwise
        """

        if self._reg.bmrb_only and self._reg.internal_mode:
            return True

        for fileListId in range(self._reg.file_path_list_len):

            input_source = self._reg.report.input_sources[fileListId]
            input_source_dic = input_source.get()

            has_poly_seq = has_key_value(input_source_dic, 'polymer_sequence')
            has_poly_seq_in_lp = has_key_value(input_source_dic, 'polymer_sequence_in_loop')

            if (not has_poly_seq) or (not has_poly_seq_in_lp):
                continue

            poly_seq = input_source_dic['polymer_sequence']
            poly_seq_in_lp = input_source_dic['polymer_sequence_in_loop']

            subtype_with_poly_seq = ['poly_seq' if has_poly_seq else None]

            for subtype in poly_seq_in_lp.keys():
                subtype_with_poly_seq.append(subtype)

            for subtype_pair in itertools.combinations_with_replacement(subtype_with_poly_seq, 2):

                # poly_seq is reference sequence and suppress tests on combinations of two sequences in loop
                if has_poly_seq and ('poly_seq' not in subtype_pair or subtype_pair == ('poly_seq', 'poly_seq')):
                    continue

                subtype1 = subtype_pair[0]  # poly_seq will appear only on subtype1
                subtype2 = subtype_pair[1]

                if None in (subtype1, subtype2):
                    continue

                # reference polymer sequence exists
                if has_poly_seq and subtype1 == 'poly_seq':
                    poly_seq1 = poly_seq

                    ref_chain_ids = {ps1['chain_id'] for ps1 in poly_seq1}

                    for _poly_seq_in_lp in poly_seq_in_lp[subtype2]:
                        poly_seq2 = _poly_seq_in_lp['polymer_sequence']

                        for ps2 in poly_seq2:
                            chain_id = ps2['chain_id']

                            if chain_id not in ref_chain_ids\
                               and not ('identical_chain_id' in ps2 and chain_id not in ps2['identical_chain_id']):
                                return False

                            for ps1 in poly_seq1:

                                if ps1['chain_id'] != chain_id\
                                   and not ('identical_chain_id' in ps2 and ps1['chain_id'] in ps2['identical_chain_id']):
                                    continue

                                for seq_id, comp_id in zip(ps2['seq_id'], ps2['comp_id']):

                                    if seq_id not in ps1['seq_id']:

                                        if comp_id != '.':
                                            return False

                                    else:
                                        _comp_id = ps1['comp_id'][ps1['seq_id'].index(seq_id)]

                                        if comp_id not in EMPTY_VALUE and _comp_id not in EMPTY_VALUE and comp_id != _comp_id:
                                            return False

                #  brute force check
                else:

                    for _poly_seq_in_lp in poly_seq_in_lp[subtype1]:
                        poly_seq1 = _poly_seq_in_lp['polymer_sequence']

                        for _poly_seq_in_lp2 in poly_seq_in_lp[subtype2]:
                            poly_seq2 = _poly_seq_in_lp2['polymer_sequence']

                            # suppress redundant tests inside the same subtype
                            if subtype1 == subtype2 and _poly_seq_in_lp['list_id'] >= _poly_seq_in_lp2['list_id']:
                                continue

                            for ps2 in poly_seq2:
                                chain_id = ps2['chain_id']

                                for ps1 in poly_seq1:

                                    if chain_id != ps1['chain_id']:
                                        continue

                                    for seq_id, comp_id in zip(ps2['seq_id'], ps2['comp_id']):

                                        if seq_id in ps1['seq_id']:
                                            _comp_id = ps1['comp_id'][ps1['seq_id'].index(seq_id)]

                                            if comp_id not in EMPTY_VALUE and _comp_id not in EMPTY_VALUE and comp_id != _comp_id:
                                                return False

                            # inverse check required for unverified sequences
                            for ps1 in poly_seq1:
                                chain_id = ps1['chain_id']

                                for ps2 in poly_seq2:
                                    if chain_id != ps2['chain_id']:
                                        continue

                                    for seq_id, comp_id in zip(ps1['seq_id'], ps1['comp_id']):

                                        if seq_id in ps2['seq_id']:
                                            j = ps2['seq_id'].index(seq_id)
                                            _comp_id = ps2['comp_id'][j]

                                            if comp_id not in EMPTY_VALUE and _comp_id not in EMPTY_VALUE and comp_id != _comp_id:
                                                return False

        return True

    def getDatumCounter(self, master_entry: pynmrstar.Entry) -> dict:
        """ Return Datum counter dictionary.
        """

        file_type = 'nmr-star'

        datum_counter = copy.copy(DEFAULT_DATUM_COUNTER)

        def get_loop_size(content_subtype):
            sf_category = SF_CATEGORIES[file_type][content_subtype]
            lp_category = LP_CATEGORIES[file_type][content_subtype]
            size = 0
            for sf in master_entry.get_saveframes_by_category(sf_category):
                try:
                    lp = sf.get_loop(lp_category)
                except KeyError:
                    continue
                size += len(lp)
            return size

        for content_subtype in self._reg.nmr_rep_content_subtypes:

            if content_subtype == 'chem_shift':
                sf_category = SF_CATEGORIES[file_type][content_subtype]
                lp_category = LP_CATEGORIES[file_type][content_subtype]
                for sf in master_entry.get_saveframes_by_category(sf_category):
                    try:
                        lp = sf.get_loop(lp_category)

                        dat = lp.get_tag(['Atom_isotope_number', 'Atom_type'])
                        for row in dat:
                            if row[0] not in EMPTY_VALUE and row[1] not in EMPTY_VALUE:
                                t = f'{row[0]}{row[1].title()} chemical shifts'
                                if t in datum_counter:
                                    datum_counter[t] += 1
                    except KeyError:
                        continue
            elif content_subtype == 'dist_restraint':
                sf_category = SF_CATEGORIES[file_type][content_subtype]
                lp_category = LP_CATEGORIES[file_type][content_subtype]
                for sf in master_entry.get_saveframes_by_category(sf_category):
                    constraint_type = get_first_sf_tag(sf, 'Constraint_type')
                    try:
                        lp = sf.get_loop(lp_category)

                        if constraint_type == 'hydrogen bond':
                            datum_counter['hydrogen bond distance constraints'] += len(lp)
                        elif constraint_type == 'symmetry':
                            datum_counter['symmetry constraints'] += len(lp)
                        else:
                            if 'Combination_ID' in lp.tags and 'Member_ID' in lp.tags:
                                dat = lp.get_tag(['Combination_ID', 'Member_ID'])
                                for row in dat:
                                    if row[0] in EMPTY_VALUE and row[1] in EMPTY_VALUE:
                                        datum_counter['distance constraints'] += 1
                                    else:
                                        datum_counter['ambiguous distance constraints'] += 1
                            else:
                                datum_counter['distance constraints'] += len(lp)
                    except KeyError:
                        continue
            elif content_subtype == 'dihed_restraint':
                datum_counter['torsion angle constraints'] += get_loop_size(content_subtype)
            elif content_subtype in ('rdc_restraint' 'rdc_raw_data'):
                datum_counter['residual dipolar couplings'] += get_loop_size(content_subtype)
            elif content_subtype == 'noepk_restraint':
                datum_counter['homonuclear NOE values'] += get_loop_size(content_subtype)
            elif content_subtype == 'jcoup_restraint':
                datum_counter['coupling constants'] += get_loop_size(content_subtype)
            elif content_subtype == 'csa_restraint':
                datum_counter['chemical shift anisotropy values'] += get_loop_size(content_subtype)
            elif content_subtype == 'ddc_restraint':
                datum_counter['dipolar coupling values'] += get_loop_size(content_subtype)
            elif content_subtype in ('hvycs_restraint', 'procs_restraint'):
                datum_counter['chemical shift constraints'] += get_loop_size(content_subtype)
            elif content_subtype == 'csp_restraint':
                datum_counter['chemical shift perturbation values'] += get_loop_size(content_subtype)
            elif content_subtype == 'heteronucl_noe_data':
                datum_counter['heteronuclear NOE values'] += get_loop_size(content_subtype)
            elif content_subtype == 'heteronucl_t1_data':
                datum_counter['T1 relaxation values'] += get_loop_size(content_subtype)
            elif content_subtype == 'heteronucl_t2_data':
                datum_counter['T2 relaxation values'] += get_loop_size(content_subtype)
            elif content_subtype == 'heteronucl_t1r_data':
                datum_counter['T1rho relaxation values'] += get_loop_size(content_subtype)
            elif content_subtype == 'order_param_data':
                datum_counter['order parameters'] += get_loop_size(content_subtype)
            elif content_subtype == 'ph_titr_data':
                datum_counter['pKa values'] += get_loop_size(content_subtype)
            elif content_subtype == 'ph_param_data':
                datum_counter['pH NMR parameter values'] += get_loop_size(content_subtype)
            elif content_subtype == 'coupling_const_data':
                datum_counter['coupling constants'] += get_loop_size(content_subtype)
            elif content_subtype == 'ccrd_dd_restraint':
                datum_counter['dipole-dipole cross correlation relaxation values'] += get_loop_size(content_subtype)

        return {k: v for k, v in datum_counter.items() if v > 0}

    def getTautomerOfHistidine(self, nmr_chain_id: str, nmr_seq_id: int) -> str:
        """ Return tautomeric state of a given histidine.
            @return: One of 'biprotonated', 'tau-tautomer', 'pi-tautomer', 'unknown'
        """

        if not self._reg.cifChecked:
            return 'unknown'

        if self._reg.report.isDiamagnetic():
            return 'unknown'

        cif_ps = self._reg.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return 'unknown'

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self._reg.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return 'unknown'

        seq_key = (nmr_chain_id, nmr_seq_id)

        if seq_key in self._reg.cpC['tautomer']:
            return self._reg.cpC['tautomer'][seq_key]

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            cif_seq_id = next((test_seq_id for ref_seq_id, ref_code, test_seq_id
                               in zip(result['ref_seq_id'], result['ref_code'], result['test_seq_id'])
                               if ref_seq_id == nmr_seq_id and ref_code == 'H'), None)

            if cif_seq_id is None:
                self._reg.cpC['tautomer'][seq_key] = 'unknown'
                return 'unknown'

            try:

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self._reg.coord_atom_site_tags else 'ndb_model'

                protons = self._reg.cR.getDictListWithFilter('atom_site',
                                                             [{'name': 'label_atom_id', 'type': 'starts-with-alnum',
                                                               'alt_name': 'atom_id'}
                                                              ],
                                                             [{'name': 'label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                                              {'name': 'label_seq_id', 'type': 'int', 'value': cif_seq_id},
                                                              {'name': 'label_comp_id', 'type': 'str', 'value': 'HIS'},
                                                              {'name': 'type_symbol', 'type': 'str', 'value': 'H'},
                                                              {'name': model_num_name, 'type': 'int',
                                                               'value': self._reg.representative_model_id},
                                                              {'name': 'label_alt_id', 'type': 'enum',
                                                               'enum': (self._reg.representative_alt_id,)}
                                                              ])

            except Exception as e:  # pylint: disable=broad-exception-caught

                self._reg.report.error.appendDescription('internal_error',
                                                         f"+{self.__class_name__}.getTautomerOfHistidine() ++ Error  - " + str(e))

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.getTautomerOfHistidine() ++ Error  - {str(e)}\n")

                return 'unknown'

            if len(protons) > 0:

                has_hd1 = has_he2 = False

                for h in protons:
                    if h['atom_id'] == 'HD1':
                        has_hd1 = True
                    elif h['atom_id'] == 'HE2':
                        has_he2 = True

                if has_hd1 and has_he2:
                    self._reg.cpC['tautomer'][seq_key] = 'biprotonated'
                    return 'biprotonated'

                if has_hd1:
                    self._reg.cpC['tautomer'][seq_key] = 'pi-tautomer'
                    return 'pi-tautomer'

                if has_he2:
                    self._reg.cpC['tautomer'][seq_key] = 'tau-tautomer'
                    return 'tau-tautomer'

        self._reg.cpC['tautomer'][seq_key] = 'unknown'
        return 'unknown'

    def getRotamerOfValine(self, nmr_chain_id: str, nmr_seq_id: int
                           ) -> List[dict]:
        """ Return rotameric state distribution of a given valine.
            @return: One of 'gauche+', 'trans', 'gauche-', 'unknown'
        """

        none = [{'name': 'chi1', 'unknown': 1.0}]

        if not self._reg.cifChecked:
            return none

        cif_ps = self._reg.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return none

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self._reg.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return none

        seq_key = (nmr_chain_id, nmr_seq_id, 'VAL')

        if seq_key in self._reg.cpC['rotamer']:
            return self._reg.cpC['rotamer'][seq_key]

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            cif_seq_id = next((test_seq_id for ref_seq_id, ref_code, test_seq_id
                               in zip(result['ref_seq_id'], result['ref_code'], result['test_seq_id'])
                               if ref_seq_id == nmr_seq_id and ref_code == 'V'), None)

            if cif_seq_id is None:
                self._reg.cpC['rotamer'][seq_key] = none
                return none

            try:

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self._reg.coord_atom_site_tags else 'ndb_model'

                atoms = self._reg.cR.getDictListWithFilter('atom_site',
                                                           [{'name': 'label_atom_id', 'type': 'starts-with-alnum',
                                                             'alt_name': 'atom_id'},
                                                            {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                            {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                            {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                            {'name': model_num_name, 'type': 'int', 'alt_name': 'model_id'}
                                                            ],
                                                           [{'name': 'label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                                            {'name': 'label_seq_id', 'type': 'int', 'value': cif_seq_id},
                                                            {'name': 'label_comp_id', 'type': 'str', 'value': 'VAL'},
                                                            {'name': 'label_alt_id', 'type': 'enum',
                                                             'enum': (self._reg.representative_alt_id,)}
                                                            ])

            except Exception as e:  # pylint: disable=broad-exception-caught

                self._reg.report.error.appendDescription('internal_error',
                                                         f"+{self.__class_name__}.getRotamerOfValine() ++ Error  - " + str(e))

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.getRotamerOfValine() ++ Error  - {str(e)}\n")

                return none

            model_ids = set(a['model_id'] for a in atoms)
            total_models = float(len(model_ids))

            rot1 = {'name': 'chi1', 'gauche-': 0.0, 'trans': 0.0, 'gauche+': 0.0, 'unknown': 0.0}

            for model_id in model_ids:
                _atoms = [a for a in atoms if a['model_id'] == model_id]

                try:
                    n = to_np_array(next(a for a in _atoms if a['atom_id'] == 'N'))
                    ca = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CA'))
                    cb = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CB'))
                    cg1 = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CG1'))

                    chi1 = dihedral_angle(n, ca, cb, cg1)

                    if 0.0 <= chi1 < 120.0:
                        rot1['gauche+'] += 1.0
                    elif -120.0 <= chi1 < 0.0:
                        rot1['gauche-'] += 1.0
                    else:
                        rot1['trans'] += 1.0
                except StopIteration:
                    rot1['unknown'] += 1.0

            if rot1['unknown'] == total_models:
                self._reg.cpC['rotamer'][seq_key] = none
                return none

            if rot1['unknown'] == 0.0:
                del rot1['unknown']

            _rot1 = rot1.copy()

            for k, v in _rot1.items():
                if k == 'name':
                    continue
                rot1[k] = round(v / total_models, 3)

            self._reg.cpC['rotamer'][seq_key] = [rot1]
            return [rot1]

        self._reg.cpC['rotamer'][seq_key] = none
        return none

    def getRotamerOfLeucine(self, nmr_chain_id: str, nmr_seq_id: int
                            ) -> List[dict]:
        """ Return rotameric state distribution of a given leucine.
            @return: One of 'gauche+', 'trans', 'gauche-', 'unknown'
        """

        none = [{'name': 'chi1', 'unknown': 1.0}, {'name': 'chi2', 'unknown': 1.0}]

        if not self._reg.cifChecked:
            return none

        cif_ps = self._reg.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return none

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self._reg.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return none

        seq_key = (nmr_chain_id, nmr_seq_id, 'LEU')

        if seq_key in self._reg.cpC['rotamer']:
            return self._reg.cpC['rotamer'][seq_key]

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            cif_seq_id = next((test_seq_id for ref_seq_id, ref_code, test_seq_id
                               in zip(result['ref_seq_id'], result['ref_code'], result['test_seq_id'])
                               if ref_seq_id == nmr_seq_id and ref_code == 'L'), None)

            if cif_seq_id is None:
                self._reg.cpC['rotamer'][seq_key] = none
                return none

            try:

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self._reg.coord_atom_site_tags else 'ndb_model'

                atoms = self._reg.cR.getDictListWithFilter('atom_site',
                                                           [{'name': 'label_atom_id', 'type': 'starts-with-alnum',
                                                             'alt_name': 'atom_id'},
                                                            {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                            {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                            {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                            {'name': model_num_name, 'type': 'int', 'alt_name': 'model_id'}
                                                            ],
                                                           [{'name': 'label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                                            {'name': 'label_seq_id', 'type': 'int', 'value': cif_seq_id},
                                                            {'name': 'label_comp_id', 'type': 'str', 'value': 'LEU'},
                                                            {'name': 'label_alt_id', 'type': 'enum',
                                                             'enum': (self._reg.representative_alt_id,)}
                                                            ])

            except Exception as e:  # pylint: disable=broad-exception-caught

                self._reg.report.error.appendDescription('internal_error',
                                                         f"+{self.__class_name__}.getRotamerOfLeucine() ++ Error  - " + str(e))

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.getRotamerOfLeucine() ++ Error  - {str(e)}\n")

                return none

            model_ids = set(a['model_id'] for a in atoms)
            total_models = float(len(model_ids))

            rot1 = {'name': 'chi1', 'gauche-': 0.0, 'trans': 0.0, 'gauche+': 0.0, 'unknown': 0.0}
            rot2 = {'name': 'chi2', 'gauche-': 0.0, 'trans': 0.0, 'gauche+': 0.0, 'unknown': 0.0}

            for model_id in model_ids:
                _atoms = [a for a in atoms if a['model_id'] == model_id]

                try:
                    n = to_np_array(next(a for a in _atoms if a['atom_id'] == 'N'))
                    ca = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CA'))
                    cb = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CB'))
                    cg = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CG'))
                    cd1 = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CD1'))

                    chi1 = dihedral_angle(n, ca, cb, cg)

                    if 0.0 <= chi1 < 120.0:
                        rot1['gauche+'] += 1.0
                    elif -120.0 <= chi1 < 0.0:
                        rot1['gauche-'] += 1.0
                    else:
                        rot1['trans'] += 1.0

                    chi2 = dihedral_angle(ca, cb, cg, cd1)

                    if 0.0 <= chi2 < 120.0:
                        rot2['gauche+'] += 1.0
                    elif -120.0 <= chi2 < 0.0:
                        rot2['gauche-'] += 1.0
                    else:
                        rot2['trans'] += 1.0

                except StopIteration:
                    rot1['unknown'] += 1.0
                    rot2['unknown'] += 1.0

            if rot1['unknown'] == total_models:
                self._reg.cpC['rotamer'][seq_key] = none
                return none

            if rot1['unknown'] == 0.0:
                del rot1['unknown']
            if rot2['unknown'] == 0.0:
                del rot2['unknown']

            _rot1 = rot1.copy()
            _rot2 = rot2.copy()

            for k, v in _rot1.items():
                if k == 'name':
                    continue
                rot1[k] = round(v / total_models, 3)

            for k, v in _rot2.items():
                if k == 'name':
                    continue
                rot2[k] = round(v / total_models, 3)

            self._reg.cpC['rotamer'][seq_key] = [rot1, rot2]
            return [rot1, rot2]

        self._reg.cpC['rotamer'][seq_key] = none
        return none

    def getRotamerOfIsoleucine(self, nmr_chain_id: str, nmr_seq_id: int
                               ) -> List[dict]:
        """ Return rotameric state distribution of a given isoleucine.
            @return: One of 'gauche+', 'trans', 'gauche-', 'unknown'
        """

        none = [{'name': 'chi1', 'unknown': 1.0}, {'name': 'chi2', 'unknown': 1.0}]

        if not self._reg.cifChecked:
            return none

        cif_ps = self._reg.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return none

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self._reg.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return none

        seq_key = (nmr_chain_id, nmr_seq_id, 'ILE')

        if seq_key in self._reg.cpC['rotamer']:
            return self._reg.cpC['rotamer'][seq_key]

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            cif_seq_id = next((test_seq_id for ref_seq_id, ref_code, test_seq_id
                               in zip(result['ref_seq_id'], result['ref_code'], result['test_seq_id'])
                               if ref_seq_id == nmr_seq_id and ref_code == 'I'), None)

            if cif_seq_id is None:
                self._reg.cpC['rotamer'][seq_key] = none
                return none

            try:

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self._reg.coord_atom_site_tags else 'ndb_model'

                atoms = self._reg.cR.getDictListWithFilter('atom_site',
                                                           [{'name': 'label_atom_id', 'type': 'starts-with-alnum',
                                                             'alt_name': 'atom_id'},
                                                            {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                            {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                            {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                            {'name': model_num_name, 'type': 'int', 'alt_name': 'model_id'}
                                                            ],
                                                           [{'name': 'label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                                            {'name': 'label_seq_id', 'type': 'int', 'value': cif_seq_id},
                                                            {'name': 'label_comp_id', 'type': 'str', 'value': 'ILE'},
                                                            {'name': 'label_alt_id', 'type': 'enum',
                                                             'enum': (self._reg.representative_alt_id,)}
                                                            ])

            except Exception as e:  # pylint: disable=broad-exception-caught

                self._reg.report.error.appendDescription('internal_error',
                                                         f"+{self.__class_name__}.getRotamerOfIsoleucine() ++ Error  - " + str(e))

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.getRotamerOfIsoleucine() ++ Error  - {str(e)}\n")

                return none

            model_ids = set(a['model_id'] for a in atoms)
            total_models = float(len(model_ids))

            rot1 = {'name': 'chi1', 'gauche-': 0.0, 'trans': 0.0, 'gauche+': 0.0, 'unknown': 0.0}
            rot2 = {'name': 'chi2', 'gauche-': 0.0, 'trans': 0.0, 'gauche+': 0.0, 'unknown': 0.0}

            for model_id in model_ids:
                _atoms = [a for a in atoms if a['model_id'] == model_id]

                try:
                    n = to_np_array(next(a for a in _atoms if a['atom_id'] == 'N'))
                    ca = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CA'))
                    cb = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CB'))
                    cg1 = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CG1'))
                    cd1 = to_np_array(next(a for a in _atoms if a['atom_id'] == 'CD1'))

                    chi1 = dihedral_angle(n, ca, cb, cg1)

                    if 0.0 <= chi1 < 120.0:
                        rot1['gauche+'] += 1.0
                    elif -120.0 <= chi1 < 0.0:
                        rot1['gauche-'] += 1.0
                    else:
                        rot1['trans'] += 1.0

                    chi2 = dihedral_angle(ca, cb, cg1, cd1)

                    if 0.0 <= chi2 < 120.0:
                        rot2['gauche+'] += 1.0
                    elif -120.0 <= chi2 < 0.0:
                        rot2['gauche-'] += 1.0
                    else:
                        rot2['trans'] += 1.0

                except StopIteration:
                    rot1['unknown'] += 1.0
                    rot2['unknown'] += 1.0

            if rot1['unknown'] == total_models:
                self._reg.cpC['rotamer'][seq_key] = none
                return none

            if rot1['unknown'] == 0.0:
                del rot1['unknown']
            if rot2['unknown'] == 0.0:
                del rot2['unknown']

            _rot1 = rot1.copy()
            _rot2 = rot2.copy()

            for k, v in _rot1.items():
                if k == 'name':
                    continue
                rot1[k] = round(v / total_models, 3)

            for k, v in _rot2.items():
                if k == 'name':
                    continue
                rot2[k] = round(v / total_models, 3)

            self._reg.cpC['rotamer'][seq_key] = [rot1, rot2]
            return [rot1, rot2]

        self._reg.cpC['rotamer'][seq_key] = none
        return none
