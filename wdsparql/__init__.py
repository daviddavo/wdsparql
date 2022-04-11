from . import wdsparqlmagic
from .exceptions import MalformedQueryException
from .wdsparqlmagic import wdSparQLJSON, wdSparQLPandas

__all__ = [
    'wdSparQLJSON',
    'wdSparQLPandas',
    'MalformedQueryException',
]


def load_ipython_extension(ipython):
    ipython.register_magic_function(wdsparqlmagic.wdsparql, 'cell')
    ipython.register_magic_function(wdsparqlmagic.wdseturl, 'line')
    ipython.register_magic_function(wdsparqlmagic.wdreseturl, 'line')
