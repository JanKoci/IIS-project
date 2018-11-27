from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django_filters.views import FilterView
from django.urls import reverse_lazy
from appointments import models
from .filters import AppointmentFilter
#from appointments.forms import AppointmentForm

# Create your views here.

class AppointmentList(FilterView):
    #model = models.Appointment
    filterset_class = AppointmentFilter
    template_name = 'appointments/appointments_list.html'


class AppointmentCreateView(CreateView):
    model = models.Appointment
    template_name = 'appointments/appointments_form.html'
    fields = ['appointment_date', 'appointment_time', 'patient']


class AppointmentDetailView(DetailView):
    context_object_name = 'appointment'
    model = models.Appointment
    template_name = 'appointments/appointments_detail.html'


class AppointmentUpdateView(UpdateView):
    model = models.Appointment
    template_name = 'appointments/appointments_form.html'
    fields = ['appointment_date', 'appointment_time', 'patient']
    #form_class = AppointmentForm


class AppointmentDeleteView(DeleteView):
    model = models.Appointment
    template_name = 'appointments/appointments_delete.html'
    success_url = reverse_lazy('appointments:appointments_list')


class PerformanceAppointmentCreateView(CreateView):
    model = models.PerformanceAppointment
    template_name = 'appointments/performance_form.html'
    fields = ['name', 'appointment_id']

    def get_initial(self):
        initial = super().get_initial()

        if 'appointment' in self.kwargs:
            initial['appointment_id'] = models.Appointment.objects.get(pk=self.kwargs['appointment'])
        return initial


class PerformanceAppointmentDetailView(DetailView):
    model = models.PerformanceAppointment
    template_name = 'appointments/performance_detail.html'


class PerformanceAppointmentUpdateView(UpdateView):
    model = models.PerformanceAppointment
    template_name = 'appointments/performance_form.html'
    fields = ['name']


class PerformanceAppointmentDeleteView(DeleteView):
    model = models.PerformanceAppointment
    template_name = 'appointments/performance_delete.html'

    def get_success_url(self):
        performance = models.PerformanceAppointment.objects.get(pk=self.kwargs['pk'])
        appointment = performance.appointment_id
        return reverse_lazy("appointments:appointment_detail", kwargs={'pk':appointment.pk})

