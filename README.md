## The #BioCitationNeeded project

You can see the latest version at [https://dubiousdod/biocitationneeded](https://dubiousdod/biocitationneeded).

Map was done with [DataMaps](http://datamaps.github.io/). Respect.

### What is this?

The Wikipedia entry [Biometric Databese Law](https://en.wikipedia.org/wiki/Biometric_Database_Law)
deals with the *Israeli* law that might soon force all citizens to submit their biometric information
(2 fingerprints and a biometric facial photo) to a database. You can read more about it
[here](http://english.no2bio.org).

Intuitively, one would assume Israel is the only country in the world that has such a world,
but - as the saying goes - *[citation needed]* :).

Among the propaganda being spread by the supporters of the Israeli database it's common for
them to claim that "many countries" or even "most of the modern world" have such a database.
Sometimes they even name specific names of countries. Frequently, these errors stem from
the fact that many countries have a
[biometric passport](https://en.wikipedia.org/wiki/Biometric_passport#Countries_using_biometric_passports)
or some other form of biometric ID card. The *crucial* difference between storing the biometric information
of a single person on a card and maintaining a database that would enable identification of the entire
population from an arbitrary photo or fingerprint.

If you read Hebrew, some of the debate regarding the situation in "other countries"
is covered [here](http://m.no2bio.org/post-other-countries.html).

This little project tries to crowdsource
**link-backed** information regarding various issues per country. Namely, does `country X` have:

1. A biometric passport
2. Biometric databases of minorities, foreigners, prisoners, etc.
3. A compulsory ID card for all citizens (each citizen has a unique identifier)
4. A compulsory biometric database for all citizens

[if you think we should be asking *other* questios, feel free to comment,
but the idea is to keep it as simple as a few "does `country X` have ..." questions ]

A good example for a link-backed answer for `1.` is this
[Wikipedia entry](https://en.wikipedia.org/wiki/Biometric_passport#Countries_using_biometric_passports),
since it answers the questions for many countries in one go.

Any link that can answer these 4 questions with a `yes`/`no`/`it's-complicated` for 1 or
more countries is welcome. It's hard to find proof that something *doesn't exist*, but sometimes there's
proof that it was *proposed* (implies that it didn't exist at the time of the proposal) or even [*abolished*](https://archive.today/56VM0).

### How to help

The simplest way to suggest links is via my [contact form](https://swatwt.com/whatmail).
Remember to write how you want to be credited (name + link).

Also feel free to fork this gist and edit stuff yourself (either the information, or the code),
but don't feel obliged. The important thing is the information itself.

## For those about to fork (we salute you):

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
