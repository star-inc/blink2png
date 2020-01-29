#!/usr/bin/env python

from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# blink2png  Copyright (C) 2019 Star Inc.
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

version = '0.9b'

setup(
    name="blink2png",
    version=version,
    url='http://github.com/star-inc/blink2png',
    license='GNU General Public License',
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='To take snapshot of web pages using Blink Engine and Qt5',
    author='Star Inc.',
    author_email='"Star Inc." <star-inc@aol.com>',
    packages=['blink2png'],
    zip_safe=True,
    include_package_data=True,
    package_dir=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Bug Tracking',
        'Topic :: Multimedia :: Graphics :: Capture :: Screen Capture',
        'Topic :: Utilities'
    ],
    entry_points={
        'console_scripts': [
            'blink2png = blink2png.__main__:main',
        ]
    }, install_requires=['PyQt5', 'PyQtWebEngine']
)
