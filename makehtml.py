import json,pystache

def import_template(t):
    return unicode(file('{}.template'.format(t)).read(),'utf-8')

def quote_or_import(s):
    if s[0]=='<':
        return u'<p>'+import_template(s[1:])+u'</p>'
    return u'<p>'+s+u'</p>'

content = json.load(file('citations.json'))
t_country = import_template('_country')

tagdict = {}
for tag in content['tags']:
    tagdict[tag['name']] = tag

for country in content['countries']:
    for citation in country.get('citations',[]):
        template = u'\n'.join(map(quote_or_import,citation['content']))
        citation['tag'] = tagdict[citation['tag']]
        citation['rendered'] = pystache.render(template,citation,country=country)
    file("country-{}.html".format(country['id']),"w").write(pystache.render(t_country,country).encode('utf-8'))

content['countries'].sort(key=lambda x:x['name']) # D'Oh

file('index.html',"w").write(pystache.render(import_template('_index'),content).encode('utf-8'))
