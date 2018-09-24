#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2017 Bitergia
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, 51 Franklin Street, Fifth Floor, Boston, MA 02110-1335, USA.
#
# Authors:
#     Santiago Dueñas <sduenas@bitergia.com>
#     Jesus M. Gonzalez-Barahona <jgb@gsyc.es>
#

import codecs
import os.path
import sys
import unittest

from setuptools import setup
from setuptools.command.test import test as TestClass


here = os.path.abspath(os.path.dirname(__file__))
readme_md = os.path.join(here, 'README.md')

# Pypi wants the description to be in reStrcuturedText, but
# we have it in Markdown. So, let's convert formats.
# Set up thinkgs so that if pypandoc is not installed, it
# just issues a warning.
try:
    import pypandoc
    long_description = pypandoc.convert(readme_md, 'rst')
except (IOError, ImportError):
    print("Warning: pypandoc module not found, or pandoc not installed. " +
          "Using md instead of rst")
    with codecs.open(readme_md, encoding='utf-8') as f:
        long_description = f.read()


version = '0.1.11'


class TestCommand(TestClass):
    user_options = []
    __dir__ = os.path.dirname(os.path.realpath(__file__))

    def initialize_options(self):
        super().initialize_options()
        sys.path.insert(0, os.path.join(self.__dir__, 'tests'))

    def run_tests(self):
        test_suite = unittest.TestLoader().discover('.', pattern='test_*.py')
        result = unittest.TextTestRunner(buffer=True).run(test_suite)
        sys.exit(not result.wasSuccessful())


cmdclass = {'test': TestCommand}

setup(name="perceval-metasploit",
      description="Bundle of Perceval backends for Metasploit ecosystem",
      long_description=long_description,
      url="https://github.com/busterb/perceval-metasploit",
      version=version,
      author="Rapid7",
      author_email="msfdev@metasploit.com",
      license="GPLv3",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Topic :: Software Development',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Programming Language :: Python :: 3'
      ],
      keywords="development repositories analytics metasploit",
      packages=[
          'perceval',
          'perceval.backends',
          'perceval.backends.metasploit',
      ],
      namespace_packages=[
          'perceval',
          'perceval.backends'
      ],
      setup_requires=[
          'wheel',
          'pandoc'
      ],
      tests_require=[
          'httpretty==0.8.6'
      ],
      install_requires=[
          'requests>=2.7.0',
          'grimoirelab-toolkit>=0.1.0',
          'perceval>=0.9.11'
      ],
      cmdclass=cmdclass,
      zip_safe=False)
