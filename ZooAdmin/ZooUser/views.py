from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'base.html')

def hotel(request):
    return render(request,'hotel.html')    