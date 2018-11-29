from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django_filters.views import FilterView
from django.urls import reverse_lazy
from appointments import models
from .filters import AppointmentFilter
from django.contrib.auth.mixins import LoginRequiredMixin
#from appointments.forms import AppointmentForm

# Create your views here.

class AppointmentList(LoginRequiredMixin, FilterView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    filterset_class = AppointmentFilter
    template_name = 'appointments/appointments_list.html'


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = models.Appointment
    template_name = 'appointments/appointments_form.html'
    fields = ['appointment_date', 'appointment_time', 'patient']


class AppointmentDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    context_object_name = 'appointment'
    model = models.Appointment
    template_name = 'appointments/appointments_detail.html'


class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = models.Appointment
    template_name = 'appointments/appointments_form.html'
    fields = ['appointment_date', 'appointment_time', 'patient']


class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = models.Appointment
    template_name = 'appointments/appointments_delete.html'
    success_url = reverse_lazy('appointments:appointments_list')


class PerformanceAppointmentCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = models.PerformanceAppointment
    template_name = 'appointments/performance_form.html'
    fields = ['name', 'appointment_id']

    def get_initial(self):
        initial = super().get_initial()

        if 'appointment' in self.kwargs:
            initial['appointment_id'] = models.Appointment.objects.get(pk=self.kwargs['appointment'])
        return initial


class PerformanceAppointmentDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = models.PerformanceAppointment
    template_name = 'appointments/performance_detail.html'


class PerformanceAppointmentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = models.PerformanceAppointment
    template_name = 'appointments/performance_form.html'
    fields = ['name']


class PerformanceAppointmentDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = models.PerformanceAppointment
    template_name = 'appointments/performance_delete.html'

    def get_success_url(self):
        performance = models.PerformanceAppointment.objects.get(pk=self.kwargs['pk'])
        appointment = performance.appointment_id
        return reverse_lazy("appointments:appointment_detail", kwargs={'pk':appointment.pk})
