from django import forms
from .models import Articulo, Categoria , Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = [
            'id',
            'descripcion',
            'precio',
            'categoria',
        ]



class ActualizaArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = [
            'descripcion', 
            'precio', 
            'categoria'
        ]

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

        widgets = {
        'rut': forms.TextInput(attrs={
            'placeholder': 'rut',
            'id':'txt_rut',
            'name':'rut',
            'oninput':'checkRut(this)',
                }),
    }

class ActualizaPersonalForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'apellido',
            'email',
            'calle_numero',
            'cargo',
            'comuna',
            'centro'
        ]



class CrearUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]