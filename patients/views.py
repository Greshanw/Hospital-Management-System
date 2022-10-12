from distutils.log import error
from django.http import JsonResponse
from django.http import HttpResponseRedirect, FileResponse
import csv
import qrcode
from multiprocessing import context
import secrets
from django.shortcuts import render, redirect
from django.http.response import StreamingHttpResponse, HttpResponse
from patients.camera import Camera

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

def edit_patient_page(request, id):
    patient = Patient.objects.filter(id=id).get()
    
    return render(request, 'edit_patient.html', {
        'patient': patient
    })

def edit_patient(request, id):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            dob = request.POST.get('dob')
            nic = request.POST.get('nic')
            email = request.POST.get('email')
            address = request.POST.get('address')

            patient = Patient.objects.get(id=id)
            patient.name = name
            patient.phone = phone
            patient.dob = dob
            patient.NIC = nic
            patient.email = email
            patient.address = address
            patient.save(update_fields=['name','phone','dob','NIC','email','address'])
    except:
        return redirect('patients')
    
    return redirect('patients')

class qr:
    def __init__(self):
        self.code = 'None'

    def setqr(self, code):
        self.code = code

    def getqr(self):
        return self.code

obj = qr()

# frameobj = Camera()

def qr_scan_page(request):
    patient = {
        "id": 0,
        "name": "",
        "phone": "",
        "dob": "",
        "nic": "",
        "email": "",
        "address": ""
    }

    return render(request, 'scan_qr.html', {
        'patient' : patient
    })

def gen(camera):
    while True:
        frame, code = camera.get_frame()
        codebyte = bytes(str(code), 'utf-8')
        obj.setqr(code)
        # print(code)
        
        yield (b'--frame\r\n' 
            b'Content_Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n' + codebyte)

def camera_feed(request):
    frame = gen(Camera())
    # frame = gen(frameobj)

    return StreamingHttpResponse(frame, content_type='multipart/x-mixed-replace; boundary=frame')

def test(request):
    code = obj.getqr()
    patient = {
        "id": 0,
        "name": "",
        "phone": "",
        "dob": "",
        "nic": "",
        "email": "",
        "address": ""
    }
    
    try:
        dbres = Patient.objects.get(qr=str(code))
        patient = {
            "id": dbres.id,
            "name": dbres.name,
            "phone": dbres.phone,
            "dob": dbres.dob,
            "nic": dbres.NIC,
            "email": dbres.email,
            "address": dbres.address
        }
    except : 
        print("Invalid Code")

    return JsonResponse({'patient': patient})