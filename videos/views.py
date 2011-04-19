from django.template import RequestContext
from django.shortcuts import *
from pytube.api.models import Api
from pytube.videos.models import getVideoDict
# Create your views here.

def play(request, id):
	api = Api()
	entry = getVideoDict(api.GetYouTubeVideoEntry(video_id=id))
	return render_to_response(
		"ytembed.html",
		{'video': entry},
		context_instance=RequestContext(request)
	)
