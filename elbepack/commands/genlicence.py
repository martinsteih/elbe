# ELBE - Debian Based Embedded Rootfilesystem Builder
# Copyright (c) 2014, 2016 Torben Hohn <torben.hohn@linutronix.de>
# Copyright (c) 2015, 2017 Manuel Traut <manut@linutronix.de>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import print_function

from optparse import OptionParser
import sys
import os
import io

from elbepack.asciidoclog import StdoutLog
from elbepack.efilesystem import ElbeFilesystem


def run_command(argv):
    oparser = OptionParser(usage="usage: %prog genlicence [options] <rfs>")
    oparser.add_option("--output", dest="output",
                       help="outputfilename")
    oparser.add_option("--xml", dest="xml", default=None,
                       help="xml outputfilename")

    (opt, args) = oparser.parse_args(argv)

    if len(args) != 1:
        print("wrong number of arguments")
        oparser.print_help()
        sys.exit(20)

    chroot = os.path.abspath(args[0])

    rfs = ElbeFilesystem(chroot)
    log = StdoutLog()

    if opt.output:
        f = io.open(opt.output, "w+", encoding='utf-8')
    else:
        f = io.open('licence.txt', "w+", encoding='utf-8')

    rfs.write_licenses(f, log, opt.xml)
    f.close()
