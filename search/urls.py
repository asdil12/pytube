from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('pytube.search.views',
	# Example:
	# (r'^pytube/', include('pytube.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# (r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	# (r'^admin/', include(admin.site.urls)),
	(r'^/?$', 'r_search'),
	(r'^/form/?$', 'form'),
	(r'/(?P<query>.*)$', 'search'),
)
