from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.core import serializers
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from .models import *
from .forms import *

#----------------------------------------------------------------------------------------------------------------------------------


#Vista para el menu base
def index(request):
    return render(
        request,
        'base/base.html'
    )


#----------------------------------------------------------------------------------------------------------------------------------


#	CRUD DEPARTAMENTO

# Crear departamento
def crearDepartamento(request):
	if request.method == 'POST':
		departamento_form = DepartamentoForm(request.POST)
		if departamento_form.is_valid():
			departamento_form.save()
			return HttpResponseRedirect(reverse_lazy('evaluacionCliente:listar_departamento'))  
	else:
		departamento_form = DepartamentoForm()
	return render(request, 'evaluacionCliente/crear_departamento.html', {'departamento_form': departamento_form})


# Vista para el Departamento
def listarDepartamento(request):
	departamentos = Departamento.objects.all()
	#Mandar la consulta al template
	return render(request, 'evaluacionCliente/listar_departamento.html', {'departamentos': departamentos})		


# Editar Departamento
def editarDepartamento(request, codigo_departamento):
	departamento_form = None
	error = None

	try:
		departamento =Departamento.objects.get(codigo_departamento = codigo_departamento)
		if request.method =='GET':
			departamento_form=DepartamentoForm(instance = departamento)
		else:
			departamento_form = DepartamentoForm(request.POST, instance = departamento)
			if departamento_form.is_valid():
				departamento_form.save()
			return HttpResponseRedirect(reverse_lazy('evaluacionCliente:listar_departamento'))
	except ObjectDoesNotExist as e:
		error = e
	return render(request, 'evaluacionCliente/editar_departamento.html', {'departamento_form': departamento_form, 'error':error})


# Eliminar Departamento
class eliminarDepartamento(DeleteView):
    model = Departamento
    template_name = 'evaluacionCliente/listar_departamento.html'
    success_url = reverse_lazy('evaluacionCliente:listar_departamento')


#----------------------------------------------------------------------------------------------------------------------------------


#	CRUD COMITE

# Crear Comite
def crearComite(request):
	if request.method == 'POST':
		comite_form = ComiteForm(request.POST)
		if comite_form.is_valid():
			comite_form.save()
			return HttpResponseRedirect(reverse_lazy('evaluacionCliente:listar_comite'))  
	else:
		comite_form = ComiteForm()
	return render(request, 'evaluacionCliente/crear_comite.html', {'comite_form': comite_form})


# Vista para el Comite
def listarComite(request):
	comites = Comite.objects.all()
	#Mandar la consulta al template
	return render(request, 'evaluacionCliente/listar_comite.html', {'comites': comites})	


# Editar Comite
def editarComite(request, id_comite):
	comite_form = None
	error = None

	try:
		comite = Comite.objects.get(id_comite = id_comite)
		if request.method =='GET':
			comite_form=ComiteForm(instance = comite)
		else:
			comite_form = ComiteForm(request.POST, instance = comite)
			if comite_form.is_valid():
				comite_form.save()
			return HttpResponseRedirect(reverse_lazy('evaluacionCliente:listar_comite'))
	except ObjectDoesNotExist as e:
		error = e
	return render(request, 'evaluacionCliente/editar_comite.html', {'comite_form': comite_form, 'error':error})


# Eliminar Comite
class eliminarComite(DeleteView):
    model = Comite
    template_name = 'evaluacionCliente/listar_comite.html'
    success_url = reverse_lazy('evaluacionCliente:listar_comite')


#----------------------------------------------------------------------------------------------------------------------------------


#	CRUD AGENCIA

# Crear Agencia
def crearAgencia(request):
	if request.method == 'POST':
		agencia_form =AgenciaForm(request.POST)
		if agencia_form.is_valid():
			agencia_form.save()
			return HttpResponseRedirect(reverse_lazy('evaluacionCliente:listar_agencia'))  
	else:
		agencia_form = AgenciaForm()
	return render(request, 'evaluacionCliente/crear_agencia.html', {'agencia_form': agencia_form})


# Vista para la Agencia
def listarAgencia(request):
	agencias = Agencia.objects.all()
	#Mandar la consulta al template
	return render(request, 'evaluacionCliente/listar_agencia.html', {'agencias': agencias})


# Editar Agencia
def editarAgencia(request, codigo_agencia):
	agencia_form = None
	error = None

	try:
		agencia = Agencia.objects.get(codigo_agencia = codigo_agencia)
		if request.method =='GET':
			agencia_form=AgenciaForm(instance = agencia)
		else:
			agencia_form = AgenciaForm(request.POST, instance = agencia)
			if agencia_form.is_valid():
				agencia_form.save()
			return HttpResponseRedirect(reverse_lazy('evaluacionCliente:listar_agencia'))
	except ObjectDoesNotExist as e:
		error = e
	return render(request, 'evaluacionCliente/editar_agencia.html', {'agencia_form': agencia_form, 'error':error})


# Eliminar Agencia
class eliminarAgencia(DeleteView):
    model = Agencia
    template_name = 'evaluacionCliente/listar_agencia.html'
    success_url = reverse_lazy('evaluacionCliente:listar_agencia')


#----------------------------------------------------------------------------------------------------------------------------------


#	CRUD ACTIVIDADES

# Crear Actividad
def crearActividad(request):
	if request.method == 'POST':
		actividad_form = ActividadForm(request.POST)
		if actividad_form.is_valid():
			actividad_form.save()
			return HttpResponseRedirect(reverse_lazy('evaluacionCliente:listar_actividad'))  
	else:
		actividad_form = ActividadForm()
		# contexto {
		# 	agencias = Agencia.objects.order_by('codigo_agencia')
		# 	departamentos = Departamento.objects.order_by('codigo_departamento')
		# 	comites = Comite.objects.order_by('nombre_comite')
		# }

	return render(request, 'evaluacionCliente/crear_actividad.html', {'actividad_form': actividad_form})


# Vista para las Actividades
def listarActividad(request):
	actividades = Actividad.objects.all()
	#Mandar la consulta al template
	return render(request, 'evaluacionCliente/listar_actividad.html', {'actividades': actividades})


#Editar Actividades
def editarActividad(request, id_actividad):
	actividad_form = None
	error = None

	try:
		actividad = Actividad.objects.get(id_actividad = id_actividad)
		if request.method =='GET':
			actividad_form=ActividadForm(instance = actividad)
		else:
			actividad_form = ActividadForm(request.POST, instance = actividad)
			if actividad_form.is_valid():
				actividad_form.save()
			return HttpResponseRedirect(reverse_lazy('evaluacionCliente:listar_actividad'))
	except ObjectDoesNotExist as e:
		error = e
	return render(request, 'evaluacionCliente/editar_actividad.html', {'actividad_form': actividad_form, 'error':error})


#Eliminar Actividad
class eliminarActividad(DeleteView):
    model = Actividad
    template_name = 'evaluacionCliente/listar_actividad.html'
    success_url = reverse_lazy('evaluacionCliente:listar_actividad')


#----------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------
#								ESTA PARTE ES PARA LA ENCUESTA DEL CLIENTE
#----------------------------------------------------------------------------------------------------------------------------------


def crearEncuesta(request, codigoAgencia):
	if request.method == 'POST':
		titulo = request.POST['titulo']
		pregunta = request.POST['pregunta']
		visibilidad = request.POST['visibilidad']
		agencia = codigoAgencia

		encuestaCliente = EncuestaCliente(codigo_agencia_id=agencia, descripcion_pregunta=pregunta, titulo_encuesta_cliente=titulo, visibilidad_pregunta_cliente=visibilidad)
		
		encuestaCliente.save()

		return HttpResponseRedirect(reverse_lazy('evaluacionCliente:consultar_encuesta2', kwargs={'codigoAgencia':agencia, 'tituloEncuesta':titulo}))
	
	else:
		codigoAgencia = codigoAgencia
		agen = Agencia.objects.filter(codigo_agencia = codigoAgencia)

		context = {
			'agen' : agen,
			'codigoAgencia' : codigoAgencia,
		}

		return render(
			request,
			'evaluacionCliente/crear_encuesta_cliente.html', 
			context
		)


#----------------------------------------------------------------------------------------------------------------------------------


def editarEncuesta(request, idEncuesta):
	if request.method == 'POST':
		pregunta = request.POST['pregunta']
		visibilidad = request.POST['visibilidad']
		idEnc = idEncuesta
		enc = EncuestaCliente.objects.filter(id=idEnc)

		i=0
		while i < len(enc):
			agencia = enc[i].codigo_agencia
			titulo = enc[i].titulo_encuesta_cliente
			i+=1

		encuestaCliente = EncuestaCliente(id=idEnc, codigo_agencia_id=agencia, descripcion_pregunta=pregunta, titulo_encuesta_cliente=titulo, visibilidad_pregunta_cliente=visibilidad)
		
		encuestaCliente.save()

		return HttpResponseRedirect(reverse_lazy('evaluacionCliente:consultar_encuesta2', kwargs={'codigoAgencia':agencia, 'tituloEncuesta':titulo}))
	
	else:
		idEnc = idEncuesta
		enc = EncuestaCliente.objects.filter(id=idEnc)

		i=0
		while i < len(enc):
			agencia = enc[i].codigo_agencia
			titulo = enc[i].titulo_encuesta_cliente
			i+=1

		encuesta = EncuestaCliente.objects.filter(id=idEnc)

		context = {
			'idEnc': idEnc,
			'encuesta' : encuesta,
			'codigoAgencia': agencia,
			'tituloEncuesta': titulo,
		}

		return render(
			request,
			'evaluacionCliente/editar_encuesta_cliente.html', 
			context
		)


#----------------------------------------------------------------------------------------------------------------------------------


def eliminarEncuesta(request, idEncuesta):
	encuesta = EncuestaCliente.objects.filter(id=idEncuesta)

	i=0
	while i < len(encuesta):
		agencia = encuesta[i].codigo_agencia
		titulo = encuesta[i].titulo_encuesta_cliente
		i+=1

	EncuestaCliente.objects.get(id=idEncuesta).delete()

	encuestaVal = EncuestaCliente.objects.filter(titulo_encuesta_cliente = titulo, codigo_agencia=agencia)

	if len(encuestaVal) == 0:
		return HttpResponseRedirect(reverse_lazy('evaluacionCliente:listar_encuesta'))
	
	else:
		return HttpResponseRedirect(reverse_lazy('evaluacionCliente:consultar_encuesta2', kwargs={'codigoAgencia':agencia, 'tituloEncuesta':titulo}))


#----------------------------------------------------------------------------------------------------------------------------------


# LISTAR Agencias para buscar ENCUESTA
def listarEncuesta(request):
	agencias = Agencia.objects.all()

	context = {
		'agenciasCon': agencias,
	}

	return render(
		request,
		'evaluacionCliente/listar_encuesta.html',
		context
	)


#----------------------------------------------------------------------------------------------------------------------------------


# Mostrar la Encuesta de esa Agencia
def consultarAgencia(request):
	if request.method == 'POST':
		codigo_agencia = request.POST['codigo_agencia']
		
		encuestasAgencia = EncuestaCliente.objects.raw('select id, titulo_encuesta_cliente from proyecto_encuestacliente where codigo_agencia_id = %s group by titulo_encuesta_cliente;', [codigo_agencia])
		nombreAgencia = Agencia.objects.filter(codigo_agencia = codigo_agencia)

		i=0
		while i < len(nombreAgencia):
			codAgencia = nombreAgencia[i].codigo_agencia
			i+=1
		
		contexto = {
			'encuestasAgencia': encuestasAgencia,
			'nombreAgencia': nombreAgencia,
			'codAgencia': codAgencia,
			'codigo_agencia': codigo_agencia,
		}
			
		return render(
			request, 
			'evaluacionCliente/listar_encuesta.html', 
			contexto
			)



# Mostrar la Encuesta de esa Agencia
def consultarAgencia2(request, codigoAgencia):
	codigo_agencia = codigoAgencia
	
	encuestasAgencia = EncuestaCliente.objects.raw('select id, titulo_encuesta_cliente from proyecto_encuestacliente where codigo_agencia_id = %s group by titulo_encuesta_cliente;', [codigo_agencia])
	nombreAgencia = Agencia.objects.filter(codigo_agencia = codigo_agencia)

	i=0
	while i < len(nombreAgencia):
		codAgencia = nombreAgencia[i].codigo_agencia
		i+=1
	
	contexto = {
		'encuestasAgencia': encuestasAgencia,
		'nombreAgencia': nombreAgencia,
		'codAgencia': codAgencia,
		'codigo_agencia': codigo_agencia,
	}
		
	return render(
		request, 
		'evaluacionCliente/listar_encuesta.html', 
		contexto
		)


#----------------------------------------------------------------------------------------------------------------------------------


# Mostrar la Encuesta de esa Agencia
def consultarEncuesta(request, codigoAgencia):
	if request.method == 'POST':
		titulo_encuesta = request.POST['titulo_encuesta']
		codigo_agencia = codigoAgencia

		encuestasClientes = EncuestaCliente.objects.filter(codigo_agencia = codigo_agencia, titulo_encuesta_cliente = titulo_encuesta)
		
		encuestas = EncuestaCliente.objects.filter(codigo_agencia = codigo_agencia)
		agencias = Agencia.objects.all()

		i=0
		while i<1:
			tituloEncuesta = encuestasClientes[i].titulo_encuesta_cliente
			nombreAgencia = encuestasClientes[i].codigo_agencia.nombre_agencia
			i+=1

		contexto = {
			'encuestasClientes': encuestasClientes,
			'agencias': agencias,
			'encuestas': encuestas,
			'nombreAgencia' : nombreAgencia,
			'tituloEncuesta' : tituloEncuesta,
			'codigoAgencia' : codigo_agencia,
		}
			
		return render(
			request, 
			'evaluacionCliente/listar_encuesta.html', 
			contexto
			)



# Mostrar la Encuesta de esa Agencia (Parametros por URL al dar cancelar)
def consultarEncuesta2(request, codigoAgencia, tituloEncuesta):
	titulo_encuesta = tituloEncuesta
	codigo_agencia = codigoAgencia

	encuestasClientes = EncuestaCliente.objects.filter(codigo_agencia = codigo_agencia, titulo_encuesta_cliente = titulo_encuesta)
	
	encuestas = EncuestaCliente.objects.filter(codigo_agencia = codigo_agencia)
	agencias = Agencia.objects.all()

	i=0
	while i<1:
		tituloEncuesta = encuestasClientes[i].titulo_encuesta_cliente
		nombreAgencia = encuestasClientes[i].codigo_agencia.nombre_agencia
		i+=1

	contexto = {
		'encuestasClientes': encuestasClientes,
		'agencias': agencias,
		'encuestas': encuestas,
		'nombreAgencia' : nombreAgencia,
		'tituloEncuesta' : tituloEncuesta,
		'codigoAgencia' : codigo_agencia,
	}
		
	return render(
		request, 
		'evaluacionCliente/listar_encuesta.html', 
		contexto
		)


#----------------------------------------------------------------------------------------------------------------------------------


# Agregar Preguntas a la Encuesta
def AgregarPreguntasEncuestaCliente(request, codigoAgencia, tituloEncuesta):
	if request.method == 'POST':
		pregunta = request.POST['pregunta']
		visibilidad = request.POST['visibilidad']
		agencia = codigoAgencia
		titulo = tituloEncuesta

		encuestaCliente = EncuestaCliente(codigo_agencia_id=agencia, descripcion_pregunta=pregunta, titulo_encuesta_cliente=titulo, visibilidad_pregunta_cliente=visibilidad)
		
		encuestaCliente.save()

		return HttpResponseRedirect(reverse_lazy('evaluacionCliente:consultar_encuesta2', kwargs={'codigoAgencia':agencia, 'tituloEncuesta':titulo}))
	
	else:
		codigoAgencia = codigoAgencia
		tituloEncuesta = tituloEncuesta
		agen = Agencia.objects.filter(codigo_agencia = codigoAgencia)

		context = {
			'agen' : agen,
			'codigoAgencia' : codigoAgencia,
			'tituloEncuesta' : tituloEncuesta,
		}

		return render(
			request,
			'evaluacionCliente/agregar_preguntas_encuesta_cliente.html', 
			context
		)



#----------------------------------------------------------------------------------------------------------------------------------
#								ESTA PARTE ES PARA LA ENCUESTA DEL PERSONAL
#----------------------------------------------------------------------------------------------------------------------------------



def crearEncuestaPersonal(request, idActividad):
	if request.method == 'POST':
		titulo = request.POST['titulo']
		pregunta = request.POST['pregunta']
		visibilidad = request.POST['visibilidad']
		actividad = idActividad

		encuestaPersonal = EncuestaPersonal(id_actividad_id=actividad, descripcion_pregunta=pregunta, titulo_encuesta_personal=titulo, visibilidad_pregunta_personal=visibilidad)
		
		encuestaPersonal.save()

		return HttpResponseRedirect(reverse_lazy('evaluacionCliente:consultar_encuesta2_personal', kwargs={'idActividad':actividad, 'tituloEncuesta':titulo}))
	
	else:
		codigoActividad = idActividad
		act = Actividad.objects.filter(id_actividad = codigoActividad)

		context = {
			'act' : act,
			'codigoActividad' : codigoActividad,
		}

		return render(
			request,
			'evaluacionCliente/crear_encuesta_personal.html', 
			context
		)


#----------------------------------------------------------------------------------------------------------------------------------


def editarEncuestaPersonal(request, idEncuesta):
	if request.method == 'POST':
		pregunta = request.POST['pregunta']
		visibilidad = request.POST['visibilidad']
		idEnc = idEncuesta
		enc = EncuestaPersonal.objects.filter(id=idEnc)

		i=0
		while i < len(enc):
			actividad = enc[i].id_actividad.id_actividad
			titulo = enc[i].titulo_encuesta_personal
			i+=1
		
		encuestaPersonal = EncuestaPersonal(id=idEnc, id_actividad_id=actividad, descripcion_pregunta=pregunta, titulo_encuesta_personal=titulo, visibilidad_pregunta_personal=visibilidad)
		
		encuestaPersonal.save()

		return HttpResponseRedirect(reverse_lazy('evaluacionCliente:consultar_encuesta2_personal', kwargs={'idActividad':actividad, 'tituloEncuesta':titulo}))
	
	else:
		idEnc = idEncuesta
		enc = EncuestaPersonal.objects.filter(id=idEnc)

		i=0
		while i < len(enc):
			actividad = enc[i].id_actividad.id_actividad
			titulo = enc[i].titulo_encuesta_personal
			i+=1

		encuesta = EncuestaPersonal.objects.filter(id=idEnc)

		context = {
			'idEnc': idEnc,
			'encuesta' : encuesta,
			'codigoActividad': actividad,
			'tituloEncuesta': titulo,
		}

		return render(
			request,
			'evaluacionCliente/editar_encuesta_personal.html', 
			context
		)


#----------------------------------------------------------------------------------------------------------------------------------


def eliminarEncuestaPersonal(request, idEncuesta):
	encuesta = EncuestaPersonal.objects.filter(id=idEncuesta)

	i=0
	while i < len(encuesta):
		actividad = encuesta[i].id_actividad.id_actividad
		titulo = encuesta[i].titulo_encuesta_personal
		i+=1
	
	EncuestaPersonal.objects.get(id=idEncuesta).delete()

	encuestaVal = EncuestaPersonal.objects.filter(id_actividad=actividad, titulo_encuesta_personal=titulo)

	if len(encuestaVal) == 0:
		return HttpResponseRedirect(reverse_lazy('evaluacionCliente:listar_encuesta_personal'))
	
	else:
		return HttpResponseRedirect(reverse_lazy('evaluacionCliente:consultar_encuesta2_personal', kwargs={'idActividad':actividad, 'tituloEncuesta':titulo}))


#----------------------------------------------------------------------------------------------------------------------------------


# LISTAR Agencias para buscar ENCUESTA
def listarEncuestaPersonal(request):
	actividades = Actividad.objects.all().order_by('codigo_agencia')

	context = {
		'actividadesCon': actividades,
	}

	return render(
		request,
		'evaluacionCliente/listar_encuesta_personal.html',
		context
	)


#----------------------------------------------------------------------------------------------------------------------------------


# Mostrar la Encuesta de esa Agencia
def consultarActividadPersonal(request):
	if request.method == 'POST':
		codigo_actividad = request.POST['codigo_actividad']
		
		encuestasActividad = EncuestaPersonal.objects.raw('select id, titulo_encuesta_personal from proyecto_encuestapersonal where id_actividad_id = %s group by titulo_encuesta_personal;', [codigo_actividad])
		nombreActividad = Actividad.objects.filter(id_actividad = codigo_actividad)
		
		i=0
		while i < len(nombreActividad):
			codActividad = nombreActividad[i].id_actividad
			i+=1
		
		contexto = {
			'encuestasActividad': encuestasActividad,
			'nombreActividad': nombreActividad,
			'codActividad': codActividad,
			'codigo_actividad': codigo_actividad,
		}
			
		return render(
			request, 
			'evaluacionCliente/listar_encuesta_personal.html', 
			contexto
			)



# Mostrar la Encuesta de esa Agencia
def consultarActividad2Personal(request, idActividad):
	codigo_actividad = idActividad
	
	encuestasActividad = EncuestaPersonal.objects.raw('select id, titulo_encuesta_personal from proyecto_encuestapersonal where id_actividad_id = %s group by titulo_encuesta_personal;', [codigo_actividad])
	nombreActividad = Actividad.objects.filter(id_actividad = codigo_actividad)

	i=0
	while i < len(nombreActividad):
		codActividad = nombreActividad[i].id_actividad
		i+=1
	
	contexto = {
		'encuestasActividad': encuestasActividad,
		'nombreActividad': nombreActividad,
		'codActividad': codActividad,
		'codigo_actividad': codigo_actividad
	}
		
	return render(
		request, 
		'evaluacionCliente/listar_encuesta_personal.html', 
		contexto
		)


#----------------------------------------------------------------------------------------------------------------------------------


# Mostrar la Encuesta de esa Agencia
def consultarEncuestaPersonal(request, idActividad):
	if request.method == 'POST':
		titulo_encuesta = request.POST['titulo_encuesta']
		codigo_actividad = idActividad

		encuestasPersonal = EncuestaPersonal.objects.filter(id_actividad = codigo_actividad, titulo_encuesta_personal = titulo_encuesta)
		
		encuestas = EncuestaPersonal.objects.filter(id_actividad = codigo_actividad)
		actividades = Actividad.objects.all()

		i=0
		while i<1:
			tituloEncuesta = encuestasPersonal[i].titulo_encuesta_personal
			nombreAgencia = encuestasPersonal[i].id_actividad.codigo_agencia.nombre_agencia
			nombreActividad = encuestasPersonal[i].id_actividad.nombre_actividad
			i+=1

		contexto = {
			'encuestasPersonal': encuestasPersonal,
			'actividades': actividades,
			'encuestas': encuestas,
			'nombreAgencia' : nombreAgencia,
			'nombreActividad' : nombreActividad,
			'tituloEncuesta' : tituloEncuesta,
			'codigoActividad' : codigo_actividad,
		}
			
		return render(
			request, 
			'evaluacionCliente/listar_encuesta_personal.html', 
			contexto
			)



# Mostrar la Encuesta de esa Agencia (Parametros por URL al dar cancelar)
def consultarEncuesta2Personal(request, idActividad, tituloEncuesta):
	titulo_encuesta = tituloEncuesta
	codigo_actividad = idActividad

	encuestasPersonal = EncuestaPersonal.objects.filter(id_actividad = codigo_actividad, titulo_encuesta_personal = titulo_encuesta)
	
	encuestas = EncuestaPersonal.objects.filter(id_actividad = codigo_actividad)
	actividades = Actividad.objects.all()

	i=0
	while i<1:
		tituloEncuesta = encuestasPersonal[i].titulo_encuesta_personal
		nombreAgencia = encuestasPersonal[i].id_actividad.codigo_agencia.nombre_agencia
		nombreActividad = encuestasPersonal[i].id_actividad.nombre_actividad
		i+=1

	contexto = {
		'encuestasPersonal': encuestasPersonal,
		'actividades': actividades,
		'encuestas': encuestas,
		'nombreAgencia' : nombreAgencia,
		'nombreActividad' : nombreActividad,
		'tituloEncuesta' : tituloEncuesta,
		'codigoActividad' : codigo_actividad,
	}
		
	return render(
		request, 
		'evaluacionCliente/listar_encuesta_personal.html', 
		contexto
		)


#----------------------------------------------------------------------------------------------------------------------------------


# Agregar Preguntas a la Encuesta
def AgregarPreguntasEncuestaPersonal(request, idActividad, tituloEncuesta):
	if request.method == 'POST':
		pregunta = request.POST['pregunta']
		visibilidad = request.POST['visibilidad']
		actividad = idActividad
		titulo = tituloEncuesta

		encuestaPersonal = EncuestaPersonal(id_actividad_id=actividad, descripcion_pregunta=pregunta, titulo_encuesta_personal=titulo, visibilidad_pregunta_personal=visibilidad)
		
		encuestaPersonal.save()

		return HttpResponseRedirect(reverse_lazy('evaluacionCliente:consultar_encuesta2_personal', kwargs={'idActividad':actividad, 'tituloEncuesta':titulo}))
	
	else:
		codigoActividad = idActividad
		tituloEncuesta = tituloEncuesta
		act = Actividad.objects.filter(id_actividad = codigoActividad)

		context = {
			'act' : act,
			'codigoActividad' : codigoActividad,
			'tituloEncuesta' : tituloEncuesta,
		}

		return render(
			request,
			'evaluacionCliente/agregar_preguntas_encuesta_personal.html', 
			context
		)