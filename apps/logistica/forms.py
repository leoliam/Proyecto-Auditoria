from django import forms
from .models import Area,Cargo,Servicio,Modelo


class RegistrarAreaForm(forms.ModelForm):
	id = forms.IntegerField(required=False,widget = forms.HiddenInput(
		attrs={ 'id': 'codigo'}))
	area_nom = forms.CharField(widget= forms.TextInput(
		attrs={ 'class' : 'input-sm', 'id': 'nombres'}))	
	area_descripcion = forms.CharField(required=False,widget= forms.Textarea(
		attrs={'class' : 'custom-scroll' , 'id': 'observacion'}))	
	class Meta:
		model = Area


class RegistrarCargoForm(forms.ModelForm):
	id = forms.IntegerField(required=False,widget = forms.HiddenInput(
		attrs={ 'id': 'codigo'}))
	cargo_nom = forms.CharField(widget= forms.TextInput(
		attrs={ 'class' : 'input-sm', 'id': 'nombres'}))	
	cargo_descripcion = forms.CharField(required=False,widget= forms.Textarea(
		attrs={'class' : 'custom-scroll' , 'id': 'observacion'}))	
	class Meta:
		model = Cargo


class RegistrarServicioForm(forms.ModelForm):
	id = forms.IntegerField(required=False,widget = forms.HiddenInput(
		attrs={ 'id': 'codigo'}))	
	servi_nom = forms.CharField(widget= forms.TextInput(
		attrs={ 'class' : 'input-sm', 'id': 'nombres'}))	
	servi_descripcion = forms.CharField(required=False,widget= forms.Textarea(
		attrs={'class' : 'custom-scroll' , 'id': 'observacion'}))
	servi_costo = forms.CharField(widget= forms.TextInput(
		attrs={'class' : 'input-xs' , 'id': 'costo','type': 'number'}))
	tiempo_requerido = forms.CharField(widget= forms.TextInput(
		attrs={'class' : 'input-xs' , 'id': 'TR','type': 'number'}))
	class Meta:
		model = Servicio


class RegistrarModeloForm(forms.ModelForm):
	id = forms.IntegerField(required=False,widget = forms.HiddenInput(
		attrs={ 'id': 'codigo'}))
	Nombre = forms.CharField(widget= forms.TextInput(
		attrs={ 'class' : 'input-sm', 'id': 'nombres'}))	
	Marca = forms.CharField(widget= forms.TextInput(
		attrs={ 'class' : 'input-sm', 'id': 'Marca'}))
	Modelo = forms.CharField(widget= forms.TextInput(
		attrs={ 'class' : 'input-sm', 'id': 'Modelo'}))	
	Serie = forms.CharField(widget= forms.TextInput(
		attrs={ 'class' : 'input-sm', 'id': 'Serie'}))	
	descripcion = forms.CharField(required=False,widget= forms.Textarea(
		attrs={'class' : 'custom-scroll' , 'id': 'observacion'}))	
	class Meta:
		model = Modelo
		
