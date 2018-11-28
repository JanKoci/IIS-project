from django.db import models
from django.urls import reverse
from visits.models import PerformanceBase


# Create your models here.
class Appointment(models.Model):
    creation_date = models.DateField(auto_now_add=True)
    appointment_date = models.DateField(verbose_name='date')
    appointment_time = models.TimeField(verbose_name='time')
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("appointments:appointment_detail", kwargs={"pk": self.pk})


class PerformanceAppointment(PerformanceBase):
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("appointments:appointment_detail", kwargs={"pk": self.appointment_id.pk})
