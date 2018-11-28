from django.urls import path
from . import views

app_name = 'invoices'

urlpatterns = [
    path('', views.InvoiceListView.as_view(), name='invoice_list'),
    path('create/', views.InvoiceCreateView.as_view(), name='invoice_create'),
    path('update/<int:pk>/', views.InvoiceUpdateView.as_view(), name='invoice_update'),
    path('<int:pk>/', views.InvoiceDetailView.as_view(), name='invoice_detail'),
    path('delete/<int:pk>/', views.InvoiceDeleteView.as_view(), name='invoice_delete'),
]
