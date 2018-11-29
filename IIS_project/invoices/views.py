from django.shortcuts import render
from django_filters.views import FilterView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from invoices import models
from invoices.filters import InvoiceFilter
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.


class InvoiceListView(PermissionRequiredMixin, LoginRequiredMixin, FilterView):
    permission_required = 'invoices.can_view'
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    filterset_class = InvoiceFilter
    template_name = 'invoices/invoice_list.html'


class InvoiceCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = models.Invoice
    fields = ['creation_date', 'amount', 'patient_id']
    template_name = 'invoices/invoice_form.html'


class InvoiceUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = models.Invoice
    fields = ['creation_date', 'amount', 'patient_id']
    template_name = 'invoices/invoice_form.html'


class InvoiceDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = models.Invoice
    template_name = 'invoices/invoice_delete.html'
    success_url = reverse_lazy('invoices:invoice_list')


class InvoiceDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = models.Invoice
    template_name = 'invoices/invoice_detail.html'
