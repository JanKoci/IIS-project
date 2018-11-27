from django.shortcuts import render
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from visits import models
from visits.filters import VisitFilter
from visits.forms import VisitCreateForm

# Create your views here.

class VisitListView(FilterView):
    # model = models.Visit
    filterset_class = VisitFilter
    template_name = 'visits/visit_list.html'
    # filterset_fields = ['visit_date', 'patient']


class VisitDetailView(DetailView):
    model = models.Visit
    context_object_name = 'visit'
    template_name = 'visits/visit.html'


class VisitCreateView(CreateView):
    model = models.Visit
    template_name = 'visits/visit_form.html'
    fields = ['visit_date', 'visit_time', 'patient_id']
    # form_class = VisitCreateForm


class VisitUpdateView(UpdateView):
    model = models.Visit
    template_name = 'visits/visit_form.html'
    fields = ['visit_date', 'visit_time', 'patient_id']


class VisitDeleteView(DeleteView):
    model = models.Visit
    template_name = 'visits/visit_confirm_delete.html'
    success_url = reverse_lazy('visits:visit_list')


class MedicamentCreateView(CreateView):
    model = models.Medicament
    template_name = 'visits/medicament_form.html'
    fields = ['name', 'substance', 'visit_id']

    def get_initial(self):
        initial = super().get_initial()
        initial['visit_id'] = models.Visit.objects.get(pk=self.kwargs['visit'])
        return initial


class MedicamentDetailView(DetailView):
    model = models.Medicament
    template_name = 'visits/medicament.html'


class MedicamentUpdateView(UpdateView):
    model = models.Medicament
    template_name = 'visits/medicament_form.html'
    fields = ['name', 'substance']


class MedicamentDeleteView(DeleteView):
    model = models.Medicament
    template_name = 'visits/medicament_confirm_delete.html'

    def get_success_url(self):
        medicament = models.Medicament.objects.get(pk=self.kwargs['pk'])
        visit = medicament.visit_id
        return reverse_lazy("visits:visit_detail", kwargs={'pk':visit.pk})


class ExaminationCreateView(CreateView):
    model = models.Examination
    template_name = 'visits/examination_form.html'
    fields = ['name', 'date', 'time', 'workplace_city', 'workplace_street',
            'workplace_postcode', 'workplace_name', 'visit_id']

    def get_initial(self):
        initial = super().get_initial()
        initial['visit_id'] = models.Visit.objects.get(pk=self.kwargs['visit'])
        return initial


class ExaminationDetailView(DetailView):
    model = models.Examination
    template_name = 'visits/examination.html'


class ExaminationUpdateView(UpdateView):
    model = models.Examination
    template_name = 'visits/examination_form.html'
    fields = ['name', 'date', 'time', 'workplace_city', 'workplace_street',
            'workplace_postcode', 'workplace_name']


class ExaminationDeleteView(DeleteView):
    model = models.Examination
    template_name = 'visits/examination_confirm_delete.html'

    def get_success_url(self):
        examination = models.Examination.objects.get(pk=self.kwargs['pk'])
        visit = examination.visit_id
        return reverse_lazy("visits:visit_detail", kwargs={'pk':visit.pk})


class PerformanceCreateView(CreateView):
    model = models.Performance
    template_name = 'visits/performance_form.html'
    fields = ['name', 'visit_id']

    # def form_valid(self, form):
    #     visit_id = models.Visit.objects.get(pk=self.kwargs['visit'])
    #     return super(PerformanceCreateView, self).form_valid(form)

    def get_initial(self):
        initial = super().get_initial()

        # if self.kwargs['visit_id']
        if ('visit' in self.kwargs):
            initial['visit_id'] = models.Visit.objects.get(pk=self.kwargs['visit'])
        return initial


class PerformanceDetailView(DetailView):
    model = models.Performance
    template_name = 'visits/performance.html'


class PerformanceUpdateView(UpdateView):
    model = models.Performance
    template_name = 'visits/performance_form.html'
    fields = ['name']


class PerformanceDeleteView(DeleteView):
    model = models.Performance
    template_name = 'visits/performance_confirm_delete.html'

    def get_success_url(self):
        performance = models.Performance.objects.get(pk=self.kwargs['pk'])
        visit = performance.visit_id
        return reverse_lazy("visits:visit_detail", kwargs={'pk':visit.pk})
