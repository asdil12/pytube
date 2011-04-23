import os
import sys

path = os.path.abspath(os.path.dirname(__file__)+"/../")
if path not in sys.path:
	sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'pytube.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()



# add this to apache config:
# WSGIScriptAlias / /path/to/this/file/pytube/django.wsgi
# WSGIDaemonProcess site-1 user=www-data group=www-data threads=25
# WSGIProcessGroup site-1
