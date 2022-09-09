from django import forms

from appoinment.models import Appoinment


class AppoinmentForm(forms.Form):
    Doctor_Name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'Doctor_Name',
        'data-val': 'true',
        'data-val-required': 'Please Enter Doctor Name',
    }))
    Patient_Name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'Patient_Name',
        'data-val': 'true',
        'data-val-required': 'Please Enter Patient Name',
    }))
    Date = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
