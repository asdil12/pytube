from django.http import HttpResponse

def r_search(request):
	if 'q' in request.GET:
		return search(request, query=request.GET['q'])
	else:
		return form(request)

def search(request, query):
	return HttpResponse(query)

def form(request):
	return HttpResponse("form")
