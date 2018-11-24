from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django_filters.views import FilterView
from appointments import models
from .filters import AppointmentFilter
from appointments.forms import AppointmentForm

# Create your views here.

class AppointmentList(FilterView):
    model = models.Appointment
    template_name = 'appointments/appointments_list.html'


class AppointmentCreateView(CreateView):
    model = models.Appointment
    template_name = 'appointments/appointments_form.html'
    fields = ['creation_date', 'appointment_date', 'patient']


class AppointmentDetailView(DetailView):
    context_object_name = 'appointment'
    model = models.Appointment
    template_name = 'appointments/appointments_detail.html'


class AppointmentUpdateView(UpdateView):
    model = models.Appointment
    template_name = 'appointments/appointments_form.html'
    form_class = AppointmentForm
