from multiprocessing import context
from django.shortcuts import render
from .forms import PatientForm

# Create your views here.
def add_patient(request):
    forms = PatientForm()
    context = {
        'form' : forms,
    }
    return render(request, 'add_patient.html', context)

def patients(request):
    return render(request, 'patients.html')