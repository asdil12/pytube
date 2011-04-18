from django.db import models

# Create your models here.
import gdata.youtube
import gdata.youtube.service

class Api(gdata.youtube.service.YouTubeService):
	def __init__(self):
		gdata.youtube.service.YouTubeService.__init__(self)
		self.ssl = False

	def authentificate(self, token):
		try:
			self.SetAuthSubToken(token)
			self.UpgradeToSessionToken()
			return True
		except:
			return False

