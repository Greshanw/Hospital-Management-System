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
       Doctor_Name = request.POST.get('Doctor_Name')
       Patient_Name = request.POST.get('Patient_Name')
       Date = request.POST.get('Date')
       Time = request.POST.get('Time')

       appoinment = appoinment(Doctor_Name=Doctor_Name,Patient_Name=Patient_Name ,Date=Date,Time=Time)
       appoinment.save()
    return redirect('appoinment')
        

    return render(request, 'add_appoinment.html')

def appoinment(request):
    appoinment =appoinment.objects.all()
    appoinment_count = appoinment.count()

    return render(request, 'appoinment.html', {
        'appoinment': appoinment,'appoinment_count':appoinment_count
    })

def dashboard(request):
    appoinment = appoinment.objects.all()
    appoinment_count = appoinment.count()

    return render(request, 'dashboard.html', {
        'appoinment': appoinment,'appoinment_count':appoinment_count
    })