from django.urls import path,include

from . import views

urlpatterns = [path('',views.home,name=''),
    path('hotel',views.hotel,name='hotel')]