from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('', views.Patient.as_view(), name='patient_list'),
]
