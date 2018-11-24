from django.db import models

# Create your models here.


class Appointment(models.Model):
    creation_date = models.DateField()
    appointment_date = models.DateTimeField()
    person_id = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)

