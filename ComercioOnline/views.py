from django.shortcuts import render
from ComercioOnline.views import *
from ComercioOnline.forms import *
from .models import *

# Create your views here.

def inicio(request):
    return render (request, "index.html")

def crear_producto(request):

    if request.method == "POST":
        form=Form_producto(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            producto_nuevo=Producto(titulo=informacion["txt_titulo"], descripcion = informacion["txt_descripcion"], precio = informacion["int_precio"])
            producto_nuevo.save()
            return render (request, "index.html")
    else:
        formulario = Form_producto()      
    
    return render (request, "crear_producto.html", {"form":formulario})

def crear_comprador(request):

    if request.method == "POST":
        form=Form_comprador(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            comprador_nuevo=Comprador(nombre = informacion["txt_nombre"], DNI = informacion["int_DNI"], email = informacion["txt_email"], contrasenia = informacion["txt_contrasenia"], direccion_de_envio = informacion["txt_direccion_de_envio"])
            comprador_nuevo.save()
            return render (request, "index.html")
    else:
        formulario = Form_comprador() 

    return render (request, "crear_comprador.html", {"form":formulario})

def crear_vendedor(request):
    if request.method == "POST":
        form=Form_vendedor(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            vendedor_nuevo=Vendedor(nombre = informacion["txt_nombre"], DNI = informacion["int_DNI"], email = informacion["txt_email"], contrasenia = informacion["txt_contrasenia"])
            vendedor_nuevo.save()
            return render (request, "index.html")
    else:
        formulario = Form_vendedor()

    return render (request, "crear_vendedor.html", {"form":formulario})


def buscar_producto(request):

    return render(request, "buscar_producto.html")

def buscar(request):

    if request.GET["busq_titulo"]:

        comision=request.GET["busq_titulo"]

        resultados=Producto.objects.filter(titulo__icontains=comision)
        return render(request,"resultados_busqueda.html", {"resultados":resultados} )
    else:
        return render(request, "buscar_producto.html")









