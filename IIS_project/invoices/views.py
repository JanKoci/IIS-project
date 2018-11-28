from django.shortcuts import render
from django_filters.views import FilterView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from invoices import models
from invoices.filters import InvoiceFilter
from django.urls import reverse_lazy

# Create your views here.


class InvoiceListView(FilterView):
    #model = models.Invoice
    filterset_class = InvoiceFilter
    template_name = 'invoices/invoice_list.html'


class InvoiceCreateView(CreateView):
    model = models.Invoice
    fields = ['creation_date', 'amount', 'patient_id']
    template_name = 'invoices/invoice_form.html'


class InvoiceUpdateView(UpdateView):
    model = models.Invoice
    fields = ['creation_date', 'amount', 'patient_id']
    template_name = 'invoices/invoice_form.html'


class InvoiceDeleteView(DeleteView):
    model = models.Invoice
    template_name = 'invoices/invoice_delete.html'
    success_url = reverse_lazy('invoices:invoice_list')


class InvoiceDetailView(DetailView):
    model = models.Invoice
    template_name = 'invoices/invoice_detail.html'