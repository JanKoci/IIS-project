import django_filters
from django.db import models
from django import forms
from visits.models import Visit


class VisitFilter(django_filters.FilterSet):
    patient_id__first_name = django_filters.CharFilter(lookup_expr='iexact')
    patient_id__last_name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Visit
        fields = {'visit_date' : ['gt', 'lt', 'exact'],
                  'patient_id' : ['exact'],
                  'patient_id__first_name' : [],
                  'patient_id__last_name' : []}

        
