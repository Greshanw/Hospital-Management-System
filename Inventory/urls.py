from django.contrib import admin
from django.urls import path
from Inventory import views
from django.conf import settings
from django.urls import include
from django.conf.urls.static import static


urlpatterns = [
    # Add a path/ url for the home page , and the respective view.
    path('home/', views.home, name='homeInventory'),
    path('medicines/', views.list_item, name='medicineList'),
    path('insert_medicine/', views.insert_product, name="insertMedicine"),
    path('generate_report/', views.generate_Report, name="generate_report"),
    path('scan_barcode/', views.main, name="scan_barcode"),
    path('product_Scaned/', views.product_Scaned, name='product_Scaned'),
    path('update_medicine/<str:pk>/', views.update_product, name="updateMedicine"),
     # url path to pass the ID of the object to be deleted. 
    path('delete_medicine/<str:pk>/', views.delete_items, name="deleteMedicine"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)