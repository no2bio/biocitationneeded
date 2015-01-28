You can see a [lame] demo [**here**](http://bl.ocks.org/thedod/raw/70f3e820380598c352c3/)

The important thing here is the structure of `citations.json`

The templates and the rendering mechanism are just to test if the concept works.
I also needed a flat directory structure because gist.

I'm sure you can do something simpler and nicer in Jekyl ;)

### Prerequsites

* Python 2 (not 3)
* [pystache](https://pypi.python.org/pypi/pystache/)

### Rendering everything

* `./build.sh`

### Files

#### Data
* `citations.json` &mdash; theoretically, contains all data. Practically,
  partial templates are used (and reused) when there's need to write more than a single paragraph
  of markup (easier to edit text when it's not inside a json string ;) ).

* Partial templates (`*.template` except for `_*.template`) &mdash; contain markdown content
  you can import into `citations.json` by writing a string like `"<biopass-wikipedia.temlplate"`.
  Mustache can be used with the relevant tag and country
  context (e.g. `{{country.name}}` or `{{tag.description}}`). See `biopass-wikipedia.temlplate` example.

#### Scripts
* `build.sh` &mdash; Normally, that's the only script you run. Read it to see how other scripts are used.
* `makemd.py` &mdash; Generates `country-*.md` and `index.md`
* `makeindex.py` &mdash;  Filters `markdown < index.md` result via `_index.html` template to generate `index.html`
* `makecountry.py` &mdash;  Filters `markdown < country-XX.md` result via `_country.html` content to generate `country-XX.html`

#### Markdown templates
* `_citation_head.template` &mdash; where we show tag description and value (e.g. `ID card: Yes`)
* `_index.template` &mdash; markdown template of homepage
* `_country.template` &mdash; markdown template of a country page

#### Html templates
* `_index.html` &mdash; wrapper template for the html rendered from `index.md` (`<head/>`, javascript, etc.)
* `_country.html` &mdash; wrapper template for a country page's html content (rendered from markdown)
