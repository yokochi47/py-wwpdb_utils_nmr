##
# File: NmrDpValidationOutStats.py
# Date: 17-Aug-2026
#
# Updates:
##
""" Output statistics of the processed NMR data.
    @author: Masashi Yokochi
"""
__docformat__ = "restructuredtext en"
__author__ = "Masashi Yokochi"
__email__ = "yokochi@protein.osaka-u.ac.jp"
__license__ = "Apache License 2.0"
__version__ = "5.4.0"

import copy
import os
import re
from datetime import datetime

import numpy

try:
    from wwpdb.utils.nmr.NmrDpConstant import (PYNMRSTAR_OBJ_KEY,
                                               NEXT_STAR_FILE_PATH_KEY,
                                               NMR_CIF_FILE_PATH_KEY,
                                               REPORT_FILE_PATH_KEY,
                                               SF_CATEGORIES,
                                               LP_CATEGORIES,
                                               INDEX_TAGS,
                                               CONSIST_ID_TAGS,
                                               NUM_DIM_ITEMS,
                                               EMPTY_VALUE,
                                               TRUE_VALUE,
                                               MAX_DIM_NUM_OF_SPECTRA,
                                               INCONSISTENT_RESTRAINT_WARNING_WO_SF_PAT,
                                               text_md5)
    from wwpdb.utils.nmr.NmrDpReport import NmrDpReportOutputStatistics
    from wwpdb.utils.nmr.CifToNmrStar import (has_key_value,
                                              get_first_sf_tag)
    from wwpdb.utils.nmr.NmrVrptUtility import NmrVrptUtility
    from wwpdb.utils.nmr.NmrDpValidationBase import NmrDpValidationBase
except ImportError:
    from nmr.NmrDpConstant import (PYNMRSTAR_OBJ_KEY,
                                   NEXT_STAR_FILE_PATH_KEY,
                                   NMR_CIF_FILE_PATH_KEY,
                                   REPORT_FILE_PATH_KEY,
                                   SF_CATEGORIES,
                                   LP_CATEGORIES,
                                   INDEX_TAGS,
                                   CONSIST_ID_TAGS,
                                   NUM_DIM_ITEMS,
                                   EMPTY_VALUE,
                                   TRUE_VALUE,
                                   MAX_DIM_NUM_OF_SPECTRA,
                                   INCONSISTENT_RESTRAINT_WARNING_WO_SF_PAT,
                                   text_md5)
    from nmr.NmrDpReport import NmrDpReportOutputStatistics
    from nmr.CifToNmrStar import (has_key_value,
                                  get_first_sf_tag)
    from nmr.NmrVrptUtility import NmrVrptUtility
    from nmr.NmrDpValidationBase import NmrDpValidationBase


class NmrDpValidationOutStats(NmrDpValidationBase):
    """ Output statistics of the processed NMR data.
    """
    __slots__ = ()

    def calculateOutputStats(self) -> bool:
        """ Calculate statistics and validation metrics of output NMR data file.
        """

        if len(self._reg.star_data) == 0 or self._reg.star_data[0] is None or self._reg.star_data_type[0] != 'Entry':
            return False

        __errors = self._reg.report.getTotalErrors()

        __srcPath = self._reg.dstPath if self._reg.dstPath is not None else self._reg.srcPath

        master_entry = self._reg.star_data[0]

        file_type = 'nef' if master_entry.frame_list[0].category.startswith('nef') else 'nmr-star'

        self._reg.output_statistics = NmrDpReportOutputStatistics(self._reg.verbose, self._reg.log)

        self._reg.output_statistics.setItemValue('file_name', os.path.basename(__srcPath))
        self._reg.output_statistics.setItemValue('file_type', file_type)
        self._reg.output_statistics.setItemValue('entry_id', self._reg.entry_id)
        self._reg.output_statistics.setItemValue('processed_date', datetime.today().strftime('%Y-%m-%d'))
        service_host = os.uname()[1]
        if has_key_value(self._reg.inputParamDict, 'service_host'):
            _service_host = self._reg.inputParamDict['service_host']
            if isinstance(_service_host, str) and _service_host not in EMPTY_VALUE:
                service_host = _service_host
        self._reg.output_statistics.setItemValue('processed_site', service_host)
        self._reg.output_statistics.setItemValue('file_size', os.path.getsize(__srcPath))
        self._reg.output_statistics.setItemValue('md5_checksum', text_md5(__srcPath))

        entry_title = entry_authors = submission_date = None

        if file_type == 'nmr-star':

            sf_category = 'entry_information'

            try:

                sf = master_entry.get_saveframes_by_category(sf_category)[0]

                entry_title = get_first_sf_tag(sf, 'Title', None)
                if entry_title is not None:
                    self._reg.output_statistics.setItemValue('entry_title', entry_title)

                submission_date = get_first_sf_tag(sf, 'Submission_date', None)
                if submission_date is not None:
                    self._reg.output_statistics.setItemValue('submission_date', submission_date)

                lp_category = '_Entry_author'

                try:

                    lp = sf.get_loop(lp_category)

                    tags = ['Given_name', 'Family_name']

                    author_list = []

                    if set(tags) & set(lp.tags) == set(tags):

                        for row in lp:

                            if row[1] in EMPTY_VALUE:
                                continue

                            author_name = row[1].title()
                            if row[0] not in EMPTY_VALUE:
                                author_name += f', {row[0].upper()}.'

                            if author_name not in author_list:
                                author_list.append(author_name)

                        if len(author_list) > 0:
                            entry_authors = ', '.join(author_list)
                            self._reg.output_statistics.setItemValue('entry_authors', entry_authors)

                except KeyError:
                    pass

            except IndexError:
                pass

            # assembly

            sf_category = 'assembly'

            try:

                sf = master_entry.get_saveframes_by_category(sf_category)[0]

                try:
                    ea_lp = sf.get_loop('_Entity_assembly')
                except KeyError:
                    ea_lp = None

                assembly_info = {'name': get_first_sf_tag(sf, 'Name', None)}

                number_of_components = get_first_sf_tag(sf, 'Number_of_components', None)
                if isinstance(number_of_components, int):
                    pass
                elif isinstance(number_of_components, str) and number_of_components.isdigit():
                    number_of_components = int(number_of_components)
                elif ea_lp is not None:
                    number_of_components = len(ea_lp)
                assembly_info['number_of_components'] = number_of_components

                organic_ligands = get_first_sf_tag(sf, 'Organic_ligands', None)
                if isinstance(organic_ligands, int):
                    assembly_info['organic_ligands'] = organic_ligands
                elif isinstance(organic_ligands, str) and organic_ligands.isdigit():
                    organic_ligands = int(organic_ligands)
                    assembly_info['organic_ligands'] = organic_ligands

                metal_ions = get_first_sf_tag(sf, 'Metal_ions', None)
                if isinstance(metal_ions, int):
                    assembly_info['metal_ions'] = metal_ions
                elif isinstance(metal_ions, str) and metal_ions.isdigit():
                    metal_ions = int(metal_ions)
                    assembly_info['metal_ions'] = metal_ions

                non_standard_bonds = get_first_sf_tag(sf, 'Non_standard_bonds', None)
                if non_standard_bonds is not None:
                    assembly_info['non_standard_bonds'] = non_standard_bonds in TRUE_VALUE
                else:
                    try:
                        sf.get_loop('_Bond')
                        assembly_info['non_standard_bonds'] = True
                    except KeyError:
                        assembly_info['non_standard_bonds'] = False

                paramagnetic = get_first_sf_tag(sf, 'Paramagnetic', None)
                if paramagnetic is not None:
                    assembly_info['paramagnetic'] = paramagnetic in TRUE_VALUE

                thiol_state = get_first_sf_tag(sf, 'Thiol_state', None)
                if thiol_state is not None:
                    assembly_info['thiol_state'] = thiol_state
                else:
                    assembly_info['thiol_state'] = 'unknown'

                molecular_mass = get_first_sf_tag(sf, 'Molecular_mass', None)
                if molecular_mass is not None:
                    if isinstance(molecular_mass, float):
                        assembly_info['molecular_mass'] = molecular_mass
                    elif isinstance(molecular_mass, str):
                        try:
                            molecular_mass = float(molecular_mass)
                            assembly_info['molecular_mass'] = molecular_mass
                        except ValueError:
                            pass

                assembly_info['entity_assembly'] = []

                if ea_lp is not None:
                    dat = ea_lp.get_tag(['ID', 'Entity_assembly_name', 'Entity_ID', 'Entity_label', 'Asym_ID', 'PDB_chain_ID',
                                         'Experimental_data_reported', 'Physical_state', 'Role'])

                    for idx, row in enumerate(dat):
                        item = {}
                        if isinstance(row[0], int):
                            entity_assembly_id = row[0]
                        elif isinstance(row[0], str) and row[0].isdigit():
                            entity_assembly_id = int(row[0])
                        else:
                            entity_assembly_id = idx + 1
                        item['entity_assembly_id'] = entity_assembly_id

                        if row[1] not in EMPTY_VALUE:
                            item['entity_assembly_name'] = row[1]

                        if isinstance(row[2], int):
                            item['entity_id'] = row[2]
                        elif isinstance(row[2], str) and row[2].isdigit():
                            item['entity_id'] = int(row[2])

                        if row[3] not in EMPTY_VALUE:
                            item['entity_label'] = row[3][1:] if row[3][0] == '$' else row[3]

                        if row[4] not in EMPTY_VALUE:
                            item['chain_id'] = row[4]

                        if row[5] not in EMPTY_VALUE:
                            item['auth_chain_id'] = row[5]

                        if row[6] not in EMPTY_VALUE:
                            item['experimental_data_reported'] = row[6] in TRUE_VALUE

                        if row[7] not in EMPTY_VALUE:
                            item['physical_state'] = row[7]

                        if row[8] not in EMPTY_VALUE:
                            item['role'] = row[8]

                        assembly_info['entity_assembly'].append(item)

                self._reg.output_statistics.setItemValue('assembly', assembly_info)

            except (IndexError, KeyError):
                pass

            # entity

            sf_category = 'entity'

            try:

                entity_info = []

                for idx, sf in enumerate(master_entry.get_saveframes_by_category(sf_category)):
                    item = {}

                    entity_id = get_first_sf_tag(sf, 'ID', None)
                    if isinstance(entity_id, int):
                        pass
                    elif isinstance(entity_id, str) and entity_id.isdigit():
                        entity_id = int(entity_id)
                    else:
                        entity_id = idx + 1
                    item['entity_id'] = entity_id

                    item['label'] = sf.name

                    name = get_first_sf_tag(sf, 'Name', None)
                    if name not in EMPTY_VALUE:
                        item['name'] = name

                    _type = get_first_sf_tag(sf, 'Type', None)
                    if _type not in EMPTY_VALUE:
                        item['type'] = _type

                    polymer_common_type = get_first_sf_tag(sf, 'Polymer_common_type', None)
                    if polymer_common_type not in EMPTY_VALUE:
                        item['polymer_common_type'] = polymer_common_type

                    polymer_type = get_first_sf_tag(sf, 'Polymer_type', None)
                    if polymer_type not in EMPTY_VALUE:
                        item['polymer_type'] = polymer_type

                    auth_chain_id = get_first_sf_tag(sf, 'Polymer_strand_ID', None)
                    if auth_chain_id not in EMPTY_VALUE:
                        item['auth_chain_id'] = auth_chain_id.split(',')

                    polymer_seq_one_letter_code = get_first_sf_tag(sf, 'Polymer_seq_one_letter_code', None)
                    if polymer_seq_one_letter_code not in EMPTY_VALUE:
                        item['polymer_seq_one_letter_code'] = re.sub(r"\s+", "", polymer_seq_one_letter_code)

                    nstd_monomer = get_first_sf_tag(sf, 'Nstd_monomer', None)
                    if nstd_monomer is not None:
                        item['nstd_monomer'] = nstd_monomer in TRUE_VALUE

                    nstd_linkage = get_first_sf_tag(sf, 'Nstd_linkage', None)
                    if nstd_linkage is not None:
                        item['nstd_linkage'] = nstd_linkage in TRUE_VALUE

                    number_of_monomers = get_first_sf_tag(sf, 'Number_of_monomers', None)
                    if isinstance(number_of_monomers, int):
                        item['number_of_monomers'] = number_of_monomers
                    elif isinstance(number_of_monomers, str) and number_of_monomers.isdigit():
                        item['number_of_monomers'] = int(number_of_monomers)

                    number_of_nonpolymer_components = get_first_sf_tag(sf, 'Number_of_nonpolymer_components', None)
                    if isinstance(number_of_nonpolymer_components, int):
                        item['number_of_nonpolymer_components'] = number_of_nonpolymer_components
                    elif isinstance(number_of_nonpolymer_components, str) and number_of_nonpolymer_components.isdigit():
                        item['number_of_nonpolymer_components'] = int(number_of_nonpolymer_components)

                    paramagnetic = get_first_sf_tag(sf, 'Paramagnetic', None)
                    if paramagnetic is not None:
                        item['paramagnetic'] = paramagnetic in TRUE_VALUE

                    thiol_state = get_first_sf_tag(sf, 'Thiol_state', None)
                    if thiol_state not in EMPTY_VALUE:
                        item['thiol_state'] = thiol_state

                    fragment = get_first_sf_tag(sf, 'Fragment', None)
                    if fragment not in EMPTY_VALUE:
                        item['fragment'] = fragment

                    mutation = get_first_sf_tag(sf, 'Mutation', None)
                    if mutation not in EMPTY_VALUE:
                        item['mutation'] = mutation

                    formula_weight = get_first_sf_tag(sf, 'Fromula_weight', None)
                    if isinstance(formula_weight, float):
                        item['formula_weight'] = formula_weight
                    elif isinstance(formula_weight, str):
                        try:
                            formula_weight = float(formula_weight)
                            item['formula_weight'] = formula_weight
                        except ValueError:
                            pass

                    entity_info.append(item)

                self._reg.output_statistics.setItemValue('entity', entity_info)

            except KeyError:
                pass

            cif_poly_seq = None

            src_id = self._reg.report.getInputSourceIdOfCoord()

            if src_id >= 0:
                cif_input_source = self._reg.report.input_sources[src_id]

                cif_input_source_dic = cif_input_source.get()

                if has_key_value(cif_input_source_dic, 'polymer_sequence'):
                    cif_poly_seq = cif_input_source_dic['polymer_sequence']

            if cif_poly_seq is None and self._reg.report_prev is not None:

                src_id = self._reg.report_prev.getInputSourceIdOfCoord()

                if src_id >= 0:
                    cif_input_source = self._reg.report_prev.input_sources[src_id]

                    cif_input_source_dic = cif_input_source.get()

                    if has_key_value(cif_input_source_dic, 'polymer_sequence'):
                        cif_poly_seq = cif_input_source_dic['polymer_sequence']

            has_cysteine = cif_poly_seq is not None\
                and any(ps for ps in cif_poly_seq if 'CYS' in ps['comp_id'] or 'DCY' in ps['comp_id'])

            # model

            if self._reg.cifChecked:
                model_info = {'file_name': os.path.basename(self._reg.cifPath),
                              'file_type': 'pdbx',
                              'file_size': os.path.getsize(self._reg.cifPath),
                              'md5_checksum': self._reg.cR.getHashCode()
                              }

                struct = self._reg.cR.getDictList('struct')
                if len(struct) > 0 and 'title' in struct[0]:
                    struct_title = struct[0]['title']
                    if struct_title not in EMPTY_VALUE:
                        model_info['struct_title'] = struct_title
                        if entry_title is None:
                            self._reg.output_statistics.setItemValue('entry_title', struct_title)

                audit = self._reg.cR.getDictList('audit')
                if len(audit) > 0 and 'name' in audit[0]:
                    author_list = []
                    for row in audit:
                        if row['name'] not in EMPTY_VALUE:
                            if row['name'] not in author_list:
                                author_list.append(row['name'])
                    if len(author_list) > 0:
                        audit_authors = ', '.join(author_list)
                        model_info['audit_authors'] = audit_authors
                        if entry_authors is None:
                            self._reg.output_statistics.setItemValue('entry_authors', audit_authors)

                self._reg.output_statistics.setItemValue('model', model_info)

            # software

            software_info = [{'name': 'wwpdb.utils.nmr.NmrDpUtility',
                              'version': __version__,
                              'classification': 'workflow that performs file conversion, integrity checks, and data validation'}]

            # chem_shift_summary

            vrpt_util = NmrVrptUtility(self._reg.verbose, self._reg.log,
                                       self._reg.cR, self._reg.caC, self._reg.ccU, self._reg.csStat)

            vrpt_util.dirPath = self._reg.dirPath
            vrpt_util.cacheDirPath = self._reg.cacheDirPath

            software_info.append({'name': 'wwpdb.utils.nmr.NmrVrptUtility',
                                  'version': vrpt_util.version,
                                  'classification': 'workflow that performs chemical shift and restraint validations'})

            if self._reg.cifChecked:
                software_info.append({'name': 'wwpdb.utils.io.CifReader',
                                      'version': self._reg.cR.version,
                                      'classification': 'PDBx/mmCIF parser, domain recognition, '
                                                        'and clustering analysis of the ensemble structure'})

            vrpt_util.addInput(name=PYNMRSTAR_OBJ_KEY, value=self._reg.star_data[0], type='param')

            if self._reg.dstPath is not None:
                vrpt_util.addOutput(name=NEXT_STAR_FILE_PATH_KEY,
                                    value=self._reg.dstPath, type='file')

            if NMR_CIF_FILE_PATH_KEY in self._reg.outputParamDict:
                vrpt_util.addOutput(name=NMR_CIF_FILE_PATH_KEY,
                                    value=self._reg.outputParamDict[NMR_CIF_FILE_PATH_KEY], type='file')

            if REPORT_FILE_PATH_KEY in self._reg.inputParamDict:
                fPath = self._reg.inputParamDict[REPORT_FILE_PATH_KEY]
                if os.path.exists(fPath):
                    vrpt_util.addInput(name=REPORT_FILE_PATH_KEY, value=fPath, type='file')

            vrpt_cs = vrpt_util.op('nmr-cs-validation')

            if vrpt_cs is not None and 'completeness' not in vrpt_cs:
                vrpt_cs = None

            vrpt_mr = vrpt_util.op('nmr-mr-validation')

            # Free memory used for NmrVrptUtility
            vrpt_util.release()

            if vrpt_cs is not None:
                completeness = vrpt_cs['completeness']

                cs_summary = {}
                if self._reg.cifChecked and completeness['well_defined'][1] > 0:
                    cs_summary['number_of_target_shifts_in_well_defined_region'] =\
                        completeness['well_defined'][1]
                    cs_summary['number_of_assigned_shifts_in_well_defined_region'] =\
                        completeness['well_defined'][0]
                    cs_summary['number_of_favorable_assigned_shifts_in_well_defined_region'] =\
                        completeness['favor_well_defined'][0]
                    cs_summary['completeness_in_well_defined_region'] =\
                        round(float(completeness['well_defined'][0]) / completeness['well_defined'][1], 3)
                    cs_summary['completeness_in_well_defined_region_with_favorable_shift'] =\
                        round(float(completeness['favor_well_defined'][0]) / completeness['well_defined'][1], 3)

                cs_summary['number_of_target_shifts_in_full_length_region'] =\
                    completeness['full_length'][1]
                cs_summary['number_of_assigned_shifts_in_full_length_region'] =\
                    completeness['full_length'][0]
                cs_summary['number_of_favorable_assigned_shifts_in_full_length_region'] =\
                    completeness['favor_full_length'][0]
                cs_summary['completeness_in_full_length_region'] =\
                    round(float(completeness['full_length'][0]) / completeness['full_length'][1], 3)
                cs_summary['completeness_in_full_length_region_with_favorable_shift'] =\
                    round(float(completeness['favor_full_length'][0]) / completeness['full_length'][1], 3)

                self._reg.output_statistics.setItemValue('chem_shift_summary', cs_summary)

                if 'rci_version' in vrpt_cs\
                   and not any(True for s in software_info if s['name'] == 'wwpdb.utils.nmr.rci.RCI'):
                    software_info.append({'name': 'wwpdb.utils.nmr.rci.RCI',
                                          'version': vrpt_cs['rci_version'],
                                          'classification': 'random coil index (RCI) calculation'})

            self._reg.output_statistics.setItemValue('software', software_info)

            def map_completeness_of(src):
                ret = {}

                for k, v in src['Total'].items():
                    if v[1] == 0:
                        continue
                    if k == 'overall':
                        ret['completeness_of_overall_assignments'] =\
                            [{'atom_group': 'overall_all_chemical_shifts',
                              'number_of_assigned_shifts': v[0],
                              'number_of_target_shifts': v[1],
                              'completeness': round(float(v[0]) / v[1], 3)}
                             ]
                    elif k == 'favorable':
                        ret['completeness_of_favorable_assignments'] =\
                            [{'atom_group': 'favorable_all_chemical_shifts',
                              'number_of_assigned_shifts': v[0],
                              'number_of_target_shifts': v[1],
                              'completeness': round(float(v[0]) / v[1], 3)}
                             ]
                    elif k == 'backbone':
                        ret['completeness_of_backbone_assignments'] =\
                            [{'atom_group': 'backbone_all_chemical_shifts',
                              'number_of_assigned_shifts': v[0],
                              'number_of_target_shifts': v[1],
                              'completeness': round(float(v[0]) / v[1], 3)}
                             ]
                    elif k == 'sidechain':
                        ret['completeness_of_sidechain_assignments'] =\
                            [{'atom_group': 'sidechain_all_chemical_shifts',
                              'number_of_assigned_shifts': v[0],
                              'number_of_target_shifts': v[1],
                              'completeness': round(float(v[0]) / v[1], 3)}
                             ]
                    elif k == 'aromatic':
                        ret['completeness_of_aromatic_assignments'] =\
                            [{'atom_group': 'aromatic_all_chemical_shifts',
                              'number_of_assigned_shifts': v[0],
                              'number_of_target_shifts': v[1],
                              'completeness': round(float(v[0]) / v[1], 3)}
                             ]
                    elif k == 'sugar':
                        ret['completeness_of_sugar_assignments'] =\
                            [{'atom_group': 'sugar_all_chemical_shifts',
                              'number_of_assigned_shifts': v[0],
                              'number_of_target_shifts': v[1],
                              'completeness': round(float(v[0]) / v[1], 3)}
                             ]
                    elif k == 'base':
                        ret['completeness_of_base_assignments'] =\
                            [{'atom_group': 'base_all_chemical_shifts',
                              'number_of_assigned_shifts': v[0],
                              'number_of_target_shifts': v[1],
                              'completeness': round(float(v[0]) / v[1], 3)}
                             ]

                for k, v in src['H'].items():
                    if v[1] == 0:
                        continue
                    if k == 'overall':
                        ret['completeness_of_overall_assignments'].append(
                            {'atom_group': 'overall_1h_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'favorable':
                        ret['completeness_of_favorable_assignments'].append(
                            {'atom_group': 'favorable_1h_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'backbone':
                        ret['completeness_of_backbone_assignments'].append(
                            {'atom_group': 'backbone_1h_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'sidechain':
                        ret['completeness_of_sidechain_assignments'].append(
                            {'atom_group': 'sidechain_1h_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'aromatic':
                        ret['completeness_of_aromatic_assignments'].append(
                            {'atom_group': 'aromatic_1h_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'sugar':
                        ret['completeness_of_sugar_assignments'].append(
                            {'atom_group': 'sugar_1h_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'base':
                        ret['completeness_of_base_assignments'].append(
                            {'atom_group': 'base_1h_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})

                for k, v in src['C'].items():
                    if v[1] == 0:
                        continue
                    if k == 'overall':
                        ret['completeness_of_overall_assignments'].append(
                            {'atom_group': 'overall_13c_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'favorable':
                        ret['completeness_of_favorable_assignments'].append(
                            {'atom_group': 'favorable_13c_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'backbone':
                        ret['completeness_of_backbone_assignments'].append(
                            {'atom_group': 'backbone_13c_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'sidechain':
                        ret['completeness_of_sidechain_assignments'].append(
                            {'atom_group': 'sidechain_13c_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'aromatic':
                        ret['completeness_of_aromatic_assignments'].append(
                            {'atom_group': 'aromatic_13c_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'sugar':
                        ret['completeness_of_sugar_assignments'].append(
                            {'atom_group': 'sugar_13c_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'base':
                        ret['completeness_of_base_assignments'].append(
                            {'atom_group': 'base_13c_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})

                for k, v in src['N'].items():
                    if v[1] == 0:
                        continue
                    if k == 'overall':
                        ret['completeness_of_overall_assignments'].append(
                            {'atom_group': 'overall_15n_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'favorable':
                        ret['completeness_of_favorable_assignments'].append(
                            {'atom_group': 'favorable_15n_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'backbone':
                        ret['completeness_of_backbone_assignments'].append(
                            {'atom_group': 'backbone_15n_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'sidechain':
                        ret['completeness_of_sidechain_assignments'].append(
                            {'atom_group': 'sidechain_15n_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'aromatic':
                        ret['completeness_of_aromatic_assignments'].append(
                            {'atom_group': 'aromatic_15n_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'sugar':
                        ret['completeness_of_sugar_assignments'].append(
                            {'atom_group': 'sugar_15n_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'base':
                        ret['completeness_of_base_assignments'].append(
                            {'atom_group': 'base_15n_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})

                for k, v in src['P'].items():
                    if v[1] == 0:
                        continue
                    if k == 'overall':
                        ret['completeness_of_overall_assignments'].append(
                            {'atom_group': 'overall_31p_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'favorable':
                        ret['completeness_of_favorable_assignments'].append(
                            {'atom_group': 'favorable_31p_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'backbone':
                        ret['completeness_of_backbone_assignments'].append(
                            {'atom_group': 'backbone_31p_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'sidechain':
                        ret['completeness_of_sidechain_assignments'].append(
                            {'atom_group': 'sidechain_31p_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'aromatic':
                        ret['completeness_of_aromatic_assignments'].append(
                            {'atom_group': 'aromatic_31p_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'sugar':
                        ret['completeness_of_sugar_assignments'].append(
                            {'atom_group': 'sugar_31p_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})
                    elif k == 'base':
                        ret['completeness_of_base_assignments'].append(
                            {'atom_group': 'base_31p_chemical_shifts',
                             'number_of_assigned_shifts': v[0],
                             'number_of_target_shifts': v[1],
                             'completeness': round(float(v[0]) / v[1], 3)})

                if 'stereomethyl' in src:
                    v = src['stereomethyl']
                    if v[1] > 0:
                        ret['completeness_of_stereomethyl_assignments'] =\
                            [{'atom_group': 'stereomethyl_13c_chemical_shifts',
                              'number_of_assigned_shifts': v[0],
                              'number_of_target_shifts': v[1],
                              'completeness': round(float(v[0]) / v[1], 3)}]

                return ret

            has_dist = vrpt_mr is not None and 'distance_summary' in vrpt_mr
            dist_any_type = 'total'
            dist_types = ('intraresidue', 'sequential', 'medium', 'long', 'interchain',
                          'hbond', 'sbond', 'sebond', 'metal', dist_any_type)
            dist_type_names = ('intra-residue', 'sequential', 'medium_range', 'long_range', 'inter-chain',
                               'hydrogen_bond', 'disulfide_bond', 'diselenide_bond', 'metal_coordiantion', dist_any_type)
            dist_type_abbrs = ('ir', 'sq', 'mr', 'lr', 'ic', 'hb', 'sb', 'seb', 'metal', 'total')
            dist_sub_types = ('backbone-backbone', 'backbone-sidechain', 'sidechain-sidechain')
            dist_bond_types = ('hbond', 'sbond', 'sebond', 'metal')
            dist_general_bond_types = ('hbond', 'sbond', 'sebond', 'metal', None)

            has_dihed = vrpt_mr is not None and 'angle_summary' in vrpt_mr
            dihed_any_type = 'Total'
            dihed_types = vrpt_mr['key_lists']['angle_type'] if has_dihed else []

            has_rdc = vrpt_mr is not None and 'rdc_summary' in vrpt_mr
            rdc_any_type = 'Total'
            rdc_types = vrpt_mr['key_lists']['rdc_type'] if has_rdc else []

            total_dist_restraint_count = sum(vrpt_mr['distance_summary'][dist_any_type][dist_sub_type][None]
                                             for dist_sub_type in dist_sub_types) if has_dist else 0
            total_dihed_restraint_count = vrpt_mr['angle_summary'][dihed_any_type] if has_dihed else 0
            total_rdc_restraint_count = vrpt_mr['rdc_summary'][rdc_any_type] if has_rdc else 0

            # integrate RDC correlation plot of observed and calculated RDCs
            if has_rdc and 'rdc_correlation_plot' in vrpt_mr:
                rdc_correlation_plot = vrpt_mr['rdc_correlation_plot']

                input_source_ = self._reg.report_prev.input_sources[0]
                input_source_dic_ = input_source_.get()
                content_subtypes_ = input_source_dic_['content_subtype']

                if 'rdc_restraint' in content_subtypes_ and 'stats_of_exptl_data' in input_source_dic_:
                    stats_of_exptl_data = input_source_dic_['stats_of_exptl_data']

                    if 'rdc_restraint' in stats_of_exptl_data:

                        for rdc_stat in stats_of_exptl_data['rdc_restraint']:
                            list_id = rdc_stat['list_id']

                            if list_id in rdc_correlation_plot:
                                rdc_stat['correlation_plot'] = rdc_correlation_plot[list_id]

            def get_dist_violations_per_model():
                violations_per_model = []
                for k, v in vrpt_mr['residual_distance_violation'].items():
                    len_bin = len(violations_per_model)
                    bin_suffix = ' (' + ('Small' if len_bin == 0
                                         else 'Medium' if len_bin == 1
                                         else 'Large') + ')'
                    violations_per_model.append({'bin_type': k + bin_suffix,
                                                 'average_number_of_violations_per_model': v[0][3],
                                                 'max_violation_in_bin': v[0][1]})
                return violations_per_model

            def get_dihed_violation_per_model():
                violations_per_model = []
                for k, v in vrpt_mr['residual_angle_violation'].items():
                    len_bin = len(violations_per_model)
                    bin_suffix = ' (' + ('Small' if len_bin == 0
                                         else 'Medium' if len_bin == 1
                                         else 'Large') + ')'
                    violations_per_model.append({'bin_type': k + bin_suffix,
                                                 'average_number_of_violations_per_model': v[0][3],
                                                 'max_violation_in_bin': v[0][1]})
                return violations_per_model

            def get_rdc_violation_per_model():
                violations_per_model = []
                for k, v in vrpt_mr['residual_rdc_violation'].items():
                    len_bin = len(violations_per_model)
                    bin_suffix = ' (' + ('Small' if len_bin == 0
                                         else 'Medium' if len_bin == 1
                                         else 'Large') + ')'
                    violations_per_model.append({'bin_type': k + bin_suffix,
                                                 'average_number_of_violations_per_model': v[0][3],
                                                 'max_violation_in_bin': v[0][1]})
                return violations_per_model

            def get_dist_violation_summary():
                violation_summary = []
                for dist_type in dist_types:
                    name_suffix = ''
                    if dist_type == 'intraresidue':
                        name_suffix = ' (|i - j| = 0)'
                    elif dist_type == 'sequential':
                        name_suffix = ' (|i - j| = 1)'
                    elif dist_type == 'medium':
                        name_suffix = ' (1 < |i - j| < 5)'
                    elif dist_type == 'long':
                        name_suffix = ' (|i - j| ≥ 5)'
                    restraint_type = dist_type_names[dist_types.index(dist_type)] + name_suffix
                    bond_type = dist_type if dist_type in ('hbond', 'sbond', 'sebond', 'metal') else None
                    if bond_type is None:
                        restraint_count = sum(vrpt_mr['distance_summary'][dist_type][dist_sub_type][bond_type]
                                              for dist_sub_type in dist_sub_types)
                    else:
                        restraint_count = sum(vrpt_mr['distance_summary'][dist_any_type][dist_sub_type][bond_type]
                                              for dist_sub_type in dist_sub_types)

                    if restraint_count == 0:
                        if dist_type in ('sebond', 'metal'):
                            continue
                        if dist_type == 'sbond' and not has_cysteine:
                            continue

                    restraint_percent = round(100.0 * restraint_count / total_dist_restraint_count, 1)

                    if bond_type is None:
                        viol_count = sum(vrpt_mr['distance_violation'][dist_type][dist_sub_type][bond_type]
                                         for dist_sub_type in dist_sub_types)
                    else:
                        viol_count = sum(vrpt_mr['distance_violation'][dist_any_type][dist_sub_type][bond_type]
                                         for dist_sub_type in dist_sub_types)

                    viol_inline_percent = round(100.0 * viol_count / restraint_count, 1)\
                        if restraint_count > 0 else None
                    viol_absol_percent = round(100.0 * viol_count / total_dist_restraint_count, 1)

                    if bond_type is None:
                        consist_viol_count = sum(vrpt_mr['consistent_distance_violation'][dist_type][dist_sub_type][bond_type]
                                                 for dist_sub_type in dist_sub_types)
                    else:
                        consist_viol_count = sum(vrpt_mr['consistent_distance_violation'][dist_any_type][dist_sub_type][bond_type]
                                                 for dist_sub_type in dist_sub_types)

                    consist_viol_inline_percent = round(100.0 * consist_viol_count / restraint_count, 1)\
                        if restraint_count > 0 else None
                    consist_viol_absol_percent = round(100.0 * consist_viol_count / total_dist_restraint_count, 1)

                    violation_summary.append({'restraint_type': restraint_type, 'restraint_count': restraint_count,
                                              'restraint_percent': restraint_percent,
                                              'viol_count': viol_count, 'viol_inline_percent': viol_inline_percent,
                                              'viol_absol_percent': viol_absol_percent,
                                              'consist_viol_count': consist_viol_count,
                                              'consist_viol_inline_percent': consist_viol_inline_percent,
                                              'consist_viol_absol_percent': consist_viol_absol_percent
                                              })

                    if dist_type in dist_bond_types:
                        continue

                    for dist_sub_type in dist_sub_types:
                        restraint_type = dist_type_abbrs[dist_types.index(dist_type)] + '; ' + dist_sub_type
                        bond_type = None
                        restraint_count = vrpt_mr['distance_summary'][dist_type][dist_sub_type][bond_type]

                        percent = round(100.0 * restraint_count / total_dist_restraint_count, 1)

                        viol_count = vrpt_mr['distance_violation'][dist_type][dist_sub_type][bond_type]

                        viol_inline_percent = round(100.0 * viol_count / restraint_count, 1)\
                            if restraint_count > 0 else None
                        viol_absol_percent = round(100.0 * viol_count / total_dist_restraint_count, 1)

                        consist_viol_count = vrpt_mr['consistent_distance_violation'][dist_type][dist_sub_type][bond_type]

                        consist_viol_inline_percent = round(100.0 * consist_viol_count / restraint_count, 1)\
                            if restraint_count > 0 else None
                        consist_viol_absol_percent = round(100.0 * consist_viol_count / total_dist_restraint_count, 1)

                        violation_summary.append({'restraint_type': restraint_type, 'restraint_count': restraint_count,
                                                  'restraint_percent': percent,
                                                  'viol_count': viol_count, 'viol_inline_percent': viol_inline_percent,
                                                  'viol_absol_percent': viol_absol_percent,
                                                  'consist_viol_count': consist_viol_count,
                                                  'consist_viol_inline_percent': consist_viol_inline_percent,
                                                  'consist_viol_absol_percent': consist_viol_absol_percent
                                                  })

                return violation_summary

            def get_dihed_violation_summary():
                violation_summary = []
                for dihed_type in dihed_types:
                    restraint_type = dihed_type.lower()
                    restraint_count = vrpt_mr['angle_summary'][dihed_type]
                    restraint_percent = round(100.0 * restraint_count / total_dihed_restraint_count, 1)

                    viol_count = vrpt_mr['angle_violation'][dihed_type]
                    viol_inline_percent = round(100.0 * viol_count / restraint_count, 1)\
                        if restraint_count > 0 else None
                    viol_absol_percent = round(100.0 * viol_count / total_dihed_restraint_count, 1)

                    consist_viol_count = vrpt_mr['consistent_angle_violation'][dihed_type]
                    consist_viol_inline_percent = round(100.0 * consist_viol_count / restraint_count, 1)\
                        if restraint_count > 0 else None
                    consist_viol_absol_percent = round(100.0 * consist_viol_count / total_dihed_restraint_count, 1)

                    violation_summary.append({'restraint_type': restraint_type, 'restraint_count': restraint_count,
                                              'restraint_percent': restraint_percent,
                                              'viol_count': viol_count, 'viol_inline_percent': viol_inline_percent,
                                              'viol_absol_percent': viol_absol_percent,
                                              'consist_viol_count': consist_viol_count,
                                              'consist_viol_inline_percent': consist_viol_inline_percent,
                                              'consist_viol_absol_percent': consist_viol_absol_percent
                                              })

                return violation_summary

            def get_rdc_violation_summary():
                violation_summary = []
                for rdc_type in rdc_types:
                    restraint_type = rdc_type.lower()
                    restraint_count = vrpt_mr['rdc_summary'][rdc_type]
                    restraint_percent = round(100.0 * restraint_count / total_rdc_restraint_count, 1)

                    viol_count = vrpt_mr['rdc_violation'][rdc_type]
                    viol_inline_percent = round(100.0 * viol_count / restraint_count, 1)\
                        if restraint_count > 0 else None
                    viol_absol_percent = round(100.0 * viol_count / total_rdc_restraint_count, 1)

                    consist_viol_count = vrpt_mr['consistent_rdc_violation'][rdc_type]
                    consist_viol_inline_percent = round(100.0 * consist_viol_count / restraint_count, 1)\
                        if restraint_count > 0 else None
                    consist_viol_absol_percent = round(100.0 * consist_viol_count / total_rdc_restraint_count, 1)

                    violation_summary.append({'restraint_type': restraint_type, 'restraint_count': restraint_count,
                                              'restraint_percent': restraint_percent,
                                              'viol_count': viol_count, 'viol_inline_percent': viol_inline_percent,
                                              'viol_absol_percent': viol_absol_percent,
                                              'consist_viol_count': consist_viol_count,
                                              'consist_viol_inline_percent': consist_viol_inline_percent,
                                              'consist_viol_absol_percent': consist_viol_absol_percent
                                              })

                return violation_summary

            def get_dist_violation_for_each_model():
                violation_summary = []
                for model_id in self._reg.eff_model_ids:
                    item = {'model_id': model_id}
                    errors = []
                    for dist_type in dist_types:
                        if dist_type in dist_bond_types:
                            continue
                        viol_type = dist_type_abbrs[dist_types.index(dist_type)] + '_viol_count'
                        count = 0
                        for dist_sub_type in dist_sub_types:
                            for bond_type in dist_general_bond_types:
                                count += len(vrpt_mr['distance_violations_in_models'][
                                    model_id][dist_type][dist_sub_type][bond_type])
                                errors.extend(vrpt_mr['distance_violations_in_models'][
                                    model_id][dist_type][dist_sub_type][bond_type])
                        item[viol_type] = count

                    if len(errors) > 1:
                        _errors = numpy.array(errors, dtype=float)

                        item['mean_violation'] = round(numpy.mean(_errors), 2)
                        item['min_violation'] = round(numpy.min(_errors), 2)
                        item['max_violation'] = round(numpy.max(_errors), 2)
                        item['std_violation'] = round(numpy.std(_errors), 2)
                        item['median_violation'] = round(numpy.median(_errors), 2)

                    else:
                        item['mean_violation'] = item['min_violation'] = item['max_violation'] =\
                            item['std_violation'] = item['median_violation'] = None

                    violation_summary.append(item)

                return violation_summary

            def get_dihed_violation_for_each_model():
                violation_summary = []
                for model_id in self._reg.eff_model_ids:
                    item = {'model_id': model_id}
                    errors = []
                    for dihed_type in dihed_types:
                        viol_type = dihed_type.lower() + '_viol_count'
                        item[viol_type] = len(vrpt_mr['angle_violations_in_models'][model_id][dihed_type])
                        errors.extend(vrpt_mr['angle_violations_in_models'][model_id][dihed_type])

                    if len(errors) > 1:
                        _errors = numpy.array(errors, dtype=float)

                        item['mean_violation'] = round(numpy.mean(_errors), 2)
                        item['min_violation'] = round(numpy.min(_errors), 2)
                        item['max_violation'] = round(numpy.max(_errors), 2)
                        item['std_violation'] = round(numpy.std(_errors), 2)
                        item['median_violation'] = round(numpy.median(_errors), 2)

                    else:
                        item['mean_violation'] = item['min_violation'] = item['max_violation'] =\
                            item['std_violation'] = item['median_violation'] = None

                    violation_summary.append(item)

                return violation_summary

            def get_rdc_violation_for_each_model():
                violation_summary = []
                for model_id in self._reg.eff_model_ids:
                    item = {'model_id': model_id}
                    errors = []
                    for rdc_type in rdc_types:
                        viol_type = rdc_type.lower() + '_viol_count'
                        item[viol_type] = len(vrpt_mr['rdc_violations_in_models'][model_id][rdc_type])
                        errors.extend(vrpt_mr['rdc_violations_in_models'][model_id][rdc_type])

                    if len(errors) > 1:
                        _errors = numpy.array(errors, dtype=float)

                        item['mean_violation'] = round(numpy.mean(_errors), 2)
                        item['min_violation'] = round(numpy.min(_errors), 2)
                        item['max_violation'] = round(numpy.max(_errors), 2)
                        item['std_violation'] = round(numpy.std(_errors), 2)
                        item['median_violation'] = round(numpy.median(_errors), 2)

                    else:
                        item['mean_violation'] = item['min_violation'] = item['max_violation'] =\
                            item['std_violation'] = item['median_violation'] = None

                    violation_summary.append(item)

                return violation_summary

            def get_dist_violation_for_ensemble():
                violation_summary = []
                len_eff_model_ids = len(self._reg.eff_model_ids)
                for fraction in range(1, len_eff_model_ids + 1):
                    item = {'fraction_count': fraction,
                            'fraction_percent': round(100.0 * fraction / len_eff_model_ids, 1)}
                    for dist_type in dist_types:
                        if dist_type in dist_bond_types:
                            continue
                        viol_type = dist_type_abbrs[dist_types.index(dist_type)] + '_viol_count'
                        count = 0
                        for dist_sub_type in dist_sub_types:
                            for bond_type in dist_general_bond_types:
                                count += vrpt_mr['distance_violations_vs_models'][
                                    dist_type][dist_sub_type][bond_type][fraction]
                        item[viol_type] = count

                    violation_summary.append(item)

                return violation_summary

            def get_dihed_violation_for_ensemble():
                violation_summary = []
                len_eff_model_ids = len(self._reg.eff_model_ids)
                for fraction in range(1, len_eff_model_ids + 1):
                    item = {'fraction_count': fraction,
                            'fraction_percent': round(100.0 * fraction / len_eff_model_ids, 1)}
                    for dihed_type in dihed_types:
                        viol_type = dihed_type.lower() + '_viol_count'
                        item[viol_type] = vrpt_mr['angle_violations_vs_models'][dihed_type][fraction]

                    violation_summary.append(item)

                return violation_summary

            def get_rdc_violation_for_ensemble():
                violation_summary = []
                len_eff_model_ids = len(self._reg.eff_model_ids)
                for fraction in range(1, len_eff_model_ids + 1):
                    item = {'fraction_count': fraction,
                            'fraction_percent': round(100.0 * fraction / len_eff_model_ids, 1)}
                    for rdc_type in rdc_types:
                        viol_type = rdc_type.lower() + '_viol_count'
                        item[viol_type] = vrpt_mr['rdc_violations_vs_models'][rdc_type][fraction]

                    violation_summary.append(item)

                return violation_summary

            def convert_to_rest_key(array):
                return '(' + ','.join([str(k) for k in array]) + ')'

            def convert_to_atom_key(array):
                _array = list(array[:-1])
                _array[1] = str(array[1])
                _ins_code = array[-1]
                if _ins_code in EMPTY_VALUE:
                    return ':'.join(_array)
                _array[1] += _ins_code
                return ':'.join(_array)

            def convert_to_distance_type(d_type, b_type):
                if b_type is None:
                    if d_type in dist_types:
                        return dist_type_names[dist_types.index(d_type)]
                    return 'unknown'
                if b_type in dist_types:
                    return dist_type_names[dist_types.index(b_type)]
                return 'unknown'

            def get_most_violated_dist_restraints():
                if len(vrpt_mr['most_violated_distance']) == 0:
                    return None

                violations = []
                for dist_viol in vrpt_mr['most_violated_distance']:
                    violations.append({'restraint_key': convert_to_rest_key(dist_viol[0]),
                                       'atom_key_1': convert_to_atom_key(dist_viol[1]),
                                       'atom_key_2': convert_to_atom_key(dist_viol[2]),
                                       'distance_type': convert_to_distance_type(dist_viol[3], dist_viol[5]),
                                       'total_violated_models': dist_viol[6],
                                       'violated_model_id': dist_viol[7],
                                       'min_violation': dist_viol[8],
                                       'max_violation': dist_viol[9],
                                       'mean_violation': round(dist_viol[10], 2),
                                       'std_violation': round(dist_viol[11], 2),
                                       'median_violation': round(dist_viol[12], 2)})

                return violations

            def get_most_violated_dihed_restraints():
                if len(vrpt_mr['most_violated_angle']) == 0:
                    return None

                violations = []
                for dihed_viol in vrpt_mr['most_violated_angle']:
                    violations.append({'restraint_key': convert_to_rest_key(dihed_viol[0]),
                                       'atom_key_1': convert_to_atom_key(dihed_viol[1]),
                                       'atom_key_2': convert_to_atom_key(dihed_viol[2]),
                                       'atom_key_3': convert_to_atom_key(dihed_viol[3]),
                                       'atom_key_4': convert_to_atom_key(dihed_viol[4]),
                                       'dihedral_angle_name': dihed_viol[5],
                                       'total_violated_models': dihed_viol[6],
                                       'violated_model_id': dihed_viol[7],
                                       'min_violation': dihed_viol[8],
                                       'max_violation': dihed_viol[9],
                                       'mean_violation': round(dihed_viol[10], 2),
                                       'std_violation': round(dihed_viol[11], 2),
                                       'median_violation': round(dihed_viol[12], 2)})

                return violations

            def get_most_violated_rdc_restraints():
                if len(vrpt_mr['most_violated_rdc']) == 0:
                    return None

                violations = []
                for rdc_viol in vrpt_mr['most_violated_rdc']:
                    violations.append({'restraint_key': convert_to_rest_key(rdc_viol[0]),
                                       'atom_key_1': convert_to_atom_key(rdc_viol[1]),
                                       'atom_key_2': convert_to_atom_key(rdc_viol[2]),
                                       'rdc_type': rdc_viol[3],
                                       'total_violated_models': rdc_viol[4],
                                       'violated_model_id': rdc_viol[5],
                                       'min_violation': rdc_viol[6],
                                       'max_violation': rdc_viol[7],
                                       'mean_violation': round(rdc_viol[8], 2),
                                       'std_violation': round(rdc_viol[9], 2),
                                       'median_violation': round(rdc_viol[10], 2)})

                return violations

            def get_all_dist_violations():
                if len(vrpt_mr['all_distance_violations']) == 0:
                    return None

                violations = []
                for dist_viol in vrpt_mr['all_distance_violations']:
                    violations.append({'restraint_key': convert_to_rest_key(dist_viol[0]),
                                       'atom_key_1': convert_to_atom_key(dist_viol[1]),
                                       'atom_key_2': convert_to_atom_key(dist_viol[2]),
                                       'distance_type': convert_to_distance_type(dist_viol[4], dist_viol[6]),
                                       'model_id': dist_viol[3],
                                       'violation': dist_viol[7]})

                return violations

            def get_all_dihed_violations():
                if len(vrpt_mr['all_angle_violations']) == 0:
                    return None

                violations = []
                for dihed_viol in vrpt_mr['all_angle_violations']:
                    violations.append({'restraint_key': convert_to_rest_key(dihed_viol[0]),
                                       'atom_key_1': convert_to_atom_key(dihed_viol[1]),
                                       'atom_key_2': convert_to_atom_key(dihed_viol[2]),
                                       'atom_key_3': convert_to_atom_key(dihed_viol[3]),
                                       'atom_key_4': convert_to_atom_key(dihed_viol[4]),
                                       'dihedral_angle_name': dihed_viol[6],
                                       'model_id': dihed_viol[5],
                                       'violation': dihed_viol[7]})

                return violations

            def get_all_rdc_violations():
                if len(vrpt_mr['all_rdc_violations']) == 0:
                    return None

                violations = []
                for dihed_viol in vrpt_mr['all_rdc_violations']:
                    violations.append({'restraint_key': convert_to_rest_key(dihed_viol[0]),
                                       'atom_key_1': convert_to_atom_key(dihed_viol[1]),
                                       'atom_key_2': convert_to_atom_key(dihed_viol[2]),
                                       'rdc_type': dihed_viol[4],
                                       'model_id': dihed_viol[3],
                                       'violation': dihed_viol[5]})

                return violations

            # exptl data

            for content_subtype in ('chem_shift', 'dist_restraint', 'dihed_restraint', 'rdc_restraint', 'spectral_peak'):

                sf_category = SF_CATEGORIES[file_type][content_subtype]

                sf_list = master_entry.get_saveframes_by_category(sf_category)

                if len(sf_list) == 0:
                    continue

                sf_info_list = []

                for sf in sf_list:

                    list_id = get_first_sf_tag(sf, 'ID', None)

                    if list_id is None:
                        continue

                    if isinstance(list_id, str):
                        list_id = int(list_id)

                    sf_framecode = get_first_sf_tag(sf, 'Sf_framecode')

                    sf_info = {'list_id': list_id,
                               'sf_framecode': sf_framecode
                               }

                    data_file_name = get_first_sf_tag(sf, 'Data_file_name', None)
                    if data_file_name is not None:
                        sf_info['original_file_name'] = data_file_name

                    consist_id_tag = CONSIST_ID_TAGS[file_type][content_subtype]
                    lp_category = LP_CATEGORIES[file_type][content_subtype]

                    _content_subtype = content_subtype
                    if content_subtype == 'spectral_peak':
                        try:
                            sf.get_loop(lp_category)
                        except KeyError:
                            _content_subtype = 'spectral_peak_alt'
                            lp_category = LP_CATEGORIES[file_type][_content_subtype]

                    err_data_type = ''

                    try:

                        lp = sf.get_loop(lp_category)

                        consist_ids = set(row for row in lp.get_tag([consist_id_tag]))

                        sf_info['number_of_parsed'] = len(consist_ids)

                        if content_subtype == 'chem_shift':

                            if vrpt_cs is not None and 'shift_summary_table' in vrpt_cs\
                               and list_id in vrpt_cs['shift_summary_table']:
                                summary = vrpt_cs['shift_summary_table'][list_id]

                                sf_info['number_of_parsed'] = summary['number_of_parsed_shifts']
                                sf_info['number_of_unparsed_with_error'] = summary['number_of_unparsed_shifts']
                                sf_info['number_of_mapped_to_model'] = summary['number_of_mapped_shifts']
                                sf_info['number_of_mapped_to_unmodel'] = summary['number_of_warnings_while_mapping']
                                # DAOTHER-10987
                                sf_info['number_of_unmapped_to_model'] = summary['number_of_errors_while_mapping']

                            else:

                                tags = ['ID', 'Auth_asym_ID', 'Auth_seq_ID', 'Auth_comp_ID', 'Auth_atom_ID', 'Details']

                                if set(tags) & set(lp.tags) != set(tags):
                                    sf_info['number_of_mapped_to_model'] = 0
                                    sf_info['number_of_unmapped_to_model'] = sf_info['number_of_parsed']

                                else:

                                    dat = lp.get_tag(tags)

                                    mapped_ids = set()
                                    for row in dat:

                                        if row[5] == 'UNMAPPED':
                                            continue

                                        if all(row[col] not in EMPTY_VALUE for col in range(1, 5)):
                                            mapped_ids.add(row[0])

                                    sf_info['number_of_mapped_to_model'] = len(mapped_ids)
                                    sf_info['number_of_unmapped_to_model'] =\
                                        sf_info['number_of_parsed'] - sf_info['number_of_mapped_to_model']

                            if vrpt_cs is not None:
                                if 'completeness_items' in vrpt_cs\
                                   and list_id in vrpt_cs['completeness_items']:
                                    src_item = vrpt_cs['completeness_items'][list_id]['well_defined']
                                    sf_info['completeness_in_well_defined_region'] = map_completeness_of(src_item)

                                    src_item = vrpt_cs['completeness_items'][list_id]['full_length']
                                    sf_info['completeness_in_full_length_region'] = map_completeness_of(src_item)

                                if 'book_keeping' in vrpt_cs\
                                   and list_id in vrpt_cs['book_keeping']['cs_error']['CS_OUTLIER']:
                                    outlier = vrpt_cs['book_keeping']['cs_error']['CS_OUTLIER'][list_id]

                                    if len(outlier) > 0:
                                        sf_info['chemical_shift_outlier'] = []
                                        for row in outlier:
                                            auth_seq_id = None if row[1] in EMPTY_VALUE else int(row[1]) if row[1].isdigit()\
                                                else int(re.findall(r'\d+', row[1])[0])
                                            ins_code = None if row[1] in EMPTY_VALUE or row[1].isdigit()\
                                                else row[1][len(str(auth_seq_id)):]
                                            item = {'auth_chain_id': row[0],
                                                    'auth_seq_id': auth_seq_id,
                                                    'ins_code': ins_code,
                                                    'comp_id': row[2],
                                                    'atom_id': row[3],
                                                    'value': row[4],
                                                    'ambig_code': row[5],
                                                    'z_score': row[6],
                                                    'expected_range': {'min_value': row[7],
                                                                       'max_value': row[8]},
                                                    'details': row[9] if len(row) > 9 else None
                                                    }
                                            sf_info['chemical_shift_outlier'].append(item)

                                    sf_info['number_of_outliers'] = len(outlier)

                                if 'book_keeping' in vrpt_cs\
                                   and list_id in vrpt_cs['book_keeping']['cs_error']['CS_VALUE']:
                                    unparsed = vrpt_cs['book_keeping']['cs_error']['CS_VALUE'][list_id]

                                    if len(unparsed) > 0:
                                        sf_info['chemical_shift_unparsed'] = []
                                        for row in unparsed:
                                            auth_seq_id = None if row[1] in EMPTY_VALUE else int(row[1]) if row[1].isdigit()\
                                                else int(re.findall(r'\d+', row[1])[0])
                                            ins_code = None if row[1] in EMPTY_VALUE or row[1].isdigit()\
                                                else row[1][len(str(auth_seq_id)):]
                                            if row[4] in EMPTY_VALUE:
                                                value = None
                                            else:
                                                try:
                                                    value = float(row[4])
                                                except ValueError:
                                                    value = row[4]
                                            if row[5] in EMPTY_VALUE:
                                                error = None
                                            else:
                                                try:
                                                    error = float(row[5])
                                                except ValueError:
                                                    error = row[5]
                                            if row[6] in EMPTY_VALUE:
                                                ambig_code = None
                                            else:
                                                try:
                                                    ambig_code = int(row[6])
                                                except ValueError:
                                                    ambig_code = row[6]
                                            item = {'auth_chain_id': row[0],
                                                    'auth_seq_id': auth_seq_id,
                                                    'ins_code': ins_code,
                                                    'comp_id': row[2],
                                                    'atom_id': row[3],
                                                    'value': value,
                                                    'error': error,
                                                    'ambig_code': ambig_code
                                                    }
                                            sf_info['chemical_shift_unparsed'].append(item)

                                if 'book_keeping' in vrpt_cs\
                                   and list_id in vrpt_cs['book_keeping']['cs_error']['CS_DUPLICATE']:
                                    duplicated = vrpt_cs['book_keeping']['cs_error']['CS_DUPLICATE'][list_id]

                                    if len(duplicated) > 0:
                                        sf_info['chemical_shift_duplicated'] = []
                                        for row in duplicated:
                                            auth_seq_id = None if row[1] in EMPTY_VALUE else int(row[1]) if row[1].isdigit()\
                                                else int(re.findall(r'\d+', row[1])[0])
                                            ins_code = None if row[1] in EMPTY_VALUE or row[1].isdigit()\
                                                else row[1][len(str(auth_seq_id)):]
                                            item = {'auth_chain_id': row[0],
                                                    'auth_seq_id': auth_seq_id,
                                                    'ins_code': ins_code,
                                                    'comp_id': row[2],
                                                    'atom_id': row[3],
                                                    'value': row[4],
                                                    'error': row[5],
                                                    'ambig_code': row[6]
                                                    }
                                            sf_info['chemical_shift_duplicated'].append(item)

                                if 'book_keeping' in vrpt_cs\
                                   and list_id in vrpt_cs['book_keeping']['cs_error']['NO_MAP']:
                                    unmapped = vrpt_cs['book_keeping']['cs_error']['NO_MAP'][list_id]

                                    if len(unmapped) > 0:
                                        sf_info['chemical_shift_unmapped'] = []
                                        for row in unmapped:
                                            ins_code = None if 'ins_code' not in row or row['ins_code'] in EMPTY_VALUE\
                                                else row['ins_code']
                                            item = {'auth_chain_id': row['auth_chain_id'],
                                                    'auth_seq_id': row['auth_seq_id'],
                                                    'ins_code': ins_code,
                                                    'comp_id': row['comp_id'],
                                                    'atom_id': row['atom_id'],
                                                    'value': row['value'],
                                                    'error': row['error'],
                                                    'ambig_code': row['ambig_code']
                                                    }
                                            sf_info['chemical_shift_unmapped'].append(item)

                                if 'book_keeping' in vrpt_cs\
                                   and list_id in vrpt_cs['book_keeping']['cs_error']['NO_MODEL']:
                                    unmapped = vrpt_cs['book_keeping']['cs_error']['NO_MODEL'][list_id]

                                    if len(unmapped) > 0:
                                        sf_info['chemical_shift_unmodeled'] = []
                                        for row in unmapped:
                                            ins_code = None if 'ins_code' not in row or row['ins_code'] in EMPTY_VALUE\
                                                else row['ins_code']
                                            item = {'auth_chain_id': row['auth_chain_id'],
                                                    'auth_seq_id': row['auth_seq_id'],
                                                    'ins_code': ins_code,
                                                    'comp_id': row['comp_id'],
                                                    'atom_id': row['atom_id'],
                                                    'value': row['value'],
                                                    'error': row['error'],
                                                    'ambig_code': row['ambig_code']
                                                    }
                                            sf_info['chemical_shift_unmodeled'].append(item)

                                # modify existing histogram of assigned chemical shift

                                try:

                                    if not self._reg.cifChecked:
                                        item = next(item for item in self._reg.report.getNmrStatsOfExptlData(content_subtype)
                                                    if item['list_id'] == list_id)
                                    else:
                                        item = next(item
                                                    for item in self._reg.report_prev.getNmrStatsOfExptlData(content_subtype)
                                                    if item['list_id'] == list_id)

                                    sf_info['histogram'] = copy.deepcopy(item['histogram'])
                                    if len(sf_info['histogram']['annotations']) > 0 and self._reg.caC is not None:
                                        auth_to_star_seq = self._reg.caC['auth_to_star_seq']
                                        for ann in sf_info['histogram']['annotations']:
                                            chain_id = ann['chain_id']
                                            if isinstance(chain_id, str) and chain_id.isdigit():
                                                chain_id = int(chain_id)
                                            seq_id = ann['seq_id']
                                            seq_key = next((k for k, v in auth_to_star_seq.items()
                                                            if v[0] == chain_id and v[1] == seq_id), None)
                                            if seq_key is not None:
                                                ann['chain_id'] = seq_key[0]
                                                ann['seq_id'] = seq_key[1]

                                except (StopIteration, KeyError, TypeError):
                                    sf_info['histogram'] = None

                                if 'rci' in vrpt_cs and list_id in vrpt_cs['rci']:
                                    rci = vrpt_cs['rci'][list_id]

                                    if len(rci) > 0:
                                        sf_info['random_coil_index'] = []
                                        for auth_chain_id, result in rci.items():
                                            item = {'auth_chain_id': auth_chain_id,
                                                    'auth_seq_id': result['seq_id'],
                                                    'rci': result['rci'],
                                                    'nmr_rmsd': result['nmr_rmsd'],
                                                    's2': result['s2']}

                                            cif_ps = None
                                            if not self._reg.cifChecked:
                                                cif_ps = self._reg.report.getNmrPolymerSequenceOf(auth_chain_id)
                                            elif cif_poly_seq is not None:
                                                cif_ps = next((ps for ps in cif_poly_seq
                                                               if ps['auth_chain_id'] == auth_chain_id), None)

                                            if cif_ps is not None:
                                                item['comp_id'] = []
                                                has_struct_conf = 'struct_conf' in cif_ps
                                                if has_struct_conf:
                                                    item['struct_conf'] = []
                                                for auth_seq_id in result['seq_id']:
                                                    if not self._reg.cifChecked:
                                                        if auth_seq_id in cif_ps['seq_id']:
                                                            idx = cif_ps['seq_id'].index(auth_seq_id)
                                                            item['comp_id'].append(cif_ps['comp_id'][idx])
                                                    elif auth_seq_id in cif_ps['auth_seq_id']:
                                                        idx = cif_ps['auth_seq_id'].index(auth_seq_id)
                                                        item['comp_id'].append(cif_ps['comp_id'][idx])
                                                        if has_struct_conf:
                                                            item['struct_conf'].append(cif_ps['struct_conf'][idx])
                                                    else:
                                                        item['comp_id'].append(None)
                                                        if has_struct_conf:
                                                            item['struct_conf'].append(None)

                                                if 'well_defined_region' in cif_ps:
                                                    auth_to_star_seq = self._reg.caC['auth_to_star_seq']
                                                    coord_unobs_res = self._reg.caC['coord_unobs_res']
                                                    dom = [None] * len(result['rci'])
                                                    for idx, (seq_id, comp_id)\
                                                            in enumerate(zip(result['seq_id'], item['comp_id'])):
                                                        seq_key = (auth_chain_id, seq_id, comp_id)
                                                        _seq_key = (auth_chain_id, seq_id)
                                                        if _seq_key in coord_unobs_res:
                                                            dom[idx] = -1
                                                        elif seq_key in auth_to_star_seq:
                                                            for r in cif_ps['well_defined_region']:
                                                                if seq_id in r['seq_id']:
                                                                    dom[idx] = r['domain_id']
                                                                    break
                                                        else:
                                                            dom[idx] = -1
                                                    item['domain_id'] = dom

                                                    _score = 0.0
                                                    dom_idx = -1

                                                    for i, r in enumerate(cif_ps['well_defined_region']):
                                                        try:
                                                            score = r['percent_of_core']\
                                                                / max(r['medoid_rmsd'], 1.0)
                                                            if score > _score:
                                                                _score = score
                                                                dom_idx = i
                                                        except Exception:  # pylint: disable=broad-exception-caught
                                                            continue

                                                    if dom_idx != -1:
                                                        item['rmsd_in_well_defined_region'] =\
                                                            cif_ps['well_defined_region'][dom_idx]['medoid_rmsd']

                                            sf_info['random_coil_index'].append(item)

                        elif _content_subtype in ('dist_restraint', 'dihed_restraint', 'rdc_restraint', 'spectral_peak'):

                            if list_id == 1:

                                if _content_subtype == 'dist_restraint':
                                    if has_dist:
                                        dist_summary = vrpt_mr['distance_summary']
                                        rest_summary = {}
                                        rest_summary['total_distance_restraints'] =\
                                            sum(v[None] for v in dist_summary['total'].values())
                                        rest_summary['intra-residue'] =\
                                            sum(v[None] for v in dist_summary['intraresidue'].values())
                                        rest_summary['sequential'] =\
                                            sum(v[None] for v in dist_summary['sequential'].values())
                                        rest_summary['medium_range'] =\
                                            sum(v[None] for v in dist_summary['medium'].values())
                                        rest_summary['long_range'] =\
                                            sum(v[None] for v in dist_summary['long'].values())
                                        rest_summary['inter-chain'] =\
                                            sum(v[None] for v in dist_summary['interchain'].values())
                                        rest_summary['hydrogen_bond_restraints'] =\
                                            sum(v['hbond'] for v in dist_summary['total'].values())
                                        if rest_summary['hydrogen_bond_restraints'] > 0:
                                            rest_summary['hydrogen_bond_dist_types'] =\
                                                ','.join(dist_type_abbrs[dist_types.index(d_type)]
                                                         for d_type in dist_types
                                                         if d_type != dist_any_type
                                                         and d_type in dist_summary
                                                         and any(True for s_type in dist_sub_types
                                                                 if dist_summary[d_type][s_type]['hbond'] > 0))
                                        rest_summary['disulfide_bond_restraints'] =\
                                            sum(v['sbond'] for v in dist_summary['total'].values())
                                        if rest_summary['disulfide_bond_restraints'] == 0:
                                            if not has_cysteine:
                                                del rest_summary['disulfide_bond_restraints']
                                        else:
                                            rest_summary['disulfide_bond_dist_types'] =\
                                                ','.join(dist_type_abbrs[dist_types.index(d_type)]
                                                         for d_type in dist_types
                                                         if d_type != dist_any_type
                                                         and d_type in dist_summary
                                                         and any(True for s_type in dist_sub_types
                                                                 if dist_summary[d_type][s_type]['sbond'] > 0))
                                        rest_summary['diselenide_bond_restraints'] =\
                                            sum(v['sebond'] for v in dist_summary['total'].values())
                                        if rest_summary['diselenide_bond_restraints'] == 0:
                                            del rest_summary['diselenide_bond_restraints']
                                        else:
                                            rest_summary['diselenide_bond_dist_types'] =\
                                                ','.join(dist_type_abbrs[dist_types.index(d_type)]
                                                         for d_type in dist_types
                                                         if d_type != dist_any_type
                                                         and d_type in dist_summary
                                                         and any(True for s_type in dist_sub_types
                                                                 if dist_summary[d_type][s_type]['sebond'] > 0))
                                        rest_summary['metal_coordination_restraints'] =\
                                            sum(v['metal'] for v in dist_summary['total'].values())
                                        if rest_summary['metal_coordination_restraints'] == 0:
                                            del rest_summary['metal_coordination_restraints']
                                        else:
                                            rest_summary['metal_coordination_dist_types'] =\
                                                ','.join(dist_type_abbrs[dist_types.index(d_type)]
                                                         for d_type in dist_types
                                                         if d_type != dist_any_type
                                                         and d_type in dist_summary
                                                         and any(True for s_type in dist_sub_types
                                                                 if dist_summary[d_type][s_type]['metal'] > 0))
                                        if has_dihed:
                                            rest_summary['total_dihedral_angle_restraints'] = total_dihed_restraint_count
                                        if has_rdc:
                                            rest_summary['total_rdc_restraints'] = total_rdc_restraint_count
                                        all_unmapped = len(vrpt_mr['unmapped_dist'])
                                        if 'unmapped_angle' in vrpt_mr:
                                            all_unmapped += len(vrpt_mr['unmapped_angle'])
                                        if 'unmapped_rdc' in vrpt_mr:
                                            all_unmapped += len(vrpt_mr['unmapped_rdc'])
                                        rest_summary['number_of_unmapped_restraints'] = all_unmapped
                                        all_total = total_dist_restraint_count\
                                            + total_dihed_restraint_count\
                                            + total_rdc_restraint_count
                                        rest_summary['number_of_restraints_per_residue'] = \
                                            round(float(all_total) / vrpt_mr['seq_length'], 1)
                                        rest_summary['number_of_long_range_restraints_per_residue'] =\
                                            round(float(sum(sum(v.values()) for v in dist_summary['long'].values()))
                                                  / vrpt_mr['seq_length'], 1)

                                        rest_summary['average_number_of_dist_violations_per_model'] =\
                                            get_dist_violations_per_model()

                                        if 'residual_angle_violation' in vrpt_mr:
                                            rest_summary['average_number_of_dihed_violations_per_model'] =\
                                                get_dihed_violation_per_model()

                                        if 'residual_rdc_violation' in vrpt_mr:
                                            rest_summary['average_number_of_rdc_violations_per_model'] =\
                                                get_rdc_violation_per_model()

                                        if total_dist_restraint_count > 0:
                                            rest_summary['dist_violation_summary'] =\
                                                get_dist_violation_summary()

                                            rest_summary['dist_violation_for_each_model'] =\
                                                get_dist_violation_for_each_model()

                                            rest_summary['dist_violation_for_ensemble'] =\
                                                get_dist_violation_for_ensemble()

                                            rest_summary['most_violated_dist_restraints'] =\
                                                get_most_violated_dist_restraints()

                                            if rest_summary['most_violated_dist_restraints'] is None:
                                                del rest_summary['most_violated_dist_restraints']

                                            rest_summary['all_dist_violations'] =\
                                                get_all_dist_violations()

                                            if rest_summary['all_dist_violations'] is None:
                                                del rest_summary['all_dist_violations']

                                        if total_dihed_restraint_count > 0:
                                            rest_summary['dihed_violation_summary'] =\
                                                get_dihed_violation_summary()

                                            rest_summary['dihed_violation_for_each_model'] =\
                                                get_dihed_violation_for_each_model()

                                            rest_summary['dihed_violation_for_ensemble'] =\
                                                get_dihed_violation_for_ensemble()

                                            rest_summary['most_violated_dihed_restraints'] =\
                                                get_most_violated_dihed_restraints()

                                            if rest_summary['most_violated_dihed_restraints'] is None:
                                                del rest_summary['most_violated_dihed_restraints']

                                            rest_summary['all_dihed_violations'] =\
                                                get_all_dihed_violations()

                                            if rest_summary['all_dihed_violations'] is None:
                                                del rest_summary['all_dihed_violations']

                                        if total_rdc_restraint_count > 0:
                                            rest_summary['rdc_violation_summary'] =\
                                                get_rdc_violation_summary()

                                            rest_summary['rdc_violation_for_each_model'] =\
                                                get_rdc_violation_for_each_model()

                                            rest_summary['rdc_violation_for_ensemble'] =\
                                                get_rdc_violation_for_ensemble()

                                            rest_summary['most_violated_rdc_restraints'] =\
                                                get_most_violated_rdc_restraints()

                                            if rest_summary['most_violated_rdc_restraints'] is None:
                                                del rest_summary['most_violated_rdc_restraints']

                                            rest_summary['all_rdc_violations'] =\
                                                get_all_rdc_violations()

                                            if rest_summary['all_rdc_violations'] is None:
                                                del rest_summary['all_rdc_violations']

                                        self._reg.output_statistics.setItemValue('restraint_summary', rest_summary)

                                if _content_subtype == 'dihed_restraint':
                                    if has_dihed and not has_dist:
                                        rest_summary = {}
                                        rest_summary['total_distance_restraints'] = 0
                                        rest_summary['intra-residue'] = 0
                                        rest_summary['sequential'] = 0
                                        rest_summary['medium_range'] = 0
                                        rest_summary['long_range'] = 0
                                        rest_summary['inter-chain'] = 0
                                        rest_summary['hydrogen_bond_restraints'] = 0
                                        if has_cysteine:
                                            rest_summary['disulfide_bond_restraints'] = 0
                                        rest_summary['total_dihedral_angle_restraints'] = total_dihed_restraint_count
                                        if has_rdc:
                                            rest_summary['total_rdc_restraints'] = total_rdc_restraint_count
                                        all_unmapped = len(vrpt_mr['unmapped_angle'])
                                        if 'unmapped_rdc' in vrpt_mr:
                                            all_unmapped += len(vrpt_mr['unmapped_rdc'])
                                        rest_summary['number_of_unmapped_restraints'] = all_unmapped
                                        all_total = total_dihed_restraint_count + total_rdc_restraint_count
                                        rest_summary['number_of_restraints_per_residue'] = \
                                            round(float(all_total) / vrpt_mr['seq_length'], 1)
                                        rest_summary['number_of_long_range_restraints_per_residue'] = 0.0

                                        rest_summary['average_number_of_dihed_violations_per_model'] =\
                                            get_dihed_violation_per_model()

                                        if 'residual_rdc_violation' in vrpt_mr:
                                            rest_summary['average_number_of_rdc_violations_per_model'] =\
                                                get_rdc_violation_per_model()

                                        rest_summary['dihed_violation_summary'] =\
                                            get_dihed_violation_summary()

                                        rest_summary['dihed_violation_for_each_model'] =\
                                            get_dihed_violation_for_each_model()

                                        rest_summary['dihed_violation_for_ensemble'] =\
                                            get_dihed_violation_for_ensemble()

                                        rest_summary['most_violated_dihed_restraints'] =\
                                            get_most_violated_dihed_restraints()

                                        if rest_summary['most_violated_dihed_restraints'] is None:
                                            del rest_summary['most_violated_dihed_restraints']

                                        rest_summary['all_dihed_violations'] =\
                                            get_all_dihed_violations()

                                        if rest_summary['all_dihed_violations'] is None:
                                            del rest_summary['all_dihed_violations']

                                        if total_rdc_restraint_count > 0:
                                            rest_summary['rdc_violation_summary'] =\
                                                get_rdc_violation_summary()

                                            rest_summary['rdc_violation_for_each_model'] =\
                                                get_rdc_violation_for_each_model()

                                            rest_summary['rdc_violation_for_ensemble'] =\
                                                get_rdc_violation_for_ensemble()

                                            rest_summary['most_violated_rdc_restraints'] =\
                                                get_most_violated_rdc_restraints()

                                            if rest_summary['most_violated_rdc_restraints'] is None:
                                                del rest_summary['most_violated_rdc_restraints']

                                            rest_summary['all_rdc_violations'] =\
                                                get_all_rdc_violations()

                                            if rest_summary['all_rdc_violations'] is None:
                                                del rest_summary['all_rdc_violations']

                                        self._reg.output_statistics.setItemValue('restraint_summary', rest_summary)

                                if _content_subtype == 'rdc_restraint':
                                    if has_rdc and not has_dist and not has_dihed:
                                        rest_summary = {}
                                        rest_summary['total_distance_restraints'] = 0
                                        rest_summary['intra-residue'] = 0
                                        rest_summary['sequential'] = 0
                                        rest_summary['medium_range'] = 0
                                        rest_summary['long_range'] = 0
                                        rest_summary['inter-chain'] = 0
                                        rest_summary['hydrogen_bond_restraints'] = 0
                                        if has_cysteine:
                                            rest_summary['disulfide_bond_restraints'] = 0
                                        rest_summary['total_rdc_restraints'] = total_rdc_restraint_count
                                        rest_summary['number_of_unmapped_restraints'] = len(vrpt_mr['unmapped_rdc'])
                                        rest_summary['number_of_restraints_per_residue'] = \
                                            round(float(total_rdc_restraint_count) / vrpt_mr['seq_length'], 1)
                                        rest_summary['number_of_long_range_restraints_per_residue'] = 0.0

                                        rest_summary['average_number_of_rdc_violations_per_model'] =\
                                            get_rdc_violation_per_model()

                                        rest_summary['rdc_violation_summary'] =\
                                            get_rdc_violation_summary()

                                        rest_summary['rdc_violation_for_each_model'] =\
                                            get_rdc_violation_for_each_model()

                                        rest_summary['rdc_violation_for_ensemble'] =\
                                            get_rdc_violation_for_ensemble()

                                        rest_summary['most_violated_rdc_restraints'] =\
                                            get_most_violated_rdc_restraints()

                                        if rest_summary['most_violated_rdc_restraints'] is None:
                                            del rest_summary['most_violated_rdc_restraints']

                                        rest_summary['all_rdc_violations'] =\
                                            get_all_rdc_violations()

                                        if rest_summary['all_rdc_violations'] is None:
                                            del rest_summary['all_rdc_violations']

                                        self._reg.output_statistics.setItemValue('restraint_summary', rest_summary)

                            if content_subtype in ('dist_restraint', 'rdc_restraint'):
                                max_dim = 3

                            elif content_subtype == 'dihed_restraint':
                                max_dim = 5

                            else:  # 'spectral_peak'

                                try:

                                    _num_dim = get_first_sf_tag(sf, NUM_DIM_ITEMS[file_type])
                                    num_dim = int(_num_dim)

                                    if num_dim not in range(1, MAX_DIM_NUM_OF_SPECTRA):
                                        raise ValueError()

                                except ValueError:  # raised error already at __testIndexConsistency()
                                    continue

                                max_dim = num_dim + 1

                            tags = [consist_id_tag]
                            for j in range(1, max_dim):
                                tags.extend([f'Auth_asym_ID_{j}', f'Auth_seq_ID_{j}',
                                             f'Auth_comp_ID_{j}', f'Auth_atom_ID_{j}'])

                            if set(tags) & set(lp.tags) != set(tags):
                                sf_info['number_of_mapped_to_model'] = 0
                                sf_info['number_of_unmapped_to_model'] = sf_info['number_of_parsed']

                            else:

                                max_col = (max_dim - 1) * 4 + 1

                                dat = lp.get_tag(tags)

                                mapped_ids = set()
                                for row in dat:
                                    if all(row[col] not in EMPTY_VALUE for col in range(1, max_col)):
                                        mapped_ids.add(row[0])

                                sf_info['number_of_mapped_to_model'] = len(mapped_ids)
                                sf_info['number_of_unmapped_to_model'] =\
                                    sf_info['number_of_parsed'] - sf_info['number_of_mapped_to_model']

                        else:  # 'spectral_peak_alt'

                            try:

                                _num_dim = get_first_sf_tag(sf, NUM_DIM_ITEMS[file_type])
                                num_dim = int(_num_dim)

                                if num_dim not in range(1, MAX_DIM_NUM_OF_SPECTRA):
                                    raise ValueError()

                            except ValueError:  # raised error already at __testIndexConsistency()
                                continue

                            max_dim = num_dim + 1

                            try:

                                lp = sf.get_loop('_Assigned_peak_chem_shift')

                                tags = ['Peak_ID', 'Auth_entity_ID', 'Auth_seq_ID', 'Auth_comp_ID', 'Auth_atom_ID']

                                if set(tags) & set(lp.tags) != set(tags):
                                    sf_info['number_of_mapped_to_model'] = 0
                                    sf_info['number_of_unmapped_to_model'] = sf_info['number_of_parsed']

                                else:

                                    dat = lp.get_tag(tags)

                                    mapped_ids = set()
                                    unmapped_ids = set()
                                    for row in dat:
                                        if all(row[col] not in EMPTY_VALUE for col in range(1, 5)):
                                            mapped_ids.add(row[0])
                                        else:
                                            unmapped_ids.add(row[0])

                                    sf_info['number_of_mapped_to_model'] =\
                                        len(mapped_ids) - len(unmapped_ids)
                                    sf_info['number_of_unmapped_to_model'] =\
                                        sf_info['number_of_parsed'] - sf_info['number_of_mapped_to_model']

                            except KeyError:
                                sf_info['number_of_mapped_to_model'] = 0
                                sf_info['number_of_unmapped_to_model'] = sf_info['number_of_parsed']

                        if content_subtype != 'chem_shift' or vrpt_cs is None:
                            errors = self._reg.report.error.getInheritableDictBySf(sf_framecode)

                            err_ordinals = set()

                            if errors is None:
                                sf_info['number_of_unparsed_with_error'] = 0

                            else:

                                for k, v in errors.items():
                                    for item in v:
                                        for msg in item['description'].split('\n'):
                                            if INCONSISTENT_RESTRAINT_WARNING_WO_SF_PAT.match(msg):
                                                g = INCONSISTENT_RESTRAINT_WARNING_WO_SF_PAT.search(msg).groups()
                                                if g not in EMPTY_VALUE:
                                                    err_ordinals.add(g[0])
                                                    if len(err_data_type) == 0:
                                                        err_data_type = g[1]

                                sf_info['number_of_unparsed_with_error'] = len(err_ordinals)

                        warnings = self._reg.report.warning.getInheritableDictBySf(sf_framecode)

                        if warnings is None:
                            sf_info['number_of_parsed_with_warning'] = 0

                        else:

                            warn_ordinals = set()
                            for k, v in warnings.items():
                                is_err = 'restraint' in content_subtype and k in self._reg.report.warning.mr_err_items
                                for item in v:
                                    for msg in item['description'].split('\n'):
                                        if INCONSISTENT_RESTRAINT_WARNING_WO_SF_PAT.match(msg):
                                            g = INCONSISTENT_RESTRAINT_WARNING_WO_SF_PAT.search(msg).groups()
                                            if g not in EMPTY_VALUE:
                                                if is_err:
                                                    err_ordinals.add(g[0])
                                                    if len(err_data_type) == 0:
                                                        err_data_type = g[1]
                                                else:
                                                    warn_ordinals.add(g[0])

                            sf_info['number_of_parsed_with_warning'] = len(warn_ordinals)
                            sf_info['number_of_unparsed_with_error'] = len(err_ordinals)

                        index_tag = INDEX_TAGS[file_type][content_subtype]

                        if index_tag is not None:
                            conflict_warns = self._reg.report.warning.getValueListWithSf('conflicted_data', sf_framecode)
                            inconsist_warns = self._reg.report.warning.getValueListWithSf('inconsistent_data', sf_framecode)
                            redundant_warns = self._reg.report.warning.getValueListWithSf('redundant_data', sf_framecode)

                            warning_index = set()

                            if conflict_warns is not None:

                                for item in conflict_warns:
                                    if 'row_locations' in item:
                                        for index in item['row_locations'][index_tag]:
                                            warning_index.add(int(index))

                            if inconsist_warns is not None:

                                for item in inconsist_warns:
                                    if 'row_locations' in item:
                                        for index in item['row_locations'][index_tag]:
                                            warning_index.add(int(index))

                            if redundant_warns is not None:

                                for item in redundant_warns:
                                    if 'row_locations' in item:
                                        for index in item['row_locations'][index_tag]:
                                            warning_index.add(int(index))

                            sf_info['number_of_parsed_with_warning'] += len(warning_index)

                    except KeyError:
                        sf_info['number_of_parsed'] = \
                            sf_info['number_of_mapped_to_model'] = \
                            sf_info['number_of_unmapped_to_model'] = \
                            sf_info['number_of_unparsed_with_error'] =\
                            sf_info['number_of_parsed_with_warning'] = 0

                    if self._reg.conversion_server and 'number_of_unparsed_with_error' in sf_info\
                       and sf_info['number_of_unparsed_with_error'] > 0:

                        err = f"Failed in data conversion of {sf_info['number_of_unparsed_with_error']} {err_data_type}s "\
                            f"of {data_file_name!r}."

                        self._reg.report.error.appendDescription('unparsed_data',
                                                                 {'file_name': data_file_name, 'sf_framecode': sf_framecode,
                                                                  'description': err})

                        self._reg.log.write(f"+{self.__class_name__}.calculateOutputStats() ++ Error  - {err}\n")

                    try:

                        item = next(item for item in self._reg.report_prev.getNmrStatsOfExptlData(content_subtype)
                                    if item['list_id'] == list_id)
                        sf_info['atom_name_mapping'] = copy.copy(item['atom_name_mapping'])

                    except (StopIteration, KeyError, TypeError):
                        sf_info['atom_name_mapping'] = None

                    sf_info_list.append(sf_info)

                self._reg.output_statistics.setItemValue(content_subtype, sf_info_list)

        return self._reg.report.getTotalErrors() == __errors
