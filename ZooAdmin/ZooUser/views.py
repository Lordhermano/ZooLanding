from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'base.html')

def hotel(request):
    return render(request,'hotel.html')    

def signup(request):
    return render(request,'signup.html')