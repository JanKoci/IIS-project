from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.AppointmentList.as_view(), name='appointments_list'),
    path('create/', views.AppointmentCreateView.as_view(), name='appointments_create')
]