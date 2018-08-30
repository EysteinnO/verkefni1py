import os
from os import environ as env
from sys import argv
from bottle import route, run, error

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@route('/')
def index():
    return '''
            <h1>Hallo heimur</h1>
            <a href='About'>About</a> 
            <a href='Biography'>Biography</a>
            <a href='Pictures'>Pictures</a>
            '''
@route('/<pagename>')
def pages(pagename):
    if pagename == 'About':
        return "This is the about page"
    if pagename == 'Biography':
            return "This is the biography page"
    if pagename == 'Pictures':
            return "This is the picture page"

@route('/Pictures')
def Pictures():
    return "Pictures page"
#run(host='localhost', port=8080, debug=True)
bottle.run(host='0.0.0.0', port=argv[1])
