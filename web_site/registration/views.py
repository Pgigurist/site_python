from django.shortcuts import render #, redirect
from .forms import UserForm, UserProfileInfoForm
from django.contrib.auth import login, logout, authenticate
from django.http import Http404, HttpResponse, HttpResponseRedirect
#from django.template import Context, Template
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import MasterClass, Entry, Camp, TeamCoaches #, UserForm, UserProfileInfoForm



#from django.contrib.auth.forms import UserCreationForm


def index(req): #

    master_classes_list =  MasterClass.objects.all() # обьект для карусели, берем все МК,
                                                    # сортируем по id и забираем 3  последних элементаэлемента
    if "member_id" in req.session:
        print('user autorized!')

        return render(req, 'registration/index.html',{'master_classes_list': master_classes_list ,'auth' : 'yes'})
        #
    else:
        print('unknown user')
    return render(req, 'registration/index.html', {'master_classes_list' :master_classes_list})

def campList(req):

    context = {
            'camps' : Camp.objects.all(),
            'groups': MasterClass.objects.all()
            }
    return render(req, 'registration/camp.html', context)


def campDetalis(req, camp_id):


    context = {
                'camp' : Camp.objects.get(pk=camp_id),
 
                'coaches': TeamCoaches.objects.filter(camp=camp_id),
                'groups': MasterClass.objects.filter(camp=camp_id)
            }

    return render(req, 'registration/campDetalis.html', context)

def MKList(req):
    """
    """
    #print('new req with {} '.format(req.session[member_id]))
    master_classes_list = MasterClass.objects.all()
    #print(master_classes_list)
    if "member_id" in req.session:

        #entry_id_list =
        #entry_list = []
        #for entry_id in entry_id_list:
            #entry_list.append(MasterClass.objects.filter(foreginKey=entry_id.master_class_id))
        entries = Entry.objects.filter(user_id=req.user.id)
        entriesKeys = []
        for obj in entries:
            entriesKeys.append(obj.master_class_id.id)
        #print(entriesKeys)
        # entriesKeys - список id курсов, на конорые подписан пользователь
        # необходимо получить выбрать в переменную 'master_classes_list' те курсы,
        # шв которых не совпают с содержимым массива entriesKeys
        #master_classes_list = MasterClass.objects.filter(id__in=entr)

        context = RequestContext = {
            'master_classes_list': master_classes_list,
            'auth' : 'yes',
            'user': req.session['member_name'],
            'entries_list': Entry.objects.filter(user_id=req.session['member_id'])
        }
    else:
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

def createEntry(req):
    entry = Entry()
    entry.user_id = req.user
    entry.master_class_id = MasterClass.objects.get(pk=int(req.GET['mk_id']))
    
    state = MasterClass.objects.get(pk=int(req.GET['mk_id'])).incrimentSeat()
    if state:
        entry.save()
    return HttpResponseRedirect('/registration/list')

def removeEntry(req):
    instanse = Entry.objects.filter(user_id=req.user.id, master_class_id=int(req.GET['master_class_id']))
    #Entry.objects.filter(user_id=req.user.id, master_class_id=int(req.GET['mk_id']).delete()
    MasterClass.objects.get(pk=int(req.GET['master_class_id'])).decrimentSeat()
    instanse.delete()
    return HttpResponseRedirect('/registration/list')

@login_required
def special(request):
    return HttpResponse("Logged!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/registration/list')

def register(request): # передаем запрос, пользователю отдали форму,
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'registration/registration.html',
    {'user_form': user_form,
     'profile_form': profile_form,
     'registered': registered})

def user_login(request): #вход на сайт
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active: # 109-110 обьект session, к user вешаем два флага, id и name. для того чтобы во view было приветствие.
                login(request, user)
                request.session['member_id'] = user.id
                request.session['member_name'] = user.username

                print('new session with {} '.format(request.session['member_id']))
                return HttpResponseRedirect('/registration/list')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login detalis given")
    else:
        return render(request, 'registration/login.html', {})
