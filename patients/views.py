from multiprocessing import context
from re import search
import secrets
from this import d
from unicodedata import name
from django.shortcuts import render, redirect

from patients.models import Patient
from django.db.models import Q

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

    if request.method == 'GET':
        search = request.GET.get('search')
        if(search):
            patients = Patient.objects.filter(
                Q(name__contains = search) | 
                Q(NIC__contains = search) | 
                Q(phone__contains = search)
            )

    return render(request, 'patients.html', {
        'patients': patients
    })