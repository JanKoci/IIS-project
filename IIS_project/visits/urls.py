from django.urls import path
from . import views

app_name = 'visits'

urlpatterns = [
    path('', views.VisitListView.as_view(), name='visit_list'),
    path('<int:pk>/', views.VisitDetailView.as_view(), name='visit_detail'),
    path('create/', views.VisitCreateView.as_view(), name='visit_create'),
    path('update/<int:pk>/', views.VisitUpdateView.as_view(), name='visit_update'),
    path('delete/<int:pk>/', views.VisitDeleteView.as_view(), name='visit_delete'),
    path('medicament/create/<int:visit>', views.MedicamentCreateView.as_view(), name='medicament_create'),
    path('medicament/<int:pk>/', views.MedicamentDetailView.as_view(), name='medicament_detail'),
    path('medicament/delete/<int:pk>', views.MedicamentDeleteView.as_view(), name='medicament_delete'),

    path('operation/create/<int:visit>/', views.OperationCreateView.as_view(), name='operation_create'),

]
