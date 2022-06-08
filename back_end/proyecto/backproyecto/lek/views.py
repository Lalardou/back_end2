from django.shortcuts import render
from .models import AgregarProducto
from .forms import  CustomUserCreation, ContactosForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def menu (request):
    return render (request, 'lek/menu.html')

def contactos(request):
    data = {
        'form':ContactosForm()
    }
    
    if request.method == 'POST':
        formulario = ContactosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mensaje Enviado!")
        else:
            data["form"] = formulario
    return render(request, 'lek/contactos.html', data)
    
def componentes (request):
    contexto = {"nombreC" :"Audifonos","nombreC1":"Hyperx Kraken" , "nombreC2":"Logitech G733", "nombreC3": "Hyperx Cloud Alpha","nombreC4" :"Hyperx Stinger Wireless","nombreC5": "Onikuma Rosado",
                  "fotocomponente1" : "/static/lek/img/componentes/audifono1.png","fotocomponente2" : "/static/lek/img/componentes/audifono2.jpg" , "fotocomponente3" : "/static/lek/img/componentes/audifono3.jpg",
                  "fotocomponente4" : "/static/lek/img/componentes/audifono4.jpg", "fotocomponente5" : "/static/lek/img/componentes/audifono5.jpg"}
    return render (request, 'lek/componentes.html',contexto )

def nosotros (request):
    return render (request, 'lek/nosotros.html')

def carrito (request):
    return render (request, 'lek/carrito.html')

def audifono1 (request):
    return render (request, 'lek/audifonos/audifono1.html')
    
def audifono2 (request):
    return render (request, 'lek/audifonos/audifono2.html')
    
def audifono3 (request):
    return render (request, 'lek/audifonos/audifono3.html')

def audifono4 (request):
    return render (request, 'lek/audifonos/audifono4.html')

def audifono5 (request):
    return render (request, 'lek/audifonos/audifono5.html')

# REGISTRO #
def registro(request):
    data = { 
        'form': CustomUserCreation()
    }

    if request.method == 'POST':
        formulario = CustomUserCreation(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="menu")
        data["form"] = formulario 
    return render(request, 'registration/registro.html', data)


# AGREGAR #
# @permission_required('lek.add_producto')
# def agregar_producto(request):
#     data = {
#         'form': ProductoForm()
#     }
#     if request.method == 'POST':
#         formulario = ProductoForm(data=request.POST, files=request.FILES)
#         if formulario.is_valid():
#             formulario.save()
#             messages.success(request, "Producto Agregado")
#         else:
#             data["form"] = formulario
#     return render(request, 'lek/producto/agregar.html', data)