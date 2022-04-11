import pytest

from wdsparql import wdSparQLJSON, wdSparQLPandas, MalformedQueryException

number_humans = dict(
    head=['count'],
    query="""
#title: Number of humans in Wikidata
SELECT (COUNT(*) AS ?count)
WHERE {
  ?item wdt:P31 wd:Q5 .
}
""")


def test_bad_query():
    with pytest.raises(MalformedQueryException):
        wdSparQLJSON("akfjalksgjalkgja")


def test_no_raise():
    r = wdSparQLJSON(number_humans['query'])
    assert r['head']['vars'] == number_humans['head']


def test_number_humans():
    df = wdSparQLPandas(number_humans['query'])
    assert df.loc[0, 'count'] >= 9704433  # 2022-04-11
