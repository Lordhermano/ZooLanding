from django.shortcuts import render
from .forms import CreateUserForm,LoginForm

# Create your views here.
def home(request):
    return render(request,'base.html')

def hotel(request):
    return render(request,'hotel.html')    

def signup(request):
    form = CreateUserForm()


    print(form)
    if request.method == "POST":
     form = CreateUserForm(request.POST)
     if form.is_valid():
        form.save()
    context = {"form":form}    
    return render(request,'signup.html',context)