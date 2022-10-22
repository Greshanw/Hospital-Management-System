from django.db import models
from datetime import date,time



class Appoinment(models.Model):
    Doctor_Name = models.CharField(max_length=120, blank=False, null=False)
    Patient_Name = models.CharField(max_length=120, blank=False, null=False)
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)

    def __str__(self):
            return self.Doctor_Name