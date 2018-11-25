from django.urls import path
from . import views
from patients import views as patient_views

app_name = 'appointments'

urlpatterns = [
    path('', views.AppointmentList.as_view(), name='appointments_list'),
    path('create/', views.AppointmentCreateView.as_view(), name='appointments_create'),
    path('<int:pk>/', views.AppointmentDetailView.as_view(), name='appointment_detail'),
    path('update/<int:pk>/', views.AppointmentUpdateView.as_view(), name='appointment_update'),
    path('delete/<int:pk>/', views.AppointmentDeleteView.as_view(), name='appointment_delete')
]