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
"""The tensor saveframe category.

For example, see http://www.bmrb.wisc.edu/dictionary/3.1html_frame/frame_SaveFramePage.html#tensor
"""

# Python module imports.
from numpy import array

# relax module imports.
from bmrblib.base_classes import BaseSaveframe, TagCategory, TagCategoryFree
from bmrblib.misc import no_missing, translate
from bmrblib.pystarlib.SaveFrame import SaveFrame
from bmrblib.pystarlib.TagTable import TagTable


class TensorSaveframe(BaseSaveframe):
    """The tensor saveframe class."""

    # Saveframe variables.
    sf_label = 'tensor'

    def add(self, tensor_type=None, geometric_shape=None, tensor_symmetry=None, euler_type=None, matrix_val_units=None, angle_units=None, iso_val_formula=None, aniso_val_formula=None, rhomb_val_formula=None, data_file_name=None, details=None, assembly_atom_ids=None, entity_assembly_ids=None, entity_ids=None, res_nums=None, seq_id=None, res_names=None, atom_names=None, atom_types=None, isotope=None, axial_sym_axis_polar_angle=None, axial_sym_axis_azimuthal_angle=None, iso_val=None, aniso_val=None, rhombic_val=None, euler_alpha=None, euler_beta=None, euler_gamma=None, iso_comp_11=None, iso_comp_22=None, iso_comp_33=None, antisym_comp_12=None, antisym_comp_13=None, antisym_comp_23=None, full_tensor=None):
        """Add relaxation data to the data nodes.

        @keyword tensor_type:                       The type of rank-2 tensor.  This can be one of 'diffusion', 'alignment', 'CS', or 'Saupe'.
        @type tensor_type:                          None or str
        @keyword geometric_shape:                   The geometric shape of the rank-2 tensor.  This can be one of 'sphere', 'spheroid', 'oblate spheroid', 'prolate spheroid', or 'ellipsoid'.
        @type geometric_shape:                      None or str
        @keyword tensor_symmetry:                   The symmetry of the rank-2 tensor.  This can be one of 'isotropic', 'axial symmetry', 'oblate axial symmetry', 'prolate axial symmetry', or 'rhombic'.
        @type tensor_symmetry:                      None or str
        @keyword euler_type:                        The Euler angle definition.  I.e. 'xyx', 'zyz', 'zxz', 'ZYZ', etc.
        @type euler_type:                           None or str
        @keyword matrix_val_units:                  The units of the matrix values.  Can be 's-1', 'ppm', etc.
        @type matrix_val_units:                     None or str
        @keyword angle_units:                       The units of the angles.  Either 'rad' or 'deg'.
        @type angle_units:                          None or str
        @keyword iso_val_formula:                   The formula for the isotropic value.  For example, 'Diso = 1/(6.tm)'.
        @type iso_val_formula:                      None or str
        @keyword aniso_val_formula:                 The formula for the anisotropic value.  For example, 'Da = Dpar - Dper'.
        @type aniso_val_formula:                    None or str
        @keyword rhomb_val_formula:                 The formula for the rhombic value.  For example, 'Dr = (Dy - Dx)/2Da'.
        @type rhomb_val_formula:                    None or str
        @keyword data_file_name:                    The name of the data file submitted with the deposition containing this data (should probably be left to None).
        @type data_file_name:                       None or str
        @keyword details:                           The details tag.
        @type details:                              None or str
        @keyword assembly_atom_ids:                 The assembly atom ID numbers.
        @type assembly_atom_ids:                    list of int
        @keyword entity_assembly_ids:               The entity assembly ID numbers.
        @type entity_assembly_ids:                  list of int
        @keyword entity_ids:                        The entity ID numbers.
        @type entity_ids:                           int
        @keyword res_nums:                          The residue number list.
        @type res_nums:                             list of int
        @keyword res_names:                         The residue name list.
        @type res_names:                            list of str
        @keyword atom_names:                        The atom name list.
        @type atom_names:                           list of str
        @keyword atom_types:                        The atom types as IUPAC element abbreviations.
        @type atom_types:                           list of str
        @keyword isotope:                           The isotope type list, ie 15 for '15N'.
        @type isotope:                              list of int
        @keyword axial_sym_axis_polar_angle:        The polar angle for the axial symmetry axis.
        @type axial_sym_axis_polar_angle:           None or float
        @keyword axial_sym_axis_azimuthal_angle:    The azimuthal angle for the axial symmetry axis.
        @type axial_sym_axis_azimuthal_angle:       None or float
        @keyword iso_val:                           The isotropic value of the tensor.
        @type iso_val:                              None or float
        @keyword aniso_val:                         The anisotropic value of the tensor.
        @type aniso_val:                            None or float
        @keyword rhombic_val:                       The rhombic value of the tensor.
        @type rhombic_val:                          None or float
        @keyword euler_alpha:                       The alpha Euler angle for an ellipsoidal tensor.
        @type euler_alpha:                          None or float
        @keyword euler_beta:                        The beta Euler angle for an ellipsoidal tensor.
        @type euler_beta:                           None or float
        @keyword euler_gamma:                       The gamma Euler angle for an ellipsoidal tensor.
        @type euler_gamma:                          None or float
        @keyword iso_comp_11:                       By the standard convention, the value of the 1_1 element of the isotropic component of the chemical shielding tensor.
        @type iso_comp_11:                          None or float
        @keyword iso_comp_22:                       By the standard convention, the value of the 2_2 element of the isotropic component of the chemical shielding tensor.
        @type iso_comp_22:                          None or float
        @keyword iso_comp_33:                       By the standard convention, the value of the 3_3 element of the isotropic component of the chemical shielding tensor.
        @type iso_comp_33:                          None or float
        @keyword antisym_comp_12:                   The value for the 1_2 element of the anti-symmetric component of the chemical shielding tensor.
        @type antisym_comp_12:                      None or float
        @keyword antisym_comp_13:                   The value for the 1_3 element of the anti-symmetric component of the chemical shielding tensor.
        @type antisym_comp_13:                      None or float
        @keyword antisym_comp_23:                   The value for the 2_3 element of the anti-symmetric component of the chemical shielding tensor.
        @type antisym_comp_23:                      None or float
        @keyword full_tensor:                       The full tensor in 3D, rank-2 form
        @type full_tensor:                          list of lists or numpy array
        """

        # Check the ID info.
        no_missing(entity_ids, 'entity ID numbers')
        no_missing(res_nums, 'residue numbers')
        no_missing(res_names, 'residue names')
        no_missing(atom_names, 'atom names')

        # Check the tensor shape.
        allowed = ['sphere', 'spheroid', 'oblate spheroid', 'prolate spheroid', 'ellipsoid']
        if geometric_shape not in allowed:
            raise NameError("The geometric tensor shape of '%s' must be one of %s." % (geometric_shape, allowed))

        # Check the tensor symmetry.
        allowed = ['isotropic', 'anisotropic', 'axial symmetry', 'oblate axial symmetry', 'prolate axial symmetry', 'rhombic']
        if tensor_symmetry not in allowed:
            raise NameError("The tensor symmetry of '%s' must be one of %s." % (tensor_symmetry, allowed))

        # Check the angle units.
        angle_allowed = [None, 'deg', 'rad']
        if angle_units not in angle_allowed:
            raise NameError("The angle units of '%s' must be one of %s." % (angle_units, angle_allowed))

        # Check the full tensor.
        if full_tensor == None or len(full_tensor) != 3 or len(full_tensor[0]) != 3:
            raise NameError("The full tensor '%s' must be in 3D, rank-2 form." % full_tensor)

        # The number of elements.
        N = len(res_nums)

        # Place the args into the namespace.
        self.tensor_type = translate(tensor_type)
        self.geometric_shape = geometric_shape
        self.tensor_symmetry = tensor_symmetry
        self.euler_type = translate(euler_type)
        self.matrix_val_units = translate(matrix_val_units)
        self.angle_units = translate(angle_units)
        self.iso_val_formula = translate(iso_val_formula)
        self.aniso_val_formula = translate(aniso_val_formula)
        self.rhomb_val_formula = translate(rhomb_val_formula)
        self.file_name = translate(data_file_name)
        self.details = translate(details)
        self.res_nums = translate(res_nums)
        self.res_names = translate(res_names)
        self.atom_names = translate(atom_names)
        self.atom_types = translate(atom_types)
        self.isotope = translate(isotope)
        self.axial_sym_axis_polar_angle = translate(axial_sym_axis_polar_angle)
        self.axial_sym_axis_azimuthal_angle = translate(axial_sym_axis_azimuthal_angle)
        self.iso_val = translate(iso_val)
        self.aniso_val = translate(aniso_val)
        self.rhombic_val = translate(rhombic_val)
        self.euler_alpha = translate(euler_alpha)
        self.euler_beta = translate(euler_beta)
        self.euler_gamma = translate(euler_gamma)
        self.iso_comp_11 = translate(iso_comp_11)
        self.iso_comp_22 = translate(iso_comp_22)
        self.iso_comp_33 = translate(iso_comp_33)
        self.antisym_comp_12 = translate(antisym_comp_12)
        self.antisym_comp_13 = translate(antisym_comp_13)
        self.antisym_comp_23 = translate(antisym_comp_23)

        # Break up the full tensor.
        full_tensor = array(full_tensor)
        self.tensor_11 = translate(full_tensor[0, 0])
        self.tensor_12 = translate(full_tensor[0, 1])
        self.tensor_13 = translate(full_tensor[0, 2])
        self.tensor_21 = translate(full_tensor[1, 0])
        self.tensor_22 = translate(full_tensor[1, 1])
        self.tensor_23 = translate(full_tensor[1, 2])
        self.tensor_31 = translate(full_tensor[2, 0])
        self.tensor_32 = translate(full_tensor[2, 1])
        self.tensor_33 = translate(full_tensor[2, 2])

        # Convert to lists and check the lengths.
        for name in ['assembly_atom_ids', 'entity_assembly_ids', 'entity_ids', 'res_nums', 'seq_id', 'res_names', 'atom_names', 'atom_types', 'isotope']:
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

        # Set up the tensor specific variables.
        self.count = self.count + 1
        self.count_str = str(self.count)
        self.count_list = translate([self.count] * N)
        self.generate_data_ids(N)

        # Initialise the save frame.
        self.frame = SaveFrame(title=self.sf_label)

        # Create the tag categories.
        for i in range(len(self.tag_categories)):
            self.tag_categories[i].create()

        # Add the saveframe to the data nodes.
        self.datanodes.append(self.frame)


    def add_tag_categories(self):
        """Create the tag categories."""

        # The tag category objects.
        self.tag_categories = []
        self.tag_categories.append(TensorList(self))
        self.tag_categories.append(Tensor(self))



class TensorList(TagCategoryFree):
    """Base class for the TensorList tag category."""

    def __init__(self, sf):
        """Setup the TensorList tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(TensorList, self).__init__(sf)

        # The category name.
        self.tag_category_label='Tensor_list'

        # Database table names to class instance variables.
        self.data_to_var_name.append(['TensorID',                    'data_ids'])
        self.data_to_var_name.append(['TensorType',                  'tensor_type'])
        self.data_to_var_name.append(['GeometricShape',              'geometric_shape'])
        self.data_to_var_name.append(['TensorSymmetry',              'tensor_symmetry'])
        self.data_to_var_name.append(['MatrixValUnits',              'matrix_val_units'])
        self.data_to_var_name.append(['AngleUnits',                  'angle_units'])
        self.data_to_var_name.append(['IsotropicValFormula',         'iso_val_formula'])
        self.data_to_var_name.append(['AnisotropicValFormula',       'aniso_val_formula'])
        self.data_to_var_name.append(['RhombicValFormula',           'rhomb_val_formula'])
        self.data_to_var_name.append(['EulerAngleType',              'euler_type'])
        self.data_to_var_name.append(['DataFileName',                'file_name'])
        self.data_to_var_name.append(['Details',                     'details'])

        # Database table name to tag name.
        self.data_to_tag_name['SfCategory'] =               'Sf_category'
        self.data_to_tag_name['SfFramecode'] =              'Sf_framecode'
        self.data_to_tag_name['EntryID'] =                  'Entry_ID'
        self.data_to_tag_name['SfID'] =                     'Sf_ID'
        self.data_to_tag_name['TensorID'] =                 'ID'
        self.data_to_tag_name['TensorType'] =               'Tensor_type'
        self.data_to_tag_name['GeometricShape'] =           'Geometric_shape'
        self.data_to_tag_name['TensorSymmetry'] =           'Tensor_symmetry'
        self.data_to_tag_name['MatrixValUnits'] =           'Matrix_val_units'
        self.data_to_tag_name['AngleUnits'] =               'Angle_units'
        self.data_to_tag_name['IsotropicValFormula'] =      'Isotropic_val_formula'
        self.data_to_tag_name['AnisotropicValFormula'] =    'Anisotropic_val_formula'
        self.data_to_tag_name['RhombicValFormula'] =        'Rhombic_val_formula'
        self.data_to_tag_name['EulerAngleType'] =           'Euler_angle_type'
        self.data_to_tag_name['DataFileName'] =             'Data_file_name'
        self.data_to_tag_name['Details'] =                  'Details'



class Tensor(TagCategory):
    """Base class for the Tensor tag category."""

    def __init__(self, sf):
        """Setup the Tensor tag category.

        @param sf:  The saveframe object.
        @type sf:   saveframe instance
        """

        # Initialise the baseclass.
        super(Tensor, self).__init__(sf)

        # The category name.
        self.tag_category_label='Tensor'

        # Database table names to class instance variables.
        self.data_to_var_name.append(['TensorID',                   'data_ids'])
        self.data_to_var_name.append(['AssemblyAtomID',             'assembly_atom_ids'])
        self.data_to_var_name.append(['EntityAssemblyID',           'entity_assembly_ids'])
        self.data_to_var_name.append(['EntityID',                   'entity_ids'])
        self.data_to_var_name.append(['CompIndexID',                'res_nums'])
        self.data_to_var_name.append(['CompID',                     'res_names'])
        self.data_to_var_name.append(['AtomID',                     'atom_names'])
        self.data_to_var_name.append(['AtomType',                   'atom_types'])
        self.data_to_var_name.append(['AtomIsotopeNumber',          'isotope'])
        self.data_to_var_name.append(['AxialSymAxisPolarAngle',     'axial_sym_axis_polar_angle'])
        self.data_to_var_name.append(['AxialSymAxisAzimuthalAngle', 'axial_sym_axis_azimuthal_angle'])
        self.data_to_var_name.append(['IsotropicVal',               'iso_val'])
        self.data_to_var_name.append(['AnisotropicVal',             'aniso_val'])
        self.data_to_var_name.append(['RhombicVal',                 'rhombic_val'])
        self.data_to_var_name.append(['EulerAngleAlpha',            'euler_alpha'])
        self.data_to_var_name.append(['EulerAngleBeta',             'euler_beta'])
        self.data_to_var_name.append(['EulerAngleGamma',            'euler_gamma'])
        self.data_to_var_name.append(['IsotropicComp11Val',         'iso_comp_11'])
        self.data_to_var_name.append(['IsotropicComp22Val',         'iso_comp_22'])
        self.data_to_var_name.append(['IsotropicComp33Val',         'iso_comp_33'])
        self.data_to_var_name.append(['AntiSymComp12Val',           'antisym_comp_12'])
        self.data_to_var_name.append(['AntiSymComp13Val',           'antisym_comp_13'])
        self.data_to_var_name.append(['AntiSymComp23Val',           'antisym_comp_23'])
        self.data_to_var_name.append(['ReduceableMatrix11Val',      'tensor_11'])
        self.data_to_var_name.append(['ReduceableMatrix12Val',      'tensor_12'])
        self.data_to_var_name.append(['ReduceableMatrix13Val',      'tensor_13'])
        self.data_to_var_name.append(['ReduceableMatrix21Val',      'tensor_21'])
        self.data_to_var_name.append(['ReduceableMatrix22Val',      'tensor_22'])
        self.data_to_var_name.append(['ReduceableMatrix23Val',      'tensor_23'])
        self.data_to_var_name.append(['ReduceableMatrix31Val',      'tensor_31'])
        self.data_to_var_name.append(['ReduceableMatrix32Val',      'tensor_32'])
        self.data_to_var_name.append(['ReduceableMatrix33Val',      'tensor_33'])
        self.data_to_var_name.append(['TensorListID',               'count_list'])

        # Database table name to tag name.
        self.data_to_tag_name['TensorID'] =                     'ID'
        self.data_to_tag_name['InteratomicDistanceListID'] =    'Interatomic_distance_list_ID'
        self.data_to_tag_name['InteratomicDistSetID'] =         'Interatomic_dist_set_ID'
        self.data_to_tag_name['CalcTypeID'] =                   'Calc_type_ID'
        self.data_to_tag_name['AssemblyAtomID'] =               'Assembly_atom_ID'
        self.data_to_tag_name['EntityAssemblyID'] =             'Entity_assembly_ID'
        self.data_to_tag_name['EntityID'] =                     'Entity_ID'
        self.data_to_tag_name['CompIndexID'] =                  'Comp_index_ID'
        self.data_to_tag_name['SeqID'] =                        'Seq_ID'
        self.data_to_tag_name['CompID'] =                       'Residue_label'
        self.data_to_tag_name['AtomID'] =                       'Atom_name'
        self.data_to_tag_name['AtomType'] =                     'Atom_type'
        self.data_to_tag_name['AtomIsotopeNumber'] =            'Atom_isotope_number'
        self.data_to_tag_name['AxialSymAxisPolarAngle'] =       'Axial_sym_axis_polar_angle'
        self.data_to_tag_name['AxialSymAxisAzimuthalAngle'] =   'Axial_sym_axis_azimuthal_angle'
        self.data_to_tag_name['IsotropicVal'] =                 'Isotropic_val'
        self.data_to_tag_name['AnisotropicVal'] =               'Anisotropic_val'
        self.data_to_tag_name['RhombicVal'] =                   'Rhombic_val'
        self.data_to_tag_name['EulerAngleAlpha'] =              'Euler_angle_alpha'
        self.data_to_tag_name['EulerAngleBeta'] =               'Euler_angle_beta'
        self.data_to_tag_name['EulerAngleGamma'] =              'Euler_angle_gamma'
        self.data_to_tag_name['IsotropicComp11Val'] =           'Isotropic_comp_1_1_val'
        self.data_to_tag_name['IsotropicComp22Val'] =           'Isotropic_comp_2_2_val'
        self.data_to_tag_name['IsotropicComp33Val'] =           'Isotropic_comp_3_3_val'
        self.data_to_tag_name['AntiSymComp12Val'] =             'Anti_sym_comp_1_2_val'
        self.data_to_tag_name['AntiSymComp13Val'] =             'Anti_sym_comp_1_3_val'
        self.data_to_tag_name['AntiSymComp23Val'] =             'Anti_sym_comp_2_3_val'
        self.data_to_tag_name['SymTracelessComp11Val'] =        'Sym_traceless_comp_1_1_val'
        self.data_to_tag_name['SymTracelessComp12Val'] =        'Sym_traceless_comp_1_2_val'
        self.data_to_tag_name['SymTracelessComp13Val'] =        'Sym_traceless_comp_1_3_val'
        self.data_to_tag_name['SymTracelessComp22Val'] =        'Sym_traceless_comp_2_2_val'
        self.data_to_tag_name['SymTracelessComp23Val'] =        'Sym_traceless_comp_2_3_val'
        self.data_to_tag_name['ReduceableMatrix11Val'] =        'Reduceable_matrix_1_1_val'
        self.data_to_tag_name['ReduceableMatrix12Val'] =        'Reduceable_matrix_1_2_val'
        self.data_to_tag_name['ReduceableMatrix13Val'] =        'Reduceable_matrix_1_3_val'
        self.data_to_tag_name['ReduceableMatrix21Val'] =        'Reduceable_matrix_2_1_val'
        self.data_to_tag_name['ReduceableMatrix22Val'] =        'Reduceable_matrix_2_2_val'
        self.data_to_tag_name['ReduceableMatrix23Val'] =        'Reduceable_matrix_2_3_val'
        self.data_to_tag_name['ReduceableMatrix31Val'] =        'Reduceable_matrix_3_1_val'
        self.data_to_tag_name['ReduceableMatrix32Val'] =        'Reduceable_matrix_3_2_val'
        self.data_to_tag_name['ReduceableMatrix33Val'] =        'Reduceable_matrix_3_3_val'
        self.data_to_tag_name['AuthEntityAssemblyID'] =         'Auth_entity_assembly_ID'
        self.data_to_tag_name['AuthSeqID'] =                    'Auth_seq_ID'
        self.data_to_tag_name['AuthCompID'] =                   'uth_comp_ID'
        self.data_to_tag_name['AuthAtomID'] =                   'Auth_atom_ID'
        self.data_to_tag_name['EntryID'] =                      'Entry_ID'
        self.data_to_tag_name['TensorListID'] =                 'Tensor_list_ID'
