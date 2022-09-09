from django.db import models
from datetime import date,time



class Appoinment(models.Model):
    Doctor_Name = models.CharField(max_length=120, unique=True)
    Patient_Name = models.CharField(max_length=120, unique=True)
    Date = models.DateField()
    Time = models.TimeField()

    def __str__(self):
            return self.Doctor_Name