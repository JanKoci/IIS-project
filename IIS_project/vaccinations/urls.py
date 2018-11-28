from django.urls import path
from . import views

app_name = 'vaccinations'

urlpatterns = [
    path('<int:patient>/', views.VaccinationView, name='vaccination_list'),
    # path('<int:patient>/', views.VaccinationListView.as_view(), name='vaccination_list'),
    path('create/<int:patient>/', views.VaccinationCreateView.as_view(), name='vaccination_create'),
    path('detail/<int:pk>/', views.VaccinationDetailView.as_view(), name='vaccination_detail'),
    path('update/<int:pk>/', views.VaccinationUpdateView.as_view(), name='vaccination_update'),
    path('delete/<int:pk>/', views.VaccinationDeleteView.as_view(), name='vaccination_delete'),
]
