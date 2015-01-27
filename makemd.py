import os,json,pystache

def import_template(t):
    return unicode(file('{}.template'.format(t)).read(),'utf-8')

def quote_or_import(s):
    if s[0]=='<':
        return import_template(s[1:])
    return s

content = json.load(file('citations.json'))
citation_head = import_template('_citation_head')

tagdict = {}
for tag in content['tags']:
    tagdict[tag['name']] = tag

for country in content['countries']:
    for citation in country.get('citations',[]):
        template = u'\n\n'.join([citation_head]+map(quote_or_import,citation['content']))
        citation['rendered'] = pystache.render(template,citation,country=country,tag=tagdict[citation['tag']])

file('index.md',"w").write(pystache.render(import_template('index'),content).encode('utf-8'))
