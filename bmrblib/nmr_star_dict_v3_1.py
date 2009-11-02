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
"""The NMR-STAR dictionary API for version 3.1.

The v3.1 NMR-STAR dictionary is documented at
http://www.bmrb.wisc.edu/dictionary/3.1html/SuperGroupPage.html.
"""

# relax module imports.
from bmrblib.assembly_supercategory.entity_v3_1 import EntitySaveframe_v3_1
from bmrblib.citations.citations import CitationsSaveframe
from bmrblib.experimental_details.method import MethodSaveframe
from bmrblib.experimental_details.software import SoftwareSaveframe
from bmrblib.kinetics.relaxation import Relaxation_v3_1
from bmrblib.NMR_parameters.chem_shift_anisotropy_v3_1 import ChemShiftAnisotropySaveframe_v3_1
from bmrblib.thermodynamics.model_free_v3_1 import ModelFreeSaveframe_v3_1
from bmrblib.nmr_star_dict import NMR_STAR


class NMR_STAR_v3_1(NMR_STAR):
    """The v3.1 NMR-STAR dictionary."""

    # Class extension string.
    ext = ''


    def create_saveframes(self):
        """Create all the saveframe objects."""

        # Initialise Supergroup 2:  The citations.
        self.citations = CitationsSaveframe(self.data.datanodes)

        # Initialise Supergroup 3:  The molecular assembly saveframe API.
        self.entity = EntitySaveframe_v3_1(self.data.datanodes)

        # Initialise Supergroup 4:  The experimental descriptions saveframe API.
        self.method = MethodSaveframe(self.data.datanodes)
        self.software = SoftwareSaveframe(self.data.datanodes)

        # Initialise Supergroup 5:  The NMR parameters saveframe API.
        self.chem_shift_anisotropy = ChemShiftAnisotropySaveframe_v3_1(self.data.datanodes)

        # Initialise Supergroup 6:  The kinetic data saveframe API.
        self.relaxation = Relaxation_v3_1(self.data.datanodes)

        # Initialise Supergroup 7:  The thermodynamics saveframe API.
        self.model_free = ModelFreeSaveframe_v3_1(self.data.datanodes)
