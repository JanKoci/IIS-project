from django.shortcuts import render
from django.views.generic.list import ListView
from vaccinations import models

# Create your views here.

class VaccinationListView(ListView):
    model = models.Vaccination
    template_name = 'vaccinations/vaccination_list.html'
    
