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
"""The v3.1 entity saveframe category.

See http://www.bmrb.wisc.edu/dictionary/3.1html/SaveFramePage.html#entity.
"""

# relax module imports.
from bmrblib.assembly_supercategory.entity import EntitySaveframe, Entity, EntityCompIndex


class EntitySaveframe_v3_1(EntitySaveframe):
    """The v3.1 entity saveframe class."""

    def add_tag_categories(self):
        """Create the v3.1 tag categories."""

        # The tag category objects.
        self.tag_categories.append(Entity_v3_1(self))
        self.tag_categories.append(EntityCompIndex_v3_1(self))



class Entity_v3_1(Entity):
    """v3.1 Entity tag category."""

    def __init__(self, sf):
        """Setup the Entity tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(Entity_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Entity'



class EntityCompIndex_v3_1(EntityCompIndex):
    """v3.1 EntityCompIndex tag category."""

    def __init__(self, sf):
        """Setup the EntityCompIndex_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(EntityCompIndex_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Entity_comp_index'
