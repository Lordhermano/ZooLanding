from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms 
from django.forms.widgets import PasswordInput, TextInput

class CreationUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ["Firstname","Lastname","Email","Password1","Password2"]


class LoginForm(AuthenticationForm):
    email = forms.CharField(min_length=3,widget=TextInput())
    password = forms.CharField(min_length=8,widget=PasswordInput())