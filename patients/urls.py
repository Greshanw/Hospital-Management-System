from operator import add
from django.urls import path
from .views import (
    add_patient,
    patients,
    patient_report,
    generate_qr,
    delete_patient
)

urlpatterns = [
    path('add-patient', add_patient, name='add-patient'),
    path('patients', patients, name='patients'),
    path('patients-report', patient_report, name='patients-report'),
    path('generate-qr/?<qr>', generate_qr, name='generate-qr'),
    path('delete-patient/?<id>', delete_patient, name='delete-patient')
]