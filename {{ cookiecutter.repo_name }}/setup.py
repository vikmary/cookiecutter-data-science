#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

import setuptools

ROOT_PACKAGE_DIR = Path(__file__).parent.resolve()


def read_requirements():
    """Parses requirements from requirements.txt"""
    with (ROOT_PACKAGE_DIR / 'requirements.txt').open('r', encoding='utf-8') as fin:
        reqs = [line.strip() for line in fin if not line.strip().startswith('#')]
    with (ROOT_PACKAGE_DIR / 'dev-requirements.txt').open('r', encoding='utf-8') as fin:
        dev_reqs = [line.strip() for line in fin if not line.strip().startswith('#')]
    return {'install_requires': reqs, 'extras_require': {'dev': dev_reqs}}


def read_readme():
    with (ROOT_PACKAGE_DIR / 'README.md').open('r', encoding='utf-8') as fin:
        long_description = fin.read()
    return long_description


setuptools.setup(name='{{ cookiecutter.repo_name }}',
                 version='0.1.0',
                 description='{{ cookiecutter.description }}',
                 long_description=read_readme(),
                 long_description_content_type='text/markdown',
                 author='{{ cookiecutter.author_name }}',
                 author_email='{{ cookiecutter.author_email }}',
                 license='{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}',
                 package_dir={'': 'src'},
                 packages=setuptools.find_packages('src'),
                 **read_requirements())
