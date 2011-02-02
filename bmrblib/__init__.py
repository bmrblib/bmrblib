#############################################################################
#                                                                           #
# The BMRB library.                                                         #
#                                                                           #
# Copyright (C) 2008-2011 Edward d'Auvergne                                 #
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
"""Package for interfacing with the BMRB (http://www.bmrb.wisc.edu/) by handling NMR-STAR formatted files."""

# The list of all modules and packages.
__all__ = ['base_classes',
           'misc',
           'nmr_star_dict',
           'nmr_star_dict_v2_1',
           'nmr_star_dict_v3_1']

# Module imports.
from nmr_star_dict_v2_1 import NMR_STAR_v2_1
from nmr_star_dict_v3_1 import NMR_STAR_v3_1


def create_nmr_star(title, file_path, version=None):
    """Initialise the NMR-STAR object.

    @param title:       The title of the NMR-STAR data.
    @type title:        str
    @param file_path:   The full file path.
    @type file_path:    str
    @keyword version:   The NMR-STAR version to use.
    @type version:      str
    @return:            The NMR-STAR python object.
    @rtype:             class instance
    """

    # Initialise the NMR-STAR data object.
    if version == '3.1':
        star = NMR_STAR_v3_1('relax_model_free_results', file_path)
    elif version == '2.1':
        star = NMR_STAR_v2_1('relax_model_free_results', file_path)
    else:
        raise NameError("The NMR-STAR version %s is unknown." % version)

    # Return the object.
    return star
