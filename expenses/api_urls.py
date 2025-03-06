from django.urls import path
from . import views

urlpatterns = [
    path('first/', views.first_api, name='first_api'),
]
