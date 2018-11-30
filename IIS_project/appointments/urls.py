from django.urls import path
from . import views
from patients import views as patient_views

app_name = 'appointments'

urlpatterns = [
    path('', views.AppointmentList.as_view(), name='appointments_list'),
    path('create/', views.AppointmentCreateView.as_view(), name='appointments_create'),
    path('<int:pk>/', views.AppointmentDetailView.as_view(), name='appointment_detail'),
    path('update/<int:pk>/', views.AppointmentUpdateView.as_view(), name='appointment_update'),
    path('delete/<int:pk>/', views.AppointmentDeleteView.as_view(), name='appointment_delete'),

    path('performance/create/<int:appointment>/',views.PerformanceAppointmentCreateView.as_view(), name='performance_create'),
    path('performance/<int:pk>/',views.PerformanceAppointmentDetailView.as_view(), name='performance_detail'),
    path('performance/update/<int:pk>', views.PerformanceAppointmentUpdateView.as_view(), name='performance_update'),
    path('performance/delete/<int:pk>', views.PerformanceAppointmentDeleteView.as_view(), name='performance_delete'),

    path('transform/<int:pk>/', views.TransformationView, name='transformation'),
    path('transformconfirm/<int:pk>/', views.ConfirmTrasformationView, name='transformation_confirm'),
]
