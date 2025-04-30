from django.shortcuts import render

from django.http import HttpResponse

def user_inicio(request):
    return render(request, "appIcasoftWeb/inicio.html")
