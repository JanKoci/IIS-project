from django.shortcuts import render
from django.views.generic import TemplateView
# from django.http import HttpResponse

# Create your views here.
class Patient(TemplateView):
    template_name = 'patients/patient_list.html'
