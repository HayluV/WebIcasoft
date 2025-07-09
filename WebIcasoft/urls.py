
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('appIcasoftWeb.urls')),
] + static('/blog-img/', document_root='E:/icasoft/ProyectoIcasoftIA/Icasoft/SIGTR/media/blog/') + static('/portafolio-img/', document_root='E:/icasoft/ProyectoIcasoftIA/Icasoft/SIGTR/media/portafolio/')