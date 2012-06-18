from distutils.core import setup


setup(name='django-templates',
      version='0.1.0',
      description='A set of templates for use within Django apps',
      author='Ryan Kanno',
      author_email='ryankanno@localkinegrinds.com',
      packages=['django-templates',],
      package_dir={'django-templates': 'django-templates'},
      package_data={'django-templates': ['templates/*/*', 'static/*/*/*']},
      long_description=open('README.txt').read(),
      install_requires=[
        "Django >= 1.4.0"
      ]
)
