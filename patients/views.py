from multiprocessing import context
import secrets
from this import d
from django.shortcuts import render, redirect

from patients.models import Patient

# Create your views here.
def add_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        nic = request.POST.get('nic')
        email = request.POST.get('email')
        address = request.POST.get('address')
        qr = secrets.token_hex(16)

        patient = Patient(name=name,phone=phone ,dob=dob ,NIC=nic ,email=email ,address=address, qr=qr)
        patient.save()
        return redirect('patients')
        

    return render(request, 'add_patient.html')

def patients(request):
    patients = Patient.objects.all()

    return render(request, 'patients.html', {
        'patients': patients
    })