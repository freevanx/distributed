from __future__ import print_function, division, absolute_import

import sys

if sys.version_info[0] == 2:
    from Queue import Queue

if sys.version_info[0] == 3:
    from queue import Queue

try:
    from functools import singledispatch
except ImportError:
    from singledispatch import singledispatch
