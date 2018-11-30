from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django_filters.views import FilterView
from django.urls import reverse_lazy
from patients import models
from patients.forms import NotRegPatientForm, RegPatientForm


# from django.http import HttpResponse

# Create your views here.

class PatientListView(FilterView):
    model = models.Patient
    template_name = 'patients/patient_list.html'
    filterset_fields = ['person_id', 'first_name', 'last_name', 'birth_date',]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'object_list': models.Patient.objects.all().order_by("last_name")
        })
        return context
 

class PatientDetailView(DetailView):
    context_object_name = 'patient'
    template_name = 'patients/patient.html'
    model = models.Patient

class RegPatientUpdateView(UpdateView):
    model = models.RegisteredPatient
    template_name = 'patients/patient_form.html'
    form_class = RegPatientForm


class NotRegPatientUpdateView(UpdateView):
    model = models.NotRegisteredPatient
    template_name = 'patients/patient_form.html'
    form_class = NotRegPatientForm



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
            'insurance']

class PatientDeleteView(DeleteView):
    model = models.Patient
    template_name = 'patients/patient_confirm_delete.html'
    success_url = reverse_lazy('patients:patient_list')
