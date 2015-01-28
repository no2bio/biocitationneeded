import sys,pystache

template = unicode(file('_index.html').read(),'utf-8')
file('index.html','w').write(
    pystache.render(
        template,
        content=unicode(sys.stdin.read(),'utf-8')
    ).encode('utf-8'))
