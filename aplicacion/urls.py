from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.welcome, name='home'),
    path('users/', views.home, name="users"), #endpoint
    path('clients/', views.view_client, name="clients"),
    path('formulario_profesor/', views.crear_profesor, name='formulario_profesor'),
    # path('register_user', views.register_user, name="register_user"),
    path('register_user/', views.register_user, name='register_user'),
    path('formulario/', views.formulario, name='formulario'),
    path('mostrar_escuela/', views.mostrar_escuela, name='mostrar_escuela'),
]
