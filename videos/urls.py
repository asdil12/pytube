from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('pytube.videos.views',
	# Example:
	# (r'^pytube/', include('pytube.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# (r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	# (r'^admin/', include(admin.site.urls)),
	(r'/(?P<id>.*)/get/(?P<itag>\d+)$', 'get'),
	(r'/(?P<id>.*)/stream/(?P<itag>\d+)$', 'stream'),
	(r'/(?P<id>.*)$', 'play'),
)
