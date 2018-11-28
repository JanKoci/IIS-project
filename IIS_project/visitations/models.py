from django.db import models
from appointments.models import Appointment
from django.urls import reverse

# Create your models here.
class Visitation(Appointment):
    note = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("visitations:visitation_detail", kwargs={"pk": self.pk})
