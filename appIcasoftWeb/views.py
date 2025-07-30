from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from appIcasoftWeb.models import User, Categoria, SubCategoria, Producto, Blog, Curso ,Proyecto, Portafolio, ModuloCurso, Horario
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from appIcasoftWeb.forms import UserForm
import os, json
import requests


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('email') 
        password = request.POST.get('password')
    
        user = authenticate(request, username=username, password=password)
        if user is not None and user.role == 'client':
            login(request, user)
            return redirect('user_inicio')
        else:
            return redirect('user_inicio')
    return render(request, 'appIcasoftWeb/inicio.html')

def user_register(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, "appIcasoftWeb/registrarse.html", {'form': form})

    elif request.method == 'POST':
        form = UserForm(request.POST)
       
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'client' 
            user.username = request.POST.get('first_name') #es el name del form 
            user.set_password(request.POST.get('password'))  
            user.save()

            login(request, user) 

            return JsonResponse({'success': 'Usuario creado'}, status=200)
        else:
            return JsonResponse({'error': 'Verifique los campos'}, status=400)

def user_dni(request):
    if request.method == 'POST':
        dni = request.POST.get('dni')
        users_dni = User.objects.all().filter(dni=dni,is_active=True).count()

        if users_dni == 0 and len(dni) == 8:
            url = f"https://api.apis.net.pe/v1/dni?numero={dni}"
            dni_api_key = os.environ.get('API_DNI_TOKEN') 

            headers = {
                "Authorization": f"Bearer {dni_api_key}"
            }

            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()
                return JsonResponse(data)
            except requests.RequestException as e:
                return JsonResponse({'error': 'Error al consultar el DNI.'}, status=500)

        elif users_dni > 0:
            return JsonResponse({'error': 'Ya existe un usuario registrado con el DNI'}, status=400)
        else:
            return JsonResponse({'error': 'DNI inválido'}, status=400)

    return render(request, "appIcasoftWeb/registrarse.html")
    

def user_logout(request):
    logout(request)
    return redirect('user_inicio')

def user_inicio(request):
    # Blogs
    data_blog = Blog.objects.all().order_by('-fechaModificacion')
    blogs = []

    for blog in data_blog:
        imagen_nombre = os.path.basename(blog.imagen_url.name) if blog.imagen_url else ''

        ruta_absoluta = os.path.join(
            'E:/icasoft/ProyectoIcasoftIA/Icasoft/SIGTR/media/blog',
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

    # Portafolios
    data_proyecto = Proyecto.objects.filter(estado=True).order_by('-fechaModificacion').prefetch_related('portafolio_set') #portafolio_set para acceder a los portafolios desde un proyecto
    proyectos = []

    for proyecto in data_proyecto:
        imagenes = []

        for portafolio in proyecto.portafolio_set.all():
            imagen_nombre = os.path.basename(portafolio.imagen_url.name) if portafolio.imagen_url else ''
            ruta_absoluta = os.path.join(
                'E:/icasoft/ProyectoIcasoftIA/Icasoft/SIGTR/media/portafolio',
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
    
    # Cursos
    data_cursos = Curso.objects.all().filter(estado=True).order_by('-fechaModificacion')
    cursos = []

    for curso in data_cursos:
        imagen_nombre = os.path.basename(curso.imagenCurso.name) if curso.imagenCurso else ''

        ruta_absoluta = os.path.join(
            'E:/icasoft/ProyectoIcasoftIA/Icasoft/SIGTR/media/curso',
            imagen_nombre
        )

        if curso.imagenCurso and os.path.exists(ruta_absoluta):
            image_url = f'/curso-img/{imagen_nombre}'
        else:
            image_url = '/static/img/no-image.jpg'

        cursos.append({
            'title': curso.nombre,
            'image_url': image_url,
        })

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

#Es el parámetro que le pasaré para que todas las demmás views funcionen
def user_curso(request, curso_nombre=None):
    cursos_activos = Curso.objects.filter(
        estado=True,
        nombre=curso_nombre
    ).first() 

    cursos_data = construir_datos_cursos(cursos_activos)

    return render(request, 'appIcasoftWeb/cursos.html', {
        'curso': cursos_data
    })

#Traer data de los módulos y horarios del curso:
def construir_datos_cursos(curso):
    modulo = ModuloCurso.objects.filter(idCurso = curso).select_related('idCurso')
    horario = Horario.objects.filter(codigoCurso = curso).select_related('codigoCurso')
    curso_data_modulo = [construir_datos_modulos(cur) for cur in modulo]
    curso_data_horario = [construir_datos_horarios(hor) for hor in horario]

    imagen_nombre = os.path.basename(curso.imagenCurso.name) if curso.imagenCurso else ''
    ruta_absoluta = os.path.join(
        'E:/icasoft/ProyectoIcasoftIA/Icasoft/SIGTR/media/curso',imagen_nombre
    )

    if curso.imagenCurso and os.path.exists(ruta_absoluta):
        image_url = f'/curso-img/{imagen_nombre}'
    else:
        image_url = '/static/img/no-image.jpg'

    return {
        'idCurso': curso.codigo,
        'nombreC': curso.nombre,
        'descrC': curso.descripcion,
        'precio': curso.precio,
        'fechaModificacion': curso.fechaModificacion,
        'imagen':image_url,
        'modulos': curso_data_modulo,
        'horarios':curso_data_horario,
    }
#Traer data del módulo que va a estar asociado al curso seleccionado
def construir_datos_modulos(modulo):
    return {
        'id': modulo.idModulo,
        'title': modulo.title,
        'descripcion': modulo.descripcion,
        'idCurso': modulo.idCurso,
    }
# Traer data del horrario que va a estar asociado al curso seleccionado
def construir_datos_horarios(horario):
    return {
        'id': horario.id,
        'day_start': horario.day_start,
        'day_end': horario.day_end,
        'dias':horario.dias
    }

def user_contacto(request):
    return render(request, "appIcasoftWeb/contacto.html")

def user_micuenta(request):
    if request.method == 'GET':
        return render(request, "appIcasoftWeb/MiCuenta.html")

    elif request.method == 'POST':
        idUser = request.POST.get('id')
        id = get_object_or_404(User, pk=idUser)
        form = UserForm(request.POST, instance=id)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST.get('password'))  
            user.save()
            login(request, user) 
            return JsonResponse({'success': 'Usuario actualizado'}, status=200)
        else:
            return JsonResponse({
                'error': 'Verifique los campos',
                'form_errors': form.errors
            }, status=400)

def user_pedido(request):
    return render(request, "appIcasoftWeb/pedido.html")

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


RUTA_MEDIA_PRODUCTOS = 'E:/icasoft/ProyectoIcasoftIA/Icasoft/SIGTR/media/productos'
IMAGEN_POR_DEFECTO = '/static/img/no-image.jpg'

def obtener_url_imagen(producto):

    if not producto.imagenProducto:
        return IMAGEN_POR_DEFECTO

    nombre_imagen = os.path.basename(producto.imagenProducto.name)
    ruta_imagen = os.path.join(RUTA_MEDIA_PRODUCTOS, nombre_imagen)

    if os.path.exists(ruta_imagen):
        return f'/producto-img/{nombre_imagen}'
    return IMAGEN_POR_DEFECTO

#Información de todos los productos:
def construir_datos_producto(producto):
    return {
        'id': producto.idProducto,
        'nombre': producto.nombreProducto,
        'descripcion': producto.descripcionProducto,
        'precio': producto.precioVenta,
        'stock': producto.stock,
        'imagen_url': obtener_url_imagen(producto),
        'slug': producto.slug
    }

#Información de todos los productos por la subcategoría seleccionada.
def construir_datos_subcategoria(subcategoria):
    productos = Producto.objects.filter(
        estado=True,
        idSubCategoria=subcategoria.idSub
    ).select_related('idSubCategoria') #realiza una sola consulta SQL con JOIN para traer no solo los productos, sino también la subcategoría asociada (idSubCategoria) en una sola consulta a la base de datos. Para evitar el: for producto in productos:

    productos_data = [construir_datos_producto(prod) for prod in productos]

    return {
        'id': subcategoria.idSub,
        'nombre': subcategoria.nombre,
        'slugSub': subcategoria.slug,
        'productos': productos_data
    }

# Información de todos los productos y subcategorías por selección de categoría. 
def construir_datos_categoria(categoria_obj):
    subcategorias = SubCategoria.objects.filter(
        estado=True,
        idCategoria=categoria_obj.idCategoria
    )

    subcategorias_data = [construir_datos_subcategoria(sub) for sub in subcategorias]

    return {
        'id': categoria_obj.idCategoria,
        'nombre': categoria_obj.nombreCategoria,
        'slugcat': categoria_obj.slug,
        'subcategorias': subcategorias_data
    }

def user_producto_categoria(request, categoria):
    """
    Vista que muestra los productos por categoría. url: dashboard/categoria
    """
    categorias_activas = Categoria.objects.filter(
        estadoCategoria=True,
        slug=categoria
    ).first() 

    categorias_data = construir_datos_categoria(categorias_activas)

    return render(request, 'appIcasoftWeb/productos/categoria.html', {
        'categoria': categorias_data
    })

def user_producto_subcategoria(request, categoria, subcategoria):
    """
    Vista que muestra los productos por subcategoría. url: dashboard/categoria/subcategoria
    """
    categorias_activas = Categoria.objects.filter(
        estadoCategoria=True,
        slug=categoria
    ).first() 

    subcategorias_activas = SubCategoria.objects.filter(
        estado=True,
        slug=subcategoria,
        idCategoria=categorias_activas.idCategoria
    ).first()

    categorias_data = construir_datos_categoria(categorias_activas)
    subcategoria_data = construir_datos_subcategoria(subcategorias_activas)

    return render(request, 'appIcasoftWeb/productos/subcategoria.html', {
        'categoria': categorias_data,
        'subcategoria': subcategoria_data
    })

def user_carrito(request):
    return render(request, "appIcasoftWeb/carrito.html")

def user_entrega(request):
    return render(request, "appIcasoftWeb/entrega.html")






