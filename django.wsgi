import os
import sys

path = os.path.abspath(os.path.dirname(__file__)+"/../")
if path not in sys.path:
	sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'pytube.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

# add "WSGIScriptAlias / /path/to/this/file/pytube/django.wsgi" to apache config
