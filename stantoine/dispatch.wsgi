"""
WSGI config for stantoine project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys

sys.path.insert(1, os.path.abspath("."))
sys.path.insert(1, os.path.abspath("./libs"))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stantoine.settings")

application = get_wsgi_application()
