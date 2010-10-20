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
"""Base classes for the relaxation data."""

# relax module imports.
from bmrblib.base_classes import BaseSaveframe, TagCategory, TagCategoryFree


class RelaxSaveframe(BaseSaveframe):
    """The heteronuclear Rx data saveframe baseclass."""

    def loop(self):
        """Loop over the Rx saveframes, yielding the relaxation data.

        @return:    The relaxation data consisting of the proton frequency, residue numbers, residue
                    names, atom names, values, and errors.
        @rtype:     tuple of float, list of int, list of str, list of str, list of float, list of
                    float
        """

        # Set up the tag information.
        self.heteronuclRxlist.tag_setup()

        # Get the saveframe name.
        sf_name = getattr(self, 'sf_label')[0]

        # Loop over all datanodes.
        for datanode in self.datanodes:
            # Find the Heteronuclear Rx saveframes via the SfCategory tag index.
            found = False
            for index in range(len(datanode.tagtables[0].tagnames)):
                # First match the tag names.
                if datanode.tagtables[0].tagnames[index] == self.heteronuclRxlist.data_to_tag_name_full['SfCategory']:
                    # Then the tag value.
                    if datanode.tagtables[0].tagvalues[index][0] == sf_name:
                        found = True
                        break

            # Skip the datanode.
            if not found:
                continue

            # Get general info.
            frq = self.heteronuclRxlist.read(datanode.tagtables[0])

            # Get the Rx info.
            entity_ids, res_nums, res_names, atom_names, values, errors = self.Rx.read(datanode.tagtables[1])

            # Yield the data.
            yield frq, entity_ids, res_nums, res_names, atom_names, values, errors



class HeteronuclRxList(TagCategoryFree):
    """Base class for the HeteronuclRxList tag categories."""

    def read(self, tagtable):
        """Extract the HeteronuclRxList tag category info.

        @param tagtable:    The HeteronuclRxList tagtable.
        @type tagtable:     Tagtable instance
        @return:            The proton frequency in Hz.
        @rtype:             float
        """

        # The general info.
        frq = float(tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name_full['SpectrometerFrequency1H'])][0]) * 1e6

        # Return the data.
        return frq



class Rx(TagCategory):
    """Base class for the Rx tag categories."""

    def __init__(self, sf):
        """Setup the Rx tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(Rx, self).__init__(sf)

        # Database table names to class instance variables.
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
        self.data_to_var_name.append(['Val',                 'data'])
        self.data_to_var_name.append(['ValErr',              'errors'])
        self.data_to_var_name.append(['HeteronuclRxListID',  'rx_inc_list'])

        # Database table name to tag name.
        self.data_to_tag_name['RxID'] = None
        self.data_to_tag_name['AssemblyAtomID'] = 'Assembly_atom_ID'
        self.data_to_tag_name['EntityAssemblyID'] = 'Entity_assembly_ID'
        self.data_to_tag_name['EntityID'] = 'Entity_ID'
        self.data_to_tag_name['CompIndexID'] = 'Residue_seq_code'
        self.data_to_tag_name['SeqID'] = 'Seq_ID'
        self.data_to_tag_name['CompID'] = 'Residue_label'
        self.data_to_tag_name['AtomID'] = 'Atom_name'
        self.data_to_tag_name['AtomType'] = 'Atom_type'
        self.data_to_tag_name['AtomIsotopeNumber'] = 'Atom_isotope_number'
        self.data_to_tag_name['Val'] = self.sf.name+'_value'
        self.data_to_tag_name['ValErr'] = self.sf.name+'_value_error'
        self.data_to_tag_name['HeteronuclRxListID'] = 'Heteronucl_'+self.sf.name+'_list_ID'


    def read(self, tagtable):
        """Extract the Rx tag category info.

        @param tagtable:    The Rx tagtable.
        @type tagtable:     Tagtable instance
        @return:            The residue numbers, residue names, atom names, values, and errors.
        @rtype:             tuple of list of int, list of str, list of str, list of float, list of
                            float
        """

        # The entity info.
        entity_ids = tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name_full['EntityID'])]
        res_nums = tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name_full['CompIndexID'])]
        res_names = tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name_full['CompID'])]
        atom_names = tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name_full['AtomID'])]
        values = tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name_full['Val'])]
        errors = tagtable.tagvalues[tagtable.tagnames.index(self.data_to_tag_name_full['ValErr'])]

        # Convert the residue numbers to ints and the values and errors to floats.
        for i in range(len(res_nums)):
            res_nums[i] = int(res_nums[i])
            if values[i] == '?':
                values[i] = None
            else:
                values[i] = float(values[i])
            if errors[i] == '?':
                errors[i] = None
            else:
                errors[i] = float(errors[i])

        # Return the data.
        return entity_ids, res_nums, res_names, atom_names, values, errors
