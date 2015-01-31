## The #BioCitationNeeded project

You can see the latest version at
[https://dubiousdod.org/biocitationneeded](https://dubiousdod.org/biocitationneeded).

Map was done with [DataMaps](http://datamaps.github.io/). Respect.

### What is this?

The Wikipedia entry [Biometric Databese Law](https://en.wikipedia.org/wiki/Biometric_Database_Law)
deals with the *Israeli* law that might soon force all citizens to submit their biometric information
(2 fingerprints and a biometric facial photo) to a database. You can read more about it
[here](http://english.no2bio.org).

Intuitively, one would assume Israel is the only country in the world that has such a law,
but - as the saying goes - *[citation needed]* :).

Among the propaganda being spread by the supporters of the Israeli database there are often
claims that "many countries" or even "most of the modern world" have such databases.
Sometimes they even name specific countries. Frequently, these errors stem from
the fact that many countries have a
[biometric passport](https://en.wikipedia.org/wiki/Biometric_passport#Countries_using_biometric_passports)
or some other form of biometric ID card. The *crucial* difference between storing the biometric information
of a single person on a card and maintaining a database that would enable identification of the entire
population from an arbitrary photo or fingerprint gets lost in the spin.

If you read Hebrew, some of the debate regarding the situation in "other countries"
is covered [here](http://m.no2bio.org/post-other-countries.html).

This little project tries to crowdsource
**link-backed** information regarding various issues per country. Namely, does `country X` have:

1. A biometric passport
2. A national ID card (compulsory / non compulsory)
3. A national biometric database (compulsory / non compulsory)

[if you think we should be asking *other* questios, feel free to comment,
but the idea is to keep it as simple as a few "does `country X` have ..." questions ]

A good example for a link-backed answer for `1.` is this
[Wikipedia entry](https://en.wikipedia.org/wiki/Biometric_passport#Countries_using_biometric_passports),
since it answers the question for many countries in one go.

Any link that can answer 1 or more of these 3 questions with a `yes`/`no`/`it's-complicated` for 1 or
more countries is welcome.

### How to help

If you have a link that could add information to this project, or even correct
something [wrong](https://xkcd.com/386/) written here, please suggest it.

The simplest way to do that is via my [contact form](https://swatwt.com/whatmail).
Remember to write how you want to be credited (name + link).

Also feel free to fork this gist and edit stuff yourself (either the information, or the code).

## For those about to fork (we salute you):

### Prerequsites

* Python 2 (not 3)
* [pystache](https://pypi.python.org/pypi/pystache/)
* [Markdown](http://daringfireball.net/projects/markdown/) (command line).

### Rendering everything

* `make` ;)

### Files


#### Layout html templates (`_*.template`)
* `_index.template` &mdash; html template of homepage

* `_index-he.template` &mdash; html template of Hebrew version

* `_country.template` &mdash; html template of a country's page

#### Data
* `citations.json` &mdash; Theoretically, contains all data. Practically,
  partial templates are used (and reused) when there's need to write more than a single paragraph
  of html (easier to edit text when it's not inside a json string ;) ).

* Partial templates (`*.template` except for `_*.template`) &mdash; contain html content
  you can import into `citations.json` by writing a string like `"<biopass-wikipedia"`
  (to include the template `biopass-wikipedia.template`.
  Mustache can be used with the relevant tag and country
  context (e.g. `{{country.name}}` or `{{tag.description}}`). See `biopass-wikipedia.temlplate` example.

* `*.md` &mdash; in most cases, the `*.template` files are generated from
  their corresponding `*.md` markdown files. For example, `biodb-wikipedia.template`
  gets generated from `biodb-wikipedia.md` by `make`.

* `en2he.csv` &mdash; a tweak to translate citation values ("Compulsory", "No", etc.)
  and country names to Hebrew. If you add new citation values, run `python2 makeen2he.py`:
  it will create `en2he-new.csv` containing whatever `en2he.csv` had, plus all additional
  values that were added to `citations.csv`. You can then edit the csv file with `soffice`
  etc. and add Hebrew translations.
