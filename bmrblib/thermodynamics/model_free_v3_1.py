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
"""The v3.1 Heteronuclear NOE data saveframe category.

See http://www.bmrb.wisc.edu/dictionary/3.1html/SaveFramePage.html#heteronucl_NOEs.
"""

# relax module imports.
from bmrblib.thermodynamics.model_free import ModelFreeSaveframe, ModelFreeList, ModelFreeExperiment, ModelFreeSoftware, ModelFree


class ModelFreeSaveframe_v3_1(ModelFreeSaveframe):
    """The v3.1 Model_free data saveframe class."""

    def add_tag_categories(self):
        """Create the v3.1 tag categories."""

        # The tag category objects.
        self.model_free_list = ModelFreeList_v3_1(self)
        self.model_free_experiment = ModelFreeExperiment_v3_1(self)
        self.model_free_software = ModelFreeSoftware_v3_1(self)
        self.model_free = ModelFree_v3_1(self)

    def specific_setup(self):
        """Method called by self.add() to set up any version specific data."""

        self.cat_name = ['order_parameters']



class ModelFreeList_v3_1(ModelFreeList):
    """v3.1 ModelFreeList tag category."""

    def __init__(self, sf):
        """Setup the ModelFreeList_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(ModelFreeList_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Model_free_list'

        # Database table name to tag name.
        self.data_to_tag_name['SfCategory'] =               'Sf_category'
        self.data_to_tag_name['ModelFreeListID'] =          'ID'
        self.data_to_tag_name['SampleConditionListLabel'] = 'Sample_condition_list_label'



class ModelFreeExperiment_v3_1(ModelFreeExperiment):
    """v3.1 ModelFreeExperiment tag category."""

    def __init__(self, sf):
        """Setup the ModelFreeExperiment_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(ModelFreeExperiment_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Model_free_list'



class ModelFreeSoftware_v3_1(ModelFreeSoftware):
    """v3.1 ModelFreeSoftware tag category."""

    def __init__(self, sf):
        """Setup the ModelFreeSoftware_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(ModelFreeSoftware_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Model_free_software'



class ModelFree_v3_1(ModelFree):
    """v3.1 ModelFree tag category."""

    def __init__(self, sf):
        """Setup the ModelFree_v3_1 tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(ModelFree_v3_1, self).__init__(sf)

        # The category name.
        self.tag_category_label = 'Model_free'

        # Database table names to class instance variables.
        self.data_to_var_name = []
        self.data_to_var_name.append(['ModelFreeID',         'data_ids'])
        self.data_to_var_name.append(['AssemblyAtomID',      'assembly_atom_ids'])
        self.data_to_var_name.append(['EntityAssemblyID',    'entity_assembly_ids'])
        self.data_to_var_name.append(['EntityID',            'entity_ids'])
        self.data_to_var_name.append(['CompIndexID',         'res_nums'])
        self.data_to_var_name.append(['CompID',              'res_names'])
        self.data_to_var_name.append(['AtomID',              'atom_names'])
        self.data_to_var_name.append(['AtomType',            'atom_types'])
        self.data_to_var_name.append(['AtomIsotopeNumber',   'isotope'])
        self.data_to_var_name.append(['S2Val',               's2'])
        self.data_to_var_name.append(['S2ValErr',            's2_err'])
        self.data_to_var_name.append(['S2fVal',              's2f'])
        self.data_to_var_name.append(['S2fValErr',           's2f_err'])
        self.data_to_var_name.append(['S2sVal',              's2s'])
        self.data_to_var_name.append(['S2sValErr',           's2s_err'])
        self.data_to_var_name.append(['LocalTauCVal',        'local_tc'])
        self.data_to_var_name.append(['LocalTauCValErr',     'local_tc_err'])
        self.data_to_var_name.append(['TauEVal',             'te'])
        self.data_to_var_name.append(['TauEValErr',          'te_err'])
        self.data_to_var_name.append(['TauFVal',             'tf'])
        self.data_to_var_name.append(['TauFValErr',          'tf_err'])
        self.data_to_var_name.append(['TauSVal',             'ts'])
        self.data_to_var_name.append(['TauSValErr',          'ts_err'])
        self.data_to_var_name.append(['RexVal',              'rex'])
        self.data_to_var_name.append(['RexValErr',           'rex_err'])
        self.data_to_var_name.append(['ChiSquaredVal',       'chi2'])
        self.data_to_var_name.append(['ModelFit',            'model_fit'])

        # Database table name to tag name.
        self.data_to_tag_name['ModelFreeID'] =       'ID'
        self.data_to_tag_name['AssemblyAtomID'] =    'Assembly_atom_ID'
        self.data_to_tag_name['EntityAssemblyID'] =  'Entity_assembly_ID'
        self.data_to_tag_name['EntityID'] =          'Entity_ID'
        self.data_to_tag_name['CompIndexID'] =       'Comp_index_ID'
        self.data_to_tag_name['CompID'] =            'Comp_ID'
        self.data_to_tag_name['AtomID'] =            'Obs_atom_ID'
        self.data_to_tag_name['AtomType'] =          'Obs_atom_type'
        self.data_to_tag_name['AtomIsotopeNumber'] = 'Obs_atom_isotope_number'
        self.data_to_tag_name['S2Val'] =             'S2_val'
        self.data_to_tag_name['S2ValErr'] =          'S2_val_err'
        self.data_to_tag_name['S2fVal'] =            'S2f_val'
        self.data_to_tag_name['S2fValErr'] =         'S2f_val_err'
        self.data_to_tag_name['S2sVal'] =            'S2s_val'
        self.data_to_tag_name['S2sValErr'] =         'S2s_val_err'
        self.data_to_tag_name['LocalTauCVal'] =      'Local_tau_c_val'
        self.data_to_tag_name['LocalTauCValErr'] =   'Local_tau_c_val_err'
        self.data_to_tag_name['TauEVal'] =           'Tau_e_val'
        self.data_to_tag_name['TauEValErr'] =        'Tau_e_val_err'
        self.data_to_tag_name['TauFVal'] =           'Tau_f_val'
        self.data_to_tag_name['TauFValErr'] =        'Tau_f_val_err'
        self.data_to_tag_name['TauSVal'] =           'Tau_s_val'
        self.data_to_tag_name['TauSValErr'] =        'Tau_s_val_err'
        self.data_to_tag_name['RexVal'] =            'Rex_val'
        self.data_to_tag_name['RexValErr'] =         'Rex_val_err'
        self.data_to_tag_name['ChiSquaredVal'] =     'Chi_squared_val'
