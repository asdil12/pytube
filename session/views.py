from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from pytube.api.models import Api

def clearsession(session):
	try:
		del session['username']
		del session['token']
		return True
	except KeyError:
		return False

def login(request):
	next = request.build_absolute_uri(reverse(process_token))
	scope = 'http://gdata.youtube.com'
	secure = False
	session = True

	redirect_url = Api().GenerateAuthSubURL(next, scope, secure, session).to_string()
	return redirect(redirect_url)

def process_token(request):
	if 'token' in request.GET:
		try:
			api = Api()
			if api.authentificate(request.GET['token']):
				request.session['username'] = api.GetYouTubeUserEntry(username='default').author[0].name.text
				request.session['token'] = api.GetAuthSubToken()
				messages.success(request, "You're logged in.")
				return redirect("/")
		except:
			clearsession(request.session)
			messages.error(request, "API Fail!")
			return redirect("/")
	else:
		clearsession(request.session)
		messages.error(request, "No Token given!")
		return redirect("/")

def logout(request):
	if 'token' in request.session:
		try:
			api = Api()
			api.SetAuthSubToken(request.session['token'])
			api.RevokeAuthSubToken()
		except:
			pass
	clearsession(request.session)
	messages.success(request, "You're logged out.")
	return redirect("/")
