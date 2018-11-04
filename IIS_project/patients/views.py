from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django_filters.views import FilterView
from patients import models

# from django.http import HttpResponse

# Create your views here.

class PatientList(FilterView):
    model = models.Patient
    template_name = 'patients/patient_list.html'

class PatientDetailView(DetailView):
    context_object_name = 'patient'
    template_name = 'patients/patient.html'
    model = models.Patient
