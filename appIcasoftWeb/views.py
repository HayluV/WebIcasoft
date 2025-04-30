from django.shortcuts import render

from django.http import HttpResponse

def user_inicio(request):
    return render(request, "appIcasoftWeb/inicio.html")

def user_curso(request):
    return render(request, "appIcasoftWeb/cursos.html")
def user_contacto(request):
    return render(request, "appIcasoftWeb/contacto.html")
def user_carrito(request):
    return render(request, "appIcasoftWeb/carrito.html")
def user_entrega(request):
    return render(request, "appIcasoftWeb/entrega.html")
def user_configuration(request):
    return render(request, "appIcasoftWeb/configuration.html")
def user_pedido(request):
    return render(request, "appIcasoftWeb/pedido.html")

