from django.db import models
from datetime import datetime
from xml.utils.iso8601 import parse
import locale
locale.setlocale(locale.LC_ALL, "")

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
	try:
		viewed_form = int(entry.statistics.view_count),
	except:
		viewed_form = 0

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
		'viewed': viewed,
		'viewed_formated': locale.format('%d', viewed_form, True)
	}
