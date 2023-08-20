#!/usr/bin/env python

from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    url='https://github.com/andreysuha2/python_core_ex7',
    description='sort files in your folder',
    author='Andrii Sukhenko',
    author_email='andreysuha2@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [ 'clean-folder = clean_folder.main:start_clearing' ]}
)