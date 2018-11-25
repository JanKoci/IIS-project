from django.forms import ModelForm
from appointments import models

class AppointmentForm(ModelForm):
    class Meta:
        model = models.Appointment
        fields = ['patient', 'appointment_date', 'creation_date']