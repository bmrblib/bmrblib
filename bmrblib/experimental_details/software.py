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
"""The software saveframe category.

For example, see http://www.bmrb.wisc.edu/dictionary/3.1html_frame/frame_SaveFramePage.html#software
"""

# relax module imports.
from bmrblib.base_classes import BaseSaveframe, TagCategory, TagCategoryFree
from bmrblib.pystarlib.SaveFrame import SaveFrame
from bmrblib.pystarlib.TagTable import TagTable
from bmrblib.misc import translate


class SoftwareSaveframe(BaseSaveframe):
    """The software saveframe class."""

    # Class variables.
    sf_label = ['software']

    def __init__(self, datanodes):
        """Initialise the class, placing the pystarlib data nodes into the namespace.

        @param datanodes:   The pystarlib data nodes object.
        @type datanodes:    list
        """

        # Place the data nodes into the namespace.
        self.datanodes = datanodes

        # The number of software programs used.
        self.software_num = 0

        # Add the specific tag category objects.
        self.add_tag_categories()


    def add(self, name, version=None, vendor_name=None, vendor_address=None, vendor_eaddress=None, task=None, cite_ids=None):
        """Add the software info to the data nodes.

        @param name:                The name of the software program.
        @type name:                 str
        @keyword version:           The software version.
        @type version:              None or str
        @keyword vendor_name:       The vendor or developers of the software.
        @type vendor_name:          None or str
        @keyword vendor_address:    The vendor address.
        @type vendor_address:       None or str
        @keyword vendor_eaddress:   The vendor electronic address.
        @type vendor_eaddress:      None or str
        @keyword task:              The task of the software.
        @type task:                 str
        @keyword cite_ids:          The citation ID numbers.
        @type cite_ids:             None or list of int
        @return:                    The software ID number.
        @rtype:                     int
        """

        # Check.
        if not isinstance(task, list):
            raise NameError, "The task argument '%s' is invalid." % task

        # Place the args into the namespace.
        self.program_name = name
        self.program_version = translate(version)
        self.vendor_name = translate(vendor_name)
        self.vendor_address = translate(vendor_address)
        self.vendor_eaddress = translate(vendor_eaddress)
        self.task = translate(task)
        self.cite_ids = translate(cite_ids)

        # Increment the ID number.
        self.software_num = self.software_num + 1
        self.software_num_str = str(self.software_num)
        self.software_id_num = [str(translate(self.software_num))]

        # Initialise the save frame.
        self.frame = SaveFrame(title=self.program_name)

        # Create the tag categories.
        self.Software.create()
        self.Software_citation.create()
        self.Vendor.create()
        self.Task.create()

        # Add the saveframe to the data nodes.
        self.datanodes.append(self.frame)

        # Return the software ID number.
        return self.software_num


    def add_tag_categories(self):
        """Create the tag categories."""

        # The tag category objects.
        self.Software = Software(self)
        self.Software_citation = SoftwareCitation(self)
        self.Task = Task(self)
        self.Vendor = Vendor(self)



class Software(TagCategoryFree):
    """Base class for the Software tag category."""

    def __init__(self, sf):
        """Setup the Software tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(Software, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Software'

        # Database table names to class instance variables.
        self.data_to_var_name.append(['SoftwareID', 'software_num_str'])
        self.data_to_var_name.append(['Name',       'program_name'])
        self.data_to_var_name.append(['Version',    'program_version'])

        # Database table name to tag name.
        self.data_to_tag_name['SfCategory'] = 'Sf_category'
        self.data_to_tag_name['SoftwareID'] = 'ID'
        self.data_to_tag_name['Name'] = 'Name'
        self.data_to_tag_name['Version'] = 'Version'



class SoftwareCitation(TagCategory):
    """Base class for the SoftwareCitation tag category."""


    def __init__(self, sf):
        """Setup the SoftwareCitation tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(SoftwareCitation, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Software_citation'

        # Database table names to class instance variables.
        self.data_to_var_name.append(['CitationID',      'cite_ids'])
        self.data_to_var_name.append(['SoftwareID',      'software_id_num'])

        # Database table name to tag name.
        self.data_to_tag_name['CitationID'] = 'Citation_ID'
        self.data_to_tag_name['SoftwareID'] = 'Software_ID'



class Task(TagCategory):
    """Base class for the Task tag category."""

    def __init__(self, sf):
        """Setup the Task tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(Task, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Task'

        # Database table names to class instance variables.
        self.data_to_var_name.append(['Task',                'task'])
        self.data_to_var_name.append(['SoftwareID',          'software_id_num'])

        # Database table name to tag name.
        self.data_to_tag_name['Task'] = 'Task'
        self.data_to_tag_name['SoftwareID'] = 'SoftwareID'



class Vendor(TagCategory):
    """Base class for the Vendor tag category."""

    def __init__(self, sf):
        """Setup the Vendor tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(Vendor, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Vendor'

        # Database table names to class instance variables.
        self.data_to_var_name.append(['Name',                'vendor_name'])
        self.data_to_var_name.append(['Address',             'vendor_address'])
        self.data_to_var_name.append(['ElectronicAddress',   'vendor_eaddress'])
        self.data_to_var_name.append(['SoftwareID',          'software_id_num'])

        # Database table name to tag name.
        self.data_to_tag_name['Name'] = 'Name'
        self.data_to_tag_name['Address'] = 'Address'
        self.data_to_tag_name['ElectronicAddress'] = 'Electronic_address'
        self.data_to_tag_name['SoftwareID'] = 'SoftwareID'
