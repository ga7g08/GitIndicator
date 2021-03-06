try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os

setup(name='checkgit',
      packages=['checkgit'],
      version='0.1',
      description='A quick visual check of several git repositories',
      requires = ['pygtk'],
      author='Greg Ashton',
      author_email='gash789@gmail.com',
      url='https://github.com/ga7g08/CheckGit',
      download_url='https://github.com/ga7g08/CheckGit/tarball/0.1',
      keywords=['git'],
      classifiers=[],
      entry_points={
          'gui_scripts': [
              'checkgit = checkgit.checkgit:main'
          ]
      }
      )
