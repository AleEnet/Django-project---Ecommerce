from django.contrib import admin
from .models import *

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Orden)
admin.site.register(Item_orden)
admin.site.register(Direccion_envio)

# Register your models here.
