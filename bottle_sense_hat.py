#!/usr/bin/env python
from bottle import route, static_file, debug, run, get, redirect
from bottle import post, request
import os, inspect, json

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
#enable bottle debug
debug(True)

# WebApp route path
routePath = '/bottle'
# get directory of WebApp (bottleJQuery.py's dir)
rootPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

@route(routePath)
def rootHome():
    return redirect(routePath+'/index.html')

@route(routePath + '/<filename:re:.*\.html>')
def html_file(filename):
    return static_file(filename, root=rootPath)

@route('/action', method='POST')
def action():
    val = request.forms.get('strState')
    on = bool(int(val))
    if on:
        sense.clear(255,0,0)
    else:
        sense.clear() 

run(host='0.0.0.0', port=8080, reloader=True)
