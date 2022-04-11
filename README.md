# wdsparqlmagic
IPython magic to run Wikidata's Sparql queries on the notebooks

## Features

### Magics

- `%%wdsparql`: Runs the cell as a sparql query on your notebook
- `%wdseturl <url>`: Sets the url to run the queries against
- `%wdreseturl`: Resets the url

### Other features
- After running a wdsparql query, a pandas dataframe will be available as `_dfwd`. You can run all common pandas operations against it.

## TODO:
- [x] What happens if an error occurs?
  - Raising custom exception
- [x] Expose the last query result to the namespace as a pandas dataframe
- [ ] Create setup.py
- [ ] Upload to pypi
- [ ] For displaying, stop using dataframes and use a custom class
  - [ ] Make links clickable
  - [ ] Display images
  - [ ] Display map
- [x] Make sample notebook (use wikipedia's queries)
- [ ] Testing
  - [ ] Unit testing for the functions
  - [ ] Visual testing for the sample notebook
- [ ] Write the README.md
  - [ ] Button to "run with binder"
  - [x] Explain all the magics:
    - [x] wdsparql
    - [x] wdseturl
    - [x] wdreseturl
- [ ] Adding more queries than the simple ones to the notebook
- [ ] Making a new kernel instead of an extension (select cell language: sparql)