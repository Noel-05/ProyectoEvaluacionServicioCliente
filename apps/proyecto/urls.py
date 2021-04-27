from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.conf.urls.static import static 
 
app_name = 'evaluacionCliente'

urlpatterns = [
    
    # URL de base 
    path('', login_required(index)),
    path('evaluacionCliente/index/', login_required(index), name='index'),


	#URLs para Departamento
    path('evaluacionCliente/crear_departamento/', login_required(crearDepartamento), name='crear_departamento'),
    path('evaluacionCliente/listar_departamento/', login_required(listarDepartamento), name='listar_departamento'),
    path('evaluacionCliente/editar_departamento/<codigo_departamento>/', login_required(editarDepartamento), name='editar_departamento'),
    path('evaluacionCliente/eliminar_departamento/<pk>/', login_required(eliminarDepartamento.as_view()), name='eliminar_departamento'),

	#URLs para Comites
    path('evaluacionCliente/crear_comite/', login_required(crearComite), name='crear_comite'),
    path('evaluacionCliente/listar_comite/', login_required(listarComite), name='listar_comite'),
    path('evaluacionCliente/editar_comite/<id_comite>/', login_required(editarComite), name='editar_comite'),
    path('evaluacionCliente/eliminar_comite/<pk>/', login_required(eliminarComite.as_view()), name='eliminar_comite'),

	#URLs para Agencias
    path('evaluacionCliente/crear_agencia/', login_required(crearAgencia), name='crear_agencia'),
    path('evaluacionCliente/listar_agencia/', login_required(listarAgencia), name='listar_agencia'),    
    path('evaluacionCliente/editar_agencia/<codigo_agencia>/', login_required(editarAgencia), name='editar_agencia'),
    path('evaluacionCliente/eliminar_agencia/<pk>/', login_required(eliminarAgencia.as_view()), name='eliminar_agencia'),

    #URLs para Actividades
    path('evaluacionCliente/crear_actividad/', login_required(crearActividad), name='crear_actividad'),
    path('evaluacionCliente/listar_actividad/', login_required(listarActividad), name='listar_actividad'),    
    path('evaluacionCliente/eliminar_actividad/<pk>/', login_required(eliminarActividad.as_view()), name='eliminar_actividad'),



]