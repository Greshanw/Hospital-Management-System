from django.contrib import admin
from .models import Inventory
from .form import InventoryCreateForm

# Register your models here.

class InventoryCreateAdmin(admin.ModelAdmin): 
    #list display define what to see in the admin site table 
    list_display = ['Product_ID','Medicine_name', 'quantity', 'Net_price',  'receive_quantity', 'Vendor',
                  'reorder_level']

    form = InventoryCreateForm
    # search any row using the category and item name
    search_fields = ['Medicine_name']

# register the model in admin in order to insert  data into database table.
admin.site.register(Inventory, InventoryCreateAdmin)