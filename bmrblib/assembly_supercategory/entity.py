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
"""The entity saveframe category.

For example, see http://www.bmrb.wisc.edu/dictionary/3.1html/SaveFramePage.html#entity.
"""

# relax module imports.
from bmrblib.base_classes import TagCategory, TagCategoryFree
from bmrblib.misc import translate
from bmrblib.pystarlib.SaveFrame import SaveFrame
from bmrblib.pystarlib.TagTable import TagTable


class EntitySaveframe:
    """The entity saveframe class."""

    # Class variables.
    label = 'entity'
    sf_label = 'entity'

    def __init__(self, datanodes):
        """Initialise the class, placing the pystarlib data nodes into the namespace.

        @param datanodes:   The pystarlib data nodes object.
        @type datanodes:    list
        """

        # Place the data nodes into the namespace.
        self.datanodes = datanodes

        # The number of entities.
        self.entity_num = 0

        # Add the specific tag category objects.
        self.add_tag_categories()


    def add(self, mol_name=None, mol_type='polymer', polymer_type='polypeptide(L)', polymer_seq_code=None, thiol_state='all free', res_nums=None, res_names=None, atom_names=None):
        """Add relaxation data to the data nodes.

        @keyword mol_name:          The molecule name.
        @type mol_name:             str
        @keyword mol_type:          The molecule type.
        @type mol_type:             str
        @keyword polymer_type:      The type of polymer.  This is only allowed to be one of 'DNA/RNA hybrid', 'polydeoxyribonucleotide', 'polypeptide(D)', 'polypeptide(L)', 'polyribonucleotide', 'polysaccharide(D)', 'polysaccharide(L)'.
        @type polymer_type:         str
        @keyword polymer_seq_code:  The complete sequence of a protein or nucleic acid as it existed in the NMR tube expressed using the one-letter code for standard residues and an X for non-standard residues. Include residues for cloning tags, etc. and for all residues even when experimental data are not reported.  For example, 'HHHHHHAFGCRESWQAKCLPHNMVIXSDF'.
        @type polymer_seq_code:     str
        @keyword thiol_state:       The state of the thiol groups in the entity.  Can be one of 'all disulfide bound', 'all free', 'all other bound', 'disulfide and other bound', 'free and disulfide bound', 'free and other bound', 'free disulfide and other bound', 'not available', 'not present', 'not reported', 'unknown'.
        @type thiol_state:          str
        @keyword res_nums:          The residue number list.
        @type res_nums:             list of int
        @keyword res_names:         The residue name list.
        @type res_names:            list of str
        @keyword atom_names:        The atom name list.
        @type atom_names:           list of str
        """

        # Check the polymer type.
        allowed = ['DNA/RNA hybrid', 'polydeoxyribonucleotide', 'polypeptide(D)', 'polypeptide(L)', 'polyribonucleotide', 'polysaccharide(D)', 'polysaccharide(L)']
        if polymer_type not in allowed:
            raise NameError("The polymer type '%s' should be one of %s." % (polymer_type, allowed))

        # Check the polymer one letter code sequence.
        if not isinstance(polymer_seq_code, str):
            raise NameError("The polymer one letter code sequence '%s' should be a string." % polymer_seq_code)

        # Place the args into the namespace.
        self.mol_name = mol_name
        self.mol_type = mol_type
        self.polymer_type = translate(polymer_type)
        self.polymer_seq_code = translate(polymer_seq_code)
        self.thiol_state = translate(thiol_state)
        self.res_names = translate(res_names)
        self.res_nums = translate(res_nums)
        self.atom_names = translate(atom_names)

        # Increment the number of entities.
        self.entity_num = self.entity_num + 1
        self.entity_num_str = str(self.entity_num)

        # The entity ID list.
        self.entity_ids = [str(self.entity_num)]*len(self.res_nums)

        # Initialise the save frame.
        self.frame = SaveFrame(title=mol_name)

        # Create the tag categories.
        self.entity.create()
        self.entity_comp_index.create()

        # Add the saveframe to the data nodes.
        self.datanodes.append(self.frame)


    def add_tag_categories(self):
        """Create the tag categories."""

        # The tag category objects.
        self.entity = Entity(self)
        self.entity_comp_index = EntityCompIndex(self)


    def loop(self):
        """Loop over the entity saveframes, yielding the entity info.

        @return:    The entity information consisting of the molecule name, molecule type, residue
                    numbers, and residue names.
        @rtype:     tuple of str, str, list of int, list of str
        """

        # Set up the tag information.
        self.entity.tag_setup()
        self.entity_comp_index.tag_setup()

        # Loop over all datanodes.
        for datanode in self.datanodes:
            # Find the Entity saveframes via the SfCategory tag index.
            found = False
            for index in range(len(datanode.tagtables[0].tagnames)):
                # First match the tag names.
                if datanode.tagtables[0].tagnames[index] == self.entity.data_to_tag_name_full['SfCategory']:
                    # Then the tag value.
                    if datanode.tagtables[0].tagvalues[index][0] == 'entity':
                        found = True
                        break

            # Skip the datanode.
            if not found:
                continue

            # Get entity info.
            mol_name, mol_type = self.entity.read(datanode.tagtables[0])

            # Get the EntityCompIndex info.
            res_nums, res_names = self.entity_comp_index.read(datanode.tagtables[1])

            # Yield the data.
            yield mol_name, mol_type, res_nums, res_names



class Entity(TagCategoryFree):
    """Base class for the Entity tag category."""

    def __init__(self, sf):
        """Setup the Entity tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(Entity, self).__init__(sf)

        # Database table names to class instance variables.
        self.data_to_var_name.append(['EntityID',                   'entity_num_str'])
        self.data_to_var_name.append(['Name',                       'mol_name'])
        self.data_to_var_name.append(['Type',                       'mol_type'])
        self.data_to_var_name.append(['PolymerType',                'polymer_type'])
        self.data_to_var_name.append(['PolymerSeqOneLetterCode',    'polymer_seq_code'])
        self.data_to_var_name.append(['ThiolState',                 'thiol_state'])

        # Database table name to tag name.
        self.data_to_tag_name['SfCategory'] = 'Saveframe_category'
        self.data_to_tag_name['EntityID'] = 'ID'
        self.data_to_tag_name['Name'] = 'Name'
        self.data_to_tag_name['Type'] = 'Type'
        self.data_to_tag_name['PolymerType'] = 'Polymer_type'
        self.data_to_tag_name['PolymerSeqOneLetterCode'] = 'Polymer_seq_one_letter_code'
        self.data_to_tag_name['ThiolState'] = 'Thiol_state'


    def read(self, tagtable):
        """Extract the Entity tag category info.

        @param tagtable:    The Entity tagtable.
        @type tagtable:     Tagtable instance
        @return:            The entity name and type.
        @rtype:             tuple of str, str
        """

        # The entity info.
        mol_name = tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name_full['Name'])][0]
        mol_type = tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name_full['Type'])][0]

        # Return the data.
        return mol_name, mol_type



class EntityCompIndex(TagCategory):
    """Base class for the EntityCompIndex tag category."""

    def __init__(self, sf):
        """Setup the Entity tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(EntityCompIndex, self).__init__(sf)

        # Database table names to class instance variables.
        self.data_to_var_name.append(['EntityCompIndexID',   'res_nums'])
        self.data_to_var_name.append(['CompID',              'res_names'])
        self.data_to_var_name.append(['EntityID',            'entity_ids'])

        # Database table name to tag name.
        self.data_to_tag_name['EntityCompIndexID'] = 'ID'
        self.data_to_tag_name['CompID'] = 'Comp_ID'
        self.data_to_tag_name['EntityID'] = 'Entity_ID'


    def read(self, tagtable):
        """Extract the EntityCompIndex tag category info.

        @param tagtable:    The EntityCompIndex tagtable.
        @type tagtable:     Tagtable instance
        @return:            The residue numbers and names.
        @rtype:             tuple of list of int, list of str
        """

        # The entity info.
        res_nums = tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name_full['EntityCompIndexID'])]
        res_names = tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name_full['CompID'])]

        # Convert the residue numbers to ints.
        for i in range(len(res_nums)):
            res_nums[i] = int(res_nums[i])

        # Return the data.
        return res_nums, res_names
