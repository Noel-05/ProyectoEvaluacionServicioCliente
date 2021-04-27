from django import forms
from .models import *

class DepartamentoForm(forms.ModelForm):
	class Meta:
		model = Departamento
		fields = {'codigo_departamento', 'nombre_departamento'}

	codigo_departamento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	nombre_departamento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))   

	def __init__(self, *args, **kwargs):
		super(DepartamentoForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			self.fields['codigo_departamento'].widget.attrs['readonly'] = True

	def clean_codigo_departamento(self):
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			return instance.codigo_departamento
		else:
			return self.cleaned_data['codigo_departamento']

class ComiteForm(forms.ModelForm):
	class Meta:
		model = Comite
		fields = {'nombre_comite', 'descripcion_comite'}

	nombre_comite = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	descripcion_comite = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})) 


class AgenciaForm(forms.ModelForm):
	class Meta:
		model = Agencia
		fields = {'codigo_agencia', 'nombre_agencia', 'direccion_agencia'}

	codigo_agencia = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	nombre_agencia = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))   
	direccion_agencia = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))   

	def __init__(self, *args, **kwargs):
		super(AgenciaForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			self.fields['codigo_agencia'].widget.attrs['readonly'] = True

	def clean_codigo_agencia(self):
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			return instance.codigo_agencia
		else:
			return self.cleaned_data['codigo_agencia']  

class ActividadForm(forms.ModelForm):
	class Meta:
		model = Actividad
		fields = {'nombre_actividad', 'descripcion_actividad', 'fecha_realizacion', 'codigo_agencia', 'codigo_departamento', 'id_comite'}

	nombre_actividad = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	descripcion_actividad = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))   
	fecha_realizacion = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Fecha de Inicio', 'autocomplete': 'off', 'type':'date', 'min':'1940-01-01', 'class': 'form-control'})) 
