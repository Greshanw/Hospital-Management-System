from operator import add
from unicodedata import name
from django.urls import path
from .views import (
    add_patient,
    camera_feed,
    edit_patient,
    edit_patient_page,
    patients,
    patient_report,
    generate_qr,
    delete_patient,
    qr_scan_page,
    getCode,
    admin_logout
)

urlpatterns = [
    path('add-patient', add_patient, name='add-patient'),
    path('patients', patients, name='patients'),
    path('patients-report', patient_report, name='patients-report'),
    path('generate-qr/?<qr>', generate_qr, name='generate-qr'),
    path('delete-patient/?<id>', delete_patient, name='delete-patient'),
    path('edit-patient/?<id>', edit_patient_page, name='edit-patient'),
    path('editPatient/?<id>', edit_patient, name='edit-patient-function'),
    path('qr-scan', qr_scan_page, name='qr-scan'),
    path('camera_feed', camera_feed, name='camera_feed'),
    path('getCode', getCode, name='getCode'),
    path('logout', admin_logout, name='logout'),
]