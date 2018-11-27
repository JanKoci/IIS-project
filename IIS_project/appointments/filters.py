import django_filters
from .models import Appointment
from django.db import models
from django import forms

class AppointmentFilter(django_filters.FilterSet):
    patient__first_name = django_filters.CharFilter(lookup_expr='iexact')
    patient__last_name = django_filters.CharFilter(lookup_expr='iexact')
    patient__person_id = django_filters.CharFilter(lookup_expr='exact', label='Personal ID')
    appointment_date = django_filters.DateFilter(label='Date')
    class Meta:
        model = Appointment
        fields = {
        #    'appointment_date' : ['exact', 'range'],
        }

        filter_overrides = { 
            models.ForeignKey: {
                'filter_class' : django_filters.ChoiceFilter,
                'extra' : lambda f: {
                    'widget' : forms.TextInput,
                }
            }
        }

    @classmethod
    def filter_for_lookup(cls, f, lookup_type):
        if isinstance(f, models.DateField) and lookup_type == 'range':
            return django_filters.DateRangeFilter, {}

        return super().filter_for_lookup(f, lookup_type)