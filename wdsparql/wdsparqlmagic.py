import json
from requests.exceptions import HTTPError
import requests

import pandas as pd

from IPython.core.magic import needs_local_scope

WD_URL = "https://query.wikidata.org/sparql"
magic_wd_url = WD_URL


class MalformedQueryException(HTTPError):
    """ Wrapper form malformed queries """

    def __init__(self, httperr: HTTPError):
        super().__init__(
            request=httperr.request,
            response=httperr.response
        )

    def __str__(self):
        if self.response.status_code == 400:
            return f'400 Bad Request: {self.response.text}'

        return super().__str__()


def _json2Pd(j: dict) -> pd.DataFrame:
    columns = j['head']['vars']
    data = []

    def _getRow(r):
        return [r[c]['value'] if c in r else None for c in columns]

    data = map(_getRow, j['results']['bindings'])

    return pd.DataFrame(data, columns=columns)


def wdSparQLJSON(query, wd_url=WD_URL) -> dict:
    r = requests.get(wd_url, params={
        'query': query,
        'format': 'json',
    })

    r.raise_for_status()

    return r.json()


def wdSpaqrQLPandas(query, wd_url=WD_URL) -> pd.DataFrame:
    return _json2Pd(wdSparQLJSON(query, wd_url))


@needs_local_scope
def wdsparql(line: str, cell: str, local_ns=None):
    """ Ejecuta directamente consultas SPARQL en wikidata """
    params = line.split(',')

    try:
        result = wdSparQLJSON(cell, magic_wd_url)

        if "showjson" in params:
            print(json.dumps(result, indent=2))

        df = _json2Pd(result)
        local_ns['_dfwd'] = df

        return df
    except HTTPError as e:
        r: requests.Response = e.response

        if r.status_code == 400:  # Bad Request
            raise MalformedQueryException(e) from None

        raise


def wdseturl(line):
    global magic_wd_url
    magic_wd_url = line


def wdreseturl(_line):
    global magic_wd_url
    magic_wd_url = WD_URL
