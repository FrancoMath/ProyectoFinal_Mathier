from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()
    en_stock = models.CharField(max_length=5)
    en_promocion = models.CharField(max_length=5)

    def __str__(self):
        return f"Nombre: {self.nombre} \n - Precio: $ {self.precio}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    email = models.EmailField(max_length=40)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Direccion: {self.direccion}"


class Pedido_basico(models.Model):
    cliente_pedido = models.CharField(max_length=100)
    fecha_pedido = models.DateField()
    horario_entrega = models.CharField(max_length=100)
    detalle_pedido = models.TextField()
    estado_pedido = models.CharField(max_length=50, default="Pendiente")

class Pedido(models.Model):
    cliente_pedido = models.CharField(max_length=100)
    fecha_pedido = models.DateField()
    horario_entrega = models.CharField(max_length=100)
    detalle_pedido = models.TextField()
    estado_pedido = models.CharField(max_length=50, default="Pendiente")


class MiPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_apellido = models.CharField(max_length=100, null=True)
    fecha_pedido = models.DateField()
    horario_entrega = models.CharField(max_length=100)
    lugar_entrega = models.CharField(max_length=100)
    estado_pedido = models.CharField(max_length=50, default="Pendiente")
    detalle_pedido = models.TextField()

class Promocion(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    titulo_promo = models.CharField(max_length=100)
    descripcion_promo = models.TextField()
    precio_promo = models.DecimalField(max_digits=8, decimal_places=2)
    estado_promo = models.CharField(max_length=50)
    imagen_promo = models.ImageField(upload_to='imagenes_promo/', blank=True, null=True)

    def __str__(self):
        return f"Promo: {self.titulo_promo} \n - Fin: {self.fecha_fin} - Estado: {self.estado_promo} "


class Comentario(models.Model):
    comentario = models.ForeignKey(Promocion, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    mensaje = models.TextField(null=True, blank=True)
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_comentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.appellido, self.comentario)

# class Pedido(models.Model):
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     productos = models.ManyToManyField(Producto, through='DetallePedido')
#     fecha_pedido = models.DateTimeField(auto_now_add=True)
#     total = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Pedido: #{self.id} - Cliente: {self.cliente.nombre} - Fecha: {self.fecha_pedido}"

# class DetallePedido(models.Model):
#     pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     cantidad = models.PositiveIntegerField()
#     subtotal = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Detalle del Pedido #{self.pedido.id} - {self.producto.nombre}"

