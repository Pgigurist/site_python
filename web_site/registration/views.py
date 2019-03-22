from django.shortcuts import render
from .models import MasterClass
# Create your views here.

def index(req):
    return HttpResponse("registration app")

def MKList(req):
    master_classes_list = MasterClass.objects.order_by('date_start')[:7]
    context = RequestContext = {'master_classes_list' : master_classes_list}
    return render(req, 'registration/index.html', context)
