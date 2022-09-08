from operator import add
from django.urls import path
from .views import (
    add_patient,
    patients
)

urlpatterns = [
    path('add-patient', add_patient, name='add-patient'),
    path('patients', patients, name='patients')
]