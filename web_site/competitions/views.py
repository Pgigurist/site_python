from django.shortcuts import render
from .models import Competition, Place
from django.http import Http404, HttpResponse, HttpResponseRedirect
# Create your views here.

def index(req):
    competitions = Competition.objects.all()

    return render(req, 'competitions/competitions.html', {'competitions' :competitions})


