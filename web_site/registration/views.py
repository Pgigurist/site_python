from django.shortcuts import render #, redirect
from .forms import UserForm, UserProfileInfoForm
from django.contrib.auth import login, logout, authenticate
from django.http import Http404, HttpResponse, HttpResponseRedirect
#from django.template import Context, Template
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import MasterClass #, UserForm, UserProfileInfoForm



#from django.contrib.auth.forms import UserCreationForm

# Create your views heqqg
"""
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
"""

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

@login_required
def special(request):
    return HttpResponse("Logged!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
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

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login detalis given")
    else:
        return render(request, 'registration/login.html', {})
