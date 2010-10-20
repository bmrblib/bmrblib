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
"""The Heteronuclear T1 data saveframe category.

For example, see http://www.bmrb.wisc.edu/dictionary/3.1html/SaveFramePage.html#heteronucl_T1_relaxation.
"""

# relax module imports.
from bmrblib.base_classes import TagCategory
from bmrblib.misc import no_missing, translate
from bmrblib.kinetics.relax_base import HeteronuclRxList, RelaxSaveframe, Rx
from bmrblib.pystarlib.SaveFrame import SaveFrame
from bmrblib.pystarlib.TagTable import TagTable


class HeteronuclT1Saveframe(RelaxSaveframe):
    """The Heteronuclear T1 data saveframe class."""

    # Saveframe variables.
    name = 'T1'


    def __init__(self, datanodes):
        """Initialise the class, placing the pystarlib data nodes into the namespace.

        @param datanodes:   The pystarlib data nodes object.
        @type datanodes:    list
        """

        # Place the data nodes into the namespace.
        self.datanodes = datanodes

        # The number of relaxation data sets.
        self.r1_inc = 0

        # Add the specific tag category objects.
        self.add_tag_categories()


    def add(self, sample_cond_list_id=None, sample_cond_list_label='$conditions_1', frq=None, details=None, assembly_atom_ids=None, entity_assembly_ids=None, entity_ids=None, res_nums=None, seq_id=None, res_names=None, atom_names=None, atom_types=None, isotope=None, data=None, errors=None):
        """Add relaxation data to the data nodes.

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
        @keyword data:                      The relaxation data.
        @type data:                         list of float
        @keyword errors:                    The errors associated with the relaxation data.
        @type errors:                       list of float
        """

        # Check the ID info.
        no_missing(entity_ids, 'entity ID numbers of the ' + repr(int(frq*1e-6)) + ' MHz R1 data')
        no_missing(res_nums, 'residue numbers of the ' + repr(int(frq*1e-6)) + ' MHz R1 data')
        no_missing(res_names, 'residue names of the ' + repr(int(frq*1e-6)) + ' MHz R1 data')
        no_missing(atom_names, 'atom names of the ' + repr(int(frq*1e-6)) + ' MHz R1 data')

        # The number of elements.
        self.N = len(res_nums)

        # Place the args into the namespace.
        self.sample_cond_list_id = translate(sample_cond_list_id)
        self.sample_cond_list_label = translate(sample_cond_list_label)
        self.frq = frq
        self.details = translate(details)

        # Convert to lists and check the lengths.
        for name in ['assembly_atom_ids', 'entity_assembly_ids', 'entity_ids', 'res_nums', 'seq_id', 'res_names', 'atom_names', 'atom_types', 'isotope', 'data', 'errors']:
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

        # Set up the R1 specific variables.
        self.r1_inc = self.r1_inc + 1
        self.rx_inc_list = translate([self.r1_inc] * self.N)
        self.generate_data_ids(self.N)

        # Set up the version specific variables.
        self.specific_setup()

        # Initialise the save frame.
        self.frame = SaveFrame(title='heteronuclear_'+self.label+'_list_'+repr(self.r1_inc))

        # Create the tag categories.
        self.heteronuclRxlist.create()
        self.heteronuclRxexperiment.create()
        self.heteronuclRxsoftware.create()
        self.Rx.create()

        # Add the saveframe to the data nodes.
        self.datanodes.append(self.frame)


    def add_tag_categories(self):
        """Create the tag categories."""

        # The tag category objects.
        self.heteronuclRxlist = HeteronuclT1List(self)
        self.heteronuclRxexperiment = HeteronuclT1Experiment(self)
        self.heteronuclRxsoftware = HeteronuclT1Software(self)
        self.Rx = T1(self)



class HeteronuclT1List(HeteronuclRxList):
    """Base class for the HeteronuclT1List tag category."""

    def __init__(self, sf):
        """Setup the HeteronuclT1List tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclT1List, self).__init__(sf)

        # Database table names to class instance variables.
        self.data_to_var_name.append(['HeteronuclT1ListID',         'r1_inc'])
        self.data_to_var_name.append(['SampleConditionListID',      'sample_cond_list_id'])
        self.data_to_var_name.append(['SampleConditionListLabel',   'conditions'])
        self.data_to_var_name.append(['SpectrometerFrequency1H',    'frq'])
        self.data_to_var_name.append(['T1CoherenceType',            'coherence'])
        self.data_to_var_name.append(['T1ValUnits',                 '1/s'])
        self.data_to_var_name.append(['Details',                    'details'])

        # Database table name to tag name.
        self.data_to_tag_name['SfCategory'] =               'Saveframe_category'
        self.data_to_tag_name['SampleConditionListID'] =    'Sample_condition_list_ID'
        self.data_to_tag_name['SampleConditionListLabel'] = 'Sample_conditions_label'
        self.data_to_tag_name['SpectrometerFrequency1H'] =  'Spectrometer_frequency_1H'
        self.data_to_tag_name['T1CoherenceType'] =          'T1_coherence_type'
        self.data_to_tag_name['T1ValUnits'] =               'T1_value_units'
        self.data_to_tag_name['Details'] =                  'Details'

        # Class variables.
        self.variables['coherence'] = 'Nz'



class HeteronuclT1Experiment(TagCategory):
    """Base class for the HeteronuclT1Experiment tag category."""

    def __init__(self, sf):
        """Setup the HeteronuclT1Experiment tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclT1Experiment, self).__init__(sf)

        # Database table names to class instance variables.
        self.data_to_var_name.append(['SampleLabel', 'sample'])

        # Database table name to tag name.
        self.data_to_tag_name['SampleLabel'] = 'Sample_label'



class HeteronuclT1Software(TagCategory):
    """Base class for the HeteronuclT1Software tag category."""



class T1(Rx):
    """Base class for the T1 tag category."""

