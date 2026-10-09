##
# File: NmrDpRemediation.py
# Date: 07-Jan-2026
#
# Updates:
##
""" Wrapper class for NMR data remediation.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.3"

try:
    from wwpdb.utils.nmr.NmrDpRemediationEnum import NmrDpRemediationEnum
    from wwpdb.utils.nmr.NmrDpRemediationPolySeq import NmrDpRemediationPolySeq
    from wwpdb.utils.nmr.NmrDpRemediationCsLoop import NmrDpRemediationCsLoop
    from wwpdb.utils.nmr.NmrDpRemediationCs import NmrDpRemediationCs
    from wwpdb.utils.nmr.NmrDpRemediationMr import NmrDpRemediationMr
    from wwpdb.utils.nmr.NmrDpRemediationPk import NmrDpRemediationPk
    from wwpdb.utils.nmr.NmrDpRemediationLegacyCs import NmrDpRemediationLegacyCs
    from wwpdb.utils.nmr.NmrDpRemediationLegacyMr import NmrDpRemediationLegacyMr
    from wwpdb.utils.nmr.NmrDpRemediationLegacyPk import NmrDpRemediationLegacyPk
    from wwpdb.utils.nmr.NmrDpRemediationStats import NmrDpRemediationStats
    from wwpdb.utils.nmr.NmrDpRemediationMerge import NmrDpRemediationMerge
    from wwpdb.utils.nmr.NmrDpRemediationBase import (get_chem_shift_format,  # noqa: F401 pylint: disable=unused-import
                                                      get_chem_shift_format_from_string)
except ImportError:
    from nmr.NmrDpRemediationEnum import NmrDpRemediationEnum
    from nmr.NmrDpRemediationPolySeq import NmrDpRemediationPolySeq
    from nmr.NmrDpRemediationCsLoop import NmrDpRemediationCsLoop
    from nmr.NmrDpRemediationCs import NmrDpRemediationCs
    from nmr.NmrDpRemediationMr import NmrDpRemediationMr
    from nmr.NmrDpRemediationPk import NmrDpRemediationPk
    from nmr.NmrDpRemediationLegacyCs import NmrDpRemediationLegacyCs
    from nmr.NmrDpRemediationLegacyMr import NmrDpRemediationLegacyMr
    from nmr.NmrDpRemediationLegacyPk import NmrDpRemediationLegacyPk
    from nmr.NmrDpRemediationStats import NmrDpRemediationStats
    from nmr.NmrDpRemediationMerge import NmrDpRemediationMerge
    from nmr.NmrDpRemediationBase import (get_chem_shift_format,  # noqa: F401 pylint: disable=unused-import
                                          get_chem_shift_format_from_string)


class NmrDpRemediation(NmrDpRemediationEnum,  # pylint: disable=too-many-ancestors
                       NmrDpRemediationPolySeq,
                       NmrDpRemediationCsLoop,
                       NmrDpRemediationCs,
                       NmrDpRemediationMr,
                       NmrDpRemediationPk,
                       NmrDpRemediationLegacyCs,
                       NmrDpRemediationLegacyMr,
                       NmrDpRemediationLegacyPk,
                       NmrDpRemediationStats,
                       NmrDpRemediationMerge):
    """ Wrapper class for NMR data remediation.
    """
    __slots__ = ()
