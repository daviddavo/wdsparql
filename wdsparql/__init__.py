from . import wdsparqlmagic
try:
    from ._version import version as __version__
except ImportError:
    __version__ = 'Unknown'
from .exceptions import MalformedQueryException
from .wdsparqlmagic import wdSparQLJSON, wdSparQLPandas

__all__ = [
    'wdSparQLJSON',
    'wdSparQLPandas',
    'MalformedQueryException',
    '__version__',
]


def load_ipython_extension(ipython):
    ipython.register_magic_function(wdsparqlmagic.wdsparql, 'cell')
    ipython.register_magic_function(wdsparqlmagic.wdseturl, 'line')
    ipython.register_magic_function(wdsparqlmagic.wdreseturl, 'line')
