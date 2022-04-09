from . import wdsparqlmagic
from .wdsparqlmagic import wdSparQLQueryJSON, wdSpaqrQLQueryPandas

__all__ = [
    'wdSparQLQueryJSON',
    'wdSpaqrQLQueryPandas',
]


def load_ipython_extension(ipython):
    ipython.register_magic_function(wdsparqlmagic.wdsparql, 'cell')
    ipython.register_magic_function(wdsparqlmagic.wdseturl, 'line')
    ipython.register_magic_function(wdsparqlmagic.wdreseturl, 'line')
