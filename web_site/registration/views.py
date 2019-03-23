from django.shortcuts import render
from .models import MasterClass
from django.http import Http404
# Create your views here.

def index(req):
    return HttpResponse("registration app")

def MKList(req):
    master_classes_list = MasterClass.objects.all()
    context = RequestContext = {'master_classes_list' : master_classes_list}
    return render(req, 'registration/index.html', context)

def masterClassDetalis(req, masterClass_id):
    try:
        mk  = MasterClass.objects.get(pk=masterClass_id)
    except MasterClass.DoesNotExist:
        raise Http404
    return render(req, 'registration/masterClassDetalis.html', {'master_class' : mk})
