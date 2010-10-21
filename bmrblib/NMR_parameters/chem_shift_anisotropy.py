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
"""The chemical shift anisotropy data saveframe category.

For example, see http://www.bmrb.wisc.edu/dictionary/3.1html_frame/frame_SaveFramePage.html#chem_shift_anisotropy
"""

# relax module imports.
from bmrblib.base_classes import BaseSaveframe, TagCategory, TagCategoryFree
from bmrblib.misc import no_missing, translate
from bmrblib.pystarlib.SaveFrame import SaveFrame
from bmrblib.pystarlib.TagTable import TagTable


class ChemShiftAnisotropySaveframe(BaseSaveframe):
    """The chemical shift anisotropy data saveframe class."""

    # Class variables.
    label = 'Chem_shift_anisotropy'
    sf_label = 'chem_shift_anisotropy'
    id = '1'

    def __init__(self, datanodes):
        """Initialise the class, placing the pystarlib data nodes into the namespace.

        @param datanodes:   The pystarlib data nodes object.
        @type datanodes:    list
        """

        # Place the data nodes into the namespace.
        self.datanodes = datanodes

        # The number of CSA data sets.
        self.csa_inc = 0

        # Add the specific tag category objects.
        self.add_tag_categories()


    def add(self, data_file_name=None, sample_label='$sample_1', sample_cond_list_id=None, sample_cond_list_label='$conditions_1', frq=None, details=None, assembly_atom_ids=None, entity_assembly_ids=None, entity_ids=None, res_nums=None, seq_id=None, res_names=None, atom_names=None, atom_types=None, isotope=None, csa=None, csa_error=None, units='ppm'):
        """Add relaxation data to the data nodes.

        @keyword data_file_name:            The name of the data file submitted with the deposition containing this data (should probably be left to None).
        @type data_file_name:               None or str
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
        @keyword csa:                       The CSA values in ppm.
        @type csa:                          list of float
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
        self.sample_label = sample_label
        self.sample_cond_list_label = sample_cond_list_label
        self.frq = frq
        self.units = units
        self.res_nums = translate(res_nums)
        self.res_names = translate(res_names)
        self.atom_names = translate(atom_names)
        self.atom_types = translate(atom_types)
        self.isotope = translate(isotope)
        self.csa = translate(csa)

        # Convert to lists and check the lengths.
        for name in ['assembly_atom_ids', 'entity_assembly_ids', 'entity_ids', 'res_nums', 'seq_id', 'res_names', 'atom_names', 'atom_types', 'isotope', 'csa', 'csa_error']:
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

        # Set up the CSA specific variables.
        self.csa_inc = self.csa_inc + 1
        self.csa_inc_list = translate([self.csa_inc] * N)
        #self.generate_data_ids(N)

        # Initialise the save frame.
        self.frame = SaveFrame(title='chem_shift_anisotropy')

        # Create the tag categories.
        self.Chem_shift_anisotropy.create()
        self.CS_anisotropy_experiment.create()
        #self.CS_anisotropy_software.create()
        self.CS_anisotropy.create()

        # Add the saveframe to the data nodes.
        self.datanodes.append(self.frame)


    def add_tag_categories(self):
        """Create the tag categories."""

        # The tag category objects.
        self.Chem_shift_anisotropy = ChemShiftAnisotropy(self)
        self.CS_anisotropy_experiment = CSAnisotropyExperiment(self)
        self.CS_anisotropy_software = CSAnisotropySoftware(self)
        self.CS_anisotropy = CSAnisotropy(self)


    def loop(self):
        """Loop over the CSA saveframes, yielding the relaxation data.

        @return:    The relaxation data consisting of the proton frequency, residue numbers, residue
                    names, atom names, values, and errors.
        @rtype:     tuple of float, list of int, list of str, list of str, list of float, list of
                    float
        """

        # Set up the tag information.
        self.Chem_shift_anisotropy.tag_setup()
        self.CS_anisotropy_experiment.tag_setup()
        self.CS_anisotropy_software.tag_setup()
        self.CS_anisotropy.tag_setup()

        # Get the saveframe name.
        sf_name = getattr(self, 'cat_name')[0]

        # Loop over all datanodes.
        for datanode in self.datanodes:
            # Find the CSA saveframes via the SfCategory tag index.
            found = False
            for index in range(len(datanode.tagtables[0].tagnames)):
                # First match the tag names.
                if datanode.tagtables[0].tagnames[index] == self.Chem_shift_anisotropy.data_to_tag_name_full['SfCategory']:
                    # Then the tag value.
                    if datanode.tagtables[0].tagvalues[index][0] == sf_name:
                        found = True
                        break

            # Skip the datanode.
            if not found:
                continue

            # Get general info.
            frq = self.Chem_shift_anisotropy.read(datanode.tagtables[0])

            # Get the CSA info.
            res_nums, res_names, atom_names, values, errors = self.CS_anisotropy.read(datanode.tagtables[1])

            # Yield the data.
            yield frq, res_nums, res_names, atom_names, values, errors


        self.cat_name = ['Chem_shift_anisotropy']



class ChemShiftAnisotropy(TagCategoryFree):
    """Base class for the ChemShiftAnisotropy tag category."""

    def __init__(self, sf):
        """Setup the ChemShiftAnisotropy tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(ChemShiftAnisotropy, self).__init__(sf)

        # Database table names to class instance variables.
        self.data_to_var_name.append(['ChemShiftAnisotropyID',      'id'])
        self.data_to_var_name.append(['DataFileName',               'file_name'])
        self.data_to_var_name.append(['SampleConditionListLabel',   'sample_cond_list_label'])
        self.data_to_var_name.append(['ValUnits',                   'units'])

        # Database table name to tag name.
        self.data_to_tag_name['SfCategory'] =               'Saveframe_category'
        self.data_to_tag_name['DataFileName'] =             'Data_file_name'
        self.data_to_tag_name['SampleConditionListLabel'] = 'Sample_conditions_label'
        self.data_to_tag_name['ValUnits'] =                 'Val_units'



class CSAnisotropyExperiment(TagCategory):
    """Base class for the CSAnisotropyExperiment tag category."""

    def __init__(self, sf):
        """Setup the CSAnisotropyExperiment tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(CSAnisotropyExperiment, self).__init__(sf)

        # Database table names to class instance variables.
        self.data_to_var_name.append(['SampleLabel',    'sample_label'])

        # Database table name to tag name.
        self.data_to_tag_name['SampleLabel'] = 'Sample_label'



class CSAnisotropySoftware(TagCategory):
    """Base class for the CSAnisotropySoftware tag category."""



class CSAnisotropy(TagCategory):
    """Base class for the CSAnisotropy tag category."""

    def __init__(self, sf):
        """Setup the CSAnisotropy tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(CSAnisotropy, self).__init__(sf)

        # Database table names to class instance variables.
        self.data_to_var_name.append(['CSAnisotropyID',          'data_ids'])
        self.data_to_var_name.append(['AssemblyAtomID',          'assembly_atom_ids'])
        self.data_to_var_name.append(['EntityAssemblyID',        'entity_assembly_ids'])
        self.data_to_var_name.append(['EntityID',                'entity_ids'])
        self.data_to_var_name.append(['CompIndexID',             'res_nums'])
        self.data_to_var_name.append(['SeqID',                   'seq_id'])
        self.data_to_var_name.append(['CompID',                  'res_names'])
        self.data_to_var_name.append(['AtomID',                  'atom_names'])
        self.data_to_var_name.append(['AtomType',                'atom_types'])
        self.data_to_var_name.append(['AtomIsotopeNumber',       'isotope'])
        self.data_to_var_name.append(['Val',                     'csa'])
        self.data_to_var_name.append(['ValErr',                  'csa_error'])
        self.data_to_var_name.append(['ChemShiftAnisotropyID',   'csa_inc_list'])

        # Database table name to tag name.
        self.data_to_tag_name['CSAnisotropyID'] = None
        self.data_to_tag_name['AssemblyAtomID'] = 'Assembly_atom_ID'
        self.data_to_tag_name['EntityAssemblyID'] = 'Entity_assembly_ID'
        self.data_to_tag_name['EntityID'] = 'Entity_ID'
        self.data_to_tag_name['CompIndexID'] = 'Residue_seq_code'
        self.data_to_tag_name['SeqID'] = 'Seq_ID'
        self.data_to_tag_name['CompID'] = 'Residue_label'
        self.data_to_tag_name['AtomID'] = 'Atom_name'
        self.data_to_tag_name['AtomType'] = 'Atom_type'
        self.data_to_tag_name['AtomIsotopeNumber'] = 'Atom_isotope_number'
        self.data_to_tag_name['Val'] = 'value'
        self.data_to_tag_name['ValErr'] = 'value_error'
        self.data_to_tag_name['ChemShiftAnisotropyID'] = 'Chem_shift_anisotropy_ID'


    def read(self, tagtable):
        """Extract the CSA tag category info.

        @param tagtable:    The CSA tagtable.
        @type tagtable:     Tagtable instance
        @return:            The residue numbers, residue names, atom names, values, and errors.
        @rtype:             tuple of list of int, list of str, list of str, list of float, list of
                            float
        """

        # The entity info.
        res_nums = tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name['CompIndexID'])]
        res_names = tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name['CompID'])]
        atom_names = tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name['AtomID'])]
        values = tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name['Val'])]
        errors = tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name['ValErr'])]

        # Convert the residue numbers to ints and the values and errors to floats.
        for i in range(len(res_nums)):
            res_nums[i] = int(res_nums[i])
            values[i] = float(values[i])
            errors[i] = float(errors[i])

        # Return the data.
        return res_nums, res_names, atom_names, values, errors
