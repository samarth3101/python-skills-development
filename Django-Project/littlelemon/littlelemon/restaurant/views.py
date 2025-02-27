from django.shortcuts import render, get_object_or_404
from .models import MenuItem

def home(request):
    return render(request, 'restaurant/home.html')

def about(request):
    return render(request, "restaurant/about.html") 

def menu(request):
    items = MenuItem.objects.all().order_by('name')  # Sorted alphabetically
    return render(request, 'restaurant/menu.html', {'items': items})

def book(request):
    return render(request, "restaurant/book.html") 

def menu_item_detail(request, item_id):
    item = get_object_or_404(MenuItem, pk=item_id)
    return render(request, 'restaurant/menu_item_detail.html', {'item': item})