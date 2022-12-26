from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=50, null=True)
    apellido = models.CharField(max_length=50,  null=True)
    email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"Usuario: {self.usuario}"


class Producto(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    precio = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    imagen = models.ImageField(null=True,blank= True)

    def __str__(self):
        return f"{self.nombre}"
    
    @property
    def imageURL(self):
        try:
            url = self.imagen.url
        except:
            url = ""
        return url

    

class Orden(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.SET_NULL, null=True, blank = True)
    fecha = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)
    transaccion_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

class Item_orden(models.Model):
    producto = models.ForeignKey(Producto, on_delete= models.SET_NULL, null=True, blank = True)
    orden = models.ForeignKey(Orden, on_delete= models.CASCADE, null= True, blank=True)
    cantidad = models.IntegerField(default=0, null= True, blank=True)
    fecha = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"Item: {self.producto.nombre} Orden: {self.orden.id}"

class Direccion_envio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete= models.SET_NULL, null=True, blank=True)
    orden = models.ForeignKey(Orden, on_delete= models.SET_NULL, null=True, blank=True)
    telefono = models.IntegerField(null=True)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.direccion
    

# Create your models here.
