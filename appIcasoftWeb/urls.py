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
    path("user/Curso/", user_curso, name="user_curso"),  
    path("user/Curso/<str:curso_nombre>/", user_curso, name="user_curso_detalle"),  
    path("user/Carrito", user_carrito, name="user_carrito"),
    path("user/Entrega", user_entrega, name="user_entrega"),
    path("user/Contacto", user_contacto, name="user_contacto"),
    path("user/Configuracion", user_configuration, name="user_configuration"),
    path("user/MisPedidos", user_pedido, name="user_pedido"),
]