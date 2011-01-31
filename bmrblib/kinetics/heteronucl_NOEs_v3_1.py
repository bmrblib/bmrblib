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
from bmrblib.kinetics.heteronucl_NOEs import HeteronuclNOESaveframe, HeteronuclNOEList, HeteronuclNOEExperiment, HeteronuclNOESoftware, HeteronuclNOE


class HeteronuclNOESaveframe_v3_1(HeteronuclNOESaveframe):
    """The v3.1 Heteronuclear NOE data saveframe class."""

    def add_tag_categories(self):
        """Create the v3.1 tag categories."""

        # The tag category objects.
        self.tag_categories.append(HeteronuclNOEList_v3_1(self))
        self.tag_categories.append(HeteronuclNOEExperiment_v3_1(self))
        self.tag_categories.append(HeteronuclNOESoftware_v3_1(self))
        self.tag_categories.append(HeteronuclNOE_v3_1(self))



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

        # Add the tag info.
        self.add(key='TempCalibrationMethod',       tag_name='Temp_calibration_method',     var_name='temp_calibration',    missing=False)
        self.add(key='TempControlMethod',           tag_name='Temp_control_method',         var_name='temp_control',        missing=False)
        self.add(key='HeteronuclearNOEValType',     tag_name='Heteronuclear_NOE_val_type',  var_name='peak_intensity_type', missing=False)

        # Change tag names.
        self['SfCategory'].tag_name = 'Sf_category'
        self['SfFramecode'].tag_name = 'Sf_framecode'
        self['SampleConditionListLabel'].tag_name = 'Sample_condition_list_label'



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

        # Add the tag info.
        self.add(key='RxID',                tag_name='ID',                      var_name='data_ids',            format='int')
        self.add(key='AssemblyAtomID',      tag_name='Assembly_atom_ID_1',      var_name='assembly_atom_ids')
        self.add(key='EntityAssemblyID',    tag_name='Entity_assembly_ID_1',    var_name='entity_assembly_ids')
        self.add(key='EntityID',            tag_name='Entity_ID_1',             var_name='entity_ids',          format='int',   missing=False)
        self.add(key='CompIndexID',         tag_name='Comp_index_ID_1',         var_name='res_nums',            format='int',   missing=False)
        self.add(key='SeqID',               tag_name='Seq_ID_1',                var_name='seq_id')
        self.add(key='CompID',              tag_name='Comp_ID_1',               var_name='res_names',           missing=False)
        self.add(key='AtomID',              tag_name='Atom_ID_1',               var_name='atom_names',          missing=False)
        self.add(key='AtomType',            tag_name='Atom_type_1',             var_name='atom_types')
        self.add(key='AtomIsotopeNumber',   tag_name='Atom_isotope_number_1',   var_name='isotope',             format='int')
        self.add(key='AssemblyAtomID2',     tag_name='Assembly_atom_ID_2',      var_name='assembly_atom_ids_2')
        self.add(key='EntityAssemblyID2',   tag_name='Entity_assembly_ID_2',    var_name='entity_assembly_ids_2')
        self.add(key='EntityID2',           tag_name='Entity_ID_2',             var_name='entity_ids_2',        format='int')
        self.add(key='CompIndexID2',        tag_name='Comp_index_ID_2',         var_name='res_nums_2',          format='int')
        self.add(key='SeqID2',              tag_name='Seq_ID_2',                var_name='seq_id_2')
        self.add(key='CompID2',             tag_name='Comp_ID_2',               var_name='res_names_2')
        self.add(key='AtomID2',             tag_name='Atom_ID_2',               var_name='atom_names_2')
        self.add(key='AtomType2',           tag_name='Atom_type_2',             var_name='atom_types_2')
        self.add(key='AtomIsotopeNumber2',  tag_name='Atom_isotope_number_2',   var_name='isotope_2',           format='int')
        self.add(key='Val',                 tag_name='Val',                     var_name='data',                format='float')
        self.add(key='ValErr',              tag_name='Val_err',                 var_name='errors',              format='float')
        self.add(key='HeteronuclNOEListID', tag_name='Heteronucl_NOE_list_ID',  var_name='count_str')
