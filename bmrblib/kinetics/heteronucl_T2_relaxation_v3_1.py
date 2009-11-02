#############################################################################
#                                                                           #
# The BMRB library.                                                         #
#                                                                           #
# Copyright (C) 2009 Edward d'Auvergne                                      #
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


    def specific_setup(self):
        """Method called by self.add() to set up any version specific data."""

        # The category name.
        self.cat_name = ['heteronucl_T2_relaxation']


class HeteronuclT2List_v3_1(HeteronuclT2List):
    """v3.1 HeteronuclT2List tag category."""

    def tag_setup(self, tag_category_label=None, sep=None):
        # Execute the base class tag_setup() method.
        HeteronuclT2List.tag_setup(self, tag_category_label='Heteronucl_T2_list', sep=sep)

        # Tag names for the relaxation data.
        self.tag_names['SfCategory'] = 'Sf_category'
        self.tag_names['HeteronuclT2ListID'] = 'ID'
        self.tag_names['SampleConditionListLabel'] = 'Sample_condition_list_label'


class HeteronuclT2Experiment_v3_1(HeteronuclT2Experiment):
    """v3.1 HeteronuclT2Experiment tag category."""

    def tag_setup(self, tag_category_label=None, sep=None):
        # Execute the base class tag_setup() method.
        HeteronuclT2Experiment.tag_setup(self, tag_category_label='Heteronucl_T2_experiment', sep=sep)


class HeteronuclT2Software_v3_1(HeteronuclT2Software):
    """v3.1 HeteronuclT2Software tag category."""

    def tag_setup(self, tag_category_label=None, sep=None):
        # Execute the base class tag_setup() method.
        HeteronuclT2Software.tag_setup(self, tag_category_label='Heteronucl_T2_software', sep=sep)


class T2_v3_1(T2):
    """v3.1 T2 tag category."""

    def tag_setup(self, tag_category_label=None, sep=None):
        # Execute the base class tag_setup() method.
        T2.tag_setup(self, tag_category_label='T2', sep=sep)

        # Tag names for the relaxation data.
        self.tag_names['RxID'] = 'ID'
        self.tag_names['CompIndexID'] = 'Comp_index_ID'
        self.tag_names['CompID'] = 'Comp_ID'
        self.tag_names['AtomID'] = 'Atom_ID'
        self.tag_names['Val'] = 'Val'
        self.tag_names['ValErr'] = 'Val_err'
