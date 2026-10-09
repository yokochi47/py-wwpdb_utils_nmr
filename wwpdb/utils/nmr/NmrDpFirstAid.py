##
# File: NmrDpFirstAid.py
# Date: 07-Jan-2026
#
# Updates:
##
""" First aid kit for NMR data processing.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.3"

import os
import re
import shutil
from typing import List, Optional, Union

from packaging import version

import pynmrstar

try:
    from wwpdb.utils.nmr.NmrDpConstant import (CS_FILE_PATH_LIST_KEY,
                                               MR_FILE_PATH_LIST_KEY,
                                               NMR_CONTENT_SUBTYPES,
                                               READABLE_FILE_TYPE,
                                               SF_CATEGORIES,
                                               LP_CATEGORIES,
                                               INDEX_TAGS,
                                               NUM_DIM_ITEMS,
                                               ERR_TEMPLATE_FOR_MISSING_MANDATORY_LP_TAG,
                                               SF_TAG_PREFIXES,
                                               AUX_LP_CATEGORIES,
                                               EMPTY_VALUE,
                                               NEF_VERSION,
                                               MAX_DIM_NUM_OF_SPECTRA,
                                               ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                               DATABLOCK_PAT,
                                               SAVE_PAT,
                                               LOOP_PAT,
                                               STOP_PAT,
                                               CIF_STOP_PAT,
                                               CATEGORY_PAT,
                                               SF_CATEGORY_PAT,
                                               SF_FRAMECODE_PAT)
    from wwpdb.utils.nmr.NmrDpRegistry import (NmrDpRegistry,
                                               get_next_path)
    from wwpdb.utils.nmr.CifToNmrStar import (get_first_sf_tag,
                                              set_sf_tag)
except ImportError:
    from nmr.NmrDpConstant import (CS_FILE_PATH_LIST_KEY,
                                   MR_FILE_PATH_LIST_KEY,
                                   NMR_CONTENT_SUBTYPES,
                                   READABLE_FILE_TYPE,
                                   SF_CATEGORIES,
                                   LP_CATEGORIES,
                                   INDEX_TAGS,
                                   NUM_DIM_ITEMS,
                                   ERR_TEMPLATE_FOR_MISSING_MANDATORY_LP_TAG,
                                   SF_TAG_PREFIXES,
                                   AUX_LP_CATEGORIES,
                                   EMPTY_VALUE,
                                   NEF_VERSION,
                                   MAX_DIM_NUM_OF_SPECTRA,
                                   ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS,
                                   DATABLOCK_PAT,
                                   SAVE_PAT,
                                   LOOP_PAT,
                                   STOP_PAT,
                                   CIF_STOP_PAT,
                                   CATEGORY_PAT,
                                   SF_CATEGORY_PAT,
                                   SF_FRAMECODE_PAT)
    from nmr.NmrDpRegistry import (NmrDpRegistry,
                                   get_next_path)
    from nmr.CifToNmrStar import (get_first_sf_tag,
                                  set_sf_tag)


__pynmrstar_v3_3__ = version.parse(pynmrstar.__version__) >= version.parse("3.3.0")


PYNMRSTAR_LP_OBJ_PAT = re.compile(r"\<pynmrstar\.Loop '(.*)'\>")

ONEDEP_ANY_UPLOAD_FILE_NAME_PAT = re.compile(r'^(\S+)\-upload_(\S+)\.V(\d+)$')
ONEDEP_ANY_FILE_NAME_PAT = re.compile(r'^(\S+)\.V(\d+)$')


class NmrDpFirstAid:
    """ First aid kit for NMR data processing.
    """
    __slots__ = ('__class_name__',
                 '__version__',
                 '__reg')

    def __init__(self, registry: NmrDpRegistry) -> None:
        self.__class_name__ = self.__class__.__name__
        self.__version__ = __version__

        self.__reg = registry

    def getNextPath(self, src_path: str, suffix: str = '~') -> str:
        """ Return candidate next file path.
        """
        return get_next_path(self.__reg, src_path, suffix)

    def fixFormatIssueOfInputSource(self, file_list_id: int, file_name: str, file_type: str,
                                    srcPath: Optional[str] = None, fileSubType: str = 'S',
                                    message: Optional[dict] = None, tmpPaths: Optional[List[str]] = None,
                                    allowEmpty: bool = False, hasLegacySfIssue: bool = False
                                    ) -> bool:
        """ Fix format issue of NMR data.
        """

        if not self.__reg.fix_format_issue or srcPath is None or fileSubType not in ('A', 'S', 'R', 'O') or message is None:

            if message is not None:

                missing_loop = True

                err = f"{file_name!r} is not compliant with the {READABLE_FILE_TYPE[file_type]} dictionary."

                if len(message['error']) > 0:

                    if any(True for err_message in message['error'] if 'The mandatory loop' in err_message):

                        err = ''
                        for err_message in message['error']:
                            if 'No such file or directory' not in err_message:
                                err += re.sub('not in list', 'unknown item.', err_message) + ' '
                        err = err[:-1]

                    else:
                        missing_loop = False

                        for err_message in self.__reg.original_error_message[file_list_id]['error']:
                            if 'No such file or directory' not in err_message:
                                err += ' ' + re.sub('not in list', 'unknown item.', err_message)

                if not self.__reg.remediation_mode or not missing_loop or file_list_id > 0:

                    if self.__reg.op != 'nmr-str-replace-cs' or not self.__reg.bmrb_only:

                        self.__reg.report.error.appendDescription('missing_mandatory_content' if missing_loop else 'format_issue',
                                                                  {'file_name': file_name, 'description': err})

                        self.__reg.log.write(f"+{self.__class_name__}.fixFormatIssueOfInputSource() ++ Error  - "
                                             f"{file_name} {err}\n")

                else:

                    self.__reg.has_star_chem_shift = False

                    if self.__reg.op != 'nmr-str-replace-cs' or not self.__reg.bmrb_only:

                        self.__reg.suspended_errors_for_lazy_eval.append({'missing_mandatory_content':
                                                                          {'file_name': file_name, 'description': err}})

                        if self.__reg.verbose:
                            self.__reg.log.write(f"+{self.__class_name__}.fixFormatIssueOfInputSource() ++ Error  - {err}\n")

            if not hasLegacySfIssue and fileSubType in ('S', 'R', 'O'):
                return False

        star_data_type = self.__reg.nefT.read_input_file(srcPath)[1] if hasLegacySfIssue else None

        _srcPath = srcPath
        if tmpPaths is None:
            tmpPaths = []

        len_tmp_paths = len(tmpPaths)

        msg_template = "Saveframe improperly terminated at end of file."

        if any(True for msg in message['error'] if msg_template in msg):
            warn = msg_template

            self.__reg.report.warning.appendDescription('corrected_format_issue',
                                                        {'file_name': file_name, 'description': warn})

            if self.__reg.verbose:
                self.__reg.log.write(f"+{self.__class_name__}.__validateInputSource() ++ Warning  - {warn}\n")

            _srcPath_next = self.getNextPath(_srcPath)

            with open(_srcPath, 'r', encoding='utf-8') as ifh, \
                    open(_srcPath_next, 'w', encoding='utf-8') as ofh:
                for line in ifh:
                    ofh.write(line)

                ofh.write('save_\n')

                _srcPath = ofh.name
                tmpPaths.append(_srcPath)

        msg_template = "Loop improperly terminated at end of file."

        if any(True for msg in message['error'] if msg_template in msg):
            warn = msg_template

            self.__reg.report.warning.appendDescription('corrected_format_issue',
                                                        {'file_name': file_name, 'description': warn})

            if self.__reg.verbose:
                self.__reg.log.write(f"+{self.__class_name__}.__validateInputSource() ++ Warning  - {warn}\n")

            _srcPath_next = self.getNextPath(_srcPath)

            with open(_srcPath, 'r', encoding='utf-8') as ifh, \
                    open(_srcPath_next, 'w', encoding='utf-8') as ofh:
                for line in ifh:
                    ofh.write(line)

                ofh.write('save_\n')

                _srcPath = ofh.name
                tmpPaths.append(_srcPath)

        msg_template = "Invalid file. NMR-STAR files must start with 'data_' followed by the data name. "\
            "Did you accidentally select the wrong file?"

        if any(True for msg in message['error'] if msg_template in msg) or (hasLegacySfIssue and star_data_type == 'Saveframe'):
            warn = 'The datablock must hook saveframe(s).'

            self.__reg.report.warning.appendDescription('corrected_format_issue',
                                                        {'file_name': file_name, 'description': warn})

            if self.__reg.verbose:
                self.__reg.log.write(f"+{self.__class_name__}.fixFormatIssueOfInputSource() ++ Warning  - {warn}\n")

            with open(_srcPath, 'r', encoding='utf-8') as ifh:
                lines = ifh.read().splitlines()
                total = len(lines)

                j = total - 1

                while total - j < 10:
                    if SAVE_PAT.match(lines[j]) or STOP_PAT.match(lines[j]):
                        break
                    j -= 1

            j += 1
            i = 0

            _srcPath_next = self.getNextPath(_srcPath)

            with open(_srcPath, 'r', encoding='utf-8') as ifh, \
                    open(_srcPath_next, 'w', encoding='utf-8') as ofh:
                ofh.write(f'data_{os.path.basename(srcPath)}\n\n')
                for line in ifh:
                    if i < j:
                        ofh.write(line)
                    i += 1

                _srcPath = ofh.name
                tmpPaths.append(_srcPath)

            # fix single loop file without datablock (D_1300055931)
            _srcPath_next = self.getNextPath(_srcPath)
            if self.__reg.c2S.convert(_srcPath, _srcPath_next):
                _srcPath = _srcPath_next
                tmpPaths.append(_srcPath)

        msg_template = "Only 'save_NAME' is valid in the body of a NMR-STAR file. Found 'loop_'."

        if any(True for msg in message['error'] if msg_template in msg):
            warn = 'A saveframe, instead of the datablock, must hook the loop.'

            self.__reg.report.warning.appendDescription('corrected_format_issue',
                                                        {'file_name': file_name, 'description': warn})

            if self.__reg.verbose:
                self.__reg.log.write(f"+{self.__class_name__}.fixFormatIssueOfInputSource() ++ Warning  - {warn}\n")

            pass_datablock = False

            _srcPath_next = self.getNextPath(_srcPath)

            with open(_srcPath, 'r', encoding='utf-8') as ifh, \
                    open(_srcPath_next, 'w', encoding='utf-8') as ofh:
                for line in ifh:
                    if pass_datablock:
                        ofh.write(line)
                    elif DATABLOCK_PAT.match(line):
                        pass_datablock = True
                    else:
                        ofh.write(line)

                _srcPath = ofh.name
                tmpPaths.append(_srcPath)

        msg_template = "Cannot use keywords as data values unless quoted or semi-colon delimited. "\
            "Perhaps this is a loop that wasn't properly terminated"

        try:

            msg = next(msg for msg in message['error'] if msg_template in msg)
            warn = 'Loops must properly terminated.'

            self.__reg.report.warning.appendDescription('corrected_format_issue',
                                                        {'file_name': file_name, 'description': warn})

            if self.__reg.verbose:
                self.__reg.log.write(f"+{self.__class_name__}.__validateInputSource() ++ Warning  - {warn}\n")

            msg_pattern = re.compile(r'^.*' + msg_template + r".*on line (\d+).*$")

            try:

                g = msg_pattern.search(msg).groups()

                line_num = int(g[0])

                i = 0

                _srcPath_next = self.getNextPath(_srcPath)

                with open(_srcPath, 'r', encoding='utf-8') as ifh, \
                        open(_srcPath_next, 'w', encoding='utf-8') as ofh:
                    for line in ifh:
                        if i == line_num:
                            ofh.write('stop_\n')
                        ofh.write(line)
                        i += 1
                    if i == line_num:
                        ofh.write('stop_\n')

                    _srcPath = ofh.name
                    tmpPaths.append(_srcPath)

            except AttributeError:
                pass

        except StopIteration:
            pass

        msg_template = "Cannot have a tag value start with an underscore unless the entire value is quoted. "\
            "You may be missing a data value on the previous line"

        try:

            msg = next(msg for msg in message['error'] if msg_template in msg)
            warn = "Loops must start with the 'loop_' keyword."

            self.__reg.report.warning.appendDescription('corrected_format_issue',
                                                        {'file_name': file_name, 'description': warn})

            if self.__reg.verbose:
                self.__reg.log.write(f"+{self.__class_name__}.__validateInputSource() ++ Warning  - {warn}\n")

            msg_pattern = re.compile(r'^.*' + msg_template + r".*on line (\d+).*$")

            try:

                g = msg_pattern.search(msg).groups()

                line_num = int(g[0])

                i = 0

                _srcPath_next = self.getNextPath(_srcPath)

                with open(_srcPath, 'r', encoding='utf-8') as ifh, \
                        open(_srcPath_next, 'w', encoding='utf-8') as ofh:
                    for line in ifh:
                        if i == line_num - 1:
                            ofh.write('loop_\n')
                        ofh.write(line)
                        i += 1

                    _srcPath = ofh.name
                    tmpPaths.append(_srcPath)

            except AttributeError:
                pass

        except StopIteration:
            pass

        msg_template = "Only 'save_NAME' is valid in the body of a NMR-STAR file. Found"

        try:

            is_cs_cif = False

            if self.__reg.op == 'nmr-cs-str-consistency-check':

                is_cs_cif = True

                try:

                    with open(_srcPath, 'r', encoding='utf-8') as ifh:
                        for line in ifh:
                            if SAVE_PAT.match(line) or STOP_PAT.match(line):
                                is_cs_cif = False
                                break

                    if is_cs_cif:

                        loop_count = 0
                        has_sf_category = has_sf_framecode = False

                        with open(_srcPath, 'r', encoding='utf-8') as ifh:
                            for line in ifh:
                                if LOOP_PAT.match(line):
                                    loop_count += 1
                                elif SF_CATEGORY_PAT.match(line):
                                    has_sf_category = True
                                elif SF_FRAMECODE_PAT.match(line):
                                    has_sf_framecode = True

                        if not has_sf_category and not has_sf_framecode:

                            in_lp = False

                            _srcPath_next = self.getNextPath(_srcPath)

                            with open(_srcPath, 'r', encoding='utf-8') as ifh, \
                                    open(_srcPath_next, 'w', encoding='utf-8') as ofh:
                                for line in ifh:
                                    if DATABLOCK_PAT.match(line):
                                        g = DATABLOCK_PAT.search(line).groups()
                                        if loop_count < 2:
                                            ofh.write(f"save_{g[0]}\n")
                                    elif CIF_STOP_PAT.match(line):
                                        if in_lp:
                                            if loop_count < 2:
                                                ofh.write('stop_\nsave_\n')
                                            else:
                                                ofh.write('stop_\n')
                                        else:
                                            ofh.write(line)
                                        in_lp = False
                                    elif LOOP_PAT.match(line):
                                        in_lp = True
                                        ofh.write(line)
                                    else:
                                        if in_lp or loop_count < 2:
                                            ofh.write(line)

                                _srcPath = ofh.name
                                tmpPaths.append(_srcPath)

                        else:

                            _srcPath_next = self.getNextPath(_srcPath)
                            if self.__reg.c2S.convert(_srcPath, _srcPath_next):
                                _srcPath = _srcPath_next
                                tmpPaths.append(_srcPath)

                except AttributeError:
                    pass

            if not is_cs_cif:

                msg = next(msg for msg in message['error'] if msg_template in msg)
                warn = "Loops must start with the 'loop_' keyword."

                self.__reg.report.warning.appendDescription('corrected_format_issue',
                                                            {'file_name': file_name, 'description': warn})

                if self.__reg.verbose:
                    self.__reg.log.write(f"+{self.__class_name__}.__validateInputSource() ++ Warning  - {warn}\n")

                msg_pattern = re.compile(r'^.*' + msg_template + r" '(.*)'.*$")

                try:

                    g = msg_pattern.search(msg).groups()

                    tag_name = g[0]

                    tag_name_pattern = re.compile(r'\s*' + tag_name + r'\s*')

                    _srcPath_next = self.getNextPath(_srcPath)

                    with open(_srcPath, 'r', encoding='utf-8') as ifh, \
                            open(_srcPath_next, 'w', encoding='utf-8') as ofh:
                        for line in ifh:
                            if tag_name_pattern.match(line) is None:
                                ofh.write(line)
                            else:
                                ofh.write('loop_\n')

                        _srcPath = ofh.name
                        tmpPaths.append(_srcPath)

                except AttributeError:
                    pass

        except StopIteration:
            pass

        msg_template = "'save_' must be followed by saveframe name. You have a 'save_' tag "\
            "which is illegal without a specified saveframe name."

        try:

            msg = next(msg for msg in message['error'] if msg_template in msg)
            warn = "The saveframe must have a specified saveframe name."

            self.__reg.report.warning.appendDescription('corrected_format_issue',
                                                        {'file_name': file_name, 'description': warn})

            if self.__reg.verbose:
                self.__reg.log.write(f"+{self.__class_name__}.__validateInputSource() ++ Warning  - {warn}\n")

            msg_pattern = re.compile(r'^.*' + msg_template + r".*on line (\d+).*$")

            try:

                g = msg_pattern.search(msg).groups()

                line_num = int(g[0])

                i = 0

                _srcPath_next = self.getNextPath(_srcPath)

                with open(_srcPath, 'r', encoding='utf-8') as ifh, \
                        open(_srcPath_next, 'w', encoding='utf-8') as ofh:
                    for line in ifh:
                        if i != line_num:
                            ofh.write(line)
                        else:
                            ofh.write(f"save_{os.path.basename(srcPath)}\n")
                        i += 1

                    _srcPath = ofh.name
                    tmpPaths.append(_srcPath)

            except AttributeError:
                pass

        except StopIteration:
            pass

        msg_template = "The tag prefix was never set! Either the saveframe had no tags, "\
            "you tried to read a version 2.1 file, or there is something else wrong with your file. "\
            "Saveframe error occurred within:"

        try:

            msg = next(msg for msg in message['error'] if msg_template in msg)
            warn = 'The saveframe must have NMR-STAR V3.2 tags. Saveframe error occurred:'\
                + msg[len(msg_template):].replace('<pynmrstar.', '').replace("'>", "'")

            self.__reg.report.warning.appendDescription('corrected_format_issue',
                                                        {'file_name': file_name, 'description': warn})

            if self.__reg.verbose:
                self.__reg.log.write(f"+{self.__class_name__}.__validateInputSource() ++ Warning  - {warn}\n")

            msg_pattern = re.compile(r'^' + msg_template + r" '(.*)'$")

            targets = []

            for msg in message['error']:

                if msg_template not in msg:
                    continue

                try:

                    target = {}

                    g = msg_pattern.search(msg).groups()
                    sf_framecode = str(g[0])

                    target = {'sf_framecode': sf_framecode}

                    pass_sf_framecode = pass_sf_loop = False

                    sf_named_pattern = re.compile(r'\s*save_' + sf_framecode + r'\s*')

                    with open(_srcPath, 'r', encoding='utf-8') as ifh:
                        for line in ifh:
                            if pass_sf_framecode:
                                if pass_sf_loop:
                                    if CATEGORY_PAT.match(line):
                                        target['lp_category'] = f'_{CATEGORY_PAT.search(line).groups()[0]}'
                                        content_subtype = next((k for k, v in LP_CATEGORIES[file_type].items()
                                                                if v == target['lp_category']), None)
                                        if content_subtype is not None:
                                            target['sf_category'] = SF_CATEGORIES[file_type][content_subtype]
                                            target['sf_tag_prefix'] = SF_TAG_PREFIXES[file_type][content_subtype]
                                        break
                                elif LOOP_PAT.match(line):
                                    pass_sf_loop = True
                            elif sf_named_pattern.match(line):
                                pass_sf_framecode = True

                    targets.append(target)

                except AttributeError:
                    pass

            for target in targets:

                sf_framecode = target['sf_framecode']

                pass_sf_framecode = pass_sf_loop = False

                sf_named_pattern = re.compile(r'\s*save_' + sf_framecode + r'\s*')

                _srcPath_next = self.getNextPath(_srcPath)

                with open(_srcPath, 'r', encoding='utf-8') as ifh, \
                        open(_srcPath_next, 'w', encoding='utf-8') as ofh:
                    for line in ifh:
                        if pass_sf_loop:
                            ofh.write(line)
                        elif pass_sf_framecode:
                            if LOOP_PAT.match(line):
                                pass_sf_loop = True
                                if 'sf_category' in target:
                                    ofh.write(f"{target['sf_tag_prefix']}."
                                              f"{'sf_framecode' if file_type == 'nef' else 'Sf_framecode'}   "
                                              f"{sf_framecode}\n")
                                    ofh.write(f"{target['sf_tag_prefix']}."
                                              f"{'sf_category' if file_type == 'nef' else 'Sf_category'}    "
                                              f"{target['sf_category']}\n")
                                    ofh.write('#\n')
                                ofh.write(line)
                        elif sf_named_pattern.match(line):
                            pass_sf_framecode = True
                            ofh.write(line)
                        elif not pass_sf_framecode:
                            ofh.write(line)

                    _srcPath = ofh.name
                    tmpPaths.append(_srcPath)

        except StopIteration:
            pass

        if len(tmpPaths) > len_tmp_paths:

            is_valid, _message = self.__reg.nefT.validate_file(_srcPath, fileSubType, allowEmpty)

            if not is_valid:

                retry = len(message['error']) != len(_message['error']) or message['error'] != _message['error']

                if not retry:

                    for msg, _msg in zip(message['error'], _message['error']):
                        if msg != _msg:
                            retry = True
                            break

                if retry and len_tmp_paths < 40:
                    return self.fixFormatIssueOfInputSource(file_list_id, file_name, file_type, _srcPath, fileSubType,
                                                            _message, tmpPaths, allowEmpty, hasLegacySfIssue)

        is_done = True

        is_valid, message = self.__reg.nefT.validate_file(_srcPath, fileSubType, allowEmpty)

        _file_type = message['file_type']  # nef/nmr-star/unknown

        if not self.__reg.combined_mode:

            if file_list_id < self.__reg.cs_file_path_list_len:

                if CS_FILE_PATH_LIST_KEY in self.__reg.outputParamDict:
                    if file_list_id < len(self.__reg.outputParamDict[CS_FILE_PATH_LIST_KEY]):
                        dstPath = self.__reg.outputParamDict[CS_FILE_PATH_LIST_KEY][file_list_id]
                        if dstPath is not None and dstPath not in self.__reg.inputParamDict[CS_FILE_PATH_LIST_KEY]:
                            shutil.copyfile(_srcPath, dstPath)

            else:

                if MR_FILE_PATH_LIST_KEY in self.__reg.outputParamDict:
                    if file_list_id - self.__reg.cs_file_path_list_len < len(self.__reg.outputParamDict[MR_FILE_PATH_LIST_KEY]):
                        dstPath = self.__reg.outputParamDict[MR_FILE_PATH_LIST_KEY][file_list_id - self.__reg.cs_file_path_list_len]
                        if dstPath is not None and dstPath not in self.__reg.inputParamDict[MR_FILE_PATH_LIST_KEY]:
                            shutil.copyfile(_srcPath, dstPath)

        if is_valid:

            if _file_type != file_type:

                err = f"{file_name!r} was selected as {READABLE_FILE_TYPE[file_type]} file, "\
                    f"but recognized as {READABLE_FILE_TYPE[_file_type]} file. Please re-upload the file."

                if len(message['error']) > 0:
                    for err_message in message['error']:
                        if 'No such file or directory' not in err_message:
                            err += ' ' + re.sub('not in list', 'unknown item.', err_message)

                self.__reg.report.error.appendDescription('content_mismatch',
                                                          {'file_name': file_name, 'description': err})

                if self.__reg.verbose:
                    self.__reg.log.write(f"+{self.__class_name__}.fixFormatIssueOfInputSource() ++ Error  - {err}\n")

            else:

                is_done, star_data_type, star_data = self.__reg.nefT.read_input_file(_srcPath)

                rescued = hasLegacySfIssue and is_done and star_data_type == 'Entry'

                if len(self.__reg.star_data_type) > file_list_id:
                    self.__reg.star_data_type[file_list_id] = star_data_type
                    self.__reg.star_data[file_list_id] = star_data
                else:
                    self.__reg.star_data_type.append(star_data_type)
                    self.__reg.star_data.append(star_data)

                self.rescueFormerNef(file_list_id)
                self.rescueImmatureStr(file_list_id)

                if rescued:
                    if ONEDEP_ANY_UPLOAD_FILE_NAME_PAT.match(srcPath):
                        g = ONEDEP_ANY_UPLOAD_FILE_NAME_PAT.search(srcPath).groups()
                        srcPath = f'{g[0]}-upload-convert_{g[1]}.V{g[2]}'
                    else:
                        if ONEDEP_ANY_FILE_NAME_PAT.match(srcPath):
                            g = ONEDEP_ANY_FILE_NAME_PAT.search(srcPath).groups()
                            srcPath = f'{g[0]}.V{int(g[1]) + 1}'

                    self.__reg.star_data[file_list_id].write_to_file(srcPath,
                                                                     show_comments=False,
                                                                     skip_empty_loops=True,
                                                                     skip_empty_tags=False)

        else:

            missing_loop = True

            err = f"{file_name!r} is not compliant with the {READABLE_FILE_TYPE[file_type]} dictionary."

            if len(message['error']) > 0:

                if any(True for err_message in message['error'] if 'The mandatory loop' in err_message):

                    err = ''
                    for err_message in message['error']:
                        if 'No such file or directory' not in err_message:
                            err += re.sub('not in list', 'unknown item.', err_message) + ' '
                    err = err[:-1]

                else:
                    missing_loop = False

                    for err_message in self.__reg.original_error_message[file_list_id]['error']:
                        if 'No such file or directory' not in err_message:
                            err += ' ' + re.sub('not in list', 'unknown item.', err_message)

            if not self.__reg.remediation_mode or not missing_loop or file_list_id > 0:

                if self.__reg.op != 'nmr-str-replace-cs' or not self.__reg.bmrb_only:

                    self.__reg.report.error.appendDescription('missing_mandatory_content' if missing_loop else 'format_issue',
                                                              {'file_name': file_name, 'description': err})

                    self.__reg.log.write(f"+{self.__class_name__}.fixFormatIssueOfInputSource() ++ Error  - "
                                         f"{file_name} {err}\n")

                is_done = False

            else:

                self.__reg.has_star_chem_shift = False

                if self.__reg.op != 'nmr-str-replace-cs' or not self.__reg.bmrb_only:

                    self.__reg.suspended_errors_for_lazy_eval.append({'missing_mandatory_content':
                                                                      {'file_name': file_name, 'description': err}})

                    if self.__reg.verbose:
                        self.__reg.log.write(f"+{self.__class_name__}.fixFormatIssueOfInputSource() ++ Error  - {err}\n")

        try:

            if self.__reg.release_mode and len(tmpPaths) > 0:
                self.__reg.srcPath = tmpPaths[-1]
                for tmpPath in tmpPaths[:-1]:
                    if os.path.exists(tmpPath):
                        os.remove(tmpPath)
            else:
                for tmpPath in tmpPaths:
                    if os.path.exists(tmpPath):
                        os.remove(tmpPath)

        except OSError:
            pass

        self.__reg.nefT.release()

        return is_done

    def rescueFormerNef(self, file_list_id: int) -> bool:
        """ Rescue former NEF version prior to 1.0.
        """

        input_source = self.__reg.report.input_sources[file_list_id]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        if file_type != 'nef' or file_list_id >= len(self.__reg.star_data) or self.__reg.star_data[file_list_id] is None:
            return True

        if self.__reg.combined_mode or self.__reg.star_data_type[file_list_id] == 'Entry':

            for content_subtype in NMR_CONTENT_SUBTYPES:

                sf_category = SF_CATEGORIES[file_type][content_subtype]

                if sf_category is None:
                    continue

                for sf in self.__reg.star_data[file_list_id].get_saveframes_by_category(sf_category):
                    sf_framecode = get_first_sf_tag(sf, 'sf_framecode')

                    if self.getSaveframeByName(file_list_id, sf_framecode) is None:

                        itName = f'_{sf_category}.sf_framecode'

                        if self.__reg.resolve_conflict:
                            warn = f"{itName} {sf_framecode!r} should be matched "\
                                f"with saveframe name {sf.name!r}. {itName} will be overwritten."

                            self.__reg.report.warning.appendDescription('missing_saveframe',
                                                                        {'file_name': file_name, 'sf_framecode': sf.name,
                                                                         'description': warn})

                            if self.__reg.verbose:
                                self.__reg.log.write(f"+{self.__class_name__}.rescueFormerNef() ++ Warning  - {warn}\n")

                            set_sf_tag(sf, 'sf_framecode', sf.name)

                        else:
                            err = f"{itName} {sf_framecode!r} must be matched with saveframe name {sf.name!r}."

                            self.__reg.report.error.appendDescription('format_issue',
                                                                      {'file_name': file_name, 'sf_framecode': sf.name,
                                                                       'description': err})

                            self.__reg.log.write(f"+{self.__class_name__}.rescueFormerNef() ++ Error  - "
                                                 f"{file_name} {sf.name} {err}\n")

        if not self.__reg.rescue_mode:
            return True

        if self.__reg.combined_mode or self.__reg.star_data_type[file_list_id] == 'Entry':

            content_subtype = 'entry_info'

            sf_category = SF_CATEGORIES[file_type][content_subtype]

            for sf in self.__reg.star_data[file_list_id].get_saveframes_by_category(sf_category):
                format_version = get_first_sf_tag(sf, 'format_version')

                if not format_version.startswith('0.'):
                    sf.format_version = NEF_VERSION

            for content_subtype in NMR_CONTENT_SUBTYPES:

                sf_category = SF_CATEGORIES[file_type][content_subtype]
                lp_category = LP_CATEGORIES[file_type][content_subtype]

                if None in (sf_category, lp_category):
                    continue

                for sf in self.__reg.star_data[file_list_id].get_saveframes_by_category(sf_category):
                    sf_framecode = get_first_sf_tag(sf, 'sf_framecode')

                    if not any(True for loop in sf.loops if loop.category == lp_category):
                        continue

                    self.__rescueFormerNef__(file_name, file_type, content_subtype, sf, sf_framecode, sf_category, lp_category)

            return True

        self.__reg.sf_category_list, self.__reg.lp_category_list =\
            self.__reg.nefT.get_inventory_list(self.__reg.star_data[file_list_id])

        # initialize loop counter
        lp_counts = {t: 0 for t in NMR_CONTENT_SUBTYPES}

        # increment loop counter of each content subtype
        for lp_category in self.__reg.lp_category_list:
            if lp_category in LP_CATEGORIES[file_type].values():
                lp_counts[[k for k, v in LP_CATEGORIES[file_type].items() if v == lp_category][0]] += 1

        content_subtypes = {k: lp_counts[k] for k in lp_counts if lp_counts[k] > 0}

        for content_subtype in NMR_CONTENT_SUBTYPES:

            sf_category = SF_CATEGORIES[file_type][content_subtype]
            lp_category = LP_CATEGORIES[file_type][content_subtype]

            if None in (sf_category, lp_category):
                continue

            if self.__reg.star_data_type[file_list_id] == 'Loop':

                if content_subtype not in content_subtypes:
                    continue

                sf = self.__reg.star_data[file_list_id]
                sf_framecode = ''

                self.__rescueFormerNef__(file_name, file_type, content_subtype, sf, sf_framecode, sf_category, lp_category)

            else:

                if content_subtype not in content_subtypes:
                    continue

                sf = self.__reg.star_data[file_list_id]
                sf_framecode = get_first_sf_tag(sf, 'sf_framecode')

                self.__rescueFormerNef__(file_name, file_type, content_subtype, sf, sf_framecode, sf_category, lp_category)

        return True

    def __rescueFormerNef__(self, file_name: str, file_type: str, content_subtype: str,
                            sf: Union[pynmrstar.Entry, pynmrstar.Saveframe, pynmrstar.Loop],
                            sf_framecode: str, sf_category: str, lp_category: str) -> None:
        """ Rescue former NEF version prior to 1.0.
        """

        if isinstance(sf, pynmrstar.Loop):
            loop = sf
        else:
            loop = sf.get_loop(lp_category)

        try:

            index_tag = INDEX_TAGS[file_type][content_subtype]

            if index_tag is not None:

                try:
                    tag_pos = next(loop.tags.index(tag) for tag in loop.tags if tag == 'ordinal')
                    loop.tags[tag_pos] = 'index'
                except StopIteration:
                    pass

                try:
                    tag_pos = next(loop.tags.index(tag) for tag in loop.tags if tag == 'index_id')
                    loop.tags[tag_pos] = 'index'
                except StopIteration:
                    pass

            if content_subtype == 'poly_seq':

                try:
                    tag_pos = next(loop.tags.index(tag) for tag in loop.tags if tag == 'residue_type')
                    loop.tags[tag_pos] = 'residue_name'
                except StopIteration:
                    pass

                if 'index' not in loop.tags:

                    lp_tag = f'{lp_category}.index'
                    err = ERR_TEMPLATE_FOR_MISSING_MANDATORY_LP_TAG % (lp_tag, file_type.upper())

                    if self.__reg.check_mandatory_tag and self.__reg.nefT.is_mandatory_tag(lp_tag, file_type):
                        self.__reg.report.error.appendDescription('missing_mandatory_item',
                                                                  {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                   'category': lp_category, 'description': err})

                        if self.__reg.verbose:
                            self.__reg.log.write(f"+{self.__class_name__}.rescueFormerNef() ++ LookupError  - "
                                                 f"{file_name} {sf_framecode} {lp_category} {err}\n")

                    try:

                        for idx, row in enumerate(loop, start=1):
                            row.append(idx)

                        loop.add_tag(f'{lp_category}.index')

                    except ValueError:
                        pass

            elif content_subtype == 'chem_shift':

                if any(True for tag in sf.tags if tag[0] == 'atom_chemical_shift_units'):
                    sf.remove_tag('atom_chemical_shift_units')

                try:
                    tag_pos = next(loop.tags.index(tag) for tag in loop.tags if tag == 'residue_type')
                    loop.tags[tag_pos] = 'residue_name'
                except StopIteration:
                    pass

                if 'element' not in loop.tags:

                    lp_tag = f'{lp_category}.element'
                    err = ERR_TEMPLATE_FOR_MISSING_MANDATORY_LP_TAG % (lp_tag, file_type.upper())

                    if self.__reg.check_mandatory_tag and self.__reg.nefT.is_mandatory_tag(lp_tag, file_type):
                        self.__reg.report.error.appendDescription('missing_mandatory_item',
                                                                  {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                   'category': lp_category, 'description': err})

                        if self.__reg.verbose:
                            self.__reg.log.write(f"+{self.__class_name__}.rescueFormerNef() ++ LookupError  - "
                                                 f"{file_name} {sf_framecode} {lp_category} {err}\n")

                    try:

                        atom_name_col = loop.tags.index('atom_name')

                        for row in loop:
                            atom_type = row[atom_name_col][0]
                            if atom_type in ('Q', 'M'):
                                atom_type = 'H'
                            row.append(atom_type)

                        loop.add_tag(f'{lp_category}.element')

                    except ValueError:
                        pass

                elif not self.__reg.combined_mode:

                    atom_type_col = loop.tags.index('element')
                    atom_name_col = loop.tags.index('atom_name')

                    for row in loop:
                        if row[atom_type_col] in EMPTY_VALUE:
                            atom_type = row[atom_name_col][0]
                            if atom_type in ('Q', 'M'):
                                atom_type = 'H'
                            row[atom_type_col] = atom_type

                if 'isotope_number' not in loop.tags:

                    lp_tag = f'{lp_category}.isotope_number'
                    err = ERR_TEMPLATE_FOR_MISSING_MANDATORY_LP_TAG % (lp_tag, file_type.upper())

                    if self.__reg.check_mandatory_tag and self.__reg.nefT.is_mandatory_tag(lp_tag, file_type):
                        self.__reg.report.error.appendDescription('missing_mandatory_item',
                                                                  {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                   'category': lp_category, 'description': err})

                        if self.__reg.verbose:
                            self.__reg.log.write(f"+{self.__class_name__}.rescueFormerNef() ++ LookupError  - "
                                                 f"{file_name} {sf_framecode} {lp_category} {err}\n")

                    try:

                        atom_name_col = loop.tags.index('atom_name')

                        for row in loop:
                            atom_type = row[atom_name_col][0]
                            if atom_type in ('Q', 'M'):
                                atom_type = 'H'
                            row.append(str(ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS[atom_type][0]))

                        loop.add_tag(f'{lp_category}.isotope_number')

                    except ValueError:
                        pass

                elif not self.__reg.combined_mode:

                    iso_num_col = loop.tags.index('isotope_number')
                    atom_name_col = loop.tags.index('atom_name')

                    for row in loop:
                        if row[iso_num_col] in EMPTY_VALUE:
                            atom_type = row[atom_name_col][0]
                            if atom_type in ('Q', 'M'):
                                atom_type = 'H'
                            row[iso_num_col] = str(ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS[atom_type][0])

            elif content_subtype == 'dihed_restraint':

                if 'name' not in loop.tags:

                    lp_tag = f'{lp_category}.name'
                    err = ERR_TEMPLATE_FOR_MISSING_MANDATORY_LP_TAG % (lp_tag, file_type.upper())

                    if self.__reg.check_mandatory_tag and self.__reg.nefT.is_mandatory_tag(lp_tag, file_type):
                        self.__reg.report.error.appendDescription('missing_mandatory_item',
                                                                  {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                   'category': lp_category, 'description': err})

                        if self.__reg.verbose:
                            self.__reg.log.write(f"+{self.__class_name__}.rescueFormerNef() ++ LookupError  - "
                                                 f"{file_name} {sf_framecode} {lp_category} {err}\n")

                    try:

                        loop.add_tag(f'{lp_category}.name', update_data=True)

                    except ValueError:
                        pass

            elif content_subtype == 'rdc_restraint':

                try:

                    tag = next(tag for tag in sf.tags if tag[0] == 'tensor_residue_type')
                    sf.add_tag(f'{sf_category}.tensor_residue_name', tag[1])
                    sf.remove_tag('tensor_residue_type')

                except StopIteration:
                    pass
                except ValueError:
                    pass

            if content_subtype in ('dist_restraint', 'rdc_restraint'):
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

            else:
                return

            for j in range(1, max_dim):

                _residue_type = f'residue_type_{j}'

                try:
                    tag_pos = next(loop.tags.index(tag) for tag in loop.tags if tag == _residue_type)
                    loop.tags[tag_pos] = f'residue_name_{j}'
                except StopIteration:
                    pass

        except KeyError:
            pass

    def rescueImmatureStr(self, file_list_id: int) -> bool:
        """ Rescue immature NMR-STAR.
        """

        input_source = self.__reg.report.input_sources[file_list_id]
        input_source_dic = input_source.get()

        file_name = input_source_dic['file_name']
        file_type = input_source_dic['file_type']

        if file_type != 'nmr-star' or file_list_id >= len(self.__reg.star_data) or self.__reg.star_data[file_list_id] is None:
            return True

        if self.__reg.combined_mode and self.__reg.star_data_type[file_list_id] == 'Entry':

            for content_subtype in NMR_CONTENT_SUBTYPES:

                if content_subtype == 'entry_info':
                    continue

                sf_category = SF_CATEGORIES[file_type][content_subtype]

                if sf_category is None:
                    continue

                for sf in self.__reg.star_data[file_list_id].get_saveframes_by_category(sf_category):
                    sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')

                    if self.getSaveframeByName(file_list_id, sf_framecode) is None:

                        itName = f'_{sf_category}.Sf_framecode'

                        if self.__reg.resolve_conflict:
                            warn = f"{itName} {sf_framecode!r} should be matched "\
                                f"with saveframe name {sf.name!r}. {itName} will be overwritten."

                            self.__reg.report.warning.appendDescription('missing_saveframe',
                                                                        {'file_name': file_name, 'sf_framecode': sf.name,
                                                                         'description': warn})

                            if self.__reg.verbose:
                                self.__reg.log.write(f"+{self.__class_name__}.rescueImmatureStr() ++ Warning  - {warn}\n")

                            tagNames = [t[0] for t in sf.tags]

                            if 'Sf_framecode' in tagNames:
                                set_sf_tag(sf, 'Sf_framecode', sf.name)
                            elif 'sf_framecode' in tagNames:
                                set_sf_tag(sf, 'sf_framecode', sf.name)

                        else:
                            err = f"{itName} {sf_framecode!r} must be matched with saveframe name {sf.name!r}."

                            self.__reg.report.error.appendDescription('format_issue',
                                                                      {'file_name': file_name, 'sf_framecode': sf.name,
                                                                       'description': err})

                            self.__reg.log.write(f"+{self.__class_name__}.rescueImmatureStr() ++ Error  - "
                                                 f"{file_name} {sf.name} {err}\n")

        if not self.__reg.rescue_mode:
            return True

        self.__reg.sf_category_list, self.__reg.lp_category_list =\
            self.__reg.nefT.get_inventory_list(self.__reg.star_data[file_list_id])

        # initialize loop counter
        lp_counts = {t: 0 for t in NMR_CONTENT_SUBTYPES}

        # increment loop counter of each content subtype
        for lp_category in self.__reg.lp_category_list:
            if lp_category in LP_CATEGORIES[file_type].values():
                lp_counts[[k for k, v in LP_CATEGORIES[file_type].items() if v == lp_category][0]] += 1

        content_subtypes = {k: lp_counts[k] for k in lp_counts if lp_counts[k] > 0}

        for content_subtype in NMR_CONTENT_SUBTYPES:

            sf_category = SF_CATEGORIES[file_type][content_subtype]
            lp_category = LP_CATEGORIES[file_type][content_subtype]

            if content_subtype.startswith('spectral_peak'):
                lp_category = AUX_LP_CATEGORIES[file_type][content_subtype][0]  # _Spectral_dim

            if None in (sf_category, lp_category):
                continue

            if self.__reg.star_data_type[file_list_id] == 'Loop':

                if content_subtype not in content_subtypes:
                    continue

                sf = self.__reg.star_data[file_list_id]
                sf_framecode = ''

                self.__rescueImmatureStr__(file_name, file_type, content_subtype, sf, sf_framecode, lp_category)

            elif self.__reg.star_data_type[file_list_id] == 'Saveframe':

                if content_subtype not in content_subtypes:
                    continue

                sf = self.__reg.star_data[file_list_id]
                sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')

                self.__rescueImmatureStr__(file_name, file_type, content_subtype, sf, sf_framecode, lp_category)

            else:

                for sf in self.__reg.star_data[file_list_id].get_saveframes_by_category(sf_category):
                    sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')

                    if not any(True for loop in sf.loops if loop.category == lp_category):
                        continue

                    self.__rescueImmatureStr__(file_name, file_type, content_subtype, sf, sf_framecode, lp_category)

        return True

    def __rescueImmatureStr__(self, file_name: str, file_type: str, content_subtype: str,
                              sf: Union[pynmrstar.Entry, pynmrstar.Saveframe, pynmrstar.Loop],
                              sf_framecode: str, lp_category: str) -> None:
        """ Rescue immature NMR-STAR.
        """

        if isinstance(sf, pynmrstar.Loop):
            loop = sf
        else:
            loop = sf.get_loop(lp_category)

        try:

            if content_subtype == 'chem_shift':

                if 'Atom_type' not in loop.tags:

                    lp_tag = f'{lp_category}.Atom_type'
                    err = ERR_TEMPLATE_FOR_MISSING_MANDATORY_LP_TAG % (lp_tag, file_type.upper())

                    if self.__reg.check_mandatory_tag and self.__reg.nefT.is_mandatory_tag(lp_tag, file_type):
                        self.__reg.report.error.appendDescription('missing_mandatory_item',
                                                                  {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                   'category': lp_category, 'description': err})

                        if self.__reg.verbose:
                            self.__reg.log.write(f"+{self.__class_name__}.rescueImmatureStr() ++ LookupError  - "
                                                 f"{file_name} {sf_framecode} {lp_category} {err}\n")

                    try:

                        atom_name_col = loop.tags.index('Atom_ID')

                        for row in loop:
                            atom_type = row[atom_name_col][0]
                            if atom_type in ('Q', 'M'):
                                atom_type = 'H'
                            row.append(atom_type)

                        loop.add_tag(f'{lp_category}.Atom_type')

                    except ValueError:
                        pass

                elif not self.__reg.combined_mode:

                    try:

                        atom_type_col = loop.tags.index('Atom_type')
                        atom_name_col = loop.tags.index('Atom_ID')

                        for row in loop:
                            if row[atom_type_col] in EMPTY_VALUE:
                                atom_type = row[atom_name_col][0]
                                if atom_type in ('Q', 'M'):
                                    atom_type = 'H'
                                row[atom_type_col] = atom_type

                    except ValueError:
                        pass

                if 'Atom_isotope_number' not in loop.tags:

                    lp_tag = f'{lp_category}.Atom_isotope_number'
                    err = ERR_TEMPLATE_FOR_MISSING_MANDATORY_LP_TAG % (lp_tag, file_type.upper())

                    if self.__reg.check_mandatory_tag and self.__reg.nefT.is_mandatory_tag(lp_tag, file_type):
                        self.__reg.report.error.appendDescription('missing_mandatory_item',
                                                                  {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                   'category': lp_category, 'description': err})

                        if self.__reg.verbose:
                            self.__reg.log.write(f"+{self.__class_name__}.rescueImmatureStr() ++ LookupError  - "
                                                 f"{file_name} {sf_framecode} {lp_category} {err}\n")

                    try:

                        atom_name_col = loop.tags.index('Atom_ID')

                        for row in loop:
                            atom_type = row[atom_name_col][0]
                            if atom_type in ('Q', 'M'):
                                atom_type = 'H'
                            row.append(str(ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS[atom_type][0]))

                        loop.add_tag(f'{lp_category}.Atom_isotope_number')

                    except ValueError:
                        pass

                elif not self.__reg.combined_mode:

                    iso_num_col = loop.tags.index('Atom_isotope_number')
                    atom_name_col = loop.tags.index('Atom_ID')

                    for row in loop:
                        if row[iso_num_col] in EMPTY_VALUE:
                            atom_type = row[atom_name_col][0]
                            if atom_type in ('Q', 'M'):
                                atom_type = 'H'
                            row[iso_num_col] = str(ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS[atom_type][0])

            elif content_subtype == 'dist_restraint':  # backward compatibility

                original_items = ['Original_PDB_strand_ID', 'Original_PDB_residue_no', 'Original_PDB_residue_name']

                for i in range(1, 3):
                    for original_item in original_items:
                        tag = f'{original_item}_{i}'
                        if tag in loop.tags:
                            loop.remove_tag(tag)

                    tag = f'Original_PDB_atom_name_{i}'
                    if tag in loop.tags:

                        _tag = f'Auth_atom_name_{i}'
                        if _tag not in loop.tags:
                            _dat = loop.get_tag([tag])

                            for idx, row in enumerate(loop):
                                row.append(_dat[idx])

                            loop.add_tag(_tag)

                        loop.remove_tag(tag)

            elif content_subtype == 'dihed_restraint':

                if 'Torsion_angle_name' not in loop.tags:

                    lp_tag = f'{lp_category}.Torsion_angle_name'
                    err = ERR_TEMPLATE_FOR_MISSING_MANDATORY_LP_TAG % (lp_tag, file_type.upper())

                    if self.__reg.check_mandatory_tag and self.__reg.nefT.is_mandatory_tag(lp_tag, file_type):
                        self.__reg.report.error.appendDescription('missing_mandatory_item',
                                                                  {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                   'category': lp_category, 'description': err})

                        if self.__reg.verbose:
                            self.__reg.log.write(f"+{self.__class_name__}.rescueImmatureStr() ++ LookupError  - "
                                                 f"{file_name} {sf_framecode} {lp_category} {err}\n")

                    try:

                        loop.add_tag(f'{lp_category}.Torsion_angle_name', update_data=True)

                    except ValueError:
                        pass

            elif content_subtype.startswith('spectral_peak'):

                if 'Atom_type' not in loop.tags:

                    lp_tag = f'{lp_category}.Atom_type'
                    err = ERR_TEMPLATE_FOR_MISSING_MANDATORY_LP_TAG % (lp_tag, file_type.upper())

                    if self.__reg.check_mandatory_tag and self.__reg.nefT.is_mandatory_tag(lp_tag, file_type):
                        self.__reg.report.error.appendDescription('missing_mandatory_item',
                                                                  {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                   'category': lp_category, 'description': err})

                        if self.__reg.verbose:
                            self.__reg.log.write(f"+{self.__class_name__}.rescueImmatureStr() ++ LookupError  - "
                                                 f"{file_name} {sf_framecode} {lp_category} {err}\n")

                    try:

                        axis_code_name_col = loop.tags.index('Axis_code')

                        for row in loop:
                            atom_type = re.sub(r'\d+', '', row[axis_code_name_col])
                            row.append(atom_type)

                        loop.add_tag(f'{lp_category}.Atom_type')

                    except ValueError:
                        pass

                if 'Atom_isotope_number' not in loop.tags:

                    lp_tag = f'{lp_category}.Atom_isotope_number'
                    err = ERR_TEMPLATE_FOR_MISSING_MANDATORY_LP_TAG % (lp_tag, file_type.upper())

                    if self.__reg.check_mandatory_tag and self.__reg.nefT.is_mandatory_tag(lp_tag, file_type):
                        self.__reg.report.error.appendDescription('missing_mandatory_item',
                                                                  {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                   'category': lp_category, 'description': err})

                        if self.__reg.verbose:
                            self.__reg.log.write(f"+{self.__class_name__}.rescueImmatureStr() ++ LookupError  - "
                                                 f"{file_name} {sf_framecode} {lp_category} {err}\n")

                    try:

                        axis_code_name_col = loop.tags.index('Axis_code')

                        for row in loop:
                            atom_type = re.sub(r'\d+', '', row[axis_code_name_col])
                            row.append(str(ISOTOPE_NUMBERS_OF_NMR_OBS_NUCS[atom_type][0]))

                        loop.add_tag(f'{lp_category}.Atom_isotope_number')

                    except ValueError:
                        pass

                if 'Axis_code' not in loop.tags:

                    lp_tag = f'{lp_category}.Axis_code'
                    err = ERR_TEMPLATE_FOR_MISSING_MANDATORY_LP_TAG % (lp_tag, file_type.upper())

                    if self.__reg.check_mandatory_tag and self.__reg.nefT.is_mandatory_tag(lp_tag, file_type):
                        self.__reg.report.error.appendDescription('missing_mandatory_item',
                                                                  {'file_name': file_name, 'sf_framecode': sf_framecode,
                                                                   'category': lp_category, 'description': err})

                        if self.__reg.verbose:
                            self.__reg.log.write(f"+{self.__class_name__}.rescueImmatureStr() ++ LookupError  - "
                                                 f"{file_name} {sf_framecode} {lp_category} {err}\n")

                    try:

                        atom_type_name_col = loop.tags.index('Atom_type')
                        iso_num_name_col = loop.tags.index('Atom_isotope_number')

                        for row in loop:
                            atom_type = row[atom_type_name_col]
                            iso_num = row[iso_num_name_col]
                            row.append(iso_num + atom_type)

                        loop.add_tag(f'{lp_category}.Axis_code')

                    except ValueError:
                        pass

                # _Spectral_dim.Encoded_source_dimension_ID should be _Spectral_dim.Encoded_reduced_dimension_ID
                if 'Encoded_source_dimension_ID' in loop.tags:
                    if 'Encoded_reduced_dimension_ID' in loop.tags:
                        loop.remove_tag('Encoded_source_dimension_ID')
                    else:
                        col = loop.tags.index('Encoded_source_dimension_ID')
                        loop.tags[col] = 'Encoded_reduced_dimension_ID'

        except KeyError:
            pass

    def getSaveframeByName(self, file_list_id: int, sf_framecode: str
                           ) -> Optional[pynmrstar.Saveframe]:
        """ Retrieve saveframe content from a given name.
        """

        try:

            return self.__reg.star_data[file_list_id].get_saveframe_by_name(sf_framecode)

        except KeyError:  # DAOTHER-7389, issue #4

            if file_list_id < len(self.__reg.sf_name_corrections) and sf_framecode in self.__reg.sf_name_corrections[file_list_id]:

                try:
                    return self.__reg.star_data[file_list_id].get_saveframe_by_name(
                        self.__reg.sf_name_corrections[file_list_id][sf_framecode])
                except KeyError:
                    return None

            else:

                # pattern for guessing original saveframe name DAOTHER-7389, issue #4
                chk_unresolved_sf_name_pattern = re.compile(r'^(.*)_\d+$')

                try:
                    g = chk_unresolved_sf_name_pattern.search(sf_framecode).groups()
                    return self.__reg.star_data[file_list_id].get_saveframe_by_name(g[0])
                except AttributeError:
                    return None
                except KeyError:
                    return None
