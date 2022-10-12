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

def Sign(request):
    return render(request,'sign.html')

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


def appoinment_report(request):
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

def delete_appoinment(request, id):
    Appoinment.objects.filter(id=id).get().delete()

    return redirect('appoinment')

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
    
class appoinment_searchResultsView(ListView):
    model = Appoinment
    template_name = 'appoinment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('appoinment')
        context['appoinment'] = Appoinment.objects.filter(
            Q(id__icontains=query) | Q(Doctor_Name__icontains=query)
        )
        return context


    