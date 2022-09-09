from operator import add
from django.urls import path
from .views import (
    add_doctor,
    doctors,
    dashboard
)

urlpatterns = [
    
    path('dashboard',dashboard,name='dashboard'),
    path('add-doctor', add_doctor, name='add-doctor'),
    path('doctors', doctors, name='doctors')
]