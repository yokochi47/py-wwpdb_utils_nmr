# File: NmrDpMrSplitter.py
# Date: 07-Jan-2026
#
# Updates:
# 18-Sep-2026  M. Yokochi - decompose detectContentSubTypeOfLegacyMr() into per-phase methods,
#                           extract the auxiliary topology detectors, and speed up the text scans
# 18-Sep-2026  M. Yokochi - fix CHARMM topology detection, whose '{Number of atoms} EXT' header test
#                           compared a single character and so never matched, and name CHARMM rather
#                           than GROMACS in its content_mismatch message
# 03-Oct-2026  M. Yokochi - test restraints before chemical shifts in __classifyLightMrCounts() (DAOTHER-7829)
##
""" File splitter for public PDB-MR formatted restraint file.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.0"

import codecs
import itertools
import os
import re
import shutil
from operator import itemgetter
from typing import Any, List, Optional, Set, Tuple

import chardet

from striprtf.striprtf import rtf_to_text

try:
    from wwpdb.utils.nmr.NmrDpConstant import (MR_FILE_PATH_LIST_KEY,
                                               AR_FILE_PATH_LIST_KEY,
                                               MR_MAX_SPACER_LINES,
                                               READABLE_FILE_TYPE,
                                               STD_MON_DICT,
                                               PROTON_BEGIN_CODE,
                                               MAX_DIM_NUM_OF_SPECTRA,
                                               HALF_SPIN_NUCLEUS,
                                               PDB_MR_FILE_HEADER_PAT,
                                               DATABLOCK_PAT,
                                               SF_ANONYMOUS_PAT,
                                               SAVE_PAT,
                                               LOOP_PAT,
                                               STOP_PAT,
                                               COMMENT_PAT,
                                               WS_PAT,
                                               MISMATCHED_INPUT_ERR_MSG,
                                               EXTRANEOUS_INPUT_ERR_MSG,
                                               NO_VIABLE_ALT_ERR_MSG,
                                               EXPECTING_L_PAREN,
                                               LINEAR_MR_FILE_TYPES,
                                               RETRIAL_MR_FILE_TYPES,
                                               PARSABLE_MR_FILE_TYPES,
                                               ARCHIVAL_MR_FILE_TYPES,
                                               PARSABLE_PK_FILE_TYPES,
                                               CS_ERROR_MIN,
                                               CS_ERROR_MAX,
                                               CS_RANGE_MIN,
                                               CS_RANGE_MAX,
                                               DIST_RANGE_MIN,
                                               DIST_RANGE_MAX,
                                               ANGLE_RANGE_MIN,
                                               ANGLE_RANGE_MAX,
                                               RDC_RANGE_MIN,
                                               RDC_RANGE_MAX,
                                               WEIGHT_RANGE_MIN,
                                               WEIGHT_RANGE_MAX,
                                               KNOWN_ANGLE_NAMES,
                                               CYANA_MR_FILE_EXTS,
                                               text_md5)
    from wwpdb.utils.nmr.NmrDpRegistry import (NmrDpRegistry,
                                               get_next_path,
                                               test_path_with_suffix)
    from wwpdb.utils.nmr.AlignUtil import (getRestraintFormatName,
                                           getRestraintFormatNames)
    from wwpdb.utils.nmr.NmrVrptUtility import (uncompress_gzip_file,
                                                get_temp_path)
    from wwpdb.utils.nmr.mr.ParserListenerUtil import (translateToStdResName,
                                                       startsWithPdbRecord,
                                                       getRestraintName)
    from wwpdb.utils.nmr.mr.AmberMRReader import AmberMRReader
    from wwpdb.utils.nmr.mr.AmberPTReader import AmberPTReader
    from wwpdb.utils.nmr.mr.AriaMRReader import AriaMRReader
    from wwpdb.utils.nmr.mr.AriaMRXReader import AriaMRXReader
    from wwpdb.utils.nmr.mr.BareMRReader import BareMRReader
    from wwpdb.utils.nmr.mr.BarePDBReader import BarePDBReader
    from wwpdb.utils.nmr.mr.BiosymMRReader import BiosymMRReader
    from wwpdb.utils.nmr.mr.CharmmCRDReader import CharmmCRDReader
    from wwpdb.utils.nmr.mr.CharmmMRReader import CharmmMRReader
    from wwpdb.utils.nmr.mr.CnsMRReader import CnsMRReader
    from wwpdb.utils.nmr.mr.CyanaMRReader import CyanaMRReader
    from wwpdb.utils.nmr.mr.CyanaNOAReader import CyanaNOAReader
    from wwpdb.utils.nmr.mr.DynamoMRReader import DynamoMRReader
    from wwpdb.utils.nmr.mr.GromacsMRReader import GromacsMRReader
    from wwpdb.utils.nmr.mr.GromacsPTReader import GromacsPTReader
    from wwpdb.utils.nmr.mr.IsdMRReader import IsdMRReader
    from wwpdb.utils.nmr.mr.RosettaMRReader import RosettaMRReader
    from wwpdb.utils.nmr.mr.SchrodingerMRReader import SchrodingerMRReader
    from wwpdb.utils.nmr.mr.SybylMRReader import SybylMRReader
    from wwpdb.utils.nmr.mr.XplorMRReader import XplorMRReader
    from wwpdb.utils.nmr.pk.AriaPKReader import AriaPKReader
    from wwpdb.utils.nmr.pk.BarePKReader import BarePKReader
    from wwpdb.utils.nmr.pk.CcpnPKReader import CcpnPKReader
    from wwpdb.utils.nmr.pk.OliviaPKReader import OliviaPKReader
    from wwpdb.utils.nmr.pk.NmrPipePKReader import NmrPipePKReader
    from wwpdb.utils.nmr.pk.PonderosaPKReader import PonderosaPKReader
    from wwpdb.utils.nmr.pk.NmrViewPKReader import NmrViewPKReader
    from wwpdb.utils.nmr.pk.SparkyPKReader import SparkyPKReader
    from wwpdb.utils.nmr.pk.SparkySPKReader import SparkySPKReader
    from wwpdb.utils.nmr.pk.TopSpinPKReader import TopSpinPKReader
    from wwpdb.utils.nmr.pk.VnmrPKReader import VnmrPKReader
    from wwpdb.utils.nmr.pk.XeasyPKReader import XeasyPKReader
    from wwpdb.utils.nmr.pk.XeasyPROTReader import XeasyPROTReader
    from wwpdb.utils.nmr.pk.XwinNmrPKReader import XwinNmrPKReader
except ImportError:
    from nmr.NmrDpConstant import (MR_FILE_PATH_LIST_KEY,
                                   AR_FILE_PATH_LIST_KEY,
                                   MR_MAX_SPACER_LINES,
                                   READABLE_FILE_TYPE,
                                   STD_MON_DICT,
                                   PROTON_BEGIN_CODE,
                                   MAX_DIM_NUM_OF_SPECTRA,
                                   HALF_SPIN_NUCLEUS,
                                   PDB_MR_FILE_HEADER_PAT,
                                   DATABLOCK_PAT,
                                   SF_ANONYMOUS_PAT,
                                   SAVE_PAT,
                                   LOOP_PAT,
                                   STOP_PAT,
                                   COMMENT_PAT,
                                   WS_PAT,
                                   MISMATCHED_INPUT_ERR_MSG,
                                   EXTRANEOUS_INPUT_ERR_MSG,
                                   NO_VIABLE_ALT_ERR_MSG,
                                   EXPECTING_L_PAREN,
                                   LINEAR_MR_FILE_TYPES,
                                   RETRIAL_MR_FILE_TYPES,
                                   PARSABLE_MR_FILE_TYPES,
                                   ARCHIVAL_MR_FILE_TYPES,
                                   PARSABLE_PK_FILE_TYPES,
                                   CS_ERROR_MIN,
                                   CS_ERROR_MAX,
                                   CS_RANGE_MIN,
                                   CS_RANGE_MAX,
                                   DIST_RANGE_MIN,
                                   DIST_RANGE_MAX,
                                   ANGLE_RANGE_MIN,
                                   ANGLE_RANGE_MAX,
                                   RDC_RANGE_MIN,
                                   RDC_RANGE_MAX,
                                   WEIGHT_RANGE_MIN,
                                   WEIGHT_RANGE_MAX,
                                   KNOWN_ANGLE_NAMES,
                                   CYANA_MR_FILE_EXTS,
                                   text_md5)
    from nmr.NmrDpRegistry import (NmrDpRegistry,
                                   get_next_path,
                                   test_path_with_suffix)
    from nmr.AlignUtil import (getRestraintFormatName,
                               getRestraintFormatNames)
    from nmr.NmrVrptUtility import (uncompress_gzip_file,
                                    get_temp_path)
    from nmr.mr.ParserListenerUtil import (translateToStdResName,
                                           startsWithPdbRecord,
                                           getRestraintName)
    from nmr.mr.AmberMRReader import AmberMRReader
    from nmr.mr.AmberPTReader import AmberPTReader
    from nmr.mr.AriaMRReader import AriaMRReader
    from nmr.mr.AriaMRXReader import AriaMRXReader
    from nmr.mr.BareMRReader import BareMRReader
    from nmr.mr.BarePDBReader import BarePDBReader
    from nmr.mr.BiosymMRReader import BiosymMRReader
    from nmr.mr.CharmmCRDReader import CharmmCRDReader
    from nmr.mr.CharmmMRReader import CharmmMRReader
    from nmr.mr.CnsMRReader import CnsMRReader
    from nmr.mr.CyanaMRReader import CyanaMRReader
    from nmr.mr.CyanaNOAReader import CyanaNOAReader
    from nmr.mr.DynamoMRReader import DynamoMRReader
    from nmr.mr.GromacsMRReader import GromacsMRReader
    from nmr.mr.GromacsPTReader import GromacsPTReader
    from nmr.mr.IsdMRReader import IsdMRReader
    from nmr.mr.RosettaMRReader import RosettaMRReader
    from nmr.mr.SchrodingerMRReader import SchrodingerMRReader
    from nmr.mr.SybylMRReader import SybylMRReader
    from nmr.mr.XplorMRReader import XplorMRReader
    from nmr.pk.AriaPKReader import AriaPKReader
    from nmr.pk.BarePKReader import BarePKReader
    from nmr.pk.CcpnPKReader import CcpnPKReader
    from nmr.pk.OliviaPKReader import OliviaPKReader
    from nmr.pk.NmrPipePKReader import NmrPipePKReader
    from nmr.pk.PonderosaPKReader import PonderosaPKReader
    from nmr.pk.NmrViewPKReader import NmrViewPKReader
    from nmr.pk.SparkyPKReader import SparkyPKReader
    from nmr.pk.SparkySPKReader import SparkySPKReader
    from nmr.pk.TopSpinPKReader import TopSpinPKReader
    from nmr.pk.VnmrPKReader import VnmrPKReader
    from nmr.pk.XeasyPKReader import XeasyPKReader
    from nmr.pk.XeasyPROTReader import XeasyPROTReader
    from nmr.pk.XwinNmrPKReader import XwinNmrPKReader


SEL_MR_FILE_HEADER_PAT = re.compile(r'^# Restraints file \((\S+)\): (\S+)\s*')
SEL_PK_FILE_HEADER_PAT = re.compile(r'^# Peak list file \((\S+)\): (\S+)\s*')
SEL_CS_FILE_HEADER_PAT = re.compile(r'^# Chemical shifts file \((\S+)\): (\S+)\s*')

PDB_FIRST_ATOM_PAT = re.compile(r'ATOM +1 .*')

AMBER_A_FORMAT_PAT = re.compile(r'%FORMAT\((\d+)a(\d+)\)\s*')
AMBER_I_FORMAT_PAT = re.compile(r'%FORMAT\((\d+)I(\d+)\)\s*')
AMBER_R_PAT = re.compile(r'r(\d+)=(.*)')

AMBER_TOP_PAT = re.compile(r"^\%FLAG ATOM_NAME\s*")
AMBER_RST_PAT = re.compile(r'\s*&[Rr][Ss][Tt].*')
AMBER_END_PAT = re.compile(r'\s*(?:&[Ee][Nn][Dd]|\/)\s*')
AMBER_MISSING_END_ERR_MSG = "missing END at"  # NOTICE: depends on ANTLR v4 and (Xplor|Cns)MRLexer.g4
AMBER_EXTRA_END_ERR_MSG_PAT = re.compile(r"extraneous input '(?:&[Ee][Nn][Dd]|\/)' expecting .*")  # NOTICE: depends on ANTLR v4
AMBER_EXPECTING_COMMA_PAT = re.compile("expecting \\{.*Comma.*\\}")  # NOTICE: depends on ANTLR v4 and AmberMRLexer.g4

CHARMM_TOP_PAT = re.compile(r"^\s*\d+\sEXT\s*")
CHARMM_RST_PAT = re.compile(r"^\s*KMAX\s+\d+\s+\-\s*")

CYANA_UNSET_INFO_PAT = re.compile(r'\s*unset\s+info.*')
CYANA_PRINT_PAT = re.compile(r'\s*print\s+\".*\".*')

GROMACS_TOP_PAT = re.compile(r"^\[ atoms \]\s*")
GROMACS_RST_PAT = re.compile(r"^\[ (distance|dihedral|orientation)_restraints \]\s*")
GROMACS_COMMENT_PAT = re.compile(r'\s*;+[^0-9]?(.*)')
GROMACS_TAG_PAT = re.compile(r'\s*[\s+[0-9a-z_]+\s+\]')

PDB_TOP_PAT = re.compile(r"^(ATOM|HETATM)\s+\d+\s+\S+\s+\S+\s+(\S+\s+)?\d+\s+([+-]?(\d+(\.\d*)?|\.\d+)\s+){3}.*$")

SPARKY_ASSIGNMENT_PAT = re.compile(r'[\w\+\*\?\'\"\/]+-[\w\+\*\?\'\"\/]+\S*')

XPLOR_ANY_ASSI_PAT = re.compile(r'[Aa][Ss][Ss][Ii][Gg]?[Nn]?')
XPLOR_ANY_REST_PAT = re.compile(r'[Rr][Ee][Ss][Tt][Rr]?[Aa]?[Ii]?[Nn]?[Tt]?[Ss]?')
XPLOR_ANY_SET_PAT = re.compile(r'[Ss][Ee][Tt]')
XPLOR_CLASS_PAT = re.compile(r'\s*[Cc][Ll][Aa][Ss][Ss]?[Ii]?.*')
XPLOR_ASSI_PAT = re.compile(r'\s*[Aa][Ss][Ss][Ii][Gg]?[Nn]?.*')
XPLOR_REST_PAT = re.compile(r'\s*[Rr][Ee][Ss][Tt][Rr]?[Aa]?[Ii]?[Nn]?[Tt]?[Ss]?.*')
XPLOR_SET_PAT = re.compile(r'\s*[Ss][Ee][Tt].*')
XPLOR_END_PAT = re.compile(r'\s*[Ee][Nn][Dd].*')
XPLOR_MISSING_END_ERR_MSG = "missing End at"  # NOTICE: depends on ANTLR v4 and (Xplor|Cns)MRLexer.g4
XPLOR_EXTRA_END_ERR_MSG_PAT = re.compile(r"extraneous input '[Ee][Nn][Dd]' expecting .*")  # NOTICE: depends on ANTLR v4
# NOTICE: depends on ANTLR v4 and (Xplor|Cns)MRLexer.g4
XPLOR_EXTRA_ASSI_ERR_MSG_PAT = re.compile(r"extraneous input '[Aa][Ss][Ss][Ii][Gg]?[Nn]?' expecting L_paren")
XPLOR_EXTRA_SSI_ERR_MSG_PAT = re.compile(r"extraneous input '[Aa]?[Ss][Ss][Ii]\S*' .*")  # NOTICE: depends on ANTLR v4
XPLOR_EXTRA_L_PAREN_ERR_MSG_PAT = re.compile(r"extraneous input '\(' expecting .*")  # NOTICE: depends on ANTLR v4
XPLOR_EXPECTNIG_SYMBOL_PAT = re.compile("expecting \\{.*Symbol_name.*\\}")  # NOTICE: depends on ANTLR v4 and (Xplor|Cns)MRLexer.g4
XPLOR_EXPECTING_EQU_OP_PAT = re.compile("expecting \\{.*Equ_op.*\\}")  # NOTICE: depends on ANTLR v4 and (Xplor|Cns)MRLexer.g4
XPLOR_EXPECTING_SEGID_PAT = re.compile("expecting \\{.*SegIdentifier.*\\}")  # NOTICE: depends on ANTLR v4 and (Xplor|Cns)MRLexer.g4

DEEP_L_PARENS_PAT = re.compile(r'.*\(\s*\(\s*\(\s*\(.*')
DEEP_R_PARENS_PAT = re.compile(r'.*\)\s*\)\s*\)\s*\).*')

POTENTIAL_TYPO_FOR_COMMENT_OUT_PAT = re.compile(r'\s*([13])$')

COMMENT_CODE_MIXED_SET = {'#', '!'}

COMMENT_CODE_SEMICOLON_SET = frozenset(('#', '!', ';'))

PAREN_SPLIT_PAT = re.compile('[ ()]')

# File types whose content subtype is guessed by the light-weight text scan of
# NmrDpMrSplitter.detectContentSubTypeOfLegacyMr(), rather than by a format-specific state machine.
LIGHT_MR_FILE_TYPES = ('nm-res-ari', 'nm-res-bar', 'nm-res-bio', 'nm-res-cya',
                       'nm-res-dyn', 'nm-res-isd', 'nm-res-noa', 'nm-res-syb',
                       'nm-res-ros', 'nm-res-oth')

# Auxiliary molecular topology file types, sharing the light-weight text scan.
AUX_TOP_FILE_TYPES = ('nm-aux-amb', 'nm-aux-cha', 'nm-aux-gro', 'nm-aux-pdb')

# One-letter codes of the standard monomers. STD_MON_DICT.values() is a view, on which
# membership is a linear scan, and the light-weight text scan tests it once per token.
STD_MON_ONE_LETTER_CODES = frozenset(STD_MON_DICT.values())

HBOND_DA_ATOM_TYPES = ('O', 'N', 'F')
RDC_ORIGIN_ATOM_NAMES = ('OO', 'X', 'Y', 'Z')

# Content subtypes detected by the text scan, as (MrContentFlags attribute, label),
# used to compose the "It looks like to have ... instead" part of a content_mismatch message.
DETECTED_SUBTYPE_LABELS = (('has_chem_shift', 'Assigned chemical shifts'),
                           ('has_dist_restraint', 'Distance restraints'),
                           ('has_dihed_restraint', 'Dihedral angle restraints'),
                           ('has_rdc_restraint', 'RDC restraints'),
                           ('has_plane_restraint', 'Planarity restraints'),
                           ('has_hbond_restraint', 'Hydrogen bond restraints'),
                           ('has_ssbond_restraint', 'Disulfide bond restraints'))


def file_md5(fPath: str) -> str:
    """ Return the MD5 digest of the text content of a given file.
    """

    return text_md5(fPath)


def first_index_map(tokens: List[str]) -> dict:
    """ Return a map from token to the position of its first occurrence, which is what
        list.index() reports, without its per-token linear scan.
    """

    first_col = {}

    for col, token in enumerate(tokens):
        if token not in first_col:
            first_col[token] = col

    return first_col


class MrAtomNames:
    """ Atom name sets the text scans of detectContentSubTypeOfLegacyMr() rely on.
    """

    __slots__ = ('atom_like', 'cs_atom_like', 'atom_like_oth', 'cs_atom_like_oth')

    def __init__(self, atom_like: Set[str], cs_atom_like: List[str],
                 atom_like_oth: Set[str], cs_atom_like_oth: Set[str]) -> None:
        self.atom_like = atom_like
        self.cs_atom_like = cs_atom_like
        self.atom_like_oth = atom_like_oth
        self.cs_atom_like_oth = cs_atom_like_oth


class MrContentFlags:
    """ Content subtype indicators collected while scanning a legacy restraint file.
        Passed by reference through the scan and report phases of
        NmrDpMrSplitter.detectContentSubTypeOfLegacyMr().
    """

    __slots__ = ('has_chem_shift', 'has_dist_restraint', 'has_dihed_restraint', 'has_rdc_restraint',
                 'has_plane_restraint', 'has_hbond_restraint', 'has_ssbond_restraint', 'has_rdc_origins',
                 'has_spectral_peak', 'has_coordinate', 'has_amb_coord', 'has_amb_inpcrd', 'has_ens_coord',
                 'has_topology', 'has_first_atom')

    def __init__(self) -> None:
        self.has_chem_shift = self.has_dist_restraint = self.has_dihed_restraint = self.has_rdc_restraint =\
            self.has_plane_restraint = self.has_hbond_restraint = self.has_ssbond_restraint =\
            self.has_rdc_origins = self.has_spectral_peak = self.has_coordinate = self.has_amb_coord =\
            self.has_amb_inpcrd = self.has_ens_coord = self.has_topology = self.has_first_atom = False

    def hasAnyRestraint(self) -> bool:
        """ Return whether any restraint subtype has been detected.
        """
        return self.has_dist_restraint or self.has_dihed_restraint or self.has_rdc_restraint\
            or self.has_plane_restraint or self.has_hbond_restraint or self.has_ssbond_restraint

    def sniffCoordinateLine(self, line: str) -> Optional[str]:
        """ Update the coordinate indicators for a given line.
            @return: 'atom' for a coordinate record, 'model' for an ensemble marker, None otherwise
        """

        if line.startswith('ATOM ') and line.count('.') >= 3:
            self.has_coordinate = True
            if PDB_FIRST_ATOM_PAT.match(line):
                if self.has_first_atom:
                    self.has_ens_coord = True
                self.has_first_atom = True
            return 'atom'

        if line.startswith('MODEL') or line.startswith('ENDMDL')\
                or line.startswith('_atom_site.pdbx_PDB_model_num')\
                or line.startswith('_atom_site.ndb_model'):
            self.has_ens_coord = True
            return 'model'

        return None


class AmbTopScanner:
    """ AMBER topology (.prmtop) detector. All four sections must be present, each with a
        parsable %FORMAT header and at least one value. Also recognizes an AMBER restart
        (aka. .crd or .rst) file, whose header is a title line, an atom count, then coordinates.
    """

    # (%FLAG keyword, %FORMAT pattern, whether the values are integers)
    SECTIONS = (('%FLAG ATOM_NAME', AMBER_A_FORMAT_PAT, False),
                ('%FLAG RESIDUE_LABEL', AMBER_A_FORMAT_PAT, False),
                ('%FLAG RESIDUE_POINTER', AMBER_I_FORMAT_PAT, True),
                ('%FLAG AMBER_ATOM_TYPE', AMBER_A_FORMAT_PAT, False))

    __slots__ = ('__has_section', '__chk_format', '__in_section', '__values', '__max_cols', '__max_char')

    def __init__(self, atom_like_names: Set[str]) -> None:  # pylint: disable=unused-argument
        self.__has_section = [False] * len(self.SECTIONS)
        self.__chk_format = [False] * len(self.SECTIONS)
        self.__in_section = [False] * len(self.SECTIONS)
        self.__values = [0] * len(self.SECTIONS)
        self.__max_cols = self.__max_char = 0

    def __columns(self, line: str):
        """ Yield the fixed-width fields of a line, as declared by the last %FORMAT header.
        """

        len_line = len(line)
        begin = col = 0
        end = self.__max_char

        while col < self.__max_cols and end < len_line:
            yield line[begin:end]
            begin = end
            end += self.__max_char
            col += 1

    def feed(self, line: str, pos: int, flags: MrContentFlags) -> bool:
        """ Consume a line of an AMBER topology file.
            @return: whether the line has been consumed, i.e. must not be scanned further
        """

        if pos == 1 and not line.isdigit():
            flags.has_amb_inpcrd = True

        elif pos == 2 and flags.has_amb_inpcrd:
            try:
                int(line.lstrip().split()[0])
            except (ValueError, IndexError):
                flags.has_amb_inpcrd = False

        elif pos == 3 and flags.has_amb_inpcrd:
            if line.count('.') != 6:
                flags.has_amb_inpcrd = False

        if line.startswith('%FLAG'):
            # NOTE: AMBER_ATOM_TYPE is deliberately not reset here, as in the original code
            self.__in_section[0] = self.__in_section[1] = self.__in_section[2] = False

            for idx, (keyword, _, _) in enumerate(self.SECTIONS):
                if line.startswith(keyword):
                    self.__has_section[idx] = self.__chk_format[idx] = True
                    break

            return False

        for idx, (_, format_pat, _) in enumerate(self.SECTIONS):

            if not self.__chk_format[idx]:
                continue

            g = format_pat.match(line)

            if g:
                self.__in_section[idx] = True
                self.__max_cols, self.__max_char = int(g.group(1)), int(g.group(2))
            else:
                self.__has_section[idx] = False

            self.__chk_format[idx] = False

            return False

        for idx, (_, _, as_int) in enumerate(self.SECTIONS):

            if not self.__in_section[idx]:
                continue

            for field in self.__columns(line):
                if as_int:
                    try:
                        int(field.lstrip())
                    except ValueError:
                        continue
                    self.__values[idx] += 1
                elif len(field.rstrip()) > 0:
                    self.__values[idx] += 1

            return False

        return False

    def isTopology(self) -> bool:
        """ Return whether a complete AMBER topology has been found.
        """
        return all(self.__has_section) and all(value > 0 for value in self.__values)


class ChaTopScanner:
    """ CHARMM topology (aka. CRD or CHARMM CARD file) detector, keyed on the
        '{Number of atoms} EXT' header followed by atom records.
    """

    __slots__ = ('__atom_like_names', '__has_ext', '__in_atoms', '__atom_names')

    def __init__(self, atom_like_names: Set[str]) -> None:
        self.__atom_like_names = atom_like_names
        self.__has_ext = self.__in_atoms = False
        self.__atom_names = 0

    def feed(self, line: str, pos: int, flags: MrContentFlags) -> bool:  # pylint: disable=unused-argument
        """ Consume a line of a CHARMM topology file.
            @return: whether the line has been consumed, i.e. must not be scanned further
        """

        if 'EXT' in line:
            l_split = line.split()

            if len(l_split) > 1 and l_split[0].isdigit() and l_split[1] == 'EXT':
                self.__has_ext = self.__in_atoms = True
                return True

        elif self.__in_atoms:
            l_split = line.split()
            _line = ' '.join(l_split)

            if len(_line) == 0 or _line[0] in COMMENT_CODE_SEMICOLON_SET:
                return True

            if len(l_split) >= 10:
                try:
                    atom_num = int(l_split[0])
                    seq_id = int(l_split[8])
                    comp_id = l_split[2]
                    atom_id = l_split[3]
                    if atom_num > 0 and seq_id > 0 and comp_id in STD_MON_DICT\
                       and atom_id in self.__atom_like_names:
                        self.__atom_names += 1
                except ValueError:
                    pass

        return False

    def isTopology(self) -> bool:
        """ Return whether a complete CHARMM topology has been found.
        """
        return self.__has_ext and self.__atom_names > 0


class GroTopScanner:
    """ GROMACS topology detector, requiring non-empty '[ system ]', '[ molecules ]',
        and '[ atoms ]' sections.
    """

    __slots__ = ('__atom_like_names', '__has_system', '__has_molecules', '__has_atoms',
                 '__in_system', '__in_molecules', '__in_atoms',
                 '__system_names', '__molecule_names', '__atom_names')

    def __init__(self, atom_like_names: Set[str]) -> None:
        self.__atom_like_names = atom_like_names
        self.__has_system = self.__has_molecules = self.__has_atoms = False
        self.__in_system = self.__in_molecules = self.__in_atoms = False
        self.__system_names = self.__molecule_names = self.__atom_names = 0

    def feed(self, line: str, pos: int, flags: MrContentFlags) -> bool:  # pylint: disable=unused-argument
        """ Consume a line of a GROMACS topology file.
            @return: whether the line has been consumed, i.e. must not be scanned further
        """

        if line.startswith('['):
            self.__in_system = self.__in_molecules = self.__in_atoms = False

            if line.startswith('[ system ]'):
                self.__has_system = self.__in_system = True

            elif line.startswith('[ molecules ]'):
                self.__has_molecules = self.__in_molecules = True

            elif line.startswith('[ atoms ]'):
                self.__has_atoms = self.__in_atoms = True

        elif self.__in_system or self.__in_molecules or self.__in_atoms:
            l_split = line.split()
            _line = ' '.join(l_split)

            if len(_line) == 0 or _line[0] in COMMENT_CODE_SEMICOLON_SET:
                return True

            if self.__in_system:
                self.__system_names += 1

            elif self.__in_molecules:
                if len(l_split) == 2:
                    try:
                        num = int(l_split[1])
                        if num > 0 and l_split[0].isalnum():
                            self.__molecule_names += 1
                    except ValueError:
                        pass

            else:  # [ atoms ]
                if len(l_split) > 6:
                    try:
                        atom_num = int(l_split[0])
                        seq_id = int(l_split[2])
                        comp_id = l_split[3]
                        atom_id = l_split[4]
                        if atom_num > 0 and seq_id > 0 and comp_id in STD_MON_DICT\
                           and atom_id in self.__atom_like_names:
                            self.__atom_names += 1
                    except ValueError:
                        pass

        return False

    def isTopology(self) -> bool:
        """ Return whether a complete GROMACS topology has been found.
        """
        return self.__has_system and self.__has_molecules and self.__has_atoms\
            and self.__system_names > 0 and self.__molecule_names > 0 and self.__atom_names > 0


class PdbTopScanner:
    """ PDB topology detector, counting atom records whose comp_id and atom_id are recognized.
    """

    __slots__ = ('__atom_like_names', '__atom_names')

    def __init__(self, atom_like_names: Set[str]) -> None:
        self.__atom_like_names = atom_like_names
        self.__atom_names = 0

    def feed(self, line: str, pos: int, flags: MrContentFlags) -> bool:  # pylint: disable=unused-argument
        """ Consume a line of a PDB topology file.
            @return: whether the line has been consumed, i.e. must not be scanned further
        """

        l_split = line.split()
        _line = ' '.join(l_split)

        if len(_line) == 0 or _line[0] in COMMENT_CODE_SEMICOLON_SET:
            return True

        if len(l_split) >= 10:
            try:
                atom_num = int(l_split[1])
                seq_id = int(l_split[4] if l_split[4].isdigit() else l_split[5])
                comp_id = l_split[3]
                atom_id = l_split[2]
                if atom_num > 0 and seq_id > 0 and comp_id in STD_MON_DICT\
                   and atom_id in self.__atom_like_names:
                    # if atom_num == 1:
                    #     has_top_num = True
                    self.__atom_names += 1
            except ValueError:
                pass

        return False

    def isTopology(self) -> bool:
        """ Return whether a PDB topology has been found.
        """
        return self.__atom_names > 0


# Topology detector per auxiliary file type. Every detector is constructed with the atom name
# set of the non-standard residues, and exposes feed() and isTopology().
AUX_TOP_SCANNERS = {'nm-aux-amb': AmbTopScanner,
                    'nm-aux-cha': ChaTopScanner,
                    'nm-aux-gro': GroTopScanner,
                    'nm-aux-pdb': PdbTopScanner}


def detect_bom(fPath: str, default: str = 'utf-8') -> str:
    """ Detect BOM of input file.
    """

    with open(fPath, 'rb') as ifh:
        raw = ifh.read(4)

    for enc, boms in \
            ('utf-8-sig', (codecs.BOM_UTF8,)), \
            ('utf-16', (codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE)), \
            ('utf-32', (codecs.BOM_UTF32_LE, codecs.BOM_UTF32_BE)):
        if any(raw.startswith(bom) for bom in boms):
            return enc

    return default


def convert_codec(inPath: str, outPath: str, in_codec: str = 'utf-8', out_codec: str = 'utf-8') -> None:
    """ Convert codec of input file.
    """

    with open(inPath, 'rb') as ifh, \
            open(outPath, 'w+b') as ofh:
        contents = ifh.read()
        ofh.write(contents.decode(in_codec).encode(out_codec))


def convert_rtf_to_ascii(inPath: str, outPath: str) -> None:
    """ Convert RTF file to ASCII text file.
    """

    with open(inPath, 'r') as ifh, \
            open(outPath, 'w+', encoding='utf-8') as ofh:  # pylint: disable=unspecified-encoding
        contents = ifh.read()
        ofh.write(rtf_to_text(contents, encoding='ascii', errors='ignore'))


def is_binary_file(fPath: str) -> bool:
    """ Check if there are non-ascii or non-printable characters in a file.
    """

    with open(fPath, 'rb') as ifh:
        chunk = ifh.read(1024)
        if b'\0' in chunk:
            return True

    return False


def is_rtf_file(fPath: str) -> bool:
    """ Check if there are RTF header characters in a file.
    """

    with open(fPath, 'rb') as ifh:
        chunk = ifh.read(1024)
        if b'\x7b\x5c\x72\x74\x66\x31' in chunk:
            return True

    return False


def is_eps_or_pdf_file(fPath: str) -> bool:
    """ Check if there are EPS/PDF header characters in a file.
    """

    with open(fPath, 'rb') as ifh:
        chunk = ifh.read(5)
        if chunk in (b'%!PS-', b'%PDF-'):
            return True

    return False


def is_star_file(fPath: str) -> bool:
    """ Check if a given file contains STAR syntax.
    """

    has_datablock = False
    has_anonymous_saveframe = False
    has_save = False
    has_loop = False
    has_stop = False

    with open(fPath, "r", encoding='utf-8', errors='ignore') as ifh:
        for line in ifh:
            if DATABLOCK_PAT.match(line):
                has_datablock = True
            elif SF_ANONYMOUS_PAT.match(line):
                has_anonymous_saveframe = True
            elif SAVE_PAT.match(line):
                has_save = True
            elif LOOP_PAT.match(line):
                has_loop = True
            elif STOP_PAT.match(line):
                has_stop = True

    return has_datablock or has_anonymous_saveframe or has_save or has_loop or has_stop


def is_amb_top_file(fPath: str) -> bool:
    """ Check if a given file contains AMBER topology/parameter syntax.
    """

    with open(fPath, "r", encoding='utf-8', errors='ignore') as ifh:
        for line in ifh:
            if AMBER_TOP_PAT.match(line):
                return True

    return False


def is_amb_rst_file(fPath: str) -> bool:
    """ Check if a given file contains AMBER restraint syntax.
    """

    with open(fPath, "r", encoding='utf-8', errors='ignore') as ifh:
        for line in ifh:
            if AMBER_RST_PAT.match(line):
                return True

    return False


def is_cha_top_file(fPath: str) -> bool:
    """ Check if a given file contains CHARMM topology/parameter syntax.
    """

    with open(fPath, "r", encoding='utf-8', errors='ignore') as ifh:
        for line in ifh:
            if CHARMM_TOP_PAT.match(line):
                return True

    return False


def is_cha_rst_file(fPath: str) -> bool:
    """ Check if a given file contains CHARMM restraint syntax.
    """

    with open(fPath, "r", encoding='utf-8', errors='ignore') as ifh:
        for line in ifh:
            if CHARMM_RST_PAT.match(line):
                return True

    return False


def is_gro_top_file(fPath: str) -> bool:
    """ Check if a given file contains GROMACS topology/parameter syntax.
    """

    with open(fPath, "r", encoding='utf-8', errors='ignore') as ifh:
        for line in ifh:
            if GROMACS_TOP_PAT.match(line):
                return True

    return False


def is_gro_rst_file(fPath: str) -> bool:
    """ Check if a given file contains GROMACS restraint syntax.
    """

    with open(fPath, "r", encoding='utf-8', errors='ignore') as ifh:
        for line in ifh:
            if GROMACS_RST_PAT.match(line):
                return True

    return False


def is_pdb_top_file(fPath: str) -> bool:
    """ Check if a given file contains PDB-line topology/parameter syntax.
    """

    with open(fPath, "r", encoding='utf-8', errors='ignore') as ifh:
        for line in ifh:
            if PDB_TOP_PAT.match(line):
                return True

    return False


def detect_encoding(line: str) -> str:
    """ Return encoding of a given string.
    """

    try:
        result = chardet.detect(line.encode('utf-8'))
        return result['encoding']
    except Exception:  # pylint: disable=broad-exception-caught
        return 'binary'


def get_type_of_star_file(fPath: str) -> str:
    """ Return type of a STAR file.
        @return: 'str' for STAR, 'cif' for CIF, 'other' otherwise
    """

    codec = detect_bom(fPath, 'utf-8')

    _fPath = __fPath = None

    if codec != 'utf-8':
        _fPath = get_temp_path(fPath)
        convert_codec(fPath, _fPath, codec, 'utf-8')
        fPath = _fPath

    if is_rtf_file(fPath):
        __fPath = get_temp_path(fPath, '.rtf2txt')
        convert_rtf_to_ascii(fPath, __fPath)
        fPath = __fPath

    try:

        is_cif = has_datablock = has_anonymous_saveframe = has_save = has_loop = has_stop = False

        with open(fPath, 'r', encoding='utf-8', errors='ignore') as ifh:
            for line in ifh:
                str_syntax = False
                if DATABLOCK_PAT.match(line):
                    str_syntax = has_datablock = True
                elif SF_ANONYMOUS_PAT.match(line):
                    str_syntax = has_anonymous_saveframe = True
                elif SAVE_PAT.match(line):
                    str_syntax = has_save = True
                elif LOOP_PAT.match(line):
                    str_syntax = has_loop = True
                elif STOP_PAT.match(line):
                    str_syntax = has_stop = True

                if str_syntax:
                    if (has_anonymous_saveframe and has_save) or (has_loop and has_stop):
                        return 'str'
                    if has_datablock and has_loop and not has_stop:
                        is_cif = True

        return 'cif' if is_cif else 'other'

    finally:

        if _fPath is not None:
            try:
                os.remove(_fPath)
            except OSError:
                pass

        if __fPath is not None:
            try:
                os.remove(__fPath)
            except OSError:
                pass


def concat_restraint_names(content_subtype: Optional[str]) -> str:
    """ Return concatenated restraint names.
    """

    if content_subtype is None:
        return ''

    f = []

    for k, v in content_subtype.items():
        if v == 0:
            continue
        try:
            f.append(getRestraintName(k))
        except KeyError:
            pass

    return ', '.join(f)


def get_peak_list_format(fPath: str, asCode: bool = False
                         ) -> Optional[str]:
    """ Return peak list format for an input file.
    """

    if not os.path.exists(fPath):
        return None

    header = None

    with open(fPath, 'r', encoding='utf-8', errors='ignore') as ifh:

        for idx, line in enumerate(ifh):

            if line.isspace() or COMMENT_PAT.match(line):

                if 'Number of dimensions' in line or line.startswith('#INAME') or line.startswith('#CYANAFORMAT')\
                   or ('Amplitude' in line or 'Intensity' in line or 'Volume' in line):
                    header = line

                else:  # XwinNMR, but not CCPN

                    file_type = get_peak_list_format_from_string(line, header, asCode)

                    if file_type is not None:

                        if file_type in ('CCPN', 'nm-pea-ccp'):
                            header = line
                            continue

                        return file_type

                continue

            if 'label' in line and 'data' in line and 'dataset' not in line:
                header = line
                continue

            if (' w1 ' in line and ' w2' in line) or ('Assignment' in line and 'Shift (ppm)' in line)\
               or ('eak' in line and ('abel' in line or 'nnotation' in line or 'ssign' in line)
                   and ('F1' in line or 'f1' in line) and ('F2' in line or 'f2' in line)):
                header = line
                continue

            file_type = get_peak_list_format_from_string(line, header, asCode)

            if file_type is not None or idx >= MR_MAX_SPACER_LINES:

                if file_type in ('Sparky', 'nm-pea-spa') and idx < 20 and header is not None\
                   and 'Assignment' in header and 'Shift (ppm)' in header:

                    col = re.split(r'[\s\t]+', line.strip())
                    len_col = len(col)

                    if SPARKY_ASSIGNMENT_PAT.match(col[0]):

                        d = len_col - 1

                        if d == 2:
                            header = ' Assignment  w1  w2\n'
                        elif d == 3:
                            header = ' Assignment  w1  w2  w3\n'
                        elif d == 4:
                            header = ' Assignment  w1  w2  w3  w4\n'
                        else:
                            return None

                        try:

                            fPath_next = get_temp_path(fPath)

                            with open(fPath, 'r', encoding='utf-8', errors='ignore') as ifh, \
                                    open(fPath_next, 'w', encoding='utf-8') as ofh:
                                ofh.write(header)
                                for _line in ifh:
                                    if 'peaks' in _line or 'Shift (ppm)' in _line:
                                        continue
                                    ofh.write(_line)

                            os.replace(fPath_next, fPath)

                        except OSError:
                            pass

                if file_type in ('CCPN', 'nm-pea-ccp') and idx < 20 and header is not None\
                   and ('Position F1' in header or 'Shift F1' in header) and ('Position F2' in header or 'Shift F2' in header)\
                   and (('Assign F1' in header and 'Assign F2' in header) or ('Height' in header or 'Volume' in header)):

                    header = header.replace('#', '')

                    try:

                        fPath_next = get_temp_path(fPath)

                        with open(fPath, 'r', encoding='utf-8', errors='ignore') as ifh, \
                                open(fPath_next, 'w', encoding='utf-8') as ofh:
                            ofh.write(header)
                            for _line in ifh:

                                if ('Position F1' in _line or 'Shift F1' in _line)\
                                   and ('Position F2' in _line or 'Shift F2' in _line)\
                                   and 'Assign F1' in _line and 'Assign F2' in _line:
                                    # and ('Height' in _line or 'Volume' in _line):
                                    continue

                                if not _line.startswith('#'):
                                    ofh.write(_line)

                        os.replace(fPath_next, fPath)

                    except OSError:
                        pass

                if file_type in ('CCPN', 'nm-pea-ccp') and idx < 20 and header is None and ',' in line\
                   and ('Position F1' in line or 'Shift F1' in line) and ('Position F2' in line or 'Shift F2' in line)\
                   and (('Assign F1' in line and 'Assign F2' in line) or ('Height' in line or 'Volume' in line)):

                    try:

                        fPath_next = get_temp_path(fPath)

                        with open(fPath, 'r', encoding='utf-8', errors='ignore') as ifh, \
                                open(fPath_next, 'w', encoding='utf-8') as ofh:
                            for _line in ifh:
                                ofh.write(_line.replace(',', ' '))

                        os.replace(fPath_next, fPath.replace('~', ''))

                    except OSError:
                        pass

                if file_type is None or idx < 20:
                    return file_type

                # fix partially broken NMRVIEW header
                if file_type in ('NMRView', 'nm-pea-vie') and header is not None\
                   and 'label' in header and 'data' in header and 'dataset' not in header\
                   and 'sw' in line and 'sf' in line:

                    try:

                        i = 0

                        fPath_next = get_temp_path(fPath)

                        with open(fPath, 'r', encoding='utf-8', errors='ignore') as ifh, \
                                open(fPath_next, 'w', encoding='utf-8') as ofh:
                            for _line in ifh:
                                if i == idx - 1:
                                    ofh.write('label dataset sw sf\n')
                                elif i == idx:
                                    pass
                                else:
                                    ofh.write(_line)
                                i += 1

                        os.replace(fPath_next, fPath)

                    except OSError:
                        pass

                    return file_type

                # fix partially broken SPARKY header
                if file_type in ('Sparky', 'nm-pea-spa') and header is None\
                   and ' w1 ' not in line and ' w2' not in line:

                    col = re.split(r'[\s\t]+', line.strip())
                    len_col = len(col)

                    if SPARKY_ASSIGNMENT_PAT.match(col[0]):

                        d = len_col - 2

                        if d == 2:
                            header = ' Assignment  w1  w2  Data Height\n'
                        elif d == 3:
                            header = ' Assignment  w1  w2  w3  Data Height\n'
                        elif d == 4:
                            header = ' Assignment  w1  w2  w3  w4  Data Height\n'
                        else:
                            return None

                    else:

                        d = len_col - 1

                        if d == 2:
                            header = ' w1  w2  Data Height\n'
                        elif d == 3:
                            header = ' w1  w2  w3  Data Height\n'
                        elif d == 4:
                            header = ' w1  w2  w3  w4  Data Height\n'
                        else:
                            return None

                    try:

                        fPath_next = get_temp_path(fPath)

                        with open(fPath, 'r', encoding='utf-8', errors='ignore') as ifh, \
                                open(fPath_next, 'w', encoding='utf-8') as ofh:
                            ofh.write(header)
                            for _line in ifh:
                                ofh.write(_line)

                        os.replace(fPath_next, fPath)

                    except OSError:
                        pass

                    return file_type

    return None


def get_peak_list_format_from_string(string: str, header: Optional[str] = None, asCode: bool = False
                                     ) -> Optional[str]:
    """ Return peak list format for a given input.
    """

    col = re.split(r'[\s\t]+', string.strip())
    string = ' '.join(col)
    len_col = len(col)

    if header is not None and ('Number of dimensions' in header or header.startswith('#INAME')
                               or header.startswith('#CYANAFORMAT')):  # XEASY peak list
        if 'U' in col or 'T' in col:
            return 'nm-pea-xea' if asCode else 'XEASY'

    if ' w1 ' in string and ' w2' in string:  # Sparky peak list
        return 'nm-pea-spa' if asCode else 'Sparky'

    if '<sparky save file>' in string:  # Sparky save file
        return 'nm-pea-sps' if asCode else 'Sparky'

    if 'label' in string and 'dataset' in string and 'sw' in string and 'sf' in string:  # NMRView peak list
        return 'nm-pea-vie' if asCode else 'NMRView'

    if 'TYPEDEF IDX_TBL_' in string or 'TYPEDEF ASS_TBL_' in string:  # OLIVIA
        return 'nm-pea-oli' if asCode else 'Olivia'

    if 'VARS' in string and 'X_PPM' in string and 'Y_PPM' in string:  # NMRPipe peak list
        return 'nm-pea-pip' if asCode else 'NMRPipe'

    if 'VARS' in string and 'PkID' in string and 'X' in string and 'Y' in string and 'Intensity' in string:  # PIPP peak list
        return 'nm-pea-pip' if asCode else 'NMRPipe'

    if 'DATA' in string and 'DIMCOUNT' in string:
        return 'nm-pea-pip' if asCode else 'NMRPipe'

    if '<!DOCTYPE spectrum SYSTEM' in string or '<spectrum name=' in string:  # ARIA peak list
        return 'nm-pea-ari' if asCode else 'ARIA'

    if ('Position F1' in string or 'Shift F1' in string) and ('Position F2' in string or 'Shift F2' in string)\
       and (('Assign F1' in string and 'Assign F2' in string) or ('Height' in string or 'Volume' in string)):
        return 'nm-pea-ccp' if asCode else 'CCPN'

    if 'NOESYTYPE' in string:  # PONDEROSA peak list
        return 'nm-pea-pon' if asCode else 'PONDEROSA'

    if '<PeakList>' in string:  # TopSpin peak list
        return 'nm-pea-top' if asCode else 'TopSpin'

    if 'peak id.' in string and 'Dim 0' in string and 'Dim 1' in string\
       and ('Amplitude' in string or 'Intensity' in string) and 'Assignment' in string:  # VNMR peak list
        return 'nm-pea-vnm' if asCode else 'VNMR'

    if '# Peak List from VNMR' in string\
       or ('Peak_Number' in string
           and (('X' in string and 'Y' in string) or ('F1' in string and 'F2' in string))
           and ('Amplitude' in string or 'Intensity' in string)):  # VNMR ll2d output
        return 'nm-pea-vnm' if asCode else 'VNMR'

    if '# PEAKLIST_VERSION' in string or '# PEAKLIST_DIMENSION' in string:  # XwinNMR peak list
        return 'nm-pea-xwi' if asCode else 'XwinNMR'

    if 'eak' in string and ('able' in string or 'nnotation' in string or 'ssign' in string)\
       and ('F1' in string or 'f1' in string) and ('F2' in string or 'f2' in string) and 'Position' not in string:
        offset = 0
        if 'mplitude' in string or 'ntensity' in string or 'eight' in string:
            offset += 1
        if 'olume' in string:
            offset += 1
        if offset > 0:
            return 'nm-pea-bar' if asCode else 'unknown'

    if ('F1' in string or 'f1' in string) and ('F2' in string or 'f2' in string) and 'Position' not in string:
        offset = 0
        if 'mplitude' in string or 'ntensity' in string or 'eight' in string:
            offset += 1
        if 'olume' in string:
            offset += 1
        if offset > 0:
            return 'nm-pea-bar' if asCode else 'unknown'

    if '1Dim' in string and '2Dim' in string and 'Intensity' in string:  # 8ep5
        return 'nm-pea-bar' if asCode else 'unknown'

    if header is None:

        if 2 <= len_col - 1 <= 4:
            try:
                if all('.' in col[idx] and CS_ERROR_MIN < float(col[idx]) < CS_ERROR_MAX for idx in range(len_col - 1)):
                    if abs(float(col[-1])) >= CS_ERROR_MAX:
                        return 'nm-pea-spa' if asCode else 'Sparky'  # header broken SPARKY
            except (ValueError, TypeError):
                pass

        if 2 <= len_col - 2 <= 4 and SPARKY_ASSIGNMENT_PAT.match(col[0]):
            try:
                if all('.' in col[idx + 1] and CS_ERROR_MIN < float(col[idx + 1]) < CS_ERROR_MAX for idx in range(len_col - 2)):
                    if abs(float(col[-1])) >= CS_ERROR_MAX:
                        return 'nm-pea-spa' if asCode else 'Sparky'  # header broken SPARKY
            except (ValueError, TypeError):
                pass

        return None

    if ' w1 ' in header and ' w2' in header\
       and len_col > 2 and ('Assignment' not in header or SPARKY_ASSIGNMENT_PAT.match(col[0])):  # Sparky
        try:
            float(col[1])
            float(col[2])
            return 'nm-pea-spa' if asCode else 'Sparky'
        except (ValueError, TypeError):
            pass

    if 'Assignment' in header and 'Shift (ppm)' in header\
       and len_col > 2 and SPARKY_ASSIGNMENT_PAT.match(col[0]):  # Sparky
        try:
            float(col[1])
            float(col[2])
            return 'nm-pea-spa' if asCode else 'Sparky'
        except (ValueError, TypeError):
            pass

    if ('Position F1' in header or 'Shift F1' in header) and ('Position F2' in header or 'Shift F2' in header)\
       and (('Assign F1' in header and 'Assign F2' in header) or ('Height' in header or 'Volume' in header)):
        if len_col > 4 and not col[0].isdigit():
            return 'nm-pea-ccp' if asCode else 'CCPN'  # header broken CCPN

    if ('Amplitude' in header or 'Intensity' in header)\
       and 'Assignment' in header:
        if len_col > 6 and SPARKY_ASSIGNMENT_PAT.match(col[6]):  # VNMR 2D
            try:
                int(col[0])
                float(col[1])
                float(col[3])
                return 'nm-pea-vnm' if asCode else 'VNMR'
            except (ValueError, TypeError):
                pass

        elif len_col > 8 and SPARKY_ASSIGNMENT_PAT.match(col[8]):  # VNMR 3D
            try:
                int(col[0])
                float(col[1])
                float(col[3])
                float(col[5])
                return 'nm-pea-vnm' if asCode else 'VNMR'
            except (ValueError, TypeError):
                pass

        elif len_col > 10 and SPARKY_ASSIGNMENT_PAT.match(col[10]):  # VNMR 4D
            try:
                int(col[0])
                float(col[1])
                float(col[3])
                float(col[5])
                float(col[7])
                return 'nm-pea-vnm' if asCode else 'VNMR'
            except (ValueError, TypeError):
                pass

    if 'eak' in header and ('able' in header or 'nnotation' in header or 'ssign' in header)\
       and ('F1' in header or 'f1' in header) and ('F2' in header or 'f2' in header) and 'Position' not in header:
        offset = 0
        if 'mplitude' in header or 'ntensity' in header or 'eight' in header:
            offset += 1
        if 'olume' in header:
            offset += 1
        if 'F3' not in header and 'f3' not in header and 'F4' not in header and 'f4' not in header\
           and len_col > 3 + offset and SPARKY_ASSIGNMENT_PAT.match(col[3 + offset]):
            try:
                int(col[0])
                float(col[1])
                float(col[2])
                return 'nm-pea-bar' if asCode else 'unknown'
            except (ValueError, TypeError):
                pass

        elif 'F4' not in header and 'f4' not in header\
                and len_col > 4 + offset and SPARKY_ASSIGNMENT_PAT.match(col[4 + offset]):
            try:
                int(col[0])
                float(col[1])
                float(col[2])
                float(col[3])
                return 'nm-pea-bar' if asCode else 'unknown'
            except (ValueError, TypeError):
                pass

        elif len_col > 5 + offset and SPARKY_ASSIGNMENT_PAT.match(col[5 + offset]):
            try:
                int(col[0])
                float(col[1])
                float(col[2])
                float(col[3])
                float(col[4])
                return 'nm-pea-bar' if asCode else 'unknown'
            except (ValueError, TypeError):
                pass

    if ('F1' in header or 'f1' in header) and ('F2' in header or 'f2' in header) and 'Position' not in header:
        offset = 0
        if 'mplitude' in header or 'ntensity' in header or 'eight' in header:
            offset += 1
        if 'olume' in header:
            offset += 1
        if 'F3' not in header and 'f3' not in header and 'F4' not in header and 'f4' not in header and offset > 0:
            try:
                int(col[0])
                float(col[1])
                float(col[2])
                return 'nm-pea-bar' if asCode else 'unknown'
            except (ValueError, TypeError):
                pass

        elif 'F4' not in header and 'f4' not in header and offset > 0:
            try:
                int(col[0])
                float(col[1])
                float(col[2])
                float(col[3])
                return 'nm-pea-bar' if asCode else 'unknown'
            except (ValueError, TypeError):
                pass

        elif offset > 0:
            try:
                int(col[0])
                float(col[1])
                float(col[2])
                float(col[3])
                float(col[4])
                return 'nm-pea-bar' if asCode else 'unknown'
            except (ValueError, TypeError):
                pass

    if '1Dim' in header and '2Dim' in header and 'Intensity' in header:  # 8ep5
        if '3Dim' not in header and '4Dim' not in header\
           and len_col > 3:
            try:
                int(col[0])
                float(col[1])
                float(col[2])
                return 'nm-pea-bar' if asCode else 'unknown'
            except (ValueError, TypeError):
                pass

        elif '4Dim' not in header\
                and len_col > 4:
            try:
                int(col[0])
                float(col[1])
                float(col[2])
                float(col[3])
                return 'nm-pea-bar' if asCode else 'unknown'
            except (ValueError, TypeError):
                pass

        elif len_col > 5:
            try:
                int(col[0])
                float(col[1])
                float(col[2])
                float(col[3])
                float(col[4])
                return 'nm-pea-bar' if asCode else 'unknown'
            except (ValueError, TypeError):
                pass

    if 'label' in header and 'data' in header and 'dataset' not in header\
       and 'sw' in col and 'sf' in col:
        return 'nm-pea-vie' if asCode else 'NMRView'  # header broken NMRVIEW

    return None


def get_number_of_dimensions_of_peak_list(fPath: str, file_format: Optional[str]
                                          ) -> Optional[int]:
    """ Return number of dimensions for an input peak list file.
    """

    if file_format is None or not os.path.exists(fPath):
        return None

    with open(fPath, 'r', encoding='utf-8') as ifh:

        has_header = False

        for idx, line in enumerate(ifh):

            if file_format == 'NMRView' and not has_header:

                if 'sw' in line and 'sf' in line:
                    has_header = True

                continue

            dimensions = get_number_of_dimensions_of_peak_list_from_string(file_format, line)

            if dimensions is not None and 0 < dimensions <= MAX_DIM_NUM_OF_SPECTRA:
                return dimensions

            if idx >= MR_MAX_SPACER_LINES:
                break

    return None


def get_number_of_dimensions_of_peak_list_from_string(file_format: str, line: str
                                                      ) -> Optional[int]:
    """ Return number of dimensions of peak list of given format and input.
    """

    col = re.split(r'[\s\t]+', line.strip())
    len_col = len(col)

    if file_format == 'XEASY':
        if 'Number of dimensions' in line:
            if col[-1].isdigit():
                return int(col[-1])
        if 'xeasy2D' in line:
            return 2
        if 'xeasy3D' in line:
            return 3
        if 'xeasy4D' in line:
            return 4
        if line.startswith('#CYANAFORMAT'):
            if all(a.isalpha() for a in col[1]):
                return len(col[1])

    if file_format == 'Sparky':
        if ' w1 ' in line:
            dim = [int(w[1:]) for w in col if w.startswith('w') and w[1:].isdigit()]
            if len(dim) > 0:
                return max(dim)

        if len_col > 3 and SPARKY_ASSIGNMENT_PAT.match(col[0]):
            return col[0].count('-') + 1

    if file_format == 'NMRView':
        return len_col

    if file_format == 'NMRPipe':
        if 'VARS' in line:
            if 'A_PPM' in col:
                return 4
            if 'Z_PPM' in col:
                return 3
            if 'Y_PPM' in col:
                return 2

    if file_format == 'PONDEROSA':
        if 'AXISORDER' in line:
            if all(a.isalpha() for a in col[1]):
                return len(col[1])

    if file_format == 'XwinNMR':
        if '# PEAKLIST_DIMENSION' in line:
            if '2' in col:
                return 2
            if '3' in col:
                return 3
            if '4' in col:
                return 4
        if 'F2[ppm]' in line:
            if 'F4[ppm]' in col:
                return 4
            if 'F3[ppm]' in col:
                return 3
            if 'F2[ppm]' in col:
                return 2

    if file_format == 'TopSpin':
        if '<PeakList2D>' in line:
            return 2
        if '<PeakList3D>' in line:
            return 3
        if '<PeakList4D>' in line:
            return 4

    if file_format == 'VNMR':
        if 'Dim 3' in line or 'A(ppm)' in line or 'A (ppm)' in line or 'F4' in line:
            return 4
        if 'Dim 2' in line or 'Z(ppm)' in line or 'Z (ppm)' in line or 'F3' in line:
            return 3
        if 'Dim 1' in line or 'Y(ppm)' in line or 'Y (ppm)' in line or 'F2' in line:
            return 2

        if len_col > 6 and SPARKY_ASSIGNMENT_PAT.match(col[6]):
            val = col[6]
            if 2 <= val.count('-') + 1 <= 4:
                return val.count('-')
            if 2 <= val.count(':') + 1 <= 4:
                return val.count(':')
            if 2 <= val.count(';') + 1 <= 4:
                return val.count(';')
            if 2 <= val.count(',') + 1 <= 4:
                return val.count(',')

        if len_col > 8 and SPARKY_ASSIGNMENT_PAT.match(col[8]):
            val = col[8]
            if 2 <= val.count('-') + 1 <= 4:
                return val.count('-')
            if 2 <= val.count(':') + 1 <= 4:
                return val.count(':')
            if 2 <= val.count(';') + 1 <= 4:
                return val.count(';')
            if 2 <= val.count(',') + 1 <= 4:
                return val.count(',')

        if len_col > 10 and SPARKY_ASSIGNMENT_PAT.match(col[10]):
            val = col[10]
            if 2 <= val.count('-') + 1 <= 4:
                return val.count('-')
            if 2 <= val.count(':') + 1 <= 4:
                return val.count(':')
            if 2 <= val.count(';') + 1 <= 4:
                return val.count(';')
            if 2 <= val.count(',') + 1 <= 4:
                return val.count(',')

    if file_format == 'unknown':
        if 'F4' in line or 'f4' in line or '4Dim' in line:
            return 4
        if 'F3' in line or 'f3' in line or '3Dim' in line:
            return 3
        if 'F2' in line or 'f2' in line or '2Dim' in line:
            return 2

    return None


def is_half_spin_nuclei(atom_type: str) -> bool:
    """ Return whether nuclei of a given atom_type has a spin 1/2.
        @return: True for spin 1/2 nuclei, False otherwise
    """

    return any(True for nucl in HALF_SPIN_NUCLEUS if atom_type.startswith(nucl))


def get_prompt_file_format(line: str
                           ) -> Optional[str]:
    """ Return prompt file type for a given input.
    """

    if 'X-PLOR>{====>}' in line:
        return 'X-PLOR NIH'

    if ('{===>}' in line and ';' in line) or 'CNSsolve>' in line:
        return 'CNS'

    return None


class NmrDpMrSplitter:
    """ File splitter for public PDB-MR formatted restraint file.
    """
    __slots__ = ('__class_name__',
                 '__version__',
                 '__reg',
                 '__cur_original_ar_file_name')

    def __init__(self, registry: NmrDpRegistry) -> None:
        self.__class_name__ = self.__class__.__name__
        self.__version__ = __version__

        self.__reg = registry

        self.__cur_original_ar_file_name: str = None

    def getNextPath(self, src_path: str, suffix: str = '~') -> str:
        """ Return candidate next file path.
        """
        return get_next_path(self.__reg, src_path, suffix)

    def testPathWithSuffix(self, src_path: str, suffix: str, defer_check: bool = False) -> str:
        """ Return basename(src_path) + suffix file path in either current workspace or default workspace if possible.
        """
        return test_path_with_suffix(self.__reg, src_path, suffix, defer_check)

    def testPath(self, src_path: str, defer_check: bool = False) -> str:
        """ Return basename(src_path) file in either current workspace or default workspace if possible.
        """
        if self.__reg.dirPath == self.__reg.spareDirPath or os.path.exists(src_path):
            return src_path

        chk_path = os.path.join(self.__reg.spareDirPath, os.path.basename(src_path))

        return chk_path if defer_check or os.path.exists(chk_path) else src_path

    def __report(self, code: str, file_name: str, description: str, warning: bool = False) -> None:
        """ Append a description to the report and echo it to the log in verbose mode.
        """

        if warning:
            self.__reg.report.warning.appendDescription(code, {'file_name': file_name, 'description': description})
        else:
            self.__reg.report.error.appendDescription(code, {'file_name': file_name, 'description': description})

        if self.__reg.verbose:
            self.__reg.log.write(f"+{self.__class_name__}.detectContentSubTypeOfLegacyMr() "
                                 f"++ {'Warning' if warning else 'Error'}  - {description}\n")

    def __suspendReport(self, code: str, file_name: str, description: str, warning: bool = False) -> None:
        """ Defer a description for lazy evaluation and echo it to the log in verbose mode.
        """

        holder = self.__reg.suspended_warnings_for_lazy_eval if warning else self.__reg.suspended_errors_for_lazy_eval
        holder.append({code: {'file_name': file_name, 'description': description}})

        if self.__reg.verbose:
            self.__reg.log.write(f"+{self.__class_name__}.detectContentSubTypeOfLegacyMr() "
                                 f"++ {'Warning' if warning else 'Error'}  - {description}\n")

    def __concatDetectedSubtypeNames(self, flags: MrContentFlags, incl_amb_inpcrd: bool = False,  # pylint: disable=no-self-use
                                     ) -> str:
        """ Return the "It looks like to have ... instead" clause for the detected content subtypes.
        """

        names = [label for attr, label in DETECTED_SUBTYPE_LABELS if getattr(flags, attr)]

        if incl_amb_inpcrd and flags.has_amb_inpcrd:
            names.append('AMBER restart coordinates (aka. .crd or .rst file)')

        return f". It looks like to have {', '.join(names)} instead" if len(names) > 0 else ''

    def __legacyMrAtomNames(self, file_type: str, cache: dict) -> MrAtomNames:
        """ Return the atom name sets the text scan of a given file type relies on.
            @param cache: memo shared by the input files of a single invocation, as
                          BmrbChemShiftStat.getAtomLikeNameSet() rebuilds its set on every call
        """

        minimum_len = 2 if file_type in ('nm-res-ari', 'nm-res-bar', 'nm-res-bio', 'nm-res-dyn',
                                         'nm-res-isd', 'nm-res-ros', 'nm-res-syb', 'nm-res-oth')\
            or file_type in AUX_TOP_FILE_TYPES else 1

        if minimum_len not in cache:
            atom_like = self.__reg.csStat.getAtomLikeNameSet(minimum_len=minimum_len)
            cache[minimum_len] = (atom_like, list(filter(is_half_spin_nuclei, atom_like)))  # DAOTHER-7491

        if 'oth' not in cache:
            atom_like_oth = self.__reg.csStat.getAtomLikeNameSet(1)
            cache['oth'] = (atom_like_oth, frozenset(filter(is_half_spin_nuclei, atom_like_oth)))  # DAOTHER-7491

        return MrAtomNames(*cache[minimum_len], *cache['oth'])

    def __scanXplorCnsMr(self, file_path: str, names: MrAtomNames, flags: MrContentFlags  # pylint: disable=no-self-use
                         ) -> None:
        """ Detect content subtypes of an XPLOR-NIH/CNS restraint file by scanning its text.
        """

        atom_like_names = names.atom_like
        cs_atom_like_names = frozenset(names.cs_atom_like)

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as ifh:

            atom_likes = atom_unlikes = cs_atom_likes = resid_likes = real_likes = 0
            _names, resids = [], []
            cs_range_like = dist_range_like = dihed_range_like = rdc_range_like = False

            rdc_atom_names = set()

            for line in ifh:

                flags.sniffCoordinateLine(line)

                _t_lower = ''

                for t in line.replace('(', ' ').replace(')', ' ').split():

                    if t[0] in COMMENT_CODE_MIXED_SET:
                        break

                    t_lower = t.lower()

                    if t_lower.startswith('assi') or (real_likes == 3 and t_lower.startswith('weight')):

                        if cs_atom_likes == 1 and resid_likes == 1 and cs_range_like:
                            flags.has_chem_shift = True

                        elif (atom_likes == 2 or (atom_likes > 0 and resid_likes == 2)) and dist_range_like:
                            flags.has_dist_restraint = True

                        elif atom_likes == 4 and dihed_range_like:
                            flags.has_dihed_restraint = True

                        elif cs_atom_likes + atom_unlikes == 6 and rdc_range_like:
                            flags.has_rdc_restraint = True

                        elif atom_likes == 3 and not (cs_range_like or dist_range_like or dihed_range_like
                                                      or rdc_range_like or flags.has_hbond_restraint)\
                                and _names[0][0] in HBOND_DA_ATOM_TYPES and _names[1][0] in PROTON_BEGIN_CODE\
                                and _names[2][0] in HBOND_DA_ATOM_TYPES:
                            flags.has_hbond_restraint = True

                        atom_likes = atom_unlikes = cs_atom_likes = resid_likes = real_likes = 0
                        _names, resids = [], []
                        cs_range_like = dist_range_like = dihed_range_like = rdc_range_like = False

                    elif _t_lower == 'name':
                        name = t.upper()
                        if name in atom_like_names:
                            if name not in _names or len(_names) > 1:
                                atom_likes += 1
                                _names.append(name)
                            if name in cs_atom_like_names:
                                cs_atom_likes += 1
                        else:
                            atom_unlikes += 1
                            if not flags.has_rdc_origins and name in RDC_ORIGIN_ATOM_NAMES:
                                rdc_atom_names.add(name)
                                if len(rdc_atom_names) == 4:
                                    flags.has_rdc_origins = True

                    elif _t_lower == 'resid':
                        try:
                            v = int(t)
                            if v not in resids:
                                resid_likes += 1
                                resids.append(v)
                        except ValueError:
                            pass

                    elif '.' in t:
                        try:
                            v = float(t)
                            if CS_RANGE_MIN <= v <= CS_RANGE_MAX:
                                cs_range_like = True
                            if DIST_RANGE_MIN <= v <= DIST_RANGE_MAX:
                                dist_range_like = True
                            if ANGLE_RANGE_MIN <= v <= ANGLE_RANGE_MAX:
                                dihed_range_like = True
                            if RDC_RANGE_MIN <= v <= RDC_RANGE_MAX:
                                rdc_range_like = True
                            real_likes += 1
                        except ValueError:
                            pass

                    _t_lower = t_lower

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as ifh:

            atom_likes = 0
            _names = []
            has_rest = has_plan = has_grou = has_sele = has_resi = False

            for line in ifh:

                _t_lower = ''

                for t in line.replace('(', ' ').replace(')', ' ').replace('=', ' ').split():

                    if t[0] in COMMENT_CODE_MIXED_SET:
                        break

                    t_lower = t.lower()

                    if t_lower.startswith('rest'):
                        has_rest = True

                    elif t_lower.startswith('plan'):
                        has_plan = True

                    elif has_rest and has_plan:

                        if t_lower.startswith('grou'):
                            has_grou = True

                        elif t_lower.startswith('sele'):
                            has_sele = True

                            atom_likes = 0
                            _names = []

                        elif _t_lower == 'name':
                            name = t.upper()
                            if name in atom_like_names:
                                if name not in _names or len(_names) > 1:
                                    atom_likes += 1
                                    _names.append(name)

                        elif t_lower.startswith('resi'):
                            has_resi = True

                        elif has_grou and has_sele and has_resi and not flags.has_plane_restraint\
                                and _t_lower.startswith('weig'):
                            if atom_likes > 0:
                                try:
                                    v = float(t)
                                    if WEIGHT_RANGE_MIN <= v <= WEIGHT_RANGE_MAX:
                                        flags.has_plane_restraint = True
                                except ValueError:
                                    pass

                        elif t_lower == 'end':
                            has_grou = has_sele = has_resi = False

                    _t_lower = t_lower

                if flags.has_plane_restraint:
                    break  # this pass sets no other indicator, so nothing can change any more

    def __scanAmberMr(self, file_path: str, flags: MrContentFlags) -> None:  # pylint: disable=no-self-use
        """ Detect content subtypes of an AMBER restraint file by scanning its text.
        """

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as ifh:
            in_rst = in_iat = in_igr1 = in_igr2 =\
                dist_range_like = dihed_range_like = rdc_range_like = False

            names, values = [], []

            pos = 0

            for line in ifh:

                flags.sniffCoordinateLine(line)

                pos += 1

                if pos == 1 and not line.isdigit():
                    flags.has_amb_inpcrd = True

                elif pos == 2 and flags.has_amb_inpcrd:
                    try:
                        int(line.lstrip().split()[0])
                    except (ValueError, IndexError):
                        flags.has_amb_inpcrd = False

                elif pos == 3 and flags.has_amb_inpcrd:
                    if line.count('.') != 6:
                        flags.has_amb_inpcrd = False

                if '&rst ' in line:
                    line = line.replace('&rst ', '&rst,')

                elif '&end' in line:
                    line = line.replace('&end', ',&end')

                elif '/' in line:
                    line = line.replace('/', ',&end')

                _line = ' '.join(line.split())

                if len(_line) == 0 or _line[0] in COMMENT_CODE_MIXED_SET:
                    continue

                for t in WS_PAT.sub('', _line).lower().split(','):

                    if len(t) == 0:
                        continue

                    if t[0] in COMMENT_CODE_MIXED_SET:
                        break

                    if t == '&rst':
                        in_rst = True

                    elif in_rst:

                        if t == '&end':

                            atom_likes = atom_unlikes = 0

                            for name in names:

                                if isinstance(name, int):
                                    if name != -1:
                                        atom_likes += 1
                                    else:
                                        atom_unlikes += 1

                                if isinstance(name, list):

                                    if any(True for n in name if n != -1):
                                        atom_likes += 1
                                    else:
                                        atom_unlikes += 1

                            if len(values) == 4:
                                v = (values[1] + values[2]) / 2.0

                                if DIST_RANGE_MIN <= v <= DIST_RANGE_MAX:
                                    dist_range_like = True
                                if ANGLE_RANGE_MIN <= v <= ANGLE_RANGE_MAX:
                                    dihed_range_like = True
                                if RDC_RANGE_MIN <= v <= RDC_RANGE_MAX:
                                    rdc_range_like = True

                                if atom_likes == 2 and dist_range_like:
                                    flags.has_dist_restraint = True

                                elif atom_likes == 4 and dihed_range_like:
                                    flags.has_dihed_restraint = True

                                elif atom_likes + atom_unlikes == 6 and rdc_range_like:
                                    flags.has_rdc_restraint = True

                            names, values = [], []

                            in_rst = in_iat = in_igr1 = in_igr2 = False

                        elif t.startswith('iat='):
                            in_iat = True
                            try:
                                iat = int(t[4:])
                                names.append(iat)
                            except ValueError:
                                pass

                            in_igr1 = in_igr2 = False

                        elif '=' not in t and in_iat:
                            try:
                                iat = int(t)
                                names.append(iat)
                            except ValueError:
                                pass

                        elif AMBER_R_PAT.match(t):
                            len_values = len(values)
                            g = AMBER_R_PAT.match(t).groups()
                            try:
                                r_idx = int(g[0]) - 1
                                v = float(g[1])
                                if len_values == r_idx:
                                    values.append(v)
                                elif len_values > r_idx:
                                    values.insert(r_idx, v)
                                else:
                                    while len(values) < r_idx:
                                        values.append(None)
                                    values.append(v)
                            except ValueError:
                                pass

                            in_iat = in_igr1 = in_igr2 = False

                        elif t.startswith('igr1'):
                            in_igr1 = True
                            try:
                                iat = int(t[5:])
                                names.insert(0, [iat])
                            except ValueError:
                                pass

                            in_iat = in_igr2 = False

                        elif '=' not in t and in_igr1:
                            try:
                                iat = int(t)
                                g = names[0]
                                g.append(iat)
                            except ValueError:
                                pass

                        elif t.startswith('igr2'):
                            in_igr2 = True
                            try:
                                iat = int(t[5:])
                                names.insert(1, [iat])
                            except ValueError:
                                pass

                            in_iat = in_igr1 = False

                        elif '=' not in t and in_igr2:
                            try:
                                iat = int(t)
                                g = names[1]
                                g.append(iat)
                            except ValueError:
                                pass

                        elif '=' in t:
                            in_iat = in_igr1 = in_igr2 = False

    def __classifyLightMrCounts(self, cs_atom_likes: int, atom_likes: int, res_like: bool,  # pylint: disable=no-self-use
                                angle_like: bool, cs_range_like: bool, dist_range_like: bool, dihed_range_like: bool,
                                flags: MrContentFlags) -> None:
        """ Record the content subtype implied by the token counts of a single line.
            Restraints are tested before chemical shifts: a restraint line can have exactly one chemical shift-like
            atom name, e.g. 'assign (resid 23 and name O) (resid 27 and name HN) 1.9 0.1 0.1', and its distances
            and angles lie in CS_RANGE, whereas a chemical shift line normally names a single atom, so it does not
            match the restraint arms. Over 265 files of tests-nmr as 'nm-res-oth', testing chemical shifts first lost
            the distance restraints of 8 files and the dihedral angle restraints of 45 (DAOTHER-7829).
        """

        if atom_likes == 2 and dist_range_like:
            flags.has_dist_restraint = True

        elif (atom_likes == 4 or (res_like and angle_like)) and dihed_range_like:
            flags.has_dihed_restraint = True

        elif cs_atom_likes == 1 and cs_range_like:
            flags.has_chem_shift = True

    def __scanLightMrAndAuxTop(self, file_path: str, file_type: str, names: MrAtomNames,
                               flags: MrContentFlags) -> None:
        """ Detect content subtypes of a light-weight restraint file or of an auxiliary topology
            file by scanning its text.
        """

        atom_like_names = names.atom_like
        cs_atom_like_names = names.cs_atom_like
        atom_like_names_oth = names.atom_like_oth
        cs_atom_like_names_oth = names.cs_atom_like_oth

        scanner = AUX_TOP_SCANNERS[file_type](atom_like_names_oth) if file_type in AUX_TOP_SCANNERS else None

        prohibited_col = set()

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as ifh:

            for pos, line in enumerate(ifh, start=1):

                sniffed = flags.sniffCoordinateLine(line)

                if sniffed == 'atom':
                    if file_type == 'nm-aux-amb':
                        flags.has_amb_coord = True

                elif sniffed is None and scanner is not None and scanner.feed(line, pos, flags):
                    continue

                _line = ' '.join(line.split())

                if len(_line) == 0 or _line[0] in COMMENT_CODE_SEMICOLON_SET:
                    continue

                s = PAREN_SPLIT_PAT.split(_line)

                atom_likes = cs_atom_likes = 0
                _names = []
                res_like = angle_like = cs_range_like = dist_range_like = dihed_range_like = False

                first_col = None

                for t in s:

                    if len(t) == 0:
                        continue

                    if t[0] in COMMENT_CODE_SEMICOLON_SET:
                        break

                    name = t.upper()

                    if name in atom_like_names:
                        if name not in _names or len(_names) > 1:
                            atom_likes += 1
                            _names.append(name)
                        if name in cs_atom_like_names:
                            cs_atom_likes += 1

                    elif name in STD_MON_ONE_LETTER_CODES and name not in atom_like_names_oth:
                        if first_col is None:
                            first_col = first_index_map(s)
                        prohibited_col.add(first_col[t])

                    elif '.' in t:
                        try:
                            v = float(t)
                            if CS_RANGE_MIN <= v <= CS_RANGE_MAX:
                                cs_range_like = True
                            if DIST_RANGE_MIN <= v <= DIST_RANGE_MAX:
                                dist_range_like = True
                            if ANGLE_RANGE_MIN <= v <= ANGLE_RANGE_MAX:
                                dihed_range_like = True
                        except ValueError:
                            pass

                    elif name in STD_MON_DICT:
                        res_like = True

                    elif name in KNOWN_ANGLE_NAMES:
                        angle_like = True

                self.__classifyLightMrCounts(cs_atom_likes, atom_likes, res_like, angle_like,
                                             cs_range_like, dist_range_like, dihed_range_like, flags)

        if file_type == 'nm-res-oth' and flags.has_chem_shift\
           and not flags.has_dist_restraint and not flags.has_dihed_restraint:

            with open(file_path, 'r', encoding='utf-8', errors='ignore') as ifh:

                for line in ifh:

                    _line = ' '.join(line.split())

                    if len(_line) == 0 or _line[0] in COMMENT_CODE_MIXED_SET:
                        continue

                    s = PAREN_SPLIT_PAT.split(_line)

                    atom_likes = cs_atom_likes = 0
                    _names = []
                    res_like = angle_like = cs_range_like = dist_range_like = dihed_range_like = False

                    first_col = first_index_map(s)

                    for t in s:

                        if len(t) == 0:
                            continue

                        if t[0] in COMMENT_CODE_MIXED_SET:
                            break

                        if first_col[t] in prohibited_col:
                            continue

                        name = t.upper()

                        if name in atom_like_names_oth:
                            if name not in _names or len(_names) > 1:
                                atom_likes += 1
                                _names.append(name)
                            if name in cs_atom_like_names_oth:
                                cs_atom_likes += 1

                        elif '.' in t:
                            try:
                                v = float(t)
                                if CS_RANGE_MIN <= v <= CS_RANGE_MAX:
                                    cs_range_like = True
                                if DIST_RANGE_MIN <= v <= DIST_RANGE_MAX:
                                    dist_range_like = True
                                if ANGLE_RANGE_MIN <= v <= ANGLE_RANGE_MAX:
                                    dihed_range_like = True
                            except ValueError:
                                pass

                        elif name in STD_MON_DICT:
                            res_like = True

                        elif name in KNOWN_ANGLE_NAMES:
                            angle_like = True

                    self.__classifyLightMrCounts(cs_atom_likes, atom_likes, res_like, angle_like,
                                                 cs_range_like, dist_range_like, dihed_range_like, flags)

        if file_type == 'nm-res-oth':

            flags.has_spectral_peak = get_peak_list_format(file_path) is not None

            with open(file_path, 'r', encoding='utf-8', errors='ignore') as ifh:
                for pos, line in enumerate(ifh, start=1):
                    if pos == 1:
                        if 'Structures from CYANA' not in line:
                            break
                    elif pos == 2:
                        if 'CYANA' not in line:
                            break
                    elif pos == 3:
                        if line.count('Number') < 3:
                            break
                    elif pos == 4:
                        if line.count('.') >= 3:
                            flags.has_coordinate = True
                        break

            with open(file_path, 'r', encoding='utf-8', errors='ignore') as ifh:
                for pos, line in enumerate(ifh, start=1):
                    if pos == 1:
                        if line.isdigit():
                            break
                    elif pos == 2:
                        try:
                            int(line.lstrip().split()[0])
                        except (ValueError, IndexError):
                            break
                    elif pos == 3:
                        if line.count('.') == 6:
                            flags.has_coordinate = True
                        break

        if scanner is not None:

            flags.has_topology = scanner.isTopology()

            if file_type == 'nm-aux-amb' and flags.has_amb_coord\
               and (not flags.has_first_atom or flags.has_ens_coord):
                flags.has_amb_coord = False

    def __scanLightMrDistFallback(self, file_path: str, names: MrAtomNames, flags: MrContentFlags) -> None:
        """ Sniff a light-weight restraint file for a plain '{seq} {comp} {atom}' distance restraint
            layout that the token-count heuristics above do not recognize (DAOTHER-7491).
        """

        atom_like_names = names.atom_like

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as ifh:

            for line in ifh:

                _line = ' '.join(line.split())

                if len(_line) == 0 or _line[0] in COMMENT_CODE_MIXED_SET:
                    continue

                s = PAREN_SPLIT_PAT.split(_line)

                if len(s) < 7:
                    continue

                try:
                    int(s[0])
                    int(s[3])
                    v = float(s[6])
                    if v < DIST_RANGE_MIN or DIST_RANGE_MAX < v:
                        continue
                except ValueError:
                    continue

                if s[1].isalnum():
                    comp_id = s[1].upper()
                    atom_id = s[2].upper()

                    if comp_id in STD_MON_DICT:
                        if atom_id not in atom_like_names:
                            continue

                    elif len(comp_id) > 3:
                        continue

                    elif not self.__reg.ccU.updateChemCompDict(comp_id):
                        continue

                if s[4].isalnum():
                    comp_id = s[4].upper()
                    atom_id = s[5].upper()

                    if comp_id in STD_MON_DICT:
                        if atom_id not in atom_like_names:
                            continue

                    elif len(comp_id) > 3:
                        continue

                    elif not self.__reg.ccU.updateChemCompDict(comp_id):
                        continue

                flags.has_dist_restraint = True

                break

    def __detectPromptDumpFile(self, file_path: str, file_type: str, file_name: str,
                               mr_format_name: str) -> bool:
        """ Report a restraint file that is binary, or that is a dump of an interactive prompt.
            @return: whether the file is still worth parsing
        """

        prompt_type = None
        valid = True

        try:

            with open(file_path, 'r', encoding='utf-8') as ifh:
                for idx, line in enumerate(ifh):
                    if line.isspace():
                        continue
                    prompt_type = get_prompt_file_format(line)
                    if prompt_type is not None:
                        break
                    if idx >= MR_MAX_SPACER_LINES:
                        break

        except UnicodeDecodeError as e:  # catch exception due to binary format (DAOTHER-9425)

            if file_type != 'nm-aux-pdb':

                self.__report('format_issue', file_name,
                              f"The {mr_format_name} restraint file {file_name!r} is not a plain text file. {str(e)}")

                valid = False

        if prompt_type is not None:

            self.__report('format_issue', file_name,
                          f"The {mr_format_name} restraint file {file_name!r} appears to be {prompt_type} "
                          "prompt message dump file. Did you accidentally upload the wrong file? "
                          f"Please re-upload valid {mr_format_name} restraint file(s) "
                          "used for the structure determination.")

            valid = False

        return valid

    def __useSllPrediction(self, file_path: str, file_type: str) -> bool:
        """ Return whether to use the ANTLR SLL prediction mode, which is a performance gain when
            restraints have a deep but simple atom selection (DAOTHER-10315).
        """

        sll_pred = False
        if file_path in self.__reg.sll_pred_holder and file_type in self.__reg.sll_pred_holder[file_path]:
            sll_pred = self.__reg.sll_pred_holder[file_path][file_type]

        if file_type not in ('nm-res-xpl', 'nm-res-cns', 'nm-res-cha'):
            return sll_pred

        has_deep_l_pattern = False

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as ifh:
            for idx, line in enumerate(ifh):
                if DEEP_L_PARENS_PAT.match(line):
                    has_deep_l_pattern = True
                if has_deep_l_pattern and DEEP_R_PARENS_PAT.match(line):
                    self.__reg.sll_pred_forced.append(file_path)
                    sll_pred = True
                    break
                if idx >= 40:
                    break

        return sll_pred

    def __parseLegacyMrWithAntlr(self, ar: dict, file_path: str, file_type: str, file_name: str,
                                 a_mr_format_name: str, valid: bool, remediation_loop_count: int,
                                 flags: MrContentFlags) -> Tuple[Optional[dict], bool, bool]:
        """ Parse a legacy restraint file with its format reader and report any syntax or data issue.
            @return: (content subtype, whether the file is valid, whether the file has been rewritten)
        """

        content_subtype = None
        corrected = div_test = False

        try:

            if file_type in PARSABLE_MR_FILE_TYPES and valid:

                file_path = self.testPathWithSuffix(file_path, '-corrected')

                sll_pred = self.__useSllPrediction(file_path, file_type)

                reader = self.getSimpleFileReader(file_type, self.__reg.verbose, sll_pred=sll_pred)

                listener, parser_err_listener, lexer_err_listener = reader.parse(file_path, None)

                if listener is not None and file_type in RETRIAL_MR_FILE_TYPES:
                    reasons = listener.getReasonsForReparsing()

                    if reasons is not None:
                        reader = self.getSimpleFileReader(file_type, self.__reg.verbose, sll_pred=sll_pred, reasons=reasons)

                        listener, parser_err_listener, lexer_err_listener = reader.parse(file_path, None)

                err = ''
                err_lines = []

                has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
                has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None

                content_subtype = listener.getContentSubtype() if listener is not None else None
                if content_subtype is not None and len(content_subtype) == 0:
                    content_subtype = None
                elif file_type in AUX_TOP_FILE_TYPES:
                    flags.has_topology = True
                    content_subtype = {'topology': 1}

                has_content = content_subtype is not None

                if has_lexer_error and has_parser_error and has_content:
                    # parser error occurs before occurrence of lexer error that implies mixing of different MR formats in a file
                    if lexer_err_listener.getErrorLineNumber()[0] > parser_err_listener.getErrorLineNumber()[0]:
                        corrected |= self.__stripLegacyMrIfNecessary(file_path, file_type,
                                                                     parser_err_listener.getMessageList()[0],
                                                                     str(file_path), 0)
                        div_test = True

                fixed_line_num = -1

                if has_lexer_error:
                    messageList = lexer_err_listener.getMessageList()

                    for description in messageList:
                        err_lines.append(description['line_number'])
                        err += f"[Syntax error] line {description['line_number']}:{description['column_position']} "\
                            f"{description['message']}\n"
                        if 'input' in description:
                            enc = detect_encoding(description['input'])
                            is_not_ascii = False
                            if enc is not None and enc != 'ascii':
                                err += f"{description['input']}\n".encode().decode('ascii', 'backslashreplace')
                                is_not_ascii = True
                            else:
                                err += f"{description['input']}\n"
                            err += f"{description['marker']}\n"
                            if is_not_ascii:
                                err += f"[Unexpected text encoding] Encoding used in the above line is {enc!r} "\
                                    "and must be 'ascii'.\n"
                            elif not div_test and has_content and self.__reg.remediation_mode:
                                fixed = self.__divideLegacyMrIfNecessary(file_path, file_type, description, str(file_path), 0)
                                corrected |= fixed
                                if fixed:
                                    fixed_line_num = description['line_number']
                                div_test = file_type != 'nm-res-amb'  # remediate missing comma issue in AMBER MR

                if has_parser_error:
                    total_line = -1
                    if os.path.exists(file_path):
                        with open(file_path, 'r', encoding='utf-8', errors='replace') as ifh:
                            total_line = sum(1 for _ in ifh)

                    messageList = parser_err_listener.getMessageList()

                    for description in messageList:
                        # ignore noeol error for linear mr file formats
                        if description['line_number'] == total_line and file_type in LINEAR_MR_FILE_TYPES:
                            continue
                        err_lines.append(description['line_number'])
                        err += f"[Syntax error] line {description['line_number']}:{description['column_position']} "\
                            f"{description['message']}\n"
                        len_err = len(err)
                        if 0 < fixed_line_num <= description['line_number']:
                            div_test = True
                        if 'input' in description:
                            err += f"{description['input']}\n"
                            err += f"{description['marker']}\n"
                            if not div_test and has_content and self.__reg.remediation_mode:
                                corrected |=\
                                    self.__divideLegacyMrIfNecessary(file_path, file_type, description, str(file_path), 0)
                                div_test = True
                        elif not div_test and has_content and self.__reg.remediation_mode:
                            corrected |= self.__divideLegacyMrIfNecessary(file_path, file_type, description, str(file_path), 0)
                            div_test = True

                        _err = next((_description.get('previous_input') for _description in self.__reg.divide_mr_error_message
                                     if _description['file_path'] == description['file_path']
                                     and _description['line_number'] == description['line_number']
                                     and _description['message'] == description['message']), None)

                        if _err is not None and not COMMENT_PAT.match(_err) and not _err.isspace():
                            s = '. ' if _err.startswith('Do you') else ':\n'
                            err = err[:len_err] +\
                                ("However, the error may be due to missing statement "
                                 "(e.g. 'noe', 'restraint dihedral', 'sanisotropy') "
                                 f"at the beginning of {_err.strip().split(' ')[0]!r} "
                                 "and note that the statement should be ended with 'end' tag "
                                 if _err.lower().strip().startswith('class')
                                 else "However, the error may be due to the previous input ") +\
                                f"(line {description['line_number']-1}){s}{_err}" + err[len_err:]

                if len(err) > 0:
                    valid = False

                    err = f"Could not interpret {file_name!r} as {a_mr_format_name} file:\n{err[0:-1]}"

                    ar['format_mismatch'], _err, _, _ =\
                        self.__detectOtherPossibleFormatAsErrorOfLegacyMr(file_path, file_name, file_type, err_lines)

                    if ar['format_mismatch']:
                        err += '\n' + _err

                    self.__reg.report.error.appendDescription('format_issue',
                                                              {'file_name': file_name, 'description': err})

                    if not self.__reg.remediation_mode or remediation_loop_count > 0:
                        self.__reg.log.write(f"+{self.__class_name__}.detectContentSubTypeOfLegacyMr() ++ Error  - "
                                             f"{file_type} {file_name} {err}\n")

                    flags.has_dist_restraint = flags.has_dihed_restraint = flags.has_rdc_restraint = False

                elif listener is not None:

                    if listener.warningMessage is not None:

                        messages = [msg for msg in listener.warningMessage
                                    if 'warning' not in msg and 'Unsupported' not in msg
                                    and 'Redundant' not in msg
                                    and ((self.__reg.remediation_mode and 'Range value error' not in msg)
                                         or not self.__reg.remediation_mode)]

                        if len(messages) > 0:
                            valid = False

                            if len(messages) > 5:
                                messages = messages[:5]
                                msg = '\n'.join(messages)
                                msg += '\nThose similar errors may continue...'
                            else:
                                msg = '\n'.join(messages)
                            err = f"Could not interpret {file_name!r} due to the following data issue(s):\n{msg}"

                            self.__reg.report.error.appendDescription('format_issue',
                                                                      {'file_name': file_name, 'description': err})

                            if not self.__reg.remediation_mode or remediation_loop_count > 0:
                                self.__reg.log.write(f"+{self.__class_name__}.detectContentSubTypeOfLegacyMr() ++ Error  - "
                                                     f"{file_type} {file_name} {err}\n")

                    if valid:

                        flags.has_chem_shift = flags.has_coordinate = False

                        if content_subtype is not None:
                            flags.has_dist_restraint = 'dist_restraint' in content_subtype
                            flags.has_dihed_restraint = 'dihed_restraint' in content_subtype
                            flags.has_rdc_restraint = 'rdc_restraint' in content_subtype
                            flags.has_plane_restraint = 'plane_restraint' in content_subtype
                            flags.has_hbond_restraint = 'hbond_restraint' in content_subtype
                            flags.has_ssbond_restraint = 'ssbond_restraint' in content_subtype

                            if file_type == 'nm-res-cya' and flags.has_dist_restraint:
                                ar['dist_type'] = listener.getTypeOfDistanceRestraints()
                            if file_type == 'nm-res-amb':
                                ar['has_comments'] = listener.hasComments()

                            ar['is_valid'] = True

            elif file_type == 'nm-res-oth':
                if not (self.__reg.remediation_mode and file_path.endswith('-div_ext.mr')):
                    ar['format_mismatch'], _, _, _ =\
                        self.__detectOtherPossibleFormatAsErrorOfLegacyMr(file_path, file_name, file_type, [])

        except ValueError as e:

            self.__reg.report.error.appendDescription('internal_error',
                                                      f"+{self.__class_name__}.detectContentSubTypeOfLegacyMr() "
                                                      "++ Error  - " + str(e))

            if self.__reg.verbose:
                self.__reg.log.write(f"+{self.__class_name__}.detectContentSubTypeOfLegacyMr() ++ Error  - {str(e)}\n")

        return content_subtype, valid, corrected

    def __reportContentMismatch(self, file_type: str, file_name: str, mr_format_name: str,
                                valid: bool, flags: MrContentFlags) -> None:
        """ Report content that does not belong in a restraint or topology file of the given format.
        """

        kind = 'topology' if file_type in AUX_TOP_FILE_TYPES else 'restraint'

        if flags.has_coordinate and not flags.hasAnyRestraint():

            self.__report('content_mismatch', file_name,
                          f"The {mr_format_name} {kind} file includes coordinates. "
                          "Did you accidentally select wrong format? Please re-upload the restraint file.")

            flags.has_chem_shift = False

        elif flags.has_chem_shift and not flags.has_coordinate and not flags.has_amb_inpcrd\
                and not flags.hasAnyRestraint():

            if flags.has_rdc_origins:

                hint = 'assign ( resid # and name OO ) ( resid # and name X ) ( resid # and name Y ) ( resid # and name Z ) "\
                    "( segid $ and resid # and name $ ) ( segid $ and resid # and name $ ) #.# #.#'

                self.__report('content_mismatch', file_name,
                              f"The restraint file {file_name!r} may be a malformed XPLOR-NIH RDC restraint file. "
                              f"Tips for XPLOR-NIH RDC restraints: {hint!r} pattern must be present in the file. "
                              "Did you accidentally select wrong format? Please re-upload the restraint file.")

                flags.has_chem_shift = False

            elif valid:

                self.__report('content_mismatch', file_name,
                              f"The {mr_format_name} {kind} file includes assigned chemical shifts. "
                              "Did you accidentally select wrong format? Please re-upload the restraint file.")

        elif flags.has_chem_shift:
            flags.has_chem_shift = False

        if flags.has_spectral_peak:

            self.__report('content_mismatch', file_name,
                          f"The {mr_format_name} restraint file includes spectral peak list. "
                          "Did you accidentally select wrong format? "
                          "Please re-upload the file as spectral peak list file.")

    def __reportUnidentifiedContent(self, file_type: str, file_name: str, mr_format_name: str,
                                    content_subtype: dict, valid: bool, flags: MrContentFlags) -> None:
        """ Report a restraint file whose content subtype could not be identified, or an auxiliary
            file in which no molecular topology could be found.
        """

        if file_type not in AUX_TOP_FILE_TYPES and not flags.has_chem_shift\
           and not flags.hasAnyRestraint() and not valid:

            hint = ''
            if len(concat_restraint_names(content_subtype)) == 0:
                if file_type in ('nm-res-xpl', 'nm-res-cns') and not flags.has_rdc_origins:
                    hint = 'assign ( segid $ and resid # and name $ ) ( segid $ and resid # and name $ ) #.# #.# #.#'
                elif file_type == 'nm-res-amb':
                    hint = '&rst iat=#[,#], r1=#.#, r2=#.#, r3=#.#, r4=#.#, [igr1=#[,#],] [igr2=#[,#],] &end'

            if len(hint) > 0:
                hint = f" Tips for {mr_format_name} restraints: {hint!r} pattern must be present in the file."

            self.__report('missing_content', file_name,
                          f"Constraint type of the restraint file ({mr_format_name}) could not be identified."
                          f"{hint} Did you accidentally select wrong format?", warning=True)

        elif file_type == 'nm-aux-amb' and not flags.has_amb_coord and not flags.has_topology:

            hint = " Tips for AMBER topology: Proper contents starting with '%FLAG ATOM_NAME', '%FLAG RESIDUE_LABEL', "\
                "'%FLAG RESIDUE_POINTER', and '%FLAG AMBER_ATOM_TYPE' lines must be present in the file."

            if flags.has_coordinate:
                hint = " Tips for AMBER coordinates: It should be directory generated by 'ambpdb' command "\
                    "and must not have MODEL/ENDMDL keywords to ensure that AMBER atomic IDs, "\
                    "referred as 'iat' in the AMBER restraint file, are preserved in the file."

            self.__report('content_mismatch', file_name,
                          f"{file_name!r} is neither AMBER topology (.prmtop) nor coordinates (.inpcrd.pdb)"
                          f"{self.__concatDetectedSubtypeNames(flags, incl_amb_inpcrd=True)}."
                          f"{hint} Did you accidentally select wrong format? "
                          "Please re-upload the AMBER topology file.")

        elif file_type == 'nm-aux-cha' and not flags.has_topology:

            hint = " Tips for CHARMM topology: '{Number of atoms} EXT' header line must be present in the file. "\
                "Then, it is followed by '{atom_number} {label_seq_id} {label_comp_id} {label_atom_id} "\
                "{Cartn_x} {Cartn_y} {Cartn_z} {segment_id} {auth_seq_id} {B_iso_or_equiv}' lines."

            self.__report('content_mismatch', file_name,
                          f"{file_name!r} is not CHARMM topology (aka. CRD or CHARM CARD file) "
                          f"{self.__concatDetectedSubtypeNames(flags)}."
                          f"{hint} Did you accidentally select wrong format? "
                          "Please re-upload the CHARMM topology file.")

        elif file_type == 'nm-aux-gro' and not flags.has_topology:

            hint = " Tips for GROMACS topology: Proper contents starting with '[ system ]', '[ molecules ]', "\
                "and '[ atoms ]' lines must be present in the file."

            self.__report('content_mismatch', file_name,
                          f"{file_name!r} is not GROMACS topology "
                          f"{self.__concatDetectedSubtypeNames(flags)}."
                          f"{hint} Did you accidentally select wrong format? "
                          "Please re-upload the GROMACS topology file.")

    def __checkMandatoryDistRestraint(self) -> None:
        """ Report the absence of distance restraints across the whole set of uploaded restraint files.
        """

        fileListId = self.__reg.file_path_list_len

        for _ in self.__reg.inputParamDict[AR_FILE_PATH_LIST_KEY]:

            input_source_dic = self.__reg.report.input_sources[fileListId].get()

            file_name = input_source_dic['file_name']
            file_type = input_source_dic['file_type']
            content_subtype = input_source_dic['content_subtype']

            fileListId += 1

            if file_type in ('nmr-star', 'nm-res-mr', 'nm-res-bar', 'nm-res-oth', 'nm-res-sax')\
               or file_type.startswith('nm-pea'):
                continue

            if (content_subtype is not None and 'dist_restraint' in content_subtype)\
               or file_type in AUX_TOP_FILE_TYPES:
                continue

            if content_subtype is None:

                if self.__reg.permit_missing_legacy_dist_restraint:
                    self.__suspendReport('content_mismatch', file_name,
                                         f"The restraint file is not recognized properly {file_type}. "
                                         "Please fix the file so that it conforms to the format specifications.")

                else:
                    self.__suspendReport('content_mismatch', file_name,
                                         "The restraint file is not recognized properly so that there is no mandatory "
                                         "distance restraints in the set of uploaded restraint files. "
                                         "Please re-upload the restraint file.")

            elif 'chem_shift' not in content_subtype and not self.__reg.remediation_mode:

                if self.__reg.permit_missing_legacy_dist_restraint:
                    self.__suspendReport('missing_content', file_name,
                                         f"The restraint file includes {concat_restraint_names(content_subtype)}. "
                                         "However, distance restraints are missing in the set of uploaded restraint file(s). "
                                         "The wwPDB NMR Validation Task Force highly recommends the submission of "
                                         "distance restraints used for the structure determination.", warning=True)

                else:
                    self.__suspendReport('content_mismatch', file_name,
                                         f"The restraint file includes {concat_restraint_names(content_subtype)}. "
                                         "However, deposition of distance restraints is mandatory. "
                                         "Please re-upload the restraint file.")

    def __detectDuplicateMrUpload(self, md5_list: List[Optional[str]]) -> None:
        """ Report restraint/spectral peak list files that have been uploaded more than once.
        """

        if len(set(md5_list)) == len(md5_list):
            return

        ar_list = self.__reg.inputParamDict[AR_FILE_PATH_LIST_KEY]

        for (i, j) in itertools.combinations(range(0, len(ar_list)), 2):

            if None in (md5_list[i], md5_list[j]) or md5_list[i] != md5_list[j]:
                continue

            file_name_1 = os.path.basename(ar_list[i]['file_name'])
            file_name_2 = os.path.basename(ar_list[j]['file_name'])

            file_type_1 = ar_list[i]['file_type']
            file_type_2 = ar_list[j]['file_type']

            if file_type_1.startswith('nm-res') and file_type_2.startswith('nm-res'):
                file_type = 'restraint'
            elif file_type_1.startswith('nm-pea') and file_type_2.startswith('nm-pea'):
                file_type = 'spectral peak list'
            elif file_type_1.startswith('nm-res'):
                file_type = 'restraint/spectral peak list'
            else:
                file_type = 'spectral peak list/restraint'

            if self.__reg.internal_mode:
                if os.path.exists(self.testPathWithSuffix(ar_list[j]['file_name'], '-ignored', True)):
                    continue
                if '-selected-as-' in file_name_1 or '-selected-as-' in file_name_2:
                    continue
                if re.search(r'\/bmr\d+\/work\/data\/', file_name_1) or re.search(r'\/bmr\d+\/work\/data\/', file_name_2):
                    continue

            self.__report('content_mismatch', f"{file_name_1} vs {file_name_2}",
                          f"You have uploaded the same NMR {file_type} file twice. "
                          f"Please replace/delete either {file_name_1} or {file_name_2}.")

            if self.__reg.remediation_mode:
                file_path_2 = ar_list[j]['file_name']
                os.symlink(file_path_2, self.testPath(file_path_2 + '-ignored', True))

    def detectContentSubTypeOfLegacyMr(self, remediation_loop_count: int) -> bool:
        """ Detect content subtype of legacy restraint files.
        """

        corrected = False

        md5_list = []
        name_set_cache = {}

        fileListId = self.__reg.file_path_list_len

        for ar in self.__reg.inputParamDict[AR_FILE_PATH_LIST_KEY]:
            file_path = ar['file_name']

            input_source = self.__reg.report.input_sources[fileListId]
            input_source_dic = input_source.get()

            file_name = input_source_dic['file_name']
            file_type = input_source_dic['file_type']

            fileListId += 1
            if file_type is None or file_type in ('nm-res-mr', 'nm-res-sax') or file_type.startswith('nm-pea'):
                md5_list.append(None if file_type == 'nm-res-mr' else file_md5(file_path))
                continue

            original_file_name = None
            if 'original_file_name' in input_source_dic:
                if input_source_dic['original_file_name'] is not None:
                    original_file_name = os.path.basename(input_source_dic['original_file_name'])
                if file_name != original_file_name and original_file_name is not None:
                    file_name = f"{original_file_name} ({file_name})"

            md5_list.append(file_md5(file_path))

            _mr_format_name = getRestraintFormatName(file_type)
            mr_format_name = _mr_format_name.split()[0]
            a_mr_format_name = ('an ' if mr_format_name[0] in ('AINMX') else 'a ') + _mr_format_name

            names = self.__legacyMrAtomNames(file_type, name_set_cache)

            flags = MrContentFlags()

            if file_type in ('nm-res-xpl', 'nm-res-cns'):
                self.__scanXplorCnsMr(file_path, names, flags)

            elif file_type == 'nm-res-amb':
                self.__scanAmberMr(file_path, flags)

            elif file_type in LIGHT_MR_FILE_TYPES or file_type in AUX_TOP_FILE_TYPES:
                self.__scanLightMrAndAuxTop(file_path, file_type, names, flags)

            if file_type in LIGHT_MR_FILE_TYPES and not flags.has_dist_restraint:  # DAOTHER-7491
                self.__scanLightMrDistFallback(file_path, names, flags)

            valid = self.__detectPromptDumpFile(file_path, file_type, file_name, mr_format_name)

            content_subtype, valid, fixed =\
                self.__parseLegacyMrWithAntlr(ar, file_path, file_type, file_name, a_mr_format_name,
                                              valid, remediation_loop_count, flags)
            corrected |= fixed

            self.__reportContentMismatch(file_type, file_name, mr_format_name, valid, flags)

            if content_subtype is None:
                content_subtype = {'chem_shift': 1 if flags.has_chem_shift else 0,
                                   'dist_restraint': 1 if flags.has_dist_restraint else 0,
                                   'dihed_restraint': 1 if flags.has_dihed_restraint else 0,
                                   'rdc_restraint': 1 if flags.has_rdc_restraint else 0,
                                   'plane_restraint': 1 if flags.has_plane_restraint else 0,
                                   'hbond_restraint': 1 if flags.has_hbond_restraint else 0,
                                   'ssbond_restraint': 1 if flags.has_ssbond_restraint else 0,
                                   'coordinate': 1 if flags.has_coordinate else 0,
                                   'topology': 1 if flags.has_topology else 0}
            else:
                for key in ('dist_restraint', 'dihed_restraint', 'rdc_restraint',
                            'plane_restraint', 'hbond_restraint', 'ssbond_restraint'):
                    if key in content_subtype:
                        setattr(flags, f'has_{key}', True)

            self.__reportUnidentifiedContent(file_type, file_name, mr_format_name, content_subtype, valid, flags)

            self.__reg.legacy_dist_restraint_uploaded |= flags.has_dist_restraint

            input_source.setItemValue('content_subtype', content_subtype)

        if not self.__reg.legacy_dist_restraint_uploaded:
            self.__checkMandatoryDistRestraint()

        self.__detectDuplicateMrUpload(md5_list)

        return corrected

    def detectContentSubTypeOfLegacyPk(self) -> bool:
        """ Detect content subtype of legacy spectral peak files.
        """

        if self.__reg.combined_mode:
            return True

        if AR_FILE_PATH_LIST_KEY not in self.__reg.inputParamDict:
            return True

        fileListId = self.__reg.file_path_list_len

        for ar in self.__reg.inputParamDict[AR_FILE_PATH_LIST_KEY]:
            file_path = ar['file_name']

            input_source = self.__reg.report.input_sources[fileListId]
            input_source_dic = input_source.get()

            file_name = input_source_dic['file_name']
            file_type = input_source_dic['file_type']

            fileListId += 1

            if file_type is None or not file_type.startswith('nm-pea'):
                continue

            # DAOTHER-8905: ignore the file in NMR data remediation (Phase 2)
            if self.__reg.internal_mode and os.path.exists(self.testPathWithSuffix(file_path, '-ignored', True)):
                continue

            original_file_name = None
            if 'original_file_name' in input_source_dic:
                if input_source_dic['original_file_name'] is not None:
                    original_file_name = os.path.basename(input_source_dic['original_file_name'])
                if file_name != original_file_name and original_file_name is not None:
                    file_name = f"{original_file_name} ({file_name})"

            if is_binary_file(file_path) or is_eps_or_pdf_file(file_path):  # DAOTHER-9425

                err = f"The spectral peak list file {file_name!r} (any plain text format) is not a plain text file."

                self.__reg.report.error.appendDescription('format_issue',
                                                          {'file_name': file_name, 'description': err})

                if self.__reg.verbose:
                    self.__reg.log.write(f"+{self.__class_name__}.detectContentSubTypeOfLegacyPk() ++ Error  - {err}\n")

                if self.__reg.internal_mode:
                    os.symlink(file_path, self.testPath(file_path + '-ignored', True))

                continue

            codec = detect_bom(file_path, 'utf-8')

            if codec != 'utf-8':
                _file_path = self.getNextPath(file_path)
                convert_codec(file_path, _file_path, codec, 'utf-8')
                file_path = _file_path

            if file_type != 'nm-pea-any':

                reader = self.getSimpleFileReader(file_type, False)

                listener, parser_err_listener, _ = reader.parse(file_path, None)

                # ignore lexer error because of incomplete XML file format
                # has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
                has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None
                content_subtype = listener.getContentSubtype() if listener is not None else None
                if not has_parser_error and content_subtype is not None and len(content_subtype) > 0:
                    input_source_dic['content_subtype'] = content_subtype
                    continue

            else:

                _file_type, _content_subtype = self.__getPeakListFileTypeAndContentSubtype(file_path)

                if _file_type is not None:
                    input_source_dic['file_type'] = _file_type
                    input_source_dic['content_subtype'] = _content_subtype
                    continue

            content_subtype = input_source_dic['content_subtype']
            if content_subtype is None:
                input_source_dic['content_subtype'] = {'spectral_peak': 1}

            has_mr_header = has_pdb_format = has_cif_format = has_str_format = False

            try:

                header = True
                in_header = pdb_record = cs_str = mr_str =\
                    has_datablock = has_anonymous_saveframe = has_save = has_loop = has_stop = False

                first_str_line_num = last_str_line_num = -1

                i = 0

                with open(file_path, 'r', encoding='utf-8', errors='ignore') as ifh:
                    for line in ifh:
                        i += 1

                        # skip MR header
                        if header:
                            if line.startswith('*'):
                                continue
                            if startsWithPdbRecord(line, True):
                                continue
                            header = False

                        if line.startswith('*') and startsWithPdbRecord(line[1:], True):
                            in_header = True
                            continue

                        if in_header and line.startswith('*END'):
                            in_header = False
                            continue

                        if PDB_MR_FILE_HEADER_PAT.match(line)\
                           or SEL_MR_FILE_HEADER_PAT.match(line)\
                           or SEL_PK_FILE_HEADER_PAT.match(line)\
                           or SEL_CS_FILE_HEADER_PAT.match(line):
                            has_mr_header = True

                        # skip legacy PDB
                        if startsWithPdbRecord(line, True):
                            has_pdb_format = pdb_record = True
                            continue
                        if pdb_record:
                            pdb_record = False
                            if line.startswith('END'):
                                continue

                        # check STAR
                        str_syntax = False
                        if DATABLOCK_PAT.match(line):
                            str_syntax = has_datablock = True
                        elif SF_ANONYMOUS_PAT.match(line):
                            str_syntax = has_anonymous_saveframe = True
                        elif SAVE_PAT.match(line):
                            str_syntax = has_save = True
                        elif LOOP_PAT.match(line):
                            str_syntax = has_loop = True
                        elif STOP_PAT.match(line):
                            str_syntax = has_stop = True

                        if str_syntax:
                            if first_str_line_num < 0:
                                first_str_line_num = i
                            last_str_line_num = i
                            if (has_anonymous_saveframe and has_save) or (has_loop and has_stop):
                                has_str_format = True
                            elif has_datablock and has_loop and not has_stop:
                                has_cif_format = True

                if last_str_line_num - first_str_line_num < 10:
                    has_str_format = has_cif_format = False

                if has_pdb_format:
                    err = f"The spectral peak list file {file_name!r} (any plain text format) is identified as coordinate file. "\
                        "Did you accidentally select wrong format? Please re-upload the spectral peak list file."

                    self.__reg.report.error.appendDescription('content_mismatch',
                                                              {'file_name': file_name, 'description': err})

                    if self.__reg.verbose:
                        self.__reg.log.write(f"+{self.__class_name__}.detectContentSubTypeOfLegacyPk() ++ Error  - {err}\n")

                    continue

                if has_mr_header:
                    err = f"The spectral peak list file {file_name!r} (any plain text format) "\
                        f"is identified as {getRestraintFormatName('nm-res-mr')}. "\
                        "Did you accidentally select wrong format? Please re-upload the spectral peak list file."

                    self.__reg.report.error.appendDescription('content_mismatch',
                                                              {'file_name': file_name, 'description': err})

                    if self.__reg.verbose:
                        self.__reg.log.write(f"+{self.__class_name__}.detectContentSubTypeOfLegacyPk() ++ Error  - {err}\n")

                    continue

                message = None

                # split STAR and others
                if has_str_format:

                    file_subtype = 'O'

                    is_valid, message = self.__reg.nefT.validate_file(file_path, file_subtype)

                    if not is_valid:
                        _is_valid, message = self.__reg.nefT.validate_file(file_path, 'S')
                        if _is_valid:
                            cs_str = True
                    else:
                        mr_str = True

                elif has_cif_format:

                    _file_path = self.getNextPath(file_path, '.cif2str')
                    if not self.__reg.c2S.convert(file_path, _file_path):
                        _file_path = file_path

                    file_subtype = 'O'

                    is_valid, message = self.__reg.nefT.validate_file(_file_path, file_subtype)

                    if not is_valid:
                        _is_valid, message = self.__reg.nefT.validate_file(_file_path, 'S')
                        if _is_valid:
                            cs_str = True
                    else:
                        mr_str = True

                if cs_str:
                    err = f"The spectral peak list file {file_name!r} (any plain text format) is identified as "\
                        f"{READABLE_FILE_TYPE[message['file_type']]} formatted assigned chemical shift file. "\
                        "Did you accidentally select wrong format? Please re-upload the spectral peak list file."

                    self.__reg.report.error.appendDescription('content_mismatch',
                                                              {'file_name': file_name, 'description': err})

                    if self.__reg.verbose:
                        self.__reg.log.write(f"+{self.__class_name__}.detectContentSubTypeOfLegacyPk() ++ Error  - {err}\n")

                    continue

                if mr_str:
                    err = f"The spectral peak list file {file_name!r} (any plain text format) is identified as "\
                        f"{READABLE_FILE_TYPE[message['file_type']]} formatted restraint file. "\
                        "Did you accidentally select wrong format? Please re-upload the spectral peak list file."

                    self.__reg.report.error.appendDescription('content_mismatch',
                                                              {'file_name': file_name, 'description': err})

                    if self.__reg.verbose:
                        self.__reg.log.write(f"+{self.__class_name__}.detectContentSubTypeOfLegacyPk() ++ Error  - {err}\n")

                    continue

            except Exception as e:  # pylint: disable=broad-exception-caught

                self.__reg.report.error.appendDescription('internal_error',
                                                          f"+{self.__class_name__}.detectContentSubTypeOfLegacyPk() "
                                                          "++ Error  - " + str(e))

                if self.__reg.verbose:
                    self.__reg.log.write(f"+{self.__class_name__}.detectContentSubTypeOfLegacyPk() ++ Error  - {str(e)}\n")

                return False

            if file_type != 'nm-pea-any':
                continue

            _, _, valid_types, possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr(file_path, file_name, 'nm-pea-any', [], True)

            len_valid_types = len(valid_types)
            len_possible_types = len(possible_types)

            if len_valid_types == 0 and len_possible_types == 0:
                continue

            if len_possible_types == 0:

                # DAOTHER-8905: rescue the file as restraint file in NMR data remediation (Phase 2)
                if self.__reg.internal_mode:

                    _file_type = None

                    if len_valid_types == 1:
                        _file_type = valid_types[0]

                    elif len_valid_types == 2:
                        if 'nm-res-cns' in valid_types and 'nm-res-xpl' in valid_types:
                            _file_type = 'nm-res-xpl'

                        elif 'nm-res-cya' in valid_types:
                            _file_type = next(valid_type for valid_type in valid_types if valid_type != 'nm-res-cya')

                        elif 'nm-res-cya' in valid_types and 'nm-res-ros' in valid_types:
                            _file_type = 'nm-res-ros'

                    elif len_valid_types == 3:
                        set_valid_types = set(valid_types)
                        if set_valid_types in ({'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'},
                                               {'nm-res-isd', 'nm-res-cns', 'nm-res-xpl'}):
                            _file_type = 'nm-res-xpl'

                        elif set_valid_types == {'nm-res-cha', 'nm-res-cns', 'nm-res-xpl'}:
                            _file_type = 'nm-res-cha'

                        elif set_valid_types == {'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'}:
                            _file_type = 'nm-res-xpl'

                    if _file_type is not None and _file_type.startswith('nm-res'):
                        input_source_dic['file_type'] = _file_type
                        input_source_dic['content_type'] = 'nmr-restraints'
                        continue

                err = f"The spectral peak list file {file_name!r} (any plain text format) "\
                    f"is identified as {getRestraintFormatNames(valid_types)} file. "\
                    "Did you accidentally select wrong format? Please re-upload the spectral peak list file."

                self.__reg.report.error.appendDescription('content_mismatch',
                                                          {'file_name': file_name, 'description': err})

                if self.__reg.verbose:
                    self.__reg.log.write(f"+{self.__class_name__}.detectContentSubTypeOfLegacyPk() ++ Error  - {err}\n")

            elif len_valid_types == 0:

                err = f"The spectral peak list file {file_name!r} (any plain text format) can be {possible_types}. "\
                    "Did you accidentally select wrong format? Please re-upload the spectral peak list file."

                self.__reg.report.error.appendDescription('content_mismatch',
                                                          {'file_name': file_name, 'description': err})

                if self.__reg.verbose:
                    self.__reg.log.write(f"+{self.__class_name__}.detectContentSubTypeOfLegacyPk() ++ Error  - {err}\n")

            else:

                err = f"The spectral peak list file {file_name!r} (any plain text format) "\
                    f"is identified as {getRestraintFormatNames(valid_types)} file "\
                    f"and can be {getRestraintFormatNames(possible_types)} file as well. "\
                    "Did you accidentally select wrong format? Please re-upload the spectral peak list file."

                self.__reg.report.error.appendDescription('content_mismatch',
                                                          {'file_name': file_name, 'description': err})

                if self.__reg.verbose:
                    self.__reg.log.write(f"+{self.__class_name__}.detectContentSubTypeOfLegacyPk() ++ Error  - {err}\n")

        return not self.__reg.report.isError()

    def extractPublicMrFileIntoLegacyMr(self) -> bool:
        """ Extract/split public PDB-MR file into legacy restraint files for NMR restraint remediation.
        """

        if self.__reg.combined_mode or not self.__reg.remediation_mode:
            return True

        if AR_FILE_PATH_LIST_KEY not in self.__reg.inputParamDict:
            return True

        fileListId = self.__reg.file_path_list_len

        dir_path = mr_file_name = '.'
        split_file_list, peak_file_list = [], []

        self.__reg.mr_atom_name_mapping = []

        remediated = aborted = False
        src_basename = mr_core_path = mr_file_path = mr_file_link = None
        mr_part_paths, pk_list_paths = [], []

        settled_file_types = list(PARSABLE_MR_FILE_TYPES)
        settled_file_types.extend(list(PARSABLE_PK_FILE_TYPES))
        settled_file_types.append('nm-res-sax')

        for ar in self.__reg.inputParamDict[AR_FILE_PATH_LIST_KEY]:
            src_file = ar['file_name']

            input_source = self.__reg.report.input_sources[fileListId]
            input_source_dic = input_source.get()

            file_name = input_source_dic['file_name']
            file_type = input_source_dic['file_type']

            fileListId += 1

            if ar['file_type'] == 'nm-aux-pdb':
                continue

            if file_type != 'nm-res-mr':

                if file_type in LINEAR_MR_FILE_TYPES:
                    with open(src_file, 'r', encoding='utf-8', errors='ignore') as ifh:
                        for line in ifh:
                            if 'Submitted Coord H atom name' in line:
                                input_source.setItemValue('file_type', 'nm-res-mr')
                                return self.extractPublicMrFileIntoLegacyMr()

                continue

            original_file_name = None
            if 'original_file_name' in input_source_dic:
                if input_source_dic['original_file_name'] is not None:
                    original_file_name = os.path.basename(input_source_dic['original_file_name'])
                if file_name != original_file_name and original_file_name is not None:
                    file_name = f"{original_file_name} ({file_name})"

            mr_file_name = file_name

            self.__cur_original_ar_file_name = original_file_name

            if is_binary_file(src_file) or is_eps_or_pdf_file(src_file):

                if not src_file.endswith('.gz'):

                    err = f"The restraint file {src_file!r} (MR format) is neither ASCII file nor gzip compressed file."

                    self.__reg.report.error.appendDescription('internal_error',
                                                              f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                              "++ Error  - " + err)

                    if self.__reg.verbose:
                        self.__reg.log.write(f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                             f"++ Error  - {err}\n")

                    return False

                dst_file = self.testPath(os.path.splitext(src_file)[0])

                if not os.path.exists(dst_file):

                    try:

                        uncompress_gzip_file(src_file, dst_file)

                    except IOError as e:

                        self.__reg.report.error.appendDescription('internal_error',
                                                                  f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                                  "++ Error  - " + str(e))

                        if self.__reg.verbose:
                            self.__reg.log.write(f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                 f"++ Error  - {str(e)}\n")

                        return False

                src_file = dst_file

            dir_path = os.path.dirname(src_file) if self.__reg.dirPath is None else self.__reg.dirPath

            _div_file_names = {div_file_name: len(div_file_name) + (0 if div_file_name.endswith('-div_src.mr')
                                                                    else (1 if div_file_name.endswith('-div_ext.mr') else 2))
                               for div_file_name in os.listdir(dir_path)
                               if os.path.isfile(os.path.join(dir_path, div_file_name))
                               and (div_file_name.endswith('-div_src.mr')
                                    or div_file_name.endswith('-div_dst.mr')
                                    or div_file_name.endswith('-div_ext.mr'))}

            div_file_names = [k for k, v in sorted(_div_file_names.items(), key=itemgetter(1))]

            src_basename = os.path.splitext(src_file)[0]

            if self.__reg.dirPath is not None:
                src_basename = os.path.join(self.__reg.dirPath, os.path.basename(src_basename))

            ar['original_file_name'] = f'{src_basename}.mr'

            dst_file = src_basename + '-trimmed.mr'
            header_file = src_basename + '-header.mr'
            footer_file = src_basename + '-footer.mr'
            cor_dst_file = self.testPathWithSuffix(src_basename, '-corrected.mr')
            cor_str_file = self.testPathWithSuffix(src_basename, '-corrected.str')
            ign_dst_file = self.testPathWithSuffix(src_basename, '-ignored.mr', True)

            if os.path.exists(ign_dst_file):  # in case the MR file can be ignored
                continue

            ign_pk_file = self.testPathWithSuffix(src_basename, '-ignored-as-pea-any.mr', True)

            if os.path.exists(ign_pk_file):  # in case the MR file can be ignored as peak list file

                settled_file_type, _ = self.__getPeakListFileTypeAndContentSubtype(ign_pk_file)

                _ar = ar.copy()

                if settled_file_type is not None:
                    sel_pk_file = self.testPath(src_basename + f'-selected-as-{settled_file_type[-7:]}.mr', True)
                    os.rename(ign_pk_file, sel_pk_file)

                    _ar['file_name'] = sel_pk_file
                    _ar['file_type'] = settled_file_type

                else:

                    _ar['file_name'] = ign_pk_file
                    _ar['file_type'] = 'nm-pea-any'

                peak_file_list.append(_ar)

                pk_list_paths.append({'nmr-peaks': f'{src_basename}.mr'})

                touch_file = os.path.join(dir_path, '.entry_with_pk')
                if not os.path.exists(self.testPath(touch_file)):
                    with open(touch_file, 'w', encoding='utf-8') as ofh:
                        ofh.write('')

                continue

            designated = False

            for _file_type in settled_file_types:

                sel_file = self.testPath(src_basename + f'-selected-as-{_file_type[-7:]}.mr', True)

                if os.path.exists(sel_file):
                    _ar = ar.copy()

                    _ar['file_name'] = sel_file
                    _ar['file_type'] = _file_type
                    split_file_list.append(_ar)

                    designated = True

                    break

            if designated:
                continue

            if mr_file_path is None:

                rem_dir = os.path.join(dir_path, 'remediation')

                try:

                    if not os.path.isdir(rem_dir):
                        os.makedirs(rem_dir)

                except OSError:
                    pass

                mr_file_path = src_basename + '-remediated.mr'
                mr_file_link = os.path.join(rem_dir, f'{os.path.basename(src_basename)}.mr')

                mr_part_paths.append({'header': header_file})
                mr_part_paths.append({'footer': footer_file})

            has_mr_header = has_pdb_format = has_cif_format = has_str_format = has_cs_str = False

            try:

                header = True
                in_header = pdb_record = footer =\
                    has_datablock = has_anonymous_saveframe = has_save = has_loop = has_stop = False

                first_str_line_num = last_str_line_num = -1

                i = 0

                with open(src_file, 'r', encoding='utf-8') as ifh, \
                        open(dst_file, 'w', encoding='utf-8') as ofh, \
                        open(header_file, 'w', encoding='utf-8') as hofh, \
                        open(footer_file, 'w', encoding='utf-8') as fofh:
                    for line in ifh:
                        i += 1

                        # skip MR header
                        if header:
                            if line.startswith('*'):
                                hofh.write(line)
                                continue
                            if startsWithPdbRecord(line):
                                continue
                            header = False

                        if not footer:
                            if line.startswith('*') and startsWithPdbRecord(line[1:]):
                                hofh.write(line)
                                in_header = True
                                continue

                            if in_header and line.startswith('*END'):
                                hofh.write(line)
                                in_header = False
                                continue

                        if PDB_MR_FILE_HEADER_PAT.match(line)\
                           or SEL_MR_FILE_HEADER_PAT.match(line)\
                           or SEL_PK_FILE_HEADER_PAT.match(line)\
                           or SEL_CS_FILE_HEADER_PAT.match(line):
                            has_mr_header = True

                        # skip legacy PDB
                        if startsWithPdbRecord(line):
                            has_pdb_format = pdb_record = True
                            continue
                        if pdb_record:
                            pdb_record = False
                            if line.startswith('END'):
                                continue

                        # check STAR
                        str_syntax = False
                        if DATABLOCK_PAT.match(line):
                            str_syntax = has_datablock = True
                        elif SF_ANONYMOUS_PAT.match(line):
                            str_syntax = has_anonymous_saveframe = True
                        elif SAVE_PAT.match(line):
                            str_syntax = has_save = True
                        elif LOOP_PAT.match(line):
                            str_syntax = has_loop = True
                        elif STOP_PAT.match(line):
                            str_syntax = has_stop = True

                        if str_syntax:
                            if first_str_line_num < 0:
                                first_str_line_num = i
                            last_str_line_num = i
                            if (has_anonymous_saveframe and has_save) or (has_loop and has_stop):
                                has_str_format = True
                            elif has_datablock and has_loop and not has_stop:
                                has_cif_format = True

                        # skip MR footer
                        if 'Submitted Coord H atom name' in line:
                            fofh.write(line)
                            footer = True
                            continue

                        if footer:
                            fofh.write(line)
                            col = line.split()
                            len_col = len(col)
                            if len_col == 10:
                                original_comp_id = col[5].upper()
                                if original_comp_id not in STD_MON_DICT:  # extract non-standard residues
                                    try:
                                        atom_map = {'auth_atom_id': col[1],
                                                    'auth_comp_id': col[2],
                                                    'auth_seq_id': int(col[3]),
                                                    'original_atom_id': col[4].upper(),
                                                    'original_comp_id': original_comp_id,
                                                    'original_seq_id': int(col[6])}
                                        if atom_map not in self.__reg.mr_atom_name_mapping:
                                            self.__reg.mr_atom_name_mapping.append(atom_map)
                                    except ValueError:
                                        pass
                            elif len_col >= 8:  # 2liw 4 digits residue number

                                def split_concat_comp_id_seq_id(string):
                                    if not string[-1].isdigit():
                                        return None, None
                                    idx = len(string) - 1
                                    while idx >= 0 and string[idx].isdigit():
                                        idx -= 1
                                    if idx == 0:
                                        return None, None
                                    if string[idx] != '-':
                                        idx += 1
                                    return string[:idx], int(string[idx:])

                                if len(col[2]) > 4:
                                    auth_comp_id, auth_seq_id = split_concat_comp_id_seq_id(col[2])

                                    if len(col[4]) > 4 and len_col == 8:
                                        orig_comp_id, orig_seq_id = split_concat_comp_id_seq_id(col[4])
                                        if auth_comp_id is not None and orig_comp_id is not None\
                                           and orig_comp_id.upper() not in STD_MON_DICT:
                                            atom_map = {'auth_atom_id': col[1],
                                                        'auth_comp_id': auth_comp_id,
                                                        'auth_seq_id': auth_seq_id,
                                                        'original_atom_id': col[3].upper(),
                                                        'original_comp_id': orig_comp_id.upper(),
                                                        'original_seq_id': orig_seq_id}
                                            if atom_map not in self.__reg.mr_atom_name_mapping:
                                                self.__reg.mr_atom_name_mapping.append(atom_map)
                                    elif len_col == 9:
                                        if auth_comp_id is not None and col[4] not in STD_MON_DICT:
                                            try:
                                                atom_map = {'auth_atom_id': col[1],
                                                            'auth_comp_id': auth_comp_id,
                                                            'auth_seq_id': auth_seq_id,
                                                            'original_atom_id': col[3].upper(),
                                                            'original_comp_id': col[4].upper(),
                                                            'original_seq_id': int(col[5])}
                                                if atom_map not in self.__reg.mr_atom_name_mapping:
                                                    self.__reg.mr_atom_name_mapping.append(atom_map)
                                            except ValueError:
                                                pass
                                elif len(col[5]) > 4 and len_col == 9:
                                    orig_comp_id, orig_seq_id = split_concat_comp_id_seq_id(col[5])
                                    if orig_comp_id is not None and orig_comp_id.upper() not in STD_MON_DICT:
                                        try:
                                            atom_map = {'auth_atom_id': col[1],
                                                        'auth_comp_id': col[2],
                                                        'auth_seq_id': int(col[3]),
                                                        'original_atom_id': col[4].upper(),
                                                        'original_comp_id': orig_comp_id.upper(),
                                                        'original_seq_id': orig_seq_id}
                                            if atom_map not in self.__reg.mr_atom_name_mapping:
                                                self.__reg.mr_atom_name_mapping.append(atom_map)
                                        except ValueError:
                                            pass

                        else:
                            ofh.write(line)

                if last_str_line_num - first_str_line_num < 10:
                    has_str_format = has_cif_format = False

                # split STAR and others
                if has_str_format and not has_mr_header:

                    remediated = True

                    mrPath = self.testPathWithSuffix(os.path.splitext(src_file)[0], '-ignored.str', True)

                    if not os.path.exists(mrPath):
                        mrPath = os.path.splitext(src_file)[0] + '-trimmed.str'

                        header = True
                        in_header = pdb_record = False

                        i = 0

                        with open(src_file, 'r', encoding='utf-8') as ifh, \
                                open(dst_file, 'w', encoding='utf-8') as ofh, \
                                open(mrPath, 'w', encoding='utf-8') as ofh2:
                            for line in ifh:
                                i += 1

                                # skip MR header
                                if header:
                                    if line.startswith('*'):
                                        continue
                                    header = False

                                if line.startswith('*') and startsWithPdbRecord(line[1:]):
                                    in_header = True
                                    continue

                                if in_header and line.startswith('*END'):
                                    in_header = False
                                    continue

                                # skip legacy PDB
                                if has_pdb_format:
                                    if startsWithPdbRecord(line):
                                        pdb_record = True
                                        continue
                                    if pdb_record:
                                        pdb_record = False
                                        if line.startswith('END'):
                                            continue

                                if first_str_line_num <= i <= last_str_line_num:
                                    ofh2.write(line)
                                    continue

                                # skip MR footer
                                if 'Submitted Coord H atom name' in line:
                                    break

                                ofh.write(line)

                        _mrPath = self.testPathWithSuffix(os.path.splitext(src_file)[0], '-corrected.str')

                        if os.path.exists(_mrPath):  # in case manually corrected NMR-STAR file exists
                            mrPath = _mrPath

                        if MR_FILE_PATH_LIST_KEY not in self.__reg.inputParamDict:
                            self.__reg.inputParamDict[MR_FILE_PATH_LIST_KEY] = [mrPath]
                        else:
                            self.__reg.inputParamDict[MR_FILE_PATH_LIST_KEY].append(mrPath)

                        insert_index = self.__reg.file_path_list_len

                        if insert_index > len(self.__reg.star_data):
                            self.__reg.star_data.append(None)
                            self.__reg.star_data_type.append(None)

                        self.__reg.report.insertInputSource(insert_index)

                        self.__reg.file_path_list_len += 1

                        input_source = self.__reg.report.input_sources[insert_index]

                        file_type = 'nmr-star'
                        file_name = os.path.basename(mrPath)

                        input_source.setItemValue('file_name', file_name)
                        input_source.setItemValue('file_type', file_type)
                        input_source.setItemValue('content_type', 'nmr-restraints')

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

                        file_subtype = 'O'

                        is_valid, message = self.__reg.nefT.validate_file(mrPath, file_subtype)

                        if not is_valid or not self.__reg.has_star_chem_shift:
                            _is_valid, _ = self.__reg.nefT.validate_file(mrPath, 'S')
                            if _is_valid:
                                has_cs_str = True

                        self.__reg.original_error_message.append(message)

                        _file_type = message['file_type']  # nef/nmr-star/unknown

                        if is_valid:

                            if _file_type != file_type:

                                err = f"{file_name!r} was selected as {READABLE_FILE_TYPE[file_type]} file, "\
                                    f"but recognized as {READABLE_FILE_TYPE[_file_type]} file."
                                # DAOTHER-5673
                                err += " Please re-upload the NEF file as an NMR unified data file."\
                                    if _file_type == 'nef' else " Please re-upload the file."

                                if len(message['error']) > 0:
                                    for err_message in message['error']:
                                        if 'No such file or directory' not in err_message:
                                            err += ' ' + re.sub('not in list', 'unknown item.', err_message)

                                self.__reg.report.error.appendDescription('content_mismatch',
                                                                          {'file_name': file_name, 'description': err})

                                if self.__reg.verbose:
                                    self.__reg.log.write(f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                         f"++ Error  - {err}\n")

                            else:

                                _is_done, star_data_type, star_data = self.__reg.nefT.read_input_file(mrPath)

                                self.__reg.has_legacy_sf_issue = False

                                if star_data_type == 'Saveframe':
                                    self.__reg.has_legacy_sf_issue = True

                                    self.__reg.dpA.fixFormatIssueOfInputSource(insert_index, file_name, file_type,
                                                                               mrPath, file_subtype, message,
                                                                               hasLegacySfIssue=self.__reg.has_legacy_sf_issue)

                                    _is_done, star_data_type, star_data = self.__reg.nefT.read_input_file(mrPath)

                                if not (self.__reg.has_legacy_sf_issue and _is_done and star_data_type == 'Entry'):

                                    if len(self.__reg.star_data_type) == self.__reg.file_path_list_len:
                                        del self.__reg.star_data_type[-1]
                                        del self.__reg.star_data[-1]

                                    self.__reg.star_data_type.append(star_data_type)
                                    self.__reg.star_data.append(star_data)

                                    self.__reg.dpA.rescueFormerNef(insert_index)
                                    self.__reg.dpA.rescueImmatureStr(insert_index)

                                if _is_done:
                                    self.__reg.dpV.detectContentSubType__(insert_index, input_source, dir_path)
                                    input_source_dic = input_source.get()
                                    if 'content_subtype' in input_source_dic:
                                        content_subtype = input_source_dic['content_subtype']
                                        if any(True for mr_content_subtype in self.__reg.mr_content_subtypes
                                               if mr_content_subtype in content_subtype):
                                            self.__reg.mr_has_valid_star_restraint = True
                                            mr_part_paths.append({'nmr-star': mrPath})

                        else:

                            if not self.__reg.dpA.fixFormatIssueOfInputSource(insert_index, file_name, file_type,
                                                                              mrPath, file_subtype, message,
                                                                              hasLegacySfIssue=self.__reg.has_legacy_sf_issue):
                                _is_done = False

                        if _mrPath is not None:
                            try:
                                os.remove(_mrPath)
                            except OSError:
                                pass

                        # release cached input data on NefTranslator because there is no chance
                        # to read the same file hereafter
                        self.__reg.nefT.release()

                elif has_cif_format and not has_mr_header:

                    remediated = True

                    mrPath = self.testPathWithSuffix(os.path.splitext(src_file)[0], '-ignored.cif', True)

                    if not os.path.exists(mrPath):
                        mrPath = os.path.splitext(src_file)[0] + '-trimmed.cif'

                        header = True
                        in_header = pdb_record = has_sharp = False

                        i = 0

                        with open(src_file, 'r', encoding='utf-8') as ifh, \
                                open(dst_file, 'w', encoding='utf-8') as ofh, \
                                open(mrPath, 'w', encoding='utf-8') as ofh2:
                            for line in ifh:
                                i += 1

                                # skip MR header
                                if header:
                                    if line.startswith('*'):
                                        continue
                                    header = False

                                if line.startswith('*') and startsWithPdbRecord(line[1:]):
                                    in_header = True
                                    continue

                                if in_header and line.startswith('*END'):
                                    in_header = False
                                    continue

                                if first_str_line_num <= i and not has_sharp:
                                    if i <= last_str_line_num:
                                        ofh2.write(line)
                                        continue
                                    ofh2.write(line)
                                    if line.startswith('#'):
                                        has_sharp = True
                                    continue

                                # skip legacy PDB
                                if has_pdb_format:
                                    if startsWithPdbRecord(line):
                                        pdb_record = True
                                        continue
                                    if pdb_record:
                                        pdb_record = False
                                        if line.startswith('END'):
                                            continue

                                # skip MR footer
                                if 'Submitted Coord H atom name' in line:
                                    break

                                ofh.write(line)

                        _mrPath = self.getNextPath(os.path.splitext(mrPath)[0], '.cif2str')
                        if not self.__reg.c2S.convert(mrPath, _mrPath):
                            _mrPath = mrPath

                        mrPath = _mrPath

                        if MR_FILE_PATH_LIST_KEY not in self.__reg.inputParamDict:
                            self.__reg.inputParamDict[MR_FILE_PATH_LIST_KEY] = [mrPath]
                        else:
                            self.__reg.inputParamDict[MR_FILE_PATH_LIST_KEY].append(mrPath)

                        insert_index = self.__reg.file_path_list_len

                        if insert_index > len(self.__reg.star_data):
                            self.__reg.star_data.append(None)
                            self.__reg.star_data_type.append(None)

                        self.__reg.report.insertInputSource(insert_index)

                        self.__reg.file_path_list_len += 1

                        input_source = self.__reg.report.input_sources[insert_index]

                        file_type = 'nmr-star'
                        file_name = os.path.basename(mrPath)

                        input_source.setItemValue('file_name', re.sub(r'\.cif2str$', '', file_name))
                        input_source.setItemValue('file_type', file_type)
                        input_source.setItemValue('content_type', 'nmr-restraints')

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

                        file_subtype = 'O'

                        is_valid, message = self.__reg.nefT.validate_file(mrPath, file_subtype)

                        if not is_valid or not self.__reg.has_star_chem_shift:
                            _is_valid, _ = self.__reg.nefT.validate_file(mrPath, 'S')
                            if _is_valid:
                                has_cs_str = True

                        self.__reg.original_error_message.append(message)

                        _file_type = message['file_type']  # nef/nmr-star/unknown

                        if is_valid:

                            if _file_type != file_type:

                                err = f"{file_name!r} was selected as {READABLE_FILE_TYPE[file_type]} file, "\
                                    f"but recognized as {READABLE_FILE_TYPE[_file_type]} file."
                                # DAOTHER-5673
                                err += " Please re-upload the NEF file as an NMR unified data file."\
                                    if _file_type == 'nef' else " Please re-upload the file."

                                if len(message['error']) > 0:
                                    for err_message in message['error']:
                                        if 'No such file or directory' not in err_message:
                                            err += ' ' + re.sub('not in list', 'unknown item.', err_message)

                                self.__reg.report.error.appendDescription('content_mismatch',
                                                                          {'file_name': file_name, 'description': err})

                                if self.__reg.verbose:
                                    self.__reg.log.write(f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                         f"++ Error  - {err}\n")

                            else:

                                _is_done, star_data_type, star_data = self.__reg.nefT.read_input_file(mrPath)

                                self.__reg.has_legacy_sf_issue = False

                                if star_data_type == 'Saveframe':
                                    self.__reg.has_legacy_sf_issue = True

                                    self.__reg.dpA.fixFormatIssueOfInputSource(insert_index, file_name, file_type,
                                                                               mrPath, file_subtype, message,
                                                                               hasLegacySfIssue=self.__reg.has_legacy_sf_issue)

                                    _is_done, star_data_type, star_data = self.__reg.nefT.read_input_file(mrPath)

                                if not (self.__reg.has_legacy_sf_issue and _is_done and star_data_type == 'Entry'):

                                    if len(self.__reg.star_data_type) == self.__reg.file_path_list_len:
                                        del self.__reg.star_data_type[-1]
                                        del self.__reg.star_data[-1]

                                    self.__reg.star_data_type.append(star_data_type)
                                    self.__reg.star_data.append(star_data)

                                    self.__reg.dpA.rescueFormerNef(insert_index)
                                    self.__reg.dpA.rescueImmatureStr(insert_index)

                                if _is_done:
                                    self.__reg.dpV.detectContentSubType__(insert_index, input_source, dir_path)
                                    input_source_dic = input_source.get()
                                    if 'content_subtype' in input_source_dic:
                                        content_subtype = input_source_dic['content_subtype']
                                        if any(True for mr_content_subtype in self.__reg.mr_content_subtypes
                                               if mr_content_subtype in content_subtype):
                                            self.__reg.mr_has_valid_star_restraint = True
                                            mr_part_paths.append({'nmr-star': mrPath})

                        else:

                            if not self.__reg.dpA.fixFormatIssueOfInputSource(insert_index, file_name, file_type,
                                                                              mrPath, file_subtype, message,
                                                                              hasLegacySfIssue=self.__reg.has_legacy_sf_issue):
                                _is_done = False

                        if _mrPath is not None:
                            try:
                                os.remove(_mrPath)
                            except OSError:
                                pass

                        # release cached input data on NefTranslator because there is no chance
                        # to read the same file hereafter
                        self.__reg.nefT.release()

            except Exception as e:  # pylint: disable=broad-exception-caught

                self.__reg.report.error.appendDescription('internal_error',
                                                          f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                          "++ Error  - " + str(e))

                if self.__reg.verbose:
                    self.__reg.log.write(f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                         f"++ Error  - {str(e)}\n")

                return False

            has_content = False
            with open(dst_file, 'r', encoding='utf-8') as ifh:
                for line in ifh:
                    if line.isspace() or COMMENT_PAT.match(line):
                        continue
                    has_content = True
                    break

            if not has_content:
                if not self.__reg.mr_has_valid_star_restraint:
                    with open(os.path.join(dir_path, '.entry_without_mr'), 'w', encoding='utf-8') as ofh:
                        ofh.write('')

                    remediated = False

                    continue

            if os.path.exists(cor_str_file) and os.path.exists(cor_dst_file) and has_content:
                mrPath = cor_str_file

                item = {'file_name': mrPath,
                        'file_type': 'nmr-star',
                        'original_file_name': f'{os.path.basename(src_basename)}.mr'}

                if MR_FILE_PATH_LIST_KEY not in self.__reg.inputParamDict:
                    self.__reg.inputParamDict[MR_FILE_PATH_LIST_KEY] = [item]
                else:
                    self.__reg.inputParamDict[MR_FILE_PATH_LIST_KEY].append(item)

                insert_index = self.__reg.file_path_list_len

                if insert_index > len(self.__reg.star_data):
                    self.__reg.star_data.append(None)
                    self.__reg.star_data_type.append(None)

                self.__reg.report.insertInputSource(insert_index)

                self.__reg.file_path_list_len += 1

                input_source = self.__reg.report.input_sources[insert_index]

                file_type = 'nmr-star'
                file_name = os.path.basename(mrPath)

                input_source.setItemValue('file_name', file_name)
                input_source.setItemValue('file_type', file_type)
                input_source.setItemValue('content_type', 'nmr-restraints')
                input_source.setItemValue('original_file_name', f'{os.path.basename(src_basename)}.mr')

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

                file_subtype = 'O'

                is_valid, message = self.__reg.nefT.validate_file(mrPath, file_subtype)

                if not is_valid or not self.__reg.has_star_chem_shift:
                    _is_valid, _ = self.__reg.nefT.validate_file(mrPath, 'S')
                    if _is_valid:
                        has_cs_str = True

                self.__reg.original_error_message.append(message)

                _file_type = message['file_type']  # nef/nmr-star/unknown

                if is_valid:

                    if _file_type != file_type:

                        err = f"{file_name!r} was selected as {READABLE_FILE_TYPE[file_type]} file, "\
                            f"but recognized as {READABLE_FILE_TYPE[_file_type]} file."
                        # DAOTHER-5673
                        err += " Please re-upload the NEF file as an NMR unified data file."\
                            if _file_type == 'nef' else " Please re-upload the file."

                        if len(message['error']) > 0:
                            for err_message in message['error']:
                                if 'No such file or directory' not in err_message:
                                    err += ' ' + re.sub('not in list', 'unknown item.', err_message)

                        self.__reg.report.error.appendDescription('content_mismatch',
                                                                  {'file_name': file_name, 'description': err})

                        if self.__reg.verbose:
                            self.__reg.log.write(f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                 f"++ Error  - {err}\n")

                    else:

                        _is_done, star_data_type, star_data = self.__reg.nefT.read_input_file(mrPath)

                        self.__reg.has_legacy_sf_issue = False

                        if star_data_type == 'Saveframe':
                            self.__reg.has_legacy_sf_issue = True

                            self.__reg.dpA.fixFormatIssueOfInputSource(insert_index, file_name, file_type,
                                                                       mrPath, file_subtype, message,
                                                                       hasLegacySfIssue=self.__reg.has_legacy_sf_issue)

                            _is_done, star_data_type, star_data = self.__reg.nefT.read_input_file(mrPath)

                        if not (self.__reg.has_legacy_sf_issue and _is_done and star_data_type == 'Entry'):

                            if len(self.__reg.star_data_type) == self.__reg.file_path_list_len:
                                del self.__reg.star_data_type[-1]
                                del self.__reg.star_data[-1]

                            self.__reg.star_data_type.append(star_data_type)
                            self.__reg.star_data.append(star_data)

                            self.__reg.dpA.rescueFormerNef(insert_index)
                            self.__reg.dpA.rescueImmatureStr(insert_index)

                        if _is_done:
                            self.__reg.dpV.detectContentSubType__(insert_index, input_source, dir_path)
                            input_source_dic = input_source.get()
                            if 'content_subtype' in input_source_dic:
                                content_subtype = input_source_dic['content_subtype']
                                if any(True for mr_content_subtype in self.__reg.mr_content_subtypes
                                       if mr_content_subtype in content_subtype):
                                    self.__reg.mr_has_valid_star_restraint = True
                                    mr_part_paths.append({'nmr-star': mrPath})

                else:

                    if not self.__reg.dpA.fixFormatIssueOfInputSource(insert_index, file_name, file_type,
                                                                      mrPath, file_subtype, message,
                                                                      hasLegacySfIssue=self.__reg.has_legacy_sf_issue):
                        _is_done = False

                if _mrPath is not None:
                    try:
                        os.remove(_mrPath)
                    except OSError:
                        pass

                # release cached input data on NefTranslator because there is no chance
                # to read the same file hereafter
                self.__reg.nefT.release()

            if os.path.exists(cor_dst_file):  # in case manually corrected MR file exists
                dst_file = cor_dst_file

                with open(dst_file, 'r', encoding='utf-8') as ifh:
                    for line in ifh:
                        if line.isspace() or COMMENT_PAT.match(line):
                            continue
                        has_content = True
                        break

                remediated = True

            if not has_content:
                continue

            mr_core_path = dst_file

            # has no MR header
            if not has_mr_header:

                dst_name_prefix = os.path.splitext(os.path.basename(dst_file))[0]
                dst_file_list = [os.path.join(dir_path, div_name) for div_name in div_file_names
                                 if div_name.startswith(dst_name_prefix)]

                if (not file_name.endswith('str') or mr_file_path.endswith('-remediated.mr')) and len(dst_file_list) == 0:
                    dst_file_list.append(dst_file)

                for dst_file in dst_file_list:

                    if dst_file.endswith('-div_ext.mr'):

                        ign_dst_file = self.testPathWithSuffix(dst_file, '-ignored', True)

                        if os.path.exists(ign_dst_file):  # in case the MR file can be ignored
                            remediated = True
                            continue

                        ign_pk_file = self.testPathWithSuffix(dst_file, '-ignored-as-pea-any', True)

                        if os.path.exists(ign_pk_file):  # in case the MR file can be ignored as peak list file

                            settled_file_type, _ = self.__getPeakListFileTypeAndContentSubtype(ign_pk_file)

                            _ar = ar.copy()

                            if settled_file_type is not None:
                                sel_pk_file = self.testPath(dst_file + f'-selected-as-{settled_file_type[-7:]}', True)
                                os.rename(ign_pk_file, sel_pk_file)

                                _ar['file_name'] = dst_file
                                _ar['file_type'] = settled_file_type

                            else:

                                _ar['file_name'] = dst_file
                                _ar['file_type'] = 'nm-pea-any'

                            peak_file_list.append(_ar)

                            pk_list_paths.append({'nmr-peaks': dst_file})

                            remediated = True

                            continue

                        designated = False

                        for _file_type in settled_file_types:

                            sel_file = self.testPathWithSuffix(dst_file, f'-selected-as-{_file_type[-7:]}', True)

                            if os.path.exists(sel_file):
                                _ar = ar.copy()

                                _ar['file_name'] = dst_file
                                _ar['file_type'] = _file_type
                                split_file_list.append(_ar)

                                mr_part_paths.append({_file_type: dst_file})

                                designated = True

                                break

                        if designated:
                            continue

                        _ar = ar.copy()

                        _ar['file_name'] = dst_file
                        _ar['file_type'] = 'nm-res-oth'
                        split_file_list.append(_ar)

                        mr_part_paths.append({_ar['file_type']: dst_file})

                        continue

                    if dst_file.endswith('-div_dst.mr'):

                        ign_dst_file = self.testPathWithSuffix(dst_file, '-ignored', True)

                        if os.path.exists(ign_dst_file):  # in case the MR file can be ignored
                            remediated = True
                            continue

                        ign_pk_file = self.testPathWithSuffix(dst_file, '-ignored-as-pea-any', True)

                        if os.path.exists(ign_pk_file):  # in case the MR file can be ignored as peak list file

                            settled_file_type, _ = self.__getPeakListFileTypeAndContentSubtype(ign_pk_file)

                            _ar = ar.copy()

                            if settled_file_type is not None:
                                sel_pk_file = self.testPath(dst_file + f'-selected-as-{settled_file_type[-7:]}', True)
                                os.rename(ign_pk_file, sel_pk_file)

                                _ar['file_name'] = dst_file
                                _ar['file_type'] = settled_file_type

                            else:

                                _ar['file_name'] = dst_file
                                _ar['file_type'] = 'nm-pea-any'

                            peak_file_list.append(_ar)

                            pk_list_paths.append({'nmr-peaks': dst_file})

                            remediated = True

                            continue

                        settled_pk_file = False

                        _ar = ar.copy()

                        for settled_file_type in PARSABLE_PK_FILE_TYPES:

                            sel_pk_file = self.testPathWithSuffix(dst_file, f'-selected-as-{settled_file_type[-7:]}', True)

                            if os.path.exists(sel_pk_file):

                                ign_dst_file = self.testPathWithSuffix(sel_pk_file, '-ignored', True)

                                if os.path.exists(ign_dst_file):
                                    continue

                                __ar = _ar.copy()

                                __ar['file_name'] = sel_pk_file
                                __ar['file_type'] = settled_file_type

                                if __ar in peak_file_list:
                                    continue

                                peak_file_list.append(__ar)

                                pk_list_paths.append({'nmr-peaks': dst_file})

                                settled_pk_file = remediated = True

                        if settled_pk_file:
                            continue

                    _, _, valid_types, possible_types =\
                        self.__detectOtherPossibleFormatAsErrorOfLegacyMr(dst_file, file_name, 'nm-res-mr', [], True)

                    len_valid_types = len(valid_types)
                    len_possible_types = len(possible_types)

                    if self.__reg.mr_debug:
                        self.__reg.log.write(f'{valid_types} {possible_types}\n')

                    if len_valid_types == 0 and len_possible_types == 0:

                        ins_msg = ''
                        if has_pdb_format and has_cs_str:
                            ins_msg = 'unexpectedly contains PDB coordinates and assigned chemical shifts, but '
                        elif has_pdb_format:
                            ins_msg = 'unexpectedly contains PDB coordinates, but '
                        elif has_cs_str:
                            ins_msg = 'unexpectedly contains assigned chemical shifts, but '

                        _file_name = os.path.basename(dst_file)
                        if file_name != _file_name:
                            _file_name = f'({_file_name}) '
                        else:
                            _file_name = ''

                        err = f"The restraint file {file_name!r} {_file_name}{ins_msg}does not match with "\
                            "any known restraint format. "\
                            "@todo: It needs to be reviewed or marked as entry without restraints."

                        self.__reg.report.error.appendDescription('internal_error',
                                                                  {'file_name': file_name, 'description': err})

                        if self.__reg.verbose:
                            self.__reg.log.write(f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                 f"++ Error  - {err}\n")

                        aborted = True

                        continue

                    if len_possible_types == 0:

                        _ar = ar.copy()

                        if len_valid_types == 1:
                            _ar['file_name'] = dst_file
                            _ar['file_type'] = valid_types[0]
                            split_file_list.append(_ar)

                            mr_part_paths.append({_ar['file_type']: dst_file})

                        elif len_valid_types == 2 and 'nm-res-cns' in valid_types and 'nm-res-xpl' in valid_types:
                            _ar['file_name'] = dst_file
                            _ar['file_type'] = 'nm-res-xpl'
                            split_file_list.append(_ar)

                            mr_part_paths.append({_ar['file_type']: dst_file})

                        elif len_valid_types == 2 and 'nm-res-cya' in valid_types:
                            _ar['file_name'] = dst_file
                            _ar['file_type'] = next(valid_type for valid_type in valid_types if valid_type != 'nm-res-cya')
                            split_file_list.append(_ar)

                            mr_part_paths.append({_ar['file_type']: dst_file})

                        elif len_valid_types == 2\
                                and set(valid_types) == {'nm-res-cya', 'nm-res-ros'}:
                            _ar['file_name'] = dst_file
                            _ar['file_type'] = 'nm-res-ros'
                            split_file_list.append(_ar)

                            mr_part_paths.append({_ar['file_type']: dst_file})

                        elif len_valid_types == 3\
                                and set(valid_types) in ({'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'},
                                                         {'nm-res-isd', 'nm-res-cns', 'nm-res-xpl'}):
                            _ar['file_name'] = dst_file
                            _ar['file_type'] = 'nm-res-xpl'
                            split_file_list.append(_ar)

                            mr_part_paths.append({_ar['file_type']: dst_file})

                        elif len_valid_types == 3\
                                and set(valid_types) == {'nm-res-cha', 'nm-res-cns', 'nm-res-xpl'}:
                            _ar['file_name'] = dst_file
                            _ar['file_type'] = 'nm-res-cha'
                            split_file_list.append(_ar)

                            mr_part_paths.append({_ar['file_type']: dst_file})

                        elif len_valid_types == 3\
                                and set(valid_types) == {'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'}:
                            _ar['file_name'] = dst_file
                            _ar['file_type'] = 'nm-res-xpl'
                            split_file_list.append(_ar)

                        else:
                            _ar['file_name'] = dst_file
                            _ar['file_type'] = valid_types[0]
                            split_file_list.append(_ar)

                            err = f"The restraint file {file_name!r} (MR format) is identified as {valid_types}. "\
                                "@todo: It needs to be split properly."

                            self.__reg.report.error.appendDescription('internal_error',
                                                                      f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                                      "++ Error  - " + err)

                            if self.__reg.verbose:
                                self.__reg.log.write(f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                     f"++ Error  - {err}\n")

                            aborted = True

                    elif len_valid_types == 0:

                        _ar = ar.copy()

                        _ar['file_name'] = dst_file
                        _ar['file_type'] = possible_types[0]
                        split_file_list.append(_ar)

                        err = f"The restraint file {file_name!r} (MR format) can be {possible_types}. "\
                            "@todo: It needs to be reviewed."

                        self.__reg.report.error.appendDescription('internal_error',
                                                                  f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                                  "++ Error  - " + err)

                        if self.__reg.verbose:
                            self.__reg.log.write(f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                 f"++ Error  - {err}\n")

                        aborted = True

                    else:

                        _ar['file_name'] = dst_file
                        _ar['file_type'] = valid_types[0]
                        split_file_list.append(_ar)

                        err = f"The restraint file {file_name!r} (MR format) is identified as {valid_types} "\
                            f"and can be {possible_types} as well. @todo: It needs to be reviewed."

                        self.__reg.report.error.appendDescription('internal_error',
                                                                  f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                                  "++ Error  - " + err)

                        if self.__reg.verbose:
                            self.__reg.log.write(f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                 f"++ Error  - {err}\n")

                        aborted = True

            # has MR header
            else:

                original_file_path_list = []

                distinct = False
                ofh = ofh_w_sel = None
                j = 0

                with open(dst_file, 'r', encoding='utf-8') as ifh:
                    for line in ifh:

                        if PDB_MR_FILE_HEADER_PAT.match(line):
                            g = PDB_MR_FILE_HEADER_PAT.search(line).groups()

                            if ofh is not None:
                                if len(g[0]) > 0:
                                    j += 1
                                    ofh.write(g[0] + '\n')
                                ofh.close()
                                if j == 0:
                                    os.remove(original_file_path_list.pop())

                            j = 0
                            _dst_file = os.path.join(dir_path, g[2])
                            original_file_path_list.append(_dst_file)
                            ofh = open(_dst_file, 'w', encoding='utf-8')  # pylint: disable=consider-using-with
                            distinct = True

                        elif SEL_MR_FILE_HEADER_PAT.match(line)\
                                or SEL_PK_FILE_HEADER_PAT.match(line):
                            if SEL_MR_FILE_HEADER_PAT.match(line):
                                g = SEL_MR_FILE_HEADER_PAT.search(line).groups()
                            else:
                                g = SEL_PK_FILE_HEADER_PAT.search(line).groups()

                            if ofh is not None:
                                ofh.close()
                                if ofh_w_sel is not None:
                                    ofh_w_sel.close()
                                    ofh_w_sel = None
                                if j == 0:
                                    os.remove(original_file_path_list.pop())

                            j = 0
                            _dst_file = os.path.join(dir_path, g[1])
                            original_file_path_list.append(_dst_file)
                            ofh = open(_dst_file, 'w', encoding='utf-8')  # pylint: disable=consider-using-with
                            _dst_file_w_sel = self.testPath(_dst_file + f'-selected-as-{g[0][-7:]}', True)
                            ofh_w_sel = open(_dst_file_w_sel, 'w', encoding='utf-8')  # pylint: disable=consider-using-with
                            distinct = True

                        elif SEL_CS_FILE_HEADER_PAT.match(line):
                            g = SEL_CS_FILE_HEADER_PAT.search(line).groups()

                            if ofh is not None:
                                ofh.close()
                                if ofh_w_sel is not None:
                                    ofh_w_sel.close()
                                    ofh_w_sel = None
                                if j == 0:
                                    os.remove(original_file_path_list.pop())

                            j = 0
                            _dst_file = os.path.join(dir_path, g[1])
                            original_file_path_list.append(_dst_file)
                            ofh = open(_dst_file, 'w', encoding='utf-8')  # pylint: disable=consider-using-with
                            _dst_file_w_sel = self.testPath(_dst_file + '-ignored', True)
                            ofh_w_sel = open(_dst_file_w_sel, 'w', encoding='utf-8')  # pylint: disable=consider-using-with
                            distinct = True

                        elif not line.isspace() and not COMMENT_PAT.match(line):
                            j += 1
                            if ofh is None:
                                _dst_file = os.path.join(dir_path, src_basename + '-noname.mr')
                                original_file_path_list.append(_dst_file)
                                ofh = open(_dst_file, 'w', encoding='utf-8')  # pylint: disable=consider-using-with
                            ofh.write(line)
                            if ofh_w_sel is not None:
                                ofh_w_sel.write(line)

                        elif ofh is not None:
                            ofh.write(line)
                            if ofh_w_sel is not None:
                                ofh_w_sel.write(line)

                if ofh is not None:
                    ofh.close()
                    if j == 0:
                        os.remove(original_file_path_list.pop())
                    if ofh_w_sel is not None:
                        ofh_w_sel.close()

                if len(original_file_path_list) == 0:
                    distinct = False
                    original_file_path_list.append(dst_file)

                for dst_file in original_file_path_list:
                    ign_dst_file = self.testPathWithSuffix(dst_file, '-ignored', True)

                    if os.path.exists(ign_dst_file):  # in case the MR file can be ignored
                        remediated = True
                        continue

                    split_ext = os.path.splitext(dst_file)

                    if len(split_ext) == 2:
                        if len(split_ext[1]) > 0:
                            file_ext = split_ext[1][1:].lower()
                        else:
                            file_ext = os.path.basename(split_ext[0]).lower()
                    else:
                        file_ext = os.path.basename(split_ext[0]).lower()

                    # AMBER coordinate file extensions
                    if file_ext in ('x', 'rc', 'crd', 'rst', 'inp', 'inpcrd', 'restrt')\
                       or 'rc' in file_ext or 'crd' in file_ext or 'rst' in file_ext or 'inp' in file_ext:
                        is_crd = False
                        with open(dst_file, 'r', encoding='utf-8') as ifh:
                            for pos, line in enumerate(ifh, start=1):
                                if pos == 1:
                                    if line.isdigit():
                                        break
                                elif pos == 2:
                                    try:
                                        int(line.lstrip().split()[0])
                                    except (ValueError, IndexError):
                                        break
                                elif pos == 3:
                                    if line.count('.') == 6:
                                        is_crd = True
                                    break

                        if is_crd:
                            shutil.copyfile(dst_file, ign_dst_file)  # ignore AMBER input coordinate file for the next time
                            remediated = True
                            continue

                    if file_ext in ('frc', 'known') or 'frc' in file_ext:
                        is_frc = False
                        with open(dst_file, 'r', encoding='utf-8') as ifh:
                            for pos, line in enumerate(ifh, start=1):
                                if pos == 1:
                                    if not line.startswith('FRCMOD'):
                                        break
                                elif pos == 2:
                                    if line.startswith('MASS'):
                                        is_frc = True
                                    break

                        if is_frc:
                            shutil.copyfile(dst_file, ign_dst_file)  # ignore AMBER frcmod file for the next time
                            remediated = True
                            continue

                    if file_ext == 'seq':
                        is_seq = False
                        _len_seq = None
                        with open(dst_file, 'r', encoding='utf-8') as ifh:
                            for line in ifh:
                                if line.isspace() or COMMENT_PAT.match(line):
                                    continue
                                seq = line.upper().split()
                                len_seq = len(seq)
                                if len_seq > 2:
                                    is_seq = False
                                    break
                                if _len_seq is None:
                                    _len_seq = len_seq
                                elif len_seq != _len_seq:
                                    is_seq = False
                                    break
                                if len_seq == 2:
                                    if (translateToStdResName(seq[0], ccU=self.__reg.ccU) in STD_MON_DICT and seq[1].isdigit())\
                                       or (translateToStdResName(seq[1], ccU=self.__reg.ccU) in STD_MON_DICT and seq[0].isdigit()):
                                        is_seq = True
                                    else:
                                        is_seq = False
                                        break
                                elif len_seq == 1:
                                    if seq[0] in STD_MON_DICT:
                                        is_seq = True
                                    else:
                                        is_seq = False
                                        break

                        if is_seq:
                            shutil.copyfile(dst_file, ign_dst_file)  # ignore sequence file for the next time
                            remediated = True
                            continue

                    if file_ext == 'cor':
                        is_cor = False
                        with open(dst_file, 'r', encoding='utf-8') as ifh:
                            for pos, line in enumerate(ifh, start=1):
                                if pos == 1:
                                    if 'Structures from CYANA' not in line:
                                        break
                                elif pos == 2:
                                    if 'CYANA' not in line:
                                        break
                                elif pos == 3:
                                    if line.count('Number') < 3:
                                        break
                                elif pos == 4:
                                    if line.count('.') >= 3:
                                        is_cor = True
                                    break

                        if is_cor:
                            shutil.copyfile(dst_file, ign_dst_file)  # ignore CYANA coordinate file for the next time
                            remediated = True
                            continue

                    ign_pk_file = self.testPathWithSuffix(dst_file, '-ignored-as-pea-any', True)

                    if os.path.exists(ign_pk_file):  # in case the MR file can be ignored as peak list file

                        settled_file_type, _ = self.__getPeakListFileTypeAndContentSubtype(ign_pk_file)

                        _ar = ar.copy()

                        if settled_file_type is not None:
                            sel_pk_file = self.testPath(dst_file + f'-selected-as-{settled_file_type[-7:]}', True)
                            os.rename(ign_pk_file, sel_pk_file)

                            _ar['file_name'] = dst_file
                            _ar['file_type'] = settled_file_type

                        else:

                            _ar['file_name'] = dst_file
                            _ar['file_type'] = 'nm-pea-any'

                        if distinct:
                            _ar['original_file_name'] = os.path.basename(dst_file)

                        peak_file_list.append(_ar)

                        pk_list_paths.append({'nmr-peaks': dst_file,
                                              'original_file_name':
                                              None if dst_file.endswith('-noname.mr') else os.path.basename(dst_file)})

                        remediated = True

                        continue

                    settled_pk_file = False

                    _ar = ar.copy()

                    for settled_file_type in PARSABLE_PK_FILE_TYPES:

                        sel_pk_file = self.testPathWithSuffix(dst_file, f'-selected-as-{settled_file_type[-7:]}', True)

                        if os.path.exists(sel_pk_file):

                            ign_dst_file = self.testPathWithSuffix(sel_pk_file, '-ignored', True)

                            if os.path.exists(ign_dst_file):
                                continue

                            __ar = _ar.copy()

                            __ar['file_name'] = sel_pk_file
                            __ar['file_type'] = settled_file_type

                            if __ar in peak_file_list:
                                continue

                            peak_file_list.append(__ar)

                            pk_list_paths.append({'nmr-peaks': dst_file})

                            settled_pk_file = remediated = True

                    if settled_pk_file:
                        continue

                    ign_ext_file = self.testPathWithSuffix(dst_file, '-ignored-as-res-oth', True)

                    if os.path.exists(ign_ext_file):  # in case the MR files can not be parsed
                        _ar = ar.copy()

                        _ar['file_name'] = dst_file
                        _ar['file_type'] = 'nm-res-oth'

                        if distinct:
                            _ar['original_file_name'] = os.path.basename(dst_file)

                        split_file_list.append(_ar)

                        mr_part_paths.append({_ar['file_type']: dst_file,
                                              'original_file_name':
                                              None if dst_file.endswith('-noname.mr') else os.path.basename(dst_file)})

                        continue

                    designated = False

                    for _file_type in settled_file_types:

                        sel_file = self.testPathWithSuffix(dst_file, f'-selected-as-{_file_type[-7:]}', True)

                        if os.path.exists(sel_file):
                            _ar = ar.copy()

                            _ar['file_name'] = dst_file
                            _ar['file_type'] = _file_type

                            if distinct:
                                _ar['original_file_name'] = os.path.basename(dst_file)

                            split_file_list.append(_ar)

                            mr_part_paths.append({_file_type: dst_file,
                                                  'original_file_name':
                                                  None if dst_file.endswith('-noname.mr') else os.path.basename(dst_file)})

                            designated = True

                            break

                    if designated:
                        continue

                    cor_dst_file = self.testPathWithSuffix(dst_file, '-corrected')

                    if os.path.exists(cor_dst_file):  # in case manually corrected MR file exists
                        dst_file = cor_dst_file

                        remediated = True

                    settled_file_type, _ = self.__getPeakListFileTypeAndContentSubtype(dst_file)

                    if settled_file_type is not None:

                        os.symlink(dst_file, self.testPath(dst_file + f'-selected-as-{settled_file_type[-7:]}', True))

                        _ar = ar.copy()

                        _ar['file_name'] = dst_file
                        _ar['file_type'] = settled_file_type

                        if distinct:
                            _ar['original_file_name'] = os.path.basename(dst_file)

                        peak_file_list.append(_ar)

                        pk_list_paths.append({'nmr-peaks': dst_file,
                                              'original_file_name':
                                              None if dst_file.endswith('-noname.mr') else os.path.basename(dst_file)})

                        remediated = True

                        continue

                    if has_str_format or has_cif_format:

                        dst_file_type = get_type_of_star_file(dst_file)

                        if dst_file_type == 'str':

                            mrPath = dst_file

                            item = {'file_name': mrPath,
                                    'file_type': 'nmr-star',
                                    'original_file_name': f'{os.path.basename(src_basename)}.mr'}

                            if MR_FILE_PATH_LIST_KEY not in self.__reg.inputParamDict:
                                self.__reg.inputParamDict[MR_FILE_PATH_LIST_KEY] = [item]
                            else:
                                self.__reg.inputParamDict[MR_FILE_PATH_LIST_KEY].append(item)

                            insert_index = self.__reg.file_path_list_len

                            if insert_index > len(self.__reg.star_data):
                                self.__reg.star_data.append(None)
                                self.__reg.star_data_type.append(None)

                            self.__reg.report.insertInputSource(insert_index)

                            self.__reg.file_path_list_len += 1

                            input_source = self.__reg.report.input_sources[insert_index]

                            file_type = 'nmr-star'
                            file_name = os.path.basename(mrPath)

                            input_source.setItemValue('file_name', file_name)
                            input_source.setItemValue('file_type', file_type)
                            input_source.setItemValue('content_type', 'nmr-restraints')
                            input_source.setItemValue('original_file_name', f'{os.path.basename(src_basename)}.mr')

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

                            file_subtype = 'O'

                            is_valid, message = self.__reg.nefT.validate_file(mrPath, file_subtype)

                            if not is_valid or not self.__reg.has_star_chem_shift:
                                _is_valid, _ = self.__reg.nefT.validate_file(mrPath, 'S')
                                if _is_valid:
                                    has_cs_str = True

                            self.__reg.original_error_message.append(message)

                            _file_type = message['file_type']  # nef/nmr-star/unknown

                            if is_valid:

                                if _file_type != file_type:

                                    err = f"{file_name!r} was selected as {READABLE_FILE_TYPE[file_type]} file, "\
                                        f"but recognized as {READABLE_FILE_TYPE[_file_type]} file."
                                    # DAOTHER-5673
                                    err += " Please re-upload the NEF file as an NMR unified data file."\
                                        if _file_type == 'nef' else " Please re-upload the file."

                                    if len(message['error']) > 0:
                                        for err_message in message['error']:
                                            if 'No such file or directory' not in err_message:
                                                err += ' ' + re.sub('not in list', 'unknown item.', err_message)

                                    self.__reg.report.error.appendDescription('content_mismatch',
                                                                              {'file_name': file_name, 'description': err})

                                    if self.__reg.verbose:
                                        self.__reg.log.write(f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                             f"++ Error  - {err}\n")

                                else:

                                    _is_done, star_data_type, star_data = self.__reg.nefT.read_input_file(mrPath)

                                    self.__reg.has_legacy_sf_issue = False

                                    if star_data_type == 'Saveframe':
                                        self.__reg.has_legacy_sf_issue = True

                                        self.__reg.dpA.fixFormatIssueOfInputSource(insert_index, file_name, file_type,
                                                                                   mrPath, file_subtype, message,
                                                                                   hasLegacySfIssue=self.__reg.has_legacy_sf_issue)

                                        _is_done, star_data_type, star_data = self.__reg.nefT.read_input_file(mrPath)

                                    if not (self.__reg.has_legacy_sf_issue and _is_done and star_data_type == 'Entry'):

                                        if len(self.__reg.star_data_type) == self.__reg.file_path_list_len:
                                            del self.__reg.star_data_type[-1]
                                            del self.__reg.star_data[-1]

                                        self.__reg.star_data_type.append(star_data_type)
                                        self.__reg.star_data.append(star_data)

                                        self.__reg.dpA.rescueFormerNef(insert_index)
                                        self.__reg.dpA.rescueImmatureStr(insert_index)

                                    if _is_done:
                                        self.__reg.dpV.detectContentSubType__(insert_index, input_source, dir_path)
                                        input_source_dic = input_source.get()
                                        if 'content_subtype' in input_source_dic:
                                            content_subtype = input_source_dic['content_subtype']
                                            if any(True for mr_content_subtype in self.__reg.mr_content_subtypes
                                                   if mr_content_subtype in content_subtype):
                                                mr_part_paths.append({'nmr-star': mrPath,
                                                                      'original_file_name':
                                                                      None if dst_file.endswith('-noname.mr')
                                                                      else os.path.basename(dst_file)})

                            else:

                                if not self.__reg.dpA.fixFormatIssueOfInputSource(insert_index, file_name, file_type,
                                                                                  mrPath, file_subtype, message,
                                                                                  hasLegacySfIssue=self.__reg.has_legacy_sf_issue):
                                    _is_done = False

                            if _mrPath is not None:
                                try:
                                    os.remove(_mrPath)
                                except OSError:
                                    pass

                            # release cached input data on NefTranslator because there is no chance
                            # to read the same file hereafter
                            self.__reg.nefT.release()

                            continue

                        if dst_file_type == 'cif':

                            mrPath = dst_file

                            _mrPath = self.getNextPath(os.path.splitext(mrPath)[0], '.cif2str')
                            if not self.__reg.c2S.convert(mrPath, _mrPath):
                                _mrPath = mrPath

                            mrPath = _mrPath

                            item = {'file_name': mrPath,
                                    'file_type': 'nmr-star',
                                    'original_file_name': f'{os.path.basename(src_basename)}.mr'}

                            if MR_FILE_PATH_LIST_KEY not in self.__reg.inputParamDict:
                                self.__reg.inputParamDict[MR_FILE_PATH_LIST_KEY] = [item]
                            else:
                                self.__reg.inputParamDict[MR_FILE_PATH_LIST_KEY].append(item)

                            insert_index = self.__reg.file_path_list_len

                            if insert_index > len(self.__reg.star_data):
                                self.__reg.star_data.append(None)
                                self.__reg.star_data_type.append(None)

                            self.__reg.report.insertInputSource(insert_index)

                            self.__reg.file_path_list_len += 1

                            input_source = self.__reg.report.input_sources[insert_index]

                            file_type = 'nmr-star'
                            file_name = os.path.basename(mrPath)

                            input_source.setItemValue('file_name', re.sub(r'\.cif2str$', '', file_name))
                            input_source.setItemValue('file_type', file_type)
                            input_source.setItemValue('content_type', 'nmr-restraints')
                            input_source.setItemValue('original_file_name', f'{os.path.basename(src_basename)}.mr')

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

                            file_subtype = 'O'

                            is_valid, message = self.__reg.nefT.validate_file(mrPath, file_subtype)

                            if not is_valid or not self.__reg.has_star_chem_shift:
                                _is_valid, _ = self.__reg.nefT.validate_file(mrPath, 'S')
                                if _is_valid:
                                    has_cs_str = True

                            self.__reg.original_error_message.append(message)

                            _file_type = message['file_type']  # nef/nmr-star/unknown

                            if is_valid:

                                if _file_type != file_type:

                                    err = f"{file_name!r} was selected as {READABLE_FILE_TYPE[file_type]} file, "\
                                        f"but recognized as {READABLE_FILE_TYPE[_file_type]} file."
                                    # DAOTHER-5673
                                    err += " Please re-upload the NEF file as an NMR unified data file."\
                                        if _file_type == 'nef' else " Please re-upload the file."

                                    if len(message['error']) > 0:
                                        for err_message in message['error']:
                                            if 'No such file or directory' not in err_message:
                                                err += ' ' + re.sub('not in list', 'unknown item.', err_message)

                                    self.__reg.report.error.appendDescription('content_mismatch',
                                                                              {'file_name': file_name, 'description': err})

                                    if self.__reg.verbose:
                                        self.__reg.log.write(f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                             f"++ Error  - {err}\n")

                                else:

                                    _is_done, star_data_type, star_data = self.__reg.nefT.read_input_file(mrPath)

                                    self.__reg.has_legacy_sf_issue = False

                                    if star_data_type == 'Saveframe':
                                        self.__reg.has_legacy_sf_issue = True

                                        self.__reg.dpA.fixFormatIssueOfInputSource(insert_index, file_name, file_type,
                                                                                   mrPath, file_subtype, message,
                                                                                   hasLegacySfIssue=self.__reg.has_legacy_sf_issue)

                                        _is_done, star_data_type, star_data = self.__reg.nefT.read_input_file(mrPath)

                                    if not (self.__reg.has_legacy_sf_issue and _is_done and star_data_type == 'Entry'):

                                        if len(self.__reg.star_data_type) == self.__reg.file_path_list_len:
                                            del self.__reg.star_data_type[-1]
                                            del self.__reg.star_data[-1]

                                        self.__reg.star_data_type.append(star_data_type)
                                        self.__reg.star_data.append(star_data)

                                        self.__reg.dpA.rescueFormerNef(insert_index)
                                        self.__reg.dpA.rescueImmatureStr(insert_index)

                                    if _is_done:
                                        self.__reg.dpV.detectContentSubType()
                                        input_source_dic = input_source.get()
                                        if 'content_subtype' in input_source_dic:
                                            content_subtype = input_source_dic['content_subtype']
                                            if any(True for mr_content_subtype in self.__reg.mr_content_subtypes
                                                   if mr_content_subtype in content_subtype):
                                                mr_part_paths.append({'nmr-star': mrPath,
                                                                      'original_file_name':
                                                                      None if dst_file.endswith('-noname.mr')
                                                                      else os.path.basename(dst_file)})

                            else:

                                if not self.__reg.dpA.fixFormatIssueOfInputSource(insert_index, file_name, file_type,
                                                                                  mrPath, file_subtype, message,
                                                                                  hasLegacySfIssue=self.__reg.has_legacy_sf_issue):
                                    _is_done = False

                            if _mrPath is not None:
                                try:
                                    os.remove(_mrPath)
                                except OSError:
                                    pass

                            # release cached input data on NefTranslator because there is no chance
                            # to read the same file hereafter
                            self.__reg.nefT.release()

                            continue

                    file_name = os.path.basename(dst_file)

                    dst_file_list = [os.path.join(dir_path, div_name) for div_name in div_file_names
                                     if div_name.startswith(file_name)]

                    if len(dst_file_list) == 0:
                        dst_file_list.append(dst_file)

                    for _dst_file in dst_file_list:

                        ign_pk_file = self.testPathWithSuffix(_dst_file, '-ignored-as-pea-any', True)

                        if os.path.exists(ign_pk_file):  # in case the MR file can be ignored as peak list file

                            settled_file_type, _ = self.__getPeakListFileTypeAndContentSubtype(ign_pk_file)

                            _ar = ar.copy()

                            if settled_file_type is not None:
                                sel_pk_file = self.testPath(_dst_file + f'-selected-as-{settled_file_type[-7:]}', True)
                                os.rename(ign_pk_file, sel_pk_file)

                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = settled_file_type

                            else:

                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = 'nm-pea-any'

                            if distinct:
                                _ar['original_file_name'] = file_name

                            peak_file_list.append(_ar)

                            pk_list_paths.append({'nmr-peaks': _dst_file,
                                                  'original_file_name':
                                                  None if file_name.endswith('-noname.mr') else file_name})

                            remediated = True

                            continue

                        designated = False

                        for _file_type in settled_file_types:

                            sel_file = self.testPathWithSuffix(_dst_file, f'-selected-as-{_file_type[-7:]}', True)

                            if os.path.exists(sel_file):
                                _ar = ar.copy()

                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = _file_type

                                if distinct:
                                    _ar['original_file_name'] = file_name

                                split_file_list.append(_ar)

                                mr_part_paths.append({_file_type: _dst_file,
                                                      'original_file_name':
                                                      None if file_name.endswith('-noname.mr') else file_name})

                                designated = True

                                break

                        if designated:
                            continue

                        if _dst_file.endswith('-div_ext.mr'):
                            _ar = ar.copy()

                            _ar['file_name'] = _dst_file
                            _ar['file_type'] = 'nm-res-oth'

                            if distinct:
                                _ar['original_file_name'] = file_name

                            split_file_list.append(_ar)

                            mr_part_paths.append({_ar['file_type']: _dst_file,
                                                  'original_file_name':
                                                  None if file_name.endswith('-noname.mr') else file_name})

                            continue

                        _, _, valid_types, possible_types =\
                            self.__detectOtherPossibleFormatAsErrorOfLegacyMr(_dst_file, file_name, 'nm-res-mr', [], True)

                        len_valid_types = len(valid_types)
                        len_possible_types = len(possible_types)

                        if self.__reg.mr_debug:
                            self.__reg.log.write(f'{valid_types} {possible_types}\n')

                        if len_valid_types == 0 and len_possible_types == 0:

                            ins_msg = ''
                            if not distinct or len(original_file_path_list) == 1:
                                if has_pdb_format and has_cs_str:
                                    ins_msg = 'unexpectedly contains PDB coordinates and assigned chemical shifts, but '
                                elif has_pdb_format:
                                    ins_msg = 'unexpectedly contains PDB coordinates, but '
                                elif has_cs_str:
                                    ins_msg = 'unexpectedly contains assigned chemical shifts, but '

                            _file_name = file_name
                            if file_name != _file_name:
                                _file_name = f'({_file_name}) '
                            else:
                                _file_name = ''

                            err = f"The restraint file {file_name!r} {_file_name}{ins_msg}does not match with "\
                                "any known restraint format. "\
                                "@todo: It needs to be reviewed or marked as entry without restraints."

                            self.__reg.report.error.appendDescription('internal_error',
                                                                      {'file_name': file_name, 'description': err})

                            if self.__reg.verbose:
                                self.__reg.log.write(f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                     f"++ Error  - {err}\n")

                            aborted = True

                            continue

                        if len_possible_types == 0:

                            _ar = ar.copy()

                            if len_valid_types == 1:
                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = valid_types[0]

                                if distinct:
                                    _ar['original_file_name'] = file_name

                                split_file_list.append(_ar)

                                mr_part_paths.append({_ar['file_type']: _dst_file,
                                                      'original_file_name':
                                                      None if _dst_file.endswith('-noname.mr') else file_name})

                            elif len_valid_types == 2 and 'nm-res-cns' in valid_types and 'nm-res-xpl' in valid_types:
                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = 'nm-res-xpl'

                                if distinct:
                                    _ar['original_file_name'] = file_name

                                split_file_list.append(_ar)

                                mr_part_paths.append({_ar['file_type']: _dst_file,
                                                      'original_file_name':
                                                      None if _dst_file.endswith('-noname.mr') else file_name})

                            elif len_valid_types == 2 and 'nm-res-cya' in valid_types:
                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = next(valid_type for valid_type in valid_types if valid_type != 'nm-res-cya')

                                if distinct:
                                    _ar['original_file_name'] = file_name

                                split_file_list.append(_ar)

                                mr_part_paths.append({_ar['file_type']: _dst_file,
                                                      'original_file_name':
                                                      None if _dst_file.endswith('-noname.mr') else file_name})

                            elif len_valid_types == 2\
                                    and set(valid_types) == {'nm-res-cya', 'nm-res-ros'}:
                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = 'nm-res-ros'

                                if distinct:
                                    _ar['original_file_name'] = file_name

                                split_file_list.append(_ar)

                                mr_part_paths.append({_ar['file_type']: _dst_file,
                                                      'original_file_name':
                                                      None if _dst_file.endswith('-noname.mr') else file_name})

                            elif len_valid_types == 3\
                                    and set(valid_types) in ({'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'},
                                                             {'nm-res-isd', 'nm-res-cns', 'nm-res-xpl'}):
                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = 'nm-res-xpl'

                                if distinct:
                                    _ar['original_file_name'] = file_name

                                split_file_list.append(_ar)

                                mr_part_paths.append({_ar['file_type']: _dst_file,
                                                      'original_file_name':
                                                      None if _dst_file.endswith('-noname.mr') else file_name})

                            elif len_valid_types == 3\
                                    and set(valid_types) == {'nm-res-cha', 'nm-res-cns', 'nm-res-xpl'}:
                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = 'nm-res-cha'

                                if distinct:
                                    _ar['original_file_name'] = file_name

                                split_file_list.append(_ar)

                                mr_part_paths.append({_ar['file_type']: _dst_file,
                                                      'original_file_name':
                                                      None if _dst_file.endswith('-noname.mr') else file_name})

                            elif len_valid_types == 3\
                                    and set(valid_types) == {'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'}:
                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = 'nm-res-xpl'

                                if distinct:
                                    _ar['original_file_name'] = file_name

                                split_file_list.append(_ar)

                                mr_part_paths.append({_ar['file_type']: _dst_file,
                                                      'original_file_name':
                                                      None if _dst_file.endswith('-noname.mr') else file_name})

                            else:
                                _ar['file_name'] = _dst_file
                                _ar['file_type'] = valid_types[0]

                                if distinct:
                                    _ar['original_file_name'] = file_name

                                err = f"The restraint file {file_name!r} (MR format) is identified as {valid_types}. "\
                                    "@todo: It needs to be split properly."

                                self.__reg.report.error.appendDescription('internal_error',
                                                                          f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "  # noqa: E501, pylint: disable=line-too-long
                                                                          "++ Error  - " + err)

                                if self.__reg.verbose:
                                    self.__reg.log.write(f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                         f"++ Error  - {err}\n")

                                aborted = True

                        elif len_valid_types == 0:

                            _ar['file_name'] = _dst_file
                            _ar['file_type'] = possible_types[0]

                            if distinct:
                                _ar['original_file_name'] = file_name

                            err = f"The restraint file {file_name!r} (MR format) can be {possible_types}. "\
                                "@todo: It needs to be reviewed."

                            self.__reg.report.error.appendDescription('internal_error',
                                                                      f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                                      "++ Error  - " + err)

                            if self.__reg.verbose:
                                self.__reg.log.write(f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                     f"++ Error  - {err}\n")

                            aborted = True

                        else:

                            _ar['file_name'] = _dst_file
                            _ar['file_type'] = valid_types[0]

                            if distinct:
                                _ar['original_file_name'] = file_name

                            err = f"The restraint file {file_name!r} (MR format) is identified as {valid_types} "\
                                f"and can be {possible_types} as well. "\
                                "@todo: It needs to be reviewed."

                            self.__reg.report.error.appendDescription('internal_error',
                                                                      f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                                      "++ Error  - " + err)

                            if self.__reg.verbose:
                                self.__reg.log.write(f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                     f"++ Error  - {err}\n")

                            aborted = True

        len_peak_file_list = len(peak_file_list)
        has_spectral_peak = len_peak_file_list > 0

        if len(split_file_list) > 0:
            self.__reg.inputParamDict[AR_FILE_PATH_LIST_KEY].extend(split_file_list)

            for _ar in split_file_list:

                self.__reg.report.appendInputSource()

                input_source = self.__reg.report.input_sources[-1]

                input_source.setItemValue('file_name', os.path.basename(_ar['file_name']))
                input_source.setItemValue('file_type', _ar['file_type'])
                input_source.setItemValue('content_type', 'nmr-restraints')
                if 'original_file_name' in _ar:
                    input_source.setItemValue('original_file_name', os.path.basename(_ar['original_file_name']))

        else:

            has_restraint = False

            for fileListId in range(self.__reg.file_path_list_len):

                input_source = self.__reg.report.input_sources[fileListId]
                input_source_dic = input_source.get()

                file_name = input_source_dic['file_name']
                file_type = input_source_dic['file_type']
                content_type = input_source_dic['content_type']

                if content_type != 'nmr-restraints':
                    continue

                content_subtype = input_source_dic['content_subtype']

                if content_subtype is None:
                    continue

                has_restraint = 'dist_restraint' in content_subtype or 'dihed_restraint' in content_subtype\
                    or 'rdc_restraint' in content_subtype
                has_spectral_peak = 'spectral_peak' in content_subtype or 'spectral_peak_alt' in content_subtype

            if not has_restraint:

                if mr_file_name == '.':

                    rem_dir = os.path.join(dir_path, 'remediation')

                    if os.path.isdir(rem_dir):

                        try:
                            os.rmdir(rem_dir)
                        except OSError:
                            pass

                elif not self.__reg.mr_has_valid_star_restraint:

                    touch_file = os.path.join(dir_path, '.entry_without_mr')
                    if not os.path.exists(self.testPath(touch_file)):
                        with open(touch_file, 'w', encoding='utf-8') as ofh:
                            ofh.write('')

                    if not any(re.search(r'\/bmr\d+\/work\/data\/', ar['file_name'])
                               for ar in self.__reg.inputParamDict[AR_FILE_PATH_LIST_KEY]
                               if ar['file_type'].startswith('nm-res') and ar['file_type'] != 'nm-res-mr'):

                        hint = ' or is not recognized properly'

                        if len_peak_file_list > 0:
                            hint = f', except for {len_peak_file_list} peak list file(s)'

                        err = f"The restraint file contains no restraints{hint}. "\
                            "Please re-upload the restraint file."

                        self.__reg.suspended_errors_for_lazy_eval.append({'content_mismatch':
                                                                          {'file_name': mr_file_name, 'description': err}})

                        if self.__reg.verbose:
                            self.__reg.log.write(f"+{self.__class_name__}.extractPublicMrFileIntoLegacyMr() "
                                                 f"++ Error  - {err}\n")

        if has_spectral_peak:

            if len_peak_file_list > 0:

                self.__reg.inputParamDict[AR_FILE_PATH_LIST_KEY].extend(peak_file_list)

                for _ar in peak_file_list:

                    self.__reg.report.appendInputSource()

                    input_source = self.__reg.report.input_sources[-1]

                    input_source.setItemValue('file_name', os.path.basename(_ar['file_name']))
                    input_source.setItemValue('file_type', _ar['file_type'])
                    input_source.setItemValue('content_type', 'nmr-peaks')
                    if 'original_file_name' in _ar:
                        input_source.setItemValue('original_file_name', os.path.basename(_ar['original_file_name']))

            touch_file = os.path.join(dir_path, '.entry_with_pk')
            if not os.path.exists(self.testPath(touch_file)):
                with open(touch_file, 'w', encoding='utf-8') as ofh:
                    ofh.write('')

        if not aborted and remediated and mr_file_path is not None:
            with open(mr_file_path, 'w', encoding='utf-8') as ofh:

                header_file = next(mr_part_path['header'] for mr_part_path in mr_part_paths if 'header' in mr_part_path)
                with open(header_file, 'r', encoding='utf-8') as ifh:
                    for line in ifh:
                        ofh.write(line)

                file_idx = 1
                for mr_part_path in mr_part_paths:
                    if 'header' in mr_part_path or 'footer' in mr_part_path:
                        continue

                    for file_type in ARCHIVAL_MR_FILE_TYPES:
                        if file_type in mr_part_path:
                            file_path = mr_part_path[file_type]
                            if 'original_file_name' in mr_part_path and mr_part_path['original_file_name'] is not None:
                                original_file_name = mr_part_path['original_file_name']
                            else:
                                original_file_name = f'{os.path.basename(src_basename)}-division_P{file_idx}.mr'

                            ofh.write(f'# Restraints file {file_idx}: {original_file_name}\n')
                            ofh.write(f'# Restraint file format: {getRestraintFormatName(file_type).split()[0]}\n')

                            with open(file_path, 'r', encoding='utf-8') as ifh:
                                for line in ifh:
                                    ofh.write(line)

                            break

                    file_idx += 1

                if file_idx == 1 and len(split_file_list) > 0:

                    ofh.write(f'# Restraints file {file_idx}: {os.path.basename(src_basename)}.mr\n')
                    file_type = split_file_list[0]['file_type']
                    ofh.write(f'# Restraint file format: {getRestraintFormatName(file_type).split()[0]}\n')

                    with open(mr_core_path, 'r', encoding='utf-8') as ifh:
                        for line in ifh:
                            ofh.write(line)

                footer_file = next(mr_part_path['footer'] for mr_part_path in mr_part_paths if 'footer' in mr_part_path)
                with open(footer_file, 'r', encoding='utf-8') as ifh:
                    for line in ifh:
                        ofh.write(line)

            try:

                if os.path.exists(self.testPath(mr_file_link)):
                    os.remove(mr_file_link)

                os.symlink(mr_file_path, mr_file_link)

                if len(pk_list_paths) > 0:

                    pk_dir = os.path.join(dir_path, 'nmr_peak_lists')

                    try:

                        if not os.path.isdir(pk_dir):
                            os.makedirs(pk_dir)

                    except OSError:
                        pass

                    for pk_list_path in pk_list_paths:

                        pk_file_path = pk_list_path['nmr-peaks']
                        if 'original_file_name' in pk_list_path and pk_list_path['original_file_name'] is not None:
                            original_file_name = pk_list_path['original_file_name']

                        rem_pk_file_path = os.path.join(pk_dir, original_file_name)

                        if os.path.exists(self.testPath(rem_pk_file_path)):
                            os.remove(rem_pk_file_path)

                        os.symlink(pk_file_path, rem_pk_file_path)

            except OSError:
                pass

        return not self.__reg.report.isError()

    def __getPeakListFileTypeAndContentSubtype(self, file_path: str
                                               ) -> Tuple[Optional[str], Optional[dict]]:
        """ Return peak list file type and content subtype of a given file path.
        """

        file_type = get_peak_list_format(file_path, True)

        if file_type is not None:

            reader = self.getSimpleFileReader(file_type, False)

            listener, parser_err_listener, _ = reader.parse(file_path, None)

            # ignore lexer error because of incomplete XML file format
            # has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
            has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None
            content_subtype = listener.getContentSubtype() if listener is not None else None
            if not has_parser_error and content_subtype is not None and len(content_subtype) > 0:
                return file_type, content_subtype

        for file_type in PARSABLE_PK_FILE_TYPES:

            reader = self.getSimpleFileReader(file_type, False)

            listener, parser_err_listener, lexer_err_listener = reader.parse(file_path, None)

            has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
            has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None
            content_subtype = listener.getContentSubtype() if listener is not None else None
            if not has_lexer_error and not has_parser_error and content_subtype is not None and len(content_subtype) > 0:
                return file_type, content_subtype

        return None, None

    def __getCorrectedMrFilePath(self, src_path: str
                                 ) -> Tuple[Optional[str], bool]:
        """ Return corrected MR file path.
        """

        dir_path = os.path.dirname(src_path) if self.__reg.dirPath is None else self.__reg.dirPath

        for div_file_name in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, div_file_name))\
               and (div_file_name.endswith('-div_src.mr') or div_file_name.endswith('-div_dst.mr')):
                div_file_path = os.path.join(dir_path, div_file_name)
                if not any(True for ar in self.__reg.inputParamDict[AR_FILE_PATH_LIST_KEY] if ar['file_name'] == div_file_path):
                    os.remove(div_file_path)

        if os.path.exists(src_path):
            src_file_name = os.path.basename(src_path)
            cor_test = '-corrected' in src_file_name
            if cor_test:
                cor_src_path = f'{src_path}~'
            else:
                if src_path.endswith('.mr'):
                    cor_src_path = re.sub(r'\-trimmed$', '', os.path.splitext(src_path)[0]) + '-corrected.mr'
                else:
                    cor_src_path = re.sub(r'\-trimmed$', '', src_path) + '-corrected'

            return cor_src_path, cor_test

        return None, False

    def getSimpleFileReader(self, file_type: str, verbose: bool, sll_pred: bool = True, reasons: Optional[dict] = None) -> Any:
        """ Return simple file reader for a given format.
        """

        if file_type == 'nm-aux-amb':
            return AmberPTReader(verbose, self.__reg.log, None, None, None, None, None,
                                 self.__reg.ccU, self.__reg.csStat, self.__reg.nefT)
        if file_type == 'nm-aux-cha':
            return CharmmCRDReader(verbose, self.__reg.log, None, None, None, None, None,
                                   self.__reg.ccU, self.__reg.csStat, self.__reg.nefT)
        if file_type == 'nm-aux-gro':
            return GromacsPTReader(verbose, self.__reg.log, None, None, None, None, None,
                                   self.__reg.ccU, self.__reg.csStat, self.__reg.nefT)
        if file_type == 'nm-aux-pdb':
            return BarePDBReader(verbose, self.__reg.log, None, None, None, None, None,
                                 self.__reg.ccU, self.__reg.csStat, self.__reg.nefT)

        if file_type == 'nm-res-amb':
            return AmberMRReader(verbose, self.__reg.log, None, None, None, None, None,
                                 self.__reg.ccU, self.__reg.csStat, self.__reg.nefT)
        if file_type == 'nm-res-ari':
            return AriaMRReader(verbose, self.__reg.log, None, None, None, None, None,
                                self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                reasons)
        if file_type == 'nm-res-arx':
            return AriaMRXReader(verbose, self.__reg.log, None, None, None, None, None,
                                 self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                 reasons)
        if file_type == 'nm-res-bar':
            return BareMRReader(verbose, self.__reg.log, None, None, None, None, None,
                                self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                reasons)
        if file_type == 'nm-res-bio':
            return BiosymMRReader(verbose, self.__reg.log, None, None, None, None, None,
                                  self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                  reasons)
        if file_type == 'nm-res-cha':
            reader = CharmmMRReader(verbose, self.__reg.log, None, None, None, None, None,
                                    self.__reg.ccU, self.__reg.csStat, self.__reg.nefT)
            reader.setSllPredMode(sll_pred)
            return reader
        if file_type == 'nm-res-cns':
            reader = CnsMRReader(verbose, self.__reg.log, None, None, None, None, None,
                                 self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                 reasons)
            reader.setSllPredMode(sll_pred)
            return reader
        if file_type == 'nm-res-cya':
            reader = CyanaMRReader(verbose, self.__reg.log, None, None, None, None, None,
                                   self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                   reasons,
                                   file_ext=self.retrieveOriginalFileExtensionOfCyanaMrFile())
            reader.setRemediateMode(self.__reg.remediation_mode)
            # do not use SLL prediction mode for CyanaMRReader
            # reader.setSllPredMode(sll_pred)
            return reader
        if file_type == 'nm-res-dyn':
            return DynamoMRReader(verbose, self.__reg.log, None, None, None, None, None,
                                  self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                  reasons)
        if file_type == 'nm-res-gro':
            return GromacsMRReader(verbose, self.__reg.log, None, None, None, None, None,
                                   self.__reg.ccU, self.__reg.csStat, self.__reg.nefT)
        if file_type == 'nm-res-isd':
            return IsdMRReader(verbose, self.__reg.log, None, None, None, None, None,
                               self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                               reasons)
        if file_type == 'nm-res-noa':
            return CyanaNOAReader(verbose, self.__reg.log, None, None, None, None, None,
                                  self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                  reasons)
        if file_type == 'nm-res-ros':
            reader = RosettaMRReader(verbose, self.__reg.log, None, None, None, None, None,
                                     self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                     reasons)
            reader.setRemediateMode(self.__reg.remediation_mode)
            return reader
        if file_type == 'nm-res-sch':
            reader = SchrodingerMRReader(verbose, self.__reg.log, None, None, None, None, None,
                                         self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                         reasons)
            reader.setSllPredMode(sll_pred)
            return reader
        if file_type == 'nm-res-syb':
            return SybylMRReader(verbose, self.__reg.log, None, None, None, None, None,
                                 self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                 reasons)
        if file_type == 'nm-res-xpl':
            reader = XplorMRReader(verbose, self.__reg.log, None, None, None, None, None,
                                   self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                   reasons)
            reader.setSllPredMode(sll_pred)
            return reader

        if file_type == 'nm-aux-xea':
            reader = XeasyPROTReader(verbose, self.__reg.log, None, None, None, None, None,
                                     self.__reg.ccU, self.__reg.csStat, self.__reg.nefT)
            return reader

        if file_type == 'nm-pea-ari':
            reader = AriaPKReader(verbose, self.__reg.log, None, None, None, None, None,
                                  self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                  reasons)
            return reader
        if file_type == 'nm-pea-bar':
            reader = BarePKReader(verbose, self.__reg.log, None, None, None, None, None,
                                  self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                  reasons)
            return reader
        if file_type == 'nm-pea-ccp':
            reader = CcpnPKReader(verbose, self.__reg.log, None, None, None, None, None,
                                  self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                  reasons)
            return reader
        if file_type == 'nm-pea-oli':
            reader = OliviaPKReader(verbose, self.__reg.log, None, None, None, None, None,
                                    self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                    reasons)
            return reader
        if file_type == 'nm-pea-pip':
            reader = NmrPipePKReader(verbose, self.__reg.log, None, None, None, None, None,
                                     self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                     reasons)
            return reader
        if file_type == 'nm-pea-pon':
            reader = PonderosaPKReader(verbose, self.__reg.log, None, None, None, None, None,
                                       self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                       reasons)
            return reader
        if file_type == 'nm-pea-spa':
            reader = SparkyPKReader(verbose, self.__reg.log, None, None, None, None, None,
                                    self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                    reasons)
            return reader
        if file_type == 'nm-pea-sps':
            reader = SparkySPKReader(verbose, self.__reg.log, None, None, None, None, None,
                                     self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                     reasons)
            return reader
        if file_type == 'nm-pea-top':
            reader = TopSpinPKReader(verbose, self.__reg.log, None, None, None, None, None,
                                     self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                     reasons)
            return reader
        if file_type == 'nm-pea-vie':
            reader = NmrViewPKReader(verbose, self.__reg.log, None, None, None, None, None,
                                     self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                     reasons)
            return reader
        if file_type == 'nm-pea-vnm':
            reader = VnmrPKReader(verbose, self.__reg.log, None, None, None, None, None,
                                  self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                  reasons)
            return reader
        if file_type == 'nm-pea-xea':
            reader = XeasyPKReader(verbose, self.__reg.log, None, None, None, None, None,
                                   self.__reg.ccU, self.__reg.csStat, self.__reg.nefT)
            return reader
        if file_type == 'nm-pea-xwi':
            reader = XwinNmrPKReader(verbose, self.__reg.log, None, None, None, None, None,
                                     self.__reg.ccU, self.__reg.csStat, self.__reg.nefT,
                                     reasons)
            return reader

        return None

    def __divideLegacyMrIfNecessary(self, file_path: str, file_type: str, err_desc: dict, src_path: str, offset: int) -> bool:
        """ Divide legacy restraint file if necessary.
        """

        src_basename = os.path.splitext(file_path)[0]

        if self.__reg.dirPath is not None:
            src_basename = os.path.join(self.__reg.dirPath, os.path.basename(src_basename))

        div_src = 'div_dst' in src_basename
        div_src_file = src_basename + '-div_src.mr'
        div_ext_file = src_basename + '-div_ext.mr'
        div_try_file = src_basename + '-div_try.mr'
        div_dst_file = src_basename + '-div_dst.mr'

        if any(True for _err_desc in self.__reg.divide_mr_error_message
               if err_desc['file_path'] == _err_desc['file_path']
               and err_desc['line_number'] == _err_desc['line_number']
               and err_desc['column_position'] == _err_desc['column_position']
               and err_desc['message'] == _err_desc['message']):
            if os.path.exists(div_src_file):
                os.remove(div_src_file)
            if os.path.exists(div_dst_file):
                os.remove(div_dst_file)
            if os.path.exists(div_ext_file):
                os.remove(div_ext_file)
            return False

        self.__reg.divide_mr_error_message.append(err_desc)

        if self.__reg.mr_debug:
            self.__reg.log.write('DIV-MR\n')

        if file_type not in PARSABLE_MR_FILE_TYPES:
            return False

        err_message = err_desc['message']
        err_line_number = err_desc['line_number']
        err_column_position = err_desc['column_position']
        err_input = err_desc.get('input', '')

        xplor_file_type = file_type in ('nm-res-xpl', 'nm-res-cns')
        amber_file_type = file_type == 'nm-res-amb'
        gromacs_file_type = file_type in ('nm-res-gro', 'nm-aux-gro')

        xplor_missing_end = xplor_file_type and err_message.startswith(XPLOR_MISSING_END_ERR_MSG)
        xplor_ends_wo_statement = xplor_file_type and (bool(XPLOR_EXTRA_END_ERR_MSG_PAT.match(err_message))
                                                       or (err_message.startswith(NO_VIABLE_ALT_ERR_MSG)
                                                           and XPLOR_END_PAT.match(err_input)))

        xplor_assi_after_or_tag = xplor_file_type and bool(XPLOR_EXTRA_ASSI_ERR_MSG_PAT.match(err_message))
        xplor_assi_incompl_tag = xplor_file_type and bool(XPLOR_EXTRA_SSI_ERR_MSG_PAT.match(err_message))

        xplor_l_paren_wo_assi = xplor_file_type and bool(XPLOR_EXTRA_L_PAREN_ERR_MSG_PAT.match(err_message))
        xplor_00_origin = xplor_file_type and err_message.startswith(NO_VIABLE_ALT_ERR_MSG) and ' 00' in err_input

        amber_missing_end = amber_file_type and err_message.startswith(AMBER_MISSING_END_ERR_MSG)
        amber_ends_wo_statement = amber_file_type and (bool(AMBER_EXTRA_END_ERR_MSG_PAT.match(err_message))
                                                       or (err_message.startswith(NO_VIABLE_ALT_ERR_MSG)
                                                           and AMBER_END_PAT.match(err_input)))

        concat_xplor_assi = (xplor_file_type
                             and (err_message.startswith(MISMATCHED_INPUT_ERR_MSG)
                                  or err_message.startswith(EXTRANEOUS_INPUT_ERR_MSG))
                             and bool(XPLOR_ASSI_PAT.search(err_input))
                             and not bool(XPLOR_CLASS_PAT.search(err_input)))
        concat_xplor_rest = (xplor_file_type
                             and (err_message.startswith(MISMATCHED_INPUT_ERR_MSG)
                                  or err_message.startswith(EXTRANEOUS_INPUT_ERR_MSG))
                             and bool(XPLOR_REST_PAT.search(err_input)))
        concat_xplor_set = (xplor_file_type
                            and (err_message.startswith(MISMATCHED_INPUT_ERR_MSG)
                                 or err_message.startswith(EXTRANEOUS_INPUT_ERR_MSG))
                            and bool(XPLOR_SET_PAT.search(err_input))
                            and get_peak_list_format_from_string(err_input) is None)
        concat_amber_rst = (amber_file_type
                            and (err_message.startswith(MISMATCHED_INPUT_ERR_MSG)
                                 or err_message.startswith(EXTRANEOUS_INPUT_ERR_MSG))
                            and bool(AMBER_RST_PAT.search(err_input))
                            and not bool(AMBER_RST_PAT.match(err_input)))

        concat_gromacs_tag = not gromacs_file_type and bool(GROMACS_TAG_PAT.search(err_input))

        concat_comment = (file_type in LINEAR_MR_FILE_TYPES
                          and err_message.startswith(NO_VIABLE_ALT_ERR_MSG)
                          and bool(COMMENT_PAT.search(err_input)))

        if concat_xplor_assi and bool(XPLOR_ASSI_PAT.match(err_input)):
            if EXPECTING_L_PAREN in err_message:
                xplor_missing_end = True
                concat_xplor_assi = False
            if concat_xplor_rest or concat_xplor_set:
                concat_xplor_assi = False

        reader = prev_input = next_input = None

        if not (xplor_missing_end or xplor_ends_wo_statement
                or xplor_l_paren_wo_assi or xplor_00_origin
                or amber_missing_end or amber_ends_wo_statement
                or concat_xplor_assi or concat_xplor_rest or concat_xplor_set
                or concat_amber_rst
                or concat_gromacs_tag
                or concat_comment):

            if err_column_position > 0 and not err_input[0:err_column_position].isspace():
                test_line = err_input[0:err_column_position]

                if reader is None:
                    reader = self.getSimpleFileReader(file_type, False)

                _, parser_err_listener, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
                has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None

                if not has_lexer_error and not has_parser_error:

                    concat_input = err_input[err_column_position:]

                    if COMMENT_PAT.match(concat_input) or (len(concat_input) > 0 and concat_input[0].isalnum()):

                        if self.__reg.mr_debug:
                            self.__reg.log.write('DIV-MR-EXIT #1-1\n')

                        return self.__divideLegacyMr(file_path, file_type, err_desc, src_path, offset)

                    if self.__reg.mr_debug:
                        self.__reg.log.write('DIV-MR-EXIT #1-2\n')

                    return False

                # try to resolve unexpected concatenation
                test_line = err_input[err_column_position + 1:]

                if len(test_line) > 0:

                    _, parser_err_listener, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                    has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
                    has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None

                    if not has_lexer_error and not has_parser_error:
                        err_desc['column_position'] += 1

                        corrected = self.__divideLegacyMr(file_path, file_type, err_desc, src_path, offset)

                        if corrected and os.path.exists(src_path):

                            cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                            if cor_src_path is not None:

                                offset += err_line_number - 1

                                j = 0

                                with open(src_path, 'r', encoding='utf-8') as ifh, \
                                        open(cor_src_path, 'w', encoding='utf-8') as ofh:
                                    for line in ifh:
                                        if j == offset:
                                            ofh.write(line[:err_column_position + 1] + '\n')
                                            ofh.write(line[err_column_position + 1:])
                                        else:
                                            ofh.write(line)
                                        j += 1

                                if cor_test:
                                    os.rename(cor_src_path, src_path)

                                if self.__reg.mr_debug:
                                    self.__reg.log.write('DIV-MR-EXIT #2-1\n')

                            else:

                                if self.__reg.mr_debug:
                                    self.__reg.log.write('DIV-MR-EXIT #2-2\n')

                                corrected = False

                        else:

                            if self.__reg.mr_debug:
                                self.__reg.log.write('DIV-MR-EXIT #2-3\n')

                        return corrected

        i = j = j_offset = 0

        ws_or_comment = True

        interval = []

        with open(file_path, 'r', encoding='utf-8') as ifh, \
                open(div_src_file, 'w', encoding='utf-8') as ofh, \
                open(div_try_file, 'w', encoding='utf-8') as ofh2:
            for line in ifh:
                i += 1

                if i < err_line_number - MR_MAX_SPACER_LINES:
                    if ws_or_comment:
                        if line.isspace() or COMMENT_PAT.match(line)\
                           or (gromacs_file_type and GROMACS_COMMENT_PAT.match(line)):
                            pass
                        else:
                            ws_or_comment = False
                    ofh.write(line)
                    j += 1
                    continue
                if i < err_line_number:
                    if ws_or_comment:
                        if line.isspace() or COMMENT_PAT.match(line)\
                           or (gromacs_file_type and GROMACS_COMMENT_PAT.match(line)):
                            pass
                        else:
                            ws_or_comment = False
                    interval.append({'line': line,
                                     'ws_or_comment': line.isspace() or bool(COMMENT_PAT.match(line))
                                     or (gromacs_file_type and bool(GROMACS_COMMENT_PAT.match(line)))})
                    if i < err_line_number - 1:
                        continue
                    if i == err_line_number - 1:
                        prev_input = line
                    _k = len(interval) - 1
                    _c = interval[-1]['line'][0]
                    for _interval in reversed(interval):
                        c = _interval['line'][0]
                        if _interval['ws_or_comment'] and {c, _c} != COMMENT_CODE_MIXED_SET:
                            _c = c
                            _k -= 1
                            continue
                        break
                    for k, _interval in enumerate(interval):
                        if k <= _k:
                            ofh.write(_interval['line'])
                            j += 1
                        else:
                            ofh2.write(_interval['line'])
                            j_offset += 1
                    continue
                if i == err_line_number + 1:
                    next_input = line
                ofh2.write(line)

        offset += err_line_number - 1

        xplor_missing_end_before = (xplor_file_type and err_message.startswith(MISMATCHED_INPUT_ERR_MSG)
                                    and not bool(XPLOR_EXPECTNIG_SYMBOL_PAT.search(err_message))  # excl. syntax errors in a factor
                                    and prev_input is not None and bool(XPLOR_ASSI_PAT.search(prev_input)))

        xplor_no_syntax_err_in_fac_or_ann = not bool(XPLOR_EXPECTING_EQU_OP_PAT.search(err_message))\
            and not bool(XPLOR_EXPECTING_SEGID_PAT.search(err_message))\
            and not err_message.startswith(NO_VIABLE_ALT_ERR_MSG)

        amber_missing_comma_before = (amber_file_type and err_message.startswith(MISMATCHED_INPUT_ERR_MSG)
                                      and bool(AMBER_EXPECTING_COMMA_PAT.search(err_message)))

        if (xplor_missing_end or xplor_ends_wo_statement
                or xplor_l_paren_wo_assi or xplor_00_origin
                or xplor_missing_end_before
                or amber_missing_end or amber_ends_wo_statement
                or amber_missing_comma_before
                or concat_xplor_assi or concat_xplor_rest or concat_xplor_set
                or concat_amber_rst
                or concat_gromacs_tag
                or concat_comment) or i <= err_line_number or j == 0:

            corrected = False

            if err_line_number - 1 in (i, j + j_offset) and xplor_l_paren_wo_assi:  # this should be before 'concat_comment' routine

                if COMMENT_PAT.match(prev_input) and XPLOR_ASSI_PAT.search(prev_input):

                    k = k2 = 0

                    with open(file_path, 'r', encoding='utf-8') as ifh:
                        for line in ifh:
                            k += 1
                            if k <= err_line_number:
                                continue
                            if k < err_line_number + MR_MAX_SPACER_LINES:
                                if XPLOR_ASSI_PAT.match(line) or COMMENT_PAT.match(line) or line.isspace():
                                    k2 = k
                                    break
                                continue
                            break

                    if k2 != 0:

                        comment_code = prev_input.rstrip()[0]

                        cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                        if cor_src_path is not None:

                            k = 0

                            with open(src_path, 'r', encoding='utf-8') as ifh, \
                                    open(cor_src_path, 'w', encoding='utf-8') as ofh:
                                for line in ifh:
                                    k += 1
                                    if k < err_line_number:
                                        ofh.write(line)
                                    elif k < k2:
                                        ofh.write(comment_code + line)
                                    else:
                                        ofh.write(line)

                            if cor_test:
                                os.rename(cor_src_path, src_path)

                            if self.__reg.mr_debug:
                                self.__reg.log.write('DIV-MR-EXIT #3-1\n')

                            return True

                if os.path.exists(div_src_file):
                    os.remove(div_src_file)
                if os.path.exists(div_try_file):
                    os.remove(div_try_file)

                if prev_input is not None:
                    err_desc['previous_input'] = f"Do you need to comment out the succeeding lines as well?\n{prev_input}"

                if self.__reg.mr_debug and not corrected:
                    self.__reg.log.write('DIV-MR-EXIT #3-2\n')

                return False

            if xplor_00_origin:

                cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                if cor_src_path is not None:

                    with open(src_path, 'r', encoding='utf-8') as ifh, \
                            open(cor_src_path, 'w', encoding='utf-8') as ofh:
                        for line in ifh:
                            if ' 00' in line:
                                ofh.write(re.sub(r' 00', ' OO', line))
                            else:
                                ofh.write(line)

                    if cor_test:
                        os.rename(cor_src_path, src_path)

                    if self.__reg.mr_debug:
                        self.__reg.log.write('DIV-MR-EXIT #3-3\n')

                    corrected = True

            if xplor_ends_wo_statement or amber_ends_wo_statement:

                has_end_tag = False

                k = 0

                with open(src_path, 'r', encoding='utf-8') as ifh:
                    for line in ifh:
                        if k == offset:
                            if xplor_ends_wo_statement and XPLOR_END_PAT.match(line):
                                has_end_tag = True
                            if amber_ends_wo_statement and AMBER_END_PAT.match(line):
                                has_end_tag = True
                            break
                        k += 1

                if has_end_tag:

                    cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                    if cor_src_path is not None:

                        k = 0

                        with open(src_path, 'r', encoding='utf-8') as ifh, \
                                open(cor_src_path, 'w', encoding='utf-8') as ofh:
                            for line in ifh:
                                if k == offset:
                                    ofh.write('#' + line)
                                else:
                                    ofh.write(line)
                                k += 1

                        if cor_test:
                            os.rename(cor_src_path, src_path)

                        if self.__reg.mr_debug:
                            self.__reg.log.write('DIV-MR-EXIT #3-4\n')

                        corrected = True

            if concat_xplor_assi or concat_xplor_rest or concat_xplor_set or concat_amber_rst:

                code_index = -1

                if concat_xplor_assi:
                    for m in XPLOR_ANY_ASSI_PAT.finditer(err_input):
                        code_index = m.start()
                elif concat_xplor_rest:
                    for m in XPLOR_ANY_REST_PAT.finditer(err_input):
                        code_index = m.start()
                elif concat_xplor_set:
                    for m in XPLOR_ANY_SET_PAT.finditer(err_input):
                        code_index = m.start()
                elif concat_amber_rst:
                    for m in AMBER_RST_PAT.finditer(err_input):
                        code_index = m.start()

                if code_index != -1:
                    test_line = err_input[0:code_index]

                    if len(test_line.strip()) > 0:
                        typo_for_comment_out = bool(POTENTIAL_TYPO_FOR_COMMENT_OUT_PAT.match(test_line))

                        if reader is None:
                            reader = self.getSimpleFileReader(file_type, False)

                        _, _, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                        has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None

                        if not has_lexer_error:

                            cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                            if cor_src_path is not None:

                                k = 0

                                with open(src_path, 'r', encoding='utf-8') as ifh, \
                                        open(cor_src_path, 'w', encoding='utf-8') as ofh:
                                    for line in ifh:
                                        if k == offset:
                                            if typo_for_comment_out:
                                                g = POTENTIAL_TYPO_FOR_COMMENT_OUT_PAT.search(test_line).groups()
                                                if g[0] == '1':
                                                    test_line = re.sub(r'1', '!', test_line)
                                                else:
                                                    test_line = re.sub(r'3', '#', test_line)
                                                ofh.write(f"{test_line}{err_input[code_index:]}\n")
                                            else:
                                                ofh.write(f"{test_line}\n{err_input[code_index:]}\n")
                                        else:
                                            ofh.write(line)
                                        k += 1

                                if cor_test:
                                    os.rename(cor_src_path, src_path)

                                if self.__reg.mr_debug:
                                    self.__reg.log.write('DIV-MR-EXIT #3-5\n')

                                corrected = True

            if concat_gromacs_tag:
                test_line = err_input[err_column_position + 1:]

                if len(test_line) > 0:

                    test_reader = self.getSimpleFileReader('nm-res-gro', False)

                    _, _parser_err_listener, _lexer_err_listener = test_reader.parse(test_line, None, isFilePath=False)

                    _has_lexer_error = _lexer_err_listener is not None and _lexer_err_listener.getMessageList() is not None

                    if not _has_lexer_error:

                        if self.__reg.mr_debug:
                            self.__reg.log.write('DIV-MR-EXIT #3-6\n')

                        return self.__divideLegacyMr(file_path, file_type, err_desc, src_path, offset)

                    test_reader = self.getSimpleFileReader('nm-aux-gro', False)

                    _, _parser_err_listener, _lexer_err_listener = test_reader.parse(test_line, None, isFilePath=False)

                    _has_lexer_error = _lexer_err_listener is not None and _lexer_err_listener.getMessageList() is not None

                    if not _has_lexer_error:

                        if self.__reg.mr_debug:
                            self.__reg.log.write('DIV-MR-EXIT #3-7\n')

                        return self.__divideLegacyMr(file_path, file_type, err_desc, src_path, offset)

            if concat_comment:

                comment_code_index = -1
                if '#' in err_input:
                    comment_code_index = err_input.index('#')
                if '!' in err_input:
                    if comment_code_index == -1:
                        comment_code_index = err_input.index('!')
                    elif err_input.index('!') < comment_code_index:
                        comment_code_index = err_input.index('!')

                if comment_code_index != -1:
                    test_line = err_input[0:comment_code_index]

                    if reader is None:
                        reader = self.getSimpleFileReader(file_type, False)

                    _, parser_err_listener, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                    has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
                    has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None

                    if not has_lexer_error and not has_parser_error:

                        cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                        if cor_src_path is not None:

                            k = 0

                            with open(src_path, 'r', encoding='utf-8') as ifh, \
                                    open(cor_src_path, 'w', encoding='utf-8') as ofh:
                                for line in ifh:
                                    if k == offset:
                                        ofh.write(f"{test_line} {err_input[comment_code_index:]}\n")
                                    else:
                                        ofh.write(line)
                                    k += 1

                            if cor_test:
                                os.rename(cor_src_path, src_path)

                            if self.__reg.mr_debug:
                                self.__reg.log.write('DIV-MR-EXIT #3-8\n')

                            corrected = True

            if err_line_number - 1 in (i, j + j_offset) and (xplor_missing_end or xplor_missing_end_before):

                if not xplor_missing_end_before or xplor_no_syntax_err_in_fac_or_ann:

                    cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                    if cor_src_path is not None:

                        middle = i != err_line_number - 1
                        is_done = False

                        k = 0 if xplor_missing_end else 1

                        with open(src_path, 'r', encoding='utf-8') as ifh, \
                                open(cor_src_path, 'w', encoding='utf-8') as ofh:
                            for line in ifh:
                                if middle:
                                    if k == err_line_number - 2 and COMMENT_PAT.match(line):
                                        ofh.write('end\n')
                                        is_done = True
                                    elif k == err_line_number - 1 and not is_done:
                                        ofh.write('end\n')
                                ofh.write(line)
                                k += 1
                            if not middle:
                                ofh.write('end\n')

                        if cor_test:
                            os.rename(cor_src_path, src_path)

                        if self.__reg.mr_debug:
                            self.__reg.log.write('DIV-MR-EXIT #3-9\n')

                        corrected = True

            if err_line_number - 1 in (i, j + j_offset) and amber_missing_comma_before:

                cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                if cor_src_path is not None:

                    k = 1

                    with open(src_path, 'r', encoding='utf-8') as ifh, \
                            open(cor_src_path, 'w', encoding='utf-8') as ofh:
                        for line in ifh:
                            if k == err_line_number:
                                ofh.write(',' + line)
                            else:
                                ofh.write(line)
                            k += 1

                    if cor_test:
                        os.rename(cor_src_path, src_path)

                    if self.__reg.mr_debug:
                        self.__reg.log.write('DIV-MR-EXIT #3-10\n')

                    corrected = True

            if i == err_line_number - 1 and amber_missing_end:

                cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                if cor_src_path is not None:

                    with open(src_path, 'r', encoding='utf-8') as ifh, \
                            open(cor_src_path, 'w', encoding='utf-8') as ofh:
                        for line in ifh:
                            ofh.write(line)
                        ofh.write('&end\n')

                    if cor_test:
                        os.rename(cor_src_path, src_path)

                    if self.__reg.mr_debug:
                        self.__reg.log.write('DIV-MR-EXIT #3-11\n')

                    corrected = True

            if not (corrected or concat_xplor_assi or concat_xplor_rest or concat_xplor_set or concat_amber_rst)\
               and (j + j_offset) in (0, err_line_number - 1)\
               and (not xplor_missing_end_before or xplor_no_syntax_err_in_fac_or_ann):
                test_line = err_input

                if reader is None:
                    reader = self.getSimpleFileReader(file_type, False)

                _, _, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None

                if not has_lexer_error:

                    cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                    if cor_src_path is not None:

                        k = 0

                        with open(src_path, 'r', encoding='utf-8') as ifh, \
                                open(cor_src_path, 'w', encoding='utf-8') as ofh:
                            for line in ifh:
                                if k == offset:
                                    ofh.write('#' + line)
                                else:
                                    ofh.write(line)
                                k += 1

                        if cor_test:
                            os.rename(cor_src_path, src_path)

                        if self.__reg.mr_debug:
                            self.__reg.log.write('DIV-MR-EXIT #3-12\n')

                        corrected = True

            if os.path.exists(div_src_file):
                os.remove(div_src_file)
            if os.path.exists(div_try_file):
                os.remove(div_try_file)

            if prev_input is not None and (err_message.startswith(NO_VIABLE_ALT_ERR_MSG)
                                           or err_message.startswith(EXTRANEOUS_INPUT_ERR_MSG)):
                if COMMENT_PAT.match(prev_input):
                    err_desc['previous_input'] = f"Do you need to comment out the succeeding lines as well?\n{prev_input}"
                elif not xplor_assi_after_or_tag and not xplor_assi_incompl_tag:
                    err_desc['previous_input'] = prev_input

            if self.__reg.mr_debug and not corrected:
                self.__reg.log.write('DIV-MR-EXIT #3-13\n')

            return corrected

        if ws_or_comment:
            os.remove(div_src_file)
            os.remove(div_try_file)

            if self.__reg.mr_debug:
                self.__reg.log.write('DIV-MR-EXIT #4\n')

            return False

        if not os.path.exists(div_try_file):
            return False

        file_name = os.path.basename(div_try_file)

        _, _, valid_types, possible_types =\
            self.__detectOtherPossibleFormatAsErrorOfLegacyMr(div_try_file, file_name, 'nm-res-mr', [], True)

        len_valid_types = len(valid_types)
        len_possible_types = len(possible_types)

        if len_valid_types == 0 and len_possible_types == 0:

            if err_column_position > 0 and not err_input[0:err_column_position].isspace():
                test_line = err_input[0:err_column_position]

                if reader is None:
                    reader = self.getSimpleFileReader(file_type, False)

                _, _, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None

                if not has_lexer_error:
                    os.remove(div_src_file)
                    os.remove(div_try_file)

                    if get_peak_list_format_from_string(err_input) is not None:

                        if self.__reg.mr_debug:
                            self.__reg.log.write('DIV-MR-EXIT #5-1\n')

                        return self.__stripLegacyMrIfNecessary(file_path, file_type, err_desc, src_path, offset)

                    if self.__reg.mr_debug:
                        self.__reg.log.write('DIV-MR-EXIT #5-2\n')

                    return False  # not split MR file because of the lexer errors to be handled by manual

            if None not in (next_input, re.search(r'[A-Za-z]', next_input)):
                test_line = next_input

                if reader is None:
                    reader = self.getSimpleFileReader(file_type, False)

                _, parser_err_listener, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None

                if not has_lexer_error and (prev_input is None
                                            or not (prev_input.isspace() or bool(COMMENT_PAT.match(prev_input)))):

                    if err_column_position == 0 and file_type not in LINEAR_MR_FILE_TYPES:

                        for test_file_type in LINEAR_MR_FILE_TYPES:
                            test_reader = self.getSimpleFileReader(test_file_type, False)

                            listener, parser_err_listener, lexer_err_listener = test_reader.parse(test_line, None, isFilePath=False)

                            has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
                            has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None
                            if test_file_type == 'nm-res-ros':
                                _content_subtype = listener.getEffectiveContentSubtype() if listener is not None else None
                            else:
                                _content_subtype = listener.getContentSubtype() if listener is not None else None
                            if _content_subtype is not None and len(_content_subtype) == 0:
                                _content_subtype = None
                            has_content = _content_subtype is not None

                            if not has_lexer_error and not has_parser_error and has_content:

                                if div_src:
                                    os.remove(file_path)

                                os.rename(div_try_file, div_dst_file)

                                is_valid = True  # trigger for more split
                                re_valid = False  # local lexer/parser errors should be handled by manual

                                k = l = 0  # noqa: E741

                                with open(div_dst_file, 'r', encoding='utf-8') as ifh:
                                    for line in ifh:
                                        if k > 0 and not (line.isspace() or bool(COMMENT_PAT.match(line))):
                                            listener, parser_err_listener, lexer_err_listener =\
                                                test_reader.parse(line, None, isFilePath=False)
                                            has_lexer_error = lexer_err_listener is not None\
                                                and lexer_err_listener.getMessageList() is not None
                                            has_parser_error = parser_err_listener is not None\
                                                and parser_err_listener.getMessageList() is not None
                                            if test_file_type == 'nm-res-ros':
                                                _content_subtype = listener.getEffectiveContentSubtype() if listener is not None\
                                                    else None
                                            else:
                                                _content_subtype = listener.getContentSubtype() if listener is not None else None
                                            if _content_subtype is not None and len(_content_subtype) == 0:
                                                _content_subtype = None
                                            has_content = _content_subtype is not None
                                            if has_lexer_error or has_parser_error or not has_content:
                                                if is_valid:
                                                    is_valid = False
                                            elif not is_valid:
                                                re_valid = True
                                                break
                                        if is_valid:
                                            k += 1
                                        else:
                                            l += 1  # noqa: E741
                                            if l >= MR_MAX_SPACER_LINES:
                                                break

                                if not is_valid and not re_valid:

                                    _src_basename = os.path.splitext(div_dst_file)[0]
                                    _div_src_file = _src_basename + '-div_src.mr'
                                    _div_dst_file = _src_basename + '-div_dst.mr'

                                    l = 0  # noqa: E741

                                    with open(div_dst_file, 'r', encoding='utf-8') as ifh, \
                                            open(_div_src_file, 'w', encoding='utf-8') as ofh, \
                                            open(_div_dst_file, 'w', encoding='utf-8') as ofh2:
                                        for line in ifh:
                                            if l < k:
                                                ofh.write(line)
                                            else:
                                                ofh2.write(line)
                                            l += 1  # noqa: E741

                                    os.remove(div_dst_file)

                                if self.__reg.mr_debug:
                                    self.__reg.log.write('DIV-MR-EXIT #6\n')

                                return True

                    os.remove(div_src_file)
                    os.remove(div_try_file)

                    if prev_input is not None:
                        if COMMENT_PAT.match(prev_input):
                            err_desc['previous_input'] = f"Do you need to comment out the succeeding lines as well?\n{prev_input}"
                        elif not xplor_assi_after_or_tag and not xplor_assi_incompl_tag:
                            err_desc['previous_input'] = prev_input

                    if self.__reg.mr_debug:
                        self.__reg.log.write('DIV-MR-EXIT #7\n')

                    return False  # not split MR file because of the lexer errors to be handled by manual

            if div_src:
                os.remove(file_path)

            os.rename(div_try_file, div_ext_file)

            if self.__reg.mr_debug:
                self.__reg.log.write('DIV-MR-EXIT #8\n')

            return True  # succeeded in eliminating uninterpretable parts

        if len_possible_types > 0:
            os.remove(div_src_file)
            os.remove(div_try_file)

            if prev_input is not None:
                if COMMENT_PAT.match(prev_input):
                    err_desc['previous_input'] = f"Do you need to comment out the succeeding lines as well?\n{prev_input}"
                elif not xplor_assi_after_or_tag and not xplor_assi_incompl_tag:
                    err_desc['previous_input'] = prev_input

            if self.__reg.mr_debug:
                self.__reg.log.write('DIV-MR-EXIT #9\n')

            return False

        if file_type in valid_types:
            os.remove(div_src_file)
            os.remove(div_try_file)

            if prev_input is not None:
                if COMMENT_PAT.match(prev_input):
                    err_desc['previous_input'] = f"Do you need to comment out the succeeding lines as well?\n{prev_input}"
                elif not xplor_assi_after_or_tag and not xplor_assi_incompl_tag:
                    err_desc['previous_input'] = prev_input

            if self.__reg.mr_debug:
                self.__reg.log.write('DIV-MR-EXIT #10\n')

            return False  # actual issue in the line before the parser error should be handled by manual

        if prev_input is not None and COMMENT_PAT.match(prev_input)\
           and len_valid_types > 0 and valid_types[0] not in PARSABLE_PK_FILE_TYPES\
           and file_type != 'nm-res-cya' and 'nm-res-cya' not in valid_types:
            # CYANA MR grammar is lax to check comment

            try:

                g = COMMENT_PAT.search(prev_input).groups()

                test_line = g[0]

                if reader is None:
                    reader = self.getSimpleFileReader(file_type, False)

                _, _, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None

                if not has_lexer_error:
                    os.remove(div_src_file)
                    os.remove(div_try_file)

                    err_desc['previous_input'] = f"Do you need to comment out the succeeding lines as well?\n{prev_input}"

                    if self.__reg.mr_debug:
                        self.__reg.log.write('DIV-MR-EXIT #11\n')

                    return False  # actual issue in the line before the parser error should be handled by manual

            except AttributeError:
                pass

        if div_src:
            os.remove(file_path)

        if self.__reg.mr_debug:
            self.__reg.log.write(f'{valid_types} {possible_types}\n')

        os.rename(div_try_file, div_dst_file)

        file_path = div_dst_file

        if len_valid_types == 1:
            file_type = valid_types[0]

        elif len_valid_types == 2:
            if 'nm-res-cns' in valid_types and 'nm-res-xpl' in valid_types:
                file_type = 'nm-res-xpl'

            elif 'nm-res-cya' in valid_types:
                file_type = next(valid_type for valid_type in valid_types if valid_type != 'nm-res-cya')

            elif 'nm-res-cya' in valid_types and 'nm-res-ros' in valid_types:
                file_type = 'nm-res-ros'

        elif len_valid_types == 3:
            set_valid_types = set(valid_types)
            if set_valid_types in ({'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'},
                                   {'nm-res-isd', 'nm-res-cns', 'nm-res-xpl'}):
                file_type = 'nm-res-xpl'

            elif set_valid_types == {'nm-res-cha', 'nm-res-cns', 'nm-res-xpl'}:
                file_type = 'nm-res-cha'

            elif set_valid_types == {'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'}:
                file_type = 'nm-res-xpl'

        if self.__reg.mr_debug:
            self.__reg.log.write(f' -> {file_type}\n')

        self.__testFormatValidityOfLegacyMr(file_path, file_type, src_path, offset)

        if self.__reg.mr_debug:
            self.__reg.log.write('DIV-MR-DONE\n')

        return True

    def __stripLegacyMrIfNecessary(self, file_path: str, file_type: str, err_desc: dict, src_path: str, offset: int) -> bool:
        """ Strip off uninterpretable restraints from the legacy NMR file if necessary.
        """

        src_basename = os.path.splitext(file_path)[0]

        if self.__reg.dirPath is not None:
            src_basename = os.path.join(self.__reg.dirPath, os.path.basename(src_basename))

        div_src = 'div_dst' in src_basename
        div_src_file = src_basename + '-div_src.mr'
        div_ext_file = src_basename + '-div_ext.mr'
        div_try_file = src_basename + '-div_try.mr'
        div_dst_file = src_basename + '-div_dst.mr'

        if any(True for _err_desc in self.__reg.strip_mr_error_message
               if err_desc['file_path'] == _err_desc['file_path']
               and err_desc['line_number'] == _err_desc['line_number']
               and err_desc['column_position'] == _err_desc['column_position']
               and err_desc['message'] == _err_desc['message']):
            if os.path.exists(div_src_file):
                os.remove(div_src_file)
            if os.path.exists(div_dst_file):
                os.remove(div_dst_file)
            if os.path.exists(div_ext_file):
                os.remove(div_ext_file)
            return False

        self.__reg.strip_mr_error_message.append(err_desc)

        if self.__reg.mr_debug:
            self.__reg.log.write('STRIP-MR\n')

        reader = self.getSimpleFileReader(file_type, False)

        if reader is None:
            return False

        err_message = err_desc['message']
        err_line_number = err_desc['line_number']
        err_column_position = err_desc['column_position']
        err_input = err_desc.get('input', '')

        xplor_file_type = file_type in ('nm-res-xpl', 'nm-res-cns')
        amber_file_type = file_type == 'nm-res-amb'
        gromacs_file_type = file_type in ('nm-res-gro', 'nm-aux-gro')

        xplor_ends_wo_statement = xplor_file_type and (bool(XPLOR_EXTRA_END_ERR_MSG_PAT.match(err_message))
                                                       or (err_message.startswith(NO_VIABLE_ALT_ERR_MSG)
                                                           and XPLOR_END_PAT.match(err_input)))
        amber_ends_wo_statement = amber_file_type and (bool(AMBER_EXTRA_END_ERR_MSG_PAT.match(err_message))
                                                       or (err_message.startswith(NO_VIABLE_ALT_ERR_MSG)
                                                           and AMBER_END_PAT.match(err_input)))

        corrected = False

        if xplor_ends_wo_statement or amber_ends_wo_statement:

            _offset = offset + err_line_number - 1

            has_end_tag = False

            k = 0

            with open(src_path, 'r', encoding='utf-8') as ifh:
                for line in ifh:
                    if k == _offset:
                        if xplor_ends_wo_statement and XPLOR_END_PAT.match(line):
                            has_end_tag = True
                        if amber_ends_wo_statement and AMBER_END_PAT.match(line):
                            has_end_tag = True
                        break
                    k += 1

            if has_end_tag:

                cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                if cor_src_path is not None:

                    k = 0

                    with open(src_path, 'r', encoding='utf-8') as ifh, \
                            open(cor_src_path, 'w', encoding='utf-8') as ofh:
                        for line in ifh:
                            if k == _offset:
                                ofh.write('#' + line)
                            else:
                                ofh.write(line)
                            k += 1

                    if cor_test:
                        os.rename(cor_src_path, src_path)

                    corrected = True

        if err_column_position > 0 and not err_input[0:err_column_position].isspace():
            test_line = err_input[err_column_position:]

            if COMMENT_PAT.match(test_line):

                if self.__reg.mr_debug:
                    self.__reg.log.write('STRIP-MR-EXIT #1\n')

                return self.__divideLegacyMr(file_path, file_type, err_desc, src_path, offset) | corrected

            for test_file_type in PARSABLE_MR_FILE_TYPES:

                if test_file_type == file_type:
                    continue

                test_reader = self.getSimpleFileReader(test_file_type, False)

                _, _parser_err_listener, _lexer_err_listener = test_reader.parse(test_line, None, isFilePath=False)

                _has_lexer_error = _lexer_err_listener is not None and _lexer_err_listener.getMessageList() is not None
                _has_parser_error = _parser_err_listener is not None and _parser_err_listener.getMessageList() is not None

                if not _has_lexer_error and not _has_parser_error:

                    if self.__reg.mr_debug:
                        self.__reg.log.write('STRIP-MR-EXIT #2\n')

                    return self.__divideLegacyMr(file_path, file_type, err_desc, src_path, offset) | corrected

            _, parser_err_listener, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)
            has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
            has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None

            if has_lexer_error or not has_parser_error:

                if self.__reg.mr_debug:
                    self.__reg.log.write('STRIP-MR-EXIT #3\n')

                return False | corrected

        i = j = j2 = j3 = 0

        interval = []

        is_done = False

        if not xplor_file_type:

            prev_input = None

            with open(file_path, 'r', encoding='utf-8') as ifh:
                for line in ifh:
                    i += 1

                    if i < err_line_number - MR_MAX_SPACER_LINES:
                        continue
                    if i < err_line_number - 1:
                        interval.append({'line': line,
                                         'ws_or_comment': line.isspace() or bool(COMMENT_PAT.match(line))
                                         or (gromacs_file_type and bool(GROMACS_COMMENT_PAT.match(line)))})
                        continue
                    if i == err_line_number - 1:
                        prev_input = line
                        break

            if prev_input is not None:
                listener, parser_err_listener, lexer_err_listener = reader.parse(prev_input, None, isFilePath=False)

                has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
                has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None
                has_content = bool(listener is not None and len(listener.getContentSubtype()) > 0)

                if has_lexer_error or has_parser_error or not has_content:

                    test_reader = self.getSimpleFileReader('nm-res-xpl', False)

                    _, _parser_err_listener, _lexer_err_listener = test_reader.parse(prev_input, None, isFilePath=False)

                    _has_lexer_error = _lexer_err_listener is not None and _lexer_err_listener.getMessageList() is not None

                    if not has_lexer_error:
                        err_line_number -= 1

                        for _interval in reversed(interval):
                            if _interval['ws_or_comment']:
                                err_line_number -= 1
                            else:
                                break

                        i = 0

                        with open(file_path, 'r', encoding='utf-8') as ifh, \
                                open(div_src_file, 'w', encoding='utf-8') as ofh, \
                                open(div_try_file, 'w', encoding='utf-8') as ofh3:
                            for line in ifh:
                                i += 1
                                if i < err_line_number:
                                    ofh.write(line)
                                    j += 1
                                    continue
                                ofh3.write(line)
                                j3 += 1

                        is_done = True

        if not is_done:

            i = j = j2 = j3 = 0

            interval.clear()

            is_valid = False
            ws_or_comment = True

            with open(file_path, 'r', encoding='utf-8') as ifh, \
                    open(div_src_file, 'w', encoding='utf-8') as ofh, \
                    open(div_ext_file, 'w', encoding='utf-8') as ofh2, \
                    open(div_try_file, 'w', encoding='utf-8') as ofh3:
                for line in ifh:
                    i += 1
                    if i < err_line_number - MR_MAX_SPACER_LINES:
                        ofh.write(line)
                        j += 1
                        continue
                    if i < err_line_number:
                        interval.append({'line': line,
                                         'ws_or_comment': line.isspace() or bool(COMMENT_PAT.match(line))
                                         or (gromacs_file_type and bool(GROMACS_COMMENT_PAT.match(line)))})
                        if i < err_line_number - 1:
                            continue
                        _k = len(interval) - 1
                        _c = interval[-1]['line'][0]
                        for _interval in reversed(interval):
                            c = _interval['line'][0]
                            if _interval['ws_or_comment'] and {c, _c} != COMMENT_CODE_MIXED_SET:
                                _c = c
                                _k -= 1
                                continue
                            break
                        for k, _interval in enumerate(interval):
                            if k <= _k:
                                ofh.write(_interval['line'])
                                j += 1
                            else:
                                ofh2.write(_interval['line'])
                                j2 += 1
                        continue
                    if not is_valid:
                        if line.isspace() or COMMENT_PAT.match(line)\
                           or (gromacs_file_type and GROMACS_COMMENT_PAT.match(line)):
                            ofh2.write(line)
                            j2 += 1
                            continue
                        _, parser_err_listener, lexer_err_listener = reader.parse(line, None, isFilePath=False)
                        if lexer_err_listener is None or lexer_err_listener.getMessageList() is not None:
                            ofh2.write(line)
                            j2 += 1
                            continue
                        if parser_err_listener is not None:
                            messageList = parser_err_listener.getMessageList()
                            if messageList is not None and messageList[0]['line_number'] == 1:
                                ofh2.write(line)
                                j2 += 1
                                continue
                        is_valid = True
                    if ws_or_comment:
                        if line.isspace() or COMMENT_PAT.match(line)\
                           or (gromacs_file_type and GROMACS_COMMENT_PAT.match(line)):
                            ofh2.write(line)
                            j2 += 1
                            continue
                    if CYANA_UNSET_INFO_PAT.match(line) or CYANA_PRINT_PAT.match(line):
                        ofh2.write(line)
                        j2 += 1
                        continue
                    ws_or_comment = False
                    ofh3.write(line)
                    j3 += 1

        offset += j + j2

        if j == 0:
            if div_src:
                os.remove(file_path)
            if os.path.exists(div_try_file):
                os.remove(div_try_file)

            if j3 > 0:
                if self.__reg.mr_debug:
                    self.__reg.log.write('STRIP-MR-EXIT #5\n')

                return False | corrected

            if os.path.getsize(div_src_file) == 0:
                if os.path.exists(div_src_file):  # remove empty file
                    os.remove(div_src_file)

                os.rename(div_ext_file, div_ext_file.replace('dst-div_ext.mr', '_ext.mr'))  # shrink div_ext file name

                if self.__reg.mr_debug:
                    self.__reg.log.write('STRIP-MR-EXIT #6\n')

                return True

        if not os.path.exists(div_try_file):
            return False

        file_name = os.path.basename(div_try_file)

        _, _, valid_types, possible_types =\
            self.__detectOtherPossibleFormatAsErrorOfLegacyMr(div_try_file if j3 > 0 else div_ext_file,
                                                              file_name, 'nm-res-mr', [], True)

        len_valid_types = len(valid_types)
        len_possible_types = len(possible_types)

        if len_valid_types == 0 and len_possible_types == 0:

            if err_column_position > 0 and not err_input[0:err_column_position].isspace():
                test_line = err_input[0:err_column_position]

                if reader is None:
                    reader = self.getSimpleFileReader(file_type, False)

                _, _, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None

                if not has_lexer_error:

                    _file_type = get_peak_list_format_from_string(err_input, asCode=True)

                    if j3 == 0 and _file_type is not None:
                        shutil.copyfile(div_ext_file, self.testPath(div_ext_file + f'-selected-as-{_file_type[-7:]}', True))
                        os.remove(div_try_file)
                        os.remove(file_path)

                        corrected = True

                    else:
                        os.remove(div_src_file)
                        if os.path.exists(div_ext_file):
                            os.remove(div_ext_file)
                        os.remove(div_try_file)

                    if self.__reg.mr_debug:
                        self.__reg.log.write('STRIP-MR-EXIT #7\n')

                    return False | corrected  # not split MR file because of the lexer errors to be handled by manual

            if div_src:
                os.remove(file_path)
            with open(div_try_file, 'r', encoding='utf-8') as ifh, \
                    open(div_ext_file, 'a', encoding='utf-8') as ofh:
                for line in ifh:
                    ofh.write(line)
            os.remove(div_try_file)

            if self.__reg.mr_debug:
                self.__reg.log.write('STRIP-MR-EXIT #8\n')

            return True  # succeeded in eliminating uninterpretable parts

        if len_possible_types > 0:
            os.remove(div_src_file)
            os.remove(div_ext_file)
            os.remove(div_try_file)

            if self.__reg.mr_debug:
                self.__reg.log.write('STRIP-MR-EXIT #9\n')

            return False | corrected

        if div_src:
            os.remove(file_path)

        os.rename(div_try_file if j3 > 0 else div_ext_file, div_dst_file)

        if j3 == 0:
            os.remove(div_try_file)

        if self.__reg.mr_debug:
            self.__reg.log.write(f'{valid_types} {possible_types}\n')

        file_path = div_dst_file

        if len_valid_types == 1:
            file_type = valid_types[0]

        elif len_valid_types == 2:
            if 'nm-res-cns' in valid_types and 'nm-res-xpl' in valid_types:
                file_type = 'nm-res-xpl'

            elif 'nm-res-cya' in valid_types:
                file_type = next(valid_type for valid_type in valid_types if valid_type != 'nm-res-cya')

            elif 'nm-res-cya' in valid_types and 'nm-res-ros' in valid_types:
                file_type = 'nm-res-ros'

        elif len_valid_types == 3:
            set_valid_types = set(valid_types)
            if set_valid_types in ({'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'},
                                   {'nm-res-isd', 'nm-res-cns', 'nm-res-xpl'}):
                file_type = 'nm-res-xpl'

            elif set_valid_types == {'nm-res-cha', 'nm-res-cns', 'nm-res-xpl'}:
                file_type = 'nm-res-cha'

            elif set_valid_types == {'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'}:
                file_type = 'nm-res-xpl'

        if self.__reg.mr_debug:
            self.__reg.log.write(f' -> {file_type}\n')

        self.__testFormatValidityOfLegacyMr(file_path, file_type, src_path, offset)

        if self.__reg.mr_debug:
            self.__reg.log.write('STRIP-MR-DONE\n')

        return True

    def __divideLegacyMr(self, file_path: str, file_type: str, err_desc: dict, src_path: str, offset: int) -> bool:
        """ Divide legacy restraint file.
        """

        src_basename = os.path.splitext(file_path)[0]

        if self.__reg.dirPath is not None:
            src_basename = os.path.join(self.__reg.dirPath, os.path.basename(src_basename))

        div_src = 'div_dst' in src_basename
        div_src_file = src_basename + '-div_src.mr'
        div_ext_file = src_basename + '-div_ext.mr'
        div_try_file = src_basename + '-div_try.mr'
        div_dst_file = src_basename + '-div_dst.mr'

        if self.__reg.mr_debug:
            self.__reg.log.write('DO-DIV-MR\n')

        if file_type not in PARSABLE_MR_FILE_TYPES:
            return False

        err_message = err_desc['message']
        err_line_number = err_desc['line_number']
        err_column_position = err_desc['column_position']
        err_input = err_desc.get('input', '')

        if 0 in (err_column_position, len(err_input)):

            if self.__reg.mr_debug:
                self.__reg.log.write('DO-DIV-MR-EXIT #1\n')

            return False

        xplor_file_type = file_type in ('nm-res-xpl', 'nm-res-cns')
        amber_file_type = file_type == 'nm-res-amb'
        gromacs_file_type = file_type in ('nm-res-gro', 'nm-aux-gro')

        xplor_missing_end = xplor_file_type and err_message.startswith(XPLOR_MISSING_END_ERR_MSG)
        xplor_ends_wo_statement = xplor_file_type and (bool(XPLOR_EXTRA_END_ERR_MSG_PAT.match(err_message))
                                                       or (err_message.startswith(NO_VIABLE_ALT_ERR_MSG)
                                                           and XPLOR_END_PAT.match(err_input)))

        xplor_l_paren_wo_assi = xplor_file_type and bool(XPLOR_EXTRA_L_PAREN_ERR_MSG_PAT.match(err_message))
        xplor_00_origin = xplor_file_type and err_message.startswith(NO_VIABLE_ALT_ERR_MSG) and ' 00' in err_input

        amber_missing_end = amber_file_type and err_message.startswith(AMBER_MISSING_END_ERR_MSG)
        amber_ends_wo_statement = amber_file_type and (bool(AMBER_EXTRA_END_ERR_MSG_PAT.match(err_message))
                                                       or (err_message.startswith(NO_VIABLE_ALT_ERR_MSG)
                                                           and AMBER_END_PAT.match(err_input)))

        concat_xplor_assi = (xplor_file_type
                             and (err_message.startswith(MISMATCHED_INPUT_ERR_MSG)
                                  or err_message.startswith(EXTRANEOUS_INPUT_ERR_MSG))
                             and bool(XPLOR_ASSI_PAT.search(err_input))
                             and not bool(XPLOR_CLASS_PAT.search(err_input)))
        concat_xplor_rest = (xplor_file_type
                             and (err_message.startswith(MISMATCHED_INPUT_ERR_MSG)
                                  or err_message.startswith(EXTRANEOUS_INPUT_ERR_MSG))
                             and bool(XPLOR_REST_PAT.search(err_input)))
        concat_xplor_set = (xplor_file_type
                            and (err_message.startswith(MISMATCHED_INPUT_ERR_MSG)
                                 or err_message.startswith(EXTRANEOUS_INPUT_ERR_MSG))
                            and bool(XPLOR_SET_PAT.search(err_input))
                            and get_peak_list_format_from_string(err_input) is None)
        concat_amber_rst = (amber_file_type
                            and (err_message.startswith(MISMATCHED_INPUT_ERR_MSG)
                                 or err_message.startswith(EXTRANEOUS_INPUT_ERR_MSG))
                            and bool(AMBER_RST_PAT.search(err_input))
                            and not bool(AMBER_RST_PAT.match(err_input)))

        concat_comment = (file_type in LINEAR_MR_FILE_TYPES
                          and err_message.startswith(NO_VIABLE_ALT_ERR_MSG)
                          and bool(COMMENT_PAT.search(err_input)))

        if concat_xplor_assi and bool(XPLOR_ASSI_PAT.match(err_input)):
            if EXPECTING_L_PAREN in err_message:
                xplor_missing_end = True
                concat_xplor_assi = False
            if concat_xplor_rest or concat_xplor_set:
                concat_xplor_assi = False

        reader = prev_input = None

        i = j = 0

        ws_or_comment = True

        with open(file_path, 'r', encoding='utf-8') as ifh, \
                open(div_src_file, 'w', encoding='utf-8') as ofh, \
                open(div_try_file, 'w', encoding='utf-8') as ofh2:
            for line in ifh:
                i += 1
                if i < err_line_number:
                    if ws_or_comment:
                        if line.isspace() or COMMENT_PAT.match(line)\
                           or (gromacs_file_type and GROMACS_COMMENT_PAT.match(line)):
                            pass
                        else:
                            ws_or_comment = False
                    if i == err_line_number - 1:
                        prev_input = line
                    ofh.write(line)
                    j += 1
                    continue
                if i == err_line_number:
                    ofh.write(line[0:err_column_position] + '\n')
                    j += 1
                    ofh2.write(line[err_column_position:])
                    continue
                ofh2.write(line)

        offset += err_line_number - 1

        xplor_missing_end_before = (xplor_file_type and err_message.startswith(MISMATCHED_INPUT_ERR_MSG)
                                    and not bool(XPLOR_EXPECTNIG_SYMBOL_PAT.search(err_message))  # excl. syntax errors in a factor
                                    and prev_input is not None and bool(XPLOR_ASSI_PAT.search(prev_input)))

        xplor_no_syntax_err_in_fac_or_ann = not bool(XPLOR_EXPECTING_EQU_OP_PAT.search(err_message))\
            and not bool(XPLOR_EXPECTING_SEGID_PAT.search(err_message))\
            and not err_message.startswith(NO_VIABLE_ALT_ERR_MSG)

        amber_missing_comma_before = (amber_file_type and err_message.startswith(MISMATCHED_INPUT_ERR_MSG)
                                      and bool(AMBER_EXPECTING_COMMA_PAT.search(err_message)))

        if (xplor_missing_end or xplor_ends_wo_statement
                or xplor_l_paren_wo_assi or xplor_00_origin
                or xplor_missing_end_before
                or amber_missing_end or amber_ends_wo_statement
                or amber_missing_comma_before
                or concat_xplor_assi or concat_xplor_rest or concat_xplor_set
                or concat_amber_rst
                or concat_comment) or i <= err_line_number or j == 0:

            corrected = False

            if err_line_number - 1 in (i, j) and xplor_l_paren_wo_assi:  # this should be before 'concat_comment' routine

                if os.path.exists(div_src_file):
                    os.remove(div_src_file)
                if os.path.exists(div_try_file):
                    os.remove(div_try_file)

                if prev_input is not None:
                    err_desc['previous_input'] = f"Do you need to comment out the succeeding lines as well?\n{prev_input}"

                if self.__reg.mr_debug and not corrected:
                    self.__reg.log.write('DO-DIV-MR-EXIT #2-1\n')

                return False

            if xplor_00_origin:

                cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                if cor_src_path is not None:

                    with open(src_path, 'r', encoding='utf-8') as ifh, \
                            open(cor_src_path, 'w', encoding='utf-8') as ofh:
                        for line in ifh:
                            if ' 00' in line:
                                ofh.write(re.sub(r' 00', ' OO', line))
                            else:
                                ofh.write(line)

                    if cor_test:
                        os.rename(cor_src_path, src_path)

                    if self.__reg.mr_debug:
                        self.__reg.log.write('DO-DIV-MR-EXIT #2-2\n')

                    corrected = True

            if xplor_ends_wo_statement or amber_ends_wo_statement:

                has_end_tag = False

                k = 0

                with open(src_path, 'r', encoding='utf-8') as ifh:
                    for line in ifh:
                        if k == offset:
                            if xplor_ends_wo_statement and XPLOR_END_PAT.match(line):
                                has_end_tag = True
                            if amber_ends_wo_statement and AMBER_END_PAT.match(line):
                                has_end_tag = True
                            break
                        k += 1

                if has_end_tag:

                    cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                    if cor_src_path is not None:

                        k = 0

                        with open(src_path, 'r', encoding='utf-8') as ifh, \
                                open(cor_src_path, 'w', encoding='utf-8') as ofh:
                            for line in ifh:
                                if k == offset:
                                    ofh.write('#' + line)
                                else:
                                    ofh.write(line)
                                k += 1

                        if cor_test:
                            os.rename(cor_src_path, src_path)

                        if self.__reg.mr_debug:
                            self.__reg.log.write('DO-DIV-MR-EXIT #2-3\n')

                        corrected = True

            if concat_xplor_assi or concat_xplor_rest or concat_xplor_set or concat_amber_rst:

                code_index = -1

                if concat_xplor_assi:
                    for m in XPLOR_ANY_ASSI_PAT.finditer(err_input):
                        code_index = m.start()
                elif concat_xplor_rest:
                    for m in XPLOR_ANY_REST_PAT.finditer(err_input):
                        code_index = m.start()
                elif concat_xplor_set:
                    for m in XPLOR_ANY_SET_PAT.finditer(err_input):
                        code_index = m.start()
                elif concat_amber_rst:
                    for m in AMBER_RST_PAT.finditer(err_input):
                        code_index = m.start()

                if code_index != -1:
                    test_line = err_input[0:code_index]

                    if len(test_line.strip()) > 0:
                        typo_for_comment_out = bool(POTENTIAL_TYPO_FOR_COMMENT_OUT_PAT.match(test_line))

                        if reader is None:
                            reader = self.getSimpleFileReader(file_type, False)

                        _, parser_err_listener, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                        has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None

                        if not has_lexer_error:

                            cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                            if cor_src_path is not None:

                                k = 0

                                with open(src_path, 'r', encoding='utf-8') as ifh, \
                                        open(cor_src_path, 'w', encoding='utf-8') as ofh:
                                    for line in ifh:
                                        if k == offset:
                                            if typo_for_comment_out:
                                                g = POTENTIAL_TYPO_FOR_COMMENT_OUT_PAT.search(test_line).groups()
                                                if g[0] == '1':
                                                    test_line = re.sub(r'1', '!', test_line)
                                                else:
                                                    test_line = re.sub(r'3', '#', test_line)
                                                ofh.write(f"{test_line}{err_input[code_index:]}\n")
                                            else:
                                                ofh.write(f"{test_line}\n{err_input[code_index:]}\n")
                                        else:
                                            ofh.write(line)
                                        k += 1

                                if cor_test:
                                    os.rename(cor_src_path, src_path)

                                if self.__reg.mr_debug:
                                    self.__reg.log.write('DIV-MR-EXIT #2-4\n')

                                corrected = True

            if concat_comment:

                comment_code_index = -1
                if '#' in err_input:
                    comment_code_index = err_input.index('#')
                if '!' in err_input:
                    if comment_code_index == -1:
                        comment_code_index = err_input.index('!')
                    elif err_input.index('!') < comment_code_index:
                        comment_code_index = err_input.index('!')

                if comment_code_index != -1:
                    test_line = err_input[0:comment_code_index]

                    if reader is None:
                        reader = self.getSimpleFileReader(file_type, False)

                    _, parser_err_listener, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                    has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
                    has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None

                    if not has_lexer_error and not has_parser_error:

                        cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                        if cor_src_path is not None:

                            k = 0

                            with open(src_path, 'r', encoding='utf-8') as ifh, \
                                    open(cor_src_path, 'w', encoding='utf-8') as ofh:
                                for line in ifh:
                                    if k == offset:
                                        ofh.write(f"{test_line} {err_input[comment_code_index:]}\n")
                                    else:
                                        ofh.write(line)
                                    k += 1

                            if cor_test:
                                os.rename(cor_src_path, src_path)

                            if self.__reg.mr_debug:
                                self.__reg.log.write('DO-DIV-MR-EXIT #2-5\n')

                            corrected = True

            if err_line_number - 1 in (i, j) and (xplor_missing_end or xplor_missing_end_before):

                if not xplor_missing_end_before or xplor_no_syntax_err_in_fac_or_ann:

                    cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                    if cor_src_path is not None:

                        middle = i != err_line_number - 1
                        is_done = False

                        k = 0 if xplor_missing_end else 1

                        with open(src_path, 'r', encoding='utf-8') as ifh, \
                                open(cor_src_path, 'w', encoding='utf-8') as ofh:
                            for line in ifh:
                                if middle:
                                    if k == err_line_number - 2 and COMMENT_PAT.match(line):
                                        ofh.write('end\n')
                                        is_done = True
                                    elif k == err_line_number - 1 and not is_done:
                                        ofh.write('end\n')
                                ofh.write(line)
                                k += 1
                            if not middle:
                                ofh.write('end\n')

                        if cor_test:
                            os.rename(cor_src_path, src_path)

                        if self.__reg.mr_debug:
                            self.__reg.log.write('DO-DIV-MR-EXIT #2-6\n')

                        corrected = True

            if err_line_number - 1 in (i, j) and amber_missing_comma_before:

                cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                if cor_src_path is not None:

                    k = 1

                    with open(src_path, 'r', encoding='utf-8') as ifh, \
                            open(cor_src_path, 'w', encoding='utf-8') as ofh:
                        for line in ifh:
                            if k == err_line_number:
                                ofh.write(',' + line)
                            else:
                                ofh.write(line)
                            k += 1

                    if cor_test:
                        os.rename(cor_src_path, src_path)

                    if self.__reg.mr_debug:
                        self.__reg.log.write('DIV-MR-EXIT #2-7\n')

                    corrected = True

            if i == err_line_number - 1 and amber_missing_end:

                cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                if cor_src_path is not None:

                    with open(src_path, 'r', encoding='utf-8') as ifh, \
                            open(cor_src_path, 'w', encoding='utf-8') as ofh:
                        for line in ifh:
                            ofh.write(line)
                        ofh.write('&end\n')

                    if cor_test:
                        os.rename(cor_src_path, src_path)

                    if self.__reg.mr_debug:
                        self.__reg.log.write('DO-DIV-MR-EXIT #2-8\n')

                    corrected = True

            if not (corrected or concat_xplor_assi or concat_xplor_rest or concat_xplor_set or concat_amber_rst)\
               and j in (0, err_line_number - 1)\
               and (not xplor_missing_end_before or xplor_no_syntax_err_in_fac_or_ann):
                test_line = err_input

                if reader is None:
                    reader = self.getSimpleFileReader(file_type, False)

                _, _, lexer_err_listener = reader.parse(test_line, None, isFilePath=False)

                has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None

                if not has_lexer_error:

                    cor_src_path, cor_test = self.__getCorrectedMrFilePath(src_path)

                    if cor_src_path is not None:

                        k = 0

                        with open(src_path, 'r', encoding='utf-8') as ifh, \
                                open(cor_src_path, 'w', encoding='utf-8') as ofh:
                            for line in ifh:
                                if k == offset:
                                    ofh.write('#' + line)
                                else:
                                    ofh.write(line)
                                k += 1

                        if cor_test:
                            os.rename(cor_src_path, src_path)

                        if self.__reg.mr_debug:
                            self.__reg.log.write('DO-DIV-MR-EXIT #2-9\n')

                        corrected = True

            if os.path.exists(div_src_file):
                os.remove(div_src_file)
            if os.path.exists(div_try_file):
                os.remove(div_try_file)

            if self.__reg.mr_debug and not corrected:
                self.__reg.log.write('DO-DIV-MR-EXIT #2-10\n')

            return corrected

        if ws_or_comment:
            os.remove(div_src_file)
            os.remove(div_try_file)

            if self.__reg.mr_debug:
                self.__reg.log.write('DO-DIV-MR-EXIT #3\n')

            return False

        if not os.path.exists(div_try_file):
            return False

        file_name = os.path.basename(div_try_file)

        _, _, valid_types, possible_types =\
            self.__detectOtherPossibleFormatAsErrorOfLegacyMr(div_try_file, file_name, 'nm-res-mr', [], True)

        len_valid_types = len(valid_types)
        len_possible_types = len(possible_types)

        if len_valid_types == 0 and len_possible_types == 0:

            if xplor_file_type and bool(XPLOR_ASSI_PAT.search(err_input)):

                if prev_input is not None and err_message.startswith(EXTRANEOUS_INPUT_ERR_MSG):
                    err_desc['previous_input'] = prev_input

                os.remove(div_src_file)
                os.remove(div_try_file)

                if self.__reg.mr_debug:
                    self.__reg.log.write('DO-DIV-MR-EXIT #4\n')

                return False

            if div_src:
                os.remove(file_path)
            os.rename(div_try_file, div_ext_file)

            if self.__reg.mr_debug:
                self.__reg.log.write('DO-DIV-MR-EXIT #5\n')

            return True  # succeeded in eliminating uninterpretable parts

        if len_possible_types > 0:
            os.remove(div_src_file)
            os.remove(div_try_file)

            if self.__reg.mr_debug:
                self.__reg.log.write('DO-DIV-MR-EXIT #6\n')

            return False

        if div_src:
            os.remove(file_path)

        os.rename(div_try_file, div_dst_file)

        if self.__reg.mr_debug:
            self.__reg.log.write(f'{valid_types} {possible_types}\n')

        file_path = div_dst_file

        if len_valid_types == 1:
            file_type = valid_types[0]

        elif len_valid_types == 2:
            if 'nm-res-cns' in valid_types and 'nm-res-xpl' in valid_types:
                file_type = 'nm-res-xpl'

            elif 'nm-res-cya' in valid_types:
                file_type = next(valid_type for valid_type in valid_types if valid_type != 'nm-res-cya')

            elif 'nm-res-cya' in valid_types and 'nm-res-ros' in valid_types:
                file_type = 'nm-res-ros'

        elif len_valid_types == 3:
            set_valid_types = set(valid_types)
            if set_valid_types in ({'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'},
                                   {'nm-res-isd', 'nm-res-cns', 'nm-res-xpl'}):
                file_type = 'nm-res-xpl'

            elif set_valid_types == {'nm-res-cha', 'nm-res-cns', 'nm-res-xpl'}:
                file_type = 'nm-res-cha'

            elif set_valid_types == {'nm-res-cya', 'nm-res-cns', 'nm-res-xpl'}:
                file_type = 'nm-res-xpl'

        if self.__reg.mr_debug:
            self.__reg.log.write(f' -> {file_type}\n')

        self.__testFormatValidityOfLegacyMr(file_path, file_type, src_path, offset)

        if self.__reg.mr_debug:
            self.__reg.log.write('DO-DIV-MR-DONE\n')

        return True

    def __testFormatValidityOfLegacyMr(self, file_path: str, file_type: str, src_path: str, offset: int) -> None:
        """ Perform format check of a given MR file, then split MR recursively if necessary.
        """

        div_test = False

        try:

            reader = self.getSimpleFileReader(file_type, False, sll_pred=False)

            listener, parser_err_listener, lexer_err_listener = reader.parse(file_path, None)

            if listener is not None:
                if file_type in RETRIAL_MR_FILE_TYPES:
                    reasons = listener.getReasonsForReparsing()

                    if reasons is not None:
                        reader = self.getSimpleFileReader(file_type, False, sll_pred=False, reasons=reasons)

                        listener, parser_err_listener, lexer_err_listener = reader.parse(file_path, None)

            has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
            has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None
            has_content = bool(listener is not None and len(listener.getContentSubtype()) > 0)

            if has_lexer_error and has_parser_error and has_content:
                # parser error occurs before occurrence of lexer error that implies mixing of different MR formats in a file
                if lexer_err_listener.getErrorLineNumber()[0] > parser_err_listener.getErrorLineNumber()[0]:
                    self.__stripLegacyMrIfNecessary(file_path, file_type,
                                                    parser_err_listener.getMessageList()[0],
                                                    src_path, offset)
                    div_test = True

            fixed_line_num = -1

            if has_lexer_error:
                messageList = lexer_err_listener.getMessageList()

                for description in messageList:
                    if 'input' in description:
                        enc = detect_encoding(description['input'])
                        if enc is not None and enc != 'ascii':
                            pass
                        elif not div_test and has_content:
                            fixed = self.__divideLegacyMrIfNecessary(file_path, file_type, description, src_path, offset)
                            if fixed:
                                fixed_line_num = description['line_number']
                            div_test = file_type != 'nm-res-amb'  # remediate missing comma issue in AMBER MR

            if has_parser_error:
                messageList = parser_err_listener.getMessageList()

                for description in messageList:
                    if 0 < fixed_line_num <= description['line_number']:
                        div_test = True
                    if 'input' in description:
                        if not div_test and has_content:
                            self.__divideLegacyMrIfNecessary(file_path, file_type, description, src_path, offset)
                            div_test = True
                    elif not div_test and has_content and file_type in ('nm-res-xpl', 'nm-res-cns'):
                        self.__divideLegacyMrIfNecessary(file_path, file_type, description, str(file_path), offset)
                        div_test = True

        except ValueError as e:

            self.__reg.report.error.appendDescription('internal_error',
                                                      f"+{self.__class_name__}.__testFormatValidityOfLegacyMr() "
                                                      "++ Error  - " + str(e))

            if self.__reg.verbose:
                self.__reg.log.write(f"+{self.__class_name__}.__testFormatValidityOfLegacyMr() ++ Error  - {str(e)}\n")

    def __detectOtherPossibleFormatAsErrorOfLegacyMr(self, file_path: str, file_name: str, file_type: str,
                                                     dismiss_err_lines: List[int], multiple_check: bool = False
                                                     ) -> Tuple[bool, str, List[str], List[str]]:
        """ Report other possible format as error of a given legacy restraint file.
        """

        is_valid = agreed_w_cns = False
        err = ''
        genuine_type = []
        valid_types, possible_types = {}, {}

        if (not is_valid or multiple_check) and file_type != 'nm-res-xpl':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-res-xpl', agreed_w_cns=agreed_w_cns)

            is_valid |= _is_valid
            agreed_w_cns |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if len(genuine_type) > 0:
            multiple_check = False

        if (not is_valid or multiple_check) and file_type != 'nm-res-cns':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-res-cns', agreed_w_cns=agreed_w_cns)

            is_valid |= _is_valid
            agreed_w_cns |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or 'Syntax error' in err) and file_type != 'nm-res-cha':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-res-cha', agreed_w_cns=agreed_w_cns)

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if len(genuine_type) > 0:
            multiple_check = False

        if (not is_valid or multiple_check) and file_type != 'nm-res-amb':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-res-amb')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-aux-amb':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-aux-amb')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-res-ari':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-res-ari')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-res-arx':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-res-arx')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-res-bio':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-res-bio')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)
        # """ conflict with nm-res-cya (2kcp)
        # if (not is_valid or multiple_check) and file_type != 'nm-aux-cha':
        #     _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
        #         self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
        #                                                             'nm-aux-cha')
        #
        #     is_valid |= _is_valid
        #     err += _err
        #     if _genuine_type is not None:
        #         genuine_type.append(_genuine_type)
        #     valid_types.update(_valid_types)
        #     possible_types.update(_possible_types)
        # """
        if (not is_valid or multiple_check) and file_type != 'nm-res-dyn':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-res-dyn')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-res-gro':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-res-gro')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-aux-gro':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-aux-gro')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-res-isd':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-res-isd')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-aux-pdb':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-aux-pdb')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-res-ros':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-res-ros')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-res-sch':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-res-sch',
                                                                    agreed_w_cns=agreed_w_cns)

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if (not is_valid or multiple_check) and file_type != 'nm-res-syb':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-res-syb')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if not is_valid and file_type != 'nm-res-noa':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-res-noa')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
                multiple_check = False
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        # prevent 'nm-pea-any' occasionally matches with 'nm-res-cya' (DAOTHER-9425)
        if (not is_valid or multiple_check) and file_type not in ('nm-res-cya', 'nm-pea-any'):
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-res-cya')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None and 'nm-res-noa' not in genuine_type:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        _file_type = get_peak_list_format(file_path, True)

        if _file_type == 'nm-pea-ari' and file_type != 'nm-pea-ari':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-pea-ari')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-ccp' and file_type != 'nm-pea-ccp':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-pea-ccp')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-oli' and file_type != 'nm-pea-oli':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-pea-oli')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-pip' and file_type != 'nm-pea-pip':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-pea-pip')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-pon' and file_type != 'nm-pea-pon':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-pea-pon')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-spa' and file_type != 'nm-pea-spa':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-pea-spa')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-sps' and file_type != 'nm-pea-sps':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-pea-sps')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-top' and file_type != 'nm-pea-top':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-pea-top')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-vie' and file_type != 'nm-pea-vie':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-pea-vie')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-vnm' and file_type != 'nm-pea-vnm':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-pea-vnm')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-xea' and file_type != 'nm-pea-xea':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-pea-xea')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if _file_type == 'nm-pea-xwi' and file_type != 'nm-pea-xwi':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-pea-xwi')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if not is_valid and _file_type is None and file_type != 'nm-aux-xea':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-aux-xea')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if not is_valid and _file_type is None and file_type != 'nm-pea-bar':
            _is_valid, _err, _genuine_type, _valid_types, _possible_types =\
                self.__detectOtherPossibleFormatAsErrorOfLegacyMr__(file_path, file_name, file_type, dismiss_err_lines,
                                                                    'nm-pea-bar')

            is_valid |= _is_valid
            err += _err
            if _genuine_type is not None:
                genuine_type.append(_genuine_type)
            valid_types.update(_valid_types)
            possible_types.update(_possible_types)

        if len(genuine_type) != 1:
            _valid_types = [k for k, v in sorted(valid_types.items(), key=itemgetter(1), reverse=True)]
            _possible_types = [k for k, v in sorted(possible_types.items(), key=itemgetter(1), reverse=True)]

        else:
            _valid_types = [genuine_type[0]]
            _possible_types = []

        return is_valid, err, _valid_types, _possible_types

    def __detectOtherPossibleFormatAsErrorOfLegacyMr__(self, file_path: str, file_name: str, file_type: str,
                                                       dismiss_err_lines: List[int],
                                                       _file_type: str, agreed_w_cns: bool = False
                                                       ) -> Tuple[bool, str, Optional[str], dict, dict]:
        """ Report other possible format as error of a given legacy restraint file.
        """

        _mr_format_name = getRestraintFormatName(file_type)
        mr_format_name = _mr_format_name.split()[0]

        __mr_format_name = getRestraintFormatName(_file_type, True)
        _mr_format_name = __mr_format_name.split()[0]
        _a_mr_format_name = ('an ' if _mr_format_name[0] in ('AINMX') else 'a ') + __mr_format_name

        is_valid = False
        err = ''
        genuine_type = None
        valid_types, possible_types = {}, {}

        try:

            sll_pred = not agreed_w_cns

            reader = self.getSimpleFileReader(_file_type, False, sll_pred=sll_pred)

            listener, parser_err_listener, lexer_err_listener = reader.parse(file_path, None)

            has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
            has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None

            if (has_lexer_error or has_parser_error) and sll_pred\
               and _file_type in ('nm-res-xpl', 'nm-res-cns', 'nm-res-cha'):
                sll_pred = False

                reader.setSllPredMode(sll_pred)

                listener, parser_err_listener, lexer_err_listener = reader.parse(file_path, None)

                has_lexer_error = lexer_err_listener is not None and lexer_err_listener.getMessageList() is not None
                has_parser_error = parser_err_listener is not None and parser_err_listener.getMessageList() is not None

            if file_path not in self.__reg.sll_pred_holder:
                self.__reg.sll_pred_holder[file_path] = {}

            if not has_lexer_error and not has_parser_error:
                self.__reg.sll_pred_holder[file_path][_file_type] = sll_pred

            # 'rdc_restraint' occasionally matches with CYANA restraints
            # 'geo_restraint' include CS-ROSETTA disulfide bond linkage, which matches any integer array
            if _file_type == 'nm-res-ros':
                _content_subtype = listener.getEffectiveContentSubtype() if listener is not None else None
            else:
                _content_subtype = listener.getContentSubtype() if listener is not None else None
            if _content_subtype is not None and len(_content_subtype) == 0:
                _content_subtype = None
            has_content = _content_subtype is not None

            if None not in (lexer_err_listener, parser_err_listener, listener)\
               and ((lexer_err_listener.getMessageList() is None and parser_err_listener.getMessageList() is None) or has_content):

                if has_content or file_type != 'nm-res-oth':

                    is_valid = True
                    if (has_lexer_error or has_parser_error) and _file_type == 'nm-aux-xea':  # 2lcn
                        is_valid = False

                    err = f"The restraint file {file_name!r} ({mr_format_name}) looks like {_a_mr_format_name} file, "\
                          f"which has {concat_restraint_names(_content_subtype)}. "\
                          "Did you accidentally select wrong format? Please re-upload the restraint file."

                    if has_content:
                        _err = ''
                        if lexer_err_listener is not None:
                            messageList = lexer_err_listener.getMessageList()

                            if messageList is not None:
                                for description in messageList:
                                    if description['line_number'] in dismiss_err_lines:
                                        continue
                                    _err = f"[Syntax error as {_a_mr_format_name} file] "\
                                           f"line {description['line_number']}:{description['column_position']} "\
                                           f"{description['message']}\n"
                                    if 'input' in description:
                                        enc = detect_encoding(description['input'])
                                        is_not_ascii = False
                                        if enc is not None and enc != 'ascii':
                                            _err += f"{description['input']}\n".encode().decode('ascii', 'backslashreplace')
                                            is_not_ascii = True
                                        else:
                                            _err += f"{description['input']}\n"
                                        _err += f"{description['marker']}\n"
                                        if is_not_ascii:
                                            _err += f"[Unexpected text encoding] Encoding used in the above line is {enc!r} "\
                                                "and must be 'ascii'.\n"

                        if parser_err_listener is not None and len(_err) == 0:
                            messageList = parser_err_listener.getMessageList()

                            if messageList is not None:
                                for description in messageList:
                                    if description['line_number'] in dismiss_err_lines:
                                        continue
                                    _err += f"[Syntax error as {_a_mr_format_name} file] "\
                                            f"line {description['line_number']}:{description['column_position']} "\
                                            f"{description['message']}\n"
                                    if 'input' in description:
                                        _err += f"{description['input']}\n"
                                        _err += f"{description['marker']}\n"

                        if len(_err) > 0:
                            err += f"\nEven assuming that the format is the {_mr_format_name!r}, "\
                                "the following issues need to be fixed.\n" + _err[:-1]
                        elif file_type != 'nm-res-oth'\
                                and (lexer_err_listener.getMessageList() is not None
                                     or parser_err_listener.getMessageList() is not None):
                            is_valid = False
                            err = ''

                        if is_valid:
                            if has_content and lexer_err_listener.getMessageList() is None\
                               and parser_err_listener.getMessageList() is None:
                                genuine_type = _file_type
                            valid_types[_file_type] = len(_content_subtype)
                        elif _file_type != 'nm-aux-xea':  # 2lcn
                            possible_types[_file_type] = len(_content_subtype)

                    if file_type == 'nm-res-oth':
                        self.__reg.report.error.appendDescription('content_mismatch',
                                                                  {'file_name': file_name, 'description': err})

                        if self.__reg.verbose:
                            self.__reg.log.write(f"+{self.__class_name__}.__detectOtherPossibleFormatAsErrorOfLegacyMr() "
                                                 f"++ Error  - {err}\n")

        except ValueError:
            pass

        return is_valid, err, genuine_type, valid_types, possible_types

    def retrieveOriginalFileExtensionOfCyanaMrFile(self) -> Optional[str]:
        """ Retrieve original file extension of CYANA MR file.
        """

        if self.__cur_original_ar_file_name is None:
            return None

        if self.__cur_original_ar_file_name.endswith('.gz'):
            self.__cur_original_ar_file_name = os.path.splitext(self.__cur_original_ar_file_name)[0]

        if self.__cur_original_ar_file_name.endswith('.mr'):
            return None

        if self.__cur_original_ar_file_name.endswith('-corrected'):
            self.__cur_original_ar_file_name = self.__cur_original_ar_file_name.replace('-corrected', '')

        if self.__cur_original_ar_file_name.endswith('.txt'):
            self.__cur_original_ar_file_name = self.__cur_original_ar_file_name.replace('.txt', '')

        if self.__cur_original_ar_file_name.endswith('.tbl'):
            self.__cur_original_ar_file_name = self.__cur_original_ar_file_name.replace('.tbl', '')

        if self.__cur_original_ar_file_name.endswith('.dat'):
            self.__cur_original_ar_file_name = self.__cur_original_ar_file_name.replace('.dat', '')

        if self.__cur_original_ar_file_name.endswith('.10'):
            self.__cur_original_ar_file_name = self.__cur_original_ar_file_name.replace('.10', '')

        split_ext = os.path.splitext(self.__cur_original_ar_file_name)

        if len(split_ext) != 2 or len(split_ext[1]) == 0:

            file_ext = split_ext[0].lower()

            if len(file_ext) > 3:

                file_ext = file_ext[len(file_ext) - 3:]

                if file_ext not in CYANA_MR_FILE_EXTS:
                    return None

                return file_ext

            if len(file_ext) == 3:

                if file_ext not in CYANA_MR_FILE_EXTS:
                    return None

                return file_ext

            return None

        file_ext = split_ext[1][1:].lower()

        if len(file_ext) > 3:
            file_ext = file_ext[:3]

        if file_ext not in CYANA_MR_FILE_EXTS:
            return None

        return file_ext
