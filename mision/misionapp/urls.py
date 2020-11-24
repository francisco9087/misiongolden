
from django.urls import path, include
from misionapp import views
from django.contrib.auth import login
from django.conf.urls import url

urlpatterns = [
    
    
    path('agregar/',views.agregar, name = "agregar" ),
    path('actualiza_articulo/<id>/', views.actualiza_articulo, name = "actualiza_articulo"),
    path('elimina_articulo/<id>/', views.elimina_articulo, name = "elimina_articulo"),
    path('agrega_personal/', views.agrega_personal, name = "agrega_personal"),
    path('', views.inicio, name = "inicio"),
    path('', include('django.contrib.auth.urls')),
    path('actualiza_personal/<rut>/', views.actualiza_personal, name = "actualiza_personal"),
    path('elimina_personal/<rut>/', views.elimina_personal, name = "elimina_personal"),
    path('registro_usuario/', views.registro_usuario, name = 'registro_usuario'),
    path('login_success/', views.login_success, name='login_success')
]
