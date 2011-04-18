def username(request):
	username = request.session['username'] if 'username' in request.session else ""
	return {'username': username}

def logged_in(request):
	logged_in = True if 'token' in request.session else False
	return {'logged_in': logged_in}
