from django.db import models
from .utils import create_new_ref_number


# Here we create all tables related to this Inventory app.


 # this is the Inventory table
class Inventory(models.Model):
    Product_ID = models.CharField(max_length=12, blank=True, default=create_new_ref_number)
    Medicine_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    Net_price = models.FloatField('Net Price(Rs.)',default='0.0', blank=True, null=True)
    receive_quantity = models.IntegerField(
        default='0', blank=True, null=True)
    Vendor = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    initial_inserted = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    export_to_CSV = models.BooleanField(default=False)


    #Change Object Display Name using __str__ function 
    def __str__(self):
        return self.Medicine_name  # here str used to convert int to string

    
    def create_unique_id():
        return str(random.randint(111111111111,999999999999))