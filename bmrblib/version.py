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
"""The NMR-STAR version singleton object."""

# Python module imports.
from re import search
from string import split


class Star_version(object):
    """A singleton for storing the NMR-STAR version information."""

    # Class variable for storing the class instance.
    instance = None

    def __new__(self, *args, **kargs):
        """Replacement function for implementing the singleton design pattern."""

        # First initialisation.
        if self.instance is None:
            self.instance = object.__new__(self, *args, **kargs)

        # Already initialised, so return the instance.
        return self.instance


    def set_version(self, version):
        """Set the version number and extract the major, minor and revision numbers.

        @param version: The NMR-STAR version number.
        @type version:  str
        """

        # Store the number.
        self.version = version

        # Determine the major, minor, and revision numbers.
        self.parse_version()


    def parse_version(self):
        """Convert the version number string into the major, minor, and revision numbers.

        @param version: The version number.
        @type version:  str
        """

        # Initialise.
        self.major = None
        self.minor = None
        self.revision = None

        # Split up the number.
        nums = split(self.version, '.')

        # Catch development versions.
        if search('^Dev', self.version):
            # Assume a version 2.1 file.
            self.major = 2
            self.minor = 1

            # Quit.
            return

        # A production tag is in the version string.
        if nums[0] == 'production':
            nums.pop(0)

        # The major and minor numbers.
        self.major = int(nums[0])
        self.minor = int(nums[1])

        # The revision number.
        if len(nums) == 3:
            self.revision = int(nums[2])
        else:
            self.revision = 0