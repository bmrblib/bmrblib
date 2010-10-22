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
from bmrblib.base_classes import BaseSaveframe, TagCategory, TagCategoryFree


class EntitySaveframe(BaseSaveframe):
    """The entity saveframe class."""

    # Class variables.
    label = 'entity'
    sf_label = 'entity'

    def add_tag_categories(self):
        """Create the tag categories."""

        # The tag category objects.
        self.tag_categories.append(Entity(self))
        self.tag_categories.append(EntityCompIndex(self))



class Entity(TagCategoryFree):
    """Base class for the Entity tag category."""

    def __init__(self, sf):
        """Setup the Entity tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(Entity, self).__init__(sf)

        # Add the tag info.
        self.add(key='EntityID',                tag_name='ID',                          var_name='count_str',       format='int')
        self.add(key='Name',                    tag_name='Name',                        var_name='mol_name')
        self.add(key='Type',                    tag_name='Type',                        var_name='mol_type')
        self.add(key='PolymerType',             tag_name='Polymer_type',                var_name='polymer_type',    allowed=['DNA/RNA hybrid', 'polydeoxyribonucleotide', 'polypeptide(D)', 'polypeptide(L)', 'polyribonucleotide', 'polysaccharide(D)', 'polysaccharide(L)'])
        self.add(key='PolymerSeqOneLetterCode', tag_name='Polymer_seq_one_letter_code', var_name='polymer_seq_code')
        self.add(key='ThiolState',              tag_name='Thiol_state',                 var_name='thiol_state')



class EntityCompIndex(TagCategory):
    """Base class for the EntityCompIndex tag category."""

    def __init__(self, sf):
        """Setup the Entity tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(EntityCompIndex, self).__init__(sf)

        # Add the tag info.
        self.add(key='EntityCompIndexID',   tag_name='ID',          var_name='res_nums',    format='int')
        self.add(key='CompID',              tag_name='Comp_ID',     var_name='res_names')
        self.add(key='EntityID',            tag_name='Entity_ID',   var_name='count_str',   format='int')
