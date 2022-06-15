from django.shortcuts import render, redirect, get_object_or_404
from app.models import Producto
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'app/home.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def galeria(request):
    return render(request, 'app/galeria.html')

def agregar_producto(request):
    
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"

        else:
            data["form"] = formulario

    return render(request, 'app/producto/agregar.html', data)

def listar_productos(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }

    return render(request, 'app/producto/listar.html', data)

def modificar_producto(request, id):
    
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto , files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listado_productos")

        else:
            data["form"] = formulario

    data = {
        'form': ProductoForm(instance=producto)
    }

    return render(request, 'app/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listado_productos")    

def login(request):
    return render(request, 'app/login.html')

def registro(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    return render(request, 'registration/registro.html', data)