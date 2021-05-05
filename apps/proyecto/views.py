from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.core import serializers
from django.http import HttpResponseRedirect
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