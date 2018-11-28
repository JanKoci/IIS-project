from django.db import models
from patients.models import RegisteredPatient
from appointments.models import Appointment
from django.urls import reverse

# Create your models here.

class Vaccination(Appointment):
    vaccine_name = models.CharField(max_length=50)
    expiry_date = models.DateField()

    def get_absolute_url(self):
        return reverse("vaccinations:vaccination_detail", kwargs={"pk": self.pk})
