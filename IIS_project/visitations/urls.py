from django.urls import path
from . import views

app_name = 'visitations'

urlpatterns = [
    path('<int:patient>/', views.VisitationsView, name='visitation_list'),
    path('create/<int:patient>/', views.VisitationCreateView.as_view(), name='visitation_create'),
    path('detail/<int:pk>/', views.VisitationDetailView.as_view(), name='visitation_detail'),
    path('update/<int:pk>/', views.VisitationUpdateView.as_view(), name='visitation_update'),
    path('delete/<int:pk>/', views.VisitationDeleteView.as_view(), name='visitation_delete'),
]
