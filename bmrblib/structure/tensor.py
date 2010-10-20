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
"""The tensor saveframe category.

For example, see http://www.bmrb.wisc.edu/dictionary/3.1html_frame/frame_SaveFramePage.html#tensor
"""

# relax module imports.
from bmrblib.base_classes import BaseSaveframe, TagCategory, TagCategoryFree
from bmrblib.misc import no_missing, translate
from bmrblib.pystarlib.SaveFrame import SaveFrame
from bmrblib.pystarlib.TagTable import TagTable


class TensorSaveframe(BaseSaveframe):
    """The tensor saveframe class."""

    # Saveframe variables.
    sf_label = 'tensor'

    def __init__(self, datanodes):
        """Initialise the class, placing the pystarlib data nodes into the namespace.

        @param datanodes:   The pystarlib data nodes object.
        @type datanodes:    list
        """

        # Place the data nodes into the namespace.
        self.datanodes = datanodes

        # The number of Tensor saveframes.
        self.tensor_inc = 0

        # Add the specific tag category objects.
        self.add_tag_categories()


    def add(self, data_file_name=None, sample_cond_list_id=None, sample_cond_list_label='$conditions_1', details=None, assembly_atom_ids=None, entity_assembly_ids=None, entity_ids=None, res_nums=None, seq_id=None, res_names=None, atom_names=None, atom_types=None, isotope=None, data=None, errors=None):
        """Add relaxation data to the data nodes.

        @keyword data_file_name:            The name of the data file submitted with the deposition containing this data (should probably be left to None).
        @type data_file_name:               None or str
        @keyword sample_cond_list_id:       The sample conditions list ID number.
        @type sample_cond_list_id:          str
        @keyword sample_cond_list_label:    The sample conditions list label.
        @type sample_cond_list_label:       str
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
        """

        # Check the ID info.
        no_missing(entity_ids, 'entity ID numbers')
        no_missing(res_nums, 'residue numbers')
        no_missing(res_names, 'residue names')
        no_missing(atom_names, 'atom names')

        # The number of elements.
        N = len(res_nums)

        # Place the args into the namespace.
        self.file_name = translate(data_file_name)
        self.sample_conditions_label = translate(sample_cond_list_label)
        self.details = translate(details)
        self.res_nums = translate(res_nums)
        self.res_names = translate(res_names)
        self.atom_names = translate(atom_names)
        self.atom_types = translate(atom_types)
        self.isotope = translate(isotope)
        self.data = translate(data)

        # Convert to lists and check the lengths.
        for name in ['assembly_atom_ids', 'entity_assembly_ids', 'entity_ids', 'res_nums', 'seq_id', 'res_names', 'atom_names', 'atom_types', 'isotope']:
            # Get the object.
            obj = locals()[name]

            # None objects.
            if obj == None:
                obj = [None] * N

            # Check the length.
            if len(obj) != N:
                raise NameError("The number of elements in the '%s' arg does not match that of 'res_nums'." % name)

            # Place the args into the namespace, translating for BMRB.
            setattr(self, name, translate(obj))

        # Set up the tensor specific variables.
        self.tensor_inc = self.tensor_inc + 1
        self.tensor_inc_str = str(self.tensor_inc)
        self.tensor_inc_list = translate([self.tensor_inc] * N)
        self.generate_data_ids(N)

        # Set up the version specific variables.
        self.specific_setup()

        # Initialise the save frame.
        self.frame = SaveFrame(title=self.sf_label)

        # Create the tag categories.
        self.Tensor_list.create()
        self.Tensor.create()

        # Add the saveframe to the data nodes.
        self.datanodes.append(self.frame)


    def add_tag_categories(self):
        """Create the tag categories."""

        # The tag category objects.
        self.Tensor_list = TensorList(self)
        self.Tensor = Tensor(self)


    def loop(self):
        """Loop over the tensor saveframes, yielding the data.

        @return:    The tensor data consisting of the proton frequency, residue numbers, residue
                    names, atom names, values, and errors.
        @rtype:     tuple of float, list of int, list of str, list of str, list of float, list of
                    float
        """

        # Set up the tag information.
        self.Tensor_list.tag_setup()
        self.Tensor.tag_setup()

        # Set up the version specific variables.
        self.specific_setup()

        # Get the saveframe name.
        sf_name = getattr(self, 'cat_name')[0]

        # Loop over all datanodes.
        for datanode in self.datanodes:
            # Find the tensor saveframes via the SfCategory tag index.
            found = False
            for index in range(len(datanode.tagtables[0].tagnames)):
                # First match the tag names.
                if datanode.tagtables[0].tagnames[index] == self.Tensor_list.data_to_tag_name_full['SfCategory']:
                    # Then the tag value.
                    if datanode.tagtables[0].tagvalues[index][0] == sf_name:
                        found = True
                        break

            # Skip the datanode.
            if not found:
                continue

            # Get the tensor info.
            res_nums, res_names, atom_names, values = self.Tensor.read(datanode.tagtables[1])

            # Yield the data.
            yield res_nums, res_names, atom_names, values


    def specific_setup(self):
        """Method called by self.add() to set up any version specific data."""

        self.cat_name = ['tensor']



class TensorList(TagCategoryFree):
    """Base class for the TensorList tag category."""

    def __init__(self, sf):
        """Setup the TensorList tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(TensorList, self).__init__(sf)

        # The category name.
        self.tag_category_label='Tensor_list'

        # Database table names to class instance variables.
        self.data_to_var_name.append(['TensorID',                    'data_ids'])
        self.data_to_var_name.append(['SampleConditionListLabel',    'sample_conditions_label'])
        self.data_to_var_name.append(['DataFileName',                'file_name'])
        self.data_to_var_name.append(['Details',                     'details'])

        # Database table name to tag name.
        self.data_to_tag_name['SfCategory'] =               'Sf_category'
        self.data_to_tag_name['SfFramecode'] =              'Sf_framecode'
        self.data_to_tag_name['EntryID'] =                  'Entry_ID'
        self.data_to_tag_name['SfID'] =                     'Sf_ID'
        self.data_to_tag_name['TensorID'] =                 'ID'
        self.data_to_tag_name['SampleConditionListLabel'] = 'Sample_conditions_label'
        self.data_to_tag_name['DataFileName'] =             'Data_file_name'
        self.data_to_tag_name['Details'] =                  'Details'



class Tensor(TagCategory):
    """Base class for the Tensor tag category."""

    def __init__(self, sf):
        """Setup the Tensor tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(Tensor, self).__init__(sf)

        # The category name.
        self.tag_category_label='Tensor'

        # Database table names to class instance variables.
        self.data_to_var_name.append(['TensorID',                'data_ids'])
        self.data_to_var_name.append(['AssemblyAtomID',          'assembly_atom_ids'])
        self.data_to_var_name.append(['EntityAssemblyID',        'entity_assembly_ids'])
        self.data_to_var_name.append(['EntityID',                'entity_ids'])
        self.data_to_var_name.append(['CompIndexID',             'res_nums'])
        self.data_to_var_name.append(['CompID',                  'res_names'])
        self.data_to_var_name.append(['AtomID',                  'atom_names'])
        self.data_to_var_name.append(['AtomType',                'atom_types'])
        self.data_to_var_name.append(['AtomIsotopeNumber',       'isotope'])
        self.data_to_var_name.append(['Val',                     'data'])
        self.data_to_var_name.append(['TensorListID',            'tensor_inc_list'])

        # Database table name to tag name.
        self.data_to_tag_name['TensorID'] =             'ID'
        self.data_to_tag_name['AssemblyAtomID'] =       'Assembly_atom_ID'
        self.data_to_tag_name['EntityAssemblyID'] =     'Entity_assembly_ID'
        self.data_to_tag_name['EntityID'] =             'Entity_ID'
        self.data_to_tag_name['CompIndexID'] =          'Comp_index_ID'
        self.data_to_tag_name['CompID'] =               'Residue_label'
        self.data_to_tag_name['AtomID'] =               'Atom_name'
        self.data_to_tag_name['AtomType'] =             'Atom_type'
        self.data_to_tag_name['AtomIsotopeNumber'] =    'Atom_isotope_number'
        self.data_to_tag_name['Val'] =                  'value'
        self.data_to_tag_name['TensorListID'] =         'Tensor_list_ID'


    def read(self, tagtable):
        """Extract the Tensor tag category info.

        @param tagtable:    The Tensor tagtable.
        @type tagtable:     Tagtable instance
        @return:            The residue numbers, residue names, atom names, and values.
        @rtype:             tuple of list of int, list of str, list of str, list of float, list of
                            float
        """

        # The entity info.
        res_nums = tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name_full['CompIndexID'])]
        res_names = tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name_full['CompID'])]
        atom_names = tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name_full['AtomID'])]
        values = tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name_full['Val'])]

        # Convert the residue numbers to ints and the values to floats.
        for i in range(len(res_nums)):
            res_nums[i] = int(res_nums[i])
            values[i] = float(values[i])

        # Return the data.
        return res_nums, res_names, atom_names, values
