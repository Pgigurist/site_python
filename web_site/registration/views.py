from django.shortcuts import render
from .models import MasterClass
from django.http import Http404
from django.template import Context, Template
from django.http import HttpResponse

# Create your views here.

def index(req):
    return HttpResponse("registration app")
    

def MKList(req):
    master_classes_list = MasterClass.objects.all()
    #print(master_classes_list)
    context = RequestContext = {'master_classes_list' : master_classes_list}
    return render(req, 'registration/index.html', context)

def MKDetalis(req, mk_id):
    try:
        mk = MasterClass.objects.get(pk=mk_id)
    except MasterClass.DoesNotExist:
        raise Http404('obj does not exist')
    return render(req, 'registration/mkdetalis.html', mk)

def Landing(req):

    return render(req, 'registration/landing.html')
