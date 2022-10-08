from django.db import models
from datetime import date

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, unique=True)
    phone = models.CharField(max_length=120)
    dob = models.DateField()
    NIC = models.CharField(max_length=12)
    email = models.CharField(max_length=120)
    address = models.CharField(max_length=220)
    qr = models.CharField(max_length=200)
    created_date = models.DateField(auto_now_add=True)

    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    age = property(age)

    def __str__(self):
        return self.name