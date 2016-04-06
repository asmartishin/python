#!/usr/bin/env python

import subprocess
import sys

rstr = str(' '.join(sys.argv[2:]))
rstr = rstr.replace('\\', '\\\\')
rstr = rstr.replace('\'', '\\\'')
rstr = "$'" + rstr + "'"
subprocess.call('{} {}'.format(sys.argv[1], rstr), shell=True)
