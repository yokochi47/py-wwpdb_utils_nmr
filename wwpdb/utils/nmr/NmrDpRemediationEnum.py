##
# File: NmrDpRemediationEnum.py
# Date: 17-Aug-2026
#
# Updates:
##
""" Remediation of enumeration failures in NMR data.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.3"

import collections
import re
from typing import List

try:
    from wwpdb.utils.nmr.NmrDpConstant import (SF_CATEGORIES,
                                               LP_CATEGORIES,
                                               DATA_ITEMS,
                                               POTENTIAL_ITEMS,
                                               ITEM_NAMES_IN_CS_LOOP,
                                               ITEM_NAMES_IN_DIST_LOOP,
                                               ITEM_NAMES_IN_DIHED_LOOP,
                                               EMPTY_VALUE,
                                               PROTON_BEGIN_CODE,
                                               CHK_DESC_PAT,
                                               CHK_DESC_ONE_PAT,
                                               CHK_DESC_MAND_PAT,
                                               CHK_DESC_MAND_ONE_PAT)
    from wwpdb.utils.nmr.NmrDpValidationBase import is_like_planality_boundary
    from wwpdb.utils.nmr.CifToNmrStar import (has_key_value,
                                              get_first_sf_tag)
    from wwpdb.utils.nmr.mr.ParserListenerUtil import getTypeOfDihedralRestraint
    from wwpdb.utils.nmr.NmrDpRemediationBase import NmrDpRemediationBase
except ImportError:
    from nmr.NmrDpConstant import (SF_CATEGORIES,
                                   LP_CATEGORIES,
                                   DATA_ITEMS,
                                   POTENTIAL_ITEMS,
                                   ITEM_NAMES_IN_CS_LOOP,
                                   ITEM_NAMES_IN_DIST_LOOP,
                                   ITEM_NAMES_IN_DIHED_LOOP,
                                   EMPTY_VALUE,
                                   PROTON_BEGIN_CODE,
                                   CHK_DESC_PAT,
                                   CHK_DESC_ONE_PAT,
                                   CHK_DESC_MAND_PAT,
                                   CHK_DESC_MAND_ONE_PAT)
    from nmr.NmrDpValidationBase import is_like_planality_boundary
    from nmr.CifToNmrStar import (has_key_value,
                                  get_first_sf_tag)
    from nmr.mr.ParserListenerUtil import getTypeOfDihedralRestraint
    from nmr.NmrDpRemediationBase import NmrDpRemediationBase


class NmrDpRemediationEnum(NmrDpRemediationBase):
    """ Remediation of enumeration failures in NMR data.
    """
    __slots__ = ()

    def fixEnumerationFailure(self, warnings) -> bool:
        """ Fix enumeration failures if possible.
        """

        if not self._reg.combined_mode:
            return True

        if len(self._reg.star_data) == 0:
            return False

        input_source = self._reg.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        if warnings is None:
            return True

        for w in warnings:

            if "be one of" not in w['description']:
                continue

            if w['description'].startswith('The mandatory type'):
                try:
                    g = CHK_DESC_MAND_PAT.search(w['description']).groups()
                except AttributeError:
                    g = CHK_DESC_MAND_ONE_PAT.search(w['description']).groups()
                mandatory_tag = True
            else:
                try:
                    g = CHK_DESC_PAT.search(w['description']).groups()
                except AttributeError:
                    g = CHK_DESC_ONE_PAT.search(w['description']).groups()
                mandatory_tag = False

            itName = g[0]
            itValue = None if g[1] in EMPTY_VALUE else g[1]
            itEnum = [str(e.strip("'")) for e in re.sub(r"\', \'", "\',\'", g[2]).split(',')]

            if self._reg.star_data_type[0] == 'Entry' or self._reg.star_data_type[0] == 'Saveframe':

                if 'sf_framecode' not in w:

                    err = "Could not specify 'sf_framecode' in NMR data processing report."

                    self._reg.report.error.appendDescription('internal_error',
                                                             f"+{self.__class_name__}.fixEnumerationFailure() ++ Error  - " + err)

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.fixEnumerationFailure() ++ Error  - {err}\n")

                else:

                    sf = self._reg.dpA.getSaveframeByName(0, w['sf_framecode'])

                    if sf is None:

                        err = f"Could not specify {w['sf_framecode']!r} saveframe unexpectedly in {file_name!r} file."

                        self._reg.report.error.appendDescription('internal_error',
                                                                 f"+{self.__class_name__}.fixEnumerationFailure() "
                                                                 "++ Error  - " + err)

                        if self._reg.verbose:
                            self._reg.log.write(f"+{self.__class_name__}.fixEnumerationFailure() ++ Error  - {err}\n")

                        continue

                    if 'category' not in w:

                        tagNames = [t[0] for t in sf.tags]

                        if itName not in tagNames:

                            err = f"Could not find saveframe tag {itName} in {w['sf_framecode']!r} saveframe, {file_name!r} file."

                            self._reg.report.error.appendDescription('internal_error',
                                                                     f"+{self.__class_name__}.fixEnumerationFailure() "
                                                                     "++ Error  - " + err)

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.fixEnumerationFailure() ++ Error  - {err}\n")

                        else:

                            itCol = tagNames.index(itName)

                            val = sf.tags[itCol][1]
                            if val in EMPTY_VALUE:
                                val = None

                            if val is itValue or val == itValue:

                                undefined_enums = ('undefined', 'unknown')

                                # assumes 'undefined', 'unknown' enum values at the end of the array
                                if (len(itEnum) == 2 and itEnum[1] in undefined_enums)\
                                   or (len(itEnum) == 3 and itEnum[1] in undefined_enums and itEnum[2] in undefined_enums):
                                    sf.tags[itCol][1] = itEnum[0]

                                # specific remediation follows
                                else:

                                    sf_category = get_first_sf_tag(sf, 'sf_category')

                                    try:

                                        content_subtype = next(c for c in input_source_dic['content_subtype']
                                                               if SF_CATEGORIES[file_type][c] == sf_category)

                                        if (file_type == 'nef' and itName == 'restraint_origin')\
                                           or (file_type == 'nmr-star' and itName == 'Constraint_type'):

                                            lp_data = next((lp['data'] for lp in self._reg.lp_data[content_subtype]
                                                            if lp['file_name'] == file_name
                                                            and lp['sf_framecode'] == w['sf_framecode']), None)

                                            if lp_data is None:
                                                lp_category = LP_CATEGORIES[file_type][content_subtype]

                                                key_items = self._reg.key_items[file_type][content_subtype]
                                                data_items = DATA_ITEMS[file_type][content_subtype]

                                                try:

                                                    lp_data =\
                                                        self._reg.nefT.check_data(sf, lp_category, key_items, data_items,
                                                                                  None, None, None,
                                                                                  enforce_allowed_tags=(file_type == 'nmr-star'),
                                                                                  excl_missing_data=self._reg.excl_missing_data)[0]  # noqa: E501, pylint: disable=line-too-long

                                                    self._reg.lp_data[content_subtype].append({'file_name': file_name,
                                                                                               'sf_framecode': w['sf_framecode'],
                                                                                               'data': lp_data})

                                                except Exception:  # pylint: disable=broad-exception-caught
                                                    pass

                                            if lp_data is not None:

                                                if content_subtype == 'dist_restraint':

                                                    if mandatory_tag:
                                                        sf.tags[itCol][1] = 'undefined' if file_type == 'nef'\
                                                            else 'general distance'

                                                    # 'NOE', 'NOE build-up', 'NOE not seen', 'ROE', 'ROE build-up', 'hydrogen bond',
                                                    # 'disulfide bond', 'paramagnetic relaxation', 'symmetry', 'general distance'

                                                    elif self._testDistRestraintAsHydrogenBond(lp_data):
                                                        sf.tags[itCol][1] = 'hbond' if file_type == 'nef' else 'hydrogen bond'

                                                    elif self._testDistRestraintAsDisulfideBond(lp_data):
                                                        sf.tags[itCol][1] = 'disulfide_bond' if file_type == 'nef'\
                                                            else 'disulfide bond'

                                                    elif self._testDistRestraintAsSymmetry(lp_data):
                                                        sf.tags[itCol][1] = 'symmetry'

                                                    else:
                                                        sf.tags[itCol][1] = 'undefined' if file_type == 'nef'\
                                                            else 'general distance'

                                                elif content_subtype == 'dihed_restraint':

                                                    if mandatory_tag:
                                                        sf.tags[itCol][1] = 'undefined'

                                                    # 'J-couplings', 'backbone chemical shifts'

                                                    elif self._testDihedRestraintAsBackBoneChemShifts(lp_data):
                                                        sf.tags[itCol][1] = 'chemical_shift' if file_type == 'nef'\
                                                            else 'backbone chemical shifts'

                                                    # else:
                                                    #    sf.tags[itCol][1] = 'J-couplings'

                                                    else:
                                                        sf.tags[itCol][1] = 'undefined'

                                                elif content_subtype == 'rdc_restraint':

                                                    if mandatory_tag:
                                                        sf.tags[itCol][1] = 'undefined'
                                                    else:
                                                        sf.tags[itCol][1] = 'measured' if file_type == 'nef' else 'RDC'

                                        if (file_type == 'nef' and itName == 'potential_type')\
                                           or (file_type == 'nmr-star' and itName == 'Potential_type'):

                                            lp_data = next((lp['data'] for lp in self._reg.lp_data[content_subtype]
                                                            if lp['file_name'] == file_name
                                                            and lp['sf_framecode'] == w['sf_framecode']), None)

                                            if lp_data is None:
                                                lp_category = LP_CATEGORIES[file_type][content_subtype]

                                                key_items = self._reg.key_items[file_type][content_subtype]
                                                data_items = DATA_ITEMS[file_type][content_subtype]

                                                try:

                                                    lp_data =\
                                                        self._reg.nefT.check_data(sf, lp_category, key_items, data_items,
                                                                                  None, None, None,
                                                                                  enforce_allowed_tags=(file_type == 'nmr-star'),
                                                                                  excl_missing_data=self._reg.excl_missing_data)[0]  # noqa: E501, pylint: disable=line-too-long

                                                    self._reg.lp_data[content_subtype].append({'file_name': file_name,
                                                                                               'sf_framecode': w['sf_framecode'],
                                                                                               'data': lp_data})

                                                except Exception:  # pylint: disable=broad-exception-caught
                                                    pass

                                            if lp_data is not None:

                                                # 'log-harmonic', 'parabolic'
                                                # 'square-well-parabolic', 'square-well-parabolic-linear',
                                                # 'upper-bound-parabolic', 'lower-bound-parabolic',
                                                # 'upper-bound-parabolic-linear', 'lower-bound-parabolic-linear'

                                                if mandatory_tag:
                                                    sf.tags[itCol][1] = 'undefined'
                                                elif self._testRestraintPotentialSWP(content_subtype, lp_data):
                                                    sf.tags[itCol][1] = 'square-well-parabolic'
                                                elif self._testRestraintPotentialSWPL(content_subtype, lp_data):
                                                    sf.tags[itCol][1] = 'square-well-parabolic-linear'
                                                elif self._testRestraintPotentialUBP(content_subtype, lp_data):
                                                    sf.tags[itCol][1] = 'upper-bound-parabolic'
                                                elif self._testRestraintPotentialLBP(content_subtype, lp_data):
                                                    sf.tags[itCol][1] = 'lower-bound-parabolic'
                                                elif self._testRestraintPotentialUBPL(content_subtype, lp_data):
                                                    sf.tags[itCol][1] = 'upper-bound-parabolic-linear'
                                                elif self._testRestraintPotentialLBPL(content_subtype, lp_data):
                                                    sf.tags[itCol][1] = 'lower-bound-parabolic-linear'
                                                elif self._testRestraintPonentialLHorP(content_subtype, lp_data):
                                                    if content_subtype == 'dist_restraint':
                                                        sf.tags[itCol][1] = 'log-harmonic'
                                                    else:
                                                        sf.tags[itCol][1] = 'parabolic'
                                                else:
                                                    sf.tags[itCol][1] = 'undefined'

                                    except StopIteration:

                                        err = "Could not specify content_subtype in NMR data processing report."

                                        self._reg.report.error.appendDescription('internal_error',
                                                                                 f"+{self.__class_name__}.fixEnumerationFailure() "
                                                                                 "++ Error  - " + err)

                                        if self._reg.verbose:
                                            self._reg.log.write(f"+{self.__class_name__}.fixEnumerationFailure() "
                                                                f"++ Error  - {err}\n")

                    else:

                        loop = sf.get_loop(w['category'])

                        if itName not in loop.tags:

                            err = f"Could not find loop tag {itName} in {w['category']} category, "\
                                f"{w['sf_framecode']!r} saveframe, {file_name!r} file."

                            self._reg.report.error.appendDescription('internal_error',
                                                                     f"+{self.__class_name__}.fixEnumerationFailure() "
                                                                     "++ Error  - " + err)

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.fixEnumerationFailure() ++ Error  - {err}\n")

                        else:

                            itCol = loop.tags.index(itName)

                            for row in loop:

                                val = row[itCol]

                                if val in EMPTY_VALUE:
                                    continue

                                if val == itValue:

                                    if len(itEnum) == 1:
                                        row[itCol] = itEnum[0]

                                    elif file_type == 'nef' and itName == 'folding':

                                        # 'circular', 'mirror', 'none'

                                        if val in ('aliased', 'folded', 'not observed'):
                                            if val == 'aliased':
                                                row[itCol] = 'mirror'
                                            elif val == 'folded':
                                                row[itCol] = 'circular'
                                            else:
                                                row[itCol] = 'none'

                                    elif file_type == 'nmr-star' and itName == 'Under_sampling_type':

                                        # 'aliased', 'folded', 'not observed'

                                        if val in ('circular', 'mirror', 'none'):
                                            if val == 'circular':
                                                row[itCol] = 'folded'
                                            elif val == 'mirror':
                                                row[itCol] = 'aliased'
                                            else:
                                                row[itCol] = 'not observed'

            else:

                err = f"Unexpected PyNMRSTAR object type {self._reg.star_data_type[0]} found about {file_name!r} file."

                self._reg.report.error.appendDescription('internal_error',
                                                         f"+{self.__class_name__}.fixEnumerationFailure() ++ Error  - " + err)

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.fixEnumerationFailure() ++ Error  - {err}\n")

        return True

    def _testDistRestraintAsHydrogenBond(self, lp_data: List[dict]) -> bool:
        """ Detect whether given distance restraints are derived from hydrogen bonds.
        """

        if not self._reg.combined_mode:
            return True

        if lp_data is None or len(lp_data) == 0:
            return False

        input_source = self._reg.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        item_names = ITEM_NAMES_IN_DIST_LOOP[file_type]
        chain_id_1_name = item_names['chain_id_1']
        chain_id_2_name = item_names['chain_id_2']
        seq_id_1_name = item_names['seq_id_1']
        seq_id_2_name = item_names['seq_id_2']
        atom_id_1_name = item_names['atom_id_1']
        atom_id_2_name = item_names['atom_id_2']

        def ext_atom_types(row):
            return (row[chain_id_1_name], row[chain_id_2_name],
                    row[seq_id_1_name], row[seq_id_2_name],
                    row[atom_id_1_name][0], row[atom_id_2_name][0])

        target_value_name = item_names['target_value']
        if 'target_value_alt' in item_names and target_value_name not in lp_data[0].keys():
            target_value_name = item_names['target_value_alt']
        lower_limit_name = item_names['lower_limit']
        upper_limit_name = item_names['upper_limit']
        lower_linear_limit_name = item_names['lower_linear_limit']
        upper_linear_limit_name = item_names['upper_linear_limit']

        def get_est_value_range(row):
            target_value = row.get(target_value_name)
            upper_limit = lower_limit = None

            if target_value is None:

                if has_key_value(row, lower_limit_name)\
                        and has_key_value(row, upper_limit_name):
                    target_value = (row[lower_limit_name] + row[upper_limit_name]) / 2.0
                    upper_limit = row[lower_limit_name]
                    lower_limit = row[upper_limit_name]

                elif has_key_value(row, lower_linear_limit_name)\
                        and has_key_value(row, upper_linear_limit_name):
                    target_value = (row[lower_linear_limit_name] + row[upper_linear_limit_name]) / 2.0

                elif has_key_value(row, upper_linear_limit_name):
                    target_value = row[upper_linear_limit_name]
                    upper_limit = target_value

                elif has_key_value(row, upper_limit_name):
                    target_value = row[upper_limit_name]
                    upper_limit = target_value

                elif has_key_value(row, lower_linear_limit_name):
                    target_value = row[lower_linear_limit_name]
                    lower_limit = target_value

                elif has_key_value(row, lower_limit_name):
                    target_value = row[lower_limit_name]
                    lower_limit = target_value

            return target_value, upper_limit, lower_limit

        try:

            for row in lp_data:

                chain_id_1, chain_id_2, seq_id_1, seq_id_2, \
                    atom_id_1_, atom_id_2_ = ext_atom_types(row)

                if chain_id_1 == chain_id_2 and seq_id_1 == seq_id_2:
                    return False

                target_value, upper_limit, lower_limit = get_est_value_range(row)

                if target_value is None:
                    return False

                if upper_limit is not None:
                    target_value -= 0.4

                if lower_limit is not None:
                    target_value += 0.4

                if (atom_id_1_ == 'F' and atom_id_2_ in PROTON_BEGIN_CODE)\
                        or (atom_id_2_ == 'F' and atom_id_1_ in PROTON_BEGIN_CODE):

                    if target_value < 1.2 or target_value > 1.5:
                        return False

                elif (atom_id_1_ == 'F' and atom_id_2_ == 'F') or (atom_id_2_ == 'F' and atom_id_1_ == 'F'):

                    if target_value < 2.2 or target_value > 2.5:
                        return False

                elif (atom_id_1_ == 'O' and atom_id_2_ in PROTON_BEGIN_CODE)\
                        or (atom_id_2_ == 'O' and atom_id_1_ in PROTON_BEGIN_CODE):

                    if target_value < 1.5 or target_value > 2.5:
                        return False

                elif (atom_id_1_ == 'O' and atom_id_2_ == 'N') or (atom_id_2_ == 'O' and atom_id_1_ == 'N'):

                    if target_value < 2.5 or target_value > 3.5:
                        return False

                elif (atom_id_1_ == 'O' and atom_id_2_ == 'O') or (atom_id_2_ == 'O' and atom_id_1_ == 'O'):

                    if target_value < 2.5 or target_value > 3.5:
                        return False

                elif (atom_id_1_ == 'N' and atom_id_2_ in PROTON_BEGIN_CODE)\
                        or (atom_id_2_ == 'N' and atom_id_1_ in PROTON_BEGIN_CODE):

                    if target_value < 1.5 or target_value > 2.5:
                        return False

                elif (atom_id_1_ == 'N' and atom_id_2_ == 'N') or (atom_id_2_ == 'N' and atom_id_1_ == 'N'):

                    if target_value < 2.5 or target_value > 3.5:
                        return False

                else:
                    return False

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.__testDistRestraintAsHydrogenBond() "
                                                     "++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.__testDistRestraintAsHydrogenBond() "
                                    f"++ Error  - {str(e)}\n")

            return False

        return True

    def _testDistRestraintAsDisulfideBond(self, lp_data: List[dict]) -> bool:
        """ Detect whether given distance restraints are derived from disulfide bonds.
        """

        if not self._reg.combined_mode:
            return True

        if lp_data is None or len(lp_data) == 0:
            return False

        input_source = self._reg.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        item_names = ITEM_NAMES_IN_DIST_LOOP[file_type]
        chain_id_1_name = item_names['chain_id_1']
        chain_id_2_name = item_names['chain_id_2']
        seq_id_1_name = item_names['seq_id_1']
        seq_id_2_name = item_names['seq_id_2']
        atom_id_1_name = item_names['atom_id_1']
        atom_id_2_name = item_names['atom_id_2']

        def ext_atom_types(row):
            return (row[chain_id_1_name], row[chain_id_2_name],
                    row[seq_id_1_name], row[seq_id_2_name],
                    row[atom_id_1_name][0], row[atom_id_2_name][0])

        target_value_name = item_names['target_value']
        if 'target_value_alt' in item_names and target_value_name not in lp_data[0].keys():
            target_value_name = item_names['target_value_alt']
        lower_limit_name = item_names['lower_limit']
        upper_limit_name = item_names['upper_limit']
        lower_linear_limit_name = item_names['lower_linear_limit']
        upper_linear_limit_name = item_names['upper_linear_limit']

        def get_est_value_range(row):
            target_value = row.get(target_value_name)
            upper_limit = lower_limit = None

            if target_value is None:

                if has_key_value(row, lower_limit_name)\
                        and has_key_value(row, upper_limit_name):
                    target_value = (row[lower_limit_name] + row[upper_limit_name]) / 2.0
                    upper_limit = row[lower_limit_name]
                    lower_limit = row[upper_limit_name]

                elif has_key_value(row, lower_linear_limit_name)\
                        and has_key_value(row, upper_linear_limit_name):
                    target_value = (row[lower_linear_limit_name] + row[upper_linear_limit_name]) / 2.0

                elif has_key_value(row, upper_linear_limit_name):
                    target_value = row[upper_linear_limit_name]
                    upper_limit = target_value

                elif has_key_value(row, upper_limit_name):
                    target_value = row[upper_limit_name]
                    upper_limit = target_value

                elif has_key_value(row, lower_linear_limit_name):
                    target_value = row[lower_linear_limit_name]
                    lower_limit = target_value

                elif has_key_value(row, lower_limit_name):
                    target_value = row[lower_limit_name]
                    lower_limit = target_value

            return target_value, upper_limit, lower_limit

        try:

            for row in lp_data:
                chain_id_1, chain_id_2, seq_id_1, seq_id_2, \
                    atom_id_1_, atom_id_2_ = ext_atom_types(row)

                if chain_id_1 == chain_id_2 and seq_id_1 == seq_id_2:
                    return False

                target_value, upper_limit, lower_limit = get_est_value_range(row)

                if target_value is None:
                    return False

                if upper_limit is not None:
                    target_value -= 0.4

                if lower_limit is not None:
                    target_value += 0.4

                if atom_id_1_ == 'S' and atom_id_2_ == 'S':

                    if target_value < 1.9 or target_value > 2.3:
                        return False

                else:
                    return False

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.__testDistRestraintAsDisulfideBond() "
                                                     "++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.__testDistRestraintAsDisulfideBond() "
                                    f"++ Error  - {str(e)}\n")

            return False

        return True

    def _testDistRestraintAsSymmetry(self, lp_data: List[dict]) -> bool:
        """ Detect whether given distance restraints are derived from symmetric assembly.
        """

        if not self._reg.combined_mode:
            return True

        if lp_data is None:
            return False

        input_source = self._reg.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        item_names = ITEM_NAMES_IN_DIST_LOOP[file_type]
        chain_id_1_name = item_names['chain_id_1']
        chain_id_2_name = item_names['chain_id_2']
        seq_id_1_name = item_names['seq_id_1']
        seq_id_2_name = item_names['seq_id_2']
        comp_id_1_name = item_names['comp_id_1']
        comp_id_2_name = item_names['comp_id_2']

        def ext_comp_names(row):
            return (row[chain_id_1_name], row[chain_id_2_name],
                    row[seq_id_1_name], row[seq_id_2_name],
                    row[comp_id_1_name], row[comp_id_2_name])

        try:

            for row in lp_data:
                chain_id_1, chain_id_2, seq_id_1, seq_id_2, \
                    comp_id_1, comp_id_2 = ext_comp_names(row)

                if chain_id_1 == chain_id_2:
                    return False

                has_symmetry = False

                for _row in lp_data:

                    if _row is row:
                        continue

                    _chain_id_1, _chain_id_2, _seq_id_1, _seq_id_2, \
                        _comp_id_1, _comp_id_2 = ext_comp_names(_row)

                    if _chain_id_1 != _chain_id_2 and _chain_id_1 != chain_id_1 and _chain_id_2 != chain_id_2:

                        if seq_id_1 == _seq_id_1 and comp_id_1 == _comp_id_1\
                           and seq_id_2 == _seq_id_2 and comp_id_2 == _comp_id_2:
                            has_symmetry = True
                            break

                        if seq_id_1 == _seq_id_2 and comp_id_1 == _comp_id_2\
                           and seq_id_2 == _seq_id_1 and comp_id_2 == _comp_id_1:
                            has_symmetry = True
                            break

                if not has_symmetry:
                    return False

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.__testDistRestraintAsSymmetry() "
                                                     "++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.__testDistRestraintAsSymmetry() "
                                    f"++ Error  - {str(e)}\n")

            return False

        return True

    def _testDihedRestraintAsBackBoneChemShifts(self, lp_data: List[dict]) -> bool:
        """ Detect whether given dihedral angle restraints are derived from backbone chemical shifts.
        """

        if not self._reg.combined_mode:
            return True

        if lp_data is None:
            return False

        input_source = self._reg.report.input_sources[0]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        item_names = ITEM_NAMES_IN_DIHED_LOOP[file_type]
        chain_id_1_name = item_names['chain_id_1']
        chain_id_2_name = item_names['chain_id_2']
        chain_id_3_name = item_names['chain_id_3']
        chain_id_4_name = item_names['chain_id_4']
        seq_id_1_name = item_names['seq_id_1']
        seq_id_2_name = item_names['seq_id_2']
        seq_id_3_name = item_names['seq_id_3']
        seq_id_4_name = item_names['seq_id_4']
        comp_id_1_name = item_names['comp_id_1']
        comp_id_2_name = item_names['comp_id_2']
        comp_id_3_name = item_names['comp_id_3']
        comp_id_4_name = item_names['comp_id_4']
        atom_id_1_name = item_names['atom_id_1']
        atom_id_2_name = item_names['atom_id_2']
        atom_id_3_name = item_names['atom_id_3']
        atom_id_4_name = item_names['atom_id_4']
        angle_type_name = item_names['angle_type']
        lower_limit_name = item_names['lower_limit']
        upper_limit_name = item_names['upper_limit']

        def ext_atoms(row):
            return ({'chain_id': row[chain_id_1_name], 'seq_id': row[seq_id_1_name],
                     'comp_id': row[comp_id_1_name], 'atom_id': row[atom_id_1_name]},
                    {'chain_id': row[chain_id_2_name], 'seq_id': row[seq_id_2_name],
                     'comp_id': row[comp_id_2_name], 'atom_id': row[atom_id_2_name]},
                    {'chain_id': row[chain_id_3_name], 'seq_id': row[seq_id_3_name],
                     'comp_id': row[comp_id_3_name], 'atom_id': row[atom_id_3_name]},
                    {'chain_id': row[chain_id_4_name], 'seq_id': row[seq_id_4_name],
                     'comp_id': row[comp_id_4_name], 'atom_id': row[atom_id_4_name]})

        dh_chain_ids, cs_chain_ids = set(), set()
        dh_seq_ids, cs_seq_ids = {}, {}

        try:

            for row in lp_data:
                atom1, atom2, atom3, atom4 = ext_atoms(row)

                angle_type = row[angle_type_name]

                if angle_type in EMPTY_VALUE:
                    continue

                angle_type = angle_type.lower()

                if angle_type not in ('phi', 'psi'):
                    return False

                peptide, nucleotide, carbohydrate = self._reg.csStat.getTypeOfCompId(atom2['comp_id'])

                if not peptide:
                    return False

                plane_like = is_like_planality_boundary(row, lower_limit_name, upper_limit_name)

                data_type = getTypeOfDihedralRestraint(peptide, nucleotide, carbohydrate,
                                                       [atom1, atom2, atom3, atom4], plane_like)

                if data_type is None or data_type.lower() not in ('phi', 'psi'):
                    return False

                chain_id = atom1['chain_id']
                dh_chain_ids.add(chain_id)

                seq_ids = [atom1['seq_id'], atom2['seq_id'], atom3['seq_id'], atom4['seq_id']]
                seq_id_common = collections.Counter(seq_ids).most_common()

                if chain_id not in dh_seq_ids:
                    dh_seq_ids[chain_id] = set()

                dh_seq_ids[chain_id].add(seq_id_common[0][0])

            # check backbone CA atoms

            content_subtype = 'chem_shift'

            if not has_key_value(input_source_dic['content_subtype'], content_subtype):
                return False

            sf_category = SF_CATEGORIES[file_type][content_subtype]
            lp_category = LP_CATEGORIES[file_type][content_subtype]

            key_items = self._reg.key_items[file_type][content_subtype]
            data_items = DATA_ITEMS[file_type][content_subtype]

            item_names = ITEM_NAMES_IN_CS_LOOP[file_type]
            chain_id_name = item_names['chain_id']
            seq_id_name = item_names['seq_id']
            atom_id_name = item_names['atom_id']

            for sf in self._reg.star_data[0].get_saveframes_by_category(sf_category):
                sf_framecode = get_first_sf_tag(sf, 'sf_framecode')

                if self._reg.report.error.exists(file_name, sf_framecode):
                    continue

                lp_data = next((lp['data'] for lp in self._reg.lp_data[content_subtype]
                                if lp['file_name'] == file_name and lp['sf_framecode'] == sf_framecode), None)

                if lp_data is None:

                    try:

                        lp_data = self._reg.nefT.check_data(sf, lp_category, key_items, data_items, None, None, None,
                                                            enforce_allowed_tags=(file_type == 'nmr-star'),
                                                            excl_missing_data=self._reg.excl_missing_data)[0]

                        self._reg.lp_data[content_subtype].append({'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                   'data': lp_data})

                    except Exception:  # pylint: disable=broad-exception-caught
                        pass

                if lp_data is not None:

                    for row in lp_data:
                        chain_id = row[chain_id_name]
                        seq_id = row[seq_id_name]
                        atom_id = row[atom_id_name]

                        if chain_id in dh_chain_ids and seq_id in dh_seq_ids[chain_id] and atom_id == 'CA':
                            cs_chain_ids.add(chain_id)

                            if chain_id not in cs_seq_ids:
                                cs_seq_ids[chain_id] = set()

                            cs_seq_ids[chain_id].add(seq_id)

            if cs_chain_ids != dh_chain_ids:
                return False

            for k, v in dh_seq_ids.items():

                if len(cs_seq_ids[k] & v) < len(v) * 0.8:
                    return False

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.__testDihedRestraintAsBackBoneChemShifts() "
                                                     "++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.__testDihedRestraintAsBackBoneChemShifts() "
                                    f"++ Error  - {str(e)}\n")

            return False

        return True

    def _testRestraintPotentialSWP(self, content_subtype: str, lp_data: List[dict]) -> bool:
        """ Detect square-well-parabolic potential.
        """

        if not self._reg.combined_mode:
            return True

        if lp_data is None:
            return False

        input_source = self._reg.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        try:

            item_names = POTENTIAL_ITEMS[file_type][content_subtype]
            lower_limit_name = item_names['lower_limit']
            upper_limit_name = item_names['upper_limit']
            lower_linear_limit_name = item_names['lower_linear_limit']
            upper_linear_limit_name = item_names['upper_linear_limit']

            for row in lp_data:
                if has_key_value(row, lower_limit_name)\
                   and has_key_value(row, upper_limit_name)\
                   and not has_key_value(row, lower_linear_limit_name)\
                   and not has_key_value(row, upper_linear_limit_name):
                    continue

                return False

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.__testRestraintPotentialSWP() ++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.__testRestraintPotentialSWP() ++ Error  - {str(e)}\n")

            return False

        return True

    def _testRestraintPotentialSWPL(self, content_subtype: str, lp_data: List[str]) -> bool:
        """ Detect square-well-parabolic-linear potential.
        """

        if not self._reg.combined_mode:
            return True

        if lp_data is None:
            return False

        input_source = self._reg.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        try:

            item_names = POTENTIAL_ITEMS[file_type][content_subtype]
            lower_limit_name = item_names['lower_limit']
            upper_limit_name = item_names['upper_limit']
            lower_linear_limit_name = item_names['lower_linear_limit']
            upper_linear_limit_name = item_names['upper_linear_limit']

            for row in lp_data:
                if has_key_value(row, lower_limit_name)\
                   and has_key_value(row, upper_limit_name)\
                   and has_key_value(row, lower_linear_limit_name)\
                   and has_key_value(row, upper_linear_limit_name):
                    continue

                return False

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.__testRestraintPotentialSWPL() "
                                                     "++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.__testRestraintPotentialSWPL() ++ Error  - {str(e)}\n")

            return False

        return True

    def _testRestraintPotentialUBP(self, content_subtype: str, lp_data: List[dict]) -> bool:
        """ Detect upper-bound-parabolic potential.
        """

        if not self._reg.combined_mode:
            return True

        if lp_data is None:
            return False

        input_source = self._reg.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        try:

            item_names = POTENTIAL_ITEMS[file_type][content_subtype]
            lower_limit_name = item_names['lower_limit']
            upper_limit_name = item_names['upper_limit']
            lower_linear_limit_name = item_names['lower_linear_limit']
            upper_linear_limit_name = item_names['upper_linear_limit']

            for row in lp_data:
                if not has_key_value(row, lower_limit_name)\
                   and has_key_value(row, upper_limit_name)\
                   and not has_key_value(row, lower_linear_limit_name)\
                   and not has_key_value(row, upper_linear_limit_name):
                    continue

                return False

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.__testRestraintPotentialUBP() ++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.__testRestraintPotentialUBP() ++ Error  - {str(e)}\n")

            return False

        return True

    def _testRestraintPotentialLBP(self, content_subtype: str, lp_data: List[str]) -> bool:
        """ Detect lower-bound-parabolic potential.
        """

        if not self._reg.combined_mode:
            return True

        if lp_data is None:
            return False

        input_source = self._reg.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        try:

            item_names = POTENTIAL_ITEMS[file_type][content_subtype]
            lower_limit_name = item_names['lower_limit']
            upper_limit_name = item_names['upper_limit']
            lower_linear_limit_name = item_names['lower_linear_limit']
            upper_linear_limit_name = item_names['upper_linear_limit']

            for row in lp_data:
                if has_key_value(row, lower_limit_name)\
                   and not has_key_value(row, upper_limit_name)\
                   and not has_key_value(row, lower_linear_limit_name)\
                   and not has_key_value(row, upper_linear_limit_name):
                    continue

                return False

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.__testRestraintPotentialLBP() ++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.__testRestraintPotentialLBP() ++ Error  - {str(e)}\n")

            return False

        return True

    def _testRestraintPotentialUBPL(self, content_subtype: str, lp_data: List[dict]) -> bool:
        """ Detect upper-bound-parabolic-linear potential.
        """

        if not self._reg.combined_mode:
            return True

        if lp_data is None:
            return False

        input_source = self._reg.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        try:

            item_names = POTENTIAL_ITEMS[file_type][content_subtype]
            lower_limit_name = item_names['lower_limit']
            upper_limit_name = item_names['upper_limit']
            lower_linear_limit_name = item_names['lower_linear_limit']
            upper_linear_limit_name = item_names['upper_linear_limit']

            for row in lp_data:
                if not has_key_value(row, lower_limit_name)\
                   and has_key_value(row, upper_limit_name)\
                   and not has_key_value(row, lower_linear_limit_name)\
                   and has_key_value(row, upper_linear_limit_name):
                    continue

                return False

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.__testRestraintPotentialUBPL() "
                                                     "++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.__testRestraintPotentialUBPL() ++ Error  - {str(e)}\n")

            return False

        return True

    def _testRestraintPotentialLBPL(self, content_subtype: str, lp_data: List[dict]) -> bool:
        """ Detect lower-bound-parabolic-linear potential.
        """

        if not self._reg.combined_mode:
            return True

        if lp_data is None:
            return False

        input_source = self._reg.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        try:

            item_names = POTENTIAL_ITEMS[file_type][content_subtype]
            lower_limit_name = item_names['lower_limit']
            upper_limit_name = item_names['upper_limit']
            lower_linear_limit_name = item_names['lower_linear_limit']
            upper_linear_limit_name = item_names['upper_linear_limit']

            for row in lp_data:
                if has_key_value(row, lower_limit_name)\
                   and not has_key_value(row, upper_limit_name)\
                   and has_key_value(row, lower_linear_limit_name)\
                   and not has_key_value(row, upper_linear_limit_name):
                    continue

                return False

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.__testRestraintPotentialLBPL() "
                                                     "++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.__testRestraintPotentialLBPL() ++ Error  - {str(e)}\n")

            return False

        return True

    def _testRestraintPonentialLHorP(self, content_subtype: str, lp_data: List[dict]) -> bool:
        """ Detect log-harmonic or parabolic potential.
        """

        if not self._reg.combined_mode:
            return True

        if lp_data is None or len(lp_data) == 0:
            return False

        input_source = self._reg.report.input_sources[0]
        input_source_dic = input_source.get()

        file_type = input_source_dic['file_type']

        try:

            item_names = POTENTIAL_ITEMS[file_type][content_subtype]
            target_value_name = item_names['target_value']
            if 'target_value_alt' in item_names and target_value_name not in lp_data[0].keys():
                target_value_name = item_names['target_value_alt']
            lower_limit_name = item_names['lower_limit']
            upper_limit_name = item_names['upper_limit']
            lower_linear_limit_name = item_names['lower_linear_limit']
            upper_linear_limit_name = item_names['upper_linear_limit']

            for row in lp_data:
                if has_key_value(row, target_value_name)\
                   and not has_key_value(row, lower_limit_name)\
                   and not has_key_value(row, upper_limit_name)\
                   and not has_key_value(row, lower_linear_limit_name)\
                   and not has_key_value(row, upper_linear_limit_name):
                    continue

                return False

        except Exception as e:  # pylint: disable=broad-exception-caught

            self._reg.report.error.appendDescription('internal_error',
                                                     f"+{self.__class_name__}.__testRestraintPotentialLHorP() "
                                                     "++ Error  - " + str(e))

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.__testRestraintPotentialLHorP() ++ Error  - {str(e)}\n")

            return False

        return True
