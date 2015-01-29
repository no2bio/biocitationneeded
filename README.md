You can see a demo [**here**](http://bl.ocks.org/thedod/raw/70f3e820380598c352c3/)

Map was done with [DataMaps](http://datamaps.github.io/). Respect

Note: no more markdown. Things are simpler now ;)

### Prerequsites

* Python 2 (not 3)
* [pystache](https://pypi.python.org/pypi/pystache/)

### Rendering everything

* `./build.sh`

### Files


#### Layout html templates (`_*.template`)
* `_index.template` &mdash; html template of homepage

* `_country.template` &mdash; html template of a country's page

#### Data
* `citations.json` &mdash; Theoretically, contains all data. Practically,
  partial templates are used (and reused) when there's need to write more than a single paragraph
  of html (easier to edit text when it's not inside a json string ;) ).

* Partial templates (`*.template` except for `_*.template`) &mdash; contain html content
  you can import into `citations.json` by writing a string like `"<biopass-wikipedia.temlplate"`.
  Mustache can be used with the relevant tag and country
  context (e.g. `{{country.name}}` or `{{tag.description}}`). See `biopass-wikipedia.temlplate` example.
