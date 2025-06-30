from django.urls import path
from .views import user_inicio
from .views import (
    user_inicio,
    user_curso,
    user_contacto,
    user_carrito,
    user_entrega,
    user_configuration,
    user_pedido,
)

urlpatterns = [
    path("", user_inicio, name="user_inicio"),
    path("Curso/", user_curso, name="user_curso"),  
    path("Curso/<str:curso_nombre>/", user_curso, name="user_curso_detalle"),  
    path("Carrito", user_carrito, name="user_carrito"),
    path("Entrega", user_entrega, name="user_entrega"),
    path("Contacto", user_contacto, name="user_contacto"),
    path("Configuracion", user_configuration, name="user_configuration"),
    path("MisPedidos", user_pedido, name="user_pedido"),
]