from django.db import models
from datetime import datetime
from xml.utils.iso8601 import parse
import locale
locale.setlocale(locale.LC_ALL, "")

def getUserDict(user):
	try:
		date = datetime.fromtimestamp(parse(user.published.text)).strftime("%d.%m.%Y")
	except:
		date = ""
	try:
		description = user.description.text
	except:
		description = ""
	try:
		thumbnail = user.thumbnail.url
	except:
		thumbnail = "ADD_DEFAULT_VIDEO_ICON_URL"
	
	return {
		'name': user.username.text,
		'date': date,
		'description': description,
		'thumbnail': thumbnail,
		'subscribed': user.statistics.subscriber_count,
		'subscribed_formated': locale.format('%d', int(user.statistics.subscriber_count), True)
	}
