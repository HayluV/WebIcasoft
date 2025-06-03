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

    cursos = [
        {
            'title': 'Curso de Soporte Técnico',
            'image_url': '/static/img/curso1.jpg',
            'link': 'user/Curso/SoporteTecnico/',
        },

        {
            'title': 'Curso de Soporte Técnico - Presencial - Ica',
            'image_url': '/static/img/curso1.jpg',
            'link': 'user/Curso/SoporteTecnicoPresencialIca/',
        },

        {
            'title': 'Curso marketing Digital',
            'image_url': '/static/img/curso2.jpg',
            'link': 'user/Curso/SoporteTecnico-Presencial/',
        }
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
         {
            'name': 'Haylú Vicuña',
            'img': '/static/img/fotousuario.jpeg',
            'text': 'Venta de laptops buenas, muy recomendado el servicio.'
        },
    ]

    return render(request, "appIcasoftWeb/inicio.html", {'blogs': blogs,'cursos': cursos, 'reviews': reviews})
def user_curso(request, curso_nombre=None):
    cursos_info = {
        "SoporteTecnico": {
            "titulo": "Curso de Soporte Técnico",
            "descripcion": "Nuestro curso de soporte técnico y mantenimiento de computadoras están diseñados para equipar a los estudiantes con las habilidades necesarias para diagnosticar y solucionar problemas comunes en sistemas informáticos, así como para realizar mantenimiento preventivo y correctivo.",
            'image_url': '/static/img/soporte-técnico.jpg',
            'info': "Módulos: 4<br>Horas: 100 horas<br>Incluye certificado",
        },
        "SoporteTecnicoPresencialIca": {
            "titulo": "Curso de Soporte Técnico - Presencial - Ica",
            "descripcion": "Nuestro curso de soporte técnico y mantenimiento de computadoras están diseñados para equipar a los estudiantes con las habilidades necesarias para diagnosticar y solucionar problemas comunes en sistemas informáticos, así como para realizar mantenimiento preventivo y correctivo en la ciudad de Ica.",
            'image_url': '/static/img/soporte-técnico.jpg',
            'info': "Módulos: 4<br>Duración: 2 meses <br>Incluye certificado",
            
        },
    }

    curso = cursos_info.get(curso_nombre, None)

    if curso is None and curso_nombre is not None:
        # Aquí podrías mostrar una página 404 o un mensaje
        return render(request, "appIcasoftWeb/curso_no_encontrado.html", {"curso_nombre": curso_nombre})

    return render(request, "appIcasoftWeb/cursos.html", {"curso": curso, "curso_nombre": curso_nombre})



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
