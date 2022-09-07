from django.contrib import admin
from django.urls import path
from Inventory import views
from django.conf import settings
from django.urls import include


urlpatterns = [
    # Add a path/ url for the home page , and the respective view.
    path('home/', views.home, name='homeInventory'),
    
    
]