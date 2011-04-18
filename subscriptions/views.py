# Create your views here.
from django.contrib import messages
from django.template import RequestContext
from django.shortcuts import *

from pytube.api.models import Api

from django.http import HttpResponse
from pytube.subscriptions.models import *
from pytube.videos.models import getVideoDict


import gdata.youtube
import gdata.youtube.service

import pp


def get_subscriptions(request):
	if 'token' in request.session:
		api = Api()
		api.SetAuthSubToken(request.session['token'])
		job_server = pp.Server(15, ppservers=())
		jobs = []
		for entry in api.GetYouTubeSubscriptionFeed().entry:
			uri = 'http://gdata.youtube.com/feeds/api/users/%s/uploads' % entry.username.text
			jobs.append(job_server.submit(gdata.youtube.service.YouTubeService().GetYouTubeUserFeed, (uri, None,), modules=("gdata.youtube", "gdata.youtube.service", )))
		feed = []
		for job in jobs:
			feed.extend(job().entry)
		job_server.destroy()
		#for entry in api.GetYouTubeSubscriptionFeed().entry:
		#	feed.extend(api.GetYouTubeUserFeed(username=entry.username.text).entry)
		feed.sort(key=lambda x: x.published.text, reverse=True)
		newfeed = []
		for entry in feed:
			newfeed.append(getVideoDict(entry))
		return render_to_response(
			"subscriptions.html",
			{'scrfeed': newfeed},
			context_instance=RequestContext(request)
		)
	else:
		return redirect("/")

def manage(request):
	return
