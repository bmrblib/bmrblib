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
"""The base classes for the NMR-STAR dictionary support within relax.

The most up to date NMR-STAR dictionary relax uses is the v3.1 version documented at
http://www.bmrb.wisc.edu/dictionary/3.1html/SuperGroupPage.html.
"""

# relax module imports.
from bmrblib.assembly_supercategory.entity import EntitySaveframe
from bmrblib.citations.citations import CitationsSaveframe
from bmrblib.experimental_details.method import MethodSaveframe
from bmrblib.experimental_details.software import SoftwareSaveframe
from bmrblib.kinetics.relaxation import Relaxation
from bmrblib.NMR_parameters.chem_shift_anisotropy import ChemShiftAnisotropySaveframe
from bmrblib.thermodynamics.model_free import ModelFreeSaveframe
from bmrblib.pystarlib.File import File


class NMR_STAR:
    """The base object for the NMR-STAR dictionary."""

    # Class extension string.
    ext = ''


    def __init__(self, title, file_path):
        """Initialise the NMR-STAR dictionary object.

        @param title:       The title of the NMR-STAR data.
        @type title:        str
        @param file_path:   The full file path.
        @type file_path:    str
        """

        # Initialise the pystarlib File object.
        self.data = File(title=title, filename=file_path)

        # Create the class objects.
        self.create_saveframes()


    def create_saveframes(self):
        """Create all the saveframe objects."""

        # Initialise Supergroup 2:  The citations.
        self.citations = CitationsSaveframe(self.data.datanodes)

        # Initialise Supergroup 3:  The molecular assembly saveframe API.
        self.entity = EntitySaveframe(self.data.datanodes)

        # Initialise Supergroup 4:  The experimental descriptions saveframe API.
        self.method = MethodSaveframe(self.data.datanodes)
        self.software = SoftwareSaveframe(self.data.datanodes)

        # Initialise Supergroup 5:  The NMR parameters saveframe API.
        self.chem_shift_anisotropy = ChemShiftAnisotropySaveframe(self.data.datanodes)

        # Initialise Supergroup 6:  The kinetic data saveframe API.
        self.relaxation = Relaxation(self.data.datanodes)

        # Initialise Supergroup 7:  The thermodynamics saveframe API.
        self.model_free = ModelFreeSaveframe(self.data.datanodes)


    def read(self):
        """Read the data from a BMRB NMR-STAR formatted file."""

        # Read the contents of the STAR formatted file.
        self.data.read()


    def write(self):
        """Write the data to a BMRB NMR-STAR formatted file."""

        # Write the contents to the STAR formatted file.
        self.data.write()
