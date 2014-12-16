from django.shortcuts import render,redirect
from .models import Area,Cargo,Servicio,Modelo
from .forms import RegistrarAreaForm,RegistrarCargoForm,RegistrarServicioForm,RegistrarModeloForm
from django.shortcuts import render_to_response
from django.core import serializers
from django.http import HttpResponse, Http404
import json


def BuscarArea(request):		
	if request.is_ajax():			
		texto= request.GET['texto']
		seleccion = request.GET['seleccion']
		if seleccion=="0":
			area = Area.objects.filter(area_nom__icontains=texto)
			data = serializers.serialize('json',area,
			fields={'area_nom','area_descripcion'})
			return HttpResponse(data, content_type='application/json')	
		elif seleccion=="1":
			area = Area.objects.filter(id=texto)
			data = serializers.serialize('json',area,
			fields={'area_nom','area_descripcion'})
			return HttpResponse(data, content_type='application/json')		
	else :
		print "mal"
		raise Http404


def CreateArea(request):	
	if request.method == 'POST':
		form = RegistrarAreaForm(request.POST)
		response_data = {} 
		if form.is_valid():
			area= Area()
			area.area_nom = form.cleaned_data.get('area_nom')			
			area.area_descripcion = form.cleaned_data.get('area_descripcion')			
			area.save()		
			response_data['result'] = "La Nueva Area fue Registrada con Exito"
			#response_data['postpk'] = paciente.pk	        print "XXSS"
			#paciente.pac_fecnac = form.cleaned_data.get('DNI')	        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")	


def ModiArea(request):	
	if request.method == 'POST':		
		form = RegistrarAreaForm(request.POST)
		response_data = {} 
		if form.is_valid():
			area= Area.objects.get(id=form.cleaned_data.get('id'))
			area.area_nom = form.cleaned_data.get('area_nom')			
			area.area_descripcion = form.cleaned_data.get('area_descripcion')			
			area.save()	
			response_data['result'] = "Los datos del Area fueron Actualizados con Exito"				        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")


def BuscarServicio(request):		
	if request.is_ajax():			
		texto= request.GET['texto']
		seleccion = request.GET['seleccion']
		if seleccion=="0":
			consulta = Servicio.objects.select_related().filter(servi_nom__icontains=texto)
			lista=[]
			for servicio in consulta:
				d={'pk':servicio.id,'servicio': servicio.servi_nom,'descripcion': servicio.servi_descripcion
				,'costo': float(servicio.servi_costo),'tiempo':servicio.tiempo_requerido,'fk':servicio.area.id,'Area':servicio.area.area_nom}
				lista.append(d)
			#busqueda= Servicio.objects.select_related().filter(area__area_nom__contains="")		
			return HttpResponse(json.dumps(lista), content_type='application/json')	
		elif seleccion=="1":
			consulta = Servicio.objects.select_related().filter(area__area_nom__icontains=texto)
			lista=[]
			for servicio in consulta:
				d={'pk':servicio.id,'servicio': servicio.servi_nom,'descripcion': servicio.servi_descripcion
				,'costo': float(servicio.servi_costo),'tiempo':servicio.tiempo_requerido,'fk':servicio.area.id,'Area':servicio.area.area_nom}
				lista.append(d)
			return HttpResponse(json.dumps(lista), content_type='application/json')
		elif seleccion=="2":
			consulta = Servicio.objects.select_related().filter(id=texto)
			lista=[]
			for servicio in consulta:
				d={'pk':servicio.id,'servicio': servicio.servi_nom,'descripcion': servicio.servi_descripcion
				,'costo': float(servicio.servi_costo),'tiempo':servicio.tiempo_requerido,'fk':servicio.area.id,
				'Area':servicio.area.area_nom,'id_area':servicio.area.id}
				lista.append(d)
			return HttpResponse(json.dumps(lista), content_type='application/json')		
		elif seleccion=="5":
			servicio = Servicio.objects.filter(area_id=texto)
			data = serializers.serialize('json',servicio,fields={'servi_nom',})
			return HttpResponse(data, content_type='application/json')	
	else :
		print "mal"
		raise Http404


def CreateServicio(request):	
	if request.method == 'POST':
		form = RegistrarServicioForm(request.POST)
		response_data = {} 
		if form.is_valid():
			servicio= Servicio()
			servicio.servi_nom = form.cleaned_data.get('servi_nom')
			servicio.servi_descripcion = form.cleaned_data.get('servi_descripcion')	
			servicio.servi_costo = form.cleaned_data.get('servi_costo')
			servicio.tiempo_requerido = form.cleaned_data.get('tiempo_requerido')
			servicio.area = form.cleaned_data.get('area')
			servicio.save()
			response_data['result'] = "El nuevo Servicio fue Registrado con Exito"
			#response_data['postpk'] = paciente.pk	        print "XXSS"
			#paciente.pac_fecnac = form.cleaned_data.get('DNI')	        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")	


def ModiServicio(request):	
	if request.method == 'POST':		
		form = RegistrarServicioForm(request.POST)
		response_data = {} 
		if form.is_valid():
			servicio= Servicio.objects.get(id=form.cleaned_data.get('id'))
			servicio.servi_nom = form.cleaned_data.get('servi_nom')
			servicio.servi_descripcion = form.cleaned_data.get('servi_descripcion')	
			servicio.servi_costo = form.cleaned_data.get('servi_costo')
			servicio.tiempo_requerido = form.cleaned_data.get('tiempo_requerido')
			servicio.area = form.cleaned_data.get('area')
			servicio.save()	
			response_data['result'] = "Los datos del Servicio fueron Actualizados con Exito"				        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")



def BuscarCargo(request):		
	if request.is_ajax():			
		texto= request.GET['texto']
		seleccion = request.GET['seleccion']
		if seleccion=="0":
			cargo = Cargo.objects.filter(cargo_nom__icontains=texto)
			data = serializers.serialize('json',cargo,
			fields={'cargo_nom','cargo_descripcion'})
			return HttpResponse(data, content_type='application/json')	
		elif seleccion=="1":
			cargo = Cargo.objects.filter(id=texto)
			data = serializers.serialize('json',cargo,
			fields={'cargo_nom','cargo_descripcion'})
			return HttpResponse(data, content_type='application/json')		
	else :
		print "mal"
		raise Http404


def CreateCargo(request):	
	if request.method == 'POST':
		form = RegistrarCargoForm(request.POST)
		response_data = {} 
		if form.is_valid():
			cargo= Cargo()
			cargo.cargo_nom = form.cleaned_data.get('cargo_nom')			
			cargo.cargo_descripcion = form.cleaned_data.get('cargo_descripcion')			
			cargo.save()		
			response_data['result'] = "El Nuevo Cargo fue Registrado con Exito"
			#response_data['postpk'] = paciente.pk	        print "XXSS"
			#paciente.pac_fecnac = form.cleaned_data.get('DNI')	        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")	


def ModiCargo(request):	
	if request.method == 'POST':		
		form = RegistrarCargoForm(request.POST)
		response_data = {} 
		if form.is_valid():
			cargo= Cargo.objects.get(id=form.cleaned_data.get('id'))
			cargo.cargo_nom = form.cleaned_data.get('cargo_nom')			
			cargo.cargo_descripcion = form.cleaned_data.get('cargo_descripcion')			
			cargo.save()	
			response_data['result'] = "Los datos del Cargo fueron Actualizados con Exito"				        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")

# Create your views here.



def HomeArea(req):
	tmpl_vars = {
		'form': RegistrarAreaForm()
	}
	return render(req, 'logistica/logisticaA.html', tmpl_vars)


def HomeCargo(req):
	tmpl_vars = {
		'form': RegistrarCargoForm()
	}
	return render(req, 'logistica/logisticaCargo.html', tmpl_vars)


def HomeServicio(req):
	tmpl_vars = {
		'form': RegistrarServicioForm()
	}
	return render(req, 'logistica/logisticaServicio.html', tmpl_vars)


def HomeModelo(req):
	tmpl_vars = {
		'form': RegistrarModeloForm()
	}
	return render(req, 'logistica/Modelo.html', tmpl_vars)




def BuscarModelo(request):		
	if request.is_ajax():			
		texto= request.GET['texto']
		seleccion = request.GET['seleccion']
		if seleccion=="0":
			modelo = Modelo.objects.filter(Nombre__icontains=texto)
			data = serializers.serialize('json',modelo)
			return HttpResponse(data, content_type='application/json')	
		elif seleccion=="1":
			modelo = Modelo.objects.filter(Marca__icontains=texto)
			data = serializers.serialize('json',modelo)
			return HttpResponse(data, content_type='application/json')
		elif seleccion=="2":
			modelo = Modelo.objects.filter(Modelo__icontains=texto)
			data = serializers.serialize('json',modelo)
			return HttpResponse(data, content_type='application/json')		
	else :
		print "mal"
		raise Http404


def CreateModelo(request):	
	if request.method == 'POST':
		form = RegistrarModeloForm(request.POST)
		response_data = {} 
		if form.is_valid():
			modelo= Modelo()
			modelo.Nombre = form.cleaned_data.get('Nombre')	
			modelo.Marca = form.cleaned_data.get('Marca')			
			modelo.Modelo = form.cleaned_data.get('Modelo')					
			modelo.Serie = form.cleaned_data.get('Serie')			
			modelo.descripcion = form.cleaned_data.get('descripcion')			
			modelo.save()		
			response_data['result'] = "El equipo fue Registrado con Exito"
			#response_data['postpk'] = paciente.pk	        print "XXSS"
			#paciente.pac_fecnac = form.cleaned_data.get('DNI')	        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")	


def ModiModelo(request):	
	if request.method == 'POST':
		instance = Modelo.objects.get(id=request.POST['id'])
		form = RegistrarModeloForm(request.POST or None, instance=instance)
		response_data = {} 
		if form.is_valid():			
			modelo= Modelo.objects.get(id=form.cleaned_data.get('id'))
			modelo.Nombre = form.cleaned_data.get('Nombre')	
			modelo.Marca = form.cleaned_data.get('Marca')			
			modelo.Modelo = form.cleaned_data.get('Modelo')					
			modelo.Serie = form.cleaned_data.get('Serie')			
			modelo.descripcion = form.cleaned_data.get('descripcion')			
			modelo.save()	
			response_data['result'] = "Los datos del Equipo fueron Actualizados con Exito"				        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")


