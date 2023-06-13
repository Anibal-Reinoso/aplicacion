from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import ProfesorForm
from .models import Profesor
from django.contrib import messages

from .forms import UserRegistrationForm
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

def crear_profesor(request):
    form = ProfesorForm()

    if request.method == "POST":
        print(request)
        form = ProfesorForm(request.POST)

        if form.is_valid():
            print(form)
            profesor = Profesor()
            profesor.nombre = form.cleaned_data['nombre']
            profesor.apellido = form.cleaned_data['apellido']
            profesor.edad = form.cleaned_data['edad']
            profesor.email = form.cleaned_data['email']
            profesor.celular = form.cleaned_data['celular']
            profesor.telefono = form.cleaned_data['telefono']
            profesor.egreso = form.cleaned_data['egreso']
            profesor.fecha_contratacion = form.cleaned_data['fecha_contratacion']
            profesor.save()
        else:
            print("Datos invalidos")
        return redirect('/home')
    
    context = {
        'form': form
    }

    return render(request, 'profesor_formulario.html', context=context)

# def register_user(request):
#     user = User.objects.create(
#         username="RodrigoF",
#         password="1234rodrigo",
#         is_staff=True
#     )
#     user.save()
#     return redirect('/home')

def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado exitosamente!!')
            return redirect('/home')
    else:
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request, 'register_user.html', context)