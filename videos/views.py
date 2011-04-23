from django.views.decorators.http import condition
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import *
from pytube.api.models import Api
from pytube.videos.models import *
from pytube.channels.models import getUserDict
import re
# Create your views here.

def play(request, id):
	api = Api()
	video = getVideoDict(api.GetYouTubeVideoEntry(video_id=id))
	author = getUserDict(api.GetYouTubeUserEntry(username=video['author']))
	related = []
	for entry in api.GetYouTubeRelatedVideoFeed(video_id=id).entry:
		related.append(getVideoDict(entry))
	flist = []
	for itag in sorted(getVideoQs(id).iterkeys()):
		qls = videoqls[itag]
		flist.append({
			'itag': itag,
			'name': qls['e'].upper(),
			'quality': qls['t']
		})

	print flist

	return render_to_response(
		"ytembed.html",
		{
			'video': video,
			'author': author,
			'related': related,
			'flist': flist
		},
		context_instance=RequestContext(request)
	)

@condition(etag_func=None)
def stream(request, id, itag):
	itag = int(itag)
	return HttpResponse(VidStream(id, itag), mimetype="video/%s" % videoqls[itag]['m'])

@condition(etag_func=None)
def get(request, id, itag):
	api = Api()
	video = getVideoDict(api.GetYouTubeVideoEntry(video_id=id))
	name = video['title'].replace(' ', '_')
	name = re.sub('[^-a-zA-Z0-9_.]+', '', name).replace('__', '_')
	itag = int(itag)
	response = HttpResponse(VidStream(id, itag), mimetype="video/%s" % videoqls[itag]['m'])
	response['Content-Disposition'] = 'attachment; filename=%s.%s' % (name, videoqls[itag]['e'])
	return response
