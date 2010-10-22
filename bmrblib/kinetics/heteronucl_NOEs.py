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
"""The Heteronuclear NOE data saveframe category.

For example, see http://www.bmrb.wisc.edu/dictionary/3.1html/SaveFramePage.html#heteronucl_NOEs.
"""

# relax module imports.
from bmrblib.base_classes import TagCategory
from bmrblib.kinetics.relax_base import HeteronuclRxList, RelaxSaveframe, Rx


class HeteronuclNOESaveframe(RelaxSaveframe):
    """The Heteronuclear NOE data saveframe class."""

    # Class variables.
    name = 'NOE'
    label = 'heteronucl_NOE'
    sf_label = 'heteronucl_NOEs'

    def add_tag_categories(self):
        """Create the tag categories."""

        # The tag category objects.
        self.tag_categories.append(HeteronuclNOEList(self))
        self.tag_categories.append(HeteronuclNOEExperiment(self))
        self.tag_categories.append(HeteronuclNOESoftware(self))
        self.tag_categories.append(HeteronuclNOE(self))


    def pre_ops(self):
        """Perform some saveframe specific operations prior to XML creation."""

        # The saveframe description.
        self.sf_framecode = '%s MHz heteronuclear NOE %s' % (self.frq, self.count)



class HeteronuclNOEList(HeteronuclRxList):
    """Base class for the HeteronuclNOEList tag category."""

    def __init__(self, sf):
        """Setup the HeteronuclNOEList tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclNOEList, self).__init__(sf)

        # Add the tag info.
        self.add(key='HeteronuclNOEListID',         tag_name='ID',                          var_name='count_str')
        self.add(key='SampleConditionListID',       tag_name='Sample_condition_list_ID',    var_name='sample_cond_list_id')
        self.add(key='SampleConditionListLabel',    tag_name='Sample_conditions_label',     var_name='sample_cond_list_label',  default='$conditions_1')
        self.add(key='SpectrometerFrequency1H',     tag_name='Spectrometer_frequency_1H',   var_name='frq',                     format='float')
        self.add(key='Details',                     tag_name='Details',                     var_name='details')



class HeteronuclNOEExperiment(TagCategory):
    """Base class for the HeteronuclNOEExperiment tag category."""

    def __init__(self, sf):
        """Setup the HeteronuclNOEExperiment tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclNOEExperiment, self).__init__(sf)

        # Add the tag info.
        self.add(key='SampleLabel', tag_name='Sample_label',    var_name='sample_label',    default='$sample_1')



class HeteronuclNOESoftware(TagCategory):
    """Base class for the HeteronuclNOESoftware tag category."""



class HeteronuclNOE(Rx):
    """Base class for the HeteronuclNOE tag category."""

    def __init__(self, sf):
        """Setup the HeteronuclNOEList tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclNOE, self).__init__(sf)

        # Add the tag info.
        self.add(key='HeteronuclNOEListID', tag_name='Heteronucl_NOE_list_ID',  var_name='count_str')
