#!/usr/bin/env python3

from distutils.core import setup

setup(name='blitz',
    version='0.1.0',
    author='Guilherme Hermeto',
    author_email='gui.hermeto@gmail.com',
    url='http://blitz.io',
    description='blitz.io python API client',
    package_dir={'': 'src'},
    packages=['blitz'],
    py_modules = ['blitz.api', 'blitz.sprint', 'blitz.rush', 'blitz.validation'],
    keywords='blitz performance load test sprint rush ping',
    license='The MIT LIcence',
    classifiers=['Operating System :: OS Independent',
               'Programming Language :: Python :: 3']
    )