from django.shortcuts import render
from django_filters.views import FilterView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView, View
from invoices import models
from patients.models import Patient
from invoices.filters import InvoiceFilter
from django.urls import reverse_lazy
from invoices.utils import render_to_pdf
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


class InvoiceListView(FilterView):
    #model = models.Invoice
    filterset_class = InvoiceFilter
    template_name = 'invoices/invoice_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'object_list': models.Invoice.objects.all().order_by("patient_id__last_name")
        })
        return context


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


class InvoicePDFView(View):
    def get(self, request, *args, **kwargs):
        invoice = models.Invoice.objects.get(pk=self.kwargs['pk'])
        context = {
            'first_name': invoice.patient_id.first_name,
            'last_name': invoice.patient_id.last_name,
            'personal_id': invoice.patient_id.person_id,
            'insurance': invoice.patient_id.insurance,
            'amount': invoice.amount,
            'creation_date': invoice.creation_date
        }
        pdf = render_to_pdf('invoices/invoice_pdf_detail.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = 'Invoice_%s.pdf' %(invoice.patient_id.person_id)
            content = "inline; filename='%s'" %(filename)
            return
        