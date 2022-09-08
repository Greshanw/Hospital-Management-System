from django.shortcuts import render, redirect
from .models import Inventory
from .form import *
from django.contrib import messages

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
        
    # assign all the objects in the Inventory to the queryset
    queryset = Inventory.objects.all()
    context = {
        "title": title,
        "queryset": queryset,  # to list out all objects
            
    }
        
    return render(request, "InventoryList.html", context)


def insert_product(request):
    form = InventoryCreateForm(request.POST or None)
    if form.is_valid(): # checking the validation of form data
        form.save() # save data in database
        messages.success(request, 'Successfully inserted the product')
        # this allow you the page to be redirected to another after saving data
        return redirect('/medicines')
    context = {
        "form": form,
        "title": "Insert Product",
    }
    return render(request, "InsertProduct.html", context)