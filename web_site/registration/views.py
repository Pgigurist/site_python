from django.shortcuts import render
from .models import MasterClass
from django.http import Http404
from django.template import Context, Template
from django.http import HttpResponse
from django.contrib import auth

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
    return render(req, 'registration/mkdetalis.html', mk)
    #pass

@login_user_required(login_url="/teacherPlan/login")
def Landing(req):
    if req.method == 'POST':
        username = req.POST['loginField']
        password = req.POST['passwordField']
        print username
        print passworuser
        user = auth.authenticate(username=username, password=password)

def account(req):

    """
    отдает user_data, user_entries, user_schedule
    :param req:
    :return:
    """
    pass