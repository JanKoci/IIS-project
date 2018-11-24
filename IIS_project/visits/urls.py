from django.urls import path
from . import views

app_name = 'visits'

urlpatterns = [
    path('', views.VisitListView.as_view(), name='visit_list'),
    path('<int:pk>/', views.VisitDetailView.as_view(), name='visit_detail'),
    path('create/', views.VisitCreateView.as_view(), name='visit_create'),

]
