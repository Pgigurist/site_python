from django.http import HttpResponse

# Create your views here.

def index(req):
    return HttpResponse("registration app")
