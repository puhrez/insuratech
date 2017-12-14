# -*- coding: utf-8 -*-
"""
    insuratech
    ~~~~~~~
    insuratech's backend
"""

from setuptools import setup, find_packages


def get_long_description():
    with open('README.md') as f:
        result = f.read()
    return result


setup(
    name='insuratech',
    version='0.0.1',
    url='https://github.com/puhrez/insuratech',
    author='Michael Pérez',
    author_email='mpuhrez@gmail.com',
    description="InsuraTech's backend",
    long_description=get_long_description(),
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
)
