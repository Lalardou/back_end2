from django.shortcuts import render
from .models import AgregarProducto
from .forms import  CustomUserCreation, ContactosForm, AddProductoForm
from django.shortcuts import render, redirect, get_object_or_404
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

def componenteM (request):
    contexto = {"nombreM" :"Monitor","nombreM1":"LG 24" , "nombreM2":"Philips 24", "nombreM3": "Monitor Asus","nombreM4" :"Samsung Odyssey","nombreM5": "BenQ PD",
                  "fotocomponenteM1" : "/static/lek/img/componentes/monitor1.jpg","fotocomponenteM2" : "/static/lek/img/componentes/monitor2.jpg" , "fotocomponenteM3" : "/static/lek/img/componentes/monitor3.jpg",
                  "fotocomponenteM4" : "/static/lek/img/componentes/monitor4.jpg", "fotocomponenteM5" : "/static/lek/img/componentes/monitor5.jpg"}
    return render (request, 'lek/componenteM.html',contexto )

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

def monitor1 (request):
    return render (request, 'lek/monitores/monitor1.html')
    
def monitor2 (request):
    return render (request, 'lek/monitores/monitor2.html')


def monitor3 (request):
    return render (request, 'lek/monitores/monitor3.html')


def monitor4 (request):
    return render (request, 'lek/monitores/monitor4.html')
    
def monitor5 (request):
    return render (request, 'lek/monitores/monitor5.html')

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
@permission_required('lek.add_productos')
def add_productos(request):
    data = {
        'form': AddProductoForm()
    }
    
    if request.method == 'POST':
        formulario = AddProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Agregado")
        else:
            data["form"] = formulario
    return render(request, 'lek/producto/agregar.html', data)  

def listar_productos(request):
    productos = AgregarProducto.objects.all()

    data = {
        'productos': productos
    }

    return render (request, 'lek/producto/listar.html',data)

# MODIFICAR #
@permission_required('lek.change_producto')
def modificar_productos(request, id):
    producto = get_object_or_404(AgregarProducto, id=id)
    data = { 
        'form': AddProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = AddProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificacion Exitosa")
            return redirect(to="listar_productos")
        data["form"] = formulario   
    return render(request, 'lek/producto/modificar.html',data)

# ELIMINAR #
@permission_required('lek.delete_producto')
def eliminar_productos(request, id):
    producto = get_object_or_404(AgregarProducto, id=id)
    producto.delete()
    return redirect(to="listar_productos")