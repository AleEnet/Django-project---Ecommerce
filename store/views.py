from django.shortcuts import render
from .models import *

def main(request):
    context={}
    return render(request,"store/main.html",context)

def store(request):
    productos = Producto.objects.all()
    context={"productos": productos}
    return render(request,"store/store.html",context)

def checkout(request):
    context={}
    return render(request,"store/checkout.html",context)

def cart(request):
    if request.user.is_authenticated:
        usuario = request.user.cliente
        orden, nueva_orden = Orden.objects.get_or_create(cliente = usuario, completado = False )
        items = orden.item_orden_set.all()
    else:
        items = []

    context={"items":items}
    return render(request,"store/cart.html",context)

