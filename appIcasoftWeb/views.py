from django.shortcuts import render
from django.http import HttpResponse

def user_inicio(request):
    blogs = [
        {
            'title': 'Icasoft AI: Presentación Oficial de la 1ra IA avanzada de Soporte Técnico',
            'image_url': '/static/img/blog1.jpg',  
            'link': 'https://icasofti21.blogspot.com/2025/01/icasoft-ai-presentacion-oficial-de-la.html',
        },
        {
            'title': 'Una inteligencia artificial se ‘autoclona’ para evitar que la apaguen',
            'image_url': '/static/img/blog3.jpg',  
            'link': 'https://icasofti21.blogspot.com/2025/02/una-inteligencia-artificial-se.html',
        },
        {
            'title': 'OpenIA anuncia deep research',
            'image_url': '/static/img/blog2.jpg',  
            'link': 'https://67814d7602356.site123.me/blog/openai-anuncia-deep-research-una-nueva-herramienta-de-investigaci%C3%93n-profunda-para-chatgpt',
        },
        {
            'title': 'TECNOLOGÍA: Así puedes cambiar el color de las conversaciones de WhatsApp',
            'image_url': '/static/img/blog4.jpg',  
            'link': 'https://icasofti21.blogspot.com/2024/11/tecnologia-asi-puedes-cambiar-el-color.html',
        },
    ]

    reviews = [
        {
            'name': 'Angelina Aramayo',
            'img': '/static/img/fotousuario.jpeg',
            'text': 'El servicio fue rápido y eficiente. Ahora mi computadora funciona perfectamente. ¡Muy recomendable!'
        },
        {
            'name': 'Carlos Gomez',
            'img': '/static/img/review2.png',
            'text': 'Excelente experiencia, la atención al cliente fue impecable. Muy contento con el servicio.'
        },
        {
            'name': 'Laura Torres',
            'img': '/static/img/fotousuario.jpeg',
            'text': 'Venta de impresoras de la mejor calidad.'
        },
    ]


    return render(request, "appIcasoftWeb/inicio.html", {'blogs': blogs, 'reviews': reviews})


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
