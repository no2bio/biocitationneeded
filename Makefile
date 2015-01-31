all: index.html

# This also creates README.template
# Sorry about that. At least it's .gitignored ;)
templates := $(patsubst %.md,%.template,$(wildcard *.md))
_templates := _index.template _index-he.template _country.template
datafiles := citations.json en2he.csv

index.html: $(templates) $(_templates) $(datafiles) makehtml.py
	python2 makehtml.py

%.template: %.md
	markdown < $< > $@
