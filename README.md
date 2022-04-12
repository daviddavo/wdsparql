![PyPI - License](https://img.shields.io/pypi/l/wdsparql?style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/wdsparql?style=for-the-badge)
![PyPI - Status](https://img.shields.io/pypi/status/wdsparql?style=for-the-badge)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/daviddavo/wdsparql/HEAD?labpath=sample.ipynb)

# wdsparqlmagic
IPython magic to run Wikidata's Sparql queries on the notebooks

## Sample Notebook

You can run the sample notebook on [binder](https://mybinder.org/v2/gh/daviddavo/wdsparql/HEAD?labpath=sample.ipynb)

## Features

### Magics

- `%%wdsparql`: Runs the cell as a sparql query on your notebook
- `%wdseturl <url>`: Sets the url to run the queries against
- `%wdreseturl`: Resets the url

### Other features
- After running a wdsparql query, a pandas dataframe will be available as `_dfwd`. You can run all common pandas operations against it.

## Developing

### Publishing

Just add a new tag or release with `git tag vX.Y.Z -m "<Comment>"; git push --tags`

## TODO:
- [x] What happens if an error occurs?
  - Raising custom exception
- [x] Expose the last query result to the namespace as a pandas dataframe
- [x] Create setup.py
- [x] Upload to pypi
- [x] Make sample notebook (use wikipedia's queries)
- [x] Write the README.md
  - [x] Button to "run with binder"
  - [x] Explain all the magics:
    - [x] wdsparql
    - [x] wdseturl
    - [x] wdreseturl
- [x] Testing
  - [x] Unit testing for the functions
  - [ ] Visual testing for the sample notebook
- [x] Make test, build and upload automatically using github actions
  - [x] Check linting tools
  - [x] Use matrix to check with multiple python versions
- [ ] For displaying, stop using dataframes and use a custom class
  - [ ] Make links clickable
  - [ ] Display images
  - [ ] Display map
- [ ] Adding more queries than the simple ones to the notebook

### Optional:
- [ ] Making a new kernel instead of an extension (select cell language: sparql)