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
    fields = ['visit_date', 'visit_time']

class VisitDeleteView(DeleteView):
    model = models.Visit
    template_name = 'visits/visit_confirm_delete.html'
    success_url = reverse_lazy('visits:visit_list')


class OperationCreateView(CreateView):
    model = models.Operation
    template_name = 'visits/operation_form.html'
    fields = ['name', 'visit_id']

    # def form_valid(self, form):
    #     visit_id = models.Visit.objects.get(pk=self.kwargs['visit'])
    #     return super(OperationCreateView, self).form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        if ('visit' in self.kwargs):
            initial['visit_id'] = models.Visit.objects.get(pk=self.kwargs['visit'])
        return initial
