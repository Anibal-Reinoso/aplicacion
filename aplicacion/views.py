from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProfesorForm
from .models import Profesor, Escuela
from django.contrib import messages

from .forms import UserRegistrationForm, EscuelaForm, LoginForm
# Create your views here.

def welcome(request):
    return render(request, "aplicacion/home.html")

@login_required
def home(request):
    users = User.objects.all()

    nuevos = ["Gonzalo", "Adrian"]

    context = {
        "usuarios": users,
        "otros": nuevos,
    }

    return render(request, "aplicacion/users.html", context=context)

@login_required
def view_client(request):

    context = {"nombre": "Javier",
               "edad": 30,
               "oficio": "empleado administrativo"}
    
    return render(request, 'aplicacion/clients.html', context=context)

@login_required
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

    return render(request, 'aplicacion/profesor_formulario.html', context=context)

# def register_user(request):
#     user = User.objects.create(
#         username="RodrigoF",
#         password="1234rodrigo",
#         is_staff=True
#     )
#     user.save()
#     return redirect('/home')

@login_required
def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            permissions = form.cleaned_data['permissions']
            username = form.cleaned_data['username']
            user.groups.add(group)
            user.user_permissions.set(permissions)
            messages.success(request, f'Usuario {username} creado exitosamente!!')
            return redirect('/home')
    else:
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request, 'aplicacion/register_user.html', context)


@login_required
def formulario(request):
    form = EscuelaForm()

    if request.method == "POST":
        form = EscuelaForm(request.POST)
        if form.is_valid():
            print(form)
            escuela = Escuela()
            escuela.nombre = form.cleaned_data['nombre']
            escuela.direccion = form.cleaned_data['direccion']
            escuela.email = form.cleaned_data['email']
            escuela.save()
        else:
            print("Datos invalidos")
        return redirect('/mostrar_escuela')
    context = {'form': form}

    return render(request, 'aplicacion/formulario.html', context=context)

@login_required
def mostrar_escuela(request):

    datos = Escuela.objects.all()

    context = {'escuelas': datos}

    return render(request, 'aplicacion/mostrar_escuela.html', context=context)

# def login(request):
#     if request.method=="POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             usuario = form.cleaned_data["nombre"]
#             clave = form.cleaned_data["password"]
#             user = authenticate(request, username=usuario, password=clave)
#             if user is not None:
#                 if user.is_active:
#                     auth_login(request, user)
#                     return redirect('/home')
#                 else:
#                     return HttpResponse('Cuenta deshabilitada')
#             else:
#                 return HttpResponse('Login no valido')
#     else:
#         form = LoginForm()
#     return render(request, 'aplicacion/login.html', {'form':form})


# def logout(request):
#     auth_logout(request)
#     return redirect('/login')