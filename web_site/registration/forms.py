from django import forms
from .models import *

class SubscriberForm(forms.ModelForm):

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