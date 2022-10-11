from operator import add
from unicodedata import name
from django.urls import path
from .views import (
    add_doctor,
    delete_doctor,
    doctors,
    dashboard,
    update_doctor,
    update_doctor_page,
    doctors_report,

)

urlpatterns = [
    
    path('dashboard',dashboard,name='dashboard'),
    path('add-doctor', add_doctor, name='add-doctor'),
    path('doctors', doctors, name='doctors'),
    path('update-doctor/?<id>',update_doctor_page, name='update-doctor'),
    path('updatedoctor/?<id>', update_doctor, name='updatedoctor'),
    path('doctors-report', doctors_report, name='doctors-report'),
    path('delete-doctor/?<id>', delete_doctor, name='delete-doctor'),


]