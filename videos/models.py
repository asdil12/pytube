from django.db import models
from datetime import datetime
from xml.utils.iso8601 import parse
import cookielib, urllib2, json, re


videoqls = {
	5 : {'e': 'flv', 't': '240p'},
	13: {'e': '3gp', 't': '240p'},
	17: {'e': 'mp4', 't': '240p'},
	18: {'e': 'mp4', 't': 'medium'},
	34: {'e': 'flv', 't': '360p'},
	35: {'e': 'flv', 't': '480p'},
	22: {'e': 'mp4', 't': '720p'},
	37: {'e': 'mp4', 't': '1080p'},
	38: {'e': 'video', 't': 'original'}, # You actually don't know if this will be MOV, AVI or whatever (maybe original video - high)
	43: {'e': 'webm', 't': 'medium'},
	45: {'e': 'webm', 't': '720p'},
}

def getVideoDict(entry):
	try:
		duration = datetime.fromtimestamp(int(entry.media.duration.seconds)).strftime("%M:%S")
	except:
		duration = "FAIL"
	try:
		description = entry.content.text
	except:
		description = ""
	try:
		thumbnail = entry.media.thumbnail[0].url.replace('0.jpg', 'default.jpg', 1)
	except:
		thumbnail = "ADD_DEFAULT_VIDEO_ICON_URL"
	try:
		keywords = entry.media.keywords.text
	except:
		keywords = ""
	try:
		author = entry.author[0].name.text
	except:
		author = ""
	try:
		player = entry.media.player.url
	except:
		player = ""
	try:
		published = datetime.fromtimestamp(parse(entry.published.text)).strftime("%d.%m.%Y")
	except:
		published = ""
	try:
		viewed = entry.statistics.view_count,
	except:
		viewed = ""

	return {
		'title': entry.media.title.text,
		'date': entry.published.text,
		'description': description,
		'thumbnail': thumbnail,
		'keywords': keywords,
		'player': player,
		'author': author,
		'duration': duration,
		'id':	entry.id.text.split('/').pop(),
		'published': published,
		'viewed': viewed
	}

def getVideoQs(vid):
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	ck = cookielib.Cookie(version=0, name='PREF', value='f2=40000000', port=None, port_specified=False,
												domain='youtube.com', domain_specified=True, domain_initial_dot=False, path='/',
												path_specified=True, secure=False, expires=None, discard=True, comment=None,
												comment_url=None, rest={'HttpOnly': None}, rfc2109=False)
	cj.set_cookie(ck)
	response = opener.open("http://www.youtube.com/watch?v=%s" % vid)
	out = response.read()
	jstr = re.search(r'\'PLAYER_CONFIG\':\s(?P<url_map>.+)\s}\);', out).group('url_map')
	jenc = json.loads(jstr)

	flist = {}
	try:
		for item in jenc['args']['fmt_url_map'].split(','):
			it = item.split('|')
			flist[int(it[0])] = videoqls[int(it[0])]
	except KeyError:
		pass
	try:
		for i in jenc['args']['html5_fmt_map']:
			flist[int(i['itag'])] = videoqls[int(i['itag'])]
	except KeyError:
		pass
	return flist

def streamVideo(vid, itag):
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	ck = cookielib.Cookie(version=0, name='PREF', value='f2=40000000', port=None, port_specified=False,
												domain='youtube.com', domain_specified=True, domain_initial_dot=False, path='/',
												path_specified=True, secure=False, expires=None, discard=True, comment=None,
												comment_url=None, rest={'HttpOnly': None}, rfc2109=False)
	cj.set_cookie(ck)
	response = opener.open("http://www.youtube.com/watch?v=%s" % vid)
	out = response.read()
	jstr = re.search(r'\'PLAYER_CONFIG\':\s(?P<url_map>.+)\s}\);', out).group('url_map')
	jenc = json.loads(jstr)

	flist = {}
	try:
		for item in jenc['args']['fmt_url_map'].split(','):
			it = item.split('|')
			flist[int(it[0])] = it[1]
	except KeyError:
		pass
	try:
		for i in jenc['args']['html5_fmt_map']:
			flist[int(i['itag'])] = i['url']
	except KeyError:
		pass

	url = flist[itag]
	# Do not include the Accept-Encoding header
	headers = {'Youtubedl-no-compression': 'True'}
	request = urllib2.Request(url, None, headers)
	try:
		data = opener.open(request)
		return data.read()
	except IOError:
		# SIGHUP: Pipe closed
		pass
	return False
