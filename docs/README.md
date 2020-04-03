# blink2png

![Version](https://img.shields.io/badge/v0.9-OpenSource-33FF33.svg)
![License](https://img.shields.io/badge/license-GPL--3.0-FF8800.svg)
![Python](https://img.shields.io/badge/python-3.x-0066FF.svg)

To take snapshot of web pages using Blink Engine and Qt5

## What is the Blink Engine
This is a browser engine from Chromium Project by [Google](https://google.com).

It is used in Chrome and more the Chromium Core Projects.

## Requirement
    python >= 3.7
    PyQt >= 5.13
    PyQtWebEngine >= 5.13

## Installation

Important: Must upgrade ``pip`` to latest version prevent from error while install PyQt5

### Debian/Ubuntu
- Add following packages: ``apt-get install libqt5core5a python3-pip``

#### Automated installation via ```pip```
- Install blink2png: ```pip3 install blink2png```

#### Manual installation via Git
- Install git: ``apt-get install git``
- Clone the project: ``git clone https://github.com/star-inc/blink2png.git``
- Install with: ``python3 blink2png/setup.py install``
- If the requirement install failed, satified with: ``pip3 install -r blink2png/requirements.txt``

### FreeBSD
- install qt5 webkit: ```www/py-qt5-webkit, www/qt5-webkit, devel/py-qt5```
- install pip: ``devel/py-pip``
- install via: ``pip install blink2png``

## Usage
- For help run: ``blink2png -h``

## Thanks for
- Origin: [All the contributors](AUTHORS.md)
- According License: [GPL 3.0](LICENSE.md)

> (c) 2019 [Star Inc.](https://starinc.xyz/)
