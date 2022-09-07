from django.shortcuts import render
from .models import Inventory

# Create your views here.

#define what will be displayed in home.html
def home(request):
    #title of the view
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