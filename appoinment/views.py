from multiprocessing import context
import secrets
from django.db.models import Q
from django.views.generic import ListView
from this import d
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, FileResponse
import csv
from django.http.response import StreamingHttpResponse, HttpResponse

from appoinment.models import Appoinment


# Create views here.
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

def Sign(request):
    return render(request,'sign.html')

#add appoinment
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
  
    
#appoinment
def appoinment(request):
    appoinments =Appoinment.objects.all()
    appoinments_count = appoinments.count()
    
    if request.method == 'GET':
        search = request.GET.get('search')
        
        if(search):
            appoinments = Appoinment.objects.filter(
                Q(Doctor_Name__contains = search) | 
                Q(id__contains = search)
                
            )

    return render(request, 'appoinment.html', {
        'appoinments': appoinments,'appoinments_count':appoinments_count
    })

def dashboard(request):
    appoinments = Appoinment.objects.all()
    appoinments_count = appoinments.count()

   

    return render(request, 'dashboard.html', {
        'appoinments': appoinments,'appoinments_count':appoinments_count
    })

# Generate Reports
def appoinment_report(request):
    appoinments = Appoinment.objects.all()
    

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="appoinment_report.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['ID','Doctor Name', 'PATIENT NAME', 'Date', 'Time'])
    for appoinment in appoinments:
       writer.writerow([appoinment.id,appoinment.Doctor_Name, appoinment.Patient_Name, appoinment.Date, appoinment.Time])

    return response

#delete appoinment
def delete_appoinment(request, id):
    Appoinment.objects.filter(id=id).delete()

    return redirect('appoinment')

#update_appoinment
def update_appoinment_page(request, id):
    appoinment = Appoinment.objects.filter(id=id).get()
    
    return render(request, 'update_appoinment.html', {
        'appoinment': appoinment
    })

def update_appoinment(request, id):
    try:
        if request.method == 'POST':
            Doctor_Name = request.POST.get('Doctor_Name')
            Patient_Name = request.POST.get('Patient_Name')
            Date = request.POST.get('Date')
            Time = request.POST.get('Time')

            appoinment = Appoinment.objects.get(id=id)
            appoinment.Doctor_Name = Doctor_Name
            appoinment.Patient_Name = Patient_Name
            appoinment.Date = Date
            appoinment.Time = Time
            appoinment.save(update_fields=['Doctor_Name','Patient_Name','Date','Time'])
    except:
        return redirect('appoinment')

    return redirect('appoinment')
    



    