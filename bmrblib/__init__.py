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

# Python module imports.
from os import F_OK, access
from re import search
from string import split
from sys import stdout

# Bmrblib module imports.
from nmr_star_dict_v2_1 import NMR_STAR_v2_1
from nmr_star_dict_v3_1 import NMR_STAR_v3_1
from version import Star_version


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

    # Determine the version.
    if not version and access(file_path, F_OK):
        version = determine_version(file_path)

    # The default version.
    if not version:
        version = '3.1'

    # Store the version in the singleton.
    star_version = Star_version()
    star_version.version = version

    # Determine the major, minor, and revision numbers.
    star_version.major, star_version.minor, star_version.revision = parse_version(version)

    # Print out.
    stdout.write("NMR-STAR version %s.%s.%s\n" % (star_version.major, star_version.minor, star_version.revision))

    # Initialise the NMR-STAR data object.
    if star_version.major == 3:
        star = NMR_STAR_v3_1('relax_model_free_results', file_path)
    elif star_version.major == 2:
        star = NMR_STAR_v2_1('relax_model_free_results', file_path)
    else:
        raise NameError("The NMR-STAR version %s is unknown." % star_version.version)

    # Return the object.
    return star


def determine_version(file_path):
    """Determine the version of the given NMR-STAR file.

    @param file_path:   The full file path.
    @type file_path:    str
    @return:            The NMR-STAR version number.
    @rtype:             str
    """

    # Read the file.
    file = open(file_path)
    lines = file.readlines()
    file.close()

    # Loop over the lines of the file.
    for line in lines:
        # Find the version line.
        if search('\.NMR_STAR_version', line) or search('_NMR_STAR_version', line):
            # Split the line.
            row = split(line)

            # Return the version number.
            return row[1]


def parse_version(version):
    """Convert the version number string into the major, minor, and revision numbers.

    @param version: The version number.
    @type version:  str
    @return:        The major, minor, and revision numbers.
    @rtype:         tuple of int
    """

    # Split up the number.
    nums = split(version, '.')

    # The major and minor numbers.
    major = int(nums[0])
    minor = int(nums[1])

    # The revision number.
    if len(nums) == 3:
        revision = int(nums[2])
    else:
        revision = 0

    # Return the numbers.
    return major, minor, revision
