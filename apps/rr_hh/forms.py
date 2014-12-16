#! /usr/bin/python
# -*- coding: UTF-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Empleado,ServicioEmpleado,Programacion
from django.contrib.auth.models import User
from django.forms import ModelMultipleChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple
from apps.logistica.models import Cargo,Area,Servicio

class UserForm(UserCreationForm):
	id = forms.IntegerField(required=False,widget = forms.HiddenInput(
		attrs={ 'id': 'codigo'}))
	emp_nom = forms.CharField(widget= forms.TextInput(
		attrs={ 'id': 'nombres','type': 'text', 'name': 'fname','placeholder': 'Nombres'}))
	emp_ape = forms.CharField(widget= forms.TextInput(
		attrs={'id': 'apellidos','type': 'text','name':'lname','placeholder': 'Apellidos'}))	
	emp_direccion = forms.CharField(widget= forms.TextInput(
		attrs={'id': 'direccion','type': 'text', 'name': 'address' ,'placeholder': 'Direccion'}))
	emp_sexo = forms.ChoiceField(required=False, choices=(('F', 'Femenino'),('M', 'Masculino')),
		widget= forms.Select(attrs={'class' : 'input-sm' ,'id': 'sex'}))
	DNI = forms.CharField(max_length=8,min_length=8,widget= forms.TextInput(
		attrs={'id': 'dni','type': 'number','name':'code'}))	
	emp_tel = forms.CharField(widget= forms.TextInput(
		attrs={'id': 'tel','type':'tel','name':'phone','placeholder': 'Telefono'}))
	email = forms.CharField(widget= forms.TextInput(
		attrs={'id': 'email','type':'email','name':'email','placeholder': 'E-mail'}))
	emp_fecnac= forms.DateField(widget=forms.DateInput( 
		attrs={ 'id': 'fecnac','type': 'text','name':'startdate','placeholder': 'Fecha de Nacimiento'}))
	emp_fecing= forms.DateField(widget=forms.DateInput( 
		attrs={'id': 'fecIng','type': 'text','name':'finishdate','placeholder': 'Fecha de Ingreso'}))
	avatar = forms.CharField(required=False,widget= forms.TextInput(
		attrs={'id': 'avatar','type':'file'}))
	username = forms.CharField(max_length=30,min_length=5,widget= forms.TextInput(
		attrs={ 'id': 'username','type': 'text', 'name': 'username','placeholder': 'Username'}))
	password1= forms.CharField(max_length=30,min_length=6,widget= forms.TextInput(
		attrs={ 'id': 'password1','type': 'password', 'name': 'password1','placeholder': 'Password'}))
	password2= forms.CharField(max_length=30,min_length=6,widget= forms.TextInput(
		attrs={ 'id': 'password2','type': 'password', 'name': 'password2','placeholder': 'Confirm password'}))
	cargo = forms.ModelChoiceField(queryset=Cargo.objects.all())


class UserFormModi(forms.ModelForm):
	id = forms.IntegerField(required=False,widget = forms.HiddenInput(
		attrs={ 'id': 'codigo'}))	
	emp_nom = forms.CharField(widget= forms.TextInput(
		attrs={ 'id': 'nombres','type': 'text', 'name': 'fname','placeholder': 'Nombres'}))
	emp_ape = forms.CharField(widget= forms.TextInput(
		attrs={'id': 'apellidos','type': 'text','name':'lname','placeholder': 'Apellidos'}))	
	emp_direccion = forms.CharField(widget= forms.TextInput(
		attrs={'id': 'direccion','type': 'text', 'name': 'address' ,'placeholder': 'Direccion'}))
	emp_sexo = forms.ChoiceField(required=False, choices=(('F', 'Femenino'),('M', 'Masculino')),
		widget= forms.Select(attrs={'class' : 'input-sm' ,'id': 'sex'}))
	DNI = forms.CharField(max_length=8,min_length=8,widget= forms.TextInput(
		attrs={'id': 'dni','type': 'number','name':'code'}))	
	emp_tel = forms.CharField(widget= forms.TextInput(
		attrs={'id': 'tel','type':'tel','name':'phone','placeholder': 'Telefono'}))
	email = forms.CharField(widget= forms.TextInput(
		attrs={'id': 'email','type':'email','name':'email','placeholder': 'E-mail'}))
	emp_fecnac= forms.DateField(widget=forms.DateInput( 
		attrs={ 'id': 'fecnac','type': 'text','name':'startdate','placeholder': 'Fecha de Nacimiento'}))
	emp_fecing= forms.DateField(widget=forms.DateInput( 
		attrs={'id': 'fecIng','type': 'text','name':'finishdate','placeholder': 'Fecha de Ingreso'}))
	avatar = forms.CharField(required=False,widget= forms.TextInput(
		attrs={'class' : 'input-sm','id': 'avatar','type':'text','placeholder': 'Foto','readonly': ''}))	
	cargo = forms.ModelChoiceField(queryset=Cargo.objects.all())
	class Meta:
		model = Empleado
		exclude = ['user']


class UserFormPass(forms.ModelForm):
	id = forms.IntegerField(required=False,widget = forms.HiddenInput(
		attrs={ 'id': 'codigo'}))	
	emp_nom = forms.CharField(widget= forms.TextInput(
		attrs={ 'id': 'nombres','type': 'text', 'name': 'fname','placeholder': 'Nombres','readonly':'readonly'}))
	emp_ape = forms.CharField(widget= forms.TextInput(
		attrs={'id': 'apellidos','type': 'text','name':'lname','placeholder': 'Apellidos','readonly':'readonly'}))
	username = forms.CharField(max_length=30,min_length=5,widget= forms.TextInput(
		attrs={ 'id': 'username','type': 'text', 'name': 'username','placeholder': 'Username','readonly':'readonly'}))
	password= forms.CharField(max_length=30,min_length=6,widget= forms.PasswordInput(
		attrs={ 'id': 'password','type': 'password', 'name': 'password1','placeholder': 'Password Actual '}))
	password1= forms.CharField(max_length=30,min_length=6,widget= forms.PasswordInput(
		attrs={ 'id': 'password1','type': 'password', 'name': 'password1','placeholder': 'Nuevo Password'}))
	password2= forms.CharField(max_length=30,min_length=6,widget= forms.PasswordInput(
		attrs={ 'id': 'password2','type': 'password', 'name': 'password2','placeholder': 'Confirma Nuevo Password'}))	
	class Meta:
		model = User
		exclude = ['date_joined','last_login']


class RegistrarCargaForm(forms.ModelForm):
	id = forms.IntegerField(widget = forms.HiddenInput(
		attrs={ 'id': 'codigo'}))
	empleado=forms.IntegerField(widget = forms.HiddenInput(
		attrs={ 'id': 'codigoemp'}))
	servicio=ModelMultipleChoiceField(queryset=Servicio.objects.all(), required=False,
		widget=forms.SelectMultiple(attrs={'class' : 'form-control custom-scroll' ,'id': 'multiselect1'}))
	servi=forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class' : 'form-control custom-scroll' ,'id': 'multiselect2'}))

	class Meta: 
		model = ServicioEmpleado


class RegistrarProgramacionForm(forms.ModelForm):
	id = forms.IntegerField(required=False,widget = forms.HiddenInput(
		attrs={ 'id': 'codigo'}))	
	serviempledos =forms.ModelMultipleChoiceField(queryset=ServicioEmpleado.objects.all(),widget=forms.SelectMultiple(
		attrs={'class' : 'select2' ,'id': 'multiselect1','multiple style':'width:100%'}))	
	turno = forms.ChoiceField(required=False, choices=(('M', 'Turno Mañana'),('T', 'Turno Tarde')),
		widget= forms.Select(attrs={'class' : 'select2' ,'id': 'turno','style':'width:100%'}))
	hor_ing= forms.TimeField(input_formats=['%H:%M','%I:%M %p'],widget=forms.TimeInput(format=["%H:%M","%I:%M %p"],
		attrs={'class' : 'form-control','type':'text' ,'id': 'timepicker','placeholder': 'Seleccione una Hora de Ingreso'}))
	hor_sal= forms.TimeField(input_formats=['%H:%M','%I:%M %p'],widget=forms.TimeInput(format=["%H:%M","%I:%M %p"],
		attrs={'class' : 'form-control','type':'text' ,'id': 'timepicker2','placeholder': 'Seleccione una Hora de Salida'}))
	
	hor_fecha= forms.DateField(widget=forms.DateInput( 
		attrs={ 'id': 'to','type': 'text','placeholder': 'Desde','class':"form-control"}))
	fec_fin= forms.DateField(required=False,widget=forms.DateInput( 
		attrs={ 'id': 'from','type': 'text','placeholder': 'Hasta','class':"form-control"}))
	class Meta:
		model = Programacion
		exclude = ['cantidadPacientes','serviempledo']



