# ELBE - Debian Based Embedded Rootfilesystem Builder
# Copyright (c) 2016-2017 Manuel Traut <manut@linutronix.de>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from npyscreen import NPSAppManaged

from .kernel import Kernel       # pylint: disable=unused-import
from .uboot import UBoot         # pylint: disable=unused-import
from .barebox import BareBox     # pylint: disable=unused-import

from .base import DebianizeBase  # pylint: disable=unused-import


class Debianize (NPSAppManaged):
    def __init__(self, debianizer):
        self.debianizer = debianizer
        NPSAppManaged.__init__(self)

    def onStart(self):
        self.registerForm('MAIN', self.debianizer())
