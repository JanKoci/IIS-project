import django_filters
from .models import Appointment
from django.db import models
from django import forms

class AppointmentFilter(django_filters.FilterSet):
    patient__first_name = django_filters.CharFilter(lookup_expr='iexact')
    patient__last_name = django_filters.CharFilter(lookup_expr='iexact')
    #appointment_date = django_filters.DateFilter(label='Date')
    
    class Meta:
        model = Appointment
        fields = {

            'appointment_date' : ['gt', 'lt', 'exact'],
            'patient' : ['exact'],
            'patient__first_name' : [],
            'patient__last_name' : [],
        }