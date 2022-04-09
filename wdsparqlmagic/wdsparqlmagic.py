import json
import requests

import pandas as pd

WD_URL = "https://query.wikidata.org/sparql"
magic_wd_url = WD_URL


def _json2Pd(j: dict) -> pd.DataFrame:
    columns = j['head']['vars']
    data = []

    def _getRow(r):
        return [r[c]['value'] if c in r else None for c in columns]

    data = map(_getRow, j['results']['bindings'])

    return pd.DataFrame(data, columns=columns)


def wdSparQLQueryJSON(query, wd_url=WD_URL) -> dict:
    return requests.get(wd_url, params={
        'query': query,
        'format': 'json',
    }).json()


def wdSpaqrQLQueryPandas(query, wd_url=WD_URL) -> pd.DataFrame:
    return _json2Pd(wdSparQLQueryJSON(query, wd_url))


def wdsparql(line: str, cell):
    """ Ejecuta directamente consultas SPARQL en wikidata """
    result = wdSparQLQueryJSON(cell, magic_wd_url)
    params = line.split(',')

    if "showjson" in params:
        print(json.dumps(result, indent=2))

    return _json2Pd(result)


def wdseturl(line):
    global magic_wd_url
    magic_wd_url = line


def wdreseturl(_line):
    global magic_wd_url
    magic_wd_url = WD_URL

# TODO: CHECK ERRORS
# TODO: Hacer setup.py
# TODO: A bit of unit testing