from django.db import models
from .utils import create_new_ref_number
import barcode
# to generate barcodes as imgages, have  to provide ImageWriter.
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File


# Here we create all tables related to this Inventory app.


 # this is the Inventory table
class Inventory(models.Model):
    Product_ID = models.CharField(max_length=13, blank=True, default=create_new_ref_number)
    BarCode = models.ImageField(upload_to='images/', blank=True)
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

    
    def create_unique_id(self):
        return str(random.randint(1111111111111,9999999999999))

    #overriding the save method.
    def save(self, *args, **kwargs):
        #getting the barcode type and save to EAN variable. here the used type is ean13
        EAN = barcode.get_barcode_class('ean13')
        #creating the barcode.
        ean = EAN(
            f'{self.Product_ID}', writer=ImageWriter())
            #save the barcode using ByteIO
        buffer = BytesIO()#chunk of memory that behaves like a file does.
        ean.write(buffer)
        # here refering the barcode field.
        self.BarCode.save(f'{self.Medicine_name}.png', File(buffer), save=False)# save false means we not saving here.
        return super().save(*args, **kwargs)