#!/usr/bin/env python

from setuptools import setup

# blink2png  Copyright (C) 2019 Star Inc.
# This program comes with ABSOLUTELY NO WARRANTY; for details type 'show w'.
# This is free software, and you are welcome to redistribute it
# under certain conditions; type 'show c' for details.

version = '0.9'

setup(
    name="blink2png",
    version=version,
    url='http://github.com/star-inc/blink2png',
    license='GNU General Public License',
    description="To take snapshot of web pages using Blink Engine and Qt5",
    author='Star Inc.',
    author_email='"Star Inc." <star-inc＠aol.com>',
    packages=['blink2png'],
    zip_safe=True,
    include_package_data=True,
    package_dir=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License, version 3',
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
