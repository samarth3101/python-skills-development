from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('menu/<int:item_id>/', views.menu_item_detail, name='menu_item_detail'),
    path("about/", views.about, name="about"), 
    path("book/", views.book, name="book"), 
]