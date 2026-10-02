##
# File: CifReader.py derived from wwpdb.apps.ccmodule.io.ChemCompIo.py
# Date: 31-May-2010  John Westbrook
#
# Update:
# 06-Aug-2010 - jdw - generalized construction of methods to apply to any category
#                     add accessors for lists of dictionaries
# 12-May-2011 - rps - added check for None when asking for category Object in __getDataList()
# 24-Oct-2012 - rps - updated to reflect reorganization of modules in pdbx packages
# 23-Jul-2019 - my  - forked original code to wwpdb.util.nmr.CifReader
# 30-Jul-2019 - my  - add 'range-float' as filter item type
# 05-Aug-2019 - my  - add 'enum' as filter item type
# 28-Jan-2020 - my  - add 'withStructConf' option of getPolymerSequence
# 19-Mar-2020 - my  - add hasItem()
# 24-Mar-2020 - my  - add 'identical_chain_id' in results of getPolymerSequence()
# 15-Apr-2020 - my  - add 'total_models' option of getPolymerSequence (DAOTHER-4060)
# 19-Apr-2020 - my  - add random rotation test for detection of non-superimposed models (DAOTHER-4060)
# 08-May-2020 - my  - make sure parse() is run only once (DAOTHER-5654)
# 20-Nov-2020 - my  - additional support for insertion code in getPolymerSequence() (DAOTHER-6128)
# 29-Jun-2021 - my  - add 'auth_chain_id', 'identical_auth_chain_id' in results of getPolymerSequence() if possible (DAOTHER-7108)
# 14-Jan-2022 - my  - precise RMSD calculation with domain and medoid model identification (DAOTHER-4060, 7544)
# 02-Feb-2022 - my  - add 'abs-int', 'abs-float', 'range-int', 'range-abs-int', 'range-abs-float'
#                     as filter item types and 'not_equal_to' range filter (NMR restraint remediation)
# 30-Mar-2022 - my  - add support for _atom_site.label_alt_id (DAOTHER-4060, 7544, NMR restraint remediation)
# 06-Apr-2022 - my  - add support for auth_comp_id (DAOTHER-7690)
# 04-Aug-2022 - my  - detect sequence gaps in auth_seq_id, 'gap_in_auth_seq' (NMR restraint remediation)
# 10-Feb-2023 - my  - add 'fetch_first_match' filter to process large assembly avoiding forced timeout (NMR restraint remediation)
# 14-Apr-2023 - my  - enable to use cache datablock (NMR restraint remediation)
# 19-Apr-2023 - my  - support multiple datablock (NMR restraint validation)
# 24-Apr-2023 - my  - add 'default' attribute for key items (NMR restraint validation)
# 18-Dec-2023 - my  - add calculate_uninstanced_coord() (DAOTHER-8945)
# 24-Jan-2024 - my  - add 'default-from' attribute for key/data items (D_1300043061)
# 21-Feb-2024 - my  - add support for discontinuous model_id (NMR restraint remediation, 2n6j)
# 07-Mar-2024 - my  - extract pdbx_poly_seq_scheme.auth_mon_id as alt_cmop_id to prevent sequence mismatch due to 5-letter CCD ID
#                     (DAOTHER-9158 vs D_1300043061)
# 20-Aug-2024 - my  - support truncated loop sequence in the model (DAOTHER-9644)
# 10-Sep-2024 - my  - ignore identical polymer sequence extensions within polynucleotide multiplexes (DAOTHER-9674)
# 18-Sep-2024 - my  - add 'starts-with-alnum' item type (DAOTHER-9694)
# 20-May-2026 - my  - add 'enum-int' as filter item type (DAOTHER-9785)
# 28-May-2026 - my  - avoid mosaic-like domain recognition (v1.0.7)
# 16-Jun-2025 - my  - set cache directory path (DAOTHER-9785)
# 10-Jul-2026 - my  - fill single gap in a domain (v1.0.8, 8vrc)
# 13-Jul-2026 - my  - implement ensemble composition analysis including cluster analysis (v1.0.9)
# 05-Aug-2026 - my  - performance enhancement on RMSD calculation (v1.1.0)
# 10-Sep-2026 - my  - run garbage collection periodically, add dbscan dependency if available (v1.2.0)
# 17-Sep-2026 - my  - revise cluster analysis incorporating multi-domain conformers like Calmodulin (v1.2.1, 2jt8)
# 18-Sep-2026 - my  - compile data/filter items once per call and index column values of a category
#                     in getDictListWithFilter() (performance enhancement)
# 18-Sep-2026 - my  - stop taking the absolute value of 'range-float' and 'range-int' filter items,
#                     which discarded row values outside the mirrored range
# 29-Sep-2026 - my  - add release() to drop the parsed data blocks between workflow operations (DAOTHER-7829, 9785)
# 29-Sep-2026 - my  - add getDistinctValues() and getFirstValue(), which scan a column without a dictionary per row
#                     (DAOTHER-7829, 9785)
# 02-Oct-2026 - my  - parse with SharingPdbxReader, which shares equal values among the parsed rows
#                     (6x63: 1313 MB -> 453 MB retained, 1330 MB -> 529 MB peak) (DAOTHER-7829, 9785)
# 02-Oct-2026 - my  - share the values in a copy of mmcif's tokenizer instead of wrapping it (parse time +30% -> +7%),
#                     and hash the file in chunks (text_md5()) (DAOTHER-7829, 9785)
# 03-Oct-2026 - my  - remove an unreadable data block cache, which was parsed around on every run, and write
#                     the cache atomically (DAOTHER-7829, 9785)
##
""" A collection of classes for parsing CIF files, extracting polymer sequence, and RMSD calculation.
"""
__docformat__ = "restructuredtext en"
__author__ = "John Westbrook, Masashi Yokochi"
__email__ = "jwest@rcsb.rutgers.edu, yokochi@protein.osaka-u.ac.jp"
__license__ = "Creative Commons Attribution 3.0 Unported"
__version__ = "1.2.1"

import collections
import copy
import gc
import hashlib
import inspect
import itertools
import math
import os
import pickle
import random
import re
import sys
import warnings
from operator import itemgetter
from typing import Any, IO, List, Optional, Tuple

from mmcif.api.PdbxContainers import DataContainer
from mmcif.io.PdbxReader import PdbxReader

import numpy

from rmsd.calculate_rmsd import (centroid, check_reflections,  # noqa: F401,E501 pylint: disable=no-name-in-module,import-error,unused-import,line-too-long
                                 kabsch_rmsd, quaternion_rmsd, quaternion_rotate,
                                 reorder_brute, reorder_distance, reorder_hungarian,
                                 rmsd)

from scipy.spatial.distance import pdist, squareform

try:
    from dbscan import DBSCAN
    SKLEARN_DBSCAN = False
except ImportError:
    from sklearn.cluster import DBSCAN
    SKLEARN_DBSCAN = True

try:
    from wwpdb.utils.nmr.NmrDpConstant import (SUB_DIR_NAME_FOR_CACHE,
                                               EMPTY_VALUE,
                                               TRUE_VALUE,
                                               ELEMENT_SYMBOLS,
                                               LEN_MAJOR_ASYM_ID,
                                               RMSD_OVERLAID_EXACTLY,
                                               RMSD_CUTOFF_FOR_DOMAIN,
                                               CARTN_DATA_ITEMS,
                                               text_md5)
except ImportError:
    from nmr.NmrDpConstant import (SUB_DIR_NAME_FOR_CACHE,
                                   EMPTY_VALUE,
                                   TRUE_VALUE,
                                   ELEMENT_SYMBOLS,
                                   LEN_MAJOR_ASYM_ID,
                                   RMSD_OVERLAID_EXACTLY,
                                   RMSD_CUTOFF_FOR_DOMAIN,
                                   CARTN_DATA_ITEMS,
                                   text_md5)

# throw RuntimeWarning as error for bug tracking, any runtimewarning should be handled
warnings.filterwarnings('error', category=RuntimeWarning, module='CifReader')

# must be one of kabsch_rmsd, quaternion_rmsd, None
# kabsch_rmsd is a fully-vectorized Kabsch (P.T@Q matmul + 3x3 SVD); it scales
# better on large N than quaternion_rmsd (Python per-atom loop in quaternion_rotate)
ROTATION_METHOD = kabsch_rmsd
# must be one of reorder_hungarian, reorder_brute, reorder_distance, None
REORDER_METHOD = reorder_hungarian
# scan through reflections in planes (e.g. Y transformed to -Y -> X, -Y, Z) and axis changes,
# (e.g. X and Z coords exchanged -> Z, Y, X). This will affect stereo-chemistry
USE_REFLECTIONS = False
# scan through reflections in planes (e.g. Y transformed to -Y -> X, -Y, Z) and axis changes,
# (e.g. X and Z coords exchanged -> Z, Y, X). Stereo-chemistry will be kept
# Disabled: for ensemble RMSD the atoms already correspond 1:1 by (chain_id, seq_id)
# order and conformers differ by a proper rotation (never a reflection), so the
# check_reflections()/reorder_hungarian() scan is unnecessary. Keeping it True made
# every calculate_rmsd() call ~24*O(N^3) (24 reflections x Hungarian) instead of the
# O(N) Kabsch superposition reached via ROTATION_METHOD below.
USE_REFLECTIONS_KEEP_STEREO = False
REORDER = False

# allowed item types
CIF_ITEM_TYPES = ('str', 'bool',
                  'int', 'range-int', 'abs-int', 'range-abs-int',
                  'float', 'range-float', 'abs-float', 'range-abs-float',
                  'enum', 'enum-int', 'starts-with-alnum')

# item types whose filter item carries a 'range' dictionary
CIF_RANGE_ITEM_TYPES = ('range-int', 'range-abs-int', 'range-float', 'range-abs-float')

# value conversion applied to a row value before the post check of a filter item
CONV_NONE, CONV_ALNUM, CONV_BOOL, CONV_INT, CONV_FLOAT, CONV_ABS_INT, CONV_ABS_FLOAT = range(7)

# conversion of each filter item type, CONV_ABS_FLOAT being the fall-through
CIF_FILTER_CONVERSIONS = {'str': CONV_NONE,
                          'enum': CONV_NONE,
                          'starts-with-alnum': CONV_ALNUM,
                          'bool': CONV_BOOL,
                          'int': CONV_INT,
                          'enum-int': CONV_INT,
                          'range-int': CONV_INT,
                          'float': CONV_FLOAT,
                          'range-float': CONV_FLOAT,
                          'abs-int': CONV_ABS_INT,
                          'range-abs-int': CONV_ABS_INT}

# post check of a filter item
POST_RANGE, POST_ENUM, POST_EQUAL = range(3)

# value conversion applied to a data item value
DATA_STR, DATA_ALNUM, DATA_BOOL, DATA_INT, DATA_FLOAT = range(5)

# conversion of each data item type, DATA_FLOAT being the fall-through
CIF_DATA_CONVERSIONS = {'str': DATA_STR,
                        'enum': DATA_STR,
                        'starts-with-alnum': DATA_ALNUM,
                        'bool': DATA_BOOL,
                        'int': DATA_INT,
                        'enum-int': DATA_INT}

# set of empty values, for O(1) membership test in the row loops
EMPTY_VALUE_SET = frozenset(EMPTY_VALUE)

# minimum number of rows of a category before a column value index is built
MIN_ROWS_FOR_COLUMN_INDEX = 1000

# maximum number of indexed columns per category
MAX_INDEXED_COLUMNS_PER_CATEGORY = 8

# threshold for garbage collection for high memory usage of DBSCAN
GARBAGE_COLLECTION_CYCLES = 32 if SKLEARN_DBSCAN else 128


# the mmCIF token regex of mmcif.io.PdbxReader.__tokenizer()
MMCIF_TOKEN_PAT = re.compile(r"(?:"
                             r"(?:_(.+?)[.](\S+))"  # _category.attribute
                             r"|"
                             r"(?:['](.*?)(?:[']\s|[']$))"  # single quoted strings
                             r"|"
                             r'(?:["](.*?)(?:["]\s|["]$))'  # double quoted strings
                             r"|"
                             r"(?:\s*#.*$)"  # comments (dumped)
                             r"|"
                             r"(\S+)"  # unquoted words
                             r")")


class SharingPdbxReader(PdbxReader):
    """ PdbxReader that shares one str object among equal values of the parsed rows.
        PdbxReader creates a new str for every value, e.g. 28.5 M values in 19.3 M str objects for the atom_site
        of a 134 MB CIF file (6x63), of which only 1.85 M are distinct; sharing them cuts the parsed data blocks
        from 1313 MB to 453 MB. The values themselves do not change.
        Sharing has to happen while tokenizing: re-sharing the values of already parsed rows frees the str
        objects but not the memory, which stays fragmented in the allocator.
        The tokenizer is that of mmcif.io.PdbxReader (Ethan Merritt, Jay Painter; mmcif, Apache License 2.0)
        with the sharing done where each token is made: wrapping the original generator instead cost 30%
        more parse time, this costs 7% (6x63: 22.3 s, wrapped 29.1 s, here 23.9 s).
        PdbxReader.read() calls its private tokenizer as self.__tokenizer, i.e. self._PdbxReader__tokenizer,
        which this class overrides, and keeps the line number for its error messages in
        self._PdbxReader__curLineNumber. Should mmcif rename the former, the override no longer applies and the
        parse falls back to unshared values; CifReaderTests detects both.
    """

    def _PdbxReader__tokenizer(self, ifh):  # pylint: disable=invalid-name
        """ Yield (category name, attribute name, quoted string, word without quotes or white space) per token.
        """

        pool = {}
        share = pool.setdefault
        finditer = MMCIF_TOKEN_PAT.finditer

        fileIter = iter(ifh)

        while True:
            try:
                line = next(fileIter)
                self._PdbxReader__curLineNumber += 1  # pylint: disable=no-member

                # dump comments
                if line.startswith('#'):
                    continue

                # gobble up the entire semi-colon/multi-line delimited string
                if line.startswith(';'):
                    mlString = [line[1:]]
                    while True:
                        line = next(fileIter)
                        self._PdbxReader__curLineNumber += 1  # pylint: disable=no-member
                        if line.startswith(';'):
                            break
                        mlString.append(line)

                    # remove trailing new-line that is part of the \n; delimiter
                    mlString[-1] = mlString[-1].rstrip()

                    quotedString = ''.join(mlString)
                    yield (None, None, share(quotedString, quotedString), None)

                    # process the remainder of the current line
                    line = line[1:]

                for it in finditer(line):
                    catName, attName, singleQuoted, doubleQuoted, word = it.groups()
                    if word is not None:
                        if word.lower() == 'stop_':
                            continue
                        yield (catName, attName, None, share(word, word))
                    elif singleQuoted is not None:
                        yield (catName, attName, share(singleQuoted, singleQuoted), None)
                    elif doubleQuoted is not None:
                        yield (catName, attName, share(doubleQuoted, doubleQuoted), None)
                    elif catName is not None or attName is not None:
                        yield (catName, attName, None, None)

            except StopIteration:
                return


def M(axis: list, theta: float) -> list:
    """ Return the rotation matrix associated with counterclockwise rotation
        about the given axis by theta radians.
    """

    axis = numpy.asarray(axis)
    axis = axis / math.sqrt(numpy.dot(axis, axis))
    a = math.cos(theta / 2.0)
    b, c, d = -axis * math.sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d

    return numpy.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                        [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                        [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]], dtype=float)


def to_np_array(a: dict) -> list:
    """ Return Numpy array of a given Cartesian coordinate
        in {'x': float, 'y': float, 'z': float} format.
    """

    return numpy.asarray([a['x'], a['y'], a['z']], dtype=float)


def get_coordinates(p: list
                    ) -> Tuple[list, list]:
    """ Convert list of atoms for RMSD calculation.
        @return: a vector set of the coordinates
    """

    V = []

    for a in p:
        V.append(a['v'] if 'v' in a else to_np_array(a))

    atoms = [ELEMENT_SYMBOLS[a['element']] for a in p]

    V = numpy.asarray(V)
    atoms = numpy.asarray(atoms)

    assert V.shape[0] == atoms.size

    return atoms, V


def calculate_rmsd(p: list, q: list) -> float:
    """ Calculate RMSD of two coordinates.
        @return: RMSD value
    """

    p_atoms, p_coord = get_coordinates(p)
    q_atoms, q_coord = get_coordinates(q)

    p_size = len(p_atoms)
    q_size = len(q_atoms)

    assert p_size > 0 and q_size > 0
    assert p_size == q_size
    assert p_coord.shape[0] == q_coord.shape[0]
    assert numpy.count_nonzero(p_atoms != q_atoms) == 0 or REORDER

    p_cent = centroid(p_coord)
    q_cent = centroid(q_coord)

    p_coord -= p_cent
    q_coord -= q_cent

    result_rmsd = None

    if USE_REFLECTIONS or USE_REFLECTIONS_KEEP_STEREO:
        if 'rmsd_method' in inspect.getfullargspec(check_reflections).args:  # API changed - detect
            result_rmsd, _, _, q_review = check_reflections(p_atoms, q_atoms,  # pylint: disable=unexpected-keyword-arg
                                                            p_coord, q_coord,
                                                            reorder_method=REORDER_METHOD,
                                                            rmsd_method=ROTATION_METHOD,
                                                            keep_stereo=USE_REFLECTIONS_KEEP_STEREO)
        else:
            result_rmsd, _, _, q_review = check_reflections(p_atoms, q_atoms,  # pylint: disable=unexpected-keyword-arg
                                                            p_coord, q_coord,
                                                            reorder_method=REORDER_METHOD,
                                                            rotation_method=ROTATION_METHOD,
                                                            keep_stereo=USE_REFLECTIONS_KEEP_STEREO)

    elif REORDER:
        q_review = REORDER_METHOD(p_atoms, q_atoms, p_coord, q_coord)
        q_coord = q_coord[q_review]
        q_atoms = q_atoms[q_review]
        assert numpy.count_nonzero(p_atoms != q_atoms) == 0

    if result_rmsd is not None:
        pass

    elif ROTATION_METHOD is None:
        result_rmsd = rmsd(p_coord, q_coord)

    else:
        result_rmsd = ROTATION_METHOD(p_coord, q_coord)

    return result_rmsd


def calculate_uninstanced_coord(p_coord: list, q_coord: list, s_coord: list
                                ) -> Tuple[list, float]:
    """ Calculate RMSD of two reference coordinates (p_coord, q_coord)
        and complement missing coordinate (s_coord). (DAOTHER-8945)
        @return: complemented coordinates, RMSD value
    """

    assert p_coord.shape[0] == q_coord.shape[0]

    p_cent = centroid(p_coord)
    q_cent = centroid(q_coord)

    p_coord -= p_cent
    s_coord -= p_cent
    q_coord -= q_cent

    rot = quaternion_rotate(p_coord, q_coord)
    p_coord = numpy.dot(p_coord, rot)

    s_coord = numpy.dot(s_coord, rot)
    s_coord += q_cent

    return s_coord, quaternion_rmsd(p_coord, q_coord)


class CifReader:
    """ Accessor methods for parsing CIF files, extracting polymer sequence, and RMSD calculation.
    """
    __slots__ = ('__class_name__',
                 '__version__',
                 '__verbose',
                 '__log',
                 '__debug',
                 '__use_cache',
                 '__filePath',
                 '__dirPath',
                 '__cacheDirPath',
                 '__dBlockList',
                 '__dBlockNameList',
                 '__dBlock',
                 '__categoryNameList',
                 '__valueIndex',
                 '__hashCode',
                 '__cachePath',
                 '__random_rotaion_test',
                 '__single_model_rotation_test',
                 '__min_features_for_clustering',
                 '__max_features_for_clustering',
                 '__min_samples_for_clustering',
                 '__max_samples_for_clustering',
                 '__min_monomers_for_domain')

    def __init__(self, verbose: bool = True, log: IO = sys.stdout,
                 use_cache: bool = True) -> None:
        self.__class_name__ = self.__class__.__name__
        self.__version__ = __version__

        self.__verbose = verbose
        self.__log = log
        self.__debug = False

        # whether to use cache file
        self.__use_cache = use_cache

        # the current file path
        self.__filePath = None

        # the current working directory
        self.__dirPath = None

        # directory for cache files
        self.__cacheDirPath = None

        # the datablock list
        self.__dBlockList = None

        # the current list of datablock names
        self.__dBlockNameList = None

        # the primary datablock
        self.__dBlock = None

        # the category name list
        self.__categoryNameList = None

        # column value indices of the current datablock, {(category name, column index, conversion): {value: [row]}}
        self.__valueIndex = {}

        # hash code of current cif file
        self.__hashCode = None

        # cache file path
        self.__cachePath = None

        # random rotation test for detection of non-superimposed models (DAOTHER-4060)
        self.__random_rotaion_test = False
        self.__single_model_rotation_test = True

        if self.__random_rotaion_test:
            self.__log.write(f"+{self.__class_name__}.__init__() ++ Warning  - Enabled random rotation test\n")
            self.__log.write(f"+{self.__class_name__}.__init__() "
                             f"++ Warning  - Single model rotation test: {self.__single_model_rotation_test}\n")

        # clustering parameters for recognition of well-defined regions
        self.__min_features_for_clustering = 4
        self.__max_features_for_clustering = 10
        self.__min_samples_for_clustering = 2
        self.__max_samples_for_clustering = 6

        # minimum monomers for domain recognition
        self.__min_monomers_for_domain = 12

        # must be greater than 6 to prevent the 6xHIS tag from being recognized as a well-defined region
        assert self.__min_monomers_for_domain > 6

    @property
    def version(self) -> str:
        """ Retrieve software version.
        """

        return __version__

    @property
    def cacheDirPath(self) -> Optional[str]:
        """ Retrieve cache directory path.
        """

        return self.__cacheDirPath

    @cacheDirPath.setter
    def cacheDirPath(self, cacheDirPath: Optional[str]) -> None:
        """ Set cache directory path.
        """

        self.__cacheDirPath = cacheDirPath

        if self.__use_cache and cacheDirPath is not None:
            if not os.path.isdir(cacheDirPath):
                os.makedirs(cacheDirPath)

    def parse(self, filePath: str) -> bool:
        """ Parse CIF file, and set internal active datablock if possible.
            @return: True for success or False otherwise
        """

        if self.__dBlock is not None and self.__filePath == filePath:
            return True

        self.__dBlockList = None
        self.__dBlockNameList = None
        self.__categoryNameList = None
        self.__valueIndex = {}

        self.__dBlock = None
        self.__hashCode = None

        self.__filePath = filePath

        try:

            if not os.access(self.__filePath, os.R_OK):
                if self.__verbose:
                    self.__log.write(f"+{self.__class_name__} ++ Error  - Missing file {self.__filePath}\n")
                return False

            if self.__use_cache:
                self.__hashCode = text_md5(self.__filePath)

            return self.__setDataBlock(self.__getDataBlockFromFile())

        except Exception as e:  # pylint: disable=broad-exception-caught
            if self.__verbose and 'loop_ declaration outside of data_ block or save_ frame' not in str(e):
                self.__log.write(f"+{self.__class_name__} ++ Error  - Parse {self.__filePath} failed {str(e)}\n")
            return False

    def __getDataBlockFromFile(self, blockName: Optional[str] = None
                               ) -> Optional[DataContainer]:
        """ Worker method to read CIF file and set the target datablock.
            If no blockName is provided return the first datablock.
            @return: target datablock
        """

        self.__dirPath = os.path.dirname(self.__filePath)

        if self.__use_cache:

            if self.__cacheDirPath is None:
                self.__cacheDirPath = os.path.join(self.__dirPath, SUB_DIR_NAME_FOR_CACHE)

            if not os.path.isdir(self.__cacheDirPath):
                os.makedirs(self.__cacheDirPath)

            self.__cachePath = os.path.join(self.__cacheDirPath,
                                            f"{self.__hashCode}{'' if blockName is None else '_' + blockName}.pkl")

            if os.path.exists(self.__cachePath):

                try:

                    with open(self.__cachePath, 'rb') as ifh:
                        dBlock = pickle.load(ifh)
                        if dBlock is not None:
                            return dBlock

                    os.remove(self.__cachePath)

                except Exception:  # pylint: disable=broad-exception-caught
                    # an unreadable cache, e.g. one that refers to a module that is no longer installed or one that was
                    # cut short, must go: __setDataBlock() writes the cache only when there is none, so it would
                    # otherwise be parsed around on every run
                    try:
                        os.remove(self.__cachePath)
                    except OSError:
                        pass

        if self.__dBlockList is None:
            self.__dBlockList, self.__dBlockNameList = [], []
            self.__categoryNameList = {}

            with open(self.__filePath, 'r', encoding='utf-8') as ifh:
                pRd = SharingPdbxReader(ifh)
                pRd.read(self.__dBlockList)

                is_star = all(container.getType() == 'data' for container in self.__dBlockList)
                for container in self.__dBlockList:
                    if is_star or (not is_star and container.getType() != 'data'):
                        blockName = container.getName()
                        self.__dBlockNameList.append(blockName)

        if blockName is not None:
            for dBlock in self.__dBlockList:
                if dBlock.getType() == 'data' and dBlock.getName() == blockName:
                    return dBlock

        else:
            for dBlock in self.__dBlockList:
                if dBlock.getType() == 'data':
                    return dBlock

        return None

    def __setDataBlock(self, dataBlock: Optional[DataContainer] = None) -> bool:
        """ Assigns the input datablock as the active internal datablock.
            @return: True for success or False otherwise
        """

        self.__valueIndex = {}

        try:

            if dataBlock.getType() == 'data':
                self.__dBlock = dataBlock

                if self.__use_cache and not os.path.exists(self.__cachePath):
                    # write a complete cache or none: a dump cut short would leave an unreadable cache behind
                    tmpPath = f'{self.__cachePath}.{os.getpid()}.tmp'
                    try:
                        with open(tmpPath, 'wb') as ofh:
                            pickle.dump(dataBlock, ofh)
                        os.replace(tmpPath, self.__cachePath)
                    finally:
                        if os.path.exists(tmpPath):
                            os.remove(tmpPath)

                return True

        except Exception:  # pylint: disable=broad-exception-caught
            pass

        self.__dBlock = None

        return False

    def release(self) -> None:
        """ Release the parsed data blocks, which dominate the memory of this reader for a large structure
            (1.28 GB for a 134 MB CIF file of 1.36 M atoms). The file path is kept, and the next parse() re-reads the file,
            because it reuses the parsed data only while the data block is present.
        """

        self.__dBlockList = None
        self.__dBlockNameList = None
        self.__categoryNameList = None
        self.__valueIndex = {}
        self.__dBlock = None

    def getDirPath(self) -> str:
        """ Return directory path of CIF file.
        """

        return self.__dirPath

    def getFilePath(self) -> str:
        """ Return CIF file path.
        """

        return self.__filePath

    def getHashCode(self) -> str:
        """ Return hash code of the CIF file.
        """

        if self.__hashCode is None:
            self.__hashCode = text_md5(self.__filePath)

        return self.__hashCode

    def getDataBlockList(self) -> List[DataContainer]:
        """ Return list of datablocks.
        """

        return self.__dBlockList

    def getDataBlockNameList(self) -> List[str]:
        """ Return list of datablock names.
        """

        return self.__dBlockNameList

    def getDataBlock(self, blockName: Optional[str] = None
                     ) -> Optional[DataContainer]:
        """ Return target datablock.
            Return None in case current blockName does not exist or no blockName does not match.
            @return: target datablock
        """

        if self.__dBlock is None or self.__dBlock.getType() != 'data':
            return None

        if blockName is None or self.__dBlock.getName() == blockName:
            return self.__dBlock

        dBlock = self.__getDataBlockFromFile(blockName)

        return dBlock if self.__setDataBlock(dBlock) else None

    def getCategoryNameList(self, blockName: Optional[str] = None
                            ) -> List[str]:
        """ Return all category names in a given datablock.
        """

        if blockName is not None and self.__dBlock is not None and self.__dBlock.getName() != blockName:
            self.__setDataBlock(self.getDataBlock(blockName))

        if self.__dBlock is None:
            return []

        if self.__categoryNameList is None:
            self.__categoryNameList = {}

        if blockName in self.__categoryNameList:
            return self.__categoryNameList[blockName]

        try:

            categoryNameList = self.__dBlock.getObjNameList()

            return categoryNameList

        finally:
            self.__categoryNameList[blockName] = categoryNameList

    def hasCategory(self, catName: str, blockName: Optional[str] = None) -> bool:
        """ Return whether a given category exists.
        """

        return catName in self.getCategoryNameList(blockName)

    def hasItem(self, catName: str, itName: str, blockName: Optional[str] = None) -> bool:
        """ Return whether a given item exists in a category.
        """

        if blockName is not None and self.__dBlock is not None and self.__dBlock.getName() != blockName:
            self.__setDataBlock(self.getDataBlock(blockName))

        if self.__dBlock is None:
            return False

        catObj = self.__dBlock.getObj(catName)

        if catObj is None:
            return False

        return itName in catObj.getAttributeList()

    def getAttributeList(self, catName: str, blockName: Optional[str] = None
                         ) -> List[str]:
        """ Return item names of a given category.
        """

        if blockName is not None and self.__dBlock is not None and self.__dBlock.getName() != blockName:
            self.__setDataBlock(self.getDataBlock(blockName))

        if self.__dBlock is None:
            return []

        catObj = self.__dBlock.getObj(catName)

        if catObj is None:
            return []

        return catObj.getAttributeList()

    def getRowLength(self, catName: str, blockName: Optional[str] = None) -> int:
        """ Return length of rows of a given category.
        """

        if blockName is not None and self.__dBlock is not None and self.__dBlock.getName() != blockName:
            self.__setDataBlock(self.getDataBlock(blockName))

        if self.__dBlock is None:
            return 0

        catObj = self.__dBlock.getObj(catName)

        if catObj is not None:
            return len(catObj.getRowList())

        return 0

    def getRowList(self, catName: str, blockName: Optional[str] = None
                   ) -> List[list]:
        """ Return length of rows of a given category.
        """

        if blockName is not None and self.__dBlock is not None and self.__dBlock.getName() != blockName:
            self.__setDataBlock(self.getDataBlock(blockName))

        if self.__dBlock is None:
            return []

        catObj = self.__dBlock.getObj(catName)

        if catObj is not None:
            return catObj.getRowList()

        return []

    def getDictList(self, catName: str, blockName: Optional[str] = None
                    ) -> List[dict]:
        """ Return a list of dictionaries of a given category.
        """

        if blockName is not None and self.__dBlock is not None and self.__dBlock.getName() != blockName:
            self.__setDataBlock(self.getDataBlock(blockName))

        if self.__dBlock is None:
            return []

        catObj = self.__dBlock.getObj(catName)

        if catObj is None:
            return []

        iList = catObj.getAttributeList()

        dList = []
        for row in catObj.getRowList():
            dList.append({itName: row[idxIt] for idxIt, itName in enumerate(iList)})

        return dList

    def __getItemColumn(self, catName: str, itemName: str, blockName: Optional[str]
                        ) -> Tuple[Optional[List[list]], int]:
        """ Return the row list and the column index of a data item, with the same data block switching, empty
            results and LookupError as getDictListWithFilter() for a single data item.
        """

        if blockName is not None and self.__dBlock is not None and self.__dBlock.getName() != blockName:
            self.__setDataBlock(self.getDataBlock(blockName))

        if self.__dBlock is None:
            return None, -1

        catObj = self.__dBlock.getObj(catName)

        if catObj is None:
            return None, -1

        iList = catObj.getAttributeList()

        if itemName not in iList:
            raise LookupError(f"Missing one of data items {[itemName]}.")

        return catObj.getRowList(), iList.index(itemName)

    def getDistinctValues(self, catName: str, itemName: str, itemType: str = 'str',
                          blockName: Optional[str] = None) -> set:
        """ Return the distinct values of a data item, converted as getDictListWithFilter() converts a data item
            of the given type without 'default', i.e. the set of d[itemName] over
            getDictListWithFilter(catName, [{'name': itemName, 'type': itemType}]), without a dictionary per row:
            that list cost +263 MB for the 1.36 M atom_site rows of 6x63 only to collect the model numbers
            (DAOTHER-7829, 9785). Each value converts on its own, so converting the distinct raw values is equivalent.
        """

        if itemType not in CIF_ITEM_TYPES:
            raise TypeError(f"Type {itemType} of data item {itemName} must be one of {CIF_ITEM_TYPES}.")

        rowList, idxIt = self.__getItemColumn(catName, itemName, blockName)

        if rowList is None:
            return set()

        conv = CIF_DATA_CONVERSIONS.get(itemType, DATA_FLOAT)

        values = set()

        for val in {row[idxIt] for row in rowList}:
            if val in EMPTY_VALUE_SET:
                val = None
            if conv == DATA_ALNUM:
                if not val[0].isalnum() and val[0] != "'":  # same as __buildDictList(), incl. its TypeError on None
                    val = None
            elif conv == DATA_BOOL:
                val = val.lower() in TRUE_VALUE
            elif conv == DATA_INT:
                if val is not None:
                    try:
                        val = int(val)
                    except ValueError:
                        val = None
            elif conv == DATA_FLOAT and val is not None:
                val = float(val)
            values.add(val)

        return values

    def getFirstValue(self, catName: str, itemName: str, blockName: Optional[str] = None) -> Optional[str]:
        """ Return the first non-empty value of a data item in row order, or None; i.e. the first d[itemName] not in
            EMPTY_VALUE over getDictListWithFilter(catName, [{'name': itemName, 'type': 'str'}]), without a
            dictionary per row (DAOTHER-7829, 9785).
        """

        rowList, idxIt = self.__getItemColumn(catName, itemName, blockName)

        if rowList is None:
            return None

        for row in rowList:
            if row[idxIt] not in EMPTY_VALUE_SET:
                return row[idxIt]

        return None

    def getDictListWithFilter(self, catName: str, dataItems: List[dict], filterItems: Optional[List[dict]] = None,
                              blockName: Optional[str] = None
                              ) -> List[dict]:
        """ Return a list of dictionaries of a given category with filter.
        """

        dataNames = [d['name'] for d in dataItems]

        for d in dataItems:
            if d['type'] not in CIF_ITEM_TYPES:
                raise TypeError(f"Type {d['type']} of data item {d['name']} must be one of {CIF_ITEM_TYPES}.")

        filterNames = None
        if filterItems is not None:
            filterNames = [f['name'] for f in filterItems]

            for f in filterItems:
                if f['type'] not in CIF_ITEM_TYPES:
                    raise TypeError(f"Type {f['type']} of filter item {f['name']} must be one of {CIF_ITEM_TYPES}.")

        if blockName is not None and self.__dBlock is not None and self.__dBlock.getName() != blockName:
            self.__setDataBlock(self.getDataBlock(blockName))

        if self.__dBlock is None:
            return []

        catObj = self.__dBlock.getObj(catName)

        if catObj is None:
            return []

        # get column name index
        iList = catObj.getAttributeList()

        colDict = {itName: idxIt for idxIt, itName in enumerate(iList)}

        if set(dataNames) & set(iList) != set(dataNames):
            raise LookupError(f"Missing one of data items {dataNames}.")

        if filterItems is not None and set(filterNames) & set(iList) != set(filterNames):
            raise LookupError(f"Missing one of filter items {filterNames}.")

        rowList = catObj.getRowList()

        if filterItems:

            plan = self.__compileFilterPlan(filterItems, colDict)

            if plan is None:  # 'fetch_first_match' filter, or a filter item that lacks its 'value'
                rowList = self.__filterRowsRowWise(rowList, filterItems, colDict)

            else:
                rowList, plan = self.__narrowRowsByColumnIndex(catName, rowList, plan)

                for idxIt, conv, post, payload, emptyRejects in plan:
                    if len(rowList) == 0:
                        break
                    rowList = self.__filterRows(rowList, idxIt, conv, post, payload, emptyRejects)

        return self.__buildDictList(rowList, dataItems, colDict, set(dataNames))

    def __compileFilterPlan(self, filterItems: List[dict], colDict: dict) -> Optional[List[tuple]]:  # pylint: disable=no-self-use
        """ Compile filter items to a list of (column index, value conversion, post check, payload,
            whether an empty value is rejected), so that the per-item decisions are made once per call
            instead of once per row.
            @return: the compiled filter plan, None if the filter items must be processed row-wise
        """

        plan = []

        for filterItem in filterItems:

            if 'fetch_first_match' in filterItem and filterItem['fetch_first_match']:
                return None  # 'abort' depends on the row order

            filterItemType = filterItem['type']

            # CONV_ABS_FLOAT is the fall-through, which covers 'abs-float' and 'range-abs-float'
            conv = CIF_FILTER_CONVERSIONS.get(filterItemType, CONV_ABS_FLOAT)

            if filterItemType in CIF_RANGE_ITEM_TYPES:
                post, payload = POST_RANGE, filterItem['range']
            elif filterItemType in ('enum', 'enum-int'):
                post, payload = POST_ENUM, frozenset(filterItem['enum'])
            elif 'value' not in filterItem:
                return None  # the row-wise code path raises KeyError, but only once a row reaches the comparison
            else:
                post, payload = POST_EQUAL, filterItem['value']

            plan.append((colDict[filterItem['name']], conv, post, payload,
                         'value' in filterItem and filterItem['value'] not in EMPTY_VALUE_SET))

        return plan

    def __filterRows(self, rowList: List[list], idxIt: int, conv: int, post: int, payload: Any,  # pylint: disable=no-self-use
                     emptyRejects: bool) -> List[list]:
        """ Return rows that satisfy a compiled filter item.
        """

        if conv == CONV_NONE:  # no value conversion, which is the common case

            if post == POST_EQUAL:
                if emptyRejects:
                    return [row for row in rowList if row[idxIt] == payload]
                return [row for row in rowList if row[idxIt] in EMPTY_VALUE_SET]

            if post == POST_ENUM:
                enum = payload - EMPTY_VALUE_SET
                if emptyRejects:
                    return [row for row in rowList if row[idxIt] in enum]
                return [row for row in rowList if row[idxIt] in enum or row[idxIt] in EMPTY_VALUE_SET]

        _rowList = []

        for row in rowList:
            val = row[idxIt]

            if val in EMPTY_VALUE_SET:
                if not emptyRejects:
                    _rowList.append(row)
                continue

            if conv == CONV_ALNUM:
                if not val[0].isalnum() and val[0] != "'":  # allow apostrophe in starts-with-alnum filter type (6hmo)
                    continue
            elif conv == CONV_BOOL:
                val = val.lower() in TRUE_VALUE
            elif conv != CONV_NONE:
                try:
                    if conv == CONV_INT:
                        val = int(val)
                    elif conv == CONV_FLOAT:
                        val = float(val)
                    elif conv == CONV_ABS_INT:
                        val = abs(int(val))
                    else:
                        val = abs(float(val))
                except ValueError:
                    continue

            if post == POST_RANGE:
                if ('min_exclusive' in payload and val <= payload['min_exclusive'])\
                   or ('min_inclusive' in payload and val < payload['min_inclusive'])\
                   or ('max_inclusive' in payload and val > payload['max_inclusive'])\
                   or ('max_exclusive' in payload and val >= payload['max_exclusive'])\
                   or ('not_equal_to' in payload and val == payload['not_equal_to']):
                    continue
            elif post == POST_ENUM:
                if val not in payload:
                    continue
            elif val != payload:
                continue

            _rowList.append(row)

        return _rowList

    def __filterRowsRowWise(self, rowList: List[list], filterItems: List[dict], colDict: dict  # pylint: disable=no-self-use
                            ) -> List[list]:
        """ Return rows that satisfy filter items, evaluating the filter items in order for each row.
            Required by the 'fetch_first_match' filter, whose 'abort' depends on the row order.
        """

        fetchDict = {}  # 'fetch_first_match': True

        abort = False

        _rowList = []

        for row in rowList:
            keep = True
            for filterItem in filterItems:
                name = filterItem['name']
                val = row[colDict[name]]
                if val in EMPTY_VALUE:
                    if 'value' in filterItem and filterItem['value'] not in EMPTY_VALUE:
                        keep = False
                        break
                else:
                    filterItemType = filterItem['type']
                    if filterItemType in ('str', 'enum'):
                        pass
                    elif filterItemType == 'starts-with-alnum':
                        if not val[0].isalnum() and val[0] != "'":  # allow apostrophe in starts-with-alnum filter type (6hmo)
                            keep = False
                            break
                    elif filterItemType == 'bool':
                        val = val.lower() in TRUE_VALUE
                    elif filterItemType in ('int', 'enum-int', 'range-int'):
                        try:
                            val = int(val)
                        except ValueError:
                            keep = False
                            break
                    elif filterItemType in ('float', 'range-float'):
                        try:
                            val = float(val)
                        except ValueError:
                            keep = False
                            break
                    elif filterItemType in ('abs-int', 'range-abs-int'):
                        try:
                            val = abs(int(val))
                        except ValueError:
                            keep = False
                            break
                    else:  # 'abs-float', 'range-abs-float'
                        try:
                            val = abs(float(val))
                        except ValueError:
                            keep = False
                            break
                    if filterItemType in ('range-int', 'range-abs-int', 'range-float', 'range-abs-float'):
                        _range = filterItem['range']
                        if ('min_exclusive' in _range and val <= _range['min_exclusive'])\
                           or ('min_inclusive' in _range and val < _range['min_inclusive'])\
                           or ('max_inclusive' in _range and val > _range['max_inclusive'])\
                           or ('max_exclusive' in _range and val >= _range['max_exclusive'])\
                           or ('not_equal_to' in _range and val == _range['not_equal_to']):
                            keep = False
                            break
                    elif filterItemType == 'enum':
                        if val not in filterItem['enum']:
                            keep = False
                            break
                        if 'fetch_first_match' in filterItem and filterItem['fetch_first_match']:
                            if name not in fetchDict:
                                fetchDict[name] = val
                            elif val != fetchDict[name]:
                                keep = False
                                abort = True
                                break
                    elif filterItemType == 'enum-int':
                        if val not in filterItem['enum']:
                            keep = False
                            break
                        if 'fetch_first_match' in filterItem and filterItem['fetch_first_match']:
                            if name not in fetchDict:
                                fetchDict[name] = val
                            elif val != fetchDict[name]:
                                keep = False
                                abort = True
                                break
                    else:
                        if val != filterItem['value']:
                            keep = False
                            break
                        if 'fetch_first_match' in filterItem and filterItem['fetch_first_match']:
                            if name not in fetchDict:
                                fetchDict[name] = val
                            elif val != fetchDict[name]:
                                keep = False
                                abort = True
                                break

            if keep:
                _rowList.append(row)

            elif abort:
                break

        return _rowList

    def __narrowRowsByColumnIndex(self, catName: str, rowList: List[list], plan: List[tuple]
                                  ) -> Tuple[List[list], List[tuple]]:
        """ Narrow candidate rows using a cached column value index of the most selective equality filter.
            @return: the candidate rows and the remaining filter plan
        """

        if len(rowList) < MIN_ROWS_FOR_COLUMN_INDEX:
            return rowList, plan

        best, bestRowList = -1, None

        for idx, (idxIt, conv, post, payload, emptyRejects) in enumerate(plan):

            # a single value lookup preserves the row order of the category, a union of values would not
            if post != POST_EQUAL or not emptyRejects or conv not in (CONV_NONE, CONV_INT, CONV_FLOAT):
                continue

            valueIndex = self.__getColumnIndex(catName, rowList, idxIt, conv)

            if valueIndex is None:
                continue

            try:
                _rowList = valueIndex.get(payload, [])
            except TypeError:  # unhashable filter value, which never matches a row value
                continue

            if bestRowList is None or len(_rowList) < len(bestRowList):
                best, bestRowList = idx, _rowList

        if bestRowList is None:
            return rowList, plan

        return bestRowList, plan[:best] + plan[best + 1:]

    def __getColumnIndex(self, catName: str, rowList: List[list], idxIt: int, conv: int) -> Optional[dict]:
        """ Return a value to rows index of a given column, building it on the first use.
            @return: the column value index, None if the category has too many indexed columns already
        """

        key = (catName, idxIt, conv)

        if key in self.__valueIndex:
            return self.__valueIndex[key]

        if sum(1 for _catName, _, _ in self.__valueIndex if _catName == catName) >= MAX_INDEXED_COLUMNS_PER_CATEGORY:
            return None

        valueIndex = {}

        for row in rowList:
            val = row[idxIt]
            if conv != CONV_NONE:
                if val in EMPTY_VALUE_SET:
                    continue
                try:
                    val = int(val) if conv == CONV_INT else float(val)
                except ValueError:
                    continue
            if val in valueIndex:
                valueIndex[val].append(row)
            else:
                valueIndex[val] = [row]

        self.__valueIndex[key] = valueIndex

        return valueIndex

    def __buildDictList(self, rowList: List[list], dataItems: List[dict], colDict: dict,  # pylint: disable=no-self-use
                        dataNames: set) -> List[dict]:
        """ Return a list of dictionaries of given rows.
        """

        plan = []

        for dataItem in dataItems:
            defaultFrom = dataItem.get('default-from')
            plan.append((dataItem['alt_name'] if 'alt_name' in dataItem else dataItem['name'],
                         colDict[dataItem['name']],
                         CIF_DATA_CONVERSIONS.get(dataItem['type'], DATA_FLOAT),
                         colDict[defaultFrom] if defaultFrom in dataNames else None,
                         dataItem.get('default')))

        dList = []

        for row in rowList:
            tD = {}
            for name, idxIt, conv, defaultFrom, default in plan:
                val = row[idxIt]
                if val in EMPTY_VALUE_SET:
                    val = row[defaultFrom] if defaultFrom is not None else default
                if conv == DATA_ALNUM:
                    if not val[0].isalnum() and val[0] != "'":  # allow apostrophe in starts-with-alnum filter type (6hmo)
                        val = None
                elif conv == DATA_BOOL:
                    val = val.lower() in TRUE_VALUE
                elif conv == DATA_INT:
                    if val is not None:
                        try:
                            val = int(val)
                        except ValueError:
                            val = None
                elif conv == DATA_FLOAT and val is not None:
                    val = float(val)
                tD[name] = val
            dList.append(tD)

        return dList

    def getPolymerSequence(self, catName: str, keyItems: List[dict],
                           withStructConf: bool = False, withRmsd: bool = False, alias: bool = False,
                           totalModels: int = 1, effModelIds: Optional[List[int]] = None, repAltId: str = 'A'
                           ) -> Tuple[List[dict], Optional[List[dict]]]:
        """ Extract sequence from a given loop in a CIF file.
        """

        keyNames = [k['name'] for k in keyItems]

        lenKeyItems = len(keyItems)

        if self.__dBlock is None:
            return [], None

        repModelId = effModelIds[0] if effModelIds is not None else 1

        # DAOTHER-9644: support for truncated loop in the model
        if withRmsd and catName == 'pdbx_poly_seq_scheme':  # avoid interference of ParserListenerUtils.coordAssemblyChecker()
            misPolyLink = []

            _catName = 'pdbx_validate_polymer_linkage'

            if self.hasCategory(_catName):
                _keyItems = [{'name': 'auth_asym_id_1', 'type': 'str', 'alt_name': 'auth_chain_id', 'default': 'A'},
                             {'name': 'auth_seq_id_1', 'type': 'int'},
                             {'name': 'auth_asym_id_2', 'type': 'str', 'alt_name': 'test_auth_chain_id', 'default': 'A'},
                             {'name': 'auth_seq_id_2', 'type': 'int'}
                             ]
                _filterItems = [{'name': 'PDB_model_num', 'type': 'int', 'value': repModelId},
                                {'name': 'label_alt_id_1', 'type': 'enum', 'enum': (repAltId,)},
                                {'name': 'label_alt_id_2', 'type': 'enum', 'enum': (repAltId,)}
                                ]

                for mis in self.getDictListWithFilter(_catName, _keyItems, _filterItems):
                    if mis['auth_chain_id'] == mis['test_auth_chain_id']:
                        del mis['test_auth_chain_id']
                        misPolyLink.append(mis)

        catObj = self.__dBlock.getObj(catName)

        if catObj is None:
            return [], None

        # get column name index
        itDict, altDict = {}, {}

        iList = catObj.getAttributeList()

        for idxIt, itName in enumerate(iList):
            itDict[itName] = idxIt
            if itName in keyNames:
                altDict[next(k['alt_name'] if 'alt_name' in k else itName for k in keyItems if k['name'] == itName)] = idxIt

        if set(keyNames) & set(itDict.keys()) != set(keyNames):
            raise LookupError(f"Missing one of data items {keyNames}.")

        # get row list
        rowList = catObj.getRowList()
        _rowList = None
        unmapSeqIds, unmapAuthSeqIds, mapAuthSeqIds = {}, {}, {}
        chainIdWoDefault = set()

        entityPoly = self.getDictList('entity_poly')

        etypes = set(e['type'] for e in entityPoly if 'pdbx_strand_id' in e)

        # DAOTHER-9674
        for row in rowList:
            for j in range(lenKeyItems):
                itCol = itDict[keyNames[j]]
                if itCol < len(row) and row[itCol] in EMPTY_VALUE:
                    if 'default-from' in keyItems[j] and keyItems[j]['default-from'] in keyNames:
                        if catName == 'pdbx_poly_seq_scheme':
                            if 'alt_name' in keyItems[j] and keyItems[j]['alt_name'] == 'auth_comp_id':
                                c = row[altDict['chain_id']]
                                etype = next((e['type'] for e in entityPoly
                                              if 'pdbx_strand_id' in e and c in e['pdbx_strand_id'].split(',')), None)
                                if etype is not None and 'polypeptide' not in etype:
                                    if c not in unmapSeqIds:
                                        unmapSeqIds[c], unmapAuthSeqIds[c] = [], []
                                    compId = row[altDict['comp_id']]
                                    if compId in EMPTY_VALUE or not compId[0].isalnum():  # DAOTHER-9694
                                        continue
                                    unmapSeqIds[c].append((row[altDict['seq_id']], compId))
                                    unmapAuthSeqIds[c].append(row[altDict['auth_seq_id']])
                                if _rowList is None:
                                    _rowList = copy.deepcopy(rowList)
                        continue
                    if 'default' not in keyItems[j]:  # or keyItems[j]['default'] not in EMPTY_VALUE:
                        raise ValueError(f"{keyNames[j]} must not be empty.")

        # DAOTHER-9674
        if catName == 'pdbx_poly_seq_scheme' and 'auth_comp_id' in altDict:
            for row in rowList:
                if row[altDict['auth_comp_id']] not in EMPTY_VALUE:
                    c = row[altDict['chain_id']]
                    etype = next((e['type'] for e in entityPoly
                                  if 'pdbx_strand_id' in e and c in e['pdbx_strand_id'].split(',')), None)
                    if etype is not None and 'polypeptide' not in etype:
                        if c not in mapAuthSeqIds:
                            mapAuthSeqIds[c] = []
                        compId = row[altDict['comp_id']]
                        if compId in EMPTY_VALUE or not compId[0].isalnum():  # DAOTHER-9694
                            continue
                        mapAuthSeqIds[c].append(row[altDict['auth_seq_id']])

        # DAOTHER-9674
        if len(unmapSeqIds) > 1:
            for i, j in itertools.combinations(unmapSeqIds.keys(), 2):
                if (i not in chainIdWoDefault or j not in chainIdWoDefault)\
                   and unmapSeqIds[i] == unmapSeqIds[j]\
                   and (len(unmapAuthSeqIds[i]) % len(mapAuthSeqIds[i]) == 0
                        or len(mapAuthSeqIds[i]) % len(unmapAuthSeqIds[i]) == 0):
                    chainIdWoDefault.add(i)
                    chainIdWoDefault.add(j)

            if len(chainIdWoDefault) > 1:
                rowList = []

                for row in _rowList:
                    skip = False
                    for j in range(lenKeyItems):
                        itCol = itDict[keyNames[j]]
                        if itCol < len(row) and row[itCol] in EMPTY_VALUE:
                            if 'default-from' in keyItems[j] and keyItems[j]['default-from'] in keyNames:
                                if catName == 'pdbx_poly_seq_scheme':
                                    if 'alt_name' in keyItems[j] and keyItems[j]['alt_name'] == 'auth_comp_id':
                                        c = row[altDict['chain_id']]
                                        if c in chainIdWoDefault:
                                            skip = True
                                            break
                                row[itCol] = row[itDict[keyItems[j]['default-from']]]
                    if not skip:
                        rowList.append(row)

        for row in rowList:
            for j in range(lenKeyItems):
                itCol = itDict[keyNames[j]]
                if itCol < len(row) and row[itCol] in EMPTY_VALUE:
                    if 'default-from' in keyItems[j] and keyItems[j]['default-from'] in keyNames:
                        if catName == 'pdbx_poly_seq_scheme':
                            if 'alt_name' in keyItems[j] and keyItems[j]['alt_name'] == 'auth_comp_id':
                                c = row[altDict['chain_id']]
                        row[itCol] = row[itDict[keyItems[j]['default-from']]]
                        continue
                    if 'default' in keyItems[j]:
                        row[itCol] = keyItems[j]['default']

        compDict, seqDict, insCodeDict, authSeqDict, labelSeqDict, authChainDict =\
            {}, {}, {}, {}, {}, {}

        chain_id_col = altDict['chain_id']
        seq_id_col = altDict['seq_id']
        comp_id_col = altDict['comp_id']
        ins_code_col = -1 if 'ins_code' not in altDict else altDict['ins_code']
        label_seq_col = seq_id_col if 'label_seq_id' not in altDict else altDict['label_seq_id']
        auth_chain_id_col = -1 if 'auth_chain_id' not in altDict else altDict['auth_chain_id']
        auth_seq_id_col = -1 if 'auth_seq_id' not in altDict else altDict['auth_seq_id']
        auth_comp_id_col = -1 if 'auth_comp_id' not in altDict else altDict['auth_comp_id']
        alt_comp_id_col = -1 if 'alt_comp_id' not in altDict else altDict['alt_comp_id']

        authScheme = auth_seq_id_col != -1

        chainIds = sorted(set(row[chain_id_col] for row in rowList), key=lambda x: (len(x), x))

        if ins_code_col == -1:
            if catName == 'pdbx_nonpoly_scheme':
                sortedSeq = sorted(set((row[chain_id_col], int(row[seq_id_col]), row[comp_id_col]) for row in rowList),
                                   key=itemgetter(1))
            else:
                sortedSeq = sorted(set((row[chain_id_col], int(row[seq_id_col]), row[comp_id_col]) for row in rowList),
                                   key=lambda x: (len(x[0]), x[0], x[1]))

            keyDict = {(row[chain_id_col], int(row[seq_id_col])): row[comp_id_col] for row in rowList}

            for row in rowList:
                key = (row[chain_id_col], int(row[seq_id_col]))
                if keyDict[key] != row[comp_id_col]:
                    raise KeyError(f"Sequence must be unique. {iList[chain_id_col]} {row[chain_id_col]}, "
                                   f"{iList[seq_id_col]} {row[seq_id_col]}, "
                                   f"{iList[comp_id_col]} {row[comp_id_col]} vs {keyDict[key]}.")

            for c in chainIds:
                compDict[c] = [x[2] for x in sortedSeq if x[0] == c]
                seqDict[c] = [x[1] for x in sortedSeq if x[0] == c]

        else:
            if catName == 'pdbx_nonpoly_scheme':
                sortedSeq = sorted(set((row[chain_id_col], int(row[seq_id_col]), row[ins_code_col],
                                        row[label_seq_col], row[comp_id_col])
                                       for row in rowList), key=itemgetter(1))
            else:
                if all(row[label_seq_col].isdigit() for row in rowList):
                    sortedSeq = sorted(set((row[chain_id_col], int(row[seq_id_col]), row[ins_code_col],
                                            int(row[label_seq_col]), row[comp_id_col])
                                           for row in rowList), key=lambda x: (len(x[0]), x[0], x[3]))
                else:
                    sortedSeq = sorted(set((row[chain_id_col], int(row[seq_id_col]), row[ins_code_col],
                                            row[label_seq_col], row[comp_id_col])
                                           for row in rowList), key=lambda x: (len(x[0]), x[0], x[1]))

            keyDict = {(row[chain_id_col], int(row[seq_id_col]), row[ins_code_col], row[label_seq_col]): row[comp_id_col]
                       for row in rowList}

            for row in rowList:
                key = (row[chain_id_col], int(row[seq_id_col]), row[ins_code_col], row[label_seq_col])
                if keyDict[key] != row[comp_id_col]:
                    raise KeyError(f"Sequence must be unique. {iList[chain_id_col]} {row[chain_id_col]}, "
                                   f"{iList[seq_id_col]} {row[seq_id_col]}, "
                                   f"{iList[ins_code_col]} {row[ins_code_col]}, "
                                   f"{iList[label_seq_col]} {row[label_seq_col]}, "
                                   f"{iList[comp_id_col]} {row[comp_id_col]} vs {keyDict[key]}.")

            for c in chainIds:
                compDict[c] = [x[4] for x in sortedSeq if x[0] == c]
                seqDict[c] = [x[1] for x in sortedSeq if x[0] == c]
                insCodeDict[c] = [x[2] for x in sortedSeq if x[0] == c]
                labelSeqDict[c] = [x[3] for x in sortedSeq if x[0] == c]

        chainIds = []
        for x in sortedSeq:
            if x[0] not in chainIds:
                chainIds.append(x[0])

        if auth_chain_id_col != -1:
            for row in rowList:
                c = row[chain_id_col]
                if c not in authChainDict:
                    authChainDict[c] = row[auth_chain_id_col]

        if authScheme:
            for c in chainIds:
                authSeqDict[c] = []
                for s in seqDict[c]:
                    row = next((row for row in rowList if row[chain_id_col] == c and int(row[seq_id_col]) == s), None)
                    if row is not None:
                        if row[auth_seq_id_col] not in EMPTY_VALUE:
                            try:
                                _s = int(row[auth_seq_id_col])
                            except ValueError:
                                _s = None
                            authSeqDict[c].append(_s)
                        else:
                            authSeqDict[c].append(None)

        largeAssembly = catName == 'pdbx_poly_seq_scheme' and len(chainIds) > LEN_MAJOR_ASYM_ID

        caRmsd = caWellDefinedRegion = None
        pRmsd = pWellDefinedRegion = None
        polyPeptideChains, polyPeptideLengths = [], []
        polyNucleotideChains, polyNucleotideLengths = [], []

        polymerLength = {c: len(seqDict[c]) for c in chainIds}

        asm = []  # assembly of a loop
        cluster = None  # cluster analysis

        for i, c in enumerate(chainIds):
            ent = {}  # entity

            ident = False
            if len(asm) > 0 and largeAssembly:
                _ent = asm[-1]
                if 'identical_chain_id' in _ent and c in _ent['identical_chain_id']:
                    ident = True

            if ident:
                ent = copy.copy(asm[-1])

            ent['chain_id'] = ent['auth_chain_id'] = c
            if auth_chain_id_col != -1:
                ent['auth_chain_id'] = authChainDict[c]

            if not ident:

                etype = next((e['type'] for e in entityPoly if 'pdbx_strand_id' in e and c in e['pdbx_strand_id'].split(',')), None)

                # DAOTHER-9644: support for truncated loop in the model
                # avoid interference of ParserListenerUtils.coordAssemblyChecker()
                if withRmsd and catName == 'pdbx_poly_seq_scheme' and len(authSeqDict) > 0:

                    if len(misPolyLink) > 0:

                        for mis in misPolyLink:

                            if mis['auth_chain_id'] != (authChainDict[c] if auth_chain_id_col != -1 else c):
                                continue

                            auth_seq_id_1 = mis['auth_seq_id_1']
                            auth_seq_id_2 = mis['auth_seq_id_2']

                            if auth_seq_id_1 in authSeqDict[c]\
                               and auth_seq_id_2 in authSeqDict[c]\
                               and auth_seq_id_1 < auth_seq_id_2:

                                for auth_seq_id_ in range(auth_seq_id_1 + 1, auth_seq_id_2):
                                    auth_seq_id_list = list(filter(None, authSeqDict[c]))

                                    if auth_seq_id_ < min(auth_seq_id_list):
                                        pos = 0
                                    elif auth_seq_id_ > max(auth_seq_id_list):
                                        pos = len(auth_seq_id_list)
                                    else:
                                        for idx, _auth_seq_id_ in enumerate(auth_seq_id_list):
                                            if _auth_seq_id_ < auth_seq_id_:
                                                continue
                                            pos = idx
                                            break

                                    authSeqDict[c].insert(pos, auth_seq_id_)
                                    compDict[c].insert(pos, '.')  # DAOTHER-9644: comp_id must be specified at Macromolecules page
                                    if ins_code_col != -1:
                                        insCodeDict[c].insert(pos, '.')

                                # DAOTHER-9644: insert label_seq_id for truncated loop in the coordinates
                                seqDict[c] = labelSeqDict[c] = list(range(1, len(authSeqDict[c]) + 1))

                    # DAOTHER-9644: simulate pdbx_poly_seq_scheme category
                    elif etype is not None:

                        if 'polypeptide' in etype:
                            BEG_ATOM = "C"
                            END_ATOM = "N"
                        else:
                            BEG_ATOM = "O3'"
                            END_ATOM = "P"

                        has_ins_code = False

                        for p in range(len(authSeqDict[c]) - 1):
                            s_p = authSeqDict[c][p]
                            s_q = authSeqDict[c][p + 1]

                            if None in (s_p, s_q):
                                continue

                            if s_p == s_q:
                                has_ins_code = True
                                continue

                            if s_p + 1 != s_q:

                                if has_ins_code:
                                    has_ins_code = False
                                    continue

                                auth_seq_id_1 = s_p
                                auth_seq_id_2 = s_q

                                _beg =\
                                    self.getDictListWithFilter('atom_site',
                                                               CARTN_DATA_ITEMS,
                                                               [{'name': 'label_asym_id', 'type': 'str', 'value': c},
                                                                {'name': 'auth_seq_id', 'type': 'int', 'value': auth_seq_id_1},
                                                                {'name': 'label_atom_id', 'type': 'starts-with-alnum',
                                                                 'value': BEG_ATOM},
                                                                {'name': 'pdbx_PDB_model_num', 'type': 'int', 'value': repModelId},
                                                                {'name': 'label_alt_id', 'type': 'enum', 'enum': (repAltId,)}
                                                                ])

                                _end =\
                                    self.getDictListWithFilter('atom_site',
                                                               CARTN_DATA_ITEMS,
                                                               [{'name': 'label_asym_id', 'type': 'str', 'value': c},
                                                                {'name': 'auth_seq_id', 'type': 'int', 'value': auth_seq_id_2},
                                                                {'name': 'label_atom_id', 'type': 'starts-with-alnum',
                                                                 'value': END_ATOM},
                                                                {'name': 'pdbx_PDB_model_num', 'type': 'int', 'value': repModelId},
                                                                {'name': 'label_alt_id', 'type': 'enum', 'enum': (repAltId,)}
                                                                ])

                                if len(_beg) == 1 and len(_end) == 1\
                                   and numpy.linalg.norm(to_np_array(_beg[0]) - to_np_array(_end[0])) > 5.0:
                                    for auth_seq_id_ in range(auth_seq_id_1 + 1, auth_seq_id_2):
                                        auth_seq_id_list = list(filter(None, authSeqDict[c]))

                                        if auth_seq_id_ < min(auth_seq_id_list):
                                            pos = 0
                                        elif auth_seq_id_ > max(auth_seq_id_list):
                                            pos = len(auth_seq_id_list)
                                        else:
                                            for idx, _auth_seq_id_ in enumerate(auth_seq_id_list):
                                                if _auth_seq_id_ < auth_seq_id_:
                                                    continue
                                                pos = idx
                                                break

                                        authSeqDict[c].insert(pos, auth_seq_id_)
                                        # DAOTHER-9644: comp_id must be specified at Macromolecules page
                                        compDict[c].insert(pos, '.')
                                        if ins_code_col != -1:
                                            insCodeDict[c].insert(pos, '.')

                                    # DAOTHER-9644: insert label_seq_id for truncated loop in the coordinates
                                    seqDict[c] = labelSeqDict[c] = list(range(1, len(authSeqDict[c]) + 1))

                ent['seq_id'] = seqDict[c]
                ent['comp_id'] = compDict[c]
                if c in insCodeDict:
                    if any(True for ic in insCodeDict[c] if ic not in EMPTY_VALUE):
                        ent['ins_code'] = insCodeDict[c]
                    if any(True for s in labelSeqDict[c] if s not in EMPTY_VALUE):
                        if c in labelSeqDict and all(isinstance(s, int) for s in labelSeqDict[c]):
                            ent['auth_seq_id'] = authSeqDict[c] if authScheme else seqDict[c]
                            ent['label_seq_id'] = labelSeqDict[c]
                            ent['seq_id'] = ent['label_seq_id']

                if authScheme:
                    ent['auth_seq_id'] = authSeqDict[c]
                    ent['gap_in_auth_seq'] = False
                    for p in range(len(authSeqDict[c]) - 1):
                        s_p = ent['auth_seq_id'][p]
                        s_q = ent['auth_seq_id'][p + 1]
                        if None in (s_p, s_q):
                            continue
                        if s_p + 1 != s_q:
                            ent['gap_in_auth_seq'] = True
                            break

                if auth_comp_id_col != -1:
                    ent['auth_comp_id'] = []
                    if authScheme:
                        if ins_code_col != -1:
                            for s, ic in zip(authSeqDict[c], insCodeDict[c]):
                                row = next((row for row in rowList if row[chain_id_col] == c
                                            and int(row[auth_seq_id_col]) == s and row[ins_code_col] == ic), None)
                                if row is not None:
                                    comp_id = row[auth_comp_id_col]
                                    if comp_id not in EMPTY_VALUE:
                                        ent['auth_comp_id'].append(comp_id)
                                    else:
                                        ent['auth_comp_id'].append('.')
                                else:
                                    ent['auth_comp_id'].append('.')
                        else:
                            for s in authSeqDict[c]:
                                row = next((row for row in rowList if row[chain_id_col] == c
                                            and int(row[auth_seq_id_col]) == s), None)
                                if row is not None:
                                    comp_id = row[auth_comp_id_col]
                                    if comp_id not in EMPTY_VALUE:
                                        ent['auth_comp_id'].append(comp_id)
                                    else:
                                        ent['auth_comp_id'].append('.')
                                else:
                                    ent['auth_comp_id'].append('.')
                    else:
                        for s in seqDict[c]:
                            row = next((row for row in rowList if row[chain_id_col] == c
                                        and int(row[seq_id_col]) == s), None)
                            if row is not None:
                                comp_id = row[auth_comp_id_col]
                                if comp_id not in EMPTY_VALUE:
                                    ent['auth_comp_id'].append(comp_id)
                                else:
                                    ent['auth_comp_id'].append('.')
                            else:
                                ent['auth_comp_id'].append('.')
                else:
                    ent['auth_comp_id'] = ent['comp_id']

                if alt_comp_id_col != -1:
                    ent['alt_comp_id'] = []
                    if authScheme:
                        if ins_code_col != -1:
                            for s, ic in zip(authSeqDict[c], insCodeDict[c]):
                                row = next((row for row in rowList if row[chain_id_col] == c
                                            and int(row[auth_seq_id_col]) == s and row[ins_code_col] == ic), None)
                                if row is not None:
                                    comp_id = row[alt_comp_id_col]
                                    if comp_id not in EMPTY_VALUE:
                                        ent['alt_comp_id'].append(comp_id)
                                    else:
                                        ent['alt_comp_id'].append('.')
                                else:
                                    ent['alt_comp_id'].append('.')
                        else:
                            for s in authSeqDict[c]:
                                row = next((row for row in rowList if row[chain_id_col] == c
                                            and int(row[auth_seq_id_col]) == s), None)
                                if row is not None:
                                    comp_id = row[alt_comp_id_col]
                                    if comp_id not in EMPTY_VALUE:
                                        ent['alt_comp_id'].append(comp_id)
                                    else:
                                        ent['alt_comp_id'].append('.')
                                else:
                                    ent['alt_comp_id'].append('.')
                    else:
                        for s in seqDict[c]:
                            row = next((row for row in rowList if row[chain_id_col] == c
                                        and int(row[seq_id_col]) == s), None)
                            if row is not None:
                                comp_id = row[alt_comp_id_col]
                                if comp_id not in EMPTY_VALUE:
                                    ent['alt_comp_id'].append(comp_id)
                                else:
                                    ent['alt_comp_id'].append('.')
                            else:
                                ent['alt_comp_id'].append('.')

                if withStructConf and i < LEN_MAJOR_ASYM_ID:  # to process large assembly avoiding forced timeout
                    ent['struct_conf'] = self.__extractStructConf(c, authSeqDict[c] if authScheme else seqDict[c], not authScheme)

                # to process large assembly avoiding forced timeout (2ms7, 21 chains)
                if withRmsd and etype is not None and totalModels > 1 and i < LEN_MAJOR_ASYM_ID / 2:
                    ent['type'] = etype

                    randomM = None
                    if self.__random_rotaion_test:
                        randomM = {}
                        for model_id in effModelIds:
                            axis = [random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)]
                            if self.__single_model_rotation_test:
                                theta = 0.0 if model_id > 1 else numpy.pi / 4.0
                            else:
                                theta = random.uniform(-numpy.pi, numpy.pi)
                            randomM[model_id] = M(axis, theta)

                    if 'polypeptide' in etype:

                        if caRmsd is None:

                            polyPeptideChains = [c]
                            polyPeptideLengths = [polymerLength[c]]

                            for c2 in chainIds:

                                if c2 == c:
                                    continue

                                etype2 = next((e['type'] for e in entityPoly
                                               if 'pdbx_strand_id' in e and c2 in e['pdbx_strand_id'].split(',')), None)

                                if etype2 is not None and 'polypeptide' in etype2:
                                    polyPeptideChains.append(c2)
                                    polyPeptideLengths.append(polymerLength[c2])

                            ca_atom_sites = self.getDictListWithFilter('atom_site',
                                                                       [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                                        {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                                        {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                                        {'name': 'label_asym_id', 'type': 'str',
                                                                         'alt_name': 'chain_id'},
                                                                        {'name': 'auth_seq_id', 'type': 'int',
                                                                         'alt_name': 'seq_id'},
                                                                        {'name': 'ndb_model' if alias else 'pdbx_PDB_model_num',
                                                                         'type': 'int', 'alt_name': 'model_id'},
                                                                        {'name': 'type_symbol', 'type': 'str',
                                                                         'alt_name': 'element'}
                                                                        ],
                                                                       [{'name': 'label_asym_id', 'type': 'enum',
                                                                         'enum': polyPeptideChains},
                                                                        {'name': 'label_atom_id', 'type': 'starts-with-alnum',
                                                                         'value': 'CA'},
                                                                        {'name': 'label_alt_id', 'type': 'enum',
                                                                         'enum': (repAltId,)},
                                                                        {'name': 'type_symbol', 'type': 'str', 'value': 'C'}])

                            bb_atom_sites = self.getDictListWithFilter('atom_site',
                                                                       [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                                        {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                                        {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                                        {'name': 'label_asym_id', 'type': 'str',
                                                                         'alt_name': 'chain_id'},
                                                                        {'name': 'auth_seq_id', 'type': 'int',
                                                                         'alt_name': 'seq_id'},
                                                                        {'name': 'ndb_model' if alias else 'pdbx_PDB_model_num',
                                                                         'type': 'int', 'alt_name': 'model_id'},
                                                                        {'name': 'type_symbol', 'type': 'str',
                                                                         'alt_name': 'element'}
                                                                        ],
                                                                       [{'name': 'label_asym_id', 'type': 'enum',
                                                                         'enum': polyPeptideChains},
                                                                        {'name': 'label_atom_id', 'type': 'enum',
                                                                         'enum': ['C', 'N']},
                                                                        {'name': 'label_alt_id', 'type': 'enum',
                                                                         'enum': (repAltId,)},
                                                                        {'name': 'type_symbol', 'type': 'enum',
                                                                         'enum': ['C', 'N']}])

                            bb_atom_sites.extend(ca_atom_sites)

                            caRmsd, caWellDefinedRegion, cluster =\
                                self.__calculateRmsd(polyPeptideChains, polyPeptideLengths,
                                                     totalModels, effModelIds,
                                                     ca_atom_sites, bb_atom_sites, randomM)

                        if caRmsd is not None:
                            ent['ca_rmsd'] = caRmsd[polyPeptideChains.index(c)]
                        if caWellDefinedRegion is not None:
                            ent['well_defined_region'] = caWellDefinedRegion[polyPeptideChains.index(c)]

                    elif 'ribonucleotide' in etype:

                        if pRmsd is None:

                            polyNucleotideChains = [c]
                            polyNucleotideLengths = [polymerLength[c]]

                            for c2 in chainIds:

                                if c2 == c:
                                    continue

                                etype2 = next((e['type'] for e in entityPoly
                                               if 'pdbx_strand_id' in e and c2 in e['pdbx_strand_id'].split(',')), None)

                                if etype2 is not None and 'ribonucleotide' in etype2:
                                    polyNucleotideChains.append(c2)
                                    polyNucleotideLengths.append(polymerLength[c2])

                            p_atom_sites = self.getDictListWithFilter('atom_site',
                                                                      [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                                       {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                                       {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                                       {'name': 'label_asym_id', 'type': 'str',
                                                                        'alt_name': 'chain_id'},
                                                                       {'name': 'auth_seq_id', 'type': 'int',
                                                                        'alt_name': 'seq_id'},
                                                                       {'name': 'ndb_model' if alias else 'pdbx_PDB_model_num',
                                                                        'type': 'int', 'alt_name': 'model_id'},
                                                                       {'name': 'type_symbol', 'type': 'str',
                                                                        'alt_name': 'element'}
                                                                       ],
                                                                      [{'name': 'label_asym_id', 'type': 'enum',
                                                                        'enum': polyNucleotideChains},
                                                                       {'name': 'label_atom_id', 'type': 'starts-with-alnum',
                                                                        'value': 'P'},
                                                                       {'name': 'label_alt_id', 'type': 'enum',
                                                                        'enum': (repAltId,)},
                                                                       {'name': 'type_symbol', 'type': 'str', 'value': 'P'}])

                            bb_atom_sites = self.getDictListWithFilter('atom_site',
                                                                       [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                                        {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                                        {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                                        {'name': 'label_asym_id', 'type': 'str',
                                                                         'alt_name': 'chain_id'},
                                                                        {'name': 'auth_seq_id', 'type': 'int',
                                                                         'alt_name': 'seq_id'},
                                                                        {'name': 'ndb_model' if alias else 'pdbx_PDB_model_num',
                                                                         'type': 'int', 'alt_name': 'model_id'},
                                                                        {'name': 'type_symbol', 'type': 'str',
                                                                         'alt_name': 'element'}
                                                                        ],
                                                                       [{'name': 'label_asym_id', 'type': 'enum',
                                                                         'enum': polyNucleotideChains},
                                                                        {'name': 'label_atom_id', 'type': 'enum',
                                                                         'enum': ("C5'", "C4'", "C3'")},
                                                                        {'name': 'label_alt_id', 'type': 'enum',
                                                                         'enum': (repAltId,)},
                                                                        {'name': 'type_symbol', 'type': 'str', 'value': 'C'}])

                            bb_atom_sites.extend(p_atom_sites)

                            pRmsd, pWellDefinedRegion, cluster =\
                                self.__calculateRmsd(polyNucleotideChains, polyNucleotideLengths,
                                                     totalModels, effModelIds,
                                                     p_atom_sites, bb_atom_sites, randomM)

                        if pRmsd is not None:
                            ent['p_rmsd'] = pRmsd[polyNucleotideChains.index(c)]
                        if pWellDefinedRegion is not None:
                            ent['well_defined_region'] = pWellDefinedRegion[polyNucleotideChains.index(c)]

            if len(chainIds) > 1:
                identity = []
                for _c in chainIds:
                    if _c == c:
                        continue
                    if compDict[_c] == compDict[c]:
                        identity.append(_c)
                if len(identity) > 0:
                    ent['identical_chain_id'] = identity
                    if auth_chain_id_col != -1:
                        ent['identical_auth_chain_id'] = [authChainDict[c] for c in identity]

                if len(unmapSeqIds) > 0 and c in unmapSeqIds and c in chainIdWoDefault:
                    ent['unmapped_seq_id'] = [int(s) for s, r in unmapSeqIds[c]]
                    ent['unmapped_auth_seq_id'] = [int(s) for s in unmapAuthSeqIds[c]]

            asm.append(ent)

        if withRmsd and 'polypeptide' in etypes and 'ribonucleotide' in etypes and totalModels > 1 and i < LEN_MAJOR_ASYM_ID / 2:
            allChains = polyPeptideChains
            allChains.extend(polyNucleotideChains)

            ca_p_atom_sites = self.getDictListWithFilter('atom_site',
                                                         [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                          {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                          {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                          {'name': 'label_asym_id', 'type': 'str',
                                                           'alt_name': 'chain_id'},
                                                          {'name': 'auth_seq_id', 'type': 'int',
                                                           'alt_name': 'seq_id'},
                                                          {'name': 'ndb_model' if alias else 'pdbx_PDB_model_num',
                                                           'type': 'int', 'alt_name': 'model_id'},
                                                          {'name': 'type_symbol', 'type': 'str',
                                                           'alt_name': 'element'}
                                                          ],
                                                         [{'name': 'label_asym_id', 'type': 'enum',
                                                           'enum': allChains},
                                                          {'name': 'label_atom_id', 'type': 'enum',
                                                           'enum': ['CA', 'P']},
                                                          {'name': 'label_alt_id', 'type': 'enum',
                                                           'enum': (repAltId,)},
                                                          {'name': 'type_symbol', 'type': 'enum',
                                                           'enum': ['C', 'P']}])

            bb_atom_sites = self.getDictListWithFilter('atom_site',
                                                       [{'name': 'Cartn_x', 'type': 'float', 'alt_name': 'x'},
                                                        {'name': 'Cartn_y', 'type': 'float', 'alt_name': 'y'},
                                                        {'name': 'Cartn_z', 'type': 'float', 'alt_name': 'z'},
                                                        {'name': 'label_asym_id', 'type': 'str',
                                                         'alt_name': 'chain_id'},
                                                        {'name': 'auth_seq_id', 'type': 'int',
                                                         'alt_name': 'seq_id'},
                                                        {'name': 'ndb_model' if alias else 'pdbx_PDB_model_num',
                                                         'type': 'int', 'alt_name': 'model_id'},
                                                        {'name': 'type_symbol', 'type': 'str',
                                                         'alt_name': 'element'}
                                                        ],
                                                       [{'name': 'label_asym_id', 'type': 'enum',
                                                         'enum': allChains},
                                                        {'name': 'label_atom_id', 'type': 'enum',
                                                         'enum': ['C', "C5'", "C4'", "C3'", 'N']},
                                                        {'name': 'label_alt_id', 'type': 'enum',
                                                         'enum': (repAltId,)},
                                                        {'name': 'type_symbol', 'type': 'enum',
                                                         'enum': ['C', 'N']}])

            bb_atom_sites.extend(ca_p_atom_sites)

            _, _, cluster = self.__calculateRmsd(allChains, polyPeptideLengths + polyNucleotideLengths,
                                                 totalModels, effModelIds,
                                                 ca_p_atom_sites, bb_atom_sites, randomM)

        return asm, cluster

    def __extractStructConf(self, chain_id: str, seq_ids: List[int], label_scheme: bool = True
                            ) -> List[Optional[str]]:
        """ Extract structure conformational annotations.
        """

        ret = [None] * len(seq_ids)

        helix_id_name = 'pdbx_PDB_helix_id' if self.hasItem('struct_conf', 'pdbx_PDB_helix_id')\
            else 'pdb_id' if self.hasItem('struct_conf', 'pdb_id')\
            else 'id'

        struct_conf = self.getDictListWithFilter('struct_conf',
                                                 [{'name': 'conf_type_id', 'type': 'str'},
                                                  {'name': helix_id_name, 'type': 'str', 'alt_name': 'helix_id'},
                                                  {'name': 'beg_label_seq_id'
                                                   if label_scheme else 'beg_auth_seq_id',
                                                   'type': 'int', 'alt_name': 'beg_seq_id'},
                                                  {'name': 'end_label_seq_id'
                                                   if label_scheme else 'end_auth_seq_id',
                                                   'type': 'int', 'alt_name': 'end_seq_id'}
                                                  ],
                                                 [{'name': 'beg_label_asym_id', 'type': 'str', 'value': chain_id},
                                                  {'name': 'end_label_asym_id', 'type': 'str', 'value': chain_id}
                                                  ])

        for sc in struct_conf:
            for seq_id in range(sc['beg_seq_id'], sc['end_seq_id'] + 1):
                if seq_id in seq_ids and sc['conf_type_id'] is not None and sc['helix_id'] is not None:
                    ret[seq_ids.index(seq_id)] = f"{sc['conf_type_id']}:{sc['helix_id']}"

        struct_sheet_range = self.getDictListWithFilter('struct_sheet_range',
                                                        [{'name': 'sheet_id', 'type': 'str'},
                                                         {'name': 'id', 'type': 'str'},
                                                         {'name': 'beg_label_seq_id'
                                                          if label_scheme else 'beg_auth_seq_id',
                                                          'type': 'int', 'alt_name': 'beg_seq_id'},
                                                         {'name': 'end_label_seq_id'
                                                          if label_scheme else 'end_auth_seq_id',
                                                          'type': 'int', 'alt_name': 'end_seq_id'}
                                                         ],
                                                        [{'name': 'beg_label_asym_id', 'type': 'str', 'value': chain_id},
                                                         {'name': 'end_label_asym_id', 'type': 'str', 'value': chain_id}
                                                         ])

        for ssr in struct_sheet_range:
            for seq_id in range(ssr['beg_seq_id'], ssr['end_seq_id'] + 1):
                if seq_id in seq_ids and ssr['sheet_id'] is not None and ssr['id'] is not None:
                    ret[seq_ids.index(seq_id)] = f"STRN:{ssr['sheet_id']}:{ssr['id']}"

        return ret

    def __calculateRmsd(self, chain_ids: List[str], lengths: List[int], total_models: int = 1,
                        eff_model_ids: Optional[List[str]] = None,
                        atom_sites: Optional[List[dict]] = None, bb_atom_sites: Optional[List[dict]] = None,
                        randomM: Optional[List[list]] = None
                        ) -> Tuple[Optional[List[dict]], Optional[List[dict]], Optional[List[dict]]]:
        """ Calculate RMSD of alpha carbons/phosphates in the ensemble.
        """

        if None in (atom_sites, bb_atom_sites):
            return None, None, None

        # Group atoms by model in a single pass (was O(models * total_atoms)); each
        # eff model keeps a list in the original atom order. 'v' (numpy coords) is
        # attached once per atom.
        eff_model_id_set = set(eff_model_ids)

        _atom_site_dict = {model_id: [] for model_id in eff_model_ids}
        for a in atom_sites:
            model_id = a['model_id']
            if model_id in eff_model_id_set:
                a['v'] = to_np_array(a)
                _atom_site_dict[model_id].append(a)

        _bb_atom_site_dict = {model_id: [] for model_id in eff_model_ids}
        for a in bb_atom_sites:
            model_id = a['model_id']
            if model_id in eff_model_id_set:
                a['v'] = to_np_array(a)
                _bb_atom_site_dict[model_id].append(a)

        size = len(_atom_site_dict[1])

        if size == 0:
            return None, None, None

        matrix_size = (size, size)

        # average and variance of intra-model inter-atom distances, vectorized.
        # Per model, pdist() returns the condensed upper-triangle distance vector in
        # one C call (was two O(models * size^2) Python loops of numpy.linalg.norm).
        # Accumulate sum and sum-of-squares; var = E[d^2] - E[d]^2, identical to the
        # old mean of squared deviations. squareform() rebuilds the symmetric
        # matrices (downstream reads only the i<j upper triangle and numpy.max()).
        # Models whose atom count != size (empty / inconsistent) are skipped, as the
        # per-atom index accumulation required all models to share `size` atoms.
        sum_d = numpy.zeros(size * (size - 1) // 2, dtype=float)
        sum_d2 = numpy.zeros_like(sum_d)

        _total_models = 0

        for model_id in eff_model_ids:

            _atom_site = _atom_site_dict[model_id]

            if len(_atom_site) != size:
                continue

            _total_models += 1

            coord = numpy.array([a['v'] for a in _atom_site], dtype=float)
            dvec = pdist(coord)
            sum_d += dvec
            sum_d2 += dvec * dvec

        if _total_models <= 1:
            return None, None, None

        avr = sum_d / _total_models
        d_var = squareform(sum_d2 / _total_models - avr * avr)  # d_avr (size x size) unused downstream

        max_d_var = min(numpy.max(d_var), RMSD_CUTOFF_FOR_DOMAIN * RMSD_CUTOFF_FOR_DOMAIN)

        d_ord = numpy.ones(matrix_size, dtype=float)

        if max_d_var > 0.0:

            for i, j in itertools.combinations(range(size), 2):

                if i < j:
                    q = max(1.0 - math.sqrt(max(d_var[i, j], 0.0) / max_d_var), 0.0)
                else:
                    q = max(1.0 - math.sqrt(max(d_var[j, i], 0.0) / max_d_var), 0.0)

                d_ord[i, j] = d_ord[j, i] = q

        _, v = numpy.linalg.eig(d_ord)

        md5_set = set()

        abort = False
        long = size > 2 * self.__min_monomers_for_domain

        min_score = 1000000.0
        min_result = None

        stop_min_samples = -1

        cycle = 0

        for min_samples in reversed(range(self.__min_samples_for_clustering, self.__max_samples_for_clustering + 1)):

            if min_samples == stop_min_samples:
                break

            for features in range(self.__min_features_for_clustering, self.__max_features_for_clustering + 1):

                x = numpy.delete(v, numpy.s_[features:], 1)

                if 'complex' in str(x.dtype):
                    x = x.real

                if min_samples >= features:
                    continue

                for _epsilon in range(4, 11):

                    if abort:
                        break

                    cycle += 1

                    epsilon = 2.0 ** (_epsilon / 2.0) / 100.0  # epsilon travels from 0.04 to 0.32

                    if SKLEARN_DBSCAN:

                        db = DBSCAN(eps=epsilon, min_samples=min_samples).fit(x)

                        labels = db.labels_

                        # Explicitly clear from memory
                        del db

                    else:

                        labels, _ = DBSCAN(x, eps=epsilon, min_samples=min_samples)

                    list_labels = list(labels)
                    set_labels = set(labels)

                    # Explicitly clear from memory
                    del labels

                    if cycle % GARBAGE_COLLECTION_CYCLES == 0:
                        gc.collect(0)

                        cycle = 0

                    n_clusters = len(set_labels) - (1 if -1 in set_labels else 0)
                    n_noise = list_labels.count(-1)

                    if n_clusters == 0 or (n_clusters >= features - 2 and long):
                        continue

                    md5 = hashlib.md5(str(list_labels).encode('utf-8'))

                    if md5 in md5_set:
                        continue

                    md5_set.add(md5)

                    result = {'features': features, 'min_samples': min_samples, 'epsilon': epsilon,
                              'clusters': n_clusters, 'noise': n_noise}

                    mosaic = len(set_labels) > 1

                    if mosaic:

                        mosaic = False

                        seq_ids_set_of = {}

                        for label in set_labels:
                            monomers = list_labels.count(label)

                            if monomers == 0 or (monomers < self.__min_monomers_for_domain and long):
                                continue

                            _atom_site_ref = _atom_site_dict[1]
                            _atom_site_p = [_a for _a, _l in zip(_atom_site_ref, list_labels) if _l == label]

                            if label != -1:
                                for chain_id in chain_ids:
                                    seq_ids = sorted(set(a['seq_id'] for a in _atom_site_p if a['chain_id'] == chain_id))
                                    if len(seq_ids) > 0:
                                        gaps = seq_ids[-1] + 1 - seq_ids[0] - len(seq_ids)
                                        if chain_id not in seq_ids_set_of:
                                            seq_ids_set_of[chain_id] = []
                                        seq_ids_set_of[chain_id].append(seq_ids)
                                        if gaps > monomers * 2:  # avoid mosaic-like domain recognition (v1.0.7)
                                            mosaic = True
                                        if gaps == 1:  # fill single gap in a domain (v1.0.8)
                                            prev_seq_id = None
                                            for seq_id in seq_ids:
                                                if prev_seq_id is not None and seq_id - 2 == prev_seq_id:
                                                    break
                                                prev_seq_id = seq_id
                                            if prev_seq_id is not None:
                                                gap_idx = None
                                                for idx, a in enumerate(_atom_site_ref):
                                                    if a['chain_id'] == chain_id and a['seq_id'] == prev_seq_id + 1:
                                                        gap_idx = idx
                                                        break
                                                if gap_idx is not None and list_labels[gap_idx] == -1:
                                                    list_labels[gap_idx] = label
                                                    n_noise -= 1
                                                    result['noise'] = n_noise

                        if mosaic:

                            mosaic = False

                            for seq_ids_set in seq_ids_set_of.values():
                                if len(seq_ids_set) < 2:
                                    continue
                                for seq_ids_pair in itertools.combinations(seq_ids_set, 2):
                                    seq_ids1 = seq_ids_pair[0]
                                    seq_ids2 = seq_ids_pair[1]
                                    if seq_ids2[0] < seq_ids1[0] < seq_ids2[-1]\
                                       or seq_ids2[0] < seq_ids1[-1] < seq_ids2[-1]\
                                       or seq_ids1[0] < seq_ids2[0] < seq_ids1[-1]\
                                       or seq_ids1[0] < seq_ids2[-1] < seq_ids1[-1]:
                                        mosaic = True
                                        break

                            if mosaic:  # 2mze
                                continue

                    score = 0.0

                    for label in set_labels:

                        monomers = list_labels.count(label)

                        if monomers == 0 or (monomers < self.__min_monomers_for_domain and long):
                            continue

                        fraction = float(monomers) / size

                        _rmsd = []

                        _atom_site_ref = _atom_site_dict[1]
                        _atom_site_p = [_a for _a, _l in zip(_atom_site_ref, list_labels) if _l == label]

                        for model_id in range(2, total_models + 1):

                            if model_id not in eff_model_ids:
                                continue

                            _atom_site_test = _atom_site_dict[model_id]

                            if len(_atom_site_test) == 0:
                                continue

                            _atom_site_q = [_a for _a, _l in zip(_atom_site_test, list_labels) if _l == label]

                            if len(_atom_site_p) != len(_atom_site_q):
                                continue

                            _rmsd.append(calculate_rmsd(_atom_site_p, _atom_site_q))

                        if len(_rmsd) == 0:
                            continue

                        mean_rmsd = numpy.mean(numpy.array(_rmsd, dtype=float))

                        score += mean_rmsd * fraction

                    if score == 0.0:
                        continue

                    domains = collections.Counter(list_labels).most_common()

                    if domains[0][0] == -1:
                        continue

                    result['score'] = score

                    if n_clusters > 0 and stop_min_samples == -1:
                        stop_min_samples = min_samples - 2

                    if self.__verbose and self.__debug:
                        self.__log.write(f'{result}\n')

                    if score < min_score or (n_noise == 0 and min_score < RMSD_OVERLAID_EXACTLY):
                        min_score = score
                        min_result = result

                        if n_noise == 0 and min_score < RMSD_OVERLAID_EXACTLY:
                            abort = True

        if min_result is None:
            return None, None, None

        x = numpy.delete(v, numpy.s_[min_result['features']:], 1)

        if 'complex' in str(x.dtype):
            x = x.real

        if SKLEARN_DBSCAN:

            db = DBSCAN(eps=min_result['epsilon'], min_samples=min_result['min_samples']).fit(x)

            labels = db.labels_

            # Explicitly clear from memory
            del db

        else:

            labels, _ = DBSCAN(x, eps=min_result['epsilon'], min_samples=min_result['min_samples'])

        list_labels = list(labels)
        domains = collections.Counter(list_labels).most_common()

        if domains[0][0] == -1:
            return None, None, None

        fill_single_gap = False

        for label in set_labels:
            monomers = list_labels.count(label)

            if monomers == 0 or (monomers < self.__min_monomers_for_domain and long):
                continue

            _atom_site_ref = _atom_site_dict[1]
            _atom_site_p = [_a for _a, _l in zip(_atom_site_ref, list_labels) if _l == label]

            if label != -1:
                for chain_id in chain_ids:
                    seq_ids = sorted(set(a['seq_id'] for a in _atom_site_p if a['chain_id'] == chain_id))
                    if len(seq_ids) > 0:
                        gaps = seq_ids[-1] + 1 - seq_ids[0] - len(seq_ids)
                        if gaps == 1:  # fill single gap in a domain (v1.0.8)
                            prev_seq_id = None
                            for seq_id in seq_ids:
                                if prev_seq_id is not None and seq_id - 2 == prev_seq_id:
                                    break
                                prev_seq_id = seq_id
                            if prev_seq_id is not None:
                                gap_idx = None
                                for idx, a in enumerate(_atom_site_ref):
                                    if a['chain_id'] == chain_id and a['seq_id'] == prev_seq_id + 1:
                                        gap_idx = idx
                                        break
                                if gap_idx is not None and list_labels[gap_idx] == -1:
                                    labels[gap_idx] = label
                                    fill_single_gap = True

        if fill_single_gap:
            list_labels = list(labels)
            domains = collections.Counter(list_labels).most_common()

        eff_labels = [label for label, count in domains if label != -1 and (count >= self.__min_monomers_for_domain
                                                                            or not long)]
        eff_domain_id = {}

        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
        if self.__verbose and self.__debug:
            self.__log.write(f"feature: {min_result['features']}, "
                             f"min_sample: {min_result['min_samples']}, epsilon: {min_result['epsilon']}, "
                             f"clusters: {n_clusters} (effective domains: {len(eff_labels)}), noise: {list_labels.count(-1)}, "
                             f"score: {min_score}\n")

        _chain_ids = [a['chain_id'] for a in _atom_site_dict[1]]
        _seq_ids = [a['seq_id'] for a in _atom_site_dict[1]]

        domain_id = 1
        for label, chain_id, seq_id in zip(labels, _chain_ids, _seq_ids):
            if label not in eff_labels:
                if self.__verbose and self.__debug:
                    self.__log.write(f"chain_id: {chain_id}, seq_id: {seq_id}, domain_id: -1\n")
            else:
                _label = int(label)
                if _label not in eff_domain_id:
                    eff_domain_id[_label] = domain_id
                    domain_id += 1
                if self.__verbose and self.__debug:
                    self.__log.write(f"chain_id: {chain_id}, seq_id: {seq_id}, "
                                     f"domain_id: {eff_domain_id[_label]} label: {_label}\n")

        rlist = []
        for chain_id in chain_ids:
            rlist.append([])

        for ref_model_id in eff_model_ids:

            item = {'model_id': ref_model_id}
            _atom_site_ref = _atom_site_dict[ref_model_id]
            _bb_atom_site_ref = _bb_atom_site_dict[ref_model_id]

            dst_chain_ids = None
            min_label = -1
            min_core_rmsd = mean_align_rmsd = 1000000.0

            for label, count in domains:

                if label not in eff_labels:
                    break

                _label = int(label)

                _atom_site_p = [_a for _a, _l in zip(_atom_site_ref, list_labels) if _l == label]

                _dst_chain_ids = set(_a['chain_id'] for _a in _atom_site_p)
                _seq_keys = frozenset((_a['chain_id'], _a['seq_id']) for _a in _atom_site_p)  # O(1) membership
                _bb_atom_site_p = [_a for _a in _bb_atom_site_ref if (_a['chain_id'], _a['seq_id']) in _seq_keys]

                core_rmsd, align_rmsd, exact_overlaid_model_ids = [], [], []

                for test_model_id in eff_model_ids:

                    if ref_model_id == test_model_id:
                        continue

                    _atom_site_test = _atom_site_dict[test_model_id]
                    _atom_site_q = [_a for _a, _l in zip(_atom_site_test, list_labels) if _l == label]

                    if len(_atom_site_p) != len(_atom_site_q):
                        continue

                    _bb_atom_site_test = _bb_atom_site_dict[test_model_id]
                    _bb_atom_site_q = [_a for _a in _bb_atom_site_test if (_a['chain_id'], _a['seq_id']) in _seq_keys]

                    _core_rmsd = []

                    for idx in range(count):

                        ref_atom = _atom_site_p[idx]
                        test_atom = _atom_site_q[idx]

                        ref_v = ref_atom['v']
                        if self.__random_rotaion_test:
                            ref_v = numpy.dot(randomM[ref_model_id], ref_v)

                        test_v = test_atom['v']
                        if self.__random_rotaion_test:
                            test_v = numpy.dot(randomM[test_model_id], test_v)
                        d = test_v - ref_v
                        _core_rmsd.append(numpy.dot(d, d))

                    if len(_core_rmsd) == 0:
                        continue

                    core_rmsd.append(math.sqrt(numpy.mean(numpy.array(_core_rmsd, dtype=float))))
                    _rmsd = calculate_rmsd(_bb_atom_site_p, _bb_atom_site_q)
                    align_rmsd.append(_rmsd)
                    if _rmsd < RMSD_OVERLAID_EXACTLY and ref_model_id < test_model_id:
                        exact_overlaid_model_ids.append({'ref_model_id': ref_model_id,
                                                         'test_model_id': test_model_id,
                                                         'rmsd_in_well_defined_region': round(_rmsd, 4)})
                if len(core_rmsd) == 0:
                    continue

                mean_core_rmsd = numpy.mean(numpy.array(core_rmsd, dtype=float))

                if mean_core_rmsd < min_core_rmsd:
                    dst_chain_ids = _dst_chain_ids
                    min_label = _label
                    min_core_rmsd = mean_core_rmsd
                    mean_align_rmsd = numpy.mean(numpy.array(align_rmsd, dtype=float))

            if min_label != -1:
                item['domain_id'] = eff_domain_id[min_label]
                item['raw_rmsd_in_well_defined_region'] = round(min_core_rmsd, 4)
                item['rmsd_in_well_defined_region'] = round(mean_align_rmsd, 4)
                if len(exact_overlaid_model_ids) > 0:
                    item['exactly_overlaid_model'] = exact_overlaid_model_ids
                for chain_id in dst_chain_ids:
                    rlist[chain_ids.index(chain_id)].append(item)

        # Explicitly clear from memory
        del labels

        cycle += 1

        # well-defined regions

        eff_size = size - sum(count for label, count in domains if label not in eff_labels)

        rmsd_cutoff_for_clustering = 0.0

        dlist = []
        for chain_id in chain_ids:
            dlist.append([])

        seq_range_p = re.compile(r'^\[(-?\d+)-(-?\d+)\]$')

        for label in sorted(eff_labels):

            item = {}

            r = numpy.full((_total_models, _total_models), RMSD_CUTOFF_FOR_DOMAIN, dtype=float)

            _rmsd = []

            # seq_keys is model-independent for a label; precompute the backbone
            # atom list per model once (was rebuilt for every ref/test model pair).
            _seq_keys = frozenset((_a['chain_id'], _a['seq_id'])
                                  for _a, _l in zip(_atom_site_dict[1], list_labels) if _l == label)
            bb_of = {m: [_a for _a in _bb_atom_site_dict[m]
                         if (_a['chain_id'], _a['seq_id']) in _seq_keys]
                     for m in eff_model_ids}

            fraction = len(_seq_keys) / eff_size

            for ref_model_id in range(1, _total_models):

                if ref_model_id not in eff_model_ids:
                    continue

                _bb_atom_site_p = bb_of[ref_model_id]

                if len(_bb_atom_site_p) == 0:
                    continue

                for test_model_id in range(ref_model_id + 1, _total_models + 1):

                    if ref_model_id >= test_model_id or test_model_id not in eff_model_ids:
                        continue

                    _bb_atom_site_q = bb_of[test_model_id]

                    if len(_bb_atom_site_p) != len(_bb_atom_site_q):
                        continue

                    _rmsd_ = calculate_rmsd(_bb_atom_site_p, _bb_atom_site_q)

                    r[ref_model_id - 1, test_model_id - 1] = _rmsd_
                    r[test_model_id - 1, ref_model_id - 1] = _rmsd_

                    _rmsd.append(_rmsd_)

            if len(_rmsd) > 0:
                item['mean_rmsd'] = round(numpy.mean(numpy.array(_rmsd, dtype=float)), 4)
                rmsd_cutoff_for_clustering += item['mean_rmsd'] * fraction

            _, v = numpy.linalg.eig(r)
            x = numpy.delete(numpy.abs(v), numpy.s_[1:], 1)
            ref_model_id = int(numpy.argmin(x, axis=0)[0]) + 1

            item['medoid_model_id'] = ref_model_id

            _atom_site_ref = _atom_site_dict[ref_model_id]
            _atom_site_p = [_a for _a, _l in zip(_atom_site_ref, list_labels) if _l == label]
            _bb_atom_site_ref = _bb_atom_site_dict[ref_model_id]
            _seq_keys = frozenset((_a['chain_id'], _a['seq_id']) for _a in _atom_site_p)  # O(1) membership
            _bb_atom_site_p = [_a for _a in _bb_atom_site_ref if (_a['chain_id'], _a['seq_id']) in _seq_keys]

            _rmsd = []

            if len(_bb_atom_site_p) > 0:

                for test_model_id in eff_model_ids:

                    if ref_model_id == test_model_id:
                        continue

                    # _atom_site_test = _atom_site_dict[test_model_id]
                    # _atom_site_q = [_a for _a, _l in zip(_atom_site_test, list_labels) if _l == label]

                    _bb_atom_site_test = _bb_atom_site_dict[test_model_id]
                    _bb_atom_site_q = [_a for _a in _bb_atom_site_test if (_a['chain_id'], _a['seq_id']) in _seq_keys]

                    if len(_bb_atom_site_p) != len(_bb_atom_site_q):
                        continue

                    _rmsd.append(calculate_rmsd(_bb_atom_site_p, _bb_atom_site_q))

            if len(_rmsd) > 0:
                item['medoid_rmsd'] = round(numpy.mean(numpy.array(_rmsd, dtype=float)), 4)

            _item = copy.copy(item)

            _label = int(label)

            dst_chain_ids = set(a['chain_id'] for a, l in zip(_atom_site_ref, list_labels)  # noqa: E741
                                if l == label)  # noqa: E741
            seq_keys = sorted(set((a['chain_id'], a['seq_id']) for a, l in zip(_atom_site_ref, list_labels)  # noqa: E741
                                  if l == label),  # noqa: E741
                              key=itemgetter(0, 1))

            for chain_id in dst_chain_ids:
                seq_ids = [s for c, s in seq_keys if c == chain_id]
                count = len(seq_ids)

                _item['domain_id'] = eff_domain_id[_label]
                _item['number_of_monomers'] = count
                _item['seq_id'] = seq_ids
                gaps = seq_ids[-1] + 1 - seq_ids[0] - len(seq_ids)
                _item['number_of_gaps'] = gaps
                if gaps == 0:
                    seq_range = f"[{seq_ids[0]}-{seq_ids[-1]}]"
                else:
                    seq_range = f"[{seq_ids[0]}-"
                    for idx, seq_id in enumerate(seq_ids):
                        if idx > 0 and seq_id != seq_ids[idx - 1] + 1:
                            seq_range += f"{seq_ids[idx - 1]}],[{seq_id}-"
                    seq_range += f"{seq_ids[-1]}]"
                _seq_range = []
                for r in seq_range.split(','):
                    try:
                        g = seq_range_p.search(r).groups()
                        if g[0] != g[1]:
                            _seq_range.append(f"[{g[0]}-{g[1]}]")
                        else:
                            _seq_range.append(f"[{g[0]}]")
                    except AttributeError:
                        pass
                _item['range_of_seq_id'] = ','.join(_seq_range)
                _item['percent_of_core'] = round(float(count) / lengths[chain_ids.index(chain_id)] * 100.0, 1)

                dlist[chain_ids.index(chain_id)].append(copy.deepcopy(_item))

        if self.__verbose and self.__debug:
            self.__log.write(f"{dlist}\n")

        # cluster analysis

        # relax too strict RMSD cutoff for clustering analysis < 1.0 (6osw)
        rmsd_cutoff_for_clustering = max(rmsd_cutoff_for_clustering, 1.0)

        if self.__verbose and self.__debug:
            self.__log.write(f'rmsd cutoff for clustering: {rmsd_cutoff_for_clustering}\n')

        clist = []

        matrix_size = (_total_models, _total_models)

        d_avr = numpy.zeros(matrix_size, dtype=float)

        for label in eff_labels:  # balancing among domains with fraction (2jt8)

            # seq_keys (atoms in the effective domains) is model-independent;
            # precompute the backbone atom list per model once.
            _seq_keys = frozenset((_a['chain_id'], _a['seq_id'])
                                  for _a, _l in zip(_atom_site_dict[1], list_labels) if _l == label)
            bb_of = {m: [_a for _a in _bb_atom_site_dict[m]
                         if (_a['chain_id'], _a['seq_id']) in _seq_keys]
                     for m in eff_model_ids}

            fraction = len(_seq_keys) / eff_size

            for ref_model_id in range(1, total_models):

                if ref_model_id not in eff_model_ids:
                    continue

                ref_idx = eff_model_ids.index(ref_model_id)

                _bb_atom_site_p = bb_of[ref_model_id]

                if len(_bb_atom_site_p) == 0:
                    continue

                for test_model_id in range(ref_model_id + 1, total_models + 1):

                    if ref_model_id >= test_model_id or test_model_id not in eff_model_ids:
                        continue

                    test_idx = eff_model_ids.index(test_model_id)

                    _bb_atom_site_q = bb_of[test_model_id]

                    if len(_bb_atom_site_p) != len(_bb_atom_site_q):
                        continue

                    _rmsd_ = calculate_rmsd(_bb_atom_site_p, _bb_atom_site_q) * fraction

                    d_avr[ref_idx, test_idx] += _rmsd_
                    d_avr[test_idx, ref_idx] = d_avr[ref_idx, test_idx]

        max_d_avr = min(numpy.max(d_var), rmsd_cutoff_for_clustering)

        d_ord = numpy.ones(matrix_size, dtype=float)

        if max_d_avr > 0.0:

            for i, j in itertools.combinations(range(_total_models), 2):

                if i < j:
                    q = max(1.0 - d_avr[i, j] / max_d_avr, 0.0)
                else:
                    q = max(1.0 - d_avr[j, i] / max_d_avr, 0.0)

                d_ord[i, j] = d_ord[j, i] = q

        _, v = numpy.linalg.eig(d_ord)

        md5_set = set()

        min_score = 1000000.0
        min_result = None

        stop_min_samples = -1

        for min_samples in reversed(range(self.__min_samples_for_clustering, self.__max_samples_for_clustering + 1)):

            if min_samples == stop_min_samples:
                break

            for features in range(self.__min_features_for_clustering, self.__max_features_for_clustering + 1):

                x = numpy.delete(v, numpy.s_[features:], 1)

                if 'complex' in str(x.dtype):
                    x = x.real

                if min_samples >= features:
                    continue

                cycle += 1

                for _epsilon in range(2, 15):

                    epsilon = 2.0 ** (_epsilon / 2.0) / 100.0  # epsilon travels from 0.02 to 1.28 (2jt8)

                    if SKLEARN_DBSCAN:

                        db = DBSCAN(eps=epsilon, min_samples=min_samples).fit(x)

                        labels = db.labels_

                        # Explicitly clear from memory
                        del db

                    else:

                        labels, _ = DBSCAN(x, eps=epsilon, min_samples=min_samples)

                    list_labels = list(labels)
                    set_labels = set(labels)

                    # single-model cluster should not have effective cluster number
                    reset_label = False
                    for label in set_labels:
                        if label != -1 and list_labels.count(label) < 2:
                            for idx, _label in enumerate(list_labels):
                                if _label == label:
                                    labels[idx] = -1
                            reset_label = True

                    if reset_label:
                        list_labels = list(labels)
                        set_labels = set(labels)

                    # Explicitly clear from memory
                    del labels

                    if cycle % GARBAGE_COLLECTION_CYCLES == 0:
                        gc.collect(0)

                        cycle = 0

                    n_clusters = len(set_labels) - (1 if -1 in set_labels else 0)
                    n_noise = list_labels.count(-1)

                    if n_clusters == 0:  # or n_clusters >= features - 2:
                        continue

                    md5 = hashlib.md5(str(list_labels).encode('utf-8'))

                    if md5 in md5_set:
                        continue

                    md5_set.add(md5)

                    result = {'features': features, 'min_samples': min_samples, 'epsilon': epsilon,
                              'clusters': n_clusters, 'noise': n_noise}

                    score = 0.0

                    for label in set_labels:

                        fraction = float(list_labels.count(label)) / _total_models

                        if label == -1:
                            score += rmsd_cutoff_for_clustering * fraction
                            continue

                        _rmsd = []

                        label_idx = [idx for idx, _label in enumerate(list_labels) if _label == label]

                        for i, j in itertools.combinations(label_idx, 2):
                            if i >= j:
                                continue
                            _rmsd.append(d_avr[i, j])

                        if len(_rmsd) == 0:
                            score = -1.0
                            break

                        mean_rmsd = numpy.mean(numpy.array(_rmsd, dtype=float))

                        score += mean_rmsd * fraction

                    if score <= 0.0:
                        continue

                    result['score'] = score

                    if n_clusters > 0 and stop_min_samples == -1:
                        stop_min_samples = min_samples - 2

                    if self.__verbose and self.__debug:
                        self.__log.write(f'{result}\n')

                    if score < min_score or (n_noise == 0 and min_score < RMSD_OVERLAID_EXACTLY):
                        min_score = score
                        min_result = result

        if min_result is not None:
            x = numpy.delete(v, numpy.s_[min_result['features']:], 1)

            if 'complex' in str(x.dtype):
                x = x.real

            if SKLEARN_DBSCAN:

                db = DBSCAN(eps=min_result['epsilon'], min_samples=min_result['min_samples']).fit(x)

                labels = db.labels_

                # Explicitly clear from memory
                del db

            else:

                labels, _ = DBSCAN(x, eps=min_result['epsilon'], min_samples=min_result['min_samples'])

            list_labels = list(labels)
            set_labels = set(labels)

            # single-model cluster should not have effective cluster number
            reset_label = False
            for label in set_labels:
                if label != -1 and list_labels.count(label) < 2:
                    for idx, _label in enumerate(list_labels):
                        if _label == label:
                            labels[idx] = -1
                    reset_label = True

            if reset_label:
                list_labels = list(labels)
                set_labels = set(labels)

            # Explicitly clear from memory
            del labels

            cycle += 1

            n_clusters = len(set_labels) - (1 if -1 in set_labels else 0)

            if self.__verbose and self.__debug:
                self.__log.write(f"feature: {min_result['features']}, "
                                 f"min_sample: {min_result['min_samples']}, epsilon: {min_result['epsilon']}, "
                                 f"clusters: {n_clusters}, noise: {list_labels.count(-1)}, score: {min_score}\n")

            most_comon = collections.Counter(list_labels).most_common()

            clust_id = 1

            for label, count in most_comon:

                if label == -1:
                    continue

                pc = []
                for idx, _label in enumerate(list_labels):
                    if _label != label:
                        continue
                    item = {'model_id': eff_model_ids[idx],
                            'pc1': round((numpy.dot(v[0], d_ord[idx])).real, 4),
                            'pc2': round((numpy.dot(v[1], d_ord[idx])).real, 4)
                            }
                    pc.append(item)

                item = {'cluster_id': clust_id,
                        'total_models': count,
                        'model_ids': [eff_model_ids[idx] for idx, _label in enumerate(list_labels)
                                      if _label == label],
                        'principal_components': pc}

                label_idx = [idx for idx, _label in enumerate(list_labels) if _label == label]

                min_rmsd = 1000000.0
                min_idx = -1

                for i in label_idx:
                    _rmsd = []
                    for j in label_idx:
                        if i == j:
                            continue
                        _rmsd.append(d_avr[i, j])

                    avr_rmsd = numpy.mean(numpy.array(_rmsd, dtype=float))
                    if avr_rmsd < min_rmsd:
                        min_idx = i
                        min_rmsd = avr_rmsd

                if min_idx != -1:
                    item['centroid_model_id'] = eff_model_ids[min_idx]
                    item['centroid_rmsd'] = round(min_rmsd, 4)

                    _rmsd = []
                    for i, j in itertools.combinations(label_idx, 2):
                        if i >= j:
                            continue
                        _rmsd.append(d_avr[i, j])

                    item['mean_rmsd'] = round(numpy.mean(numpy.array(_rmsd, dtype=float)), 4)

                clist.append(item)

                clust_id += 1

            for label, _ in most_comon:

                if label != -1:
                    continue

                pc = []
                for idx, _label in enumerate(list_labels):
                    if _label != label:
                        continue
                    item = {'model_id': eff_model_ids[idx],
                            'pc1': round((numpy.dot(v[0], d_ord[idx])).real, 4),
                            'pc2': round((numpy.dot(v[1], d_ord[idx])).real, 4)
                            }
                    pc.append(item)

                item = {'cluster_id': -1,
                        'total_models': 1,
                        'model_ids': [eff_model_ids[idx] for idx, _label in enumerate(list_labels)
                                      if _label == label],
                        'principal_components': pc}

                clist.append(item)

            if self.__verbose and self.__debug:
                self.__log.write(f'{clist}')

        if cycle > 0:
            gc.collect(0)

        return rlist, dlist, clist
