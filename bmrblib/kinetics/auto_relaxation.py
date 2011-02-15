#############################################################################
#                                                                           #
# The BMRB library.                                                         #
#                                                                           #
# Copyright (C) 2009-2011 Edward d'Auvergne                                 #
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
"""The Auto relaxation data saveframe category.

For example, see http://www.bmrb.wisc.edu/dictionary/3.1html/SaveFramePage.html#auto_relaxation.
"""

# relax module imports.
from bmrblib.base_classes import BaseSaveframe, TagCategory, TagCategoryFree


class AutoRelaxationSaveframe(BaseSaveframe):
    """The Auto relaxation data saveframe class."""

    # Class variables.
    name = 'auto'
    sf_label = 'auto_relaxation'

    def add_tag_categories(self):
        """Create the tag categories."""

        # The tag category objects.
        self.tag_categories.append(AutoRelaxationList(self))
        self.tag_categories.append(AutoRelaxationExperiment(self))
        self.tag_categories.append(AutoRelaxationSoftware(self))
        self.tag_categories.append(AutoRelaxation(self))


    def pre_ops(self):
        """Perform some saveframe specific operations prior to XML creation."""

        # The operators of the relaxation superoperator.
        if self.data_type == 'R1':
            self.coherence = 'Iz'
            self.coherence_common_name = 'R1'
        elif self.data_type == 'R2':
            self.coherence = 'I+'
            self.coherence_common_name = 'R2'
        else:
            raise NameError("The data type '%s' is not one of ['R1', 'R2']." % data_type)

        # The saveframe description.
        self.sf_framecode = '%s MHz %s relaxation %s' % (self.frq, self.data_type, self.count)


class AutoRelaxationList(TagCategoryFree):
    """Base class for the AutoRelaxationList tag category."""

    def __init__(self, sf):
        """Setup the AutoRelaxationList tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(AutoRelaxationList, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Auto_relaxation_list'

        # Add the tag info.
        self.add(key='EntryID',                  tag_name='Entry_ID',                    var_name='entry_id',               format='str')
        self.add(key='AutoRelaxationListID',     tag_name='ID',                          var_name='count_str',              format='int')
        self.add(key='DataFileName',             tag_name='Data_file_name',              var_name='data_file_name',         format='str')
        self.add(key='SampleConditionListID',    tag_name='Sample_condition_list_ID',    var_name='sample_cond_list_id',    format='int')
        self.add(key='SampleConditionListLabel', tag_name='Sample_condition_list_label', var_name='sample_cond_list_label', format='str',   default='$conditions_1')
        self.add(key='TempCalibrationMethod',    tag_name='Temp_calibration_method',     var_name='temp_calibration',       format='str',   missing=False)
        self.add(key='TempControlMethod',        tag_name='Temp_control_method',         var_name='temp_control',           format='str',   missing=False)
        self.add(key='SpectrometerFrequency1H',  tag_name='Spectrometer_frequency_1H',   var_name='frq',                    format='float')
        self.add(key='CommonRelaxationTypeName', tag_name='Common_relaxation_type_name', var_name='coherence_common_name',  format='str')
        self.add(key='RelaxationCoherenceType',  tag_name='Relaxation_coherence_type',   var_name='coherence',              format='str')
        self.add(key='RelaxationValUnits',       tag_name='Relaxation_val_units',        var_name='units',                  format='str',   default='s-1')
        self.add(key='RelaxationValType',        tag_name='Relaxation_val_type',         var_name='peak_intensity_type',    format='str',   missing=False)
        self.add(key='RexUnits',                 tag_name='Rex_units',                   var_name='rex_units',              format='str')
        self.add(key='Details',                  tag_name='Details',                     var_name='details',                format='str')
        self.add(key='TextDataFormat',           tag_name='Text_data_format',            var_name='text_data_format',       format='str')
        self.add(key='TextData',                 tag_name='Text_data',                   var_name='text_data',              format='str')

        # Change tag names.
        self['SfCategory'].tag_name = 'Sf_category'
        self['SfFramecode'].tag_name = 'Sf_framecode'


class AutoRelaxationExperiment(TagCategory):
    """Base class for the AutoRelaxationExperiment tag category."""

    def __init__(self, sf):
        """Setup the AutoRelaxationExperiment tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(AutoRelaxationExperiment, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Auto_relaxation_experiment'

        # Add the tag info.
        self.add(key='ExperimentID',       tag_name='Experiment_ID',           var_name='experiment_id',           format='int')
        self.add(key='ExperimentName',     tag_name='Experiment_name',         var_name='experiment_name',         format='str')
        self.add(key='SampleID',           tag_name='Sample_ID',               var_name='sample_id',               format='int')
        self.add(key='SampleLabel',        tag_name='Sample_label',            var_name='sample_label',            format='str', default='$sample_1')
        self.add(key='SampleState',        tag_name='Sample_state',            var_name='sample_state',            format='str')
        self.add(key='EntryID',            tag_name='Entry_ID',                var_name='entry_id',                format='str')
        self.add(key='HeteronuclT1ListID', tag_name='Auto_relaxation_list_ID', var_name='heteronucl_t1_list_id',   format='int')



class AutoRelaxationSoftware(TagCategory):
    """Base class for the AutoRelaxationSoftware tag category."""

    def __init__(self, sf):
        """Setup the AutoRelaxationSoftware tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(AutoRelaxationSoftware, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Auto_relaxation_software'

        # Add the tag info.
        self.add(key='SoftwareID',           tag_name='Software_ID',             var_name='software_id',           format='int')
        self.add(key='SoftwareLabel',        tag_name='Software_label',          var_name='software_label',        format='str')
        self.add(key='MethodID',             tag_name='Method_ID',               var_name='method_id',             format='int')
        self.add(key='MethodLabel',          tag_name='Method_label',            var_name='method_label',          format='str')
        self.add(key='EntryID',              tag_name='Entry_ID',                var_name='entry_id',              format='str')
        self.add(key='AutoRelaxationListID', tag_name='Auto_relaxation_list_ID', var_name='heteronucl_t1_list_id', format='int')



class AutoRelaxation(TagCategory):
    """Base class for the AutoRelaxation tag category."""

    def __init__(self, sf):
        """Setup the AutoRelaxation tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(AutoRelaxation, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Auto_relaxation'

        # Add the tag info.
        self.add(key='AutoRelaxationID',     tag_name='ID',                      var_name='data_ids',                format='int')
        self.add(key='AssemblyID',           tag_name='Assembly_ID',             var_name='assembly_ids',            format='int')
        self.add(key='AssemblyAtomID',       tag_name='Assembly_atom_ID',        var_name='assembly_atom_ids',       format='int')
        self.add(key='EntityAssemblyID',     tag_name='Entity_assembly_ID',      var_name='entity_assembly_ids',     format='int')
        self.add(key='EntityID',             tag_name='Entity_ID',               var_name='entity_ids',              format='int',  missing=False)
        self.add(key='CompIndexID',          tag_name='Comp_index_ID',           var_name='res_nums',                format='int',  missing=False)
        self.add(key='SeqID',                tag_name='Seq_ID',                  var_name='seq_id',                  format='int')
        self.add(key='CompID',               tag_name='Comp_ID',                 var_name='res_names',               format='str',  missing=False)
        self.add(key='AtomID',               tag_name='Atom_ID',                 var_name='atom_names',              format='str',  missing=False)
        self.add(key='AtomType',             tag_name='Atom_type',               var_name='atom_types',              format='str')
        self.add(key='AtomIsotopeNumber',    tag_name='Atom_isotope_number',     var_name='isotope',                 format='int')
        self.add(key='Val',                  tag_name='Auto_relaxation_val',     var_name='data',                    format='float')
        self.add(key='ValErr',               tag_name='Auto_relaxation_val_err', var_name='errors',                  format='float')
        self.add(key='RexVal',               tag_name='Rex_val',                 var_name='rex_val',                 format='float')
        self.add(key='RexErr',               tag_name='Rex_err',                 var_name='rex_err',                 format='float')
        self.add(key='ResonanceID',          tag_name='Resonance_ID',            var_name='resonance_id',            format='int')
        self.add(key='AuthEntityAssemblyID', tag_name='Auth_entity_assembly_ID', var_name='auth_entity_assembly_id', format='str')
        self.add(key='AuthSeqID',            tag_name='Auth_seq_ID',             var_name='auth_seq_id',             format='str')
        self.add(key='AuthCompID',           tag_name='Auth_comp_ID',            var_name='auth_atom_id',            format='str')
        self.add(key='AuthAtomID',           tag_name='Auth_atom_ID',            var_name='auth_atom_id',            format='str')
        self.add(key='EntryID',              tag_name='Entry_ID',                var_name='entry_id',                format='str')
        self.add(key='AutoRelaxationListID', tag_name='Auto_relaxation_list_ID', var_name='count_str',               format='int')
