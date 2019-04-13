from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm (UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    group_id = forms.CharField(max_length=30, required = False, help_text='Optional.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'group_id', 'email', 'password1', 'password2', )
class SubscriberForm (forms.ModelForm):

    class Meta:
        model = MasterClass
        exclude = [""]

class RegisterUserForm(forms.form):
    username = CharField(
        label='Логин',
        max_length=100,
        required=True,
    )
    email = EmailField(
        label="Email",
        max_length=100,
        required=True,
    )
    password = CharField(
        label="Пароль",
        max_length=100,
        required=True,
    )
    first_name = CharField(
        label="Имя",
        max_length=100,
        required=True,
    )
    last_name = CharField(
        label="Фамилия",
        max_length=100,
        required=True,
    )