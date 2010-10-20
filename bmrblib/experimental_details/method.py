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
"""The method saveframe category.

For example, see http://www.bmrb.wisc.edu/dictionary/3.1html_frame/frame_SaveFramePage.html#method
"""

# relax module imports.
from bmrblib.base_classes import BaseSaveframe, TagCategory, TagCategoryFree
from bmrblib.pystarlib.SaveFrame import SaveFrame
from bmrblib.pystarlib.TagTable import TagTable
from bmrblib.misc import no_missing, translate


class MethodSaveframe(BaseSaveframe):
    """The method saveframe class."""

    # Class variables.
    sf_label = 'method'

    def __init__(self, datanodes):
        """Initialise the class, placing the pystarlib data nodes into the namespace.

        @param datanodes:   The pystarlib data nodes object.
        @type datanodes:    list
        """

        # Place the data nodes into the namespace.
        self.datanodes = datanodes

        # The number of methods used.
        self.method_num = 0

        # Add the specific tag category objects.
        self.add_tag_categories()


    def add(self, name=None, details=None, cite_ids=None, file_name=None, file_text=None, param_file_name=None, param_file_text=None):
        """Add the method info to the data nodes.

        @keyword name:              The unique name describing this method.
        @type name:                 str
        @keyword details:           Text description providing additional information about the reported method.
        @type details:              None or str
        @keyword cite_ids:          The citation ID numbers.
        @type cite_ids:             None or list of int
        @keyword file_name:         The name of the file containing the source code or protocol for the reported method.
        @type file_name:            str
        @keyword file_text:         The method provided as an ASCII text document that is included in the NMR-STAR file.
        @type file_text:            str
        @keyword param_file_name:   The name of the file that contains parameters required to execute the method.
        @type param_file_name:      None or str
        @keyword param_file_text:   The text of the parameter file.
        @type param_file_text:      None or str
        """

        # Check that nothing is missing.
        no_missing(name, 'method name')
        no_missing(file_name, 'file name')
        no_missing(file_text, 'file text')

        # Check.
        if not isinstance(cite_ids, list):
            raise NameError, "The cite_ids argument '%s' should be a list." % cite_ids

        # Place the args into the namespace.
        self.method_name = name
        self.details = translate(details)
        self.cite_ids = translate(cite_ids)
        self.file_name = translate(file_name)
        self.file_text = translate(file_text)
        self.param_file_name = translate(param_file_name)
        self.param_file_text = translate(param_file_text)

        # The text format.
        self.text_format = '?'

        # Increment the ID number.
        self.method_num = self.method_num + 1
        self.method_num_str = str(self.method_num)
        self.method_id_num = [str(translate(self.method_num))]

        # Initialise the save frame.
        self.frame = SaveFrame(title='method')

        # Create the tag categories.
        self.Method.create()
        if len(self.cite_ids):
            self.Method_citation.create()
        self.Method_file.create()
        self.Method_parameter_file.create()

        # Add the saveframe to the data nodes.
        self.datanodes.append(self.frame)


    def add_tag_categories(self):
        """Create the tag categories."""

        # The tag category objects.
        self.Method = Method(self)
        self.Method_citation = MethodCitation(self)
        self.Method_file = MethodFile(self)
        self.Method_parameter_file = MethodParam(self)



class Method(TagCategoryFree):
    """Base class for the Method tag category."""

    def __init__(self, sf):
        """Setup the Method tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(Method, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Method'

        # Database table names to class instance variables.
        self.data_to_var_name.append(['SfFramecode',    'method_name'])
        self.data_to_var_name.append(['MethodID',       'method_num_str'])
        self.data_to_var_name.append(['Details',        'details'])

        # Database table name to tag name.
        self.data_to_tag_name['SfCategory'] =   'Sf_category'
        self.data_to_tag_name['SfFramecode'] =  'Sf_framecode'
        self.data_to_tag_name['MethodID'] =     'ID'
        self.data_to_tag_name['Details'] =      'Details'



class MethodCitation(TagCategory):
    """Base class for the MethodCitation tag category."""

    def __init__(self, sf):
        """Setup the MethodCitation tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(MethodCitation, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Method_citation'

        # Database table names to class instance variables.
        self.data_to_var_name.append(['CitationID',      'cite_ids'])
        self.data_to_var_name.append(['MethodID',        'method_id_num'])

        # Database table name to tag name.
        self.data_to_tag_name['CitationID'] =   'Citation_ID'
        self.data_to_tag_name['MethodID'] =     'Method_ID'



class MethodFile(TagCategory):
    """Base class for the MethodFile tag category."""

    def __init__(self, sf):
        """Setup the MethodFile tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(MethodFile, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Method_file'

        # Database table names to class instance variables.
        self.data_to_var_name.append(['Name',                'file_name'])
        self.data_to_var_name.append(['TextFormat',          'text_format'])
        self.data_to_var_name.append(['Text',                'file_text'])
        self.data_to_var_name.append(['MethodID',            'method_id_num'])

        # Database table name to tag name.
        self.data_to_tag_name['Name'] =        'Name'
        self.data_to_tag_name['TextFormat'] =  'Text_format'
        self.data_to_tag_name['Text'] =        'Text'
        self.data_to_tag_name['MethodID'] =    'Method_ID'



class MethodParam(TagCategory):
    """Base class for the MethodParam tag category."""

    def __init__(self, sf):
        """Setup the MethodParam tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(MethodParam, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Method_param'

        # Database table names to class instance variables.
        self.data_to_var_name.append(['FileName',            'param_file_name'])
        self.data_to_var_name.append(['TextFormat',          'text_format'])
        self.data_to_var_name.append(['Text',                'param_file_text'])
        self.data_to_var_name.append(['MethodID',            'method_id_num'])

        # Database table name to tag name.
        self.data_to_tag_name['FileName'] =    'File_name'
        self.data_to_tag_name['TextFormat'] =  'Text_format'
        self.data_to_tag_name['Text'] =        'Text'
        self.data_to_tag_name['MethodID'] =    'Method_ID'
