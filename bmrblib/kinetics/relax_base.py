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



class HeteronuclRxList(TagCategoryFree):
    """Base class for the HeteronuclRxList tag categories."""



class Rx(TagCategory):
    """Base class for the Rx tag categories."""

    def __init__(self, sf):
        """Setup the Rx tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(Rx, self).__init__(sf)

        # Add the tag info.
        self.add(key='RxID',                tag_name='id',                                  var_name='data_ids')
        self.add(key='AssemblyAtomID',      tag_name='Assembly_atom_ID',                    var_name='assembly_atom_ids')
        self.add(key='EntityAssemblyID',    tag_name='Entity_assembly_ID',                  var_name='entity_assembly_ids')
        self.add(key='EntityID',            tag_name='Entity_ID',                           var_name='entity_ids')
        self.add(key='CompIndexID',         tag_name='Residue_seq_code',                    var_name='res_nums')
        self.add(key='SeqID',               tag_name='Seq_ID',                              var_name='seq_id')
        self.add(key='CompID',              tag_name='Residue_label',                       var_name='res_names')
        self.add(key='AtomID',              tag_name='Atom_name',                           var_name='atom_names')
        self.add(key='AtomType',            tag_name='Atom_type',                           var_name='atom_types')
        self.add(key='AtomIsotopeNumber',   tag_name='Atom_isotope_number',                 var_name='isotope')
        self.add(key='Val',                 tag_name=self.sf.name+'_value',                 var_name='data')
        self.add(key='ValErr',              tag_name=self.sf.name+'_value_error',           var_name='errors')
