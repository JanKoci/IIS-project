from django.contrib import admin
from appointments.models import Appointment, PerformanceAppointment

# Register your models here.
admin.site.register(Appointment)
admin.site.register(PerformanceAppointment)
