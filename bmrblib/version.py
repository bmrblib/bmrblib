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
