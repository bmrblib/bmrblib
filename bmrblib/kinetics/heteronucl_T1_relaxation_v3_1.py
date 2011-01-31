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
"""The v3.1 Heteronuclear T1 data saveframe category.

See http://www.bmrb.wisc.edu/dictionary/3.1html/SaveFramePage.html#heteronucl_T1_relaxation.
"""

# relax module imports.
from bmrblib.kinetics.heteronucl_T1_relaxation import HeteronuclT1Saveframe, HeteronuclT1List, HeteronuclT1Experiment, HeteronuclT1Software, T1


class HeteronuclT1Saveframe_v3_1(HeteronuclT1Saveframe):
    """The v3.1 Heteronuclear T1 data saveframe class."""

    # Class variables.
    sf_label = 'heteronucl_T1_relaxation'

    def add_tag_categories(self):
        """Create the v3.1 tag categories."""

        # The tag category objects.
        self.tag_categories.append(HeteronuclT1List_v3_1(self))
        self.tag_categories.append(HeteronuclT1Experiment_v3_1(self))
        self.tag_categories.append(HeteronuclT1Software_v3_1(self))
        self.tag_categories.append(T1_v3_1(self))



class HeteronuclT1List_v3_1(HeteronuclT1List):
    """v3.1 HeteronuclT1List tag category."""

    def __init__(self, sf):
        """Setup the HeteronuclT1List_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclT1List_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Heteronucl_T1_list'

        # Change tag names.
        self['SfCategory'].tag_name = 'Sf_category'
        self['SfFramecode'].tag_name = 'Sf_framecode'
        self['HeteronuclT1ListID'].tag_name =       'ID'
        self['SampleConditionListLabel'].tag_name = 'Sample_condition_list_label'



class HeteronuclT1Experiment_v3_1(HeteronuclT1Experiment):
    """v3.1 HeteronuclT1Experiment tag category."""

    def __init__(self, sf):
        """Setup the HeteronuclT1Experiment_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclT1Experiment_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Heteronucl_T1_experiment'


class HeteronuclT1Software_v3_1(HeteronuclT1Software):
    """v3.1 HeteronuclT1Software tag category."""

    def __init__(self, sf):
        """Setup the HeteronuclT1Software_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclT1Software_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Heteronucl_T1_software'



class T1_v3_1(T1):
    """v3.1 T1 tag category."""

    def __init__(self, sf):
        """Setup the T1_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(T1_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'T1'

        # Change tag names.
        self['RxID'] =         'ID'
        self['CompIndexID'] =  'Comp_index_ID'
        self['CompID'] =       'Comp_ID'
        self['AtomID'] =       'Atom_ID'
        self['Val'] =          'Val'
        self['ValErr'] =       'Val_err'
