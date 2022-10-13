from operator import add
from django.urls import path
from .views import About,Home,Contact,Loginsign,add_appoinment,update_appoinment_page,appoinment,dashboard,appoinment_report,delete_appoinment,Login,Sign,update_appoinment



urlpatterns = [
    path('',Home, name='home'),
    path('contact/',Contact, name='contact'),
    path('about/',About, name='about'),
    path('loginsign/',Loginsign, name='loginsign'),
    path('dashboard/',dashboard,name='dashboard'),
    path('add_appoinment/', add_appoinment, name='add_appoinment'),
    path('appoinment/', appoinment, name='appoinment'),
    path('appoinment_report/', appoinment_report, name='appoinment_report'),
    path('delete_appoinment/?<id>',delete_appoinment,  name='delete_appoinment'),
    path('login/',Login, name='login'),
    path('sign/',Sign, name='sign'),
    path('update_appoinment/?<id>', update_appoinment_page, name='update_appoinment'),
    path('updateAppoinment/?<id>',update_appoinment, name='update-appoinment-function')
    
]
    





