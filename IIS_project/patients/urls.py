from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('', views.PatientList.as_view(), name='patient_list'),
]
