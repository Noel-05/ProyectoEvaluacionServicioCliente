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
    path('evaluacionCliente/editar_actividad/<id_actividad>/', login_required(editarActividad), name='editar_actividad'),
    path('evaluacionCliente/eliminar_actividad/<pk>/', login_required(eliminarActividad.as_view()), name='eliminar_actividad'),


    #URLs para Encuesta Cliente
    path('evaluacionCliente/listar_encuesta/', login_required(listarEncuesta), name='listar_encuesta'),
    path('evaluacionCliente/listar_encuesta/Agencia/', login_required(consultarAgencia), name='consultar_agencia'),
    path('evaluacionCliente/listar_encuesta/Agencia2/<str:codigoAgencia>/', login_required(consultarAgencia2), name='consultar_agencia2'),
    path('evaluacionCliente/listar_encuesta/Encuesta/<str:codigoAgencia>', login_required(consultarEncuesta), name='consultar_encuesta'),
    path('evaluacionCliente/listar_encuesta/Encuesta2/<str:codigoAgencia>/<str:tituloEncuesta>/', login_required(consultarEncuesta2), name='consultar_encuesta2'),
    path('evaluacionCliente/listar_encuesta/Preguntas/<str:codigoAgencia>/<str:tituloEncuesta>/', login_required(AgregarPreguntasEncuestaCliente), name='agregar_preguntas_encuesta_cliente'),

    path('evaluacionCliente/crear_encuesta/<str:codigoAgencia>/', login_required(crearEncuesta), name='crear_encuesta'),
    path('evaluacionCliente/editar_encuesta/<int:idEncuesta>/', login_required(editarEncuesta), name='editar_encuesta'),
    path('evaluacionCliente/eliminar_encuesta/<int:idEncuesta>/', login_required(eliminarEncuesta), name='eliminar_encuesta'),


    #URLs para Encuesta Personal
    path('evaluacionCliente/listar_encuesta_personal/', login_required(listarEncuestaPersonal), name='listar_encuesta_personal'),
    path('evaluacionCliente/listar_encuesta_personal/Actividad/', login_required(consultarActividadPersonal), name='consultar_actividad_personal'),
    path('evaluacionCliente/listar_encuesta_personal/Agencia2/<str:idActividad>/', login_required(consultarActividad2Personal), name='consultar_actividad2_personal'),
    path('evaluacionCliente/listar_encuesta_personal/Encuesta/<str:idActividad>', login_required(consultarEncuestaPersonal), name='consultar_encuesta_personal'),
    path('evaluacionCliente/listar_encuesta_personal/Encuesta2/<str:idActividad>/<str:tituloEncuesta>/', login_required(consultarEncuesta2Personal), name='consultar_encuesta2_personal'),
    path('evaluacionCliente/listar_encuesta_personal/Preguntas/<str:idActividad>/<str:tituloEncuesta>/', login_required(AgregarPreguntasEncuestaPersonal), name='agregar_preguntas_encuesta_personal'),

    path('evaluacionCliente/crear_encuesta_personal/<str:idActividad>/', login_required(crearEncuestaPersonal), name='crear_encuesta_personal'),
    path('evaluacionCliente/editar_encuesta_personal/<int:idEncuesta>/', login_required(editarEncuestaPersonal), name='editar_encuesta_personal'),
    path('evaluacionCliente/eliminar_encuesta_personal/<int:idEncuesta>/', login_required(eliminarEncuestaPersonal), name='eliminar_encuesta_personal'),
    
]