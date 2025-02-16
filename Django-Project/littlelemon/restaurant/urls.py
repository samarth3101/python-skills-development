from django.urls import path
from . import views  # Import views.py

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name='menu'),  
]