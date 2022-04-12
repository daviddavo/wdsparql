from typing import List, Dict, Any

import json

import requests
from requests.exceptions import HTTPError
import pandas as pd
from IPython.core.magic import needs_local_scope

from .exceptions import MalformedQueryException

WD_URL = "https://query.wikidata.org/sparql"
magic_wd_url = WD_URL


def _json2Pd(j: Dict[str, Any]) -> pd.DataFrame:
    columns = j['head']['vars']

    def _getRow(r: Dict[str, Dict[str, Any]]) -> List[Any]:
        return [r[c]['value'] if c in r else None for c in columns]

    data = map(_getRow, j['results']['bindings'])

    return pd.DataFrame(data, columns=columns).apply(pd.to_numeric, errors='ignore')


def wdSparQLJSON(query: str, wd_url: str=WD_URL) -> Any:
    r = requests.get(wd_url, params={
        'query': query,
        'format': 'json',
    })

    try:
        r.raise_for_status()
    except HTTPError as e:
        r: requests.Response = e.response

        if r.status_code == 400:  # Bad Request
            raise MalformedQueryException(e) from None

        raise

    return r.json()


def wdSparQLPandas(query: str, wd_url: str = WD_URL) -> pd.DataFrame:
    return _json2Pd(wdSparQLJSON(query, wd_url))


@needs_local_scope
def wdsparql(line: str, cell: str, local_ns: Dict[str, Any] = dict()) -> pd.DataFrame:
    """ Ejecuta directamente consultas SPARQL en wikidata """
    params = line.split(',')

    result = wdSparQLJSON(cell, magic_wd_url)

    if "showjson" in params:
        print(json.dumps(result, indent=2))

    df = _json2Pd(result)
    local_ns['_dfwd'] = df

    return df


def wdseturl(line: str) -> None:
    global magic_wd_url
    magic_wd_url = line


def wdreseturl(_line: str) -> None:
    global magic_wd_url
    magic_wd_url = WD_URL
