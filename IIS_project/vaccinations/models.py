from django.db import models
from patients.models import RegisteredPatient

# Create your models here.

class Vaccination(models.Model):
    id = models.AutoField(primary_key=True)
    vaccine_name = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    creation_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()
    patient_id = models.ForeignKey(RegisteredPatient, on_delete=models.CASCADE)
