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
        self.heteronuclRxlist = HeteronuclT2List_v3_1(self)
        self.heteronuclRxexperiment = HeteronuclT2Experiment_v3_1(self)
        self.heteronuclRxsoftware = HeteronuclT2Software_v3_1(self)
        self.Rx = T2_v3_1(self)



class HeteronuclT2List_v3_1(HeteronuclT2List):
    """v3.1 HeteronuclT2List tag category."""

    # The category name.
    tag_category_label = 'Heteronucl_T2_list'

    def __init__(self, sf):
        """Setup the HeteronuclT2List_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclT2List_v3_1, self).__init__(sf)

        # Database table name to tag name.
        self.data_to_tag_name['SfCategory'] =               'Sf_category'
        self.data_to_tag_name['HeteronuclT2ListID'] =       'ID'
        self.data_to_tag_name['SampleConditionListLabel'] = 'Sample_condition_list_label'



class HeteronuclT2Experiment_v3_1(HeteronuclT2Experiment):
    """v3.1 HeteronuclT2Experiment tag category."""

    # The category name.
    tag_category_label = 'Heteronucl_T2_experiment'



class HeteronuclT2Software_v3_1(HeteronuclT2Software):
    """v3.1 HeteronuclT2Software tag category."""

    # The category name.
    tag_category_label = 'Heteronucl_T2_software'



class T2_v3_1(T2):
    """v3.1 T2 tag category."""

    # The category name.
    tag_category_label = 'T2'

    def __init__(self, sf):
        """Setup the T2_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(T2_v3_1, self).__init__(sf)

        # Database table names to class instance variables.
        self.data_to_tag_name['RxID'] =         'ID'
        self.data_to_tag_name['CompIndexID'] =  'Comp_index_ID'
        self.data_to_tag_name['CompID'] =       'Comp_ID'
        self.data_to_tag_name['AtomID'] =       'Atom_ID'
        self.data_to_tag_name['Val'] =          'Val'
        self.data_to_tag_name['ValErr'] =       'Val_err'
