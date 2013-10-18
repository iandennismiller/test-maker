from setuptools import setup, find_packages
import os, shutil

version = '0.1'

setup(name='test-maker',
      version=version,
      description="Test Maker",
      scripts=[
            "bin/make-test", 
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
      install_requires = [
            "Jinja2==2.6",
            "mr.bob==0.1a7",
            "nose==1.2.1",
      ],
      packages = ["TestMaker"],
      license='MIT',
      zip_safe=False,
      )
