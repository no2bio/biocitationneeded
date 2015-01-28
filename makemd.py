import json,pystache

def import_template(t):
    return unicode(file('{}.template'.format(t)).read(),'utf-8')

def quote_or_import(s):
    if s[0]=='<':
        return import_template(s[1:])
    return s

content = json.load(file('citations.json'))
t_citation_head = import_template('_citation_head')
t_country = import_template('_country')

tagdict = {}
for tag in content['tags']:
    tagdict[tag['name']] = tag

for country in content['countries']:
    for citation in country.get('citations',[]):
        template = u'\n\n'.join([t_citation_head]+map(quote_or_import,citation['content']))
        citation['tag'] = tagdict[citation['tag']]
        citation['rendered'] = pystache.render(template,citation,country=country)
    file("country-{}.md".format(country['id']),"w").write(pystache.render(t_country,country).encode('utf-8'))

file('index.md',"w").write(pystache.render(import_template('_index'),content).encode('utf-8'))
