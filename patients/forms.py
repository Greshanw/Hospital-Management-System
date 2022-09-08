from django import forms

from patients.models import Patient


class PatientForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'phone',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    }))
    dob = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
