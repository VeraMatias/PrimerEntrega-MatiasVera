from django.urls import path
from ComercioOnline.views import *

urlpatterns = [
    path("inicio/", inicio, name="_inicio"),
    path("crearproducto/", crear_producto, name="_crearproducto"),
    path("crearcomprador/", crear_comprador, name="_crearcomprador"),
    path("crearvendedor/", crear_vendedor, name="_crearvendedor"),
    path("buscarproducto/", buscar_producto, name="_buscarproducto"),
    path("buscar/", buscar, name="_buscar"),
]