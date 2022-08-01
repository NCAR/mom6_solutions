#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import sys
from os.path import exists

from setuptools import setup, find_packages

long_description = 'Collection of notebooks and scripts used to '\
                   'diagnose MOM6 solutions derived from CESM.'

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Scientific/Engineering',
]

setup(
    maintainer='Gustavo Marques',
    maintainer_email='gmarques@ucar.edu',
    description='Diagnose MOM6 solutions derived from CESM',

    install_requires=install_requires,
    license='Apache License 2.0',
    long_description=long_description,
    classifiers=CLASSIFIERS,
    keywords='ocean modeling, ocean diagnostics, CESM/MOM6',
    name='mom6_solutions',
    packages=find_packages (),
    include_package_data=True,
    url='https://github.com/NCAR/mom6_solutions',
    use_scm_version={'version_scheme': 'post-release', 'local_scheme': 'dirty-tag'},
    setup_requires=['setuptools_scm', 'setuptools>=30.3.0'],
    zip_safe=False,
)

