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
"""The TagCategory base class."""

# relax module imports.
from bmrblib.misc import translate
from bmrblib.pystarlib.TagTable import TagTable


class BaseSaveframe:
    """The base class for the saveframe classes."""

    def extract_data(self, datanode):
        """Read all the tensor tags from the datanodes.

        @keyword datanode:  The tensor datanode.
        @type datanode:     Datanode instance
        @return:            The tensor data.
        @rtype:             tuple
        """

        # Loop over the tag categories.
        for i in range(len(self.tag_categories)):
            # Extract the data.
            self.tag_categories[i].extract_tag_data(datanode.tagtables[i])


    def generate_data_ids(self, N):
        """Generate the data ID structure.

        @keyword N: The number of data points.
        @type N:    int
        """

        # The data ID values.
        self.data_ids = translate(range(1, N+1))


    def loop(self):
        """Loop over the saveframes, yielding the data.

        @return:    The saveframe data.
        @rtype:     tuple
        """

        # Set up the tag information.
        for i in range(len(self.tag_categories)):
            self.tag_categories[i].tag_setup()

        # Get the saveframe name.
        sf_name = getattr(self, 'sf_label')

        # Loop over all datanodes.
        for datanode in self.datanodes:
            # Find the saveframes via the SfCategory tag index.
            found = False
            for index in range(len(datanode.tagtables[0].tagnames)):
                # First match the tag names.
                if datanode.tagtables[0].tagnames[index] == self.tag_categories[0].data_to_tag_name_full['SfCategory']:
                    # Then the tag value.
                    if datanode.tagtables[0].tagvalues[index][0] == sf_name:
                        found = True
                        break

            # Skip the datanode.
            if not found:
                continue

            # Extract the information.
            self.extract_data(datanode)

            # Return the saveframe info.
            yield self.read()



class TagCategory(object):
    """The base class for tag category classes."""

    # The category name.
    tag_category_label = None

    # The base category is not free.
    free = False

    def __init__(self, sf):
        """Initialise the tag category object, placing the saveframe into its namespace.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Place the saveframe and tag info into the namespace.
        self.sf = sf

        # The translation tables.
        self.data_to_var_name = []
        self.data_to_tag_name = {}
        self.data_to_tag_name_full = {}

        # The specific variables dictionary.
        self.variables = {}

        # The tag category name.
        self.tag_category_label = None


    def create(self):
        """Create the TensorList tag category."""

        # Set up the tag information.
        self.tag_setup()

        # Create the TabTable.
        table = self.create_tag_table(self.data_to_var_name, free=self.free)

        # Add the tagtable to the save frame.
        self.sf.frame.tagtables.append(table)


    def create_full_tag_names(self):
        """Generate the full NMR-STAR tag names."""

        # Loop over each tag name.
        for key, name in self.data_to_tag_name.items():
            self.data_to_tag_name_full[key] = self.tag_category_label_full + name


    def create_tag_table(self, info, free=False):
        """Create and return a tag table based on the info structure.

        @param info:    The key and object pair list.  This consists of the keys of
                        self.data_to_tag_name being the first element and the names of the objects being
                        the second element, both of the second dimension.  The fist dimension are
                        the different pairs.
        @type info:     list of list of str
        @keyword free:  Flag to create a free STAR table.
        @type free:     bool
        @return:        The tag table.
        @rtype:         TagTable instance
        """

        # Init.
        keys = list(self.data_to_tag_name.keys())
        data_to_tag_name = []
        tag_values = []

        # Loop over the keys and object names of the info structure.
        for key, name in info:
            # Key check.
            if key not in keys:
                raise NameError("The key '%s' is not located in the self.data_to_tag_name structure." % key)

            # The tag names and values (skipping empty entries in self.data_to_tag_name).
            if self.data_to_tag_name[key] != None:
                # The name.
                data_to_tag_name.append(self.data_to_tag_name_full[key])

                # The value.
                val = getattr(self.sf, name)

                # Convert to a list, if necessary.
                if not isinstance(val, list):
                    val = [val]

                # Append the value list.
                tag_values.append(val)

        # Check the input data to avoid cryptic pystarlib error messages.
        N = len(tag_values[0])
        for i in range(len(tag_values)):
            if len(tag_values[i]) > N:
                # Mismatch.
                if N != 1:
                    raise NameError("The tag values are not all the same length '%s'." % tag_values)

                # First element was single.
                N = len(tag_values[i])

        # Fix the single values if the other data are lists.
        for i in range(len(tag_values)):
            if len(tag_values[i]) == 1:
                tag_values[i] = tag_values[i] * N

        # Add the data and return the table.
        return TagTable(free=free, tagnames=data_to_tag_name, tagvalues=tag_values)


    def extract_tag_data(self, tagtable):
        """Extract all of the tag data from the tagtable, placing it into the designated variable names.

        @param tagtable:    The Tensor tagtable.
        @type tagtable:     Tagtable instance
        """

        # Loop over the variables.
        for i in range(len(self.data_to_var_name)):
            # The database table name.
            table_name = self.data_to_var_name[i][0]

            # The variable name.
            var_name = self.data_to_var_name[i][1]

            # The full tag name.
            full_tag_name = self.data_to_tag_name_full[table_name]

            # The data.
            data = tagtable.tagvalues[tagtable.tagnames.index(full_tag_name)]

            # Set the data.
            setattr(self.sf, var_name, data)


    def tag_setup(self, tag_category_label=None, sep=None):
        """Setup the tag names.

        @keyword tag_category_label:    The tag name prefix specific for the tag category.
        @type tag_category_label:       None or str
        @keyword sep:                   The string separating the tag name prefix and suffix.
        @type sep:                      str
        """

        # Place the args into the class namespace.
        if tag_category_label:
            self.tag_category_label = tag_category_label
        if sep:
            self.sep = sep
        else:
            self.sep = '.'

        # Create the full tag label.
        self.tag_category_label_full = '_'
        if self.tag_category_label:
            self.tag_category_label_full = self.tag_category_label_full + self.tag_category_label + self.sep

        # Generate the full tag names.
        self.create_full_tag_names()



class TagCategoryFree(TagCategory):

    # The base category is free.
    free = True

    def __init__(self, sf):
        """Setup the TagCategoryFree tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(TagCategoryFree, self).__init__(sf)

        # Database table names to class instance variables.
        self.data_to_var_name.append(['SfCategory',         'sf_label'])
