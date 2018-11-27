from django.urls import path
from . import views

app_name = 'visits'

urlpatterns = [
    path('', views.VisitListView.as_view(), name='visit_list'),
    path('<int:pk>/', views.VisitDetailView.as_view(), name='visit_detail'),
    path('create/', views.VisitCreateView.as_view(), name='visit_create'),
    path('update/<int:pk>/', views.VisitUpdateView.as_view(), name='visit_update'),
    path('delete/<int:pk>/', views.VisitDeleteView.as_view(), name='visit_delete'),

    path('medicament/create/<int:visit>/', views.MedicamentCreateView.as_view(), name='medicament_create'),
    path('medicament/<int:pk>/', views.MedicamentDetailView.as_view(), name='medicament_detail'),
    path('medicament/update/<int:pk>/', views.MedicamentUpdateView.as_view(), name='medicament_update'),
    path('medicament/delete/<int:pk>/', views.MedicamentDeleteView.as_view(), name='medicament_delete'),

    path('examination/create/<int:visit>/', views.ExaminationCreateView.as_view(), name='examination_create'),
    path('examination/<int:pk>/', views.ExaminationDetailView.as_view(), name='examination_detail'),
    path('examination/update/<int:pk>/', views.ExaminationUpdateView.as_view(), name='examination_update'),
    path('examination/delete/<int:pk>/', views.ExaminationDeleteView.as_view(), name='examination_delete'),

    path('performance/create/<int:visit>/', views.PerformanceCreateView.as_view(), name='performance_create'),
    path('performance/<int:pk>/', views.PerformanceDetailView.as_view(), name='performance_detail'),
    path('performance/update/<int:pk>/', views.PerformanceUpdateView.as_view(), name='performance_update'),
    path('performance/delete/<int:pk>/', views.PerformanceDeleteView.as_view(), name='performance_delete'),

]
