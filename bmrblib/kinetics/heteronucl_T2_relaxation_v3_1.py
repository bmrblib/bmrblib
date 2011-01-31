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
"""The v3.1 Heteronuclear T2 data saveframe category.

See http://www.bmrb.wisc.edu/dictionary/3.1html/SaveFramePage.html#heteronucl_T2_relaxation.
"""

# relax module imports.
from bmrblib.kinetics.heteronucl_T2_relaxation import HeteronuclT2Saveframe, HeteronuclT2List, HeteronuclT2Experiment, HeteronuclT2Software, T2


class HeteronuclT2Saveframe_v3_1(HeteronuclT2Saveframe):
    """The v3.1 Heteronuclear T2 data saveframe class."""

    def add_tag_categories(self):
        """Create the v3.1 tag categories."""

        # The tag category objects.
        self.tag_categories.append(HeteronuclT2List_v3_1(self))
        self.tag_categories.append(HeteronuclT2Experiment_v3_1(self))
        self.tag_categories.append(HeteronuclT2Software_v3_1(self))
        self.tag_categories.append(T2_v3_1(self))



class HeteronuclT2List_v3_1(HeteronuclT2List):
    """v3.1 HeteronuclT2List tag category."""

    def __init__(self, sf):
        """Setup the HeteronuclT2List_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclT2List_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Heteronucl_T2_list'

        # Change tag names.
        self['SfCategory'].tag_name = 'Sf_category'
        self['SfFramecode'].tag_name = 'Sf_framecode'
        self['HeteronuclT2ListID'].tag_name =       'ID'
        self['SampleConditionListLabel'].tag_name = 'Sample_condition_list_label'



class HeteronuclT2Experiment_v3_1(HeteronuclT2Experiment):
    """v3.1 HeteronuclT2Experiment tag category."""

    def __init__(self, sf):
        """Setup the HeteronuclT2Experiment_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclT2Experiment_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Heteronucl_T2_experiment'



class HeteronuclT2Software_v3_1(HeteronuclT2Software):
    """v3.1 HeteronuclT2Software tag category."""

    def __init__(self, sf):
        """Setup the HeteronuclT2Software_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclT2Software_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Heteronucl_T2_software'



class T2_v3_1(T2):
    """v3.1 T2 tag category."""

    def __init__(self, sf):
        """Setup the T2_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(T2_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'T2'

        # Change tag names.
        self['RxID'] =         'ID'
        self['CompIndexID'] =  'Comp_index_ID'
        self['CompID'] =       'Comp_ID'
        self['AtomID'] =       'Atom_ID'
        self['Val'] =          'Val'
        self['ValErr'] =       'Val_err'
