all: index.html

index.html: index.md
	markdown < index.md > index.html

index.md: citations.json makemd.py *.template
	python2 makemd.py
