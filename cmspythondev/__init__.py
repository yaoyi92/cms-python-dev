"""
Main init file for the cms-python-dev package
"""

from .cmspythondev import *
from .listtools import *



from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
