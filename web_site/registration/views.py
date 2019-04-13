from django.shortcuts import render, redirect
from .models import MasterClass
from django.http import Http404, HttpResponse
from django.template import Context, Template
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import *
# Create your views here.
def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print('test')
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

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

def Landing(req):

    return render(req, 'registration/landing.html')

def account(req):
    """
    отдает user_data, user_entries, user_schedule
    :param req:
    :return:
    """
    pass
def signup(req):
   return render(req, 'registration/signup.html')