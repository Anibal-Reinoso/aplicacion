from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def welcome(request):
    return render(request, "home.html")

def home(request):
    users = User.objects.all()

    nuevos = ["Gonzalo", "Adrian"]

    context = {
        "usuarios": users,
        "otros": nuevos,
    }

    return render(request, "users.html", context=context)

def view_client(request):

    context = {"nombre": "Javier",
               "edad": 30,
               "oficio": "empleado administrativo"}
    
    return render(request, 'clients.html', context=context)