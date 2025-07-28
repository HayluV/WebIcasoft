from django.urls import path
from .views import user_inicio
from .views import (
    user_inicio,
    user_login,
    user_register,
    user_dni,
    user_logout,
    user_curso,
    user_producto,
    user_producto_categoria,
    user_producto_subcategoria,
    user_contacto,
    user_carrito,
    user_entrega,
    user_micuenta,
    user_pedido,
)

urlpatterns = [
    path("", user_inicio, name="user_inicio"),
    path("Login/", user_login, name="user_login"),
    path("Registrarse/", user_register, name="user_register"),
    path("APIDNI/", user_dni, name="user_api_dni"),
    path("Logout/", user_logout, name="user_logout"),
    path("Curso/", user_curso, name="user_curso"),  
    path("Curso/<str:curso_nombre>/", user_curso, name="user_curso_detalle"),  
    path("Productos/", user_producto, name="user_producto"), 
    path("Productos/<slug:categoria>/", user_producto_categoria, name="user_producto_categoria"),
    path("Productos/<slug:categoria>/<slug:subcategoria>/", user_producto_subcategoria, name="user_producto_subcategoria"),
    path("Contacto/", user_contacto, name="user_contacto"),
    path("Carrito/", user_carrito, name="user_carrito"),
    path("Entrega/", user_entrega, name="user_entrega"),
    path("MiCuenta/", user_micuenta, name="user_micuenta"),
    path("MisPedidos/", user_pedido, name="user_pedido"),
]
