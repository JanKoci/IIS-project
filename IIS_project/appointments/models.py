from django.db import models
from django.urls import reverse


# Create your models here.
class Appointment(models.Model):
    creation_date = models.DateField(auto_now_add=True)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("appointments:appointment_detail", kwargs={"pk": self.pk})
    
