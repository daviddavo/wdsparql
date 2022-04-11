from . import wdsparqlmagic
from .wdsparqlmagic import wdSparQLJSON, wdSpaqrQLPandas

__all__ = [
    'wdSparQLJSON',
    'wdSpaqrQLPandas',
]


def load_ipython_extension(ipython):
    ipython.register_magic_function(wdsparqlmagic.wdsparql, 'cell')
    ipython.register_magic_function(wdsparqlmagic.wdseturl, 'line')
    ipython.register_magic_function(wdsparqlmagic.wdreseturl, 'line')
