from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('', views.PatientList.as_view(), name='patient_list'),
    path('<int:pk>/', views.PatientDetailView.as_view(), name='patient_detail'),
    path('update/<int:pk>/', views.PatientUpdateView.as_view(), name='patient_update'),
    path('create/', views.PatientCreateView.as_view(), name='patient_create'),
]
