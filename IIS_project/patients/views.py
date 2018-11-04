from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, CreateView
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

class PatientUpdateView(UpdateView):
    model = models.Patient
    template_name = 'patients/patient_form.html'
    fields = ['first_name', 'last_name', 'person_id', 'birth_date', 'address_city',
            'address_street', 'address_psc', 'address_country', 'insurance']


class PatientCreateView(CreateView):
    model = models.Patient
    template_name = 'patients/patient_form.html'
    fields = ['first_name', 'last_name', 'person_id', 'birth_date', 'address_city',
            'address_street', 'address_psc', 'address_country', 'insurance']
