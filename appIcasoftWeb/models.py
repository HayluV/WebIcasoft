from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("El correo electrónico es obligatorio")
        if not username:
            raise ValueError("El nombre de usuario es obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", "admin")
        extra_fields.setdefault("can_add_admin", True)  

        if extra_fields.get("is_staff") is not True:
            raise ValueError("El superusuario debe tener is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("El superusuario debe tener is_superuser=True.")
        if extra_fields.get("role") not in ["admin", "superadmin"]:
            raise ValueError("El superusuario debe tener el rol 'admin' o 'superadmin'.")

        return self.create_user(email, username, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    ROLES = (
        ('admin', 'Administrador'),
        ('tech', 'Técnico'),
        ('client', 'Cliente'),
    )

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True) # va a jalar de la bd esto, obtener los valores de la bd
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    role = models.CharField(max_length=10, choices=ROLES, default='client')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    can_add_admin = models.BooleanField(default=False)  # Indica si el usuario puede agregar otros admins

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'telefono']
    class Meta:
        managed = False
        db_table = 'users_user'
    def __str__(self):
        return self.email #esto es lo que retorna
    
class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=100)
    estadoCategoria = models.BooleanField(default=True)
    fechaCreacionCategoria = models.DateTimeField(auto_now_add=True)
    fechaModificacionCategoria = models.DateTimeField(auto_now=True)
    class Meta:
        managed = False
        db_table = 'users_categoria'

    def __str__(self):
        return self.nombreCategoria
    
class SubCategoria(models.Model):
    idSub = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'users_subcategoria'

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=200)
    descripcionProducto = models.TextField()
    idSubCategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE, null=True, blank=True)
    stock = models.IntegerField(default=0)
    precioVenta = models.DecimalField(max_digits=10, decimal_places=2)
    precioCompra = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)
    fechaCaducidad = models.DateField(null=True, blank=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagenProducto = models.ImageField(upload_to='productos/', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'users_producto'
    
    def __str__(self):
        return self.title
   
class Curso(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=2000)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now_add=True)
    imagenCurso = models.ImageField(upload_to='curso/', null = True, blank=False)

    class Meta:
        managed = False
        db_table = 'users_curso'
    def __str__(self):
        return self.nombre
class ModuloCurso(models.Model):
    idModulo = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    descripcion = models.TextField(max_length=2000)
    idCurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
    class Meta:
        managed = False
        db_table = 'users_modulocurso'
    def __str__(self):
        return self.title 
class Horario(models.Model):
    codigoCurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    day_start = models.DateField(blank=True, null=True)
    day_end = models.DateField(blank=True, null=True)
    dias = models.TextField(max_length=500)

    class Meta:
        managed = False
        db_table = 'users_horario'
    
    def __str__(self):
        return self.dias
    
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    blog_url = models.URLField(verbose_name="URL de blogs")
    imagen_url = models.ImageField(upload_to='blog/', null = True, blank=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = False
        db_table = 'users_blog'
    def __str__(self):
        return self.title

class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=2000)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = False
        db_table = 'users_proyecto'
    def __str__(self):
        return self.title
class Portafolio(models.Model):
    idProyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    imagen_url = models.ImageField(upload_to='portafolio/', null = True, blank=True)
    class Meta:
        managed = False
        db_table = 'users_portafolio'
    def __str__(self):
        return self.imagen_url.url
    
class Carrito(models.Model):
    idCarrito = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    precioConImpuesto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cantidadSeleccionada = models.IntegerField(default=0)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    class Meta:
        managed = False
        db_table = 'users_carrito'

    def __str__(self):
        return f"Carrito de {self.idUsuario.username}"

class RegistroVenta(models.Model):
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    )
    
    idRegistroVenta = models.AutoField(primary_key=True)
    serieVenta = models.CharField(max_length=50)
    numVenta = models.CharField(max_length=50)
    horaVenta = models.TimeField(auto_now_add=True)
    igv = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    numCuotas = models.IntegerField(default=1)
    subTotal = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    totalVenta = models.DecimalField(max_digits=10, decimal_places=2)
    estadoVenta = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    idTipoC = models.ForeignKey('TipoComprobante', on_delete=models.CASCADE)
    idMetodoP= models.ForeignKey('MetodoPago', on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'users_registroventa'
    def __str__(self):
        return f"Venta {self.serieVenta}-{self.numVenta}"

class DetalleVenta(models.Model):
    idDetalleVenta = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    precioTotalProducto = models.DecimalField(max_digits=10, decimal_places=2)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idRegistroVenta = models.ForeignKey(RegistroVenta, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'users_detalleventa'
    def __str__(self):
        return f"Detalle {self.idRegistroVenta.serieVenta}-{self.idRegistroVenta.numVenta} - {self.idProducto.nombreProducto}"

class Ubicacion(models.Model):
    idUbicacion = models.AutoField(primary_key=True)
    direccion = models.TextField()
    tiempoEntrega = models.IntegerField(help_text="Tiempo en días")
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    class Meta:
        managed = False
        db_table = 'users_ubicacion'
    def __str__(self):
        return self.direccion

class TipoComprobante(models.Model):
    idTipoC = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    class Meta:
        managed = False
        db_table = 'users_tipocomprobante'
    def __str__(self):
        return self.nombre

class MetodoPago(models.Model):
    idMetodoP = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    class Meta:
        managed = False
        db_table = 'users_metodopago'
    def __str__(self):
        return self.nombre

class Entrega(models.Model):
    ESTADO_CHOICES = (
        ('preparado', 'Preparado'),
        ('en_camino', 'En Camino'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    )
    
    idEntrega = models.AutoField(primary_key=True)
    fechaPreparado = models.DateTimeField(null=True, blank=True)
    fechaEntrega = models.DateTimeField(null=True, blank=True)
    estadoEntrega = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='preparado')
    idRegistroVenta = models.ForeignKey(RegistroVenta, on_delete=models.CASCADE)
    idUbicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'users_entrega'
    def __str__(self):
        return f"Entrega para venta {self.idRegistroVenta.serieVenta}-{self.idRegistroVenta.numVenta}"

class CompraRecurrente(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(default=1)
    nombre = models.CharField(max_length=200)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    idRegistroVenta = models.ForeignKey(RegistroVenta, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'users_comprarecurrente'
    def __str__(self):
        return self.nombre
    
class TipoAsistenciaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='open')

class TipoAsistencia(models.Model):
    STATUS_CHOICES = (
        ('open', 'Activo'),
        ('closed', 'Eliminado'),
    )

    tipo_asistencia = models.CharField(max_length=30, unique=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TipoAsistenciaManager()    
    all_objects = models.Manager()          

    class Meta:
        db_table = 'users_asistencia'
        managed = False
        verbose_name = "Tipo de Asistencia"
        verbose_name_plural = "Tipos de Asistencia"
        ordering = ['tipo_asistencia']

    def __str__(self):
        return f"{self.tipo_asistencia} ({self.get_status_display()})"

    def soft_delete(self):
        self.status = 'closed'
        self.save()

    def restore(self):
        self.status = 'open'
        self.save()