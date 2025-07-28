
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('Icasoft/', permanent=False)),
    path('Icasoft/', include('appIcasoftWeb.urls')),
] + static('/blog-img/', document_root='E:/icasoft/ProyectoIcasoftIA/Icasoft/SIGTR/media/blog/') + static('/portafolio-img/', document_root='E:/icasoft/ProyectoIcasoftIA/Icasoft/SIGTR/media/portafolio/') + static('/curso-img/', document_root='E:/icasoft/ProyectoIcasoftIA/Icasoft/SIGTR/media/curso/') + static('/producto-img/', document_root='E:/icasoft/ProyectoIcasoftIA/Icasoft/SIGTR/media/productos/')
