#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext
from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='poetrylab_api',
    version='0.0.1',
    license='Apache Software License 2.0',
    description='API for the PoetryLab project',
    author='LINHD POSTDATA Project',
    author_email='info@linhd.uned.es',
    url='https://github.com/linhd-postdata/poetrylab-api',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires='>3.6',
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov', 'snapshottest'],
    install_requires=read('requirements.txt').splitlines()
)
