from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from vaccinations import models
from patients.models import Patient
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def VaccinationView(request, patient):
    object_list = models.Vaccination.objects.all().filter(patient=patient)
    context_dict = {'object_list' : object_list, 'patient' : patient}
    return render(request, 'vaccinations/vaccination_list.html', context=context_dict)


class VaccinationCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = models.Vaccination
    template_name = 'vaccinations/vaccination_form.html'
    fields = ['vaccine_name', 'appointment_date', 'appointment_time',
                'expiry_date', 'patient']

    def get_initial(self):
        initial = super().get_initial()
        initial['patient'] = Patient.objects.get(pk=self.kwargs['patient'])
        return initial


class VaccinationDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = models.Vaccination
    template_name = 'vaccinations/vaccination.html'


class VaccinationUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = models.Vaccination
    template_name = 'vaccinations/vaccination_form.html'
    fields = ['vaccine_name', 'appointment_date', 'appointment_time',
                'expiry_date', 'patient']


class VaccinationDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = models.Vaccination
    template_name = 'vaccinations/vaccination_confirm_delete.html'

    def get_success_url(self):
        vaccination = models.Vaccination.objects.get(pk=self.kwargs['pk'])
        return reverse_lazy("vaccinations:vaccination_list", kwargs={'patient':vaccination.patient.pk})
