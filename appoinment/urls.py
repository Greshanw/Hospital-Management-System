from operator import add
from django.urls import path
from .views import About,Home,Contact,Loginsign,add_appoinment,appoinment,dashboard



urlpatterns = [
    path('',Home, name='home'),
    path('contact/',Contact, name='contact'),
    path('about/',About, name='about'),
    path('loginsign/',Loginsign, name='loginsign'),
     path('dashboard',dashboard,name='dashboard'),
    path('add_appoinment', add_appoinment, name='add_appoinment'),
    path('appoinment', appoinment, name='appoinment'),
    
   
    
]




