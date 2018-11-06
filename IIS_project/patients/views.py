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
            'address_street', 'address_psc', 'address_country', 'phone_number', 'insurance']


class NotRegisteredPatientCreateView(CreateView):
    model = models.NotRegisteredPatient
    template_name = 'patients/patient_form.html'
    fields = ['first_name', 'last_name', 'person_id', 'birth_date', 'address_city',
            'address_street', 'address_psc', 'address_country', 'phone_number',
            'insurance', 'doctor_first_name', 'doctor_last_name', 'doctor_phone',
            'doctor_address_city', 'doctor_address_street', 'doctor_address_psc',
            'doctor_address_country']

class RegisteredPatientCreateView(CreateView):
    model = models.RegisteredPatient
    template_name = 'patients/patient_form.html'
    fields = ['first_name', 'last_name', 'person_id', 'birth_date', 'address_city',
            'address_street', 'address_psc', 'address_country', 'phone_number',
            'insurance', 'registration_date']
