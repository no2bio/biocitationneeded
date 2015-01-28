import sys,json,pystache

countries = json.load(file('citations.json'))['countries']
try:
    country = [c for c in countries if c['id']==sys.argv[1].split('-')[-1].split('.')[0]][0]
except:
    sys.stderr.write('Usage: markdown country-XX.md | python2 {} country-XX.md\n'.format(sys.argv[0]))
    sys.exit(1)

template = unicode(file('_country.html').read(),'utf-8')
file('country-{}.html'.format(country['id']),'w').write(
    pystache.render(
        template, country,
        content=unicode(sys.stdin.read(),'utf-8')
    ).encode('utf-8'))
