import json,csv,pystache

def import_template(t):
    return unicode(file('{}.template'.format(t)).read(),'utf-8')

def quote_or_import(s):
    if s[0]=='<':
        return u'<p>'+import_template(s[1:])+u'</p>'
    return u'<p>'+s+u'</p>'

en2he = {}
for r in csv.reader(file('en2he.csv')):
    en2he[unicode(r[0],'utf-8')] = unicode(r[1],'utf-8')

content = json.load(file('citations.json'))
t_country = import_template('_country')

tagdict = {}
for tag in content['tags']:
    tagdict[tag['name']] = tag
for country in content['countries']:
    country['he'] = en2he.get(country['name'],'') or country['name']
    for citation in country.get('citations',[]):
        template = u'\n'.join(map(quote_or_import,citation['content']))
        citation['tag'] = tagdict[citation['tag']]
        if citation.has_key('value'):
            citation['he'] = en2he.get(citation['value'],'') or citation['value']
        citation['rendered'] = pystache.render(template,citation,country=country)
        country['any_citations'] = len(country.get('citations',[]))
    file("country-{}.html".format(country['id']),"w").write(pystache.render(t_country,country).encode('utf-8'))

content['countries'].sort(key=lambda x:x['name']) # D'Oh
content['numtags'] = len(content['tags'])-1 # needed for html

file('index.html',"w").write(pystache.render(import_template('_index'),content).encode('utf-8'))
file('index-he.html',"w").write(pystache.render(import_template('_index-he'),content).encode('utf-8'))
