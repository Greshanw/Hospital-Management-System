from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=120, unique=True)
    phone = models.CharField(max_length=120)
    dob = models.DateField()
    NIC = models.CharField(max_length=12)
    email = models.CharField(max_length=120)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name