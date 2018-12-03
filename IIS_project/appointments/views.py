from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django_filters.views import FilterView
from django.urls import reverse_lazy
from appointments import models
from visits.models import Visit
from .filters import AppointmentFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

# Create your views here.

class AppointmentList(LoginRequiredMixin, FilterView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    filterset_class = AppointmentFilter
    template_name = 'appointments/appointments_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'object_list': models.Appointment.objects.all().order_by('appointment_date')
        })
        return context


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


def ConfirmTrasformationView(request, pk):
    context_dict = {'pk':pk}
    return render(request, 'appointments/confirm_transformation.html', context=context_dict)


def TransformationView(request, pk):
    appointment = models.Appointment.objects.get(pk=pk)
    new_visit = Visit(visit_date=appointment.appointment_date,
                        visit_time=appointment.appointment_time,
                        patient_id=appointment.patient)
    new_visit.save()
    appointment.delete()
    return redirect('visits:visit_detail', pk=new_visit.pk)
