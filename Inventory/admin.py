from django.contrib import admin
from .models import Inventory

# Register your models here.

# register the model in admin in order to insert  data into database table.

admin.site.register(Inventory)