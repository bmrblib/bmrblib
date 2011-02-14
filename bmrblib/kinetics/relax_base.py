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
        self.add(key='RxID',                    var_name='data_ids',                format='int')
        self.add(key='AssemblyAtomID',          var_name='assembly_atom_ids',       format='int')
        self.add(key='EntityAssemblyID',        var_name='entity_assembly_ids',     format='int')
        self.add(key='EntityID',                var_name='entity_ids',              format='int')
        self.add(key='CompIndexID',             var_name='res_nums',                format='int')
        self.add(key='SeqID',                   var_name='seq_id',                  format='int')
        self.add(key='CompID',                  var_name='res_names',               format='str')
        self.add(key='AtomID',                  var_name='atom_names',              format='str')
        self.add(key='AtomType',                var_name='atom_types',              format='str')
        self.add(key='AtomIsotopeNumber',       var_name='isotope',                 format='int')
        self.add(key='Val',                     var_name='data',                    format='float')
        self.add(key='ValErr',                  var_name='errors',                  format='float')
        self.add(key='ResonanceID',             var_name='resonance_id',            format='int')
        self.add(key='AuthEntityAssemblyID',    var_name='auth_entity_assembly_id', format='str')
        self.add(key='AuthSeqID',               var_name='auth_seq_id',             format='str')
        self.add(key='AuthCompID',              var_name='auth_comp_id',            format='str')
        self.add(key='AuthAtomID',              var_name='auth_atom_id',            format='str')
        self.add(key='EntryID',                 var_name='entry_id',                format='str')
        self.add(key='HeteronuclT1ListID',      var_name='heteronucl_t1_list_id',   format='int')
