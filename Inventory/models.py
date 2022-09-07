from django.db import models


# Here we create all tables related to this Inventory app.

category_choice = (
    ('IT Equipment', 'IT Equipment'),
    ('Vegetables', 'Vegetables'),
    ('Fruits', 'Fruits'),
    ('Stationary', 'Stationary'),
    ('Beverages', 'Beverages'),
    ('Biscuits', 'Biscuits'),
    ('Bakery Products', 'Bakery Products'),
    ('Frozen Food', 'Frozen Food'),
    ('Personal Care', 'Personal Care'),
    ('Dairy', 'Dairy'),
)

 # this is the Inventory table
class Inventory(models.Model): 
    category = models.CharField(
        max_length=50, blank=True, null=True, choices=category_choice)
    Product_ID = models.CharField(max_length=12, blank=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    unit_price = models.FloatField(default='0.0', blank=True, null=True)
    selling_price = models.FloatField(default='0.0', blank=True, null=True)
    receive_quantity = models.IntegerField(
        default='0', blank=True, null=True)
    receive_by = models.CharField(max_length=50, blank=True, null=True)
    issue_quantity = models.IntegerField(
        default='0', blank=True, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    initial_inserted = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    export_to_CSV = models.BooleanField(default=False)


    #Change Object Display Name using __str__ function 
    def __str__(self):
        return self.item_name  # here str used to convert int to string

    
