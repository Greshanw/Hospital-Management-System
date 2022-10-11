from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import secrets
import csv
from django.db.models import Q
from this import d
from django.shortcuts import render, redirect


from doctors.models import Doctor



#add doctors
def add_doctor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        speciality = request.POST.get('speciality')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        doctor = Doctor(name=name,phone=phone ,speciality=speciality,email=email)
        doctor.save()
        return redirect('doctors')
        

    return render(request, 'add_doctor.html')

#doctors 
def doctors(request):
    doctors = Doctor.objects.all()
    doctors_count = doctors.count()

    if request.method == 'GET':
        search = request.GET.get('search')
        
        if(search):
            doctors = Doctor.objects.filter(
                Q(name__contains = search) | 
                Q(id__contains = search)
                
            )

    return render(request, 'doctors.html', {
        'doctors': doctors,'doctors_count':doctors_count
    })

def dashboard(request):
    doctors = Doctor.objects.all()
    doctors_count = doctors.count()

    return render(request, 'dashboard.html', {
        'doctors': doctors,'doctors_count':doctors_count
    })

#get the id as a parameter to find the specific record and load the UI for update details
# def update_doctor(request,id):
#     doctor = Doctor.objects.get(id=id)
#     template = loader.get_template('update_doctor.html')
#     context = {
#     'doctor': doctor,
#     }
#     return HttpResponse(template.render(context, request))

# def update_doctor_record(request, id):
#     name = request.POST.get('name')
#     speciality = request.POST.get('speciality')
#     phone = request.POST.get('phone')
#     email = request.POST.get('email')
#     doctor = Doctor.objects.get(id=id)
#     doctor.name = name
#     doctor.speciality = speciality
#     doctor.phone = phone
#     doctor.email = email
#     doctor.save(update_fields=['name','speciality','phone','email'])
#     return HttpResponseRedirect(reverse('index'))

def update_doctor_page(request, id):
    doctor = Doctor.objects.filter(id=id).get()
    
    return render(request, 'update_doctor.html', {
        'doctor': doctor
    })

def update_doctor(request, id):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            speciality = request.POST.get('speciality')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            

            doctor = Doctor.objects.get(id=id)
            doctor.name = name
            doctor.speciality = speciality
            doctor.phone = phone
            doctor.email = email
            
            doctor.save(update_fields=['name','speciality', 'phone','email'])
    except:
        return redirect('doctors')
    
    return redirect('doctors')


    
# Generate Reports
def doctors_report(request):
    doctors = Doctor.objects.all()

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="Doctors_report.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['ID', 'Doctor Name', 'Speciality', 'Contact-No', 'EMAIL'])
    for doctor in doctors:
        writer.writerow([doctor.id, doctor.name, doctor.speciality, doctor.phone, doctor.email,])

    return response

#delete doctor
def delete_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    # doctor.delete()
    # return redirect('doctors')
    if request.method == "POST":
        doctor.delete()
    context = {
        "object" : doctor
    }
    return render(request,"confirmation_dialog.html",context)

#saerch doctor by name or id

