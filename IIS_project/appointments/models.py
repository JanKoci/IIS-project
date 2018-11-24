from django.db import models
from django.urls import reverse


# Create your models here.
class Appointment(models.Model):
    creation_date = models.DateField()
    appointment_date = models.DateTimeField()
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("appointments:appointment_detail", kwargs={"pk": self.pk})
    
