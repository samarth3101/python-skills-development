from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'restaurant/home.html', {'restaurant_name': 'Little Lemon'})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f"Thank you, {name}! Your message has been received.")
    
    return HttpResponse('''
        <form method="post">
            <label>Name:</label>
            <input type="text" name="name"><br>
            <label>Message:</label>
            <textarea name="message"></textarea><br>
            <input type="submit" value="Send">
        </form>
    ''')

def menu(request):
    return HttpResponse("<h1>Welcome to the Menu Page</h1>")