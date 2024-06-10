"""Demo package for live course"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pyadv-coursegw")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Guillaume Witz"
__email__ = "guillaume.witz@unibe.ch"

from . import algos