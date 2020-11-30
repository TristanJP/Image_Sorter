#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
from setuptools import setup

README = ''
if os.path.exists('README.md'):
    with open('README.md') as readme_file:
        README = readme_file.read()

LICENSE = ''
if os.path.exists('LICENSE'):
    with open('LICENSE') as license_file:
        LICENSE = license_file.read()

REQUIREMENTS = ''
if os.path.exists('requirements.txt'):
    with open('requirements.txt') as reqs_file:
        REQUIREMENTS = reqs_file.read()

TEST_REQUIREMENTS = [
]

setup(
    name='image-sorter',
    version='0.0.1',
    description='Tool for sorting through large volumes of images and removing duplicates.',
    long_description=README,
    license=LICENSE,
    author='Tristan Perkins',
    author_email='trisperk@hotmail.com',
    url='https://github.com/TristanJP/Image_Sorter',
    packages=[
        'image_sorter'
    ],
    package_dir={
        'image_sorter': 'image_sorter',
    },
    entry_points={
        'console_scripts': [
            'sort-images=image_sorter.__main__:main',
        ]
    },
    include_package_data=True,
    install_requires=REQUIREMENTS,
    zip_safe=True,
    keywords=['image', 'sorter', 'duplicate'],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
    ],
    test_suite='tests',
    tests_require=TEST_REQUIREMENTS
)
