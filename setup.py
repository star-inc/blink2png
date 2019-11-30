#!/usr/bin/env python

from setuptools import setup

version = '0.9.0'

description = "Takes snapshot of web pages using Webkit and Qt5"
long_description = description

setup(
    name="webkit2png",
    version=version,
    url='http://github.com/AdamN/python-webkit2png',
    license='GNU Lesser General Public License',
    description=description,
    long_description=long_description,
    author='Roland Tapken',
    author_email='roland at dau-sicher de',
    packages=['webkit2png'],
    zip_safe=True,
    include_package_data=True,
    package_dir=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Bug Tracking',
        'Topic :: Multimedia :: Graphics :: Capture :: Screen Capture',
        'Topic :: Utilities'
    ],
    entry_points={
        'console_scripts': [
            'webkit2png = webkit2png.scripts:main',
        ]
    }, install_requires=['PyQt5', 'sip']
)
