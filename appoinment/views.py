from multiprocessing import context
import secrets
from this import d
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, FileResponse
import csv
from django.http.response import StreamingHttpResponse, HttpResponse

from appoinment.models import Appoinment


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

       appoinment = Appoinment(Doctor_Name=Doctor_Name,Patient_Name=Patient_Name ,Date=Date,Time=Time)
       appoinment.save()
       return redirect('appoinment')
        

    return render(request, 'add_appoinment.html')
  
    

def appoinment(request):
    appoinments =Appoinment.objects.all()
    appoinments_count = appoinments.count()
    

    return render(request, 'appoinment.html', {
        'appoinments': appoinments,'appoinments_count':appoinments_count
    })

def dashboard(request):
    appoinments = Appoinment.objects.all()
    appoinments_count = appoinments.count()

   

    return render(request, 'dashboard.html', {
        'appoinments': appoinments,'appoinments_count':appoinments_count
    })


def patient_report(request):
    appoinments = Appoinment.objects.all()
    

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="appoinment_report.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['Doctor Name', 'PATIENT NAME', 'Date', 'Time'])
    for appoinment in appoinments:
       writer.writerow([appoinment.Doctor_Name, appoinment.Patient_Name, appoinment.Date, appoinment.Time])

    return response