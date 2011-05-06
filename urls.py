from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.static import serve
from django.conf import settings

_media_url = settings.MEDIA_URL
if _media_url.startswith('/'):
	_media_url = _media_url[1:]

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	# Example:
	# (r'^pytube/', include('pytube.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# (r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	# (r'^admin/', include(admin.site.urls)),
	(r'^%s(?P<path>.*)$' % _media_url, serve, {'document_root': settings.MEDIA_ROOT}),
	(r'^login$', 'pytube.session.views.login'),
	(r'^login/process_token$', 'pytube.session.views.process_token'),
	(r'^logout$', 'pytube.session.views.logout'),
	(r'^$', direct_to_template, {'template': 'index.html'}),
	(r'^subscriptions', include('pytube.subscriptions.urls')),
	(r'^video', include('pytube.videos.urls')),
	(r'^search', include('pytube.search.urls')),
)
