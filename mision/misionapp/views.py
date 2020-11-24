from django.shortcuts import render, redirect, get_object_or_404
from .models import Articulo, Usuario
from .forms import ArticuloForm, ActualizaArticuloForm, PersonalForm, ActualizaPersonalForm,CrearUsuarioForm
from django.contrib import messages
from .filters import FiltroUsuario, FiltroArticulo


def inicio(request):
    return render (request, "inicio.html")

def agregar(request):
    data = {'form':ArticuloForm() }
    articulos  = Articulo.objects.all()
    filtro = FiltroArticulo(request.GET, queryset = articulos)
    articulos = filtro.qs
    if request.method == 'POST':
        formulario = ArticuloForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data["form"]  = formulario  
    
    return render (request, "producto/agregar.html", {'form':ArticuloForm(), 'articulos':articulos, 'filtro':filtro})

def actualiza_articulo(request, id):
    articulo = get_object_or_404(Articulo, id = id)
    data = {'form': ActualizaArticuloForm(instance = articulo)}
    if request.method == "POST":
        formulario = ActualizaArticuloForm(data = request.POST, instance = articulo, files = request.FILES )
        if formulario.is_valid():
            formulario.save()
            return redirect('/agregar')
        data["form"] = formulario
    return render(request, "producto/actualizar.html", data)

def elimina_articulo(request, id):
    articulo = get_object_or_404(Articulo, id = id)
    articulo.delete()
    return redirect('/agregar')    


def agrega_personal(request):
    data = {'form':PersonalForm()}
    usuario = Usuario.objects.all()
    filtro = FiltroUsuario(request.GET, queryset = usuario)
    usuario = filtro.qs
    if request.method == "POST":
        formulario = PersonalForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data["form"] = formulario
    
    return render (request, "personal/agrega_personal.html", {'form':PersonalForm(), 'usuario':usuario, 'filtro':filtro})

def actualiza_personal(request, rut):
   
    usuario = get_object_or_404(Usuario, rut = rut)
    data = {'form' : ActualizaPersonalForm(instance = usuario)}
    if request.method == "POST":
        formulario = ActualizaPersonalForm(data = request.POST, instance = usuario, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/agrega_personal')
        data["form"] = formulario
    return render(request, "personal/actualiza_personal.html", data)    

def elimina_personal(request, rut):
    usuario = get_object_or_404(Usuario, rut = rut)
    usuario.delete()
    return redirect('/agrega_personal')
def elimina_articulo(request, id):
    articulo = get_object_or_404(Articulo, id = id)
    articulo.delete()
    return redirect('/agregar')    

def registro_usuario(request):
    data = {'form': CrearUsuarioForm()}
    if request.method == 'POST':
        formulario = CrearUsuarioForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Usuario creado correctamente")
        data["form"] = formulario    
    return render(request,"registration/registo_usuario.html", data)


def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.is_staff:
        # user is an admin
        return redirect('/admin')
    else:
        return redirect('/')