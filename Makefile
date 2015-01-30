all: index.html

# This also created README.template
# Sorry about that. At least it's .gitignored ;)
templates := $(patsubst %.md,%.template,$(wildcard *.md))

index.html: $(templates) makehtml.py citations.json _index.template _country.template
	python2 makehtml.py

%.template: %.md
	markdown < $< > $@
