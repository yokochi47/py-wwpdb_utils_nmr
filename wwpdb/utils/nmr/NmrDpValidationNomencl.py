##
# File: NmrDpValidationNomencl.py
# Date: 17-Aug-2026
#
# Updates:
##
""" Atom nomenclature validation for NMR data validation.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.2"

from typing import Union

import pynmrstar

try:
    from wwpdb.utils.nmr.NmrDpConstant import (AUX_LP_CATEGORIES,
                                               EMPTY_VALUE,
                                               STD_MON_DICT,
                                               PSE_PRO_BEGIN_CODE,
                                               PARAMAGNETIC_ELEMENTS,
                                               FERROMAGNETIC_ELEMENTS,
                                               ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS)
    from wwpdb.utils.nmr.CifToNmrStar import get_first_sf_tag
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (translateToStdResName,
                                                       translateToStdAtomName)
    from wwpdb.utils.nmr.NmrDpValidationBase import NmrDpValidationBase
except ImportError:
    from nmr.NmrDpConstant import (AUX_LP_CATEGORIES,
                                   EMPTY_VALUE,
                                   STD_MON_DICT,
                                   PSE_PRO_BEGIN_CODE,
                                   PARAMAGNETIC_ELEMENTS,
                                   FERROMAGNETIC_ELEMENTS,
                                   ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS)
    from nmr.CifToNmrStar import get_first_sf_tag
    from nmr.mr.ParserListenerUtil import (translateToStdResName,
                                           translateToStdAtomName)
    from nmr.NmrDpValidationBase import NmrDpValidationBase


class NmrDpValidationNomencl(NmrDpValidationBase):
    """ Atom nomenclature validation for NMR data validation.
    """
    __slots__ = ()

    def validateAtomNomenclature(self, file_name: str, file_type: str, content_subtype: str,
                                 sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                                 sf_framecode: str, lp_category: str) -> None:
        """ Validate atom nomenclature using NefTranslator and CCD.
        """

        try:

            if file_type == 'nef':  # DAOTHER-7389, issue #3, allow empty for 'chem_shift'
                pairs = self._reg.nefT.get_nef_comp_atom_pair(sf, lp_category,
                                                              allow_empty=content_subtype in ('chem_shift', 'spectral_peak'))[0]
            else:  # DAOTHER-7389, issue #3, allow empty for 'chem_shift'
                pairs = self._reg.nefT.get_star_comp_atom_pair(sf, lp_category,
                                                               allow_empty=content_subtype in ('chem_shift', 'spectral_peak'))[0]

            for pair in pairs:
                comp_id = pair['comp_id']
                atom_ids = pair['atom_id']

                # standard residue
                if comp_id in STD_MON_DICT:

                    if file_type == 'nef':

                        _atom_ids = []
                        for atom_id in atom_ids:

                            if atom_id in EMPTY_VALUE:
                                continue

                            _atom_id = self._reg.nefT.get_star_atom(comp_id, atom_id, leave_unmatched=False)[0]

                            if len(_atom_id) == 0:

                                if self._reg.nonblk_bad_nterm and self._reg.csStat.peptideLike(comp_id)\
                                   and atom_id in ('H1', 'H2', 'H3', 'HT1', 'HT2', 'HT3'):
                                    continue

                                if self._reg.remediation_mode and atom_id[0] in ('Q', 'M'):  # DAOTHER-8663, 8751
                                    continue

                                if self._reg.remediation_mode and self._reg.csStat.getTypeOfCompId(comp_id)[1]\
                                   and atom_id == "HO5'":
                                    continue

                                err = f"Invalid atom name {atom_id!r} (comp_id {comp_id!r}) in a loop {lp_category}."

                                self._reg.report.error.appendDescription('invalid_atom_nomenclature',
                                                                         {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                          'category': lp_category, 'description': err})

                                if self._reg.verbose:
                                    self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                                        f"++ Error  - {err}\n")

                            else:
                                _atom_ids.extend(_atom_id)

                        atom_ids = sorted(set(_atom_ids))

                    for atom_id in atom_ids:

                        if atom_id in EMPTY_VALUE:
                            continue

                        if self._reg.remediation_mode and atom_id[0] in ('Q', 'M'):  # DAOTHER-8663, 8751
                            continue

                        if self._reg.csStat.peptideLike(comp_id):
                            if atom_id.upper() == 'HN':
                                self._reg.dpR.fixAtomNomenclature(comp_id, {atom_id: 'H'})
                                continue
                            if atom_id.upper() == 'CO':
                                self._reg.dpR.fixAtomNomenclature(comp_id, {atom_id: 'C'})
                                continue

                            _atom_id = self._reg.nefT.get_star_atom(comp_id,
                                                                    translateToStdAtomName(atom_id, comp_id, ccU=self._reg.ccU),
                                                                    leave_unmatched=False)[0]
                            if len(_atom_id) == 1 and atom_id != _atom_id[0]:
                                self._reg.dpR.fixAtomNomenclature(comp_id, {atom_id: _atom_id[0]})
                                continue

                        elif len(atom_id) > 2 and atom_id.endswith('"') and atom_id[-2].isdigit():  # 7zew, 7zex: H5" -> H5''
                            self._reg.dpR.fixAtomNomenclature(comp_id, {atom_id: f"{atom_id[:-1]}''"})
                            continue

                        atom_id_ = atom_id

                        if (file_type == 'nef' or not self._reg.combined_mode or self._reg.transl_pseudo_name)\
                           and self.isNmrAtomName(comp_id, atom_id):
                            atom_id_ = self.getRepAtomId(comp_id, atom_id)

                            if file_type == 'nmr-star' and self._reg.combined_mode and self._reg.transl_pseudo_name\
                               and atom_id != atom_id_\
                               and not content_subtype.startswith('spectral_peak'):

                                warn = f"Conventional pseudoatom name {comp_id}:{atom_id} is translated to {atom_id_!r} "\
                                    "according to the IUPAC atom nomenclature."

                                self._reg.report.warning.appendDescription('auth_atom_nomenclature_mismatch',
                                                                           {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                            'category': lp_category, 'description': warn})

                                if self._reg.verbose:
                                    self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                                        f"++ Warning  - {warn}\n")

                                self._reg.dpR.fixAtomNomenclature(comp_id, {atom_id: atom_id_})

                        if not self._reg.nefT.validate_comp_atom(comp_id, atom_id_):

                            if self._reg.csStat.peptideLike(comp_id) and atom_id_.startswith('H') and atom_id_.endswith('1')\
                               and self._reg.nefT.validate_comp_atom(comp_id, f'{atom_id_[:-1]}2')\
                               and self._reg.nefT.validate_comp_atom(comp_id, f'{atom_id_[:-1]}3')\
                               and not content_subtype.startswith('spectral_peak'):

                                _atom_id_ = atom_id_[:-1]
                                _atom_id_1 = f'{_atom_id_}1'
                                _atom_id_2 = f'{_atom_id_}2'
                                _atom_id_3 = f'{_atom_id_}3'

                                warn = f"{comp_id}:{_atom_id_1}/{_atom_id_2} should be {comp_id}:{_atom_id_3}/{_atom_id_2} "\
                                    "according to the IUPAC atom nomenclature, respectively."

                                self._reg.report.warning.appendDescription('auth_atom_nomenclature_mismatch',
                                                                           {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                            'category': lp_category, 'description': warn})

                                if self._reg.verbose:
                                    self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                                        f"++ Warning  - {warn}\n")

                                # @see: https://bmrb.io/ref_info/atom_nom.tbl
                                self._reg.dpR.fixAtomNomenclature(comp_id, {_atom_id_1: _atom_id_3})

                            elif self._reg.nonblk_bad_nterm and self._reg.csStat.peptideLike(comp_id)\
                                    and atom_id in ('H1', 'H2', 'H3', 'HT1', 'HT2', 'HT3'):
                                pass

                            elif self._reg.remediation_mode and atom_id[0] in ('Q', 'M'):  # DAOTHER-8663, 8751
                                pass

                            elif self._reg.remediation_mode and self._reg.csStat.getTypeOfCompId(comp_id)[1]\
                                    and atom_id == "HO5'":
                                pass

                            else:
                                is_valid, cc_name, cc_rel_status = self.getChemCompNameAndStatusOf(comp_id)

                                if is_valid:
                                    if cc_rel_status != 'REL':
                                        cc_name = f"(Not available due to CCD status code {cc_rel_status})"
                                cc_name = '' if cc_name is None else ', ' + cc_name

                                if content_subtype.startswith('spectral_peak')\
                                   or (self._reg.csStat.peptideLike(comp_id)
                                       and atom_id in ('H1', 'H2', 'H3', 'HT1', 'HT2', 'HT3')):

                                    err = f"Unmatched atom name {atom_id!r} (comp_id {comp_id!r}{cc_name}) in a loop {lp_category}."

                                    self._reg.report.warning.appendDescription('atom_nomenclature_mismatch',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': err})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                                            f"++ Warning  - {err}\n")

                                else:

                                    err = f"Invalid atom name {atom_id!r} (comp_id {comp_id!r}{cc_name}) in a loop {lp_category}."

                                    if self._reg.remediation_mode and len(self.getAtomIdListInXplor(comp_id, atom_id)) > 0:

                                        self._reg.report.warning.appendDescription('atom_nomenclature_mismatch',
                                                                                   {'file_name': file_name,
                                                                                    'sf_framecode': sf_framecode,
                                                                                    'category': lp_category, 'description': err})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                                                f"++ Warning  - {err}\n")

                                    else:

                                        self._reg.report.error.appendDescription('invalid_atom_nomenclature',
                                                                                 {'file_name': file_name,
                                                                                  'sf_framecode': sf_framecode,
                                                                                  'category': lp_category, 'description': err})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                                                f"++ Error  - {err}\n")

                # non-standard residue
                else:

                    if self._reg.ccU.updateChemCompDict(comp_id):  # matches with comp_id in CCD

                        ref_atom_ids = [a['atom_id'] for a in self._reg.ccU.lastAtomDictList]
                        # if a['leaving_atom_flag'] != 'Y']
                        unk_atom_ids = []

                        for atom_id in atom_ids:

                            if atom_id in EMPTY_VALUE:
                                continue

                            if file_type == 'nef':
                                _atom_id = self._reg.nefT.get_star_atom(comp_id, atom_id, leave_unmatched=False)[0]
                                if len(_atom_id) > 0:
                                    atom_id = _atom_id[0]

                            if atom_id not in ref_atom_ids:

                                if self._reg.remediation_mode and atom_id[0] in ('Q', 'M'):  # DAOTHER-8663, 8751
                                    continue

                                unk_atom_ids.append(atom_id)

                        if len(unk_atom_ids) > 0:
                            is_valid, cc_name, cc_rel_status = self.getChemCompNameAndStatusOf(comp_id)

                            if is_valid:
                                if cc_rel_status != 'REL':
                                    cc_name = f"(Not available due to CCD status code {cc_rel_status})"
                            cc_name = '' if cc_name is None else ', ' + cc_name

                            warn = f"Unknown atom_id {unk_atom_ids!r} (comp_id {comp_id!r}{cc_name})."

                            self._reg.report.warning.appendDescription('atom_nomenclature_mismatch',
                                                                       {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                        'category': lp_category, 'description': warn})

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                                    f"++ Warning  - {warn}\n")

                        ref_elems = set(a['type_symbol'] for a in self._reg.ccU.lastAtomDictList
                                        if a['leaving_atom_flag'] != 'Y')

                        for elem in ref_elems:
                            if elem in PARAMAGNETIC_ELEMENTS or elem in FERROMAGNETIC_ELEMENTS:
                                self._reg.report.setDiamagnetic(False)
                                break

                        for atom_id in atom_ids:

                            if atom_id in EMPTY_VALUE:
                                continue

                            if self._reg.remediation_mode and atom_id[0] in ('Q', 'M'):  # DAOTHER-8663, 8751
                                continue

                            if self._reg.csStat.peptideLike(comp_id):
                                if atom_id.upper() == 'HN':
                                    self._reg.dpR.fixAtomNomenclature(comp_id, {atom_id: 'H'})
                                    continue
                                if atom_id.upper() == 'CO':
                                    self._reg.dpR.fixAtomNomenclature(comp_id, {atom_id: 'C'})
                                    continue

                            elif len(atom_id) > 2 and atom_id.endswith('"') and atom_id[-2].isdigit():  # 7zew, 7zex: H5" -> H5''
                                self._reg.dpR.fixAtomNomenclature(comp_id, {atom_id: f"{atom_id[:-1]}''"})
                                continue

                            atom_id_ = atom_id

                            if (file_type == 'nef' or not self._reg.combined_mode or self._reg.transl_pseudo_name)\
                               and self.isNmrAtomName(comp_id, atom_id) and not content_subtype.startswith('spectral_peak'):
                                atom_id_ = self.getRepAtomId(comp_id, atom_id)

                                if file_type == 'nmr-star' and self._reg.combined_mode and self._reg.transl_pseudo_name\
                                   and atom_id != atom_id_:

                                    warn = f"Conventional pseudoatom name {comp_id}:{atom_id} is translated to {atom_id_!r} "\
                                        "according to the IUPAC atom nomenclature."

                                    self._reg.report.warning.appendDescription('auth_atom_nomenclature_mismatch',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': warn})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                                            f"++ Warning  - {warn}\n")

                                    self._reg.dpR.fixAtomNomenclature(comp_id, {atom_id: atom_id_})

                    else:
                        pass

            if file_type == 'nmr-star':

                try:

                    peptide_only = all(len(pair['comp_id']) == 3 and pair['comp_id'] in STD_MON_DICT for pair in pairs)

                    auth_pairs = self._reg.nefT.get_star_auth_comp_atom_pair(sf, lp_category)[0]

                    for auth_pair in auth_pairs:
                        auth_comp_id = auth_pair['comp_id']
                        if peptide_only and len(auth_comp_id) == 1:
                            comp_id = next((k for k, v in STD_MON_DICT.items() if v == auth_comp_id), auth_comp_id)
                        else:
                            comp_id = auth_comp_id
                        comp_id = translateToStdResName(comp_id, ccU=self._reg.ccU)
                        auth_atom_ids = auth_pair['atom_id']

                        # standard residue
                        if comp_id in STD_MON_DICT:

                            self._reg.ccU.updateChemCompDict(comp_id)
                            ref_atom_ids = [a['atom_id'] for a in self._reg.ccU.lastAtomDictList]

                            _auth_atom_ids = []
                            for auth_atom_id in auth_atom_ids:

                                if auth_atom_id in EMPTY_VALUE:
                                    continue

                                _auth_atom_id = translateToStdAtomName(auth_atom_id, comp_id, ref_atom_ids, ccU=self._reg.ccU)

                                auth_atom_ids = self.getAtomIdList(comp_id, _auth_atom_id)

                                if len(auth_atom_ids) > 0:
                                    _auth_atom_ids.extend(auth_atom_ids)

                                else:

                                    if self._reg.nonblk_bad_nterm and self._reg.csStat.peptideLike(comp_id)\
                                       and _auth_atom_id in ('H1', 'H2', 'H3', 'HT1', 'HT2', 'HT3'):
                                        continue

                                    if self._reg.remediation_mode and _auth_atom_id[0] in ('Q', 'M'):  # DAOTHER-8663, 8751
                                        continue

                                    if self._reg.remediation_mode and self._reg.csStat.getTypeOfCompId(comp_id)[1]\
                                       and atom_id == "HO5'":
                                        continue

                                    auth_atom_ids = self.getAtomIdListInXplor(comp_id, _auth_atom_id)

                                    if len(auth_atom_ids) > 0:
                                        _auth_atom_ids.extend(auth_atom_ids)

                                    else:

                                        warn = f"Unmatched Auth_atom_ID {auth_atom_id!r} (Auth_comp_ID {auth_comp_id})."

                                        self._reg.report.warning.appendDescription('auth_atom_nomenclature_mismatch',
                                                                                   {'file_name': file_name,
                                                                                    'sf_framecode': sf_framecode,
                                                                                    'category': lp_category, 'description': warn})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                                                f"++ Warning  - {warn}\n")

                            auth_atom_ids = sorted(set(_auth_atom_ids))

                            for auth_atom_id in auth_atom_ids:

                                if auth_atom_id in EMPTY_VALUE:
                                    continue

                                if not self._reg.nefT.validate_comp_atom(comp_id,
                                                                         translateToStdAtomName(auth_atom_id, comp_id,
                                                                                                ref_atom_ids,
                                                                                                ccU=self._reg.ccU)):

                                    if self._reg.nonblk_bad_nterm and self._reg.csStat.peptideLike(comp_id)\
                                       and auth_atom_id in ('H1', 'H2', 'H3', 'HT1', 'HT2', 'HT3'):
                                        continue

                                    if self._reg.remediation_mode and auth_atom_id[0] in ('Q', 'M'):  # DAOTHER-8663, 8751
                                        continue

                                    if self._reg.remediation_mode and self._reg.csStat.getTypeOfCompId(comp_id)[1]\
                                       and atom_id == "HO5'":
                                        continue

                                    warn = f"Unmatched Auth_atom_ID {auth_atom_id!r} (Auth_comp_ID {auth_comp_id})."

                                    self._reg.report.warning.appendDescription('auth_atom_nomenclature_mismatch',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': warn})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                                            f"++ Warning  - {warn}\n")

                        # non-standard residue
                        else:
                            has_comp_id = False

                            for pair in pairs:

                                if pair['comp_id'] != comp_id:
                                    continue

                                has_comp_id = True

                                atom_ids = pair['atom_id']

                                if (set(auth_atom_ids) | set(atom_ids)) != set(atom_ids):

                                    for auth_atom_id in (set(auth_atom_ids) | set(atom_ids)) - set(atom_ids):

                                        if auth_atom_id in EMPTY_VALUE:
                                            continue

                                        if self._reg.nonblk_bad_nterm and self._reg.csStat.peptideLike(comp_id)\
                                           and auth_atom_id in ('H1', 'H2', 'H3', 'HT1', 'HT2', 'HT3'):
                                            continue

                                        if self._reg.remediation_mode and auth_atom_id[0] in ('Q', 'M'):  # DAOTHER-8663, 8751
                                            continue

                                        if self._reg.remediation_mode and self._reg.csStat.getTypeOfCompId(comp_id)[1]\
                                           and atom_id == "HO5'":
                                            continue

                                        warn = f"Unmatched Auth_atom_ID {auth_atom_id!r} "\
                                            f"(Auth_comp_ID {comp_id}, non-standard residue)."

                                        self._reg.report.warning.appendDescription('auth_atom_nomenclature_mismatch',
                                                                                   {'file_name': file_name,
                                                                                    'sf_framecode': sf_framecode,
                                                                                    'category': lp_category, 'description': warn})

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                                                f"++ Warning  - {warn}\n")

                                break

                            if not has_comp_id:

                                for auth_atom_id in auth_atom_ids:

                                    if auth_atom_id in EMPTY_VALUE:
                                        continue

                                    if self._reg.nonblk_bad_nterm and self._reg.csStat.peptideLike(comp_id)\
                                       and auth_atom_id in ('H1', 'H2', 'H3', 'HT1', 'HT2', 'HT3'):
                                        continue

                                    if self._reg.remediation_mode and auth_atom_id[0] in ('Q', 'M'):  # DAOTHER-8663, 8751
                                        continue

                                    if self._reg.remediation_mode and self._reg.csStat.getTypeOfCompId(comp_id)[1]\
                                       and atom_id == "HO5'":
                                        continue

                                    warn = f"Unmatched Auth_atom_ID {auth_atom_id!r} "\
                                        f"(Auth_comp_ID {comp_id}, non-standard residue)."

                                    self._reg.report.warning.appendDescription('auth_atom_nomenclature_mismatch',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': warn})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                                            f"++ Warning  - {warn}\n")

                except LookupError:
                    # """
                    # self._reg.report.error.appendDescription('missing_mandatory_item',
                    #                                           {'file_name': file_name, 'sf_framecode': sf_framecode,
                    #                                            'category': lp_category, 'description': str(e).strip("'")})
                    #
                    # self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                    #                      f"++ LookupError  - {file_name} {sf_framecode} {lp_category} {str(e)}\n")
                    # """
                    pass

                except ValueError as e:

                    self._reg.report.error.appendDescription('invalid_data',
                                                             {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                              'category': lp_category, 'description': str(e).strip("'")})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                            f"++ ValueError  - {str(e)}\n")

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
                                self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                                    f"++ ValueError  - {err}\n")

                        else:

                            self._reg.report.error.appendDescription('internal_error',
                                                                     f"+{self.__class_name__}.validateAtomNomenclature() "
                                                                     "++ Error  - " + err)

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                                    f"++ Error  - {err}\n")

                except Exception as e:  # pylint: disable=broad-exception-caught

                    self._reg.report.error.appendDescription('internal_error',
                                                             f"+{self.__class_name__}.validateAtomNomenclature() "
                                                             "++ Error  - " + str(e))

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                            f"++ Error  - {str(e)}\n")

        except LookupError as e:

            self._reg.report.error.appendDescription('missing_mandatory_item',
                                                     {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                      'category': lp_category, 'description': str(e).strip("'")})

            self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                f"++ LookupError  - {file_name} {sf_framecode} {lp_category} {str(e)}\n")

        except ValueError as e:

            self._reg.report.error.appendDescription('invalid_data',
                                                     {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                      'category': lp_category, 'description': str(e).strip("'")})

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                    f"++ ValueError  - {str(e)}\n")

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
                        self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                            f"++ ValueError  - {err}\n")

                else:

                    self._reg.report.error.appendDescription('internal_error',
                                                             f"+{self.__class_name__}.validateAtomNomenclature() "
                                                             "++ Error  - " + err)

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                            f"++ Error  - {err}\n")

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.validateAtomNomenclature() "
                                                     "++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.validateAtomNomenclature() "
                                    f"++ Error  - {str(e)}\n")

    def validateAtomTypeOfCsLoop(self, file_name: str, file_type: str,
                                 sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                                 sf_framecode: str, lp_category: str) -> None:
        """ Validate atom type, isotope number on assigned chemical shifts.
        """

        if not self._reg.combined_mode:
            return

        try:

            # DAOTHER-7389, issue #3, allow empty for 'chem_shift'
            if file_type == 'nef':
                a_types = self._reg.nefT.get_nef_atom_type_from_cs_loop(sf, allow_empty=True)[0]
            else:
                a_types = self._reg.nefT.get_star_atom_type_from_cs_loop(sf, allow_empty=True)[0]

            for a_type in a_types:
                atom_type = a_type['atom_type']
                isotope_nums = a_type['isotope_number']
                atom_ids = a_type['atom_id']

                if atom_type not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS.keys():

                    err = f"Invalid atom_type {atom_type!r} in a loop {lp_category}."

                    self._reg.report.error.appendDescription('invalid_atom_type',
                                                             {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                              'category': lp_category, 'description': err})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.validateAtomTypeOfCsLoop() ++ Error  - {err}\n")

                else:

                    for isotope_num in isotope_nums:
                        if isotope_num not in ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS[atom_type]:

                            err = f"Invalid isotope number {str(isotope_num)!r} (atom_type {atom_type}, "\
                                f"allowed isotope number {ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS[atom_type]}) in a loop {lp_category}."

                            self._reg.report.error.appendDescription('invalid_isotope_number',
                                                                     {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                      'category': lp_category, 'description': err})

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.validateAtomTypeOfCsLoop() ++ Error  - {err}\n")

                    for atom_id in atom_ids:
                        if not atom_id.startswith(atom_type):

                            if self._reg.remediation_mode and 1 in isotope_nums\
                               and atom_id[0] in PSE_PRO_BEGIN_CODE:  # DAOTHER-8663, 8751, 9520
                                continue

                            err = f"Invalid atom name {atom_id!r} (atom_type {atom_type!r}) in a loop {lp_category}."

                            self._reg.report.error.appendDescription('invalid_atom_nomenclature',
                                                                     {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                      'category': lp_category, 'description': err})

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.validateAtomTypeOfCsLoop() ++ Error  - {err}\n")

        except LookupError as e:

            if not self._reg.resolve_conflict:
                self._reg.report.error.appendDescription('missing_mandatory_item',
                                                         {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                          'category': lp_category, 'description': str(e).strip("'")})

                self._reg.log.write(f"+{self.__class_name__}.validateAtomTypeOfCsLoop() ++ LookupError  - "
                                    f"{file_name} {sf_framecode} {lp_category} {str(e)}\n")

        except ValueError as e:

            self._reg.report.error.appendDescription('invalid_data',
                                                     {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                      'category': lp_category, 'description': str(e).strip("'")})

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.validateAtomTypeOfCsLoop() ++ ValueError  - {str(e)}\n")

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
                        self._reg.log.write(f"+{self.__class_name__}.validateAtomTypeOfCsLoop() ++ ValueError  - {err}\n")

                else:

                    self._reg.report.error.appendDescription('internal_error',
                                                             f"+{self.__class_name__}.validateAtomTypeOfCsLoop() "
                                                             "++ Error  - " + err)

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.validateAtomTypeOfCsLoop() ++ Error  - {err}\n")

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.validateAtomTypeOfCsLoop() ++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.validateAtomTypeOfCsLoop() ++ Error  - {str(e)}\n")

    def validateAmbigCodeOfCsLoop(self, file_name: str,
                                  sf: Union[pynmrstar.Saveframe, pynmrstar.Loop],
                                  sf_framecode: str, lp_category: str) -> bool:
        """ Validate ambiguity code on assigned chemical shifts.
        """

        try:

            need_set_id = False
            valid = True

            a_codes = self._reg.nefT.get_star_ambig_code_from_cs_loop(sf)[0]

            comp_ids_wo_ambig_code = []

            for a_code in a_codes:
                comp_id = a_code['comp_id']
                ambig_code = a_code['ambig_code']
                atom_ids = a_code['atom_id']

                if ambig_code is None:
                    comp_ids_wo_ambig_code.append(comp_id)

                elif ambig_code == 1 or ambig_code >= 4:
                    need_set_id |= ambig_code in (4, 5, 6, 9)

                # ambig_code is 2 (geminal atoms) or 3 (aromatic ring atoms in opposite side)
                else:

                    for atom_id in atom_ids:

                        _atom_id = atom_id

                        if self.isNmrAtomName(comp_id, atom_id):
                            _atom_id = self.getRepAtomId(comp_id, atom_id)

                        allowed_ambig_code = self._reg.csStat.getMaxAmbigCodeWoSetId(comp_id, _atom_id)

                        if ambig_code > allowed_ambig_code > 0:

                            if allowed_ambig_code < 1:

                                if self._reg.remediation_mode:
                                    pass

                                else:

                                    warn = f"Ambiguity code {str(ambig_code)!r} (comp_id {comp_id}, atom_id {atom_id}) "\
                                        "should be '1' according to the BMRB definition."

                                    self._reg.report.warning.appendDescription('ambiguity_code_mismatch',
                                                                               {'file_name': file_name,
                                                                                'sf_framecode': sf_framecode,
                                                                                'category': lp_category, 'description': warn})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() "
                                                            f"++ Warning  - {warn}\n")

                                    valid = False

                            else:

                                if self._reg.remediation_mode:
                                    pass

                                else:

                                    err = f"Invalid ambiguity code {str(ambig_code)!r} (comp_id {comp_id}, atom_id {atom_id}, "\
                                        f"allowed ambig_code {[1, allowed_ambig_code, 4, 5, 6, 9]}) in a loop {lp_category}."

                                    self._reg.report.error.appendDescription('invalid_ambiguity_code',
                                                                             {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                              'category': lp_category, 'description': err})

                                    if self._reg.verbose:
                                        self._reg.log.write(f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() "
                                                            f"++ Error  - {err}\n")

                                    valid = False

            if len(comp_ids_wo_ambig_code) > 0:

                warn = f"Missing ambiguity code for the following residues {comp_ids_wo_ambig_code}."

                self._reg.report.warning.appendDescription('missing_data',
                                                           {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                            'category': lp_category, 'description': warn})

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() ++ Warning  - {warn}\n")

                valid = False

            if need_set_id and valid:

                list_id = get_first_sf_tag(sf, 'ID')

                try:

                    lp = sf.get_loop(lp_category)

                    ambig_code_col = lp.tags.index('Ambiguity_code')
                    ambig_set_id_col = lp.tags.index('Ambiguity_set_ID')

                    id_col = lp.tags.index('ID')
                    chain_id_col = lp.tags.index('Entity_assembly_ID')
                    seq_id_col = lp.tags.index('Comp_index_ID')
                    atom_type_col = lp.tags.index('Atom_type')

                    aux_lp_category = AUX_LP_CATEGORIES['nmr-star']['chem_shift'][0]

                    if any(True for aux_loop in sf if aux_loop.category == aux_lp_category):

                        aux_loop = sf.get_loop(aux_lp_category)

                        del sf[aux_loop]

                    aux_lp = pynmrstar.Loop.from_scratch(aux_lp_category)

                    aux_items = ['Ambiguous_shift_set_ID', 'Atom_chem_shift_ID', 'Entry_ID', 'Assigned_chem_shift_list_ID']

                    aux_tags = [f'{aux_lp_category}.{item}' for item in aux_items]

                    aux_lp.add_tag(aux_tags)

                    inter_residue_seq_id = {}

                    for _row in lp:

                        ambig_code = _row[ambig_code_col]

                        if ambig_code in EMPTY_VALUE:
                            continue

                        if isinstance(ambig_code, str):
                            ambig_code = int(ambig_code)

                        if ambig_code not in (5, 6, 9):
                            continue

                        chain_id = _row[chain_id_col]
                        seq_id = _row[seq_id_col]

                        if chain_id not in inter_residue_seq_id:
                            inter_residue_seq_id[chain_id] = set()

                        inter_residue_seq_id[chain_id].add(seq_id)

                    aux_index_id = 0
                    ambig_shift_set_id = {}

                    for _idx, _row in enumerate(lp):

                        ambig_code = _row[ambig_code_col]

                        if ambig_code in EMPTY_VALUE:
                            continue

                        if isinstance(ambig_code, str):
                            ambig_code = int(ambig_code)

                        if ambig_code not in (4, 5):
                            continue

                        chain_id = _row[chain_id_col]
                        seq_id = _row[seq_id_col]
                        atom_type = _row[atom_type_col]

                        if ambig_code == 4:
                            key = (chain_id, str(seq_id), atom_type, ambig_code)
                        else:
                            key = (chain_id, str(inter_residue_seq_id[chain_id]), atom_type, ambig_code)

                        if key not in ambig_shift_set_id:
                            aux_index_id += 1
                            ambig_shift_set_id[key] = aux_index_id

                        lp.data[_idx][ambig_set_id_col] = ambig_shift_set_id[key]

                        _aux_row = [None] * 4
                        _aux_row[0], _aux_row[1], _aux_row[2], _aux_row[3] =\
                            ambig_shift_set_id[key], _row[id_col], self._reg.entry_id, list_id

                        aux_lp.add_data(_aux_row)

                    if len(aux_lp) > 0:
                        sf.add_loop(aux_lp)
                        return True

                except (KeyError, IndexError, ValueError):
                    pass

        except LookupError as e:

            if not self._reg.resolve_conflict:
                self._reg.report.error.appendDescription('missing_mandatory_item',
                                                         {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                          'category': lp_category, 'description': str(e).strip("'")})

                self._reg.log.write(f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() ++ LookupError  - "
                                    f"{file_name} {sf_framecode} {lp_category} {str(e)}\n")

        except ValueError as e:

            self._reg.report.error.appendDescription('invalid_data',
                                                     {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                      'category': lp_category, 'description': str(e).strip("'")})

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() ++ ValueError  - {str(e)}\n")

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
                        self._reg.log.write(f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() ++ ValueError  - {err}\n")

                else:

                    self._reg.report.error.appendDescription('internal_error',
                                                             f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() "
                                                             "++ Error  - " + err)

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() ++ Error  - {err}\n")

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() ++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.validateAmbigCodeOfCsLoop() ++ Error  - {str(e)}\n")

        return False
