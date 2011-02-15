#############################################################################
#                                                                           #
# The BMRB library.                                                         #
#                                                                           #
# Copyright (C) 2009-2011 Edward d'Auvergne                                 #
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
        self.add(key='EntryID',                     var_name='entry_id',                format='str')
        self.add(key='HeteronuclT2ListID',          var_name='count_str',               format='int')
        self.add(key='DataFileName',                var_name='data_file_name',          format='str')
        self.add(key='SampleConditionListID',       var_name='sample_cond_list_id',     format='int')
        self.add(key='SampleConditionListLabel',    var_name='sample_cond_list_label',  format='str',  default='$conditions_1')
        self.add(key='SpectrometerFrequency1H',     var_name='frq',                     format='float')
        self.add(key='T2CoherenceType',             var_name='coherence',               format='str',  default='Ny')
        self.add(key='T2ValUnits',                  var_name='units',                   format='str',  default='1/s')
        self.add(key='Details',                     var_name='details',                 format='str')
        self.add(key='TextDataFormat',              var_name='text_data_format',        format='str')
        self.add(key='TextData',                    var_name='text_data',               format='str')



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
        self.add(key='ExperimentID',        var_name='experiment_id',           format='int')
        self.add(key='ExperimentName',      var_name='experiment_name',         format='str')
        self.add(key='SampleID',            var_name='sample_id',               format='int')
        self.add(key='SampleLabel',         var_name='sample_label',            format='str',    default='$sample_1')
        self.add(key='SampleState',         var_name='sample_state',            format='str')
        self.add(key='EntryID',             var_name='entry_id',                format='str')
        self.add(key='HeteronuclT2ListID',  var_name='heteronucl_t1_list_id',   format='int')



class HeteronuclT2Software(TagCategory):
    """Base class for the HeteronuclT2Software tag category."""

    def __init__(self, sf):
        """Setup the HeteronuclT2Software tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(HeteronuclT2Software, self).__init__(sf)

        # Add the tag info.
        self.add(key='SoftwareID',          var_name='software_id',             format='int')
        self.add(key='SoftwareLabel',       var_name='software_label',          format='str')
        self.add(key='MethodID',            var_name='method_id',               format='int')
        self.add(key='MethodLabel',         var_name='method_label',            format='str')
        self.add(key='EntryID',             var_name='entry_id',                format='str')
        self.add(key='HeteronuclT2ListID',  var_name='heteronucl_t1_list_id',   format='int')



class T2(Rx):
    """Base class for the T2 tag category."""
