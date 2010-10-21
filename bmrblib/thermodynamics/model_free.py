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
"""The model_free saveframe category (used to be called order_parameters).

For example, see http://www.bmrb.wisc.edu/dictionary/3.1html_frame/frame_SaveFramePage.html#order_parameters
"""

# relax module imports.
from bmrblib.base_classes import BaseSaveframe, TagCategory, TagCategoryFree
from bmrblib.misc import no_missing, translate
from bmrblib.pystarlib.SaveFrame import SaveFrame
from bmrblib.pystarlib.TagTable import TagTable


class ModelFreeSaveframe(BaseSaveframe):
    """The Order parameters saveframe class."""

    # Class variables.
    sf_label = 'model_free'
    id = '1'
    name = 'S2_parameters'

    def __init__(self, datanodes):
        """Initialise the class, placing the pystarlib data nodes into the namespace.

        @param datanodes:   The pystarlib data nodes object.
        @type datanodes:    list
        """

        # Place the data nodes into the namespace.
        self.datanodes = datanodes

        # Add the specific tag category objects.
        self.add_tag_categories()


    def add(self, sample_label='$sample_1', sample_cond_list_id=None, sample_cond_list_label='$conditions_1', te_units='s', tf_units='s', ts_units='s', global_chi2=None, details=None, software_ids=None, software_labels=None, assembly_atom_ids=None, entity_assembly_ids=None, entity_ids=None, res_nums=None, res_names=None, atom_names=None, atom_types=None, isotope=None, local_tc=None, local_tc_err=None, s2=None, s2_err=None, s2f=None, s2f_err=None, s2s=None, s2s_err=None, te=None, te_err=None, tf=None, tf_err=None, ts=None, ts_err=None, rex=None, rex_err=None, rex_frq=None, chi2=None, model_fit=None):
        """Add model-free data to the data nodes.

        Note the te, tf, and ts units include the hidden radian unit as these are angular correlation times, e.g. the default of 's' is really 's/rad', the average time it take to rotate 1 radian.

        The model_free argument is a string describing the model used for the spin.  For no internal model-free motions, it can be one of:

            - ''
            - 'Rex'

        For the original Lipari-Szabo model-free motions (Lipari and Szabo, 1982), plus additional parameters such as Rex, model_fit can be one of:

            - 'S2'
            - 'S2, te'
            - 'S2, Rex'
            - 'S2, te, Rex'

        For the extended model-free motions (Clore et al., 1990), plus additional parameters such as Rex, model_fit can be one of:

            - 'S2f, S2, ts'
            - 'S2f, S2s, ts'
            - 'S2f, tf, S2, ts'
            - 'S2f, tf, S2s, ts'
            - 'S2f, S2, ts, Rex'
            - 'S2f, S2s, ts, Rex'
            - 'S2f, tf, S2, ts, Rex'
            - 'S2f, tf, S2s, ts, Rex'


        @keyword sample_label:              The sample label.
        @type sample_label:                 str
        @keyword sample_cond_list_id:       The sample conditions list ID number.
        @type sample_cond_list_id:          str
        @keyword sample_cond_list_label:    The sample conditions list label.
        @type sample_cond_list_label:       str
        @keyword te_units:                  The units of the te model-free parameters.
        @type te_units:                     str
        @keyword tf_units:                  The units of the tf model-free parameters.
        @type tf_units:                     str
        @keyword ts_units:                  The units of the ts model-free parameters.
        @type ts_units:                     str
        @keyword global_chi2:               The optimised global chi-squared value for the global model (the sum of the diffusion tensor together with the model-free models for all spins).
        @type global_chi2:                  None or float
        @keyword details:                   The details tag.
        @type details:                      str
        @keyword software_ids:              The software ID numbers for all software used in the model-free analysis.
        @type software_ids:                 list of int
        @keyword software_labels:           The names of all software used in the model-free analysis.
        @type software_labels:              list of str
        @keyword res_nums:                  The residue number for each spin.
        @keyword assembly_atom_ids:         The assembly atom ID numbers.
        @type assembly_atom_ids:            list of int
        @keyword entity_assembly_ids:       The entity assembly ID numbers.
        @type entity_assembly_ids:          list of int
        @keyword entity_ids:                The entity ID numbers.
        @type entity_ids:                   int
        @type res_nums:                     list of int
        @keyword res_names:                 The residue name for each spin.
        @type res_names:                    list of str
        @keyword atom_names:                The atom name for each spin.
        @type atom_names:                   list of str
        @keyword atom_types:                The atom types as IUPAC element abbreviations for each spin.
        @type atom_types:                   list of str
        @keyword isotope:                   The isotope type list, ie 15 for '15N'.
        @type isotope:                      list of int
        @keyword local_tc:                  The spin specific diffusional correlation time.
        @type local_tc:                     lost of float
        @keyword local_tc_err:              The spin specific diffusional correlation time errors.
        @type local_tc_err:                 lost of float
        @keyword s2:                        The S2 values for each spin.
        @type s2:                           list of float
        @keyword s2_err:                    The S2 errors for each spin.
        @type s2_err:                       list of float
        @keyword s2f:                       The S2f values for each spin.
        @type s2f:                          list of float
        @keyword s2f_err:                   The S2f errors for each spin.
        @type s2f_err:                      list of float
        @keyword s2s:                       The S2s values for each spin.
        @type s2s:                          list of float
        @keyword s2s_err:                   The S2s errors for each spin.
        @type s2s_err:                      list of float
        @keyword te:                        The te values for each spin (in rad/s units).
        @type te:                           list of float
        @keyword te_err:                    The te errors for each spin (in rad/s units).
        @type te_err:                       list of float
        @keyword tf:                        The tf values for each spin (in rad/s units).
        @type tf:                           list of float
        @keyword tf_err:                    The tf errors for each spin (in rad/s units).
        @type tf_err:                       list of float
        @keyword ts:                        The ts values for each spin (in rad/s units).
        @type ts:                           list of float
        @keyword ts_err:                    The ts errors for each spin (in rad/s units).
        @type ts_err:                       list of float
        @keyword rex:                       The Rex values for each spin (in rad/s units for the field strength specified in
                                            rex_frq).
        @type rex:                          list of float
        @keyword rex_err:                   The Rex errors for each spin (in rad/s units for the field strength specified in
                                            rex_frq).
        @type rex_err:                      list of float
        @keyword rex_frq:                   The 1H spectrometer frequency in Hz that the Rex values are reported
                                            in.
        @type rex_frq:                      float
        @keyword chi2:                      The optimised chi-squared values for each spin.  This should be none if the global model was optimised.
        @type chi2:                         None or list of float
        @keyword model_free:                The model-free model fit.
        @type model_free:                   str
        """

        # Check the ID info.
        no_missing(res_nums, 'residue numbers of the model-free data')
        no_missing(res_names, 'residue names of the model-free data')
        no_missing(atom_names, 'atom names of the model-free data')

        # The Rex frequency in MHz.
        if rex:
            # Check.
            if not rex_frq:
                raise NameError("The rex_frq arg must be supplied if the rex values are supplied.")

            # Convert to MHz.
            self.rex_frq = str(rex_frq / 1e6)

        # No Rex.
        else:
            self.rex_frq = None

        # Check the model.
        allowed_models = ['',
                          'Rex',
                          'S2',
                          'S2, te',
                          'S2, Rex',
                          'S2, te, Rex',
                          'S2f, S2, ts',
                          'S2f, S2s, ts',
                          'S2f, tf, S2, ts',
                          'S2f, tf, S2s, ts',
                          'S2f, S2, ts, Rex',
                          'S2f, S2s, ts, Rex',
                          'S2f, tf, S2, ts, Rex',
                          'S2f, tf, S2s, ts, Rex'
                          'tm',
                          'tm, Rex',
                          'tm, S2',
                          'tm, S2, te',
                          'tm, S2, Rex',
                          'tm, S2, te, Rex',
                          'tm, S2f, S2, ts',
                          'tm, S2f, S2s, ts',
                          'tm, S2f, tf, S2, ts',
                          'tm, S2f, tf, S2s, ts',
                          'tm, S2f, S2, ts, Rex',
                          'tm, S2f, S2s, ts, Rex',
                          'tm, S2f, tf, S2, ts, Rex',
                          'tm, S2f, tf, S2s, ts, Rex'
         ]
        for model in model_fit:
            if model not in allowed_models:
                raise NameError("The model-free model '%s' is unknown.  It must be one of %s." % (model_fit, allowed_models))

        # Place the args into the namespace.
        self.sample_label = sample_label
        self.sample_cond_list_id = translate(sample_cond_list_id)
        self.sample_cond_list_label = translate(sample_cond_list_label)
        self.te_units = translate(te_units)
        self.tf_units = translate(tf_units)
        self.ts_units = translate(ts_units)
        self.global_chi2 = translate(global_chi2)
        self.details = translate(details)
        self.software_ids = translate(software_ids)
        self.software_labels = translate(software_labels)

        # Number of elements.
        N = len(res_nums)

        # Convert and translate all the spin specific args.
        names = ['assembly_atom_ids', 'entity_assembly_ids', 'entity_ids', 'res_nums', 'res_names', 'atom_names', 'atom_types', 'isotope', 'local_tc', 'local_tc_err', 's2', 's2_err', 's2f', 's2f_err', 's2s', 's2s_err', 'te', 'te_err', 'tf', 'tf_err', 'ts', 'ts_err', 'rex', 'rex_err', 'chi2', 'model_fit']
        for name in names:
            # Get the object.
            obj = locals()[name]

            # None objects.
            if obj == None:
                obj = [None] * N

            # Check the length.
            if len(obj) != N:
                raise NameError("The number of elements in the '%s' arg does not match that of 'res_nums'." % name)

            # Place the args into the namespace, translating for BMRB.
            setattr(self, name, translate(obj))

        # The model-free ID number.
        self.model_free_id = translate([1] * len(self.software_ids))

        # The ID numbers.
        #self.generate_data_ids(N)

        # Initialise the save frame.
        self.frame = SaveFrame(title=self.sf_label)

        # Create the tag categories.
        self.model_free_list.create()
        self.model_free_experiment.create()
        self.model_free_software.create()
        self.model_free.create()

        # Add the saveframe to the data nodes.
        self.datanodes.append(self.frame)


    def add_tag_categories(self):
        """Create the v3.1 tag categories."""

        # The tag category objects.
        self.model_free_list = ModelFreeList(self)
        self.model_free_experiment = ModelFreeExperiment(self)
        self.model_free_software = ModelFreeSoftware(self)
        self.model_free = ModelFree(self)


class ModelFreeList(TagCategoryFree):
    """Base class for the ModelFreeList tag category."""

    # The category name.
    tag_category_label = None

    def __init__(self, sf):
        """Setup the ModelFreeList tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(ModelFreeList, self).__init__(sf)

        # Database table names to class instance variables.
        self.data_to_var_name.append(['ModelFreeListID',            'id'])
        self.data_to_var_name.append(['SampleConditionListID',      'sample_cond_list_id'])
        self.data_to_var_name.append(['SampleConditionListLabel',   'sample_cond_list_label'])
        self.data_to_var_name.append(['TaueValUnits',               'te_units'])
        self.data_to_var_name.append(['TaufValUnits',               'tf_units'])
        self.data_to_var_name.append(['TausValUnits',               'ts_units'])
        self.data_to_var_name.append(['GlobalChiSquaredFitVal',     'global_chi2'])
        self.data_to_var_name.append(['Details',                    'details'])

        # Database table name to tag name.
        self.data_to_tag_name['SfCategory'] =               'Saveframe_category'
        self.data_to_tag_name['SampleConditionListID'] =    'Sample_condition_list_ID'
        self.data_to_tag_name['SampleConditionListLabel'] = 'Sample_conditions_label'
        self.data_to_tag_name['TaueValUnits'] =             'Tau_e_val_units'
        self.data_to_tag_name['TaufValUnits'] =             'Tau_f_val_units'
        self.data_to_tag_name['TausValUnits'] =             'Tau_s_val_units'
        self.data_to_tag_name['GlobalChiSquaredFitVal'] =   'Global_chi_squared_fit_val'
        self.data_to_tag_name['Details'] =                  'Details'



class ModelFreeExperiment(TagCategory):
    """Base class for the ModelFreeExperiment tag category."""

    def __init__(self, sf):
        """Setup the ModelFreeExperiment tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(ModelFreeExperiment, self).__init__(sf)

        # Database table names to class instance variables.
        self.data_to_var_name.append(['SampleLabel', 'sample_label'])

        # Database table name to tag name.
        self.data_to_tag_name['SampleLabel'] = 'Sample_label'



class ModelFreeSoftware(TagCategory):
    """Base class for the ModelFreeSoftware tag category."""

    # The category name.
    tag_category_label = 'Model_free_software'

    def __init__(self, sf):
        """Setup the ModelFreeSoftware tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(ModelFreeSoftware, self).__init__(sf)

        # Database table names to class instance variables.
        self.data_to_var_name.append(['SoftwareID',      'software_ids'])
        self.data_to_var_name.append(['SoftwareLabel',   'software_labels'])
        self.data_to_var_name.append(['ModelFreeListID', 'model_free_id'])

        # Database table name to tag name.
        self.data_to_tag_name['SoftwareID'] =       'Software_ID'
        self.data_to_tag_name['SoftwareLabel'] =    'Software_label'
        self.data_to_tag_name['ModelFreeListID'] =  'Model_free_list_ID'



class ModelFree(TagCategory):
    """Base class for the ModelFree tag category."""

    def __init__(self, sf):
        """Setup the ModelFree tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(ModelFree, self).__init__(sf)

        # Database table names to class instance variables.
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
        self.data_to_var_name.append(['TauEVal',             'te'])
        self.data_to_var_name.append(['TauEValErr',          'te_err'])
        self.data_to_var_name.append(['TauFVal',             'tf'])
        self.data_to_var_name.append(['TauFValErr',          'tf_err'])
        self.data_to_var_name.append(['TauSVal',             'ts'])
        self.data_to_var_name.append(['TauSValErr',          'ts_err'])
        self.data_to_var_name.append(['RexVal',              'rex'])
        self.data_to_var_name.append(['RexValErr',           'rex_err'])
        self.data_to_var_name.append(['ChiSquaredVal',       'chi2'])

        # Database table name to tag name.
        self.data_to_tag_name['ModelFreeID'] =          None
        self.data_to_tag_name['AssemblyAtomID'] =       'Assembly_atom_ID'
        self.data_to_tag_name['EntityAssemblyID'] =     'Entity_assembly_ID'
        self.data_to_tag_name['EntityID'] =             'Entity_ID'
        self.data_to_tag_name['CompIndexID'] =          'Residue_seq_code'
        self.data_to_tag_name['CompID'] =               'Residue_label'
        self.data_to_tag_name['AtomID'] =               'Atom_name'
        self.data_to_tag_name['AtomType'] =             'Atom_type'
        self.data_to_tag_name['AtomIsotopeNumber'] =    'Atom_isotope_number'
        self.data_to_tag_name['S2Val'] =                'S2_value'
        self.data_to_tag_name['S2ValErr'] =             'S2_value_fit_error'
        self.data_to_tag_name['TauEVal'] =              'Tau_e_value'
        self.data_to_tag_name['TauEValErr'] =           'Tau_e_value_fit_error'
        self.data_to_tag_name['TauFVal'] =              'Tau_f_value'
        self.data_to_tag_name['TauFValErr'] =           'Tau_f_value_fit_error'
        self.data_to_tag_name['TauSVal'] =              'Tau_s_value'
        self.data_to_tag_name['TauSValErr'] =           'Tau_s_value_fit_error'
        self.data_to_tag_name['RexVal'] =               None
        self.data_to_tag_name['RexValErr'] =            None
        self.data_to_tag_name['S2fVal'] =               'S2f_value'
        self.data_to_tag_name['S2fValErr'] =            'S2f_value_fit_error'
        self.data_to_tag_name['S2sVal'] =               'S2s_value'
        self.data_to_tag_name['S2sValErr'] =            'S2s_value_fit_error'
        self.data_to_tag_name['ChiSquaredVal'] =        'SSE_val'
        self.data_to_tag_name['ModelFit'] =             'Model_fit'
