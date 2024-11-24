from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Record

from django import forms 
from django.forms.widgets import PasswordInput, TextInput

class CreateRecord(models.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','last_name','email','password']
