from django.db import models

# Create your models here.


def getVideoDict(entry):
	try:
		duration = entry.media.duration.seconds
	except:
		duration = "FAIL"
	try:
		description = entry.content.text
	except:
		description = ""
	try:
		thumbnail = entry.media.thumbnail[1].url
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
	
	return {
		'title': entry.media.title.text,
		'date': entry.published.text,
		'description': description,
		'thumbnail': thumbnail,
		'keywords': keywords,
		'player': player,
		'author': author,
		'duration': duration,
		'id':	entry.id.text.split().pop()
	}
