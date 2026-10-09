##
# File: NmrDpValidationLoop.py
# Date: 17-Aug-2026
#
# Updates:
##
""" Loop data consistency tests for NMR data validation.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.3"

import copy
from typing import List, Union

import pynmrstar

try:
    from wwpdb.utils.nmr.NmrDpConstant import (LP_CATEGORIES,
                                               HARD_PROBE_LIMIT,
                                               INCONSIST_OVER_CONFLICTED,
                                               R_CONFLICTED_DIST_RESTRAINT,
                                               R_INCONSISTENT_DIST_RESTRAINT,
                                               INDEX_TAGS,
                                               CONSIST_ID_TAGS,
                                               PK_KEY_ITEMS,
                                               DATA_ITEMS,
                                               CONSIST_DATA_ITEMS,
                                               NUM_DIM_ITEMS,
                                               ALLOWED_TAGS,
                                               DISALLOWED_PK_TAGS,
                                               SF_TAG_PREFIXES,
                                               AUX_LP_CATEGORIES,
                                               AUX_ALLOWED_TAGS,
                                               ITEM_NAMES_IN_DIHED_LOOP,
                                               MAX_DIM_NUM_OF_SPECTRA,
                                               DIST_UNCERT_MAX,
                                               ANGLE_UNCERT_MAX,
                                               RDC_UNCERT_MAX)
    from wwpdb.utils.nmr.CifToNmrStar import get_first_sf_tag
    from wwpdb.utils.nmr.NmrDpValidationBase import (NmrDpValidationBase,
                                                     is_like_planality_boundary)
except ImportError:
    from nmr.NmrDpConstant import (LP_CATEGORIES,
                                   HARD_PROBE_LIMIT,
                                   INCONSIST_OVER_CONFLICTED,
                                   R_CONFLICTED_DIST_RESTRAINT,
                                   R_INCONSISTENT_DIST_RESTRAINT,
                                   INDEX_TAGS,
                                   CONSIST_ID_TAGS,
                                   PK_KEY_ITEMS,
                                   DATA_ITEMS,
                                   CONSIST_DATA_ITEMS,
                                   NUM_DIM_ITEMS,
                                   ALLOWED_TAGS,
                                   DISALLOWED_PK_TAGS,
                                   SF_TAG_PREFIXES,
                                   AUX_LP_CATEGORIES,
                                   AUX_ALLOWED_TAGS,
                                   ITEM_NAMES_IN_DIHED_LOOP,
                                   MAX_DIM_NUM_OF_SPECTRA,
                                   DIST_UNCERT_MAX,
                                   ANGLE_UNCERT_MAX,
                                   RDC_UNCERT_MAX)
    from nmr.CifToNmrStar import get_first_sf_tag
    from nmr.NmrDpValidationBase import (NmrDpValidationBase,
                                         is_like_planality_boundary)


class NmrDpValidationLoop(NmrDpValidationBase):
    """ Loop data consistency tests for NMR data validation.
    """
    __slots__ = ()

    def testIndexConsistency(self, file_name: str,
                             sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                             sf_framecode: str, lp_category: str, index_tag: str) -> None:
        """ Perform consistency test on index of interesting loops.
        """

        try:

            indices = self._reg.nefT.get_index(sf, lp_category, index_tag)[0]

            if indices != list(range(1, len(indices) + 1)):

                warn = f"Index of loop, '{lp_category}.{index_tag}', should be ordinal numbers."

                self._reg.report.warning.appendDescription('disordered_index',
                                                           {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                            'category': lp_category, 'description': warn})

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.testIndexConsistency() ++ Warning  - {warn}\n")

        except KeyError as e:

            self._reg.report.error.appendDescription('duplicated_index',
                                                     {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                      'category': lp_category, 'description': str(e).strip("'")})

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.testIndexConsistency() ++ KeyError  - {str(e)}\n")

        except LookupError:
            # """
            # self._reg.report.error.appendDescription('missing_mandatory_item',
            #                                           {'file_name': file_name, 'sf_framecode': sf_framecode,
            #                                            'category': lp_category, 'description': str(e).strip("'")})
            #
            # self._reg.log.write(f"+{self.__class_name__}.testIndexConsistency() ++ LookupError  - "
            #                      f"{file_name} {sf_framecode} {lp_category} {str(e)}\n")
            # """
            pass

        except ValueError as e:

            self._reg.report.error.appendDescription('invalid_data',
                                                     {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                      'category': lp_category, 'description': str(e).strip("'")})

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.testIndexConsistency() ++ ValueError  - {str(e)}\n")

        except UserWarning as e:

            errs = str(e).strip("'").split('\n')

            for err in errs:

                if len(err) == 0:
                    continue

                if err.startswith('[Invalid data]'):

                    p = err.index(']') + 2
                    err = err[p:]

                    self._reg.report.error.appendDescription('invalid_data',
                                                             {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                              'category': lp_category, 'description': err})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.testIndexConsistency() ++ ValueError  - {err}\n")

                elif err.startswith('[Too big loop]'):
                    continue

                else:

                    self._reg.report.error.appendDescription('internal_error',
                                                             f"+{self.__class_name__}.testIndexConsistency() ++ Error  - " + err)

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.testIndexConsistency() ++ Error  - {err}\n")

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.testIndexConsistency() ++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.testIndexConsistency() ++ Error  - {str(e)}\n")

    def testDataConsistencyInLoop(self, file_list_id: int, file_name: str, file_type: str, content_subtype: str,
                                  sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                                  sf_framecode: str, lp_category: str, parent_pointer: int) -> bool:
        """ Perform consistency test on data of interesting loops.
        """

        allowed_tags = ALLOWED_TAGS[file_type][content_subtype]
        disallowed_tags = None

        modified = False

        if content_subtype == 'spectral_peak':

            try:

                _num_dim = get_first_sf_tag(sf, NUM_DIM_ITEMS[file_type])
                num_dim = int(_num_dim)

                if num_dim not in range(1, MAX_DIM_NUM_OF_SPECTRA):
                    raise ValueError()

            except ValueError:  # raised error already at testIndexConsistency()
                return False

            max_dim = num_dim + 1

            key_items = []
            for dim in range(1, max_dim):
                for k in PK_KEY_ITEMS[file_type]:
                    if k['type'] == 'float':  # position
                        _k = copy.copy(k)
                        if '%s' in k['name']:
                            _k['name'] = k['name'] % dim
                        key_items.append(_k)
            for k in PK_KEY_ITEMS[file_type]:
                if k['type'] == 'positive-int':  # peak_id
                    key_items.append(k)

            data_items = []
            for d in DATA_ITEMS[file_type][content_subtype]:
                data_items.append(d)
            for dim in range(1, max_dim):
                for d in self._reg.pk_data_items[file_type]:
                    _d = copy.copy(d)
                    if '%s' in d['name']:
                        _d['name'] = d['name'] % dim
                    if 'default-from' in d and '%s' in d['default-from']:  # DAOTHER-7421
                        _d['default-from'] = d['default-from'] % dim
                    data_items.append(_d)

            if max_dim < MAX_DIM_NUM_OF_SPECTRA:
                disallowed_tags = []
                for dim in range(max_dim, MAX_DIM_NUM_OF_SPECTRA):
                    for t in DISALLOWED_PK_TAGS[file_type]:
                        if '%s' in t:
                            t = t % dim
                        disallowed_tags.append(t)

                if self._reg.bmrb_only:
                    loop = sf.get_loop(lp_category)
                    disallowed_tags = list(set(loop.tags) & set(disallowed_tags))
                    loop.remove_tag(disallowed_tags)

        else:

            key_items = self._reg.key_items[file_type][content_subtype]
            data_items = DATA_ITEMS[file_type][content_subtype]

            if file_type == 'nmr-star' and content_subtype == 'ccr_dd_restraint':
                loop = sf.get_loop(lp_category)
                if 'Dipole_2_chem_comp_index_ID_2' in loop.tags:
                    key_items = copy.copy(key_items)
                    key_item = next((key_item for key_item in key_items if key_item['name'] == 'Dipole_2_comp_index_ID_2'), None)
                    if key_item is not None:
                        key_item['name'] = 'Dipole_2_chem_comp_index_ID_2'

        lp_data = None

        try:

            lp_data = self._reg.nefT.check_data(sf, lp_category, key_items, data_items,
                                                allowed_tags, disallowed_tags, parent_pointer=parent_pointer,
                                                test_on_index=True, enforce_non_zero=True, enforce_sign=True,
                                                enforce_range=True, enforce_enum=True,
                                                enforce_allowed_tags=(file_type == 'nmr-star' and not self._reg.bmrb_only),
                                                excl_missing_data=self._reg.excl_missing_data)[0]

            self._reg.lp_data[content_subtype].append({'file_name': file_name, 'sf_framecode': sf_framecode,
                                                       'category': lp_category, 'data': lp_data})

        except KeyError as e:

            self._reg.report.error.appendDescription('multiple_data',
                                                     {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                      'category': lp_category, 'description': str(e).strip("'")})

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInLoop() ++ KeyError  - {str(e)}\n")

        except LookupError as e:

            item = 'format_issue' if 'Unauthorized' in str(e) else 'missing_mandatory_item'

            self._reg.report.error.appendDescription(item,
                                                     {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                      'category': lp_category, 'description': str(e).strip("'")})

            self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInLoop() ++ LookupError  - "
                                f"{file_name} {sf_framecode} {lp_category} {str(e)}\n")

        except ValueError as e:

            self._reg.report.error.appendDescription('invalid_data',
                                                     {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                      'category': lp_category, 'description': str(e).strip("'")})

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInLoop() ++ ValueError  - {str(e)}\n")

        except UserWarning as e:

            warns = str(e).strip("'").split('\n')

            has_multiple_data = has_bad_pattern = False

            for warn in warns:

                if len(warn) == 0:
                    continue

                zero = warn.startswith('[Zero value error]')
                nega = warn.startswith('[Negative value error]')
                rang = warn.startswith('[Range value error]')
                enum = warn.startswith('[Enumeration error]')
                mult = warn.startswith('[Multiple data]')
                remo = warn.startswith('[Remove bad pattern]')
                clea = warn.startswith('[Clear bad pattern]')

                if zero or nega or range or enum or mult or remo or clea:

                    p = warn.index(']') + 2
                    warn = warn[p:]

                    if zero or nega or rang:
                        item = 'unusual_data'
                    elif enum:
                        item = 'enum_mismatch'
                    elif remo:
                        if content_subtype == 'chem_shift':
                            warn += ' Your unassigned chemical shifts have been removed.'
                            item = 'incompletely_assigned_chemical_shift'
                        else:
                            item = 'insufficient_data'
                        has_bad_pattern = True
                    elif clea:
                        if content_subtype == 'chem_shift':
                            warn += ' Partially assigned chemical shifts should be resolved or removed.'
                            item = 'incompletely_assigned_chemical_shift'
                        elif content_subtype.startswith('spectral_peak'):

                            if self._reg.remediation_mode:
                                continue

                            warn += ' Unassigned spectral peaks can be included in your peak list(s).'
                            item = 'incompletely_assigned_spectral_peak'
                        else:
                            item = 'insufficient_data'
                    elif self._reg.resolve_conflict:
                        # item = 'redundant_data'
                        has_multiple_data = True
                        continue
                    else:
                        item = 'multiple_data'

                    if zero or nega or rang or enum or remo or clea or self._reg.resolve_conflict:

                        self._reg.report.warning.appendDescription(item,
                                                                   {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                    'category': lp_category, 'description': warn})

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInLoop() ++ Warning  - {warn}\n")

                    else:

                        self._reg.report.error.appendDescription(item,
                                                                 {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                  'category': lp_category, 'description': warn})

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInLoop() ++ KeyError  - {warn}\n")

                else:

                    self._reg.report.error.appendDescription('internal_error',
                                                             f"+{self.__class_name__}.testDataConsistencyInLoop() "
                                                             "++ Error  - " + warn)

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInLoop() ++ Error  - {warn}\n")

            # try to parse data without constraints
            if has_multiple_data:
                conflict_id = self._reg.nefT.get_conflict_id(sf, lp_category, key_items)[0]

                if len(conflict_id) > 0:
                    loop = sf if self._reg.star_data_type[file_list_id] == 'Loop' else sf.get_loop(lp_category)

                    for lcid in conflict_id:
                        del loop.data[lcid]

                    index_tag = INDEX_TAGS[file_type][content_subtype]
                    if index_tag is not None:
                        index_col = loop.tags.index(index_tag) if index_tag in loop.tags else -1
                        if index_col != -1:
                            for idx, row in enumerate(loop, start=1):
                                row[index_col] = idx

                    modified = True

            # try to parse data without bad patterns
            if has_bad_pattern:
                conflict_id = self._reg.nefT.get_bad_pattern_id(sf, lp_category, key_items, data_items)[0]

                if len(conflict_id) > 0:
                    loop = sf if self._reg.star_data_type[file_list_id] == 'Loop' else sf.get_loop(lp_category)

                    for lcid in conflict_id:
                        del loop.data[lcid]

                    modified = True

            # collect unresolved redundant data
            if has_multiple_data:

                try:

                    lp_data = self._reg.nefT.check_data(sf, lp_category, key_items, data_items,
                                                        allowed_tags, disallowed_tags, parent_pointer=parent_pointer,
                                                        test_on_index=True,  # important
                                                        enforce_allowed_tags=(file_type == 'nmr-star'
                                                                              and not self._reg.bmrb_only),
                                                        excl_missing_data=self._reg.excl_missing_data)[0]

                except UserWarning as e2:

                    warns = str(e2).strip("'").split('\n')

                    for warn in warns:

                        if len(warn) == 0 or not warn.startswith('[Multiple data]'):
                            continue

                        p = warn.index(']') + 2
                        warn = warn[p:]

                        self._reg.report.warning.appendDescription('redundant_data',
                                                                   {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                    'category': lp_category, 'description': warn})

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInLoop() ++ Warning  - {warn}\n")

                except Exception:  # pylint: disable=broad-exception-caught
                    pass

            try:

                lp_data = self._reg.nefT.check_data(sf, lp_category, key_items, data_items,
                                                    allowed_tags, disallowed_tags, parent_pointer=parent_pointer,
                                                    enforce_allowed_tags=(file_type == 'nmr-star' and not self._reg.bmrb_only),
                                                    excl_missing_data=self._reg.excl_missing_data)[0]

                self._reg.lp_data[content_subtype].append({'file_name': file_name, 'sf_framecode': sf_framecode,
                                                           'category': lp_category, 'data': lp_data})

            except Exception:  # pylint: disable=broad-exception-caught
                pass

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.testDataConsistencyInLoop() ++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInLoop() ++ Error  - {str(e)}\n")

        return modified

    def detectConflictDataInLoop(self, file_name: str, file_type: str, content_subtype: str,
                                 sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                                 sf_framecode: str, lp_category: str) -> None:
        """ Detect redundant/inconsistent data of interesting loops.
        """

        lp_data = next((lp['data'] for lp in self._reg.lp_data[content_subtype]
                        if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode), None)

        if lp_data is None or len(lp_data) == 0:
            return

        key_items = self._reg.consist_key_items[file_type][content_subtype]

        if file_type == 'nmr-star' and content_subtype == 'ccr_dd_restraint':
            loop = sf.get_loop(lp_category)
            if 'Dipole_2_chem_comp_index_ID_2' in loop.tags:
                key_items = copy.copy(key_items)
                key_item = next((key_item for key_item in key_items if key_item['name'] == 'Dipole_2_comp_index_ID_2'), None)
                if key_item is not None:
                    key_item['name'] = 'Dipole_2_chem_comp_index_ID_2'

        conflict_id_set = self._reg.nefT.get_conflict_id_set(sf, lp_category, key_items)[0]

        if conflict_id_set is None:
            return

        data_items = CONSIST_DATA_ITEMS[file_type][content_subtype]
        index_tag = INDEX_TAGS[file_type][content_subtype]
        id_tag = CONSIST_ID_TAGS[file_type][content_subtype]

        data_unit_name = 'atom pair'

        if content_subtype == 'dist_restraint':
            max_inclusive = DIST_UNCERT_MAX

        elif content_subtype == 'dihed_restraint':
            max_inclusive = ANGLE_UNCERT_MAX

            data_unit_name = 'dihedral angle'

            dh_item_names = ITEM_NAMES_IN_DIHED_LOOP[file_type]
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
            lower_limit_name = dh_item_names['lower_limit']
            upper_limit_name = dh_item_names['upper_limit']

            def ext_atoms(row):
                return ({'chain_id': row[chain_id_1_name], 'seq_id': row[seq_id_1_name],
                         'comp_id': row[comp_id_1_name], 'atom_id': row[atom_id_1_name]},
                        {'chain_id': row[chain_id_2_name], 'seq_id': row[seq_id_2_name],
                         'comp_id': row[comp_id_2_name], 'atom_id': row[atom_id_2_name]},
                        {'chain_id': row[chain_id_3_name], 'seq_id': row[seq_id_3_name],
                         'comp_id': row[comp_id_3_name], 'atom_id': row[atom_id_3_name]},
                        {'chain_id': row[chain_id_4_name], 'seq_id': row[seq_id_4_name],
                         'comp_id': row[comp_id_4_name], 'atom_id': row[atom_id_4_name]})

        elif content_subtype == 'rdc_restraint':
            max_inclusive = RDC_UNCERT_MAX

            data_unit_name = 'bond vector'

        for id_set in conflict_id_set:
            len_id_set = len(id_set)

            if len_id_set < 2:
                continue

            redundant = True

            for i in range(len_id_set - 1):

                for j in range(i + 1, len_id_set):

                    try:
                        row_1 = lp_data[id_set[i]]
                        row_2 = lp_data[id_set[j]]
                    except IndexError:
                        continue

                    conflict = inconsist = False

                    discrepancy = ''

                    for d in data_items:
                        dname = d['name']

                        if dname not in row_1:
                            continue

                        val_1 = row_1[dname]
                        val_2 = row_2[dname]

                        if val_1 is None and val_2 is None:
                            continue

                        if None in (val_1, val_2):
                            redundant = False
                            continue

                        if val_1 == val_2:
                            continue

                        redundant = False

                        _val_1 = str(val_1) if val_1 >= 0.0 else f'({val_1})'
                        _val_2 = str(val_2) if val_2 >= 0.0 else f'({val_2})'

                        if content_subtype == 'dist_restraint':

                            r = abs(val_1 - val_2) / abs(val_1 + val_2)

                            if r >= R_CONFLICTED_DIST_RESTRAINT:
                                discrepancy += f"{dname} |{_val_1}-{_val_2}|/|{_val_1}+{_val_2}| = {r:.1%} "\
                                    "is out of acceptable range, "\
                                    f"{int(R_CONFLICTED_DIST_RESTRAINT * 100)} %, "
                                conflict = True

                            elif r >= R_INCONSISTENT_DIST_RESTRAINT:
                                discrepancy += f"{dname} |{_val_1}-{_val_2}|/|{_val_1}+{_val_2}| = {r:.1%} "\
                                    "is out of typical range, "\
                                    f"{int(R_INCONSISTENT_DIST_RESTRAINT * 100)} %, "
                                inconsist = True

                        else:

                            r = abs(val_1 - val_2)

                            if content_subtype == 'dihed_restraint':

                                if r > 180.0:
                                    if val_1 < val_2:
                                        r = abs(val_1 - (val_2 - 360.0))
                                    if val_1 > val_2:
                                        r = abs(val_1 - (val_2 + 360.0))

                                atom1, atom2, atom3, atom4 = ext_atoms(row_1)

                                data_type = row_1[angle_type_name]

                                peptide, nucleotide, carbohydrate = self._reg.csStat.getTypeOfCompId(atom2['comp_id'])
                                plane_like = is_like_planality_boundary(row_1, lower_limit_name, upper_limit_name)

                                data_type = self.getTypeOfDihedralRestraint(data_type, peptide, nucleotide, carbohydrate,
                                                                            [atom1, atom2, atom3, atom4], plane_like)[0]

                                if not data_type.startswith('phi') and not data_type.startswith('psi')\
                                   and not data_type.startswith('omega'):
                                    continue

                            if r > max_inclusive:
                                discrepancy += f"{dname} |{_val_1}-{_val_2}| = {r:.1f} is out of acceptable range, "\
                                               f"{max_inclusive}{'°' if content_subtype == 'dihed_restraint' else 'Hz'}, "
                                conflict = True

                            elif r > max_inclusive * INCONSIST_OVER_CONFLICTED:
                                discrepancy +=\
                                    f"{dname} |{_val_1}-{_val_2}| = {r:.1f} is out of typical range, "\
                                    f"{max_inclusive * INCONSIST_OVER_CONFLICTED}{'°' if content_subtype == 'dihed_restraint' else 'Hz'}, "  # noqa: E501, pylint: disable=line-too-long
                                inconsist = True

                    if conflict:

                        msg = '' if content_subtype != 'dihed_restraint' else angle_type_name + f" {row_1[angle_type_name]}, "
                        msg += self._getReducedAtomNotations(key_items, row_1)

                        if index_tag in row_1:
                            warn = f"[Check rows of {index_tag} {row_1[index_tag]} vs {row_2[index_tag]}, "\
                                f"{id_tag} {row_1[id_tag]} vs {row_2[id_tag]}] "
                        else:
                            warn = f"[Check rows of {index_tag} {id_set[i] + 1} vs {id_set[j] + 1}, "\
                                f"{id_tag} {row_1[id_tag]} vs {row_2[id_tag]}] "
                        warn += f"Found conflict on restraints ({discrepancy[:-2]}) for the same {data_unit_name} ({msg})."

                        self._reg.report.warning.appendDescription('conflicted_data',
                                                                   {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                    'category': lp_category, 'description': warn,
                                                                    'sigma': round(r / max_inclusive, 2)})

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.detetConflictDataInLoop() ++ Warning  - {warn}\n")

                    elif inconsist:

                        msg = '' if content_subtype != 'dihed_restraint' else angle_type_name + f" {row_1[angle_type_name]}, "
                        msg += self._getReducedAtomNotations(key_items, row_1)

                        if index_tag in row_1:
                            warn = f"[Check rows of {index_tag} {row_1[index_tag]} vs {row_2[index_tag]}, "\
                                f"{id_tag} {row_1[id_tag]} vs {row_2[id_tag]}] "
                        else:
                            warn = f"[Check rows of {index_tag} {id_set[i] + 1} vs {id_set[j] + 1}, "\
                                f"{id_tag} {row_1[id_tag]} vs {row_2[id_tag]}] "
                        warn += f"Found discrepancy in restraints ({discrepancy[:-2]}) for the same {data_unit_name} ({msg})."

                        self._reg.report.warning.appendDescription('inconsistent_data',
                                                                   {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                    'category': lp_category, 'description': warn,
                                                                    'sigma': round(r / max_inclusive, 2)})

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.detetConflictDataInLoop() ++ Warning  - {warn}\n")

            if redundant:

                idx_msg = index_tag + ' '
                if index_tag in lp_data[0]:
                    for row_id in id_set:
                        try:
                            idx_msg += f"{lp_data[row_id][index_tag]} vs "
                        except IndexError:
                            continue
                else:
                    for row_id in id_set:
                        idx_msg += f"{row_id + 1} vs "
                idx_msg = idx_msg[:-4] + ', '
                idx_msg += id_tag + ' '
                for row_id in id_set:
                    try:
                        idx_msg += f"{lp_data[row_id][id_tag]} vs "
                    except IndexError:
                        continue

                if not idx_msg.endswith(' vs '):
                    continue

                warn = f"[Check rows of {idx_msg[:-4]}] Found redundant restraints for the same {data_unit_name}."

                self._reg.report.warning.appendDescription('redundant_data',
                                                           {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                            'category': lp_category, 'description': warn})

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.detetConflictDataInLoop() ++ Warning  - {warn}\n")

    def testParentChildRelation(self, file_name: str, file_type: str, content_subtype: str,
                                parent_keys: set, list_id: int, sf_framecode: str,
                                sf_framecode_dict: dict, sf_tag_data: dict) -> bool:
        """ Perform consistency test on saveframe category and loop category relationship of interesting loops.
        """

        if file_type == 'nef' or content_subtype in ('entry_info', 'entity'):
            return True

        __errors = self._reg.report.getTotalErrors()

        key_base = SF_TAG_PREFIXES['nmr-star'][content_subtype].lstrip('_')

        parent_key_name = f'{key_base}.ID'
        child_key_name = f'{key_base}_ID'

        try:

            if parent_key_name in sf_tag_data:
                parent_key = sf_tag_data[parent_key_name]
            else:
                parent_key = list_id

            if parent_key in parent_keys:

                err = f"{parent_key_name} {str(parent_key)!r} must be unique."

                self._reg.report.error.appendDescription('duplicated_index',
                                                         {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                          'description': err})

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.testParentChildRelation() ++ KeyError  - {err}\n")

            index_tag = INDEX_TAGS[file_type][content_subtype]
            lp_category = LP_CATEGORIES[file_type][content_subtype]

            lp_data = next((lp['data'] for lp in self._reg.lp_data[content_subtype]
                            if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode), None)

            if lp_data is not None:

                for row in lp_data:
                    if child_key_name in row and row[child_key_name] != parent_key:

                        if index_tag is None or index_tag not in row:
                            err = f"{child_key_name} {str(row[child_key_name])!r} must be {parent_key}."
                        else:
                            err = f"[Check row of {index_tag} {row[index_tag]}] {child_key_name} {row[child_key_name]!r} "\
                                f"must be {parent_key}."

                        if row[child_key_name] in sf_framecode_dict:
                            err = err[0:-1] + f" to point the parent {sf_framecode!r} saveframe. "\
                                f"The pointer has been reserved for the {sf_framecode_dict[row[child_key_name]]!r} saveframe."

                        self._reg.report.error.appendDescription('invalid_data',
                                                                 {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                  'category': lp_category, 'description': err})

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.testParentChildRelation() ++ ValueError  - {err}\n")

                        break

            if AUX_LP_CATEGORIES[file_type][content_subtype] is not None:

                for lp_category in AUX_LP_CATEGORIES[file_type][content_subtype]:

                    aux_data = next((lp['data'] for lp in self._reg.aux_data[content_subtype]
                                     if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode
                                     and lp['category'] == lp_category), None)

                    if aux_data is None:
                        continue

                    for row in aux_data:
                        if child_key_name in row and row[child_key_name] != parent_key:

                            if index_tag is None or index_tag not in row:
                                err = f"{child_key_name} {str(row[child_key_name])!r} must be {parent_key}."
                            else:
                                err = f"[Check row of {index_tag} {row[index_tag]}] {child_key_name} {row[child_key_name]!r} "\
                                    f"must be {parent_key}."

                            if row[child_key_name] in sf_framecode_dict:
                                err = err[0:-1] + f" to point the parent {sf_framecode!r} saveframe. "\
                                    f"The pointer has been reserved for the {sf_framecode_dict[row[child_key_name]]!r} saveframe."

                            self._reg.report.error.appendDescription('invalid_data',
                                                                     {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                      'category': lp_category, 'description': err})

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.testParentChildRelation() ++ ValueError  - {err}\n")

                            break

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.testParentChildRelation() ++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.testParentChildRelation() ++ Error  - {str(e)}\n")

        return self._reg.report.getTotalErrors() == __errors

    def testDataConsistencyInAuxLoopOfSpectralPeak(self, file_name: str, file_type: str, sf_framecode: str,
                                                   num_dim: int, lp_category: str, aux_data: List[List[dict]]) -> None:
        """ Perform consistency test on data of spectral peak loops.
        """

        content_subtype = 'spectral_peak'

        max_dim = num_dim + 1

        if (file_type == 'nef' and lp_category == '_nef_spectrum_dimension')\
           or (file_type == 'nmr-star' and lp_category == '_Spectral_dim'):

            err = f"The number of dimension {str(num_dim)!r} and the number of rows {str(len(aux_data))!r} are not matched."

            if len(aux_data) != num_dim:
                self._reg.report.error.appendDescription('missing_data',
                                                         {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                          'category': lp_category, 'description': err})

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInAuxLoopOfSpectralPeak() "
                                        f"++ Error  - {err}\n")

            try:

                min_points = [None] * num_dim
                max_points = [None] * num_dim
                min_limits = [None] * num_dim
                max_limits = [None] * num_dim
                abs_positions = [None] * num_dim

                first_point_in_hz = True
                for i in range(1, max_dim):

                    for sp_dim in aux_data:

                        if file_type == 'nef':

                            if sp_dim['dimension_id'] != i:
                                continue

                            first_point = sp_dim.get('value_first_point')
                            sp_width = sp_dim.get('spectral_width')
                            sp_freq = sp_dim.get('spectrometer_frequency')

                            if 'axis_unit' in sp_dim and sp_dim['axis_unit'] == 'Hz'\
                               and None not in (sp_freq, first_point, sp_width):
                                if first_point / sp_freq - sp_width / sp_freq < -1.0:
                                    first_point_in_hz = False
                                    break

                        else:

                            if sp_dim['ID'] != i:
                                continue

                            first_point = sp_dim.get('Value_first_point')
                            sp_width = sp_dim.get('Sweep_width')
                            sp_freq = sp_dim.get('Spectrometer_frequency')

                            if 'Sweep_width_units' in sp_dim and sp_dim['Sweep_width_units'] == 'Hz'\
                               and None not in (sp_freq, first_point, sp_width):
                                if first_point / sp_freq - sp_width / sp_freq < -1.0:
                                    first_point_in_hz = False
                                    break

                for i in range(1, max_dim):

                    for sp_dim in aux_data:

                        if file_type == 'nef':

                            if sp_dim['dimension_id'] != i:
                                continue

                            first_point = sp_dim.get('value_first_point')
                            sp_width = sp_dim.get('spectral_width')
                            sp_freq = sp_dim.get('spectrometer_frequency')
                            abs_positions[i - 1] = False if 'absolute_peak_positions' not in sp_dim\
                                else sp_dim['absolute_peak_positions']

                            if 'axis_unit' in sp_dim and sp_dim['axis_unit'] == 'Hz'\
                               and None not in (sp_freq, first_point, sp_width):
                                if first_point_in_hz:
                                    first_point /= sp_freq
                                sp_width /= sp_freq

                        else:

                            if sp_dim['ID'] != i:
                                continue

                            first_point = sp_dim.get('Value_first_point')
                            sp_width = sp_dim.get('Sweep_width')
                            sp_freq = sp_dim.get('Spectrometer_frequency')
                            abs_positions[i - 1] = False if 'Absolute_peak_positions' not in sp_dim\
                                else sp_dim['Absolute_peak_positions']

                            if 'Sweep_width_units' in sp_dim and sp_dim['Sweep_width_units'] == 'Hz'\
                               and None not in (sp_freq, first_point, sp_width):
                                if first_point_in_hz:
                                    first_point /= sp_freq
                                sp_width /= sp_freq

                        min_point = max_point = min_limit = max_limit = None

                        if None not in (first_point, sp_width):

                            last_point = first_point - sp_width

                            # DAOTHER-7389, issue #1, relax expected range of peak position by three times of spectral width
                            # if absolute_peak_positions are true
                            tolerance = (sp_width * (1.0 if self._reg.bmrb_only else 3.0) if abs_positions[i - 1] else 0.0)
                            min_point = last_point - tolerance
                            max_point = first_point + tolerance

                            min_limit = min_point
                            max_limit = max_point

                            if None not in (sp_freq, min_point, max_point):
                                center_point = (max_point - min_point) / 2.0
                                min_limit = center_point - HARD_PROBE_LIMIT / 2.0 / sp_freq
                                max_limit = center_point + HARD_PROBE_LIMIT / 2.0 / sp_freq

                        if min_point is not None:
                            min_points[i - 1] = round(min_point, 7)
                        if max_point is not None:
                            max_points[i - 1] = round(max_point, 7)

                        if min_limit is not None:
                            min_limits[i - 1] = round(min_limit, 7)
                        if max_limit is not None:
                            max_limits[i - 1] = round(max_limit, 7)

                        break

                key_items = []
                for dim in range(1, max_dim):
                    for k in PK_KEY_ITEMS[file_type]:
                        if k['type'] == 'float':  # position
                            _k = copy.copy(k)
                            if '%s' in k['name']:
                                _k['name'] = k['name'] % dim
                            key_items.append(_k)

                position_names = [k['name'] for k in key_items]
                id_tag = CONSIST_ID_TAGS[file_type][content_subtype]

                lp_data = next((lp['data'] for lp in self._reg.lp_data[content_subtype]
                                if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode), None)

                if lp_data is not None:

                    for row in lp_data:
                        for j in range(num_dim):

                            if None in (min_points[j], max_points[j]):
                                continue

                            position = row[position_names[j]]

                            if position < min_points[j] or position > max_points[j]:

                                err = f"[Check row of {id_tag} {row[id_tag]}] {position_names[j]} {position} "\
                                    "is not within expected range "\
                                    f"(min_position {min_points[j]}, max_position {max_points[j]}, "\
                                    f"absolute_peak_positions {abs_positions[j]}). "\
                                    "Please check for reference frequency and spectral width."

                                self._reg.report.warning.appendDescription('anomalous_data',
                                                                           {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                            'category': lp_category, 'description': err})

                                if self._reg.verbose:
                                    self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInAuxLoopOfSpectralPeak() "
                                                        f"++ Warning  - {err}\n")

                            if None in (min_limits[j], max_limits[j]):
                                continue

                            if position < min_limits[j] or position > max_limits[j]:

                                err = f"[Check row of {id_tag} {row[id_tag]}] {position_names[j]} {position} "\
                                    "is not within expected range "\
                                    f"(min_position {min_limits[j]}, max_position {max_limits[j]}, "\
                                    f"absolute_peak_positions {abs_positions[j]}), "\
                                    f"which exceeds limit of current probe design ({HARD_PROBE_LIMIT / 1000.0} kHz). "\
                                    "Please check for reference frequency and spectral width."

                                self._reg.report.error.appendDescription('invalid_data',
                                                                         {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                          'category': lp_category, 'description': err})

                                if self._reg.verbose:
                                    self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInAuxLoopOfSpectralPeak() "
                                                        f"++ ValueError  - {err}\n")

            except Exception as e:  # pylint: disable=broad-exception-caught

                self._reg.report.error.appendDescription('internal_error',
                                                         f"+{self.__class_name__}.testDataConsistencyInAuxLoopOfSpectralPeak() "
                                                         "++ Error  - " + str(e))

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInAuxLoopOfSpectralPeak() "
                                        f"++ Error  - {str(e)}\n")

        if (file_type == 'nef' and lp_category == '_nef_spectrum_dimension_transfer')\
           or (file_type == 'nmr-star' and lp_category == '_Spectral_dim_transfer'):

            for row in aux_data:
                for name in [key['name'] for key in self._reg.aux_key_items[file_type][content_subtype][lp_category]]:
                    if row[name] not in range(1, max_dim):

                        err = f"{name} {row[name]!r} must be one of {range(1, max_dim)}."

                        self._reg.report.error.appendDescription('invalid_data',
                                                                 {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                  'category': lp_category, 'description': err})

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInAuxLoopOfSpectralPeak() "
                                                f"++ ValueError  - {err}\n")

    def testDataConsistencyInAuxLoopOfSpectralPeakAlt(self, file_name: str, file_type: str, sf_framecode: str,
                                                      num_dim: int, lp_category: str, aux_data: List[List[dict]],
                                                      sf: pynmrstar.Saveframe,
                                                      parent_pointer: int) -> None:
        """ Perform consistency test on data of spectral peak loops.
        """

        content_subtype = 'spectral_peak_alt'

        max_dim = num_dim + 1

        if lp_category == '_Spectral_dim':

            err = f"The number of dimension {str(num_dim)!r} and the number of rows {str(len(aux_data))!r} are not matched."

            if len(aux_data) != num_dim:
                self._reg.report.error.appendDescription('missing_data',
                                                         {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                          'category': lp_category, 'description': err})

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInAuxLoopOfSpectralPeakAlt() "
                                        f"++ Error  - {err}\n")

            try:

                min_points = [None] * num_dim
                max_points = [None] * num_dim
                min_limits = [None] * num_dim
                max_limits = [None] * num_dim
                abs_positions = [None] * num_dim

                first_point_in_hz = True
                for i in range(1, max_dim):

                    for sp_dim in aux_data:

                        if sp_dim['ID'] != i:
                            continue

                        first_point = sp_dim.get('Value_first_point')
                        sp_width = sp_dim.get('Sweep_width')
                        sp_freq = sp_dim.get('Spectrometer_frequency')

                        if 'Sweep_width_units' in sp_dim and sp_dim['Sweep_width_units'] == 'Hz'\
                           and None not in (sp_freq, first_point, sp_width):
                            if first_point / sp_freq - sp_width / sp_freq < -1.0:
                                first_point_in_hz = False
                                break

                for i in range(1, max_dim):

                    for sp_dim in aux_data:

                        if sp_dim['ID'] != i:
                            continue

                        first_point = sp_dim.get('Value_first_point')
                        sp_width = sp_dim.get('Sweep_width')
                        sp_freq = sp_dim.get('Spectrometer_frequency')
                        abs_positions[i - 1] = False if 'Absolute_peak_positions' not in sp_dim\
                            else sp_dim['Absolute_peak_positions']

                        if 'Sweep_width_units' in sp_dim and sp_dim['Sweep_width_units'] == 'Hz'\
                           and None not in (sp_freq, first_point, sp_width):
                            if first_point_in_hz:
                                first_point /= sp_freq
                            sp_width /= sp_freq

                        min_point = max_point = min_limit = max_limit = None

                        if None not in (first_point, sp_width):

                            last_point = first_point - sp_width

                            # DAOTHER-7389, issue #1, relax expected range of peak position by three times of spectral width
                            # if absolute_peak_positions are true
                            torelance = (sp_width * (1.0 if self._reg.bmrb_only else 3.0) if abs_positions[i - 1] else 0.0)
                            min_point = last_point - torelance
                            max_point = first_point + torelance

                            min_limit = min_point
                            max_limit = max_point

                            if None not in (sp_freq, min_point, max_point):
                                center_point = (max_point - min_point) / 2.0
                                min_limit = center_point - HARD_PROBE_LIMIT / 2.0 / sp_freq
                                max_limit = center_point + HARD_PROBE_LIMIT / 2.0 / sp_freq

                        if min_point is not None:
                            min_points[i - 1] = round(min_point, 7)
                        if max_point is not None:
                            max_points[i - 1] = round(max_point, 7)

                        if min_limit is not None:
                            min_limits[i - 1] = round(min_limit, 7)
                        if max_limit is not None:
                            max_limits[i - 1] = round(max_limit, 7)

                        break

                _pk_char_category = '_Peak_char'

                _pk_char_data = next((lp['data'] for lp in self._reg.aux_data[content_subtype]
                                      if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode
                                      and lp['category'] == _pk_char_category), None)

                if _pk_char_data is None and any(True for loop in sf.loops if loop.category == _pk_char_category):

                    key_items = self._reg.aux_key_items[file_type][content_subtype][_pk_char_category]
                    data_items = self._reg.aux_data_items[file_type][content_subtype][_pk_char_category]
                    allowed_tags = AUX_ALLOWED_TAGS[file_type][content_subtype][_pk_char_category]

                    _pk_char_data = self._reg.nefT.check_data(sf, _pk_char_category, key_items, data_items,
                                                              allowed_tags, None, parent_pointer=parent_pointer,
                                                              enforce_allowed_tags=(file_type == 'nmr-star'),
                                                              excl_missing_data=self._reg.excl_missing_data)[0]

                pk_id_name = 'Peak_ID'
                dim_id_name = 'Spectral_dim_ID'
                position_name = 'Chem_shift_val'

                if _pk_char_data is not None:

                    for row in _pk_char_data:

                        j = row[dim_id_name] - 1

                        if j >= num_dim or None in (min_points[j], max_points[j]):
                            continue

                        position = row[position_name]

                        if position < min_points[j] or position > max_points[j]:

                            warn = f"[Check row of {pk_id_name} {row[pk_id_name]}] {position_name} {position} "\
                                "is not within expected range "\
                                f"(min_position {min_points[j]}, max_position {max_points[j]}, "\
                                f"absolute_peak_positions {abs_positions[j]}). "\
                                "Please check for reference frequency and spectral width."

                            self._reg.report.warning.appendDescription('anomalous_data',
                                                                       {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                        'category': lp_category, 'description': warn})

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInAuxLoopOfSpectralPeakAlt() "
                                                    f"++ Warning  - {warn}\n")

                        if None in (min_limits[j], max_limits[j]):
                            continue

                        if position < min_limits[j] or position > max_limits[j]:

                            err = f"[Check row of {pk_id_name} {row[pk_id_name]}] {position_name} {position} "\
                                "is not within expected range "\
                                f"(min_position {min_limits[j]}, max_position {max_limits[j]}, "\
                                f"absolute_peak_positions {abs_positions[j]}), "\
                                f"which exceeds limit of current probe design ({HARD_PROBE_LIMIT / 1000.0} kHz). "\
                                "Please check for reference frequency and spectral width."

                            self._reg.report.error.appendDescription('invalid_data',
                                                                     {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                      'category': lp_category, 'description': err})

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInAuxLoopOfSpectralPeakAlt() "
                                                    f"++ ValueError  - {err}\n")

            except LookupError as e:

                item = 'format_issue' if 'Unauthorized' in str(e) else 'missing_mandatory_item'

                self._reg.report.error.appendDescription(item,
                                                         {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                          'category': lp_category, 'description': str(e).strip("'")})

                self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInAuxLoopOfSpectralPeakAlt() "
                                    f"++ LookupError  - {file_name} {sf_framecode} {lp_category} {str(e)}\n")

            except ValueError as e:

                self._reg.report.error.appendDescription('invalid_data',
                                                         {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                          'category': lp_category, 'description': str(e).strip("'")})

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInAuxLoopOfSpectralPeakAlt() "
                                        f"++ ValueError  - {str(e)}\n")

            except Exception as e:  # pylint: disable=broad-exception-caught

                self._reg.report.error.appendDescription('internal_error',
                                                         f"+{self.__class_name__}.testDataConsistencyInAuxLoopOfSpectralPeakAlt() "
                                                         "++ Error  - " + str(e))

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInAuxLoopOfSpectralPeakAlt() "
                                        f"++ Error  - {str(e)}\n")

        if lp_category == '_Spectral_dim_transfer':

            for row in aux_data:
                for name in [key['name'] for key in self._reg.aux_key_items[file_type][content_subtype][lp_category]]:
                    if row[name] not in range(1, max_dim):

                        err = f"{name} {row[name]!r} must be one of {range(1, max_dim)}."

                        self._reg.report.error.appendDescription('invalid_data',
                                                                 {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                  'category': lp_category, 'description': err})

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.testDataConsistencyInAuxLoopOfSpectralPeakAlt() "
                                                f"++ ValueError  - {err}\n")
