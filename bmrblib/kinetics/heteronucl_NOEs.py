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
"""The Heteronuclear NOE data saveframe category.

For example, see http://www.bmrb.wisc.edu/dictionary/3.1html/SaveFramePage.html#heteronucl_NOEs.
"""

# relax module imports.
from bmrblib.base_classes import TagCategory
from bmrblib.misc import no_missing, translate
from bmrblib.kinetics.relax_base import HeteronuclRxList, RelaxSaveframe, Rx
from bmrblib.pystarlib.SaveFrame import SaveFrame
from bmrblib.pystarlib.TagTable import TagTable


class HeteronuclNOESaveframe(RelaxSaveframe):
    """The Heteronuclear NOE data saveframe class."""

    # Saveframe variables.
    name = 'NOE'
    sf_label = 'heteronucl_NOEs'


    def __init__(self, datanodes):
        """Initialise the class, placing the pystarlib data nodes into the namespace.

        @param datanodes:   The pystarlib data nodes object.
        @type datanodes:    list
        """

        # Place the data nodes into the namespace.
        self.datanodes = datanodes

        # The number of relaxation data sets.
        self.noe_inc = 0

        # Add the specific tag category objects.
        self.add_tag_categories()


    def add(self, sample_label='$sample_1', sample_cond_list_id=None, sample_cond_list_label='$conditions_1', frq=None, details=None, assembly_atom_ids=None, entity_assembly_ids=None, entity_ids=None, res_nums=None, seq_id=None, res_names=None, atom_names=None, atom_types=None, isotope=None, assembly_atom_ids_2=None, entity_assembly_ids_2=None, entity_ids_2=None, res_nums_2=None, seq_id_2=None, res_names_2=None, atom_names_2=None, atom_types_2=None, isotope_2=None, data=None, errors=None):
        """Add relaxation data to the data nodes.

        @keyword sample_label:              The sample label.
        @type sample_label:                 str
        @keyword sample_cond_list_id:       The sample conditions list ID number.
        @type sample_cond_list_id:          str
        @keyword sample_cond_list_label:    The sample conditions list label.
        @type sample_cond_list_label:       str
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

        # Check the ID info.
        no_missing(entity_ids, 'entity ID numbers of the ' + repr(int(frq*1e-6)) + ' MHz NOE data')
        no_missing(res_nums, 'residue numbers of the ' + repr(int(frq*1e-6)) + ' MHz NOE data')
        no_missing(res_names, 'residue names of the ' + repr(int(frq*1e-6)) + ' MHz NOE data')
        no_missing(atom_names, 'atom names of the ' + repr(int(frq*1e-6)) + ' MHz NOE data')

        # The number of elements.
        self.N = len(res_nums)

        # Place the args into the namespace.
        self.sample_label = sample_label
        self.sample_cond_list_id = translate(sample_cond_list_id)
        self.sample_cond_list_label = translate(sample_cond_list_label)
        self.frq = translate(frq / 1e6)
        self.details = translate(details)

        # Convert to lists and check the lengths.
        for name in ['assembly_atom_ids', 'entity_assembly_ids', 'entity_ids', 'res_nums', 'seq_id', 'res_names', 'atom_names', 'atom_types', 'isotope', 'assembly_atom_ids_2', 'entity_assembly_ids_2', 'entity_ids_2', 'res_nums_2', 'seq_id_2', 'res_names_2', 'atom_names_2', 'atom_types_2', 'isotope_2', 'data', 'errors']:
            # Get the object.
            obj = locals()[name]

            # None objects.
            if obj == None:
                obj = [None] * self.N

            # Check the length.
            if len(obj) != self.N:
                raise NameError("The number of elements in the '%s' arg does not match that of 'res_nums'." % name)

            # Place the args into the namespace, translating for BMRB.
            setattr(self, name, translate(obj))

        # Set up the NOE specific variables.
        self.noe_inc = self.noe_inc + 1
        self.noe_inc_str = str(self.noe_inc)
        self.rx_inc_list = translate([self.noe_inc] * self.N)
        #self.generate_data_ids(self.N)

        # The label.
        self.label = 'heteronuclear NOE ' + repr(self.noe_inc)

        # Initialise the save frame.
        self.frame = SaveFrame(title='heteronuclear_NOEs')

        # Create the tag categories.
        self.heteronuclRxlist.create()
        self.heteronuclRxexperiment.create()
        #self.heteronuclRxsoftware.create()
        self.Rx.create()

        # Add the saveframe to the data nodes.
        self.datanodes.append(self.frame)


    def add_tag_categories(self):
        """Create the tag categories."""

        # The tag category objects.
        self.heteronuclRxlist = HeteronuclNOEList(self)
        self.heteronuclRxexperiment = HeteronuclNOEExperiment(self)
        self.heteronuclRxsoftware = HeteronuclNOESoftware(self)
        self.Rx = HeteronuclNOE(self)



class HeteronuclNOEList(HeteronuclRxList):
    """Base class for the HeteronuclNOEList tag category."""

    def __init__(self, sf):
        """Setup the HeteronuclNOEList tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclNOEList, self).__init__(sf)

        # Database table names to class instance variables.
        self.data_to_var_name.append(['SfFramecode',                'label'])
        self.data_to_var_name.append(['HeteronuclNOEListID',        'noe_inc_str'])
        self.data_to_var_name.append(['SampleConditionListID',      'sample_cond_list_id'])
        self.data_to_var_name.append(['SampleConditionListLabel',   'sample_cond_list_label'])
        self.data_to_var_name.append(['SpectrometerFrequency1H',    'frq'])
        self.data_to_var_name.append(['Details',                    'details'])

        # Database table name to tag name.
        self.data_to_tag_name['SfCategory'] =               'Saveframe_category'
        self.data_to_tag_name['SfFramecode'] =              'Sf_framecode'
        self.data_to_tag_name['SampleConditionListID'] =    'Sample_condition_list_ID'
        self.data_to_tag_name['SampleConditionListLabel'] = 'Sample_conditions_label'
        self.data_to_tag_name['SpectrometerFrequency1H'] =  'Spectrometer_frequency_1H'
        self.data_to_tag_name['Details'] =                  'Details'



class HeteronuclNOEExperiment(TagCategory):
    """Base class for the HeteronuclNOEExperiment tag category."""

    def __init__(self, sf):
        """Setup the HeteronuclNOEExperiment tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclNOEExperiment, self).__init__(sf)

        # Database table names to class instance variables.
        self.data_to_var_name.append(['SampleLabel', 'sample_label'])

        # Database table name to tag name.
        self.data_to_tag_name['SampleLabel'] = 'Sample_label'



class HeteronuclNOESoftware(TagCategory):
    """Base class for the HeteronuclNOESoftware tag category."""



class HeteronuclNOE(Rx):
    """Base class for the HeteronuclNOE tag category."""
