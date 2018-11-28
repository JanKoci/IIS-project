import django_filters 
from django.db import models
from invoices.models import Invoice

class InvoiceFilter(django_filters.FilterSet):
    patient_id__first_name = django_filters.CharFilter(lookup_expr='iexact')
    patient_id__last_name = django_filters.CharFilter(lookup_expr='iexact')
    patient_id__insurance = django_filters.CharFilter(lookup_expr='iexact', label='Patient insurance company')

    class Meta:
        model = Invoice
        fields = {
            'patient_id' : ['exact'],
            'patient_id__first_name' : [],
            'patient_id__last_name' : [],
            'amount' : ['gt', 'lt'],
            'creation_date' : ['gt', 'lt', 'exact'],
            'patient_id__insurance' : ['exact'],
        }