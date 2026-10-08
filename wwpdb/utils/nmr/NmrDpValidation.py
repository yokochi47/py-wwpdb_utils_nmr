##
# File: NmrDpValidation.py
# Date: 07-Jan-2026
#
# Updates:
##
""" Wrapper class for NMR data validation.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.2"

try:
    from wwpdb.utils.nmr.NmrDpValidationInput import NmrDpValidationInput
    from wwpdb.utils.nmr.NmrDpValidationCoord import NmrDpValidationCoord
    from wwpdb.utils.nmr.NmrDpValidationLoop import NmrDpValidationLoop
    from wwpdb.utils.nmr.NmrDpValidationNomencl import NmrDpValidationNomencl
    from wwpdb.utils.nmr.NmrDpValidationCs import NmrDpValidationCs
    from wwpdb.utils.nmr.NmrDpValidationMr import NmrDpValidationMr
    from wwpdb.utils.nmr.NmrDpValidationPk import NmrDpValidationPk
    from wwpdb.utils.nmr.NmrDpValidationCoordChk import NmrDpValidationCoordChk
    from wwpdb.utils.nmr.NmrDpValidationCsStats import NmrDpValidationCsStats
    from wwpdb.utils.nmr.NmrDpValidationMrStats import NmrDpValidationMrStats
    from wwpdb.utils.nmr.NmrDpValidationOutStats import NmrDpValidationOutStats
    from wwpdb.utils.nmr.NmrDpValidationBase import (is_non_metal_element,  # noqa: F401 pylint: disable=unused-import
                                                     is_like_planality_boundary,
                                                     get_atom_name_mapping)
    from wwpdb.utils.nmr.NmrVrptUtility import predict_redox_state_of_cysteine  # noqa: F401 pylint: disable=unused-import
except ImportError:
    from nmr.NmrDpValidationInput import NmrDpValidationInput
    from nmr.NmrDpValidationCoord import NmrDpValidationCoord
    from nmr.NmrDpValidationLoop import NmrDpValidationLoop
    from nmr.NmrDpValidationNomencl import NmrDpValidationNomencl
    from nmr.NmrDpValidationCs import NmrDpValidationCs
    from nmr.NmrDpValidationMr import NmrDpValidationMr
    from nmr.NmrDpValidationPk import NmrDpValidationPk
    from nmr.NmrDpValidationCoordChk import NmrDpValidationCoordChk
    from nmr.NmrDpValidationCsStats import NmrDpValidationCsStats
    from nmr.NmrDpValidationMrStats import NmrDpValidationMrStats
    from nmr.NmrDpValidationOutStats import NmrDpValidationOutStats
    from nmr.NmrDpValidationBase import (is_non_metal_element,  # noqa: F401 pylint: disable=unused-import
                                         is_like_planality_boundary,
                                         get_atom_name_mapping)
    from nmr.NmrVrptUtility import predict_redox_state_of_cysteine  # noqa: F401 pylint: disable=unused-import


class NmrDpValidation(NmrDpValidationInput,  # pylint: disable=too-many-ancestors
                      NmrDpValidationCoord,
                      NmrDpValidationLoop,
                      NmrDpValidationNomencl,
                      NmrDpValidationCs,
                      NmrDpValidationMr,
                      NmrDpValidationPk,
                      NmrDpValidationCoordChk,
                      NmrDpValidationCsStats,
                      NmrDpValidationMrStats,
                      NmrDpValidationOutStats):
    """ Wrapper class for NMR data validation.
    """
    __slots__ = ()
