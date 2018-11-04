from django.shortcuts import render
from django.views.generic import TemplateView
from django_filters.views import FilterView
from patients import models

# from django.http import HttpResponse

# Create your views here.

class PatientList(FilterView):
    model = models.Patient
    template_name = 'patients/patient_list.html'
