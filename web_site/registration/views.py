from django.shortcuts import render
from .models import MasterClass
from django.http import Http404
from django.template import Context, Template
from django.http import HttpResponse

# Create your views here.

def index(req):
    #return HttpResponse("registration app")
    return render(req, 'registration/index.html')

def MKList(req):
    """
    нужно добавить вывод avelable_seats
    :param req:
    :return:
    """
    master_classes_list = MasterClass.objects.all()
    #print(master_classes_list)
    context = RequestContext = {'master_classes_list' : master_classes_list}
    return render(req, 'registration/list.html', context)

def MKDetalis(req, mk_id):
    """
    отдает данные о курсе: MasterClass<id>, Entries<mk_id>
    :param req:
    :param mk_id:
    :return:
    """
    try:
        mk = MasterClass.objects.get(pk=mk_id)
    except MasterClass.DoesNotExist:
        raise Http404('obj does not exist')
    #return render(req, 'registration/mkdetalis.html', mk)
    pass

def Landing(req):

    return render(req, 'registration/landing.html')

def account(req):
    """
    отдает user_data, user_entries, user_schedule
    :param req:
    :return:
    """
    pass