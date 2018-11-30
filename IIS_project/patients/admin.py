from django.contrib import admin
from patients.models import Patient, RegisteredPatient, NotRegisteredPatient

# Register your models here.
admin.site.register(Patient)
admin.site.register(RegisteredPatient)
admin.site.register(NotRegisteredPatient)
