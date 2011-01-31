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
"""The Heteronuclear T2 data saveframe category.

For example, see http://www.bmrb.wisc.edu/dictionary/3.1html/SaveFramePage.html#heteronucl_T2_relaxation.
"""

# relax module imports.
from bmrblib.base_classes import TagCategory
from bmrblib.kinetics.relax_base import HeteronuclRxList, RelaxSaveframe, Rx


class HeteronuclT2Saveframe(RelaxSaveframe):
    """The Heteronuclear T2 data saveframe class."""

    # Class variables.
    name = 'T2'
    label = 'heteronucl_T2'
    sf_label = 'T2_relaxation'

    def add_tag_categories(self):
        """Create the tag categories."""

        # The tag category objects.
        self.tag_categories.append(HeteronuclT2List(self))
        self.tag_categories.append(HeteronuclT2Experiment(self))
        self.tag_categories.append(HeteronuclT2Software(self))
        self.tag_categories.append(T2(self))



class HeteronuclT2List(HeteronuclRxList):
    """Base class for the HeteronuclT2List tag category."""


    def __init__(self, sf):
        """Setup the HeteronuclT2List tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclT2List, self).__init__(sf)

        # Add the tag info.
        self.add(key='HeteronuclT2ListID',          tag_name='ID',                          var_name='count_str',               format='int')
        self.add(key='SampleConditionListID',       tag_name='Sample_condition_list_ID',    var_name='sample_cond_list_id')
        self.add(key='SampleConditionListLabel',    tag_name='Sample_conditions_label',     var_name='sample_cond_list_label',  default='$conditions_1')
        self.add(key='SpectrometerFrequency1H',     tag_name='Spectrometer_frequency_1H',   var_name='frq',                     format='float')
        self.add(key='T2CoherenceType',             tag_name='T2_coherence_type',           var_name='coherence',               default='Ny')
        self.add(key='T2ValUnits',                  tag_name='T2_value_units',              var_name='units',                   default='1/s')
        self.add(key='Details',                     tag_name='Details',                     var_name='details')



class HeteronuclT2Experiment(TagCategory):
    """Base class for the HeteronuclT2Experiment tag category."""

    def __init__(self, sf):
        """Setup the HeteronuclT2Experiment tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclT2Experiment, self).__init__(sf)

        # Add the tag info.
        self.add(key='SampleLabel', tag_name='Sample_label',    var_name='sample_label',    default='$sample_1')



class HeteronuclT2Software(TagCategory):
    """Base class for the HeteronuclT2Software tag category."""



class T2(Rx):
    """Base class for the T2 tag category."""
