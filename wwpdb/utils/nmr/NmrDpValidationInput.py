##
# File: NmrDpValidationInput.py
# Date: 17-Aug-2026
#
# Updates:
# 28-Sep-2026  M. Yokochi - collect the cyclic garbage of the previous NMR unified data before validating
#                           a large one, which otherwise sets the peak memory of 'nmr-str2str-deposit' (DAOTHER-7829, 9785)
# 02-Oct-2026  M. Yokochi - return the freed heap to the OS after that collection (6x63: 76-91 MB) (DAOTHER-7829, 9785)
##
""" Input source validation and content subtype detection for NMR data validation.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.0"

import copy
import gc
import os
import re
import shutil
from typing import Optional, Union

import pynmrstar

try:
    from wwpdb.utils.nmr.NmrDpConstant import (CS_FILE_PATH_LIST_KEY,
                                               MR_FILE_PATH_LIST_KEY,
                                               AR_FILE_PATH_LIST_KEY,
                                               AC_FILE_PATH_LIST_KEY,
                                               NMR_CIF_FILE_PATH_KEY,
                                               NMR_CONTENT_SUBTYPES,
                                               READABLE_FILE_TYPE,
                                               SF_CATEGORIES,
                                               LP_CATEGORIES,
                                               SF_TAG_PREFIXES,
                                               EMPTY_VALUE,
                                               PDB_ID_PAT,
                                               DEP_ID_PAT,
                                               BMRB_NMR_STAR_FILE_NAME_PAT,
                                               INTNL_ANY_MR_FILE_NAME_PAT,
                                               PDB_MR_FILE_NAME_PAT,
                                               WS_PAT,
                                               MIN_INPUT_SIZE_FOR_GC,
                                               trim_heap)
    from wwpdb.utils.nmr.NmrDpMrSplitter import (detect_bom,
                                                 convert_codec,
                                                 convert_rtf_to_ascii,
                                                 is_rtf_file)
    from wwpdb.utils.nmr.NmrDpReport import NmrDpReportInputSource
    from wwpdb.utils.nmr.CifToNmrStar import (get_first_sf_tag,
                                              set_sf_tag)
    from wwpdb.utils.nmr.NmrVrptUtility import (uncompress_gzip_file,
                                                compress_as_gzip_file)
    from wwpdb.utils.nmr.NmrDpValidationBase import NmrDpValidationBase
except ImportError:
    from nmr.NmrDpConstant import (CS_FILE_PATH_LIST_KEY,
                                   MR_FILE_PATH_LIST_KEY,
                                   AR_FILE_PATH_LIST_KEY,
                                   AC_FILE_PATH_LIST_KEY,
                                   NMR_CIF_FILE_PATH_KEY,
                                   NMR_CONTENT_SUBTYPES,
                                   READABLE_FILE_TYPE,
                                   SF_CATEGORIES,
                                   LP_CATEGORIES,
                                   SF_TAG_PREFIXES,
                                   EMPTY_VALUE,
                                   PDB_ID_PAT,
                                   DEP_ID_PAT,
                                   BMRB_NMR_STAR_FILE_NAME_PAT,
                                   INTNL_ANY_MR_FILE_NAME_PAT,
                                   PDB_MR_FILE_NAME_PAT,
                                   WS_PAT,
                                   MIN_INPUT_SIZE_FOR_GC,
                                   trim_heap)
    from nmr.NmrDpMrSplitter import (detect_bom,
                                     convert_codec,
                                     convert_rtf_to_ascii,
                                     is_rtf_file)
    from nmr.NmrDpReport import NmrDpReportInputSource
    from nmr.CifToNmrStar import (get_first_sf_tag,
                                  set_sf_tag)
    from nmr.NmrVrptUtility import (uncompress_gzip_file,
                                    compress_as_gzip_file)
    from nmr.NmrDpValidationBase import NmrDpValidationBase


class NmrDpValidationInput(NmrDpValidationBase):
    """ Input source validation and content subtype detection for NMR data validation.
    """
    __slots__ = ()

    def validateInputSource(self, srcPath: str = None) -> bool:
        """ Validate NMR data as primary input source.
        """

        if srcPath is None:
            srcPath = self._reg.srcPath

        is_done = True

        self._reg.legacy_dist_restraint_uploaded = False

        def proc_cs_path_path_list(offset):

            for csListId, cs in enumerate(self._reg.inputParamDict[CS_FILE_PATH_LIST_KEY], start=offset):

                if isinstance(cs, str):
                    csPath = cs
                else:
                    csPath = cs['file_name']

                if csListId == 0:
                    self._reg.spareDirPath = os.path.dirname(csPath)
                    if self._reg.dirPath is None:
                        self._reg.dirPath = self._reg.spareDirPath

                if csPath.endswith('.gz'):

                    _csPath = os.path.splitext(csPath)[0]

                    if not os.path.exists(_csPath):

                        try:

                            uncompress_gzip_file(csPath, _csPath)

                        except Exception as e:  # pylint: disable=broad-exception-caught

                            self._reg.report.error.appendDescription('internal_error',
                                                                     f"+{self.__class_name__}.validateInputSource() "
                                                                     "++ Error  - " + str(e))

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.validateInputSource() "
                                                    f"++ Error  - {str(e)}\n")

                            return False

                    csPath = _csPath

                if self._reg.op == 'nmr-cs-mr-merge' and not os.path.basename(csPath).startswith('bmr'):

                    _csPath = self.getNextPath(csPath, '.cif2str')
                    if not self._reg.c2S.convert(csPath, _csPath,
                                                 originalFileName=cs.get('original_file_name') if isinstance(cs, dict) else None):
                        _csPath = csPath

                    csPath = _csPath

                codec = detect_bom(csPath, 'utf-8')

                _csPath = None

                if codec != 'utf-8':
                    _csPath = self.getNextPath(csPath)
                    convert_codec(csPath, _csPath, codec, 'utf-8')
                    csPath = _csPath

                if is_rtf_file(csPath):
                    _csPath = self.getNextPath(csPath, '.rtf2txt')
                    convert_rtf_to_ascii(csPath, _csPath)
                    csPath = _csPath

                if self._reg.op == 'nmr-cs-mr-merge':

                    dir_path = os.path.dirname(csPath) if self._reg.dirPath is None else self._reg.dirPath

                    rem_dir = os.path.join(dir_path, 'remediation')

                    try:

                        if not os.path.isdir(rem_dir):
                            os.makedirs(rem_dir)

                        cs_file_name = os.path.basename(csPath)

                        if cs_file_name.endswith('.cif2str'):
                            cs_file_name = os.path.splitext(cs_file_name)[0]

                        if cs_file_name.endswith('.str'):
                            cs_file_name = os.path.splitext(cs_file_name)[0]

                        if cs_file_name.endswith('-corrected'):
                            cs_file_link = os.path.join(rem_dir, f'{cs_file_name[:-10]}.str')
                            cs_file_path = os.path.join(dir_path, f'{cs_file_name}.str')

                            if os.path.exists(cs_file_link):
                                os.remove(cs_file_link)

                            os.symlink(cs_file_path, cs_file_link)

                    except OSError:
                        pass

                allow_empty = self._reg.bmrb_only and self._reg.internal_mode\
                    and (NMR_CIF_FILE_PATH_KEY in self._reg.inputParamDict
                         or (csListId == 0 and len(self._reg.inputParamDict[CS_FILE_PATH_LIST_KEY]) > 1))

                is_valid, message = self._reg.nefT.validate_file(csPath, 'S', allow_empty)  # 'S' for assigned chemical shifts

                self._reg.original_error_message.append(message)

                _file_type = message['file_type']  # nef/nmr-star/unknown

                input_source = self._reg.report.input_sources[csListId]
                input_source_dic = input_source.get()

                file_name = input_source_dic['file_name']
                file_type = input_source_dic['file_type']

                if CS_FILE_PATH_LIST_KEY in self._reg.outputParamDict:
                    if csListId < len(self._reg.outputParamDict[CS_FILE_PATH_LIST_KEY]):
                        dstPath = self._reg.outputParamDict[CS_FILE_PATH_LIST_KEY][csListId]
                        if dstPath is not None and dstPath not in self._reg.inputParamDict[CS_FILE_PATH_LIST_KEY]:
                            shutil.copyfile(csPath, dstPath)

                if is_valid:

                    if _file_type != file_type:

                        if (self._reg.internal_mode or self._reg.conversion_server) and _file_type == 'nef':

                            _csPath = self.getNextPath(csPath, '.nef2str')

                            try:

                                is_valid, message = self._reg.nefT.nef_to_nmrstar(csPath, _csPath)

                                if is_valid:
                                    csPath = _csPath

                                    _is_done, star_data_type, star_data = self._reg.nefT.read_input_file(csPath)

                                    self._reg.has_legacy_sf_issue = False

                                    if star_data_type == 'Saveframe':
                                        self._reg.has_legacy_sf_issue = True

                                        self._reg.dpA.fixFormatIssueOfInputSource(csListId, file_name, file_type, csPath,
                                                                                  'S', message,
                                                                                  allowEmpty=allow_empty,
                                                                                  hasLegacySfIssue=self._reg.has_legacy_sf_issue)

                                        _is_done, star_data_type, star_data = self._reg.nefT.read_input_file(csPath)

                                    if not (self._reg.has_legacy_sf_issue and _is_done and star_data_type == 'Entry'):

                                        if len(self._reg.star_data_type) > csListId:
                                            self._reg.star_data_type[csListId] = star_data_type
                                            self._reg.star_data[csListId] = star_data
                                        else:
                                            self._reg.star_data_type.append(star_data_type)
                                            self._reg.star_data.append(star_data)

                                        self._reg.dpA.rescueFormerNef(csListId)
                                        self._reg.dpA.rescueImmatureStr(csListId)

                                    if star_data_type != 'Entry':
                                        _star_data = self._convertCsToEntry(star_data, csListId + 1)
                                        if isinstance(_star_data, pynmrstar.Entry):
                                            self._reg.star_data[-1] = _star_data
                                            self._reg.star_data_type[-1] = 'Entry'
                                    else:
                                        self._reg.star_data[-1] = self._convertCsToEntry(star_data)

                            except Exception as e:  # pylint: disable=broad-exception-caught

                                err = f"{file_name!r} is not compliant with the {READABLE_FILE_TYPE[_file_type]} dictionary."

                                if 'No such file or directory' not in str(e):
                                    err += ' ' + re.sub('not in list', 'unknown item.', str(e))

                                self._reg.report.error.appendDescription('format_issue',
                                                                         {'file_name': file_name, 'description': err})

                                self._reg.log.write(f"+{self.__class_name__}.validateInputSource() "
                                                    f"++ Error  - {file_name} {err}\n")

                        else:

                            err = f"{file_name!r} was selected as {READABLE_FILE_TYPE[file_type]} file, "\
                                  f"but recognized as {READABLE_FILE_TYPE[_file_type]} file."
                            # DAOTHER-5673
                            err += " Please re-upload the NEF file as an NMR unified data file." if _file_type == 'nef'\
                                else " Please re-upload the file."

                            if len(message['error']) > 0:
                                for err_message in message['error']:
                                    if 'No such file or directory' not in err_message:
                                        err += ' ' + re.sub('not in list', 'unknown item.', err_message)

                            self._reg.report.error.appendDescription('content_mismatch',
                                                                     {'file_name': file_name, 'description': err})

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.validateInputSource() "
                                                    f"++ Error  - {err}\n")

                            return False

                    else:

                        _is_done, star_data_type, star_data = self._reg.nefT.read_input_file(csPath)

                        self._reg.has_legacy_sf_issue = False

                        if star_data_type == 'Saveframe':
                            self._reg.has_legacy_sf_issue = True

                            self._reg.dpA.fixFormatIssueOfInputSource(csListId, file_name, file_type, csPath, 'S', message,
                                                                      allowEmpty=allow_empty,
                                                                      hasLegacySfIssue=self._reg.has_legacy_sf_issue)

                            _is_done, star_data_type, star_data = self._reg.nefT.read_input_file(csPath)

                        if not (self._reg.has_legacy_sf_issue and _is_done and star_data_type == 'Entry'):

                            if len(self._reg.star_data_type) > csListId:
                                self._reg.star_data_type[csListId] = star_data_type
                                self._reg.star_data[csListId] = star_data
                            else:
                                self._reg.star_data_type.append(star_data_type)
                                self._reg.star_data.append(star_data)

                            self._reg.dpA.rescueFormerNef(csListId)
                            self._reg.dpA.rescueImmatureStr(csListId)

                        if star_data_type != 'Entry':
                            _star_data = self._convertCsToEntry(star_data, csListId + 1)
                            if isinstance(_star_data, pynmrstar.Entry):
                                self._reg.star_data[-1] = _star_data
                                self._reg.star_data_type[-1] = 'Entry'
                        else:
                            self._reg.star_data[-1] = self._convertCsToEntry(star_data)

                else:

                    if not self._reg.dpA.fixFormatIssueOfInputSource(csListId, file_name, file_type, csPath, 'S', message,
                                                                     allowEmpty=allow_empty,
                                                                     hasLegacySfIssue=self._reg.has_legacy_sf_issue):
                        pass

                if _csPath is not None:
                    try:
                        os.remove(_csPath)
                    except OSError:
                        pass

            return True

        def proc_mr_file_path_list():

            if MR_FILE_PATH_LIST_KEY in self._reg.inputParamDict:

                for mr in self._reg.inputParamDict[MR_FILE_PATH_LIST_KEY]:

                    if isinstance(mr, str):
                        mrPath = mr
                    else:
                        mrPath = mr['file_name']

                    codec = detect_bom(mrPath, 'utf-8')

                    _mrPath = None

                    if codec != 'utf-8':
                        _mrPath = self.getNextPath(mrPath)
                        convert_codec(mrPath, _mrPath, codec, 'utf-8')
                        mrPath = _mrPath

                    if is_rtf_file(mrPath):
                        _mrPath = self.getNextPath(mrPath, '.rtf2txt')
                        convert_rtf_to_ascii(mrPath, _mrPath)
                        mrPath = _mrPath

                    is_valid, message = self._reg.nefT.validate_file(mrPath, 'R')  # 'R' for restraints

                    if is_valid:
                        self._reg.legacy_dist_restraint_uploaded = True

                    if _mrPath is not None:
                        try:
                            os.remove(_mrPath)
                        except OSError:
                            pass

                has_atypical_restraint = False

                if AR_FILE_PATH_LIST_KEY in self._reg.inputParamDict:

                    for ar in self._reg.inputParamDict[AR_FILE_PATH_LIST_KEY]:
                        arPath = ar['file_name']

                        if os.path.exists(arPath):
                            has_atypical_restraint = True
                            break

                # DAOTHER-7545, issue #2, 'R' for restraints, 'O' for other conventional restraints
                file_subtype = 'O' if self._reg.legacy_dist_restraint_uploaded or has_atypical_restraint else 'R'

                file_path_list_len = self._reg.cs_file_path_list_len

                for mr in self._reg.inputParamDict[MR_FILE_PATH_LIST_KEY]:

                    if isinstance(mr, str):
                        mrPath = mr
                    else:
                        mrPath = mr['file_name']

                    mrPath = self.testPathWithSuffix(mrPath, '-corrected')

                    if self._reg.op == 'nmr-cs-mr-merge':

                        _mrPath = self.getNextPath(mrPath, '.cif2str')
                        if not self._reg.c2S.convert(mrPath, _mrPath,
                                                     originalFileName=mr.get('original_file_name') if isinstance(mr, dict) else None):  # noqa: E501, pylint: disable=line-too-long
                            mrPath = _mrPath

                    codec = detect_bom(mrPath, 'utf-8')

                    _mrPath = None

                    if codec != 'utf-8':
                        _mrPath = self.getNextPath(mrPath)
                        convert_codec(mrPath, _mrPath, codec, 'utf-8')
                        mrPath = _mrPath

                    if is_rtf_file(mrPath):
                        _mrPath = self.getNextPath(mrPath, '.rtf2txt')
                        convert_rtf_to_ascii(mrPath, _mrPath)
                        mrPath = _mrPath

                    is_valid, message = self._reg.nefT.validate_file(mrPath, file_subtype)

                    self._reg.original_error_message.append(message)

                    _file_type = message['file_type']  # nef/nmr-star/unknown

                    input_source = self._reg.report.input_sources[file_path_list_len]
                    input_source_dic = input_source.get()

                    file_name = input_source_dic['file_name']
                    file_type = input_source_dic['file_type']

                    if MR_FILE_PATH_LIST_KEY in self._reg.outputParamDict:
                        if file_path_list_len - self._reg.cs_file_path_list_len <\
                           len(self._reg.outputParamDict[MR_FILE_PATH_LIST_KEY]):
                            dstPath = self._reg.outputParamDict[MR_FILE_PATH_LIST_KEY][
                                file_path_list_len - self._reg.cs_file_path_list_len]
                            if dstPath is not None and dstPath not in self._reg.inputParamDict[MR_FILE_PATH_LIST_KEY]:
                                shutil.copyfile(mrPath, dstPath)

                    if is_valid:

                        if _file_type != file_type:

                            err = f"{file_name!r} was selected as {READABLE_FILE_TYPE[file_type]} file, "\
                                  f"but recognized as {READABLE_FILE_TYPE[_file_type]} file."
                            # DAOTHER-5673
                            err += " Please re-upload the NEF file as an NMR unified data file." if _file_type == 'nef'\
                                else " Please re-upload the file."

                            if len(message['error']) > 0:
                                for err_message in message['error']:
                                    if 'No such file or directory' not in err_message:
                                        err += ' ' + re.sub('not in list', 'unknown item.', err_message)

                            self._reg.report.error.appendDescription('content_mismatch',
                                                                     {'file_name': file_name, 'description': err})

                            if self._reg.verbose:
                                self._reg.log.write(f"+{self.__class_name__}.validateInputSource() "
                                                    f"++ Error  - {err}\n")

                            return False

                        _is_done, star_data_type, star_data = self._reg.nefT.read_input_file(mrPath)

                        self._reg.has_legacy_sf_issue = False

                        if star_data_type == 'Saveframe':
                            self._reg.has_legacy_sf_issue = True

                            self._reg.dpA.fixFormatIssueOfInputSource(file_path_list_len, file_name, file_type,
                                                                      mrPath, file_subtype, message,
                                                                      hasLegacySfIssue=self._reg.has_legacy_sf_issue)

                            _is_done, star_data_type, star_data = self._reg.nefT.read_input_file(mrPath)

                        self._reg.star_data_type.append(star_data_type)
                        self._reg.star_data.append(star_data)

                        if not (self._reg.has_legacy_sf_issue and _is_done and star_data_type == 'Entry'):
                            if len(self._reg.star_data_type) > file_path_list_len:
                                self._reg.star_data_type[file_path_list_len] = star_data_type
                                self._reg.star_data[file_path_list_len] = star_data
                            else:

                                self._reg.dpA.rescueFormerNef(file_path_list_len)
                                self._reg.dpA.rescueImmatureStr(file_path_list_len)

                        if not _is_done:
                            pass

                    else:

                        if not self._reg.dpA.fixFormatIssueOfInputSource(file_path_list_len, file_name, file_type,
                                                                         mrPath, file_subtype, message,
                                                                         hasLegacySfIssue=self._reg.has_legacy_sf_issue):
                            pass

                    file_path_list_len += 1

                    if _mrPath is not None:
                        try:
                            os.remove(_mrPath)
                        except OSError:
                            pass

            return True

        def proc_ar_file_path_list():

            if AR_FILE_PATH_LIST_KEY in self._reg.inputParamDict:

                for ar in self._reg.inputParamDict[AR_FILE_PATH_LIST_KEY]:
                    arPath = ar['file_name']

                    if arPath.endswith('.gz'):

                        _arPath = os.path.splitext(arPath)[0]

                        if not os.path.exists(_arPath):

                            try:

                                uncompress_gzip_file(arPath, _arPath)

                            except Exception as e:  # pylint: disable=broad-exception-caught

                                self._reg.report.error.appendDescription('internal_error',
                                                                         f"+{self.__class_name__}.validateInputSource() "
                                                                         "++ Error  - " + str(e))

                                if self._reg.verbose:
                                    self._reg.log.write(f"+{self.__class_name__}.validateInputSource() "
                                                        f"++ Error  - {str(e)}\n")

                                return False

                        arPath = _arPath

                    codec = detect_bom(arPath, 'utf-8')

                    if codec != 'utf-8':
                        arPath_ = self.getNextPath(arPath)
                        convert_codec(arPath, arPath_, codec, 'utf-8')
                        arPath = arPath_

                    if is_rtf_file(arPath):
                        arPath_ = self.getNextPath(arPath, '.rtf2txt')
                        convert_rtf_to_ascii(arPath, arPath_)
                        arPath = arPath_

                    ar['file_name'] = arPath

            return True

        def proc_ac_file_path_list():

            if AC_FILE_PATH_LIST_KEY in self._reg.inputParamDict and self._reg.conversion_server:

                for acs in self._reg.inputParamDict[AC_FILE_PATH_LIST_KEY]:
                    acsPath = acs['file_name']

                    codec = detect_bom(acsPath, 'utf-8')

                    if codec != 'utf-8':
                        acsPath_ = self.getNextPath(acsPath)
                        convert_codec(acsPath, acsPath_, codec, 'utf-8')
                        acsPath = acsPath_

                    if is_rtf_file(acsPath):
                        acsPath_ = self.getNextPath(acsPath, '.rtf2txt')
                        convert_rtf_to_ascii(acsPath, acsPath_)
                        acsPath = acsPath_

                    acs['file_name'] = acsPath

        def post_internal_processing():

            if not self._reg.bmrb_only or not self._reg.internal_mode:
                return

            if self._reg.combined_mode and self._reg.op == 'nmr-cs-mr-merge'\
               and CS_FILE_PATH_LIST_KEY in self._reg.inputParamDict\
               and len(self._reg.inputParamDict[CS_FILE_PATH_LIST_KEY]) > 0:
                src_cs_sfs = []
                cs_list_id = 0
                for csListId in range(len(self._reg.inputParamDict[CS_FILE_PATH_LIST_KEY])):
                    _csListId = csListId + 1
                    if _csListId == 1:
                        dst_sf_category_list, _ = self._reg.nefT.get_inventory_list(self._reg.star_data[0])
                        if 'assigned_chemical_shifts' in dst_sf_category_list:
                            src_cs_sfs = self._reg.star_data[0].get_saveframes_by_category('assigned_chemical_shifts')
                            for sf in src_cs_sfs:
                                self._reg.star_data[0].remove_saveframe(sf.name)
                    if _csListId < len(self._reg.star_data) and self._reg.star_data_type[_csListId] == 'Entry'\
                       and self._reg.star_data[_csListId] is not None:
                        src_sf_category_list, _ = self._reg.nefT.get_inventory_list(self._reg.star_data[_csListId])
                        # copy cs data of the annotated cs file to the master template
                        if 'assigned_chemical_shifts' in src_sf_category_list:
                            for sf in self._reg.star_data[_csListId].get_saveframes_by_category('assigned_chemical_shifts'):
                                if cs_list_id < len(src_cs_sfs):
                                    for src_cs_lp in src_cs_sfs[cs_list_id]:
                                        if not any(True for lp in sf if lp.category == src_cs_lp.category):
                                            sf.add_loop(src_cs_lp)
                                self._reg.star_data[0].add_saveframe(sf)
                                self._reg.star_data[_csListId].remove_saveframe(sf.name)
                                cs_list_id += 1

            elif CS_FILE_PATH_LIST_KEY in self._reg.inputParamDict\
                    and len(self._reg.inputParamDict[CS_FILE_PATH_LIST_KEY]) > 1:
                for csListId in range(len(self._reg.inputParamDict[CS_FILE_PATH_LIST_KEY])):
                    if csListId == 0:
                        dst_sf_category_list, _ = self._reg.nefT.get_inventory_list(self._reg.star_data[0])
                        if 'assigned_chemical_shifts' in dst_sf_category_list:
                            for sf in self._reg.star_data[0].get_saveframes_by_category('assigned_chemical_shifts'):
                                self._reg.star_data[0].remove_saveframe(sf.name)
                        continue
                    if csListId < len(self._reg.star_data) and self._reg.star_data_type[csListId] == 'Entry'\
                       and self._reg.star_data[csListId] is not None:
                        src_sf_category_list, _ = self._reg.nefT.get_inventory_list(self._reg.star_data[csListId])

                        # copy cs data of the annotated cs file to the master template
                        if 'assigned_chemical_shifts' in src_sf_category_list:
                            for _sf in self._reg.star_data[csListId].get_saveframes_by_category('assigned_chemical_shifts'):
                                self._reg.star_data[0].add_saveframe(_sf)
                                self._reg.star_data[csListId].remove_saveframe(_sf.name)

            if self._reg.srcNmrCifPath is not None:

                is_valid, message = self._reg.nefT.validate_file(self._reg.srcNmrCifPath, 'A')  # 'A' for NMR unified data

                _file_type = message['file_type']  # nef/nmr-star/unknown

                file_type = 'nmr-star'

                if is_valid:

                    if _file_type == file_type:

                        _is_done, _star_data_type, _star_data = self._reg.nefT.read_input_file(self._reg.srcNmrCifPath)

                        if _is_done and _star_data_type == 'Entry' and is_done and self._reg.star_data_type[0] == 'Entry':

                            self._reg.nmr_cif_sf_category_list, _ = self._reg.nefT.get_inventory_list(_star_data)
                            dst_sf_category_list, _ = self._reg.nefT.get_inventory_list(self._reg.star_data[0])
                            self._reg.orig_cst_sf = None

                            # give priority to cs data of the combined file over ones of the cs-annotate file
                            if 'assigned_chemical_shifts' in self._reg.nmr_cif_sf_category_list:
                                if 'assigned_chemical_shifts' in dst_sf_category_list:
                                    dst_sf_tags = []
                                    for sf in self._reg.star_data[0].get_saveframes_by_category('assigned_chemical_shifts'):
                                        dst_sf_tags.append(copy.copy(sf.tags))
                                        self._reg.star_data[0].remove_saveframe(sf.name)
                                for idx, _sf in enumerate(_star_data.get_saveframes_by_category('assigned_chemical_shifts')):
                                    if idx < len(dst_sf_tags):
                                        for tag in dst_sf_tags[idx]:
                                            if tag[0] not in EMPTY_VALUE and len(get_first_sf_tag(_sf, tag[0])) == 0:
                                                set_sf_tag(_sf, tag[0], tag[1])
                                    self._reg.star_data[0].add_saveframe(_sf)

                            # move restraints of the combined file to the primary file
                            for src_sf_category in self._reg.nmr_cif_sf_category_list:
                                if src_sf_category == 'assigned_chemical_shifts':
                                    continue
                                if src_sf_category == 'constraint_statistics':
                                    for _sf in _star_data.get_saveframes_by_category(src_sf_category):
                                        self._reg.orig_cst_sf = _sf
                                        break
                                    continue
                                if src_sf_category not in dst_sf_category_list:
                                    for _sf in _star_data.get_saveframes_by_category(src_sf_category):
                                        for sf in self._reg.star_data[0].frame_list:
                                            if sf.name == _sf.name:
                                                self._reg.star_data[0].remove_saveframe(_sf.name)
                                                break
                                        self._reg.star_data[0].add_saveframe(_sf)

        if self._reg.combined_mode:

            self._reg.spareDirPath = os.path.dirname(srcPath)
            if self._reg.dirPath is None:
                self._reg.dirPath = self._reg.spareDirPath

            if os.path.exists(srcPath):
                codec = detect_bom(srcPath, 'utf-8')

                _srcPath = None

                if codec != 'utf-8':
                    _srcPath = self.getNextPath(srcPath)
                    convert_codec(srcPath, _srcPath, codec, 'utf-8')
                    srcPath = _srcPath

                if is_rtf_file(srcPath):
                    _srcPath = self.getNextPath(srcPath, '.rtf2txt')
                    convert_rtf_to_ascii(srcPath, _srcPath)
                    srcPath = _srcPath

            # The previous NMR unified data, e.g. the one that 'nmr-str2str-deposit' has just written and now
            # re-reads as the next version, has been dropped from star_data, but it is still reachable through
            # reference cycles (a plain pynmrstar entry is not cyclic; the cycles come from the surrounding data),
            # and the full collection that frees it runs rarely once the heap is large. Collect it before the
            # new entry is parsed: on a 32 MB entry that is 450k objects, 1226 MB -> 666 MB (DAOTHER-7829, 9785).
            if os.path.exists(srcPath) and os.path.getsize(srcPath) >= MIN_INPUT_SIZE_FOR_GC:
                gc.collect(2)
                trim_heap()

            is_valid, message = self._reg.nefT.validate_file(srcPath, 'A')  # 'A' for NMR unified data

            if not is_valid:

                _srcPath = self.getNextPath(srcPath, '.cif2str')
                if self._reg.c2S.convert(srcPath, _srcPath):
                    is_valid, message = self._reg.nefT.validate_file(_srcPath, 'A')  # 'A' for NMR unified data
                    self._reg.srcPath = srcPath = _srcPath

            self._reg.original_error_message.append(message)

            _file_type = message['file_type']  # nef/nmr-star/unknown

            input_source = self._reg.report.input_sources[0]
            input_source_dic = input_source.get()

            file_name = input_source_dic['file_name']
            file_type = input_source_dic['file_type']

            if is_valid:

                if _file_type != file_type:

                    err = f"{file_name!r} was selected as {READABLE_FILE_TYPE[file_type]} file, "\
                          f"but recognized as {READABLE_FILE_TYPE[_file_type]} file. Please re-upload the file."

                    if len(message['error']) > 0:
                        for err_message in message['error']:
                            if 'No such file or directory' not in err_message:
                                err += ' ' + re.sub('not in list', 'unknown item.', err_message)

                    self._reg.report.error.appendDescription('content_mismatch',
                                                             {'file_name': file_name, 'description': err})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.validateInputSource() "
                                            f"++ Error  - {err}\n")

                    is_done = False

                else:

                    is_done, star_data_type, star_data = self._reg.nefT.read_input_file(srcPath)

                    if len(self._reg.star_data_type) > 0:
                        del self._reg.star_data_type[-1]
                        del self._reg.star_data[-1]

                    self._reg.star_data_type.append(star_data_type)
                    self._reg.star_data.append(star_data)

                    self._reg.dpA.rescueFormerNef(0)
                    self._reg.dpA.rescueImmatureStr(0)

            else:

                is_done = False

                if self._reg.op == 'nmr-str-replace-cs'\
                   or (self._reg.op == 'nmr-cs-mr-merge' and self._reg.bmrb_only and self._reg.internal_mode
                       and CS_FILE_PATH_LIST_KEY in self._reg.inputParamDict):
                    is_done, star_data_type, star_data = self._reg.nefT.read_input_file(srcPath)
                    if is_done and star_data_type == 'Entry':
                        self._reg.star_data_type.append(star_data_type)
                        self._reg.star_data.append(star_data)

                        self._reg.dpA.rescueFormerNef(0)
                        self._reg.dpA.rescueImmatureStr(0)

                if not is_done and not self._reg.dpA.fixFormatIssueOfInputSource(0, file_name, file_type, srcPath, 'A', message):

                    if any(True for err_message in message['error'] if 'The mandatory loop' in err_message):

                        _, star_data_type, star_data = self._reg.nefT.read_input_file(srcPath)

                        if len(self._reg.star_data_type) > 0:
                            del self._reg.star_data_type[-1]
                            del self._reg.star_data[-1]

                        self._reg.star_data_type.append(star_data_type)
                        self._reg.star_data.append(star_data)

                        self._reg.dpA.rescueFormerNef(0)
                        self._reg.dpA.rescueImmatureStr(0)

                    is_done = False

            if _srcPath is not None and not self._reg.submission_mode and not self._reg.annotation_mode:
                try:
                    os.remove(_srcPath)
                except OSError:
                    pass

            if is_done and file_type == 'nmr-star':
                for sf in self._reg.star_data[0].get_saveframes_by_category('assembly'):
                    self._reg.assembly_name = get_first_sf_tag(sf, 'Name', '?')
                    details = get_first_sf_tag(sf, 'Details')
                    if details not in EMPTY_VALUE and WS_PAT.match(details):
                        set_sf_tag(sf, 'Details', None)
                    break

            if self._reg.op == 'nmr-str-replace-cs'\
               or (self._reg.op == 'nmr-cs-mr-merge' and self._reg.conversion_server):  # DAOTHER-9785:
                if self._reg.internal_mode and self._reg.combined_mode\
                   and CS_FILE_PATH_LIST_KEY not in self._reg.inputParamDict:
                    pass
                elif not proc_cs_path_path_list(1):
                    return False

            # DAOTHER-9785
            if self._reg.op == 'nmr-cs-mr-merge' and self._reg.bmrb_only and self._reg.internal_mode:
                if not proc_mr_file_path_list():
                    return False

                if not proc_ar_file_path_list():
                    return False

                proc_ac_file_path_list()

                post_internal_processing()

        else:

            if not proc_cs_path_path_list(0):
                return False

            if not proc_mr_file_path_list():
                return False

            if not proc_ar_file_path_list():
                return False

            proc_ac_file_path_list()

            post_internal_processing()

        # release cached input data on NefTranslator because there is no chance
        # to read the same file hereafter
        self._reg.nefT.release()

        return is_done

    def _convertCsToEntry(self, src_data: Optional[Union[pynmrstar.Entry, pynmrstar.Saveframe, pynmrstar.Loop]] = None,
                          list_id: int = 1
                          ) -> Optional[pynmrstar.Entry]:
        """ Convert NMR-STAR CS loop/saveframe to pynmrstar Entry object.
        """

        if src_data is None:
            return None

        file_type = 'nmr-star'

        def update_entry_info_saveframe(master_entry):
            content_subtype = 'entry_info'

            sf_category = SF_CATEGORIES[file_type][content_subtype]

            orig_ent_sf = next((sf for sf in master_entry.frame_list if sf_category in (sf.category, sf.name)), None)

            if orig_ent_sf is not None:

                tagNames = [t[0] for t in orig_ent_sf.tags]

                if 'Sf_category' not in tagNames:
                    orig_ent_sf.add_tag('Sf_category', sf_category)
                if 'Sf_framecode' not in tagNames:
                    orig_ent_sf.add_tag('Sf_framecode', orig_ent_sf.name)
                set_sf_tag(orig_ent_sf, 'ID', self._reg.entry_id)

            else:

                ent_sf = pynmrstar.Saveframe.from_scratch(sf_category, SF_TAG_PREFIXES[file_type][content_subtype])
                ent_sf.add_tag('Sf_category', sf_category)
                ent_sf.add_tag('Sf_framecode', sf_category)
                ent_sf.add_tag('ID', self._reg.entry_id)

                master_entry.add_saveframe(ent_sf)

            return master_entry

        if isinstance(src_data, pynmrstar.Entry):
            return update_entry_info_saveframe(src_data)

        content_subtype = 'chem_shift'

        master_entry = pynmrstar.Entry.from_scratch(self._reg.entry_id)

        if isinstance(src_data, (pynmrstar.Saveframe, pynmrstar.Loop)):

            if isinstance(src_data, pynmrstar.Saveframe):
                set_sf_tag(src_data, 'Sf_category', SF_CATEGORIES[file_type][content_subtype])
                set_sf_tag(src_data, 'Entry_ID', self._reg.entry_id)
                set_sf_tag(src_data, 'ID', list_id)
                set_sf_tag(src_data, 'Data_file_name', self._reg.srcName)

                master_entry.add_saveframe(src_data)

            else:
                sf_framecode = f'assigned_chemical_shifts_{list_id}'
                sf_tag_prefix = SF_TAG_PREFIXES[file_type][content_subtype]

                acs_sf = pynmrstar.Saveframe.from_scratch(sf_framecode, sf_tag_prefix)

                acs_sf.add_tag('Sf_category', SF_CATEGORIES[file_type][content_subtype])
                acs_sf.add_tag('Sf_framecode', sf_framecode)
                acs_sf.add_tag('Entry_ID', self._reg.entry_id)
                acs_sf.add_tag('ID', list_id)
                acs_sf.add_tag('Data_file_name', self._reg.srcName)

                acs_sf.add_loop(src_data)

                master_entry.add_saveframe(acs_sf)

            src_data = update_entry_info_saveframe(master_entry)

        return src_data

    def detectContentSubType(self) -> bool:
        """ Detect content subtype of NMR data file in any STAR format.
        """

        if len(self._reg.star_data) != self._reg.file_path_list_len:
            return False

        for fileListId in range(self._reg.file_path_list_len):

            input_source = self._reg.report.input_sources[fileListId]

            self.detectContentSubType__(fileListId, input_source, self._reg.dirPath)

        return not self._reg.report.isError()

    def detectContentSubType__(self, file_list_id: int, input_source: NmrDpReportInputSource,
                               dir_path: Optional[str] = None) -> None:
        """ Detect content subtype of NMR data file in any STAR format.
        """

        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']
        content_type = input_source_dic['content_type']

        if input_source_dic['content_subtype'] is not None:
            return

        self._reg.sf_category_list, self._reg.lp_category_list =\
            self._reg.nefT.get_inventory_list(self._reg.star_data[file_list_id])

        if self._reg.combined_mode and file_list_id == 0 and file_type == 'nmr-star'\
           and 'constraint_statistics' in self._reg.sf_category_list\
           and '_Constraint_file' in self._reg.lp_category_list:
            _sf = self._reg.star_data[file_list_id].get_saveframes_by_category('constraint_statistics')[0]
            data_file_name = get_first_sf_tag(_sf, 'Data_file_name')
            if PDB_MR_FILE_NAME_PAT.match(data_file_name) or INTNL_ANY_MR_FILE_NAME_PAT.match(data_file_name):
                entry_id = get_first_sf_tag(_sf, 'Entry_ID')
                if (PDB_ID_PAT.match(entry_id) or DEP_ID_PAT.match(entry_id))\
                   and self._reg.op != 'nmr-str2cif-annotate':  # DAOTHER-10616
                    self._reg.remediation_mode = True
                    self._reg.nefT.set_remediation_mode(True)

        is_valid, messages, corrections =\
            self._reg.nefT.resolve_sf_names_for_cif(self._reg.star_data[file_list_id])  # DAOTHER-7389, issue #4
        self._reg.sf_name_corrections.append(corrections)

        if not is_valid:

            for warn in messages:
                self._reg.report.warning.appendDescription('corrected_saveframe_name',
                                                           {'file_name': file_name, 'description': warn})

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.detectContentSubType() ++ Warning  - {warn}\n")

        tags_with_null_str = []

        for sf_category in self._reg.sf_category_list:  # DAOTHER-5896

            for sf in self._reg.star_data[file_list_id].get_saveframes_by_category(sf_category):

                if file_type == 'nmr-star' and sf_category == 'assembly' and self._reg.assembly_name in EMPTY_VALUE:
                    self._reg.assembly_name = get_first_sf_tag(sf, 'Name', '?')

                for tag in sf.tags:
                    if isinstance(tag[1], str) and len(tag[1]) == 0:
                        tags_with_null_str.append(f'_{sf_category}.{tag[0]}')
                        tag[1] = '.'

        if len(tags_with_null_str) > 0:

            warn = f"Empty strings for {tags_with_null_str} are not allowed as values. Use a '.' or a '?' if needed."

            self._reg.report.warning.appendDescription('corrected_format_issue',
                                                       {'file_name': file_name, 'description': warn})

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.detectContentSubType() ++ Warning  - {warn}\n")

        for sf_category in self._reg.sf_category_list:

            if file_type == 'nmr-star' and sf_category == 'entity':
                self._reg.has_star_entity = True

            if sf_category is not None and sf_category not in SF_CATEGORIES[file_type].values():

                if not self._reg.bmrb_only:

                    if file_type == 'nef':
                        warn = f"Ignored third party software's saveframe {sf_category!r}."
                    else:

                        if sf_category == 'constraint_statistics':
                            continue

                        warn = f"Ignored saveframe category {sf_category!r}."

                    self._reg.report.warning.appendDescription('skipped_saveframe_category',
                                                               {'file_name': file_name, 'sf_category': sf_category,
                                                                'description': warn})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.detectContentSubType() ++ Warning  - {warn}\n")

        # initialize loop counter
        lp_counts = {t: 0 for t in NMR_CONTENT_SUBTYPES}

        # increment loop counter of each content subtype
        for lp_category in self._reg.lp_category_list:
            if lp_category in LP_CATEGORIES[file_type].values():
                lp_counts[[k for k, v in LP_CATEGORIES[file_type].items() if v == lp_category][0]] += 1

        if file_type == 'nmr-star' and lp_counts['spectral_peak'] + lp_counts['spectral_peak_alt'] == 0\
           and '_Spectral_dim' in self._reg.lp_category_list:
            lp_counts['spectral_peak'] = self._reg.lp_category_list.count('_Spectral_dim')

        content_subtype = 'poly_seq'

        lp_category = LP_CATEGORIES[file_type][content_subtype]

        if lp_counts[content_subtype] == 0:

            if not self._reg.has_star_entity and self._reg.combined_mode:

                if self._reg.resolve_conflict and self._reg.update_poly_seq:  # DAOTHER-6694
                    warn = f"A saveframe with a category {lp_category!r} is missing in the NMR data."

                    self._reg.report.warning.appendDescription('missing_saveframe',
                                                               {'file_name': file_name, 'description': warn})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.detectContentSubType() ++ Warning  - {warn}\n")

                elif not self._reg.remediation_mode:
                    err = f"A saveframe with a category {lp_category!r} is missing. Please re-upload the {file_type.upper()} file."

                    if self._reg.validation_server and lp_category == '_Chem_comp_assembly':
                        err = f"A saveframe with a category {lp_category!r} is missing "\
                            f"that indicates {file_name!r} is not NMR unified data file. "\
                            f"Please re-upload the file as an usual assigned chemical shift file."

                    self._reg.report.error.appendDescription('missing_mandatory_content',
                                                             {'file_name': file_name, 'description': err})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.detectContentSubType() ++ Error  - {err}\n")

            elif lp_counts['chem_shift'] == 0 and lp_counts['dist_restraint'] > 0 and content_type != 'nmr-restraints':
                err = f"A saveframe with a category {lp_category!r} is missing. Please re-upload the {file_type.upper()} file."

                self._reg.report.error.appendDescription('missing_mandatory_content',
                                                         {'file_name': file_name, 'description': err})

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.detectContentSubType() ++ Error  - {err}\n")

        elif lp_counts[content_subtype] > 1:

            err = f"Unexpectedly, multiple saveframes having {lp_category!r} category exist."

            self._reg.report.error.appendDescription('format_issue',
                                                     {'file_name': file_name, 'description': err})

            self._reg.log.write(f"+{self.__class_name__}.detectContentSubType() ++ Error  - "
                                f"{file_name} {err}\n")

        if self._reg.remediation_mode and not self._reg.bmrb_only:

            if content_type == 'nmr-restraints':

                for content_subtype in ('entry_info', 'poly_seq', 'entity', 'chem_shift', 'chem_shift_ref'):

                    sf_category = SF_CATEGORIES[file_type][content_subtype]

                    if sf_category is None or lp_counts[content_subtype] == 0:
                        continue

                    for sf in self._reg.star_data[file_list_id].get_saveframes_by_category(sf_category):

                        if content_subtype == 'chem_shift' and not self._reg.has_star_chem_shift:
                            if self._reg.star_data[0] is None:
                                self._reg.star_data[0] = pynmrstar.Entry.from_scratch(self._reg.entry_id)
                                self._reg.star_data_type[0] = 'Entry'

                            if sf not in self._reg.star_data[0].frame_list:
                                self._reg.star_data[0].add_saveframe(sf)

                                input_source_ = self._reg.report.input_sources[0]
                                input_source_dic_ = input_source_.get()
                                content_subtypes_ = input_source_dic_['content_subtype']

                                if content_subtypes_ is None:
                                    content_subtypes_ = {content_subtype: 0}

                                content_subtypes_[content_subtype] += 1

                                input_source_.setItemValue('content_subtype', content_subtypes_)

                                for idx, msg in enumerate(self._reg.suspended_errors_for_lazy_eval):
                                    for k, v in msg.items():
                                        if k == 'missing_mandatory_content':
                                            del self._reg.suspended_errors_for_lazy_eval[idx]
                                            break

                            cs = self._reg.inputParamDict[CS_FILE_PATH_LIST_KEY][0]

                            if isinstance(cs, str):
                                cs_path = cs
                            else:
                                cs_path = cs['file_name']

                            if dir_path is None:
                                dir_path = os.path.dirname(cs_path)

                            cs_file_name = os.path.basename(cs_path)

                            if cs_file_name.endswith('.cif2str'):
                                cs_file_name = os.path.splitext(cs_file_name)[0]

                            if cs_file_name.endswith('.str'):
                                cs_file_name = os.path.splitext(cs_file_name)[0]

                            if cs_file_name.endswith('-corrected'):
                                cs_file_name = cs_file_name[:-10]

                            cs_base_name = cs_file_name
                            cs_file_path = self.testPathWithSuffix(os.path.join(dir_path, cs_base_name), '-corrected.str')

                            if not os.path.exists(cs_file_path):
                                self._reg.star_data[0].write_to_file(cs_file_path,
                                                                     show_comments=False,
                                                                     skip_empty_loops=True,
                                                                     skip_empty_tags=False)

                                compress_as_gzip_file(cs_file_path, f'{cs_file_path}.gz')

                            rem_dir = os.path.join(dir_path, 'remediation')

                            try:

                                if not os.path.isdir(rem_dir):
                                    os.makedirs(rem_dir)

                                cs_file_link = os.path.join(rem_dir, f'{cs_base_name}.str')

                                if os.path.exists(cs_file_link):
                                    os.remove(cs_file_link)

                                os.symlink(cs_file_path, cs_file_link)

                            except OSError:
                                pass

                        self._reg.star_data[file_list_id].remove_saveframe(sf.name)

                    lp_counts[content_subtype] = 0

            elif content_type == 'nmr-chemical-shifts' and BMRB_NMR_STAR_FILE_NAME_PAT.match(file_name):

                for content_subtype in NMR_CONTENT_SUBTYPES:

                    if content_subtype == 'chem_shift':
                        continue

                    sf_category = SF_CATEGORIES[file_type][content_subtype]

                    if sf_category is None or lp_counts[content_subtype] == 0:
                        continue

                    for sf in self._reg.star_data[file_list_id].get_saveframes_by_category(sf_category):
                        self._reg.star_data[file_list_id].remove_saveframe(sf.name)

                    lp_counts[content_subtype] = 0

        content_subtype = 'chem_shift'

        if lp_counts[content_subtype] == 0 and self._reg.combined_mode:

            sf_category = SF_CATEGORIES[file_type][content_subtype]
            lp_category = LP_CATEGORIES[file_type][content_subtype]

            if self._reg.op != 'nmr-str-replace-cs' or not self._reg.bmrb_only:

                err = f"The saveframe with a category {sf_category!r} is missing. "\
                    f"Deposition of assigned chemical shifts is mandatory. Please re-upload the {file_type.upper()} file."

                self._reg.report.error.appendDescription('missing_mandatory_content',
                                                         {'file_name': file_name, 'description': err})

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.detectContentSubType() ++ Error  - {err}\n")

            if self._reg.remediation_mode and dir_path is not None:
                touch_file = os.path.join(dir_path, '.entry_without_cs')
                if not os.path.exists(touch_file):
                    with open(touch_file, 'w', encoding='utf-8') as ofh:
                        ofh.write('')

        if lp_counts[content_subtype] > 0 and content_type == 'nmr-restraints' and not self._reg.bmrb_only:

            if self._reg.remediation_mode\
               and lp_counts['dist_restraint'] + lp_counts['dihed_restraint'] + lp_counts['rdc_restraint'] > 0:

                warn = "The restraint file includes assigned chemical shifts. "\
                    "which will be ignored during remediation."

                self._reg.report.warning.appendDescription('corrected_format_issue',
                                                           {'file_name': file_name, 'description': warn})

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.detectContentSubType() ++ Warning  - {warn}\n")

            else:

                err = "The restraint file includes assigned chemical shifts. "\
                    f"Please re-upload the {file_type.upper()} file as an NMR unified data file."

                self._reg.report.error.appendDescription('content_mismatch',
                                                         {'file_name': file_name, 'description': err})

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.detectContentSubType() ++ Error  - {err}\n")

        content_subtype = 'dist_restraint'

        if lp_counts[content_subtype] == 0 and self._reg.combined_mode and file_list_id == 0 and not self._reg.conversion_server:

            sf_category = SF_CATEGORIES[file_type][content_subtype]
            lp_category = LP_CATEGORIES[file_type][content_subtype]

            if self._reg.permit_missing_dist_restraint:

                warn = f"The saveframe with a category {sf_category!r} is missing. "\
                       "The wwPDB NEF Working Group strongly recommends the submission of distance restraints "\
                       "used for the structure determination."

                if 'noepk_restraint' in lp_counts and lp_counts['noepk_restraint'] > 0:
                    warn += " '_Homonucl_NOE' category is only useful for describing assigned NOE peak height/volume. "\
                        "Please use the '_Gen_dist_constraint' category to describe general distance restraint."

                if 'other_data_types' in self._reg.sf_category_list:
                    sf_framecodes_wo_loop = []
                    for sf in self._reg.star_data[file_list_id].get_saveframes_by_category('other_data_types'):

                        try:
                            loop = sf.get_loop('_Other_data')
                        except KeyError:
                            sf_framecodes_wo_loop.append(get_first_sf_tag(sf, 'sf_framecode'))
                            continue

                        if loop is None:
                            sf_framecodes_wo_loop.append(get_first_sf_tag(sf, 'sf_framecode'))

                    if len(sf_framecodes_wo_loop) > 0:
                        _sf_framecodes_wo_loop = "', '".join(sf_framecodes_wo_loop)
                        warn += f" Uninterpreted restraints are stored in {_sf_framecodes_wo_loop!r} "\
                            f"saveframe{'s' if len(sf_framecodes_wo_loop) > 1 else ''} as raw text format. "\
                            "Please consider incorporating those restraints into well-known formats "\
                            "that OneDep supports, if possible."

                self._reg.report.warning.appendDescription('missing_content',
                                                           {'file_name': file_name, 'description': warn})

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.detectContentSubType() ++ Warning  - {warn}\n")

            elif not self._reg.validation_server:

                err = f"The saveframe with a category {sf_category!r} is missing. "\
                    f"Deposition of distance restraints is mandatory. Please re-upload the {file_type.upper()} file."

                self._reg.report.error.appendDescription('missing_mandatory_content',
                                                         {'file_name': file_name, 'description': err})

                if self._reg.verbose:
                    self._reg.log.write(f"+{self.__class_name__}.detectContentSubType() ++ Error  - {err}\n")

        if (lp_counts['dist_restraint'] > 0 or lp_counts['dihed_restraint'] or lp_counts['rdc_restraint'])\
           and content_type == 'nmr-chemical-shifts' and not self._reg.bmrb_only and not self._reg.internal_mode:

            err = "The assigned chemical shift file includes restraints. "\
                f"Please re-upload the {file_type.upper()} file as an NMR unified data file."

            self._reg.report.error.appendDescription('content_mismatch',
                                                     {'file_name': file_name, 'description': err})

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.detectContentSubType() ++ Error  - {err}\n")

        has_spectral_peak = lp_counts['spectral_peak'] + lp_counts['spectral_peak_alt'] > 0

        if not has_spectral_peak and self._reg.remediation_mode:
            if 'spectral_peak_list' in self._reg.sf_category_list:
                has_spectral_peak = True

        if not has_spectral_peak and self._reg.combined_mode and file_list_id == 0 and not self._reg.conversion_server:

            primary_spectra_for_structure_determination =\
                'NOESY or ROESY' if self._reg.exptl_method != 'SOLID-STATE NMR' else 'DARR, REDOR, TEDOR or RFDR'

            warn = "The wwPDB NMR Validation Task Force strongly encourages the submission of spectral peak lists, "\
                f"in particular those generated from the {primary_spectra_for_structure_determination} spectra."

            self._reg.report.warning.appendDescription('encouragement',
                                                       {'file_name': file_name, 'description': warn})

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.detectContentSubType() ++ Warning  - {warn}\n")

        if has_spectral_peak and content_type == 'nmr-chemical-shifts'\
           and not self._reg.bmrb_only and not self._reg.internal_mode:

            err = "The assigned chemical shift file includes spectral peak lists. "\
                f"Please re-upload the {file_type.upper()} file as an NMR unified data file."

            self._reg.report.error.appendDescription('content_mismatch',
                                                     {'file_name': file_name, 'description': err})

            if self._reg.verbose:
                self._reg.log.write(f"+{self.__class_name__}.detectContentSubType() ++ Error  - {err}\n")

            if self._reg.remediation_mode and dir_path is not None:
                touch_file = os.path.join(dir_path, '.entry_with_pk')
                if not os.path.exists(touch_file):
                    with open(touch_file, 'w', encoding='utf-8') as ofh:
                        ofh.write('')

        if self._reg.combined_mode and file_list_id == 0:

            mr_loops = 0

            for content_subtype in self._reg.mr_content_subtypes:
                if content_subtype in lp_counts:
                    mr_loops += lp_counts[content_subtype]

            if mr_loops == 0 and not self._reg.validation_server and not self._reg.bmrb_only:

                if 'other_data_types' not in self._reg.sf_category_list:

                    err = "Deposition of restraints used for the structure determination is mandatory. "\
                        f"Please re-upload the {file_type.upper()} file."

                    self._reg.report.error.appendDescription('missing_mandatory_content',
                                                             {'file_name': file_name, 'description': err})

                    if self._reg.verbose:
                        self._reg.log.write(f"+{self.__class_name__}.detectContentSubType() ++ Error  - {err}\n")

        content_subtypes = {k: lp_counts[k] for k in lp_counts if lp_counts[k] > 0}

        input_source.setItemValue('content_subtype', content_subtypes)
