from django.shortcuts import render
from .forms import  CustomUserCreation
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login

# Create your views here.

def menu (request):
    return render (request, 'lek/menu.html')

def contactos (request):
    return render (request, 'lek/contactos.html')
    
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