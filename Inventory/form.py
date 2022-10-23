from django import forms
from .models import Inventory

# Create a form
class InventoryCreateForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['Product_ID','Medicine_name', 'quantity', 'Net_price',  'receive_quantity', 'Vendor',
                  'reorder_level']

    error = 'This field is required'
    #validation the input fields
    def clean_Product_ID(self):
        product_id = self.cleaned_data.get('Product_ID')
        if not product_id:  # if it is blank
            raise forms.ValidationError(self.error)

        for instance in Inventory.objects.all():
            if instance.Product_ID == product_id:
                raise forms.ValidationError(
                    product_id + ' is already created')
            
        
        return product_id

    def clean_Medicine_name(self):
        medicine_name = self.cleaned_data.get('Medicine_name')
        if not medicine_name:
            raise forms.ValidationError(self.error)

        for instance in Inventory.objects.all():
            if instance.Medicine_name == medicine_name:
                raise forms.ValidationError(
                    medicine_name + ' is already created')

        return medicine_name

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if not quantity:
            raise forms.ValidationError(self.error)

        
        if quantity <= 0:
            raise forms.ValidationError(
                 ' Quantity should be greater than 0')

        return quantity
    
    def clean_Net_price(self):
        Net_price = self.cleaned_data.get('Net_price')
        if not Net_price:
            raise forms.ValidationError(self.error)

        
        if Net_price <= 0:
            raise forms.ValidationError(
                 ' Net_price should be greater than 0')

        return Net_price
    
    def clean_receive_quantity(self):
        receive_quantity = self.cleaned_data.get('receive_quantity')
        if not receive_quantity:
            raise forms.ValidationError(self.error)

        if receive_quantity <= 0:
            raise forms.ValidationError(
                 ' receive_quantity should be greater than 0')
        
        return receive_quantity
    
    def clean_reorder_level(self):
        reorder_level = self.cleaned_data.get('reorder_level')
        if not reorder_level:
            raise forms.ValidationError(self.error)

        
        if reorder_level <= 0:
            raise forms.ValidationError(
                 ' Reorder Level should be greater than 0')

        return reorder_level

    def clean_Vendor(self):
        vendor = self.cleaned_data.get('Vendor')
        if not vendor:
            raise forms.ValidationError(self.error)

        return vendor


# Create a search form
class InventorySearchForm(forms.ModelForm):
    

    class Meta:
        model = Inventory
        #search fields 
        fields = ['Medicine_name']
    

#form for the Updating Product details of the Inventory
class InventoryUpdateForm(forms.ModelForm):
 class Meta:
        model = Inventory
        fields = ['Product_ID','Medicine_name', 'quantity', 'Net_price',  'receive_quantity', 'Vendor',
                  'reorder_level']