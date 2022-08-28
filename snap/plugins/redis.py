import os
import logging
import shutil
import re
import subprocess

import snapcraft_legacy
from snapcraft_legacy.plugins.v1 import make

logger = logging.getLogger(__name__)


class RedisPlugin(make.MakePlugin):

    def build(self):
        super(make.MakePlugin, self).build()

        command = ['make']

        if self.options.makefile:
            command.extend(['-f', self.options.makefile])

        if self.options.make_parameters:
            command.extend(self.options.make_parameters)

        self.run(command + ['-j{}'.format(self.project.parallel_build_count)])
        self.run(command + ['install', 'PREFIX=' + self.installdir])
