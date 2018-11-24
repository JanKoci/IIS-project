from django.db import models
from patients.models import Patient

# Create your models here.

class Visit(models.Model):
    id = models.AutoField(primary_key=True)
    visit_date = models.DateField()
    visit_time = models.TimeField()
    # creation_date = models.DateField(auto_now_add=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Operation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    visit_id = models.ForeignKey(Visit, on_delete=models.CASCADE)


class Medicament(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    substance = models.CharField(max_length=50)
    visit_id = models.ForeignKey(Visit, on_delete=models.CASCADE)


# ExternalExamination ???
class Examination(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    workplace_city = models.CharField(max_length=50)
    workplace_street = models.CharField(max_length=50)
    workplace_postcode = models.CharField(max_length=5)
    workplace_name = models.CharField(max_length=50)
    visit_id = models.ForeignKey(Visit, on_delete=models.CASCADE)
