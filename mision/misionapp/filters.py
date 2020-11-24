import django_filters
from .models import *


class FiltroUsuario(django_filters.FilterSet):
    class Meta:
        model = Usuario
        fields = [
            'rut',
            'apellido',
            'cargo',
            'centro'
        ]


class FiltroArticulo(django_filters.FilterSet):
    class Meta:
        model = Articulo
        fields = [
            'descripcion',
            'categoria',
        ]