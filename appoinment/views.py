from multiprocessing import context
import secrets
from this import d
from django.shortcuts import render, redirect

from appoinment.models import appoinment


# Create your views here.
def Home(request):
    return render(request,'home.html')

def Contact(request):
    return render(request,'contact.html')

def About(request):
    return render(request,'about.html')

def Loginsign(request):
    return render(request,'loginsign.html')

def Login(request):
    return render(request,'login.html')


def add_appoinment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        speciality = request.POST.get('speciality')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        doctor = Doctor(name=name,phone=phone ,speciality=speciality,email=email)
        doctor.save()
        return redirect('doctors')
        

    return render(request, 'add_doctor.html')

def doctors(request):
    doctors = Doctor.objects.all()
    doctors_count = doctors.count()

    return render(request, 'doctors.html', {
        'doctors': doctors,'doctors_count':doctors_count
    })

def dashboard(request):
    doctors = Doctor.objects.all()
    doctors_count = doctors.count()

    return render(request, 'dashboard.html', {
        'doctors': doctors,'doctors_count':doctors_count
    })