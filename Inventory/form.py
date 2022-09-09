from django import forms
from .models import Inventory

# Create a form
class InventoryCreateForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['Product_ID','Medicine_name', 'quantity', 'Net_price',  'receive_quantity', 'Vendor',
                  'reorder_level']
    #validation the input fields
    def clean_Product_ID(self):
        Product_ID = self.cleaned_data.get('Product_ID')
        if not Product_ID:  # if it is blank
            raise forms.ValidationError('This field is required')

        for instance in Inventory.objects.all():
            if instance.Product_ID == Product_ID:
                raise forms.ValidationError(
                    Product_ID + ' is already created')
            
        if len(Product_ID) > 12:
            raise forms.ValidationError(
                 ' Quantity should be greater than 0')
        return Product_ID

    def clean_Medicine_name(self):
        Medicine_name = self.cleaned_data.get('Medicine_name')
        if not Medicine_name:
            raise forms.ValidationError('This field is required')

        for instance in Inventory.objects.all():
            if instance.Medicine_name == Medicine_name:
                raise forms.ValidationError(
                    Medicine_name + ' is already created')

        return Medicine_name

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if not quantity:
            raise forms.ValidationError('This field is required')

        
        if quantity <= 0:
            raise forms.ValidationError(
                 ' Quantity should be greater than 0')

        return quantity


# Create a search form
class InventorySearchForm(forms.ModelForm):
    # export_to_CSV = forms.BooleanField(required=False)

    class Meta:
        model = Inventory
        #search fields 
        fields = ['Medicine_name']