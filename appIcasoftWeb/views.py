from django.shortcuts import render
from django.http import HttpResponse
from appIcasoftWeb.models import Categoria, Blog, Proyecto, Portafolio
import os, json

def user_inicio(request):
    data_blog = Blog.objects.all()
    blogs = []

    for blog in data_blog:
        imagen_nombre = os.path.basename(blog.imagen_url.name) if blog.imagen_url else ''

        ruta_absoluta = os.path.join(
            'C:/Users/angelina/Downloads/ProyectoIcasoftIA/ProyectoIcasoftIA/Icasoft/SIGTR/media/blog',
            imagen_nombre
        )

        if blog.imagen_url and os.path.exists(ruta_absoluta):
            image_url = f'/blog-img/{imagen_nombre}'
        else:
            image_url = '/static/img/no-image.jpg'

        blogs.append({
            'title': blog.title,
            'image_url': image_url,
            'link': blog.blog_url,
        })

    data_proyecto = Proyecto.objects.filter(estado=True).prefetch_related('portafolio_set') #portafolio_set para acceder a los portafolios desde un proyecto
    proyectos = []

    for proyecto in data_proyecto:
        imagenes = []

        for portafolio in proyecto.portafolio_set.all():
            imagen_nombre = os.path.basename(portafolio.imagen_url.name) if portafolio.imagen_url else ''
            ruta_absoluta = os.path.join(
                'C:/Users/angelina/Downloads/ProyectoIcasoftIA/ProyectoIcasoftIA/Icasoft/SIGTR/media/portafolio',
                imagen_nombre
            )

            if portafolio.imagen_url and os.path.exists(ruta_absoluta):
                imagenes.append(f'/portafolio-img/{imagen_nombre}')

        if not imagenes:
            imagenes.append('/static/img/no-image.jpg')

        proyectos.append({
            'title': proyecto.title,
            'descripcion': proyecto.descripcion,
            'imagenes': imagenes,
            'imagenes_json': json.dumps(imagenes),
        })

    fotos = [
        {
        'title': 'Proyecto: IcaSoft IA',
        'image_url': '/static/img/portafolio/icasoftia/icasoftia.webp',
        'additional_images': '["/static/img/portafolio/icasoftia/icasoftia2.webp", "/static/img/portafolio/icasoftia/icasoftia3.webp", "/static/img/portafolio/icasoftia/icasoft5.jpeg"]'
        },
        {
        'title': 'Proyecto: MetalMark',
        'image_url': '/static/img/portafolio/metalmark/metalmark.webp',
        'additional_images': '["/static/img/portafolio/metalmark/extra1.webp", "/static/img/portafolio/metalmark/extra2.webp"]'
        },
        {
            'title': 'Proyecto: Shuman Peru',
            'image_url': '/static/img/portafolio/shuman/shuman1.webp',  
        'additional_images': '["/static/img/portafolio/shuman/shuman2.webp", "/static/img/portafolio/shuman/shuman3.webp"]'
           
        },
        {
            'title': 'Proyecto: Interbank',
            'image_url': '/static/img/portafolio/interbank/interbank.png',  
            'link': 'https://67814d7602356.site123.me/blog/openai-anuncia-deep-research-una-nueva-herramienta-de-investigaci%C3%93n-profunda-para-chatgpt',
        },
        {
            'title': 'Proyecto: GILAT',
            'image_url': '/static/img/portafolio/gilat/gilat.png',  
            'link': 'https://icasofti21.blogspot.com/2024/11/tecnologia-asi-puedes-cambiar-el-color.html',
        },
            {
            'title': 'Proyecto: Metalmark',
            'image_url': '/static/img/portafolio/metalmark2/metalmark.png',  
            'link': 'https://67814d7602356.site123.me/blog/openai-anuncia-deep-research-una-nueva-herramienta-de-investigaci%C3%93n-profunda-para-chatgpt',
        },
        {
            'title': 'Proyecto Vanguard Perú',
            'image_url': '/static/img/portafolio/vanguard/vanguard1.webp',  
            'link': 'https://icasofti21.blogspot.com/2024/11/tecnologia-asi-puedes-cambiar-el-color.html',
        },

    ]

    cursos = [
        {
            'title': 'Curso de Soporte Técnico - Presencial - Ica',
            'image_url': '/static/img/info-cursos/soporte.jpg',
            'link': 'Curso/SoporteTecnico/',
        },

        {
            'title': 'Curso de Ofimatica - Virtual',
            'image_url': '/static/img/info-cursos/ofimatica.jpg',
            'link': 'Curso/Ofimática/',
        },

        {
            'title': 'Proximamente más cursos',
            'image_url': '/static/img/info-cursos/proximamente.jpg',
            'link': '/#cursos',
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
         {
            'name': 'Haylú Vicuña',
            'img': '/static/img/fotousuario.jpeg',
            'text': 'Venta de laptops buenas, muy recomendado el servicio.'
        },
    ]

    productos = [
        {
            'marca': 'EPSON',
            'img': '/static/img/inicio/productosTop/producto1.jpg',
            'text': 'Tinta EPSON amarrilla',
            'precio': '35.00'
        },
        {
            'marca': 'HP',
            'img': '/static/img/inicio/productosTop/producto2.jpg',
            'text': 'Laptop HP 15 pulgadas',
            'precio': '1100.00'

        },
        {
            'marca': 'LOGITECH',
            'img': '/static/img/inicio/productosTop/producto4.jpg',
            'text': 'Mouse LOGITECH',
            'precio': '60.00'

            
        },
         {
            'marca': 'GENIUS',
            'img': '/static/img/productos/tecladoGenius.webp',
            'text': 'Teclado GENIUS',
            'precio': '45.00'
        },
    ]

    servicios = [
        {
            'nombre': 'Reparación de hardware',
            'imagen': 'img/inicio/servicios/soporte.webp',
            'descripcion': 'Ofrecemos servicios expertos de Reparación de Hardware para garantizar el funcionamiento adecuado de tus equipos. Desde la reparación de componentes internos hasta el reemplazo de piezas dañadas, trabajamos para devolverle a tu tecnología su máximo rendimiento con soluciones rápidas y eficaces.'
        },
        {
            'nombre': 'Actualización de software',
            'imagen': 'img/inicio/servicios/actualización.webp',
            'descripcion': 'Brindamos servicios de Actualización de Software para mantener tus sistemas y aplicaciones al día con las últimas mejoras y correcciones de seguridad. Aseguramos un rendimiento óptimo y protegemos tu infraestructura tecnológica contra vulnerabilidades, garantizando que siempre estés un paso adelante.'

        },
        {
            'nombre': 'Eliminación de virus y malware',
            'imagen': 'img/inicio/servicios/virus.webp',
            'descripcion': 'Ofrecemos servicios profesionales de Eliminación de Virus y Malware para proteger tus dispositivos y datos. Detectamos, eliminamos y prevenimos amenazas cibernéticas, garantizando la seguridad de tus sistemas y evitando pérdidas de información o daños a tu infraestructura tecnológica.'

        },
        {
            'nombre': 'Marketing digital con IA',
            'imagen': 'img/inicio/servicios/MarketingDigital.webp',
            'descripcion': 'Transforma tu negocio con soluciones de marketing digital impulsadas por IA: optimiza estrategias, personaliza experiencias y maximiza resultados con análisis avanzados y automatización inteligente.'
        },

        {
            'nombre': 'Desarrollo de Software y aplicaciones',
            'imagen': 'img/inicio/servicios/desarrolloWeb.webp',
            'descripcion': 'Brindamos soluciones a medida en Desarrollo de Software y Aplicaciones para impulsar la productividad de tu empresa. Diseñamos y desarrollamos plataformas personalizadas adaptados a tus necesidades específicas, asegurando eficiencia y escalabilidad.'
        },

         {
            'nombre': 'Redes de computadoras',
            'imagen': 'img/inicio/servicios/redes.webp',
            'descripcion': 'Ofrecemos servicios especializados en Redes de Computadora para optimizar la conectividad y el rendimiento de tu infraestructura tecnológica. Desde la instalación y configuración hasta el mantenimiento y monitoreo, aseguramos una red estable, segura y eficiente para ti o para tu empresa.'
        },
    ]

    return render(request, "appIcasoftWeb/inicio.html", {'blogs': blogs,'proyectos': proyectos,'cursos': cursos, 'reviews': reviews, 'productos':productos ,'servicios': servicios})


def user_curso(request, curso_nombre=None):
    cursos_info = {
        "SoporteTecnico": {
            "titulo": "Curso de Soporte Técnico - Presencial - Ica",
            "descripcion": "Nuestro curso de soporte técnico y mantenimiento de computadoras están diseñados para equipar a los estudiantes con las habilidades necesarias para diagnosticar y solucionar problemas comunes en sistemas informáticos, así como para realizar mantenimiento preventivo y correctivo.",
            'image_url': '/static/img/soporte-técnico.jpg',
            'info': "Módulos: 4<br>Duración: 2 meses <br>Incluye certificado",
            'precio': "250.00",
            'presencial_info': {
                'dirección' : "Av. Los Maestros",
                'horarios' : "Lunes a Viernes de 6pm a 9pm",
                'dias' : "Inicio 15 de cada mes",
                'duración' : "33333"
            },
            'modulos': [
                {
                    'nombre': 'Diagnóstico',
                    'clases': ['Aprende','realiza']
                },
                {
                    'nombre': 'Mantenimiento',
                    'clases': ['limpia','saca']
                }
            ]

        },
        "Ofimática": {
            "titulo": "Curso de Ofimática - Virtual",
            "descripcion": "Aprende a manejar las herramientas esenciales de Microsoft Office (Word, Excel, PowerPoint) y otras aplicaciones clave para mejorar tu productividad en tareas administrativas, crear documentos profesionales y gestionar datos eficientemente. Ideal para quienes inician en el mundo de la informática.",
            'image_url': '/static/img/cursos/office.jpg',
            'info': "Módulos: 4<br>Duración: 100 horas <br>Incluye certificado",
            'precio': "250.00",

            
        },
    }

    curso = cursos_info.get(curso_nombre, None)

    if curso is None and curso_nombre is not None:
        # Aquí podrías mostrar una página 404 o un mensaje
        return render(request, "appIcasoftWeb/curso_no_encontrado.html", {"curso_nombre": curso_nombre})

    return render(request, "appIcasoftWeb/cursos.html", {"curso": curso, "curso_nombre": curso_nombre})

def user_producto(request):
    categorias = {
        'laptops': {
            'nombre': 'Laptops', 
            'subcategorias': {
                'gaming': 'Gaming',
                'empresariales': 'Empresariales',
                'ultrabooks': 'Ultrabooks'
            }
        },
        'impresoras': {
            'nombre': 'Impresoras',
            'subcategorias': {
                'laser': 'Láser',
                'tinta': 'de Tinta',
                'multifuncion': 'Multifunción'
            }
        }
    }
    return render(request, 'appIcasoftWeb/productos/todos.html', {'categorias': categorias})

def user_producto_categoria(request, categoria):

    productos = [
        {'img': '/static/img/productos/laptop1.jpg', 'text': 'Laptop Gaming X1', 'precio': 1200},
        {'img': '/static/img/productos/laptop2.jpg', 'text': 'Laptop Empresarial E5', 'precio': 1500}
    ]
    return render(request, 'appIcasoftWeb/productos/categoria.html', {
        'productos': productos,
        'categoria': categoria
    })

def user_producto_subcategoria(request, categoria, subcategoria):
    productos = [
        {'img': '/static/img/productos/laptop-gaming.jpg', 'text': 'Laptop Gaming Pro', 'precio': 2000}
    ]
    return render(request, 'appIcasoftWeb/productos/subcategoria.html', {
        'productos': productos,
        'categoria': categoria,
        'subcategoria': subcategoria
    })



def user_contacto(request):
    return render(request, "appIcasoftWeb/contacto.html")

def user_carrito(request):
    return render(request, "appIcasoftWeb/carrito.html")

from django.shortcuts import render
from django.shortcuts import render
import json

def user_entrega(request):


    return render(request, "appIcasoftWeb/entrega.html")




def user_pedido(request):
    return render(request, "appIcasoftWeb/pedido.html")

def user_micuenta(request):
    return render(request, "appIcasoftWeb/micuenta.html")


