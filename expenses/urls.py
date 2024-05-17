from django.urls import path
from .import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('expense/<int:pk>/', views.expense_detail, name='expense_detail'),
    path('expense/new/', views.expense_new, name='expense_new'),
    path('expense/<int:pk>/edit/', views.expense_edit, name='expense_edit'),
]