#!/usr/bin/env python

from setuptools import setup

version = '0.9'

description = "To take snapshot of web pages using Blink Engine and Qt5"
long_description = description

setup(
    name="blink2png",
    version=version,
    url='http://github.com/star-inc/blink2png',
    license='GNU General Public License',
    description=description,
    long_description=long_description,
    author='Star Inc.',
    author_email='star-inc(at)aol.com',
    packages=['blink2png'],
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
            'blink2png = blink2png.__main__:main',
        ]
    }, install_requires=['PyQt5', 'PyQtWebEngine']
)
