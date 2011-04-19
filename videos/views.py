from django.template import RequestContext
from django.shortcuts import *
from pytube.api.models import Api
from pytube.videos.models import getVideoDict
from pytube.channels.models import getUserDict
# Create your views here.

def play(request, id):
	api = Api()
	entry = getVideoDict(api.GetYouTubeVideoEntry(video_id=id))
	author = getUserDict(api.GetYouTubeUserEntry(username=entry['author']))
	return render_to_response(
		"ytembed.html",
		{
			'video': entry,
			'author': author
		},
		context_instance=RequestContext(request)
	)
