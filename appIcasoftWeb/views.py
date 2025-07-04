from django.shortcuts import render
from django.http import HttpResponse

def user_inicio(request):
    blogs = [
        {
            'title': 'Lanzamiento Oficial de ICASOFT AI',
            'image_url': '/static/img/blogs/blog6.png',  
            'link': 'https://icasofti21.blogspot.com/2025/05/lanzamiento-oficial-de-icasoft-ai.html',
        },
        {
            'title': 'Icasoft AI: Presentación Oficial de la 1ra IA avanzada de Soporte Técnico',
            'image_url': '/static/img/blogs/blog1.jpg',  
            'link': 'https://icasofti21.blogspot.com/2025/01/icasoft-ai-presentacion-oficial-de-la.html',
        },
        {
            'title': 'Una inteligencia artificial se ‘autoclona’ para evitar que la apaguen',
            'image_url': '/static/img/blogs/blog3.jpg',  
            'link': 'https://icasofti21.blogspot.com/2025/02/una-inteligencia-artificial-se.html',
        },
        {
            'title': 'OpenIA anuncia deep research',
            'image_url': '/static/img/blogs/blog2.jpg',  
            'link': 'https://67814d7602356.site123.me/blog/openai-anuncia-deep-research-una-nueva-herramienta-de-investigaci%C3%93n-profunda-para-chatgpt',
        },
        {
            'title': 'TECNOLOGÍA: Así puedes cambiar el color de las conversaciones de WhatsApp',
            'image_url': '/static/img/blogs/blog4.jpg',  
            'link': 'https://icasofti21.blogspot.com/2024/11/tecnologia-asi-puedes-cambiar-el-color.html',
        },
            {
            'title': 'TECNOLOGÍA: WhatsApp Plus V12: DESCARGAR la última versión actualizada para Android en noviembre 2024',
            'image_url': '/static/img/blogs/blog5.jpg',  
            'link': 'https://icasofti21.blogspot.com/2024/11/tecnologia-whatsapp-plus-v12-descargar.html',
        },
        {
            'title': 'TECNOLOGÍA: Así puedes cambiar el color de las conversaciones de WhatsApp',
            'image_url': '/static/img/blogs/blog5.jpg',  
            'link': 'https://icasofti21.blogspot.com/2024/11/tecnologia-asi-puedes-cambiar-el-color.html',
        },
            {
            'title': 'TECNOLOGÍA: Así puedes cambiar el color de las conversaciones de WhatsApp',
            'image_url': '/static/img/blogs/blog5.jpg',  
            'link': 'https://icasofti21.blogspot.com/2024/11/tecnologia-asi-puedes-cambiar-el-color.html',
        },
         
    ]

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
            'link': 'Curso/SoporteTecnicoPresencialIca/',
        },

        {
            'title': 'Proximamente más cursos',
            'image_url': '/static/img/info-cursos/proximamente.jpg',
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
            'img': '/static/img/inicio/productosTop/producto1.jpg',
            'text': 'Tinta EPSON original'
        },
        {
            'img': '/static/img/inicio/productosTop/producto2.jpg',
            'text': 'Laptop HP 15 pulgadas'
        },
        {
            'img': '/static/img/inicio/productosTop/producto4.jpg',
            'text': 'Mouse LOGITECH'
        },
         {
            'img': '/static/img/productos/tecladoGenius.webp',
            'text': 'Teclado GENIUS'
        },
    ]


    servicios = [
        {
            'nombre': 'Reparación de hardware',
            'imagen': 'img/servicios/servicio2.jpg',
            'descripcion': 'Ofrecemos servicios expertos de Reparación de Hardware para garantizar el funcionamiento adecuado de tus equipos. Desde la reparación de componentes internos hasta el reemplazo de piezas dañadas, trabajamos para devolverle a tu tecnología su máximo rendimiento con soluciones rápidas y eficaces.'
        },
        {
            'nombre': 'Actualización de software',
            'imagen': 'img/servicios/servicio1.jpg',
            'descripcion': 'Brindamos servicios de Actualización de Software para mantener tus sistemas y aplicaciones al día con las últimas mejoras y correcciones de seguridad. Aseguramos un rendimiento óptimo y protegemos tu infraestructura tecnológica contra vulnerabilidades, garantizando que siempre estés un paso adelante.'

        },
        {
            'nombre': 'Eliminación de virus y malware',
            'imagen': 'img/servicios/virus.jpg',
            'enlace': 'https://ejemplo.com/servicio3',
            'descripcion': 'Ofrecemos servicios profesionales de Eliminación de Virus y Malware para proteger tus dispositivos y datos. Detectamos, eliminamos y prevenimos amenazas cibernéticas, garantizando la seguridad de tus sistemas y evitando pérdidas de información o daños a tu infraestructura tecnológica.'

        },
        {
            'nombre': 'Marketing digital con IA',
            'imagen': 'img/servicios/diseñoWeb.jpg',
            'enlace': 'https://ejemplo.com/servicio3',
            'descripcion': 'Transforma tu negocio con soluciones de marketing digital impulsadas por IA: optimiza estrategias, personaliza experiencias y maximiza resultados con análisis avanzados y automatización inteligente.'


        },

        {
            'nombre': 'Desarrollo de Software y aplicaciones',
            'imagen': 'img/servicios/desarrollo.jpg',
            'enlace': 'https://ejemplo.com/servicio3',
            'descripcion': 'Brindamos soluciones a medida en Desarrollo de Software y Aplicaciones para impulsar la productividad de tu empresa. Diseñamos y desarrollamos plataformas personalizadas adaptados a tus necesidades específicas, asegurando eficiencia y escalabilidad.'

        },

         {
            'nombre': 'Redes de computadoras',
            'imagen': 'img/servicios/redes.jpg',
            'descripcion': 'Ofrecemos servicios especializados en Redes de Computadora para optimizar la conectividad y el rendimiento de tu infraestructura tecnológica. Desde la instalación y configuración hasta el mantenimiento y monitoreo, aseguramos una red estable, segura y eficiente para ti o para tu empresa.'
        },
    ]
    
    return render(request, "appIcasoftWeb/inicio.html", {'blogs': blogs,'fotos': fotos,'cursos': cursos, 'reviews': reviews, 'productos':productos ,'servicios': servicios})


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
    # Ejemplo con datos estáticos (reemplazar con query real)
    productos = [
        {'img': '/static/img/productos/laptop1.jpg', 'text': 'Laptop Gaming X1', 'precio': 1200},
        {'img': '/static/img/productos/laptop2.jpg', 'text': 'Laptop Empresarial E5', 'precio': 1500}
    ]
    return render(request, 'appIcasoftWeb/productos/categoria.html', {
        'productos': productos,
        'categoria': categoria
    })

def user_producto_subcategoria(request, categoria, subcategoria):
    # Ejemplo con datos estáticos
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

def user_entrega(request):
    return render(request, "appIcasoftWeb/entrega.html")

def user_configuration(request):
    return render(request, "appIcasoftWeb/configuration.html")

def user_pedido(request):
    return render(request, "appIcasoftWeb/pedido.html")
