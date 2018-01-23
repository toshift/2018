from django.http import HttpResponse

def index(request):
    return HttpResponse("Test Hello World Django!")