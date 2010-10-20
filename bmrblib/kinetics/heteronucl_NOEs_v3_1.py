#############################################################################
#                                                                           #
# The BMRB library.                                                         #
#                                                                           #
# Copyright (C) 2009-2010 Edward d'Auvergne                                 #
#                                                                           #
# This program is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                           #
#############################################################################

# Module docstring.
"""The v3.1 Heteronuclear NOE data saveframe category.

See http://www.bmrb.wisc.edu/dictionary/3.1html/SaveFramePage.html#heteronucl_NOEs.
"""

# relax module imports.
from bmrblib.misc import translate
from bmrblib.kinetics.heteronucl_NOEs import HeteronuclNOESaveframe, HeteronuclNOEList, HeteronuclNOEExperiment, HeteronuclNOESoftware, HeteronuclNOE


class HeteronuclNOESaveframe_v3_1(HeteronuclNOESaveframe):
    """The v3.1 Heteronuclear NOE data saveframe class."""

    def add(self, sample_cond_list_id=None, sample_cond_list_label='$conditions_1', temp_calibration=None, temp_control=None, peak_intensity_type=None, frq=None, details=None, assembly_atom_ids=None, entity_assembly_ids=None, entity_ids=None, res_nums=None, seq_id=None, res_names=None, atom_names=None, atom_types=None, isotope=None, assembly_atom_ids_2=None, entity_assembly_ids_2=None, entity_ids_2=None, res_nums_2=None, seq_id_2=None, res_names_2=None, atom_names_2=None, atom_types_2=None, isotope_2=None, data=None, errors=None):
        """Add relaxation data to the data nodes.

        @keyword sample_cond_list_id:       The sample conditions list ID number.
        @type sample_cond_list_id:          str
        @keyword sample_cond_list_label:    The sample conditions list label.
        @type sample_cond_list_label:       str
        @keyword temp_calibration:          The temperature calibration method.
        @type temp_calibration:             str
        @keyword temp_control:              The temperature control method.
        @type temp_control:                 str
        @keyword peak_intensity_type:       The peak intensity type - one of 'height' or 'volume'.
        @type peak_intensity_type:          str
        @keyword frq:                       The spectrometer proton frequency, in Hz.
        @type frq:                          float
        @keyword details:                   The details tag.
        @type details:                      None or str
        @keyword assembly_atom_ids:         The assembly atom ID numbers.
        @type assembly_atom_ids:            list of int
        @keyword entity_assembly_ids:       The entity assembly ID numbers.
        @type entity_assembly_ids:          list of int
        @keyword entity_ids:                The entity ID numbers.
        @type entity_ids:                   int
        @keyword res_nums:                  The residue number list.
        @type res_nums:                     list of int
        @keyword res_names:                 The residue name list.
        @type res_names:                    list of str
        @keyword atom_names:                The atom name list.
        @type atom_names:                   list of str
        @keyword atom_types:                The atom types as IUPAC element abbreviations.
        @type atom_types:                   list of str
        @keyword isotope:                   The isotope type list, ie 15 for '15N'.
        @type isotope:                      list of int
        @keyword assembly_atom_ids_2:       The assembly atom ID numbers.  This is for the second atom used in the heteronuclear NOE.
        @type assembly_atom_ids_2:          list of int
        @keyword entity_assembly_ids_2:     The entity assembly ID numbers.  This is for the second atom used in the heteronuclear NOE.
        @type entity_assembly_ids_2:        list of int
        @keyword entity_ids_2:              The entity ID numbers.  This is for the second atom used in the heteronuclear NOE.
        @type entity_ids_2:                 int
        @keyword res_nums_2:                The residue number list.  This is for the second atom used in the heteronuclear NOE.
        @type res_nums_2:                   list of int
        @keyword res_names_2:               The residue name list.  This is for the second atom used in the heteronuclear NOE.
        @type res_names_2:                  list of str
        @keyword atom_names_2:              The atom name list.  This is for the second atom used in the heteronuclear NOE.
        @type atom_names_2:                 list of str
        @keyword atom_types_2:              The atom types as IUPAC element abbreviations.  This is for the second atom used in the heteronuclear NOE.
        @type atom_types_2:                 list of str
        @keyword isotope_2:                 The isotope type list, ie 1 for '1H'.  This is for the second atom used in the heteronuclear NOE.
        @type isotope_2:                    list of int
        @keyword data:                      The relaxation data.
        @type data:                         list of float
        @keyword errors:                    The errors associated with the relaxation data.
        @type errors:                       list of float
        """

        # Check the args.
        if not temp_calibration:
            raise NameError("The temperature calibration method has not been specified.")
        if not temp_control:
            raise NameError("The temperature control method has not been specified.")
        if not peak_intensity_type:
            raise NameError("The peak intensity type has not been specified.")

        # Place the args into the namespace.
        self.temp_calibration = translate(temp_calibration)
        self.temp_control = translate(temp_control)
        self.peak_intensity_type = translate(peak_intensity_type)

        # Execute the base class add method.
        HeteronuclNOESaveframe.add(self,
                                   sample_cond_list_id=sample_cond_list_id,
                                   sample_cond_list_label=sample_cond_list_label,
                                   frq=frq,
                                   details=details,
                                   assembly_atom_ids=assembly_atom_ids,
                                   entity_assembly_ids=entity_assembly_ids,
                                   entity_ids=entity_ids,
                                   res_nums=res_nums,
                                   seq_id=seq_id,
                                   res_names=res_names,
                                   atom_names=atom_names,
                                   atom_types=atom_types,
                                   isotope=isotope,
                                   assembly_atom_ids_2=assembly_atom_ids_2,
                                   entity_assembly_ids_2=entity_assembly_ids_2,
                                   entity_ids_2=entity_ids_2,
                                   res_nums_2=res_nums_2,
                                   seq_id_2=seq_id_2,
                                   res_names_2=res_names_2,
                                   atom_names_2=atom_names_2,
                                   atom_types_2=atom_types_2,
                                   isotope_2=isotope_2,
                                   data=data,
                                   errors=errors)


    def add_tag_categories(self):
        """Create the v3.1 tag categories."""

        # The tag category objects.
        self.heteronuclRxlist = HeteronuclNOEList_v3_1(self)
        self.heteronuclRxexperiment = HeteronuclNOEExperiment_v3_1(self)
        self.heteronuclRxsoftware = HeteronuclNOESoftware_v3_1(self)
        self.Rx = HeteronuclNOE_v3_1(self)



class HeteronuclNOEList_v3_1(HeteronuclNOEList):
    """v3.1 HeteronuclNOEList tag category."""

    def __init__(self, sf):
        """Setup the HeteronuclNOEList_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclNOEList_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Heteronucl_NOE_list'

        # Database table names to class instance variables.
        self.data_to_var_name.append(['TempCalibrationMethod',      'temp_calibration'])
        self.data_to_var_name.append(['TempControlMethod',          'temp_control'])
        self.data_to_var_name.append(['HeteronuclearNOEValType',    'peak_intensity_type'])

        # Database table name to tag name.
        self.data_to_tag_name['SfCategory'] =               'Sf_category'
        self.data_to_tag_name['HeteronuclNOEListID'] =      'ID'
        self.data_to_tag_name['SampleConditionListLabel'] = 'Sample_condition_list_label'
        self.data_to_tag_name['TempCalibrationMethod'] =    'Temp_calibration_method'
        self.data_to_tag_name['TempControlMethod'] =        'Temp_control_method'
        self.data_to_tag_name['HeteronuclearNOEValType'] =  'Heteronuclear_NOE_val_type'



class HeteronuclNOEExperiment_v3_1(HeteronuclNOEExperiment):
    """v3.1 HeteronuclNOEExperiment tag category."""

    def __init__(self, sf):
        """Setup the HeteronuclNOEExperiment_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclNOEExperiment_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Heteronucl_NOE_experiment'



class HeteronuclNOESoftware_v3_1(HeteronuclNOESoftware):
    """v3.1 HeteronuclNOESoftware tag category."""

    def __init__(self, sf):
        """Setup the HeteronuclNOESoftware_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclNOESoftware_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Heteronucl_NOE_software'



class HeteronuclNOE_v3_1(HeteronuclNOE):
    """v3.1 HeteronuclNOE tag category."""

    def __init__(self, sf):
        """Setup the HeteronuclNOE_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclNOE_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Heteronucl_NOE'

        # Database table names to class instance variables.
        self.data_to_var_name = []
        self.data_to_var_name.append(['RxID',                'data_ids'])
        self.data_to_var_name.append(['AssemblyAtomID',      'assembly_atom_ids'])
        self.data_to_var_name.append(['EntityAssemblyID',    'entity_assembly_ids'])
        self.data_to_var_name.append(['EntityID',            'entity_ids'])
        self.data_to_var_name.append(['CompIndexID',         'res_nums'])
        self.data_to_var_name.append(['SeqID',               'seq_id'])
        self.data_to_var_name.append(['CompID',              'res_names'])
        self.data_to_var_name.append(['AtomID',              'atom_names'])
        self.data_to_var_name.append(['AtomType',            'atom_types'])
        self.data_to_var_name.append(['AtomIsotopeNumber',   'isotope'])
        self.data_to_var_name.append(['AssemblyAtomID2',     'assembly_atom_ids_2'])
        self.data_to_var_name.append(['EntityAssemblyID2',   'entity_assembly_ids_2'])
        self.data_to_var_name.append(['EntityID2',           'entity_ids_2'])
        self.data_to_var_name.append(['CompIndexID2',        'res_nums_2'])
        self.data_to_var_name.append(['SeqID2',              'seq_id_2'])
        self.data_to_var_name.append(['CompID2',             'res_names_2'])
        self.data_to_var_name.append(['AtomID2',             'atom_names_2'])
        self.data_to_var_name.append(['AtomType2',           'atom_types_2'])
        self.data_to_var_name.append(['AtomIsotopeNumber2',  'isotope_2'])
        self.data_to_var_name.append(['Val',                 'data'])
        self.data_to_var_name.append(['ValErr',              'errors'])
        self.data_to_var_name.append(['HeteronuclRxListID',  'rx_inc_list'])

        # Database table name to tag name.
        self.data_to_tag_name['RxID'] =                 'ID'
        self.data_to_tag_name['AssemblyAtomID'] =       'Assembly_atom_ID_1'
        self.data_to_tag_name['EntityAssemblyID'] =     'Entity_assembly_ID_1'
        self.data_to_tag_name['EntityID'] =             'Entity_ID_1'
        self.data_to_tag_name['CompIndexID'] =          'Comp_index_ID_1'
        self.data_to_tag_name['SeqID'] =                'Seq_ID_1'
        self.data_to_tag_name['CompID'] =               'Comp_ID_1'
        self.data_to_tag_name['AtomID'] =               'Atom_ID_1'
        self.data_to_tag_name['AtomType'] =             'Atom_type_1'
        self.data_to_tag_name['AtomIsotopeNumber'] =    'Atom_isotope_number_1'
        self.data_to_tag_name['AssemblyAtomID2'] =      'Assembly_atom_ID_2'
        self.data_to_tag_name['EntityAssemblyID2'] =    'Entity_assembly_ID_2'
        self.data_to_tag_name['EntityID2'] =            'Entity_ID_2'
        self.data_to_tag_name['CompIndexID2'] =         'Comp_index_ID_2'
        self.data_to_tag_name['SeqID2'] =               'Seq_ID_2'
        self.data_to_tag_name['CompID2'] =              'Comp_ID_2'
        self.data_to_tag_name['AtomID2'] =              'Atom_ID_2'
        self.data_to_tag_name['AtomType2'] =            'Atom_type_2'
        self.data_to_tag_name['AtomIsotopeNumber2'] =   'Atom_isotope_number_2'
        self.data_to_tag_name['Val'] =                  'Val'
        self.data_to_tag_name['ValErr'] =               'Val_err'
