from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from vaccinations import models
from patients.models import Patient
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
# Create your views here.



def VaccinationView(request, patient):
    object_list = models.Vaccination.objects.all().filter(patient=patient)
    context_dict = {'object_list' : object_list, 'patient' : patient}
    return render(request, 'vaccinations/vaccination_list.html', context=context_dict)


# class VaccinationListView(ListView):
#     model = models.Vaccination
#     template_name = 'vaccinations/vaccination_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         patient = self.kwargs['patient']
#         context.update({
#             'object_list' : models.Vaccination.objects.all().filter(patient=patient),
#             'patient' : patient,
#         })
#         return context


class VaccinationCreateView(CreateView):
    model = models.Vaccination
    template_name = 'vaccinations/vaccination_form.html'
    fields = ['vaccine_name', 'appointment_date', 'appointment_time',
                'expiry_date', 'patient']

    def get_initial(self):
        initial = super().get_initial()
        initial['patient'] = Patient.objects.get(pk=self.kwargs['patient'])
        return initial


class VaccinationDetailView(DetailView):
    model = models.Vaccination
    template_name = 'vaccinations/vaccination.html'


class VaccinationUpdateView(UpdateView):
    model = models.Vaccination
    template_name = 'vaccinations/vaccination_form.html'
    fields = ['vaccine_name', 'appointment_date', 'appointment_time',
                'expiry_date', 'patient']


class VaccinationDeleteView(DeleteView):
    model = models.Vaccination
    template_name = 'vaccinations/vaccination_confirm_delete.html'

    def get_success_url(self):
        vaccination = models.Vaccination.objects.get(pk=self.kwargs['pk'])
        return reverse_lazy("vaccinations:vaccination_list", kwargs={'patient':vaccination.patient.pk})
