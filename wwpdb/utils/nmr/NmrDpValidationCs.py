##
# File: NmrDpValidationCs.py
# Date: 17-Aug-2026
#
# Updates:
##
""" Chemical shift value validation for NMR data validation.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.3"

import math
from operator import itemgetter
from typing import Optional, Union

import numpy

import pynmrstar

try:
    from wwpdb.utils.nmr.NmrDpConstant import (CUTOFF_AROMATIC,
                                               CUTOFF_PARAMAGNETIC,
                                               VICINITY_AROMATIC,
                                               VICINITY_PARAMAGNETIC,
                                               MAGIC_ANGLE,
                                               DATA_ITEMS,
                                               ITEM_NAMES_IN_CS_LOOP,
                                               EMPTY_VALUE,
                                               STD_MON_DICT,
                                               PROTON_BEGIN_CODE,
                                               PARAMAGNETIC_ELEMENTS,
                                               FERROMAGNETIC_ELEMENTS,
                                               ALLOWED_AMBIGUITY_CODES,
                                               CS_UNCERT_MAX,
                                               REPRESENTATIVE_ASYM_ID)
    from wwpdb.utils.nmr.AlignUtil import letterToDigit
    from wwpdb.utils.nmr.CifToNmrStar import has_key_value
    from wwpdb.utils.nmr.NmrVrptUtility import (to_np_array,
                                                distance,
                                                to_unit_vector)
    from wwpdb.utils.nmr.NmrDpValidationBase import NmrDpValidationBase
except ImportError:
    from nmr.NmrDpConstant import (CUTOFF_AROMATIC,
                                   CUTOFF_PARAMAGNETIC,
                                   VICINITY_AROMATIC,
                                   VICINITY_PARAMAGNETIC,
                                   MAGIC_ANGLE,
                                   DATA_ITEMS,
                                   ITEM_NAMES_IN_CS_LOOP,
                                   EMPTY_VALUE,
                                   STD_MON_DICT,
                                   PROTON_BEGIN_CODE,
                                   PARAMAGNETIC_ELEMENTS,
                                   FERROMAGNETIC_ELEMENTS,
                                   ALLOWED_AMBIGUITY_CODES,
                                   CS_UNCERT_MAX,
                                   REPRESENTATIVE_ASYM_ID)
    from nmr.AlignUtil import letterToDigit
    from nmr.CifToNmrStar import has_key_value
    from nmr.NmrVrptUtility import (to_np_array,
                                    distance,
                                    to_unit_vector)
    from nmr.NmrDpValidationBase import NmrDpValidationBase


class NmrDpValidationCs(NmrDpValidationBase):
    """ Chemical shift value validation for NMR data validation.
    """
    __slots__ = ()

    def validateCsValue(self, file_list_id: int, file_name: str, file_type: str, content_subtype: str,
                        sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                        sf_framecode: str, lp_category: str) -> bool:
        """ Validate assigned chemical shift value based on BMRB chemical shift statistics.
        """

        no_reason_message = " Neither aromatic ring nor paramagnetic/ferromagnetic atom was found in the vicinity."
        fold_warn_message = " Please check for folded/aliased signals."

        item_names = ITEM_NAMES_IN_CS_LOOP[file_type]
        chain_id_name = item_names['chain_id']
        seq_id_name = item_names['seq_id']
        comp_id_name = item_names['comp_id']
        atom_id_name = item_names['atom_id']
        value_name = item_names['value']
        ambig_code_name = 'Ambiguity_code'  # NMR-STAR specific
        occupancy_name = 'Occupancy'  # NMR-STAR specific

        full_value_name = f'{lp_category}.{value_name}'

        max_inclusive = 0.01

        modified = False

        has_mr_atom_name_mapping = file_type == 'nmr-star' and self._reg.remediation_mode\
            and self._reg.mr_atom_name_mapping is not None and len(self._reg.mr_atom_name_mapping) > 0

        try:

            details_col = -1

            if file_type == 'nmr-star':

                loop = sf if self._reg.star_data_type[file_list_id] == 'Loop' else sf.get_loop(lp_category)

                if has_mr_atom_name_mapping:
                    auth_seq_id_col = loop.tags.index('Auth_seq_ID') if 'Auth_seq_ID' in loop.tags else -1
                    auth_comp_id_col = loop.tags.index('Auth_comp_ID') if 'Auth_comp_ID' in loop.tags else -1
                    auth_atom_id_col = loop.tags.index('Auth_atom_ID') if 'Auth_atom_ID' in loop.tags else -1
                    orig_atom_name_col = loop.tags.index('Original_PDB_atom_name') if 'Original_PDB_atom_name' in loop.tags else -1
                    if -1 in (auth_seq_id_col, auth_comp_id_col, auth_atom_id_col, orig_atom_name_col):
                        has_mr_atom_name_mapping = False

                if 'Details' in loop.tags:
                    details_col = loop.tags.index('Details')

                if ambig_code_name in loop.tags:
                    ambig_code_col = loop.tags.index(ambig_code_name)
                    ambig_code_dat = loop.get_tag(ambig_code_name)
                    if len(ambig_code_dat) > 0:
                        ambig_code_set = set()
                        invalid_ambig_code_set = set()
                        for row in ambig_code_dat:
                            if row not in EMPTY_VALUE:
                                if row.isdigit() and int(row) in ALLOWED_AMBIGUITY_CODES:
                                    ambig_code_set.add(int(row))
                                else:
                                    invalid_ambig_code_set.add(row)
                        if len(invalid_ambig_code_set) > 0:
                            if seq_id_name in loop.tags and comp_id_name in loop.tags:
                                seq_key_set = set()
                                seq_key_dat = loop.get_tag([seq_id_name, comp_id_name])
                                for row in seq_key_dat:
                                    seq_key = (row[0], row[1])
                                    seq_key_set.add(seq_key)
                                if len(invalid_ambig_code_set) > len(seq_key_set) * 2:
                                    for row in loop:
                                        row[ambig_code_col] = '.'
                                else:
                                    for row in loop:
                                        if row[ambig_code_col] in invalid_ambig_code_set:
                                            row[ambig_code_col] = '.'
                        if len(ambig_code_set) == 1:
                            if 1 not in ambig_code_set:  # 2lrk
                                comp_id_col = loop.tags.index(comp_id_name)
                                atom_id_col = loop.tags.index(atom_id_name)
                                for row in loop:
                                    comp_id = row[comp_id_col]
                                    _atom_id = atom_id = row[atom_id_col]
                                    if self.isNmrAtomName(comp_id, atom_id):
                                        _atom_id = self.getRepAtomId(comp_id, atom_id)
                                    allowed_ambig_code = self._reg.csStat.getMaxAmbigCodeWoSetId(comp_id, _atom_id)
                                    if allowed_ambig_code in (0, 1):
                                        row[ambig_code_col] = '1'

            if (file_type == 'nef' or not self._reg.nonblk_anomalous_cs) and len(self._reg.lp_data[content_subtype]) > 0:
                lp_data = next(lp['data'] for lp in self._reg.lp_data[content_subtype]
                               if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode)

            else:

                key_items = self._reg.key_items[file_type][content_subtype]
                data_items = DATA_ITEMS[file_type][content_subtype]

                try:

                    lp_data = self._reg.nefT.check_data(sf, lp_category, key_items, data_items, None, None, None,
                                                        enforce_allowed_tags=(file_type == 'nmr-star'),
                                                        excl_missing_data=self._reg.excl_missing_data)[0]

                except Exception:  # pylint: disable=broad-exception-caught

                    err = f"Assigned chemical shifts of {sf_framecode!r} saveframe was not parsed properly. "\
                        "Please fix problems reported."

                    self._reg.report.error.appendDescription('missing_mandatory_content',
                                                             {'file_name': file_name, 'description': err})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                            f"++ Error  - {err}\n")

                    return False

            chk_row_tmp = f"[Check row of {chain_id_name} %s, {seq_id_name} %s, {comp_id_name} %s, {atom_id_name} %s"
            row_tmp = f"{chain_id_name} %s, {seq_id_name} %s, {comp_id_name} %s, {atom_id_name} %s"

            methyl_cs_vals = {}
            failed_methyl_cs_keys = []

            for idx, row in enumerate(lp_data):
                chain_id = row[chain_id_name]
                seq_id = row[seq_id_name]
                comp_id = row[comp_id_name]
                atom_id = row[atom_id_name]
                value = row[value_name]
                occupancy = '.' if file_type == 'nef' else row[occupancy_name]

                alt_chain_id = set(EMPTY_VALUE)
                alt_chain_id.add(chain_id)
                if chain_id.isalpha():
                    alt_chain_id.add(str(letterToDigit(chain_id)))

                if value in EMPTY_VALUE:
                    continue

                if file_type == 'nef' or self.isNmrAtomName(comp_id, atom_id):
                    _atom_id, ambig_code, details = self._getAtomIdListWithAmbigCode(comp_id, atom_id)

                    len_atom_id = len(_atom_id)

                    if len_atom_id == 0:
                        continue

                    if len_atom_id == 1 and atom_id == _atom_id[0]:
                        atom_id_ = atom_id
                        atom_name = atom_id

                        if details is not None:
                            atom_name += f", where {details.rstrip('.')}"

                    else:
                        atom_name = f'{atom_id} (e.g. '

                        for atom_id_ in _atom_id:
                            atom_name += f'{atom_id_} '

                        atom_name = f'{atom_name.rstrip()})'

                        # representative atom id
                        atom_id_ = _atom_id[0]

                else:
                    atom_id_ = atom_id
                    atom_name = atom_id

                has_cs_stat = False

                # non-standard residue
                if comp_id not in STD_MON_DICT:

                    if has_mr_atom_name_mapping and atom_id_[0] == 'H':
                        try:
                            _row_ = loop.data[idx]
                            auth_seq_id, auth_comp_id, auth_atom_id, orig_atom_name =\
                                int(_row_[auth_seq_id_col]), _row_[auth_comp_id_col], \
                                _row_[auth_atom_id_col], _row_[orig_atom_name_col].upper()
                            if auth_comp_id not in EMPTY_VALUE and auth_atom_id not in EMPTY_VALUE\
                               and orig_atom_name not in EMPTY_VALUE and auth_atom_id != orig_atom_name:
                                try:
                                    atom_map =\
                                        next(atom_map for atom_map in self._reg.mr_atom_name_mapping
                                             if atom_map['auth_seq_id'] == auth_seq_id
                                             and atom_map['auth_comp_id'] == auth_comp_id
                                             and atom_map['auth_atom_id'] == auth_atom_id
                                             and atom_map['original_atom_id'] == auth_atom_id)
                                    atom_map['original_atom_id'] = orig_atom_name
                                except StopIteration:
                                    pass
                        except (ValueError, TypeError):
                            pass

                    neighbor_comp_ids =\
                        set(_row[comp_id_name] for _row in lp_data
                            if _row[chain_id_name] == chain_id and abs(_row[seq_id_name] - seq_id) < 4
                            and _row[seq_id_name] != seq_id)

                    polypeptide_like = False

                    for comp_id2 in neighbor_comp_ids:
                        polypeptide_like |= self._reg.csStat.peptideLike(comp_id2)

                    cs_stats = self._reg.csStat.get(comp_id)
                    if len(cs_stats) == 0:
                        if self._reg.ccU.updateChemCompDict(comp_id):
                            parent_comp_id = self._reg.ccU.lastChemCompDict['parent_comp_id']
                            # DAOTHER-9198: retrieve BMRB chemical shift statistics from parent comp_id if possible (i.e. DNR -> DC)
                            if parent_comp_id in STD_MON_DICT:
                                cs_stats = self._reg.csStat.get(parent_comp_id)

                    cs_stat = next((cs_stat for cs_stat in cs_stats
                                    if cs_stat['atom_id'] == atom_id_ and cs_stat['count'] > 0), None)

                    if cs_stat is not None:
                        min_value = cs_stat['min']
                        max_value = cs_stat['max']
                        avg_value = cs_stat['avg']
                        std_value = cs_stat['std']

                        has_cs_stat = True

                        if atom_id_[0] in PROTON_BEGIN_CODE and 'methyl' in cs_stat['desc']:
                            methyl_h_list = self._reg.csStat.getProtonsInSameGroup(comp_id, atom_id)
                            _atom_id = methyl_h_list[0] if len(methyl_h_list) > 0 else atom_id
                            methyl_cs_key = (chain_id, seq_id, _atom_id, occupancy)

                            if methyl_cs_key not in methyl_cs_vals:
                                methyl_cs_vals[methyl_cs_key] = value

                            elif value != methyl_cs_vals[methyl_cs_key] and methyl_cs_key not in failed_methyl_cs_keys:
                                failed_methyl_cs_keys.append(methyl_cs_key)

                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                    + "] Chemical shift values in the same methyl group "\
                                    f"({full_value_name} {value} vs {methyl_cs_vals[methyl_cs_key]}) are inconsistent."

                                if self._reg.combined_mode and not self._reg.remediation_mode:

                                    self._reg.report.error.appendDescription('invalid_data',
                                                                             {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                              'category': lp_category, 'description': err})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                            f"++ ValueError  - {err}\n")

                                else:

                                    _sigma = round(abs(value - methyl_cs_vals[methyl_cs_key]) / max_inclusive, 2)

                                    self._reg.report.warning.appendDescription('conflicted_data',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': err,
                                                                                'sigma': _sigma})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                            f"++ Warning  - {err}\n")

                        if std_value is None or std_value <= 0.0:

                            warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                + f"] Insufficient chemical shift statistics on comp_id {comp_id}, atom_id {atom_name} "\
                                f"is available to verify {full_value_name} {value} (avg {avg_value})."

                            self._reg.report.warning.appendDescription('unusual_data',
                                                                       {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                        'category': lp_category, 'description': warn})

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                    f"++ Warning  - {warn}\n")

                            continue

                        if avg_value is None:

                            warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                + f"] Insufficient chemical shift statistics on comp_id {comp_id}, atom_id {atom_name} "\
                                f"is available to verify {full_value_name} {value}."

                            self._reg.report.warning.appendDescription('unusual_data',
                                                                       {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                        'category': lp_category, 'description': warn})

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                    f"++ Warning  - {warn}\n")

                            continue

                        z_score = round((value - avg_value) / std_value, 2)
                        sigma = abs(z_score)

                        if self._reg.csStat.hasSufficientStat(comp_id, polypeptide_like):
                            tolerance = std_value

                            if (value < min_value - tolerance or value > max_value + tolerance)\
                               and sigma > self._reg.cs_anomalous_error_scaled_by_sigma\
                               and std_value > max_inclusive:

                                na = self._getNearestAromaticRing(chain_id, seq_id, atom_id_)
                                pa = self._getNearestParaFerroMagneticAtom(chain_id, seq_id, atom_id_)

                                if na is None and pa is None:

                                    err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                        + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                        "is not within expected range "\
                                        f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                        f"Z_score {z_score:.2f})."

                                    err_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} "\
                                        f"({value} ppm, {sigma:.2f} sigma), "\
                                        "which is outside of expected range "\
                                        f"({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                        f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value})."

                                    if self._reg.cifChecked:
                                        err += no_reason_message
                                        err_alt += no_reason_message

                                    err += fold_warn_message
                                    err_alt += fold_warn_message

                                    if self._reg.nonblk_anomalous_cs or self._reg.remediation_mode:

                                        self._reg.report.warning.appendDescription('anomalous_data',
                                                                                   {'file_name': file_name,
                                                                                    'sf_framecode': sf_framecode,
                                                                                    'category': lp_category, 'description': err,
                                                                                    'value': value, 'z_score': z_score,
                                                                                    'description_alt': err_alt, 'sigma': sigma})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                                f"++ Warning  - {err}\n")

                                        if self._reg.bmrb_only and self._reg.leave_intl_note\
                                           and file_type == 'nmr-star' and details_col != -1:
                                            _details = loop.data[idx][details_col]
                                            details = f"{full_value_name} {value} is not within expected range "\
                                                f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                                f"Z_score {z_score:.2f})."\
                                                f"{no_reason_message if self._reg.cifChecked else ''}"\
                                                f"{fold_warn_message}\n"
                                            if _details in EMPTY_VALUE or (details not in _details):
                                                if _details in EMPTY_VALUE:
                                                    loop.data[idx][details_col] = details
                                                else:
                                                    loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                                modified = True

                                    else:

                                        self._reg.report.error.appendDescription('anomalous_data',
                                                                                 {'file_name': file_name,
                                                                                  'sf_framecode': sf_framecode,
                                                                                  'category': lp_category, 'description': err,
                                                                                  'value': value, 'z_score': z_score,
                                                                                  'description_alt': err_alt, 'sigma': sigma})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                                f"++ ValueError  - {err}\n")

                                elif pa is None:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                        + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                        "should be verified "\
                                        f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                        f"Z_score {z_score:.2f}). "\
                                        "The nearest aromatic ring "\
                                        f"({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                        f"is located at a distance of {na['ring_distance']}Å, "\
                                        f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                    warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} "\
                                        f"({value} ppm, {sigma:.2f} sigma), "\
                                        "which is outside of expected range "\
                                        f"({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                        f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                        "The nearest aromatic ring "\
                                        f"({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                        f"is located at a distance of {na['ring_distance']}Å, "\
                                        f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                    if (na['ring_angle'] - MAGIC_ANGLE) * z_score > 0.0\
                                       or self._reg.nonblk_anomalous_cs or self._reg.remediation_mode:

                                        self._reg.report.warning.appendDescription('anomalous_data'
                                                                                   if (na['ring_angle'] - MAGIC_ANGLE) * z_score < 0.0  # noqa: E501, pylint: disable=line-too-long
                                                                                   or na['ring_distance'] > VICINITY_AROMATIC
                                                                                   else 'unusual_data',
                                                                                   {'file_name': file_name,
                                                                                    'sf_framecode': sf_framecode,
                                                                                    'category': lp_category, 'description': warn,
                                                                                    'value': value, 'z_score': z_score,
                                                                                    'description_alt': warn_alt, 'sigma': sigma})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                                f"++ Warning  - {warn}\n")

                                        if self._reg.bmrb_only and self._reg.leave_intl_note\
                                           and file_type == 'nmr-star' and details_col != -1\
                                           and ((na['ring_angle'] - MAGIC_ANGLE) * z_score < 0.0
                                                or na['ring_distance'] > VICINITY_AROMATIC):
                                            _details = loop.data[idx][details_col]
                                            details = f"{full_value_name} {value} is not within expected range "\
                                                f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                                f"Z_score {z_score:.2f}). "\
                                                "The nearest aromatic ring "\
                                                f"({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                                f"is located at a distance of {na['ring_distance']}Å, "\
                                                f"and has an elevation angle of {na['ring_angle']}° with the ring plane.\n"
                                            if _details in EMPTY_VALUE or (details not in _details):
                                                if _details in EMPTY_VALUE:
                                                    loop.data[idx][details_col] = details
                                                else:
                                                    loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                                modified = True

                                    else:

                                        self._reg.report.error.appendDescription('anomalous_data',
                                                                                 {'file_name': file_name,
                                                                                  'sf_framecode': sf_framecode,
                                                                                  'category': lp_category, 'description': warn,
                                                                                  'value': value, 'z_score': z_score,
                                                                                  'description_alt': warn_alt, 'sigma': sigma})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                                f"++ ValueError  - {warn}\n")

                                else:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                        + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                        "should be verified "\
                                        f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                        f"Z_score {z_score:.2f}). "\
                                        "The nearest paramagnetic/ferromagnetic atom "\
                                        f"({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                        f"is located at a distance of {pa['distance']}Å."

                                    warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} "\
                                        f"({value} ppm, {sigma:.2f} sigma), "\
                                        "which is outside of expected range "\
                                        f"({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                        f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                        "The nearest paramagnetic/ferromagnetic atom "\
                                        f"({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                        f"is located at a distance of {pa['distance']}Å."

                                    self._reg.report.warning.appendDescription('anomalous_data'
                                                                               if pa['distance'] > VICINITY_PARAMAGNETIC
                                                                               else 'unusual_data',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': warn,
                                                                                'value': value, 'z_score': z_score,
                                                                                'description_alt': warn_alt, 'sigma': sigma})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                            f"++ Warning  - {warn}\n")

                                    if self._reg.bmrb_only and self._reg.leave_intl_note\
                                       and file_type == 'nmr-star' and details_col != -1\
                                       and pa['distance'] > VICINITY_PARAMAGNETIC:
                                        _details = loop.data[idx][details_col]
                                        details = f"{full_value_name} {value} is not within expected range "\
                                            f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                            f"Z_score {z_score:.2f}). "\
                                            "The nearest paramagnetic/ferromagnetic atom "\
                                            f"({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                            f"is located at a distance of {pa['distance']}Å.\n"
                                        if _details in EMPTY_VALUE or (details not in _details):
                                            if _details in EMPTY_VALUE:
                                                loop.data[idx][details_col] = details
                                            else:
                                                loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                            modified = True

                            elif sigma > self._reg.cs_anomalous_error_scaled_by_sigma and std_value > max_inclusive:

                                na = self._getNearestAromaticRing(chain_id, seq_id, atom_id_)
                                pa = self._getNearestParaFerroMagneticAtom(chain_id, seq_id, atom_id_)

                                if na is None and pa is None:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                        + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                        f"must be verified (avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                        f"Z_score {z_score:.2f})."

                                    warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} "\
                                        f"({value} ppm, {sigma:.2f} sigma), "\
                                        "which is outside of expected range "\
                                        f"({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                        f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value})."

                                    if self._reg.cifChecked:
                                        warn += no_reason_message
                                        warn_alt += no_reason_message

                                    self._reg.report.warning.appendDescription('anomalous_data',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': warn,
                                                                                'value': value, 'z_score': z_score,
                                                                                'description_alt': warn_alt, 'sigma': sigma})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                            f"++ Warning  - {warn}\n")

                                elif pa is None:

                                    if (na['ring_angle'] - MAGIC_ANGLE) * z_score < 0.0 or na['ring_distance'] > VICINITY_AROMATIC:

                                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                            + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                            "should be verified "\
                                            f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                            f"Z_score {z_score:.2f}). "\
                                            f"The nearest aromatic ring "\
                                            f"({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                            f"is located at a distance of {na['ring_distance']}Å, "\
                                            f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                        warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} "\
                                            f"({value} ppm, {sigma:.2f} sigma), "\
                                            "which is outside of expected range "\
                                            f"({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                            f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                            "The nearest aromatic ring "\
                                            f"({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                            f"is located at a distance of {na['ring_distance']}Å, "\
                                            f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                        self._reg.report.warning.appendDescription('unusual_data',
                                                                                   {'file_name': file_name,
                                                                                    'sf_framecode': sf_framecode,
                                                                                    'category': lp_category, 'description': warn,
                                                                                    'value': value, 'z_score': z_score,
                                                                                    'description_alt': warn_alt, 'sigma': sigma})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                                f"++ Warning  - {warn}\n")

                                else:

                                    if pa['distance'] > VICINITY_PARAMAGNETIC:

                                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                            + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                            "should be verified "\
                                            f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                            f"Z_score {z_score:.2f}). "\
                                            "The nearest paramagnetic/ferromagnetic atom "\
                                            f"({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                            f"is located at a distance of {pa['distance']}Å."

                                        warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} "\
                                            f"({value} ppm, {sigma:.2f} sigma), "\
                                            "which is outside of expected range "\
                                            f"({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                            f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                            "The nearest paramagnetic/ferromagnetic atom "\
                                            f"({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                            f"is located at a distance of {pa['distance']}Å."

                                        self._reg.report.warning.appendDescription('unusual_data',
                                                                                   {'file_name': file_name,
                                                                                    'sf_framecode': sf_framecode,
                                                                                    'category': lp_category, 'description': warn,
                                                                                    'value': value, 'z_score': z_score,
                                                                                    'description_alt': warn_alt, 'sigma': sigma})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                                f"++ Warning  - {warn}\n")

                            elif sigma > self._reg.cs_unusual_error_scaled_by_sigma and std_value > max_inclusive:

                                na = self._getNearestAromaticRing(chain_id, seq_id, atom_id_)
                                pa = self._getNearestParaFerroMagneticAtom(chain_id, seq_id, atom_id_)

                                warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                    + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                    "should be verified "\
                                    f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, Z_score {z_score:.2f})."

                                warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} "\
                                    f"({value} ppm, {sigma:.2f} sigma), "\
                                    "which is outside of expected range "\
                                    f"({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                    f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value})."

                                if na is not None:

                                    if (na['ring_angle'] - MAGIC_ANGLE) * z_score < 0.0 or na['ring_distance'] > VICINITY_AROMATIC:
                                        warn += " The nearest aromatic ring "\
                                            f"({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                            f"is located at a distance of {na['ring_distance']}Å, "\
                                            f"and has an elevation angle of {na['ring_angle']}° with the ring plane."
                                        warn_alt += " The nearest aromatic ring "\
                                            f"({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                            f"is located at a distance of {na['ring_distance']}Å, "\
                                            f"and has an elevation angle of {na['ring_angle']}° with the ring plane."
                                    else:
                                        warn = warn_alt = None

                                elif pa is not None:

                                    if pa['distance'] > VICINITY_PARAMAGNETIC:
                                        warn += " The nearest paramagnetic/ferromagnetic atom "\
                                            f"({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                            f"is located at a distance of {pa['distance']}Å."
                                        warn_alt += " The nearest paramagnetic/ferromagnetic atom "\
                                            f"({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                            f"is located at a distance of {pa['distance']}Å."
                                    else:
                                        warn = warn_alt = None

                                elif self._reg.cifChecked:
                                    warn += no_reason_message
                                    warn_alt += no_reason_message

                                if warn is not None:
                                    self._reg.report.warning.appendDescription('unusual_data',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': warn,
                                                                                'value': value, 'z_score': z_score,
                                                                                'description_alt': warn_alt, 'sigma': sigma})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                            f"++ Warning  - {warn}\n")

                            elif not cs_stat['primary'] and cs_stat['norm_freq'] < 0.03\
                                    and self._reg.exptl_method != 'SOLID-STATE NMR':

                                warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                    + f"] {full_value_name} {value} is an unusual/rare assignment. "\
                                    f"Occurrence of {atom_name} in {comp_id} is {cs_stat['norm_freq']:.1%} in BMRB archive."

                                self._reg.report.warning.appendDescription('unusual/rare_data',
                                                                           {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                            'category': lp_category, 'description': warn})

                                if self._reg.verbose:
                                    self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                        f"++ Warning  - {warn}\n")

                        else:

                            tolerance = std_value * 10.0  # rare residue/ligand

                            if min_value < max_value and (value < min_value - tolerance or value > max_value + tolerance)\
                               and sigma > self._reg.cs_anomalous_error_scaled_by_sigma\
                               and std_value > max_inclusive:

                                na = self._getNearestAromaticRing(chain_id, seq_id, atom_id_)
                                pa = self._getNearestParaFerroMagneticAtom(chain_id, seq_id, atom_id_)

                                if na is None and pa is None:

                                    err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                        + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                        "is not within expected range "\
                                        f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                        f"Z_score {z_score:.2f})."

                                    err_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} "\
                                        f"({value} ppm, {sigma:.2f} sigma), "\
                                        "which is outside of expected range "\
                                        f"({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                        f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value})."

                                    if self._reg.cifChecked:
                                        err += no_reason_message
                                        err_alt += no_reason_message

                                    err += fold_warn_message
                                    err_alt += fold_warn_message

                                    if self._reg.nonblk_anomalous_cs or self._reg.remediation_mode:

                                        self._reg.report.warning.appendDescription('anomalous_data',
                                                                                   {'file_name': file_name,
                                                                                    'sf_framecode': sf_framecode,
                                                                                    'category': lp_category, 'description': err,
                                                                                    'value': value, 'z_score': z_score,
                                                                                    'description_alt': err_alt, 'sigma': sigma})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                                f"++ Warning  - {err}\n")

                                        if self._reg.bmrb_only and self._reg.leave_intl_note\
                                           and file_type == 'nmr-star' and details_col != -1:
                                            _details = loop.data[idx][details_col]
                                            details = f"{full_value_name} {value} is not within expected range "\
                                                f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                                f"Z_score {z_score:.2f})."\
                                                f"{no_reason_message if self._reg.cifChecked else ''}"\
                                                f"{fold_warn_message}\n"
                                            if _details in EMPTY_VALUE or (details not in _details):
                                                if _details in EMPTY_VALUE:
                                                    loop.data[idx][details_col] = details
                                                else:
                                                    loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                                modified = True

                                    else:

                                        self._reg.report.error.appendDescription('anomalous_data',
                                                                                 {'file_name': file_name,
                                                                                  'sf_framecode': sf_framecode,
                                                                                  'category': lp_category, 'description': err,
                                                                                  'value': value, 'z_score': z_score,
                                                                                  'description_alt': err_alt, 'sigma': sigma})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                                f"++ ValueError  - {err}\n")

                                elif pa is None:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                        + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                        "should be verified "\
                                        f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                        f"Z_score {z_score:.2f}). "\
                                        "The nearest aromatic ring "\
                                        f"({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                        f"is located at a distance of {na['ring_distance']}Å, "\
                                        f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                    warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} "\
                                        f"({value} ppm, {sigma:.2f} sigma), "\
                                        "which is outside of expected range "\
                                        f"({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                        f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                        "The nearest aromatic ring "\
                                        f"({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                        f"is located at a distance of {na['ring_distance']}Å, "\
                                        f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                    if (na['ring_angle'] - MAGIC_ANGLE) * z_score > 0.0\
                                       or self._reg.nonblk_anomalous_cs or self._reg.remediation_mode:

                                        if (na['ring_angle'] - MAGIC_ANGLE) * z_score < 0.0\
                                           or na['ring_distance'] > VICINITY_AROMATIC:

                                            self._reg.report.warning.appendDescription('anomalous_data',
                                                                                       {'file_name': file_name,
                                                                                        'sf_framecode': sf_framecode,
                                                                                        'category': lp_category,
                                                                                        'description': warn,
                                                                                        'value': value, 'z_score': z_score,
                                                                                        'description_alt': warn_alt,
                                                                                        'sigma': sigma})

                                            if self._reg.verbose:
                                                self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                                    f"++ Warning  - {warn}\n")

                                            if self._reg.bmrb_only and self._reg.leave_intl_note and file_type == 'nmr-star'\
                                               and details_col != -1:
                                                _details = loop.data[idx][details_col]
                                                details = f"{full_value_name} {value} is not within expected range "\
                                                    f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                                    f"Z_score {z_score:.2f}). "\
                                                    "The nearest aromatic ring "\
                                                    f"({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                                    f"is located at a distance of {na['ring_distance']}Å, "\
                                                    f"and has an elevation angle of {na['ring_angle']}° with the ring plane.\n"
                                                if _details in EMPTY_VALUE or (details not in _details):
                                                    if _details in EMPTY_VALUE:
                                                        loop.data[idx][details_col] = details
                                                    else:
                                                        loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                                    modified = True

                                    else:

                                        self._reg.report.error.appendDescription('anomalous_data',
                                                                                 {'file_name': file_name,
                                                                                  'sf_framecode': sf_framecode,
                                                                                  'category': lp_category, 'description': warn,
                                                                                  'value': value, 'z_score': z_score,
                                                                                  'description_alt': warn_alt, 'sigma': sigma})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                                f"++ ValueError  - {warn}\n")

                                else:

                                    if pa['distance'] > VICINITY_PARAMAGNETIC:

                                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                            + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                            "should be verified "\
                                            f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                            f"Z_score {z_score:.2f}). "\
                                            "The nearest paramagnetic/ferromagnetic atom "\
                                            f"({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                            f"is located at a distance of {pa['distance']}Å."

                                        warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} "\
                                            f"({value} ppm, {sigma:.2f} sigma), "\
                                            "which is outside of expected range "\
                                            f"({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                            f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                            "The nearest paramagnetic/ferromagnetic atom "\
                                            f"({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                            f"is located at a distance of {pa['distance']}Å."

                                        self._reg.report.warning.appendDescription('unusual_data',
                                                                                   {'file_name': file_name,
                                                                                    'sf_framecode': sf_framecode,
                                                                                    'category': lp_category, 'description': warn,
                                                                                    'value': value, 'z_score': z_score,
                                                                                    'description_alt': warn_alt, 'sigma': sigma})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                                f"++ Warning  - {warn}\n")

                                        if self._reg.bmrb_only and self._reg.leave_intl_note\
                                           and file_type == 'nmr-star' and details_col != -1:
                                            _details = loop.data[idx][details_col]
                                            details = f"{full_value_name} {value} is not within expected range "\
                                                f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                                f"Z_score {z_score:.2f}). "\
                                                "The nearest paramagnetic/ferromagnetic atom "\
                                                f"({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                                f"is located at a distance of {pa['distance']}Å.\n"
                                            if _details in EMPTY_VALUE or (details not in _details):
                                                if _details in EMPTY_VALUE:
                                                    loop.data[idx][details_col] = details
                                                else:
                                                    loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                                modified = True

                            elif sigma > self._reg.cs_anomalous_error_scaled_by_sigma and std_value > max_inclusive:

                                na = self._getNearestAromaticRing(chain_id, seq_id, atom_id_)
                                pa = self._getNearestParaFerroMagneticAtom(chain_id, seq_id, atom_id_)

                                if na is None and pa is None:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                        + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                        f"must be verified (avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                        f"Z_score {z_score:.2f})."

                                    warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} "\
                                        f"({value} ppm, {sigma:.2f} sigma), "\
                                        "which is outside of expected range "\
                                        f"({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                        f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value})."

                                    if self._reg.cifChecked:
                                        warn += no_reason_message
                                        warn_alt += no_reason_message

                                    self._reg.report.warning.appendDescription('anomalous_data',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': warn,
                                                                                'value': value, 'z_score': z_score,
                                                                                'description_alt': warn_alt, 'sigma': sigma})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                            f"++ Warning  - {warn}\n")

                                elif pa is None:

                                    if (na['ring_angle'] - MAGIC_ANGLE) * z_score < 0.0 or na['ring_distance'] > VICINITY_AROMATIC:

                                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                            + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                            "should be verified "\
                                            f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                            f"Z_score {z_score:.2f}). "\
                                            "The nearest aromatic ring "\
                                            f"({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                            f"is located at a distance of {na['ring_distance']}Å, "\
                                            f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                        warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} "\
                                            f"({value} ppm, {sigma:.2f} sigma), "\
                                            "which is outside of expected range "\
                                            f"({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                            f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                            "The nearest aromatic ring "\
                                            f"({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                            f"is located at a distance of {na['ring_distance']}Å, "\
                                            f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                        self._reg.report.warning.appendDescription('unusual_data',
                                                                                   {'file_name': file_name,
                                                                                    'sf_framecode': sf_framecode,
                                                                                    'category': lp_category, 'description': warn,
                                                                                    'value': value, 'z_score': z_score,
                                                                                    'description_alt': warn_alt, 'sigma': sigma})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                                f"++ Warning  - {warn}\n")

                                else:

                                    if pa['distance'] > VICINITY_PARAMAGNETIC:

                                        warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                            + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                            "should be verified "\
                                            f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                            f"Z_score {z_score:.2f}). "\
                                            "The nearest paramagnetic/ferromagnetic atom "\
                                            f"({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                            f"is located at a distance of {pa['distance']}Å."

                                        warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} "\
                                            f"({value} ppm, {sigma:.2f} sigma), "\
                                            "which is outside of expected range "\
                                            f"({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                            f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                            "The nearest paramagnetic/ferromagnetic atom "\
                                            f"({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                            f"is located at a distance of {pa['distance']}Å."

                                        self._reg.report.warning.appendDescription('unusual_data',
                                                                                   {'file_name': file_name,
                                                                                    'sf_framecode': sf_framecode,
                                                                                    'category': lp_category, 'description': warn,
                                                                                    'value': value, 'z_score': z_score,
                                                                                    'description_alt': warn_alt, 'sigma': sigma})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                                f"++ Warning  - {warn}\n")

                # standard residue
                else:

                    cs_stat = next((cs_stat for cs_stat in self._reg.csStat.get(comp_id, self._reg.report.isDiamagnetic())
                                    if cs_stat['atom_id'] == atom_id_ and cs_stat['count'] > 0), None)

                    if cs_stat is not None:
                        min_value = cs_stat['min']
                        max_value = cs_stat['max']
                        avg_value = cs_stat['avg']
                        std_value = cs_stat['std']

                        has_cs_stat = True

                        if atom_id_[0] in PROTON_BEGIN_CODE and 'methyl' in cs_stat['desc']:
                            methyl_cs_key = (chain_id, seq_id, atom_id_[:-1], occupancy)

                            if methyl_cs_key not in methyl_cs_vals:
                                methyl_cs_vals[methyl_cs_key] = value

                            elif value != methyl_cs_vals[methyl_cs_key] and methyl_cs_key not in failed_methyl_cs_keys:
                                failed_methyl_cs_keys.append(methyl_cs_key)

                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                    + "] Chemical shift values in the same methyl group "\
                                    f"({full_value_name} {value} vs {methyl_cs_vals[methyl_cs_key]}) are inconsistent."

                                if self._reg.combined_mode and not self._reg.remediation_mode:

                                    self._reg.report.error.appendDescription('invalid_data',
                                                                             {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                              'category': lp_category, 'description': err})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                            f"++ ValueError  - {err}\n")

                                else:

                                    _sigma = round(abs(value - methyl_cs_vals[methyl_cs_key]) / max_inclusive, 2)

                                    self._reg.report.warning.appendDescription('conflicted_data',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': err,
                                                                                'sigma': _sigma})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                            f"++ Warning  - {err}\n")

                        if std_value is None or std_value <= 0.0:

                            warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                + f"] Insufficient chemical shift statistics on comp_id {comp_id}, atom_id {atom_name} "\
                                f"is available to verify {full_value_name} {value} (avg {avg_value})."

                            self._reg.report.warning.appendDescription('unusual_data',
                                                                       {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                        'category': lp_category, 'description': warn})

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                    f"++ Warning  - {warn}\n")

                            continue

                        if avg_value is None:

                            warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                + f"] Insufficient chemical shift statistics on comp_id {comp_id}, atom_id {atom_name} "\
                                f"is available to verify {full_value_name} {value}."

                            self._reg.report.warning.appendDescription('unusual_data',
                                                                       {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                        'category': lp_category, 'description': warn})

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                    f"++ Warning  - {warn}\n")

                            continue

                        z_score = round((value - avg_value) / std_value, 2)
                        sigma = abs(z_score)
                        tolerance = std_value

                        if (value < min_value - tolerance or value > max_value + tolerance)\
                           and sigma > self._reg.cs_unusual_error_scaled_by_sigma\
                           and std_value > max_inclusive:

                            na = self._getNearestAromaticRing(chain_id, seq_id, atom_id_)
                            pa = self._getNearestParaFerroMagneticAtom(chain_id, seq_id, atom_id_)

                            if na is None and pa is None:

                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                    + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                    "is not within expected range "\
                                    f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                    f"Z_score {z_score:.2f})."

                                err_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} "\
                                    f"({value} ppm, {sigma:.2f} sigma), "\
                                    "which is outside of expected range "\
                                    f"({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                    f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value})."

                                if self._reg.cifChecked:
                                    err += no_reason_message
                                    err_alt += no_reason_message

                                err += fold_warn_message
                                err_alt += fold_warn_message

                                if self._reg.nonblk_anomalous_cs or self._reg.remediation_mode:

                                    self._reg.report.warning.appendDescription('anomalous_data',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': err,
                                                                                'value': value, 'z_score': z_score,
                                                                                'description_alt': err_alt, 'sigma': sigma})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                            f"++ Warning  - {err}\n")

                                    if self._reg.bmrb_only and self._reg.leave_intl_note\
                                       and file_type == 'nmr-star' and details_col != -1:
                                        _details = loop.data[idx][details_col]
                                        details = f"{full_value_name} {value} is not within expected range "\
                                            f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                            f"Z_score {z_score:.2f})."\
                                            f"{no_reason_message if self._reg.cifChecked else ''}"\
                                            f"{fold_warn_message}\n"
                                        if _details in EMPTY_VALUE or (details not in _details):
                                            if _details in EMPTY_VALUE:
                                                loop.data[idx][details_col] = details
                                            else:
                                                loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                            modified = True

                                else:

                                    self._reg.report.error.appendDescription('anomalous_data',
                                                                             {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                              'category': lp_category, 'description': err,
                                                                              'value': value, 'z_score': z_score,
                                                                              'description_alt': err_alt, 'sigma': sigma})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                            f"++ ValueError  - {err}\n")

                            elif pa is None:

                                warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                    + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                    "should be verified "\
                                    f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                    f"Z_score {z_score:.2f}). "\
                                    "The nearest aromatic ring "\
                                    f"({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                    f"is located at a distance of {na['ring_distance']}Å, "\
                                    f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} "\
                                    f"({value} ppm, {sigma:.2f} sigma), "\
                                    "which is outside of expected range "\
                                    f"({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                    f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                    "The nearest aromatic ring "\
                                    f"({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                    f"is located at a distance of {na['ring_distance']}Å, "\
                                    f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                if (na['ring_angle'] - MAGIC_ANGLE) * z_score > 0.0\
                                   or self._reg.nonblk_anomalous_cs or self._reg.remediation_mode:

                                    self._reg.report.warning.appendDescription('anomalous_data'
                                                                               if (na['ring_angle'] - MAGIC_ANGLE) * z_score < 0.0
                                                                               or na['ring_distance'] > VICINITY_AROMATIC
                                                                               else 'unusual_data',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': warn,
                                                                                'value': value, 'z_score': z_score,
                                                                                'description_alt': warn_alt, 'sigma': sigma})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                            f"++ Warning  - {warn}\n")

                                    if self._reg.bmrb_only and self._reg.leave_intl_note\
                                       and file_type == 'nmr-star' and details_col != -1\
                                       and ((na['ring_angle'] - MAGIC_ANGLE) * z_score > 0.0 or self._reg.nonblk_anomalous_cs):
                                        _details = loop.data[idx][details_col]
                                        details = f"{full_value_name} {value} is not within expected range "\
                                            f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                            f"Z_score {z_score:.2f}). "\
                                            "The nearest aromatic ring "\
                                            f"({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                            f"is located at a distance of {na['ring_distance']}Å, "\
                                            f"and has an elevation angle of {na['ring_angle']}° with the ring plane.\n"
                                        if _details in EMPTY_VALUE or (details not in _details):
                                            if _details in EMPTY_VALUE:
                                                loop.data[idx][details_col] = details
                                            else:
                                                loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                            modified = True

                                else:

                                    self._reg.report.error.appendDescription('anomalous_data',
                                                                             {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                              'category': lp_category, 'description': warn,
                                                                              'value': value, 'z_score': z_score,
                                                                              'description_alt': warn_alt, 'sigma': sigma})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                            f"++ ValueError  - {warn}\n")

                            else:

                                warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                    + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                    "should be verified "\
                                    f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                    f"Z_score {z_score:.2f}). "\
                                    "The nearest paramagnetic/ferromagnetic atom "\
                                    f"({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                    f"is located at a distance of {pa['distance']}Å."

                                warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} "\
                                    f"({value} ppm, {sigma:.2f} sigma), "\
                                    "which is outside of expected range "\
                                    f"({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                    f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                    "The nearest paramagnetic/ferromagnetic atom "\
                                    f"({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                    f"is located at a distance of {pa['distance']}Å."

                                self._reg.report.warning.appendDescription('anomalous_data' if pa['distance'] > VICINITY_PARAMAGNETIC  # noqa: E501, pylint: disable=line-too-long
                                                                           else 'unusual_data',
                                                                           {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                            'category': lp_category, 'description': warn,
                                                                            'value': value, 'z_score': z_score,
                                                                            'description_alt': warn_alt, 'sigma': sigma})

                                if self._reg.verbose:
                                    self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                        f"++ Warning  - {warn}\n")

                                if self._reg.bmrb_only and self._reg.leave_intl_note and file_type == 'nmr-star'\
                                   and details_col != -1\
                                   and pa['distance'] > VICINITY_PARAMAGNETIC:
                                    _details = loop.data[idx][details_col]
                                    details = f"{full_value_name} {value} is not within expected range "\
                                        f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                        f"Z_score {z_score:.2f}). "\
                                        "The nearest paramagnetic/ferromagnetic atom "\
                                        f"({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                        f"is located at a distance of {pa['distance']}Å.\n"
                                    if _details in EMPTY_VALUE or (details not in _details):
                                        if _details in EMPTY_VALUE:
                                            loop.data[idx][details_col] = details
                                        else:
                                            loop.data[idx][details_col] += ('' if '\n' in _details else '\n') + details
                                        modified = True

                        # Set 5.0 to be consistent with validation report
                        elif sigma > self._reg.cs_unusual_error_scaled_by_sigma and std_value > max_inclusive:

                            na = self._getNearestAromaticRing(chain_id, seq_id, atom_id_)
                            pa = self._getNearestParaFerroMagneticAtom(chain_id, seq_id, atom_id_)

                            if na is None and pa is None:

                                warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                    + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                    f"must be verified (avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                    f"Z_score {z_score:.2f})."

                                warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} "\
                                    f"({value} ppm, {sigma:.2f} sigma), "\
                                    "which is outside of expected range "\
                                    f"({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                    f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value})."

                                if self._reg.cifChecked:
                                    warn += no_reason_message
                                    warn_alt += no_reason_message

                                self._reg.report.warning.appendDescription('anomalous_data',
                                                                           {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                            'category': lp_category, 'description': warn,
                                                                            'value': value, 'z_score': z_score,
                                                                            'description_alt': warn_alt, 'sigma': sigma})

                                if self._reg.verbose:
                                    self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                        f"++ Warning  - {warn}\n")

                            elif pa is None:

                                if (na['ring_angle'] - MAGIC_ANGLE) * z_score < 0.0 or na['ring_distance'] > VICINITY_AROMATIC:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                        + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                        "should be verified "\
                                        f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                        f"Z_score {z_score:.2f}). "\
                                        "The nearest aromatic ring "\
                                        f"({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                        f"is located at a distance of {na['ring_distance']}Å, "\
                                        f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                    warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} "\
                                        f"({value} ppm, {sigma:.2f} sigma), "\
                                        "which is outside of expected range "\
                                        f"({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                        f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                        "The nearest aromatic ring "\
                                        f"({na['chain_id']}:{na['seq_id']}:{na['comp_id']}:{na['ring_atoms']}) "\
                                        f"is located at a distance of {na['ring_distance']}Å, "\
                                        f"and has an elevation angle of {na['ring_angle']}° with the ring plane."

                                    self._reg.report.warning.appendDescription('unusual_data',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': warn,
                                                                                'value': value, 'z_score': z_score,
                                                                                'description_alt': warn_alt, 'sigma': sigma})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                            f"++ Warning  - {warn}\n")

                            else:

                                if pa['distance'] > VICINITY_PARAMAGNETIC:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                        + f"] {full_value_name} {value} ({chain_id}:{seq_id}:{comp_id}:{atom_name}) "\
                                        "should be verified "\
                                        f"(avg {avg_value}, std {std_value}, min {min_value}, max {max_value}, "\
                                        f"Z_score {z_score:.2f}). "\
                                        "The nearest paramagnetic/ferromagnetic atom "\
                                        f"({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                        f"is located at a distance of {pa['distance']}Å."

                                    warn_alt = f"Verify chemical shift value for {chain_id}:{seq_id}:{comp_id}:{atom_name} "\
                                        f"({value} ppm, {sigma:.2f} sigma), "\
                                        "which is outside of expected range "\
                                        f"({avg_value + 5.0 * std_value:.2f} ~ {avg_value - 5.0 * std_value:.2f} ppm, "\
                                        f"avg {avg_value}, std {std_value}, min {min_value}, max {max_value}). "\
                                        "The nearest paramagnetic/ferromagnetic atom "\
                                        f"({pa['chain_id']}:{pa['seq_id']}:{pa['comp_id']}:{pa['atom_id']}) "\
                                        f"is located at a distance of {pa['distance']}Å."

                                    self._reg.report.warning.appendDescription('unusual_data',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': warn,
                                                                                'value': value, 'z_score': z_score,
                                                                                'description_alt': warn_alt, 'sigma': sigma})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                            f"++ Warning  - {warn}\n")

                        elif not cs_stat['primary'] and cs_stat['norm_freq'] < 0.03\
                                and self._reg.exptl_method != 'SOLID-STATE NMR':

                            warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                                + f"] {full_value_name} {value} is an unusual/rare assignment. "\
                                f"Occurrence of {atom_name} in {comp_id} is {cs_stat['norm_freq']:.1%} in BMRB archive."

                            self._reg.report.warning.appendDescription('unusual/rare_data',
                                                                       {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                        'category': lp_category, 'description': warn})

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                    f"++ Warning  - {warn}\n")

                if not has_cs_stat:

                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_name)\
                        + f"] No chemical shift statistics is available to verify {full_value_name} {value}."

                    self._reg.report.warning.appendDescription('unusual_data',
                                                               {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                'category': lp_category, 'description': warn})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                            f"++ Warning  - {warn}\n")

                # check ambiguity code
                if file_type == 'nmr-star' and ambig_code_name in row:
                    ambig_code = row[ambig_code_name]

                    if ambig_code in EMPTY_VALUE or ambig_code == 1:
                        continue

                    _atom_id = atom_id

                    if self.isNmrAtomName(comp_id, atom_id):
                        _atom_id = self.getRepAtomId(comp_id, atom_id)

                    allowed_ambig_code = self._reg.csStat.getMaxAmbigCodeWoSetId(comp_id, _atom_id)

                    if ambig_code in (2, 3):

                        ambig_code_desc = 'ambiguity of geminal atoms or geminal methyl proton groups' if ambig_code == 2\
                            else 'aromatic atoms on opposite sides of symmetrical rings'

                        _atom_id2 = self._reg.csStat.getGeminalAtom(comp_id, _atom_id)

                        if ambig_code != allowed_ambig_code:

                            if allowed_ambig_code == 1:

                                try:

                                    _row = next(_row for _row in lp_data
                                                if _row[chain_id_name] == chain_id
                                                and _row[seq_id_name] == seq_id
                                                and _row[comp_id_name] == comp_id
                                                and _row[atom_id_name] == _atom_id2)

                                    loop.data[lp_data.index(_row)][loop.tags.index(ambig_code_name)] = 1

                                except StopIteration:
                                    pass

                            elif allowed_ambig_code > 0:

                                if self._reg.remediation_mode:
                                    pass

                                else:

                                    err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                        + f"] Invalid {ambig_code_name} {str(ambig_code)!r} "\
                                        f"(allowed ambig_code {[1, allowed_ambig_code, 4, 5, 6, 9]}) in a loop {lp_category}."

                                    self._reg.report.error.appendDescription('invalid_ambiguity_code',
                                                                             {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                              'category': lp_category, 'description': err})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                            f"++ ValueError  - {err}\n")

                        try:

                            _row = next(_row for _row in lp_data
                                        if _row[chain_id_name] == chain_id
                                        and _row[seq_id_name] == seq_id
                                        and _row[comp_id_name] == comp_id
                                        and _row[atom_id_name] == _atom_id2)

                            ambig_code2 = _row[ambig_code_name]

                            if ambig_code2 is not None and ambig_code2 != ambig_code:

                                if ambig_code2 < 4:
                                    loop.data[lp_data.index(_row)][loop.tags.index(ambig_code_name)] = ambig_code

                                if self._reg.remediation_mode:
                                    pass

                                else:

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                        + f"] {ambig_code_name} {str(ambig_code)!r} indicates {ambig_code_desc}. "\
                                        f"However, {ambig_code_name} {ambig_code2} of {atom_id_name} {_atom_id2} is inconsistent."

                                    self._reg.report.warning.appendDescription('ambiguity_code_mismatch',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': warn})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                            f"++ Warning  - {warn}\n")

                        except StopIteration:
                            pass

                    elif ambig_code in (4, 5, 6, 9):

                        ambig_set_id_name = 'Ambiguity_set_ID'

                        if ambig_set_id_name not in row:

                            err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                + f"] {ambig_code_name} {str(ambig_code)!r} requires {ambig_set_id_name} loop tag."

                            if self._reg.remediation_mode:

                                self._reg.report.warning.appendDescription('missing_data',
                                                                           {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                            'category': lp_category, 'description': err})

                                if self._reg.verbose:
                                    self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                        f"++ Warning  - {err}\n")

                            else:

                                self._reg.report.error.appendDescription('missing_mandatory_item',
                                                                         {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                          'category': lp_category, 'description': err})

                                if self._reg.verbose:
                                    self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                        f"++ LookupError  - {file_name} {sf_framecode} {lp_category} {err}\n")

                        else:

                            ambig_set_id = row[ambig_set_id_name]

                            if ambig_set_id in EMPTY_VALUE:

                                if ambig_code in (4, 5):

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                        + f"] {ambig_code_name} {str(ambig_code)!r} requires {ambig_set_id_name} value."

                                    self._reg.report.warning.appendDescription('missing_data',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': warn})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                            f"++ Warning  - {warn}\n")

                            else:

                                ambig_set = [_row for _row in lp_data if _row[ambig_set_id_name] == ambig_set_id and _row != row]

                                if len(ambig_set) == 0:

                                    if ambig_code == 4:
                                        ambig_desc = 'of intra-residue atoms '
                                    elif ambig_code == 5:
                                        ambig_desc = 'of inter-residue atoms '
                                    else:
                                        ambig_desc = ''

                                    warn = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                        + f"] {ambig_code_name} {str(ambig_code)!r} requires other rows {ambig_desc}"\
                                        f"sharing {ambig_set_id_name} {ambig_set_id}."

                                    self._reg.report.warning.appendDescription('missing_data',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': warn})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                            f"++ Warning  - {warn}\n")

                                # intra-residue ambiguities
                                elif ambig_code == 4:

                                    for _row in ambig_set:
                                        chain_id2 = _row[chain_id_name]
                                        seq_id2 = _row[seq_id_name]
                                        comp_id2 = _row[comp_id_name]
                                        atom_id2 = _row[atom_id_name]

                                        _atom_id2 = atom_id2

                                        if self.isNmrAtomName(comp_id2, atom_id2):
                                            _atom_id2 = self.getRepAtomId(comp_id2, atom_id2)

                                        if (chain_id2 != chain_id or seq_id2 != seq_id or comp_id2 != comp_id)\
                                           and _atom_id < _atom_id2:

                                            err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                                + f", {ambig_code_name} {str(ambig_code)!r}, {ambig_set_id_name} {ambig_set_id}] "\
                                                "It indicates intra-residue ambiguities. However, row of "\
                                                + row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2) + ' exists.'

                                            self._reg.report.error.appendDescription('invalid_ambiguity_code',
                                                                                     {'file_name': file_name,
                                                                                      'sf_framecode': sf_framecode,
                                                                                      'category': lp_category, 'description': err})

                                            if self._reg.verbose:
                                                self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                                    f"++ ValueError  - {err}\n")

                                # inter-residue ambiguities
                                elif ambig_code == 5:

                                    inter_residue_seq_id = False

                                    for _row in ambig_set:
                                        chain_id2 = _row[chain_id_name]
                                        seq_id2 = _row[seq_id_name]
                                        comp_id2 = _row[comp_id_name]
                                        atom_id2 = _row[atom_id_name]

                                        _atom_id2 = atom_id2

                                        if self.isNmrAtomName(comp_id2, atom_id2):
                                            _atom_id2 = self.getRepAtomId(comp_id2, atom_id2)

                                        if chain_id2 != chain_id or seq_id2 != seq_id:
                                            inter_residue_seq_id = True
                                            break

                                    if not inter_residue_seq_id:

                                        for _row in ambig_set:
                                            chain_id2 = _row[chain_id_name]
                                            seq_id2 = _row[seq_id_name]
                                            comp_id2 = _row[comp_id_name]
                                            atom_id2 = _row[atom_id_name]

                                            _atom_id2 = atom_id2

                                            if self.isNmrAtomName(comp_id2, atom_id2):
                                                _atom_id2 = self.getRepAtomId(comp_id2, atom_id2)

                                            if chain_id2 == chain_id and seq_id2 == seq_id and _atom_id < _atom_id2:

                                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                                    + f", {ambig_code_name} {str(ambig_code)!r}, "\
                                                    f"{ambig_set_id_name} {ambig_set_id}] "\
                                                    "It indicates inter-residue ambiguities. However, row of "\
                                                    + row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2) + ' exists.'

                                                self._reg.report.error.appendDescription('invalid_ambiguity_code',
                                                                                         {'file_name': file_name,
                                                                                          'sf_framecode': sf_framecode,
                                                                                          'category': lp_category,
                                                                                          'description': err})

                                                if self._reg.verbose:
                                                    self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                                        f"++ ValueError  - {err}\n")

                                # inter-molecular ambiguities
                                elif ambig_code == 6:

                                    for _row in ambig_set:
                                        chain_id2 = _row[chain_id_name]
                                        seq_id2 = _row[seq_id_name]
                                        comp_id2 = _row[comp_id_name]
                                        atom_id2 = _row[atom_id_name]

                                        _atom_id2 = atom_id2

                                        if self.isNmrAtomName(comp_id2, atom_id2):
                                            _atom_id2 = self.getRepAtomId(comp_id2, atom_id2)

                                        if chain_id2 == chain_id\
                                           and (seq_id < seq_id2 or (seq_id == seq_id2 and _atom_id < _atom_id2)):

                                            if chain_id == chain_id2 and seq_id == seq_id2:
                                                if _atom_id2 in self._reg.csStat.getProtonsInSameGroup(comp_id, _atom_id):
                                                    continue

                                            if not any(True for _row_ in ambig_set if _row_[chain_id_name] != chain_id
                                               and _row_[seq_id_name] == seq_id and _row_[comp_id_name] == comp_id
                                               and _row_[atom_id_name] == atom_id):

                                                err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                                    + f", {ambig_code_name} {str(ambig_code)!r}, "\
                                                    f"{ambig_set_id_name} {ambig_set_id}] "\
                                                    "It indicates inter-molecular ambiguities. However, row of "\
                                                    + row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2) + ' exists.'

                                                self._reg.report.error.appendDescription('invalid_ambiguity_code',
                                                                                         {'file_name': file_name,
                                                                                          'sf_framecode': sf_framecode,
                                                                                          'category': lp_category,
                                                                                          'description': err})

                                                if self._reg.verbose:
                                                    self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                                        f"++ ValueError  - {err}\n")

                                for _row in ambig_set:
                                    chain_id2 = _row[chain_id_name]
                                    seq_id2 = _row[seq_id_name]
                                    comp_id2 = _row[comp_id_name]
                                    atom_id2 = _row[atom_id_name]
                                    value2 = _row[value_name]

                                    if comp_id2 not in STD_MON_DICT:
                                        continue

                                    _atom_id2 = atom_id2

                                    if self.isNmrAtomName(comp_id2, atom_id2):
                                        _atom_id2 = self.getRepAtomId(comp_id2, atom_id2)

                                    if _atom_id[0] != _atom_id2[0] and _atom_id < _atom_id2:

                                        if self._reg.remediation_mode:

                                            chain_id_col = loop.tags.index(chain_id_name)
                                            seq_id_col = loop.tags.index(seq_id_name)
                                            comp_id_col = loop.tags.index(comp_id_name)
                                            atom_id_col = loop.tags.index(atom_id_name)
                                            ambig_code_col = loop.tags.index(ambig_code_name)

                                            row = next(row for row in loop
                                                       if row[chain_id_col] in alt_chain_id and int(row[seq_id_col]) == seq_id
                                                       and row[comp_id_col] == comp_id and row[atom_id_col] == atom_id)

                                            row[ambig_code_col] = allowed_ambig_code

                                            row = next(row for row in loop
                                                       if row[chain_id_col] in alt_chain_id and int(row[seq_id_col]) == seq_id2
                                                       and row[comp_id_col] == comp_id2 and row[atom_id_col] == atom_id2)

                                            row[ambig_code_col] = allowed_ambig_code

                                            modified = True

                                        else:

                                            err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                                + f", {ambig_code_name} {str(ambig_code)!r}, {ambig_set_id_name} {ambig_set_id}] "\
                                                "However, observation nucleus of "\
                                                + row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2)\
                                                + " is different in the set that share the same ambiguity code "\
                                                f"({_atom_id[0]!r} vs {_atom_id2[0]!r})."

                                            self._reg.report.error.appendDescription('invalid_ambiguity_code',
                                                                                     {'file_name': file_name,
                                                                                      'sf_framecode': sf_framecode,
                                                                                      'category': lp_category, 'description': err})

                                            if self._reg.verbose:
                                                self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                                    f"++ ValueError  - {err}\n")

                                    elif abs(value2 - value) > CS_UNCERT_MAX and value < value2 and ambig_code <= 4:

                                        if self._reg.remediation_mode:

                                            chain_id_col = loop.tags.index(chain_id_name)
                                            seq_id_col = loop.tags.index(seq_id_name)
                                            comp_id_col = loop.tags.index(comp_id_name)
                                            atom_id_col = loop.tags.index(atom_id_name)
                                            ambig_code_col = loop.tags.index(ambig_code_name)

                                            row = next(row for row in loop
                                                       if row[chain_id_col] in alt_chain_id and int(row[seq_id_col]) == seq_id
                                                       and row[comp_id_col] == comp_id and row[atom_id_col] == atom_id)

                                            row[ambig_code_col] = allowed_ambig_code

                                            row = next(row for row in loop
                                                       if row[chain_id_col] in alt_chain_id and int(row[seq_id_col]) == seq_id2
                                                       and row[comp_id_col] == comp_id2 and row[atom_id_col] == atom_id2)

                                            row[ambig_code_col] = allowed_ambig_code

                                            modified = True

                                        else:

                                            err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                                                + f", {value_name} {value}, {ambig_code_name} {str(ambig_code)!r}, "\
                                                f"{ambig_set_id_name} {ambig_set_id}] "\
                                                f"However, {value_name} {value2} of "\
                                                + row_tmp % (chain_id2, seq_id2, comp_id2, atom_id2)\
                                                + " is noticeably different from others in the set "\
                                                "that share the same ambiguity code "\
                                                f"by {value2 - value:.3f} (tolerance {CS_UNCERT_MAX})."

                                            self._reg.report.error.appendDescription('invalid_ambiguity_code',
                                                                                     {'file_name': file_name,
                                                                                      'sf_framecode': sf_framecode,
                                                                                      'category': lp_category, 'description': err})

                                            if self._reg.verbose:
                                                self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                                    f"++ ValueError  - {err}\n")

                    else:

                        err = chk_row_tmp % (chain_id, seq_id, comp_id, atom_id)\
                            + f"] Invalid ambiguity code {str(ambig_code)!r} "\
                            f"(allowed ambig_code {ALLOWED_AMBIGUITY_CODES}) in a loop."

                        self._reg.report.error.appendDescription('invalid_ambiguity_code',
                                                                 {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                  'category': lp_category, 'description': err})

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                                f"++ ValueError  - {err}\n")

        except StopIteration:

            err = f"Assigned chemical shifts of {sf_framecode!r} saveframe was not parsed properly. Please fix problems reported."

            self._reg.report.error.appendDescription('missing_mandatory_content',
                                                     {'file_name': file_name, 'description': err})

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                    f"++ Error  - {err}\n")

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.validateCsValue() "
                                                     "++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.validateCsValue() "
                                    f"++ Error  - {str(e)}\n")

        return modified

    def _getNearestAromaticRing(self, nmr_chain_id: str, nmr_seq_id: int, nmr_atom_id: str
                                ) -> Optional[dict]:
        """ Return the nearest aromatic ring around a given atom.
            @return: the nearest aromatic ring
        """

        if not self._reg.cifChecked:
            return None

        cif_ps = self._reg.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return None

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self._reg.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return None

        seq_key = (nmr_chain_id, nmr_seq_id, nmr_atom_id)

        if seq_key in self._reg.cpC['near_ring']:
            return self._reg.cpC['near_ring'][seq_key]

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            cif_seq_id = next((test_seq_id for ref_seq_id, test_seq_id
                               in zip(result['ref_seq_id'], result['test_seq_id'])
                               if ref_seq_id == nmr_seq_id), None)

            if cif_seq_id is None:
                self._reg.cpC['near_ring'][seq_key] = None
                return None

            try:

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self._reg.coord_atom_site_tags else 'ndb_model'

                _origin = self._reg.cR.getDictListWithFilter('atom_site',
                                                             [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                              {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                              {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                              ],
                                                             [{'name': 'label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                                              {'name': 'label_seq_id', 'type': 'int', 'value': cif_seq_id},
                                                              {'name': 'label_atom_id', 'type': 'str', 'value': nmr_atom_id},
                                                              {'name': model_num_name, 'type': 'int',
                                                               'value': self._reg.representative_model_id},
                                                              {'name': 'label_alt_id', 'type': 'enum',
                                                               'enum': (self._reg.representative_alt_id,)}
                                                              ])

            except Exception as e:  # pylint: disable=broad-exception-caught

                self._reg.report.error.appendDescription('internal_error',
                                                         f"+{self.__class_name__}.__getNearestAromaticRing() "
                                                         "++ Error  - " + str(e))

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.__getNearestAromaticRing() "
                                        f"++ Error  - {str(e)}\n")

                return None

            if len(_origin) != 1:
                self._reg.cpC['near_ring'][seq_key] = None
                return None

            o = to_np_array(_origin[0])

            try:

                _neighbor = self._reg.cR.getDictListWithFilter('atom_site',
                                                               [{'name': 'label_asym_id', 'type': 'str', 'alt_name': 'chain_id'},
                                                                {'name': 'label_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                                {'name': 'label_comp_id', 'type': 'starts-with-alnum',
                                                                 'alt_name': 'comp_id'},
                                                                {'name': 'label_atom_id', 'type': 'starts-with-alnum',
                                                                 'alt_name': 'atom_id'},
                                                                {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                                {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                                {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                                {'name': 'type_symbol', 'type': 'str'}
                                                                ],
                                                               [{'name': 'Cartn_x', 'type': 'range-float',
                                                                 'range': {'min_exclusive': (o[0] - CUTOFF_AROMATIC),
                                                                           'max_exclusive': (o[0] + CUTOFF_AROMATIC)}},
                                                                {'name': 'Cartn_y', 'type': 'range-float',
                                                                 'range': {'min_exclusive': (o[1] - CUTOFF_AROMATIC),
                                                                           'max_exclusive': (o[1] + CUTOFF_AROMATIC)}},
                                                                {'name': 'Cartn_z', 'type': 'range-float',
                                                                 'range': {'min_exclusive': (o[2] - CUTOFF_AROMATIC),
                                                                           'max_exclusive': (o[2] + CUTOFF_AROMATIC)}},
                                                                {'name': model_num_name, 'type': 'int',
                                                                 'value': self._reg.representative_model_id},
                                                                {'name': 'label_alt_id', 'type': 'enum',
                                                                 'enum': (self._reg.representative_alt_id,)}
                                                                ])

            except Exception as e:  # pylint: disable=broad-exception-caught

                self._reg.report.error.appendDescription('internal_error',
                                                         f"+{self.__class_name__}.__getNearestAromaticRing() "
                                                         "++ Error  - " + str(e))

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.__getNearestAromaticRing() "
                                        f"++ Error  - {str(e)}\n")

                return None

            if len(_neighbor) == 0:
                self._reg.cpC['near_ring'][seq_key] = None
                return None

            neighbor = [n for n in _neighbor
                        if n['seq_id'] != cif_seq_id
                        and n['type_symbol'] not in PROTON_BEGIN_CODE
                        and distance(to_np_array(n), o) < CUTOFF_AROMATIC
                        and n['atom_id'] in self._reg.csStat.getAromaticAtoms(n['comp_id'])]

            if len(neighbor) == 0:
                self._reg.cpC['near_ring'][seq_key] = None
                return None

            if not has_key_value(seq_align_dic, 'model_poly_seq_vs_nmr_poly_seq'):
                self._reg.cpC['near_ring'][seq_key] = None
                return None

            atom_list = []

            for n in neighbor:

                _cif_chain_id = n['chain_id']

                _ps = self._reg.report.getNmrPolymerSequenceWithModelChainId(_cif_chain_id)

                if _ps is None:
                    continue

                _nmr_chain_id = _ps['chain_id']

                result = next((seq_align for seq_align in seq_align_dic['model_poly_seq_vs_nmr_poly_seq']
                               if seq_align['ref_chain_id'] == _cif_chain_id and seq_align['test_chain_id'] == _nmr_chain_id), None)

                if result is not None:

                    _nmr_seq_id = next((test_seq_id for ref_seq_id, test_seq_id
                                        in zip(result['ref_seq_id'], result['test_seq_id'])
                                        if ref_seq_id == n['seq_id']), None)

                    atom_list.append({'chain_id': _nmr_chain_id,
                                      'seq_id': _nmr_seq_id,
                                      'cif_chain_id': _cif_chain_id,
                                      'cif_seq_id': n['seq_id'],
                                      'comp_id': n['comp_id'],
                                      'atom_id': n['atom_id'],
                                      'distance': distance(to_np_array(n), o)})

            if len(atom_list) == 0:
                return None

            na = sorted(atom_list, key=itemgetter('distance'))[0]

            na_atom_id = na['atom_id']

            if not self._reg.ccU.updateChemCompDict(na['comp_id']):
                self._reg.cpC['near_ring'][seq_key] = None
                return None

            # matches with comp_id in CCD

            half_ring_traces = []

            for b1 in self._reg.ccU.lastBondDictList:

                if b1['aromatic_flag'] != 'Y':
                    continue

                if b1['atom_id_1'] == na_atom_id and b1['atom_id_2'][0] not in PROTON_BEGIN_CODE:
                    na_ = b1['atom_id_2']

                elif b1['atom_id_2'] == na_atom_id and b1['atom_id_1'][0] not in PROTON_BEGIN_CODE:
                    na_ = b1['atom_id_1']

                else:
                    continue

                for b2 in self._reg.ccU.lastBondDictList:

                    if b2['aromatic_flag'] != 'Y':
                        continue

                    if b2['atom_id_1'] == na_ and b2['atom_id_2'][0] not in PROTON_BEGIN_CODE\
                            and b2['atom_id_2'] != na_atom_id:
                        na__ = b2['atom_id_2']

                    elif b2['atom_id_2'] == na_ and b2['atom_id_1'][0] not in PROTON_BEGIN_CODE\
                            and b2['atom_id_1'] != na_atom_id:
                        na__ = b2['atom_id_1']

                    else:
                        continue

                    for b3 in self._reg.ccU.lastBondDictList:

                        if b3['aromatic_flag'] != 'Y':
                            continue

                        if b3['atom_id_1'] == na__ and b3['atom_id_2'][0] not in PROTON_BEGIN_CODE\
                                and b3['atom_id_2'] != na_:
                            na___ = b3['atom_id_2']

                        elif b3['atom_id_2'] == na__ and b3['atom_id_1'][0] not in PROTON_BEGIN_CODE\
                                and b3['atom_id_1'] != na_:
                            na___ = b3['atom_id_1']

                        else:
                            continue

                        half_ring_traces.append(f"{na_atom_id}:{na_}:{na__}:{na___}")

            len_half_ring_traces = len(half_ring_traces)

            if len_half_ring_traces < 2:
                self._reg.cpC['near_ring'][seq_key] = None
                return None

            ring_traces = []

            for i in range(len_half_ring_traces - 1):

                half_ring_trace_1 = half_ring_traces[i].split(':')

                for j in range(i + 1, len_half_ring_traces):

                    half_ring_trace_2 = half_ring_traces[j].split(':')

                    # hexagonal ring
                    if half_ring_trace_1[3] == half_ring_trace_2[3]:
                        ring_traces.append(f'{half_ring_traces[i]}:{half_ring_trace_2[2]}:{half_ring_trace_2[1]}')

                    # pentagonal ring
                    elif half_ring_trace_1[3] == half_ring_trace_2[2] and half_ring_trace_1[2] == half_ring_trace_2[3]:
                        ring_traces.append(f'{half_ring_traces[i]}:{half_ring_trace_2[1]}')

            if len(ring_traces) == 0:
                self._reg.cpC['near_ring'][seq_key] = None
                return None

            ring_atoms = None
            ring_trace_score = 0

            for ring_trace in ring_traces:

                _ring_atoms = ring_trace.split(':')

                score = 0

                for a in atom_list:

                    if a['chain_id'] != na['chain_id'] or a['seq_id'] != na['seq_id'] or a['comp_id'] != na['comp_id']:
                        continue

                    if a['atom_id'] in _ring_atoms:
                        score += 1

                if score > ring_trace_score:
                    ring_atoms = _ring_atoms
                    ring_trace_score = score

            try:

                _na = self._reg.cR.getDictListWithFilter('atom_site',
                                                         [{'name': 'label_atom_id', 'type': 'starts-with-alnum',
                                                           'alt_name': 'atom_id'},
                                                          {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                          {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                          {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                          {'name': model_num_name, 'type': 'int', 'alt_name': 'model_id'}
                                                          ],
                                                         [{'name': 'label_asym_id', 'type': 'str', 'value': na['cif_chain_id']},
                                                          {'name': 'label_seq_id', 'type': 'int', 'value': na['cif_seq_id']},
                                                          {'name': 'label_comp_id', 'type': 'str', 'value': na['comp_id']},
                                                          {'name': 'label_atom_id', 'type': 'enum', 'enum': ring_atoms},
                                                          {'name': 'label_alt_id', 'type': 'enum',
                                                           'enum': (self._reg.representative_alt_id,)}
                                                          ])

            except Exception as e:  # pylint: disable=broad-exception-caught

                self._reg.report.error.appendDescription('internal_error',
                                                         f"+{self.__class_name__}.__getNearestAromaticRing() "
                                                         "++ Error  - " + str(e))

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.__getNearestAromaticRing() "
                                        f"++ Error  - {str(e)}\n")

                return None

            if len(_na) == 0:
                self._reg.cpC['near_ring'][seq_key] = None
                return None

            model_ids = set(a['model_id'] for a in _na)

            len_model_ids = 0

            dist = ring_dist = ring_angle = 0.0

            for model_id in model_ids:

                rc = numpy.array([0.0] * 3, dtype=float)

                total = 0

                for a in _na:

                    if a['model_id'] == model_id:

                        _a = to_np_array(a)

                        if a['atom_id'] == na_atom_id:
                            dist += distance(_a, o)

                        rc = numpy.add(rc, _a)

                        total += 1

                if total == len(ring_atoms):

                    rc = rc / total

                    ring_dist += distance(rc, o)

                    na_ = next(to_np_array(na_) for na_ in _na if na_['atom_id'] == ring_atoms[0])
                    na__ = next(to_np_array(na__) for na__ in _na if na__['atom_id'] == ring_atoms[1])
                    na___ = next(to_np_array(na___) for na___ in _na if na___['atom_id'] == ring_atoms[-1])

                    ring_vector = numpy.cross(na__ - na_, na___ - na_)

                    ring_angle += math.acos(abs(numpy.dot(to_unit_vector(o - rc), to_unit_vector(ring_vector))))

                    len_model_ids += 1

            if len_model_ids == 0:  # DAOTHER-8840
                return None

            na['ring_atoms'] = ring_atoms
            na['distance'] = round(dist / len_model_ids, 1)
            na['ring_distance'] = round(ring_dist / len_model_ids, 1)
            na['ring_angle'] = round(numpy.degrees(ring_angle / len_model_ids), 1)

            self._reg.cpC['near_ring'][seq_key] = na
            return na

        self._reg.cpC['near_ring'][seq_key] = None
        return None

    def _getNearestParaFerroMagneticAtom(self, nmr_chain_id: str, nmr_seq_id: int, nmr_atom_id: str
                                         ) -> Optional[dict]:
        """ Return the nearest paramagnetic/ferromagnetic atom around a given atom.
            @return: the nearest paramagnetic/ferromagnetic atom
        """

        if not self._reg.cifChecked:
            return None

        if self._reg.report.isDiamagnetic():
            return None

        cif_ps = self._reg.report.getModelPolymerSequenceWithNmrChainId(nmr_chain_id)

        if cif_ps is None:
            return None

        cif_chain_id = cif_ps['chain_id']

        seq_align_dic = self._reg.report.sequence_alignment.get()

        if not has_key_value(seq_align_dic, 'nmr_poly_seq_vs_model_poly_seq'):
            return None

        seq_key = (nmr_chain_id, nmr_seq_id, nmr_atom_id)

        if seq_key in self._reg.cpC['near_para_ferro']:
            return self._reg.cpC['near_para_ferro'][seq_key]

        result = next((seq_align for seq_align in seq_align_dic['nmr_poly_seq_vs_model_poly_seq']
                       if seq_align['ref_chain_id'] == nmr_chain_id and seq_align['test_chain_id'] == cif_chain_id), None)

        if result is not None:

            cif_seq_id = next((test_seq_id for ref_seq_id, test_seq_id
                               in zip(result['ref_seq_id'], result['test_seq_id'])
                               if ref_seq_id == nmr_seq_id), None)

            if cif_seq_id is None:
                self._reg.cpC['near_para_ferro'][seq_key] = None
                return None

            try:

                model_num_name = 'pdbx_PDB_model_num' if 'pdbx_PDB_model_num' in self._reg.coord_atom_site_tags else 'ndb_model'

                _origin = self._reg.cR.getDictListWithFilter('atom_site',
                                                             [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                              {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                              {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                              ],
                                                             [{'name': 'label_asym_id', 'type': 'str', 'value': cif_chain_id},
                                                              {'name': 'label_seq_id', 'type': 'int', 'value': cif_seq_id},
                                                              {'name': 'label_atom_id', 'type': 'str', 'value': nmr_atom_id},
                                                              {'name': model_num_name, 'type': 'int',
                                                               'value': self._reg.representative_model_id},
                                                              {'name': 'label_alt_id', 'type': 'enum',
                                                               'enum': (self._reg.representative_alt_id,)}
                                                              ])

            except Exception as e:  # pylint: disable=broad-exception-caught

                self._reg.report.error.appendDescription('internal_error',
                                                         f"+{self.__class_name__}.__getNearestParaFerroMagneticAtom() "
                                                         "++ Error  - " + str(e))

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.__getNearestParaFerroMagneticAtom() "
                                        f"++ Error  - {str(e)}\n")

                return None

            if len(_origin) != 1:
                self._reg.cpC['near_para_ferro'][seq_key] = None
                return None

            o = to_np_array(_origin[0])

            try:

                _neighbor = self._reg.cR.getDictListWithFilter('atom_site',
                                                               [{'name': 'auth_asym_id', 'type': 'str',
                                                                 'alt_name': 'chain_id', 'default': REPRESENTATIVE_ASYM_ID},
                                                                {'name': 'auth_seq_id', 'type': 'int', 'alt_name': 'seq_id'},
                                                                {'name': 'label_comp_id', 'type': 'starts-with-alnum',
                                                                 'alt_name': 'comp_id'},
                                                                {'name': 'label_atom_id', 'type': 'starts-with-alnum',
                                                                 'alt_name': 'atom_id'},
                                                                {'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                                {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                                {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                                {'name': 'type_symbol', 'type': 'str'}
                                                                ],
                                                               [{'name': 'Cartn_x', 'type': 'range-float',
                                                                 'range': {'min_exclusive': (o[0] - CUTOFF_PARAMAGNETIC),
                                                                           'max_exclusive': (o[0] + CUTOFF_PARAMAGNETIC)}},
                                                                {'name': 'Cartn_y', 'type': 'range-float',
                                                                 'range': {'min_exclusive': (o[1] - CUTOFF_PARAMAGNETIC),
                                                                           'max_exclusive': (o[1] + CUTOFF_PARAMAGNETIC)}},
                                                                {'name': 'Cartn_z', 'type': 'range-float',
                                                                 'range': {'min_exclusive': (o[2] - CUTOFF_PARAMAGNETIC),
                                                                           'max_exclusive': (o[2] + CUTOFF_PARAMAGNETIC)}},
                                                                {'name': model_num_name, 'type': 'int',
                                                                 'value': self._reg.representative_model_id},
                                                                {'name': 'label_alt_id', 'type': 'enum',
                                                                 'enum': (self._reg.representative_alt_id,)}
                                                                ])

            except Exception as e:  # pylint: disable=broad-exception-caught

                self._reg.report.error.appendDescription('internal_error',
                                                         f"+{self.__class_name__}.__getNearestParaFerroMagneticAtom() "
                                                         "++ Error  - " + str(e))

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.__getNearestParaFerroMagneticAtom() "
                                        f"++ Error  - {str(e)}\n")

                return None

            if len(_neighbor) == 0:
                self._reg.cpC['near_para_ferro'][seq_key] = None
                return None

            neighbor = [n for n in _neighbor
                        if n['seq_id'] != cif_seq_id
                        and distance(to_np_array(n), o) < CUTOFF_PARAMAGNETIC
                        and (n['type_symbol'] in PARAMAGNETIC_ELEMENTS
                             or n['type_symbol'] in FERROMAGNETIC_ELEMENTS)]

            if len(neighbor) == 0:
                self._reg.cpC['near_para_ferro'][seq_key] = None
                return None

            atom_list = []

            for n in neighbor:
                atom_list.append({'chain_id': n['chain_id'], 'seq_id': n['seq_id'],
                                  'comp_id': n['comp_id'], 'atom_id': n['atom_id'],
                                  'distance': distance(to_np_array(n), o)})

            if len(atom_list) == 0:
                return None

            p = sorted(atom_list, key=itemgetter('distance'))[0]

            try:

                _p = self._reg.cR.getDictListWithFilter('atom_site',
                                                        [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                         {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                         {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'}
                                                         ],
                                                        [{'name': 'auth_asym_id', 'type': 'str', 'value': p['chain_id']},
                                                         {'name': 'auth_seq_id', 'type': 'int', 'value': p['seq_id']},
                                                         {'name': 'label_comp_id', 'type': 'str', 'value': p['comp_id']},
                                                         {'name': 'label_atom_id', 'type': 'str', 'value': p['atom_id']},
                                                         {'name': 'label_alt_id', 'type': 'enum',
                                                          'enum': (self._reg.representative_alt_id,)}
                                                         ])

            except Exception as e:  # pylint: disable=broad-exception-caught

                self._reg.report.error.appendDescription('internal_error',
                                                         f"+{self.__class_name__}.__getNearestParaFerroMagneticAtom() "
                                                         "++ Error  - " + str(e))

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.__getNearestParaFerroMagneticAtom() "
                                        f"++ Error  - {str(e)}\n")

                return None

            if len(_p) == 0:
                self._reg.cpC['near_para_ferro'][seq_key] = None
                return None

            dist = 0.0

            for __p in _p:
                dist += distance(to_np_array(__p), o)

            p['distance'] = round(dist / len(_p), 1)

            self._reg.cpC['near_para_ferro'][seq_key] = p
            return p

        self._reg.cpC['near_para_ferro'][seq_key] = None
        return None
