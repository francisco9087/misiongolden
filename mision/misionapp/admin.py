from django.contrib import admin
from misionapp.models import Categoria, Departamento, Articulo, Asignacion

# Register your models here.

class DescripcionArticulo(admin.ModelAdmin):
    list_display = ('categoria',)


admin.site.register(Categoria)
admin.site.register(Departamento)
admin.site.register(Articulo, DescripcionArticulo )
admin.site.register(Asignacion)