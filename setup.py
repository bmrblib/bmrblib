from distutils.core import setup


# Setup for distutils.
setup(name='bmrblib',
      version='1.0.1',
      description='The BMRB library',
      author="Edward d'Auvergne",
      author_email='edward@nmr-relax.com',
      url='https://gna.org/projects/bmrblib/',
      license='GPL',
      packages=['bmrblib',
                'bmrblib.assembly_supercategory',
                'bmrblib.citations',
                'bmrblib.entry_information',
                'bmrblib.experimental_details',
                'bmrblib.kinetics',
                'bmrblib.NMR_parameters',
                'bmrblib.pystarlib',
                'bmrblib.structure',
                'bmrblib.thermodynamics'
      ]
)
