#!/usr/bin/python3.6

import os, sys, logging

application = None 

try:
    dirName = os.path.abspath(os.path.dirname(__file__) + '/..')
    sys.path.insert(1, dirName)
    sys.path.insert(1, dirName + "/libs")
    from django.core.wsgi import get_wsgi_application
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stantoine.settings")
    application = get_wsgi_application()
except Exception as e:
    err = e
    def _application(env, start_response):
        global err
        start_response('200 OK', [('Content-Type','text/html')])
        return [b"Error: ", str(err).encode('ascii')]

    application = _application

