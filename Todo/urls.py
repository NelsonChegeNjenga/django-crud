from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('view/', view, name='view'),
    path('add/', add, name='add'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
]
