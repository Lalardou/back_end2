from django import forms
from .models import AgregarProducto, Contactos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# FORMULARIO DE CONTACTO #
class ContactosForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=15) #VALIDACION 1
    class Meta:
        model = Contactos
        fields = '__all__'

# FORMULARIO DE REGISTRO #
class CustomUserCreation(UserCreationForm):
    email = forms.CharField(required=True) #VALIDACION 1
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']


# class AgregarProductoForm (forms.ModelForm):

#     class meta:
#         model = AgregarProducto
#         fields = '__all__'
#         Widgets = {
#                 "fecha_pelicula": forms.SelectDateWidget()
#         }