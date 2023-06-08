from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.welcome, name='home'),
    path('users/', views.home, name="users"), #endpoint
    path('clients/', views.view_client, name="clients"),
]
