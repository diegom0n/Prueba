from django.db import models

# Create your models here.
class Marca(models.Model):
    nombreMarca = models.TextField(max_length=100)
    activoMarca = models.BooleanField()

    def __str__(self):
        return self.nombreMarca

class Categoria(models.Model):
    nombreCategoria = models.TextField(max_length=100)
    activoCategoria = models.BooleanField()

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    codigoProducto = models.IntegerField()
    nombreProducto = models.TextField()
    precioProducto = models.TextField()
    precioCosto = models.TextField()
    stockProducto = models.TextField()
    descripcionProducto = models.TextField()
    categoriaProducto = models.IntegerField()
    marcaProducto = models.IntegerField()
    activo = models.BooleanField()

    def __str__(self):
        return self.codigoProducto

class Usuario(models.Model):
    rut = models.TextField(max_length=10)
    dv = models.TextField(max_length=1)
    nombreUsuario = models.TextField(max_length=50)
    apellidosUsuario = models.TextField(max_length=100)
    fechaNac = models.DateField()
    clave = models.TextField()
    email = models.TextField()
    direccion = models.TextField()
    telefono = models.TextField(max_length=12)
    tipoUsuario = models.IntegerField()
    
    def __str__(self):
        return self.rut
    
class tipoUsuario(models.Model):
    nombreTipoUsuario = models.TextField()
    activo = models.BooleanField()

    def __str__(self):
        return self.nombreTipoUsuario

class tipoPago(models.Model):
    nombreTipoPago = models.TextField()
    activo = models.BooleanField()

    def __str__(self):
        return self.nombreTipoPago
