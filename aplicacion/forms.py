from django import forms

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    edad = forms.IntegerField()
    email = forms.EmailField()
    celular = forms.CharField(max_length=15)
    telefono = forms.CharField(max_length=15)
    egreso = forms.IntegerField()
    fecha_contratacion = forms.DateField()