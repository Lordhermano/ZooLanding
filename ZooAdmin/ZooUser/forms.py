from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import ZooUser

from django import forms 
from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):

    class Meta:

        model = ZooUser
        fields = ["first_name","last_name","email","password1","password2"]


class LoginForm(AuthenticationForm):
    email = forms.CharField(min_length=3,widget=TextInput())
    password = forms.CharField(min_length=8,widget=PasswordInput())