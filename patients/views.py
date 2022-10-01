from django.http import HttpResponseRedirect, FileResponse
import csv
import qrcode
from multiprocessing import context
import secrets
from django.shortcuts import render, redirect
from django.http.response import StreamingHttpResponse, HttpResponse

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

def patient_report(request):
    patients = Patient.objects.all()

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="patient_report.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['#', 'PATIENT NAME', 'Date of Birth', 'NIC', 'Phone', 'E-MAIL', 'Address'])
    for patient in patients:
        writer.writerow([patient.id, patient.name, patient.dob, patient.NIC, patient.phone, patient.email, patient.address])

    return response

def generate_qr(request, qr):
    name = 'myqr.png'
    img = qrcode.make(qr)
    img.save(name)
    download_image = open('./myqr.png', 'rb')
    
    response = FileResponse(download_image, as_attachment=True)
    return response

def delete_patient(request, id):
    Patient.objects.filter(id=id).delete()

    return redirect('patients')