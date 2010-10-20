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
"""The v3.1 chemical shift anisotropy data saveframe category.

See http://www.bmrb.wisc.edu/dictionary/3.1html_frame/frame_SaveFramePage.html#chem_shift_anisotropy
"""

# relax module imports.
from bmrblib.misc import translate
from bmrblib.NMR_parameters.chem_shift_anisotropy import ChemShiftAnisotropySaveframe, ChemShiftAnisotropy, CSAnisotropyExperiment, CSAnisotropySoftware, CSAnisotropy


class ChemShiftAnisotropySaveframe_v3_1(ChemShiftAnisotropySaveframe):
    """The v3.1 chemical shift anisotropy data saveframe class."""

    def add_tag_categories(self):
        """Create the v3.1 tag categories."""

        # The tag category objects.
        self.Chem_shift_anisotropy = ChemShiftAnisotropy_v3_1(self)
        self.CS_anisotropy_experiment = CSAnisotropyExperiment_v3_1(self)
        self.CS_anisotropy_software = CSAnisotropySoftware_v3_1(self)
        self.CS_anisotropy = CSAnisotropy_v3_1(self)



class ChemShiftAnisotropy_v3_1(ChemShiftAnisotropy):
    """v3.1 ChemShiftAnisotropy tag category."""

    def __init__(self, sf):
        """Setup the ChemShiftAnisotropy_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(ChemShiftAnisotropy_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Chem_shift_anisotropy'

        # Database table name to tag name.
        self.data_to_tag_name['SfCategory'] =               'Sf_category'
        self.data_to_tag_name['ChemShiftAnisotropyID'] =    'ID'
        self.data_to_tag_name['SampleConditionListLabel'] = 'Sample_condition_list_label'



class CSAnisotropyExperiment_v3_1(CSAnisotropyExperiment):
    """v3.1 CSAnisotropyExperiment tag category."""

    def __init__(self, sf):
        """Setup the CSAnisotropyExperiment_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(CSAnisotropyExperiment_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'CS_anisotropy_experiment'



class CSAnisotropySoftware_v3_1(CSAnisotropySoftware):
    """v3.1 CSAnisotropySoftware tag category."""

    def __init__(self, sf):
        """Setup the CSAnisotropySoftware_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(CSAnisotropySoftware_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'CS_anisotropy_software'



class CSAnisotropy_v3_1(CSAnisotropy):
    """v3.1 CSAnisotropy tag category."""

    def __init__(self, sf):
        """Setup the CSAnisotropy_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(CSAnisotropy_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'CS_anisotropy'

        # Database table name to tag name.
        self.data_to_tag_name['CSAnisotropyID'] = 'ID'
        self.data_to_tag_name['CompIndexID'] = 'Comp_index_ID'
        self.data_to_tag_name['CompID'] = 'Comp_ID'
        self.data_to_tag_name['AtomID'] = 'Atom_ID'
        self.data_to_tag_name['Val'] = 'Val'
        self.data_to_tag_name['ValErr'] = 'Val_err'
