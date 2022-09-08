from django.shortcuts import render, redirect
from .models import Inventory
from django.http import HttpResponse
from .form import *
from django.contrib import messages
import csv

# Create your views here.

# define what will be displayed in home.html


def home(request):
    # title of the view
    title = 'DashBoard of the Inventory'
    queryset = Inventory.objects.all()

    # inside the context stores the variables
    # these variables can be called from the html page
    context = {
        "title": title,
        "Inventory": Inventory,
        "queryset": queryset
    }
    # return the html page and the context
    return render(request, "home.html", context)

def list_item(request):
    title = 'List of Medical Products'
    form = InventorySearchForm(request.POST or None)
        
    # assign all the objects in the Inventory to the queryset
    queryset = Inventory.objects.all()
    context = {
        "title": title,
        "queryset": queryset,  # to list out all objects
         "form": form,   
    }
    if request.method == 'POST': # if press the search button
        queryset = Inventory.objects.filter(Medicine_name__icontains=form['Medicine_name'].value())

    context = {
        "title": title,
        "form": form,
        "queryset": queryset,
    }
    return render(request, "InventoryList.html", context)


def insert_product(request):
    form = InventoryCreateForm(request.POST or None)
    if form.is_valid(): # checking the validation of form data
        form.save() # save data in database
        messages.success(request, 'Successfully inserted the Medical product')
        # this allow you the page to be redirected to another after saving data
        return redirect('/medicines')
    context = {
        "form": form,
        "title": "Insert Product",
    }
    return render(request, "InsertProduct.html", context)


def generate_Report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="List of Medicines.csv"'
    writer = csv.writer(response)
    writer.writerow([ 'Medicine NAME', 'QUANTITY',
                        'Net PRICE', 'Vendor'])
    queryset = Inventory.objects.all().values_list('Medicine_name', 'quantity',
                        'Net_price', 'Vendor')
    
    for stock in queryset:
        writer.writerow(stock)
    return response