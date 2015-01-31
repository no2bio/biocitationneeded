import json,csv
en2he = {}
def addword(w):
    if not en2he.has_key(w):
        en2he[w] = ''
print "Reading en2he.csv..."
try:
    for r in csv.reader(file('en2he.csv')):
        en2he[unicode(r[0],'utf-8')] = unicode(r[1],'utf-8')
    print "Imported {} phrases".format(len(en2he))
except Exception as e:
    print `e`
print "Reading citations..."
citations = json.load(file('citations.json'))
for country in citations['countries']:
    addword(country['name'])
    for citation in country.get('citations',[]):
        v = citation.get('value')
        if v:
            addword(v)
print "writing en2he-new.csv..."
output = csv.writer(file('en2he-new.csv','w'))
for w in sorted(en2he.keys()):
    output.writerow([w.encode('utf-8'),en2he[w].encode('utf-8')])
print "Done."
