import os, sys

sys.path.append("/srv")
sys.path.append("/srv/libs")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stantoine.settings")

application = get_wsgi_application()