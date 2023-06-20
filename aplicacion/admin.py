from django.contrib import admin
from .models import Escuela, Profesor, RegistroProfesorEscuela
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Escuela)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email')
    list_filter = ('is_staff', 'is_superuser')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class RegistroProfesorInline(admin.TabularInline):
    model = RegistroProfesorEscuela
    extra = 1

class ProfesorAdmin(admin.ModelAdmin):
    inlines = [RegistroProfesorInline,]
    list_display = ('nombre', 'apellido', 'email', 'fecha_contratacion')
    list_per_page = 5

admin.site.register(Profesor, ProfesorAdmin)