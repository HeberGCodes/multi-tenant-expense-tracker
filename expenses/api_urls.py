from django.urls import path
from .views import (
    ExpenseListCreateView, 
    ExpenseDetailView,
    CompanyListCreateView,
    CompanyDetailView,
)

urlpatterns = [
    path('expenses/', ExpenseListCreateView.as_view(), name='expenses-list-create'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    path('companies/', CompanyListCreateView.as_view(), name='companies-list-create'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
]
