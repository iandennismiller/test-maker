from setuptools import setup, find_packages
import os, shutil

version = '0.1'

setup(name='test-maker',
      version=version,
      description="Test Maker",
      scripts=[
            "bin/test-make", 
            ],
      long_description="""test-maker""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      include_package_data = True,
      #package_data = {
      #      '': ['templates/*.html'],
      #},
      keywords='',
      author='',
      author_email='',
      url='',
      #install_requires = [],
      packages = ["TestMaker"],
      license='MIT',
      zip_safe=False,
      )
