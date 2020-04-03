#!/usr/bin/env python3

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

import logging
import os
import signal
import sys
import urllib.parse
from optparse import OptionParser

from PyQt5.QtCore import *
from PyQt5.QtNetwork import *
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
from PyQt5.QtWidgets import QApplication

from .core import WebEngineRenderer

VERSION = "0.9"
LOG_FILENAME = 'blink2png.log'
logger = logging.getLogger('blink2png')

app = QApplication([])


def init_qtgui(display=None, style=None, qtargs=None):
    """Initiates the QApplication environment using the given args."""
    if app.instance():
        logger.debug("QApplication has already been instantiated. \
                        Ignoring given arguments and returning existing QApplication.")
        return app.instance()

    qt_args2 = [sys.argv[0]]

    if display:
        qt_args2.append('-display')
        qt_args2.append(display)
        # Also export DISPLAY var as this may be used
        # by flash plugin
        os.environ["DISPLAY"] = display

    if style:
        qt_args2.append('-style')
        qt_args2.append(style)

    qt_args2.extend(qtargs or [])

    return QApplication(qt_args2)


def main():
    # This code will be executed if this module is run 'as-is'.

    # Enable HTTP proxy
    if 'http_proxy' in os.environ:
        proxy_url = urllib.parse.urlparse(os.environ.get('http_proxy'))
        proxy = QNetworkProxy(QNetworkProxy.HttpProxy, proxy_url.hostname, proxy_url.port)
        proxy.setApplicationProxy(proxy)

    # Parse command line arguments.
    # Syntax:
    # $0 [--display=DISPLAY] [--debug] [--output=FILENAME] <URL>

    description = "Creates a snapshot of a website using QtWebEngine." \
                  + "This program comes with ABSOLUTELY NO WARRANTY. " \
                  + "This is free software, and you are welcome to redistribute " \
                  + "it under the terms of the GNU General Public License v3."

    parser = OptionParser(
        usage="usage: %prog [options] <URL>",
        version="%prog " + VERSION + ", Copyright (c) Star Inc.",
        description=description,
        add_help_option=True
    )

    parser.add_option(
        "-g",
        "--geometry",
        dest="geometry",
        nargs=2,
        default=(1024, 600),
        type="int",
        help="Geometry of the virtual browser window (0 means 'autodetect') [default: %default].",
        metavar="WIDTH HEIGHT"
    )

    parser.add_option(
        "-o", "--output",
        dest="output",
        help="Set output filename [default: capture.png] or using stdout [type: \"stdout\" only]",
        metavar="FILE"
    )

    parser.add_option(
        "-f",
        "--format",
        dest="format",
        default="png",
        help="Output image format [default: %default]",
        metavar="FORMAT"
    )

    parser.add_option(
        "--scale",
        dest="scale",
        nargs=2,
        type="int",
        help="Scale the image to this size",
        metavar="WIDTH HEIGHT"
    )

    parser.add_option(
        "--aspect-ratio",
        dest="ratio",
        type="choice",
        choices=["ignore", "keep", "expand", "crop"],
        help="One of 'ignore', 'keep', 'crop' or 'expand' [default: %default]"
    )

    parser.add_option(
        "-F",
        "--feature",
        dest="features",
        action="append",
        type="choice",
        choices=["javascript", "plugins"],
        help="Enable additional WebEngine features ('javascript', 'plugins')",
        metavar="FEATURE")

    parser.add_option(
        "-c", "--cookie",
        dest="cookies",
        action="append",
        help="Add this cookie. "
             "Use multiple times for more cookies. Specification is value of a Set-Cookie HTTP response header.",
        metavar="COOKIE"
    )

    parser.add_option(
        "-w",
        "--wait",
        dest="wait",
        default=0,
        type="int",
        help="Time to wait after loading before the screenshot is taken [default: %default]",
        metavar="SECONDS"
    )

    parser.add_option(
        "-t",
        "--timeout",
        dest="timeout", default=0, type="int",
        help="Time before the request will be canceled [default: %default]", metavar="SECONDS"
    )

    parser.add_option(
        "-W", "--window",
        dest="window",
        action="store_true",
        help="Grab whole window instead of frame (may be required for plugins)",
        default=False
    )

    parser.add_option(
        "-T",
        "--transparent",
        dest="transparent",
        action="store_true",
        help="Render output on a transparent background (Be sure to have a transparent background defined in the html)",
        default=False
    )

    parser.add_option(
        "", "--style",
        dest="style",
        help="Change the Qt look and feel to STYLE (e.G. 'windows').",
        metavar="STYLE"
    )

    parser.add_option(
        "",
        "--encoded-url",
        dest="encoded_url",
        action="store_true",
        help="Treat URL as url-encoded",
        metavar="ENCODED_URL",
        default=False
    )

    parser.add_option(
        "-d",
        "--display",
        dest="display",
        help="Connect to X server at DISPLAY.",
        metavar="DISPLAY"
    )

    parser.add_option(
        "--debug",
        action="store_true",
        dest="debug",
        help="Show debugging information.",
        default=False
    )

    parser.add_option(
        "--log",
        action="store",
        dest="logfile",
        default=LOG_FILENAME,
        help="Select the log output file",
    )

    # Parse command line arguments and validate them (as far as we can)
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments")
    options.url = args[0]

    logging.basicConfig(filename=options.logfile, level=logging.WARN, )

    # Enable output of debugging information
    if options.debug:
        logger.setLevel(logging.DEBUG)

    # Prepare output ("1" means STDOUT)
    if options.output is None:
        options.output = open("capture.png", "wb+")
    elif options.output == "stdout":
        options.output = sys.stdout
    else:
        options.output = open(str(options.output), "wb+")

    logger.debug("Version %s, Python %s, Qt %s", VERSION, sys.version, qVersion())

    # Technically, this is a QtGui application, because QWebPage requires it
    # to be. But because we will have no user interaction, and rendering can
    # not start before 'app.exec_()' is called, we have to trigger our "main"
    # by a timer event.
    def __main_qt():
        # Render the page.
        # If this method times out or loading failed, a
        # RuntimeException is thrown
        try:
            # Initialize WebEngineRenderer object
            renderer = WebEngineRenderer()
            renderer.logger = logger
            renderer.width = options.geometry[0]
            renderer.height = options.geometry[1]
            renderer.timeout = options.timeout
            renderer.wait = options.wait
            renderer.format = options.format
            renderer.grabWholeWindow = options.window
            renderer.renderTransparentBackground = options.transparent
            renderer.encodedUrl = options.encoded_url
            if options.cookies:
                renderer.cookies = options.cookies

            if options.scale:
                renderer.scaleRatio = options.ratio
                renderer.scaleToWidth = options.scale[0]
                renderer.scaleToHeight = options.scale[1]

            if options.features:
                if "javascript" in options.features:
                    renderer.qWebSettings[QWebEngineSettings.JavascriptEnabled] = True
                if "plugins" in options.features:
                    renderer.qWebSettings[QWebEngineSettings.PluginsEnabled] = True

            renderer.render_to_file(res=options.url, file_object=options.output)
            options.output.close()
            app.exit(0)
        except RuntimeError as e:
            logger.error("main: %s" % e)
            sys.stderr.write(e)
            app.exit(1)

    # Initialize Qt-Application, but make this script
    # To interrupt via CTRL-C
    app_ = init_qtgui(display=options.display, style=options.style)
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    QTimer().singleShot(0, __main_qt)
    return app_.exec_()


if __name__ == '__main__':
    sys.exit(main())
