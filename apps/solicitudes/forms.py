#! /usr/bin/python
# -*- coding: UTF-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Solicitud,Paciente
from django.contrib.auth.models import User
from django.forms import ModelMultipleChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple
from apps.logistica.models import Cargo,Area,Servicio


class RegistrarPacienteForm(forms.ModelForm):
	id = forms.IntegerField(required=False,widget = forms.HiddenInput(
		attrs={ 'id': 'codigo'}))
	pac_nombre = forms.CharField(widget= forms.TextInput(
		attrs={ 'class' : 'input-sm', 'id': 'nombres'}))
	pac_apellido = forms.CharField(widget= forms.TextInput(
		attrs={'class' : 'input-sm' , 'id': 'apellidos'}))
	DNI = forms.CharField(max_length=8,min_length=8,widget= forms.TextInput(
		attrs={'class' : 'input-xs' , 'id': 'dni'}))
	pac_direccion = forms.CharField(widget= forms.TextInput(
		attrs={'class' : 'input-xs' , 'id': 'direccion'}))
	pac_fecnac= forms.DateField(widget=forms.DateInput( 
		attrs={'id': 'fecnac'}))
	pac_telefono = forms.CharField(widget= forms.TextInput(
		attrs={'class' : 'input-xs'  , 'id': 'tel'}))	
	pac_sexo = forms.ChoiceField(required=False, choices=(('F', 'Femenino'),('M', 'Masculino')),
		widget= forms.Select(attrs={'class' : 'input-sm' ,'id': 'sex'}))
	pac_obs = forms.CharField(required=False,widget= forms.Textarea(
		attrs={'class' : 'custom-scroll' , 'id': 'observacion'}))	
	class Meta:
		model = Paciente
		

class RegistrarSolicitud(forms.ModelForm):
	id = forms.IntegerField(required=False,widget = forms.HiddenInput(
		attrs={ 'id': 'codigo'}))
	paciente=forms.IntegerField(widget = forms.HiddenInput(
		attrs={ 'id': 'idpaciente'}))
	fecha= forms.DateField(required=False,widget=forms.DateInput( 
		attrs={ 'id': 'fecha','type': 'text','name':'startdate','placeholder': 'Fecha de Cita Medica'}))
	turno = forms.ChoiceField(required=False, choices=(('M', 'Turno Mañana'),('T', 'Turno Tarde')),
		widget= forms.Select(attrs={'class' : 'select2' ,'id': 'turno','style':'width:100%'}))	
	
	area=forms.ModelChoiceField(required=False,queryset=Area.objects.all(),
		widget= forms.Select(attrs={'class' : 'select2' ,'id': 'select-1','style':'width:100%'}))		
	#servi=forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class' : 'form-control custom-scroll' ,'id': 'multiselect2'}))

	class Meta: 
		model = Solicitud
		exclude = ['paciente','usuario','soli_abono']




