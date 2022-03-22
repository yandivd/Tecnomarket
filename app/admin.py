from django.contrib import admin
from .models import *


class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',) #detalles mostrados en los models

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','marca','modelo','precio','nuevo','fecha_fab')
    search_fields = ('nombre',) #campos para filtrar
    list_filter = ('marca','modelo' ,'nuevo') #filtros
    list_per_page = 9 #cantidad de registros por pagina

# Register your models here.
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)
