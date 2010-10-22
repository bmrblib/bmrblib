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


class TensorSaveframe(BaseSaveframe):
    """The tensor saveframe class."""

    # Saveframe variables.
    sf_label = 'tensor'

    def add_tag_categories(self):
        """Create the tag categories."""

        # The tag category objects.
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
        self.tag_category_label = 'Tensor_list'

        # Add the tag info.
        self.add(key='EntryID',                 tag_name='Entry_ID',                var_name=None)
        self.add(key='SfID',                    tag_name='Sf_ID',                   var_name=None)
        self.add(key='TensorID',                tag_name='ID',                      var_name='data_ids')
        self.add(key='TensorType',              tag_name='Tensor_type',             var_name='tensor_type')
        self.add(key='GeometricShape',          tag_name='Geometric_shape',         var_name='geometric_shape',     allowed=['sphere', 'spheroid', 'oblate spheroid', 'prolate spheroid', 'ellipsoid'])
        self.add(key='TensorSymmetry',          tag_name='Tensor_symmetry',         var_name='tensor_symmetry',     allowed=['isotropic', 'anisotropic', 'axial symmetry', 'oblate axial symmetry', 'prolate axial symmetry', 'rhombic'])
        self.add(key='MatrixValUnits',          tag_name='Matrix_val_units',        var_name='matrix_val_units')
        self.add(key='AngleUnits',              tag_name='Angle_units',             var_name='angle_units',         allowed=[None, 'deg', 'rad'])
        self.add(key='IsotropicValFormula',     tag_name='Isotropic_val_formula',   var_name='iso_val_formula')
        self.add(key='AnisotropicValFormula',   tag_name='Anisotropic_val_formula', var_name='aniso_val_formula')
        self.add(key='RhombicValFormula',       tag_name='Rhombic_val_formula',     var_name='rhomb_val_formula')
        self.add(key='EulerAngleType',          tag_name='Euler_angle_type',        var_name='euler_type')
        self.add(key='DataFileName',            tag_name='Data_file_name',          var_name='file_name')
        self.add(key='Details',                 tag_name='Details',                 var_name='details')



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
        self.tag_category_label = 'Tensor'

        # Add the tag info.
        self.add(key='TensorID',                    tag_name='ID',                              var_name='data_ids')
        self.add(key='InteratomicDistanceListID',   tag_name='Interatomic_distance_list_ID',    var_name=None)
        self.add(key='InteratomicDistSetID',        tag_name='Interatomic_dist_set_ID',         var_name=None)
        self.add(key='CalcTypeID',                  tag_name='Calc_type_ID',                    var_name=None)
        self.add(key='AssemblyAtomID',              tag_name='Assembly_atom_ID',                var_name='assembly_atom_ids')
        self.add(key='EntityAssemblyID',            tag_name='Entity_assembly_ID',              var_name='entity_assembly_ids')
        self.add(key='EntityID',                    tag_name='Entity_ID',                       var_name='entity_ids',                      missing=False)
        self.add(key='CompIndexID',                 tag_name='Comp_index_ID',                   var_name='res_nums',                        missing=False)
        self.add(key='SeqID',                       tag_name='Seq_ID',                          var_name=None)
        self.add(key='CompID',                      tag_name='Residue_label',                   var_name='res_names',                       missing=False)
        self.add(key='AtomID',                      tag_name='Atom_name',                       var_name='atom_names',                      missing=False)
        self.add(key='AtomType',                    tag_name='Atom_type',                       var_name='atom_types')
        self.add(key='AtomIsotopeNumber',           tag_name='Atom_isotope_number',             var_name='isotope')
        self.add(key='AxialSymAxisPolarAngle',      tag_name='Axial_sym_axis_polar_angle',      var_name='axial_sym_axis_polar_angle')
        self.add(key='AxialSymAxisAzimuthalAngle',  tag_name='Axial_sym_axis_azimuthal_angle',  var_name='axial_sym_axis_azimuthal_angle')
        self.add(key='IsotropicVal',                tag_name='Isotropic_val',                   var_name='iso_val')
        self.add(key='AnisotropicVal',              tag_name='Anisotropic_val',                 var_name='aniso_val')
        self.add(key='RhombicVal',                  tag_name='Rhombic_val',                     var_name='rhombic_val')
        self.add(key='EulerAngleAlpha',             tag_name='Euler_angle_alpha',               var_name='euler_alpha')
        self.add(key='EulerAngleBeta',              tag_name='Euler_angle_beta',                var_name='euler_beta')
        self.add(key='EulerAngleGamma',             tag_name='Euler_angle_gamma',               var_name='euler_gamma')
        self.add(key='IsotropicComp11Val',          tag_name='Isotropic_comp_1_1_val',          var_name='iso_comp_11')
        self.add(key='IsotropicComp22Val',          tag_name='Isotropic_comp_2_2_val',          var_name='iso_comp_22')
        self.add(key='IsotropicComp33Val',          tag_name='Isotropic_comp_3_3_val',          var_name='iso_comp_33')
        self.add(key='AntiSymComp12Val',            tag_name='Anti_sym_comp_1_2_val',           var_name='antisym_comp_12')
        self.add(key='AntiSymComp13Val',            tag_name='Anti_sym_comp_1_3_val',           var_name='antisym_comp_13')
        self.add(key='AntiSymComp23Val',            tag_name='Anti_sym_comp_2_3_val',           var_name='antisym_comp_23')
        self.add(key='SymTracelessComp11Val',       tag_name='Sym_traceless_comp_1_1_val',      var_name=None)
        self.add(key='SymTracelessComp12Val',       tag_name='Sym_traceless_comp_1_2_val',      var_name=None)
        self.add(key='SymTracelessComp13Val',       tag_name='Sym_traceless_comp_1_3_val',      var_name=None)
        self.add(key='SymTracelessComp22Val',       tag_name='Sym_traceless_comp_2_2_val',      var_name=None)
        self.add(key='SymTracelessComp23Val',       tag_name='Sym_traceless_comp_2_3_val',      var_name=None)
        self.add(key='ReduceableMatrix11Val',       tag_name='Reduceable_matrix_1_1_val',       var_name='tensor_11')
        self.add(key='ReduceableMatrix12Val',       tag_name='Reduceable_matrix_1_2_val',       var_name='tensor_12')
        self.add(key='ReduceableMatrix13Val',       tag_name='Reduceable_matrix_1_3_val',       var_name='tensor_13')
        self.add(key='ReduceableMatrix21Val',       tag_name='Reduceable_matrix_2_1_val',       var_name='tensor_21')
        self.add(key='ReduceableMatrix22Val',       tag_name='Reduceable_matrix_2_2_val',       var_name='tensor_22')
        self.add(key='ReduceableMatrix23Val',       tag_name='Reduceable_matrix_2_3_val',       var_name='tensor_23')
        self.add(key='ReduceableMatrix31Val',       tag_name='Reduceable_matrix_3_1_val',       var_name='tensor_31')
        self.add(key='ReduceableMatrix32Val',       tag_name='Reduceable_matrix_3_2_val',       var_name='tensor_32')
        self.add(key='ReduceableMatrix33Val',       tag_name='Reduceable_matrix_3_3_val',       var_name='tensor_33')
        self.add(key='AuthEntityAssemblyID',        tag_name='Auth_entity_assembly_ID',         var_name=None)
        self.add(key='AuthSeqID',                   tag_name='Auth_seq_ID',                     var_name=None)
        self.add(key='AuthCompID',                  tag_name='uth_comp_ID',                     var_name=None)
        self.add(key='AuthAtomID',                  tag_name='Auth_atom_ID',                    var_name=None)
        self.add(key='EntryID',                     tag_name='Entry_ID',                        var_name=None)
        self.add(key='TensorListID',                tag_name='Tensor_list_ID',                  var_name='count_str')
