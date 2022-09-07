from django.shortcuts import render
from .models import Inventory

# Create your views here.

# define what will be displayed in home.html


def home(request):
    # title of the view
    title = 'Welcome: DashBoard of the Inventory'
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
