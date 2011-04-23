from django.views.decorators.http import condition
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import *
from pytube.api.models import Api
from pytube.videos.models import *
from pytube.channels.models import getUserDict
# Create your views here.

def play(request, id):
	api = Api()
	video = getVideoDict(api.GetYouTubeVideoEntry(video_id=id))
	author = getUserDict(api.GetYouTubeUserEntry(username=video['author']))
	related = []
	for entry in api.GetYouTubeRelatedVideoFeed(video_id=id).entry:
		related.append(getVideoDict(entry))
	return render_to_response(
		"ytembed.html",
		{
			'video': video,
			'author': author,
			'related': related
		},
		context_instance=RequestContext(request)
	)

@condition(etag_func=None)
def get(request, id, itag):
	itag = int(itag)
	return HttpResponse(VidStream(id, itag), mimetype="video/%s" % videoqls[itag]['m'])
