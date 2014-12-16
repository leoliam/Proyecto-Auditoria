#! /usr/bin/python
# -*- coding: UTF-8 -*-
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Empleado,ServicioEmpleado,Programacion
from apps.logistica.models import Cargo,Area,Servicio
from .forms import UserForm,UserFormModi,UserFormPass,RegistrarCargaForm,RegistrarProgramacionForm
from datetime import datetime
from django.shortcuts import render_to_response
from django.core import serializers
from django.http import HttpResponse, Http404
from datetime import datetime


import json
import datetime as dt

def CreatePersonal(request):	
	if request.method == 'POST':
		form = UserForm(request.POST)		
		response_data = {} 
		if form.is_valid() :			
			user= form.save()
			empleado=Empleado()	
			empleado.emp_nom = form.cleaned_data.get('emp_nom')	
			empleado.emp_ape = form.cleaned_data.get('emp_ape')
			empleado.emp_fecnac = form.cleaned_data.get('emp_fecnac')
			empleado.emp_direccion = form.cleaned_data.get('emp_direccion')
			empleado.emp_sexo = form.cleaned_data.get('emp_sexo')
			empleado.DNI = form.cleaned_data.get('DNI')
			empleado.email= form.cleaned_data.get('email')
			empleado.emp_tel = form.cleaned_data.get('emp_tel')
			empleado.emp_fecing = form.cleaned_data.get('emp_fecing')	
			empleado.cargo = form.cleaned_data.get('cargo')		
			empleado.user= user					
			empleado.save()			
			response_data['result'] = "El nuevo Personal fue Registrado con Exito"
			#response_data['postpk'] = paciente.pk	        print "XXSS"
			#paciente.pac_fecnac = form.cleaned_data.get('DNI')	        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			response_data['errorsEmp'] = dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])						     
			return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")	



def BuscarPersonal(request):		
	if request.is_ajax():			
		texto= request.GET['texto']
		seleccion = request.GET['seleccion']
		if seleccion=="0":
			empleado = Empleado.objects.filter(DNI__icontains=texto)
			data = serializers.serialize('json',empleado,
			fields={'emp_nom','emp_ape','emp_direccion','DNI','emp_tel'})
			return HttpResponse(data, content_type='application/json')	
		elif seleccion=="1":
			empleado = Empleado.objects.filter(emp_nom__icontains=texto)
			data = serializers.serialize('json',empleado,
			fields={'emp_nom','emp_ape','emp_direccion','DNI','emp_tel'})
			return HttpResponse(data, content_type='application/json')
		elif seleccion=="2":
			empleado = Empleado.objects.filter(emp_ape__icontains=texto)
			data = serializers.serialize('json',empleado,
			fields={'emp_nom','emp_ape','emp_direccion','DNI','emp_tel'})
			return HttpResponse(data, content_type='application/json')
		elif seleccion=="3":
			empleado = Empleado.objects.filter(cargo__id=2)
			empleado= empleado.filter(DNI__icontains=texto)
			data = serializers.serialize('json',empleado,
			fields={'emp_nom','emp_ape','emp_direccion','DNI','emp_tel'})
			return HttpResponse(data, content_type='application/json')
		elif seleccion=="4":
			empleado = Empleado.objects.filter(cargo__id=2)
			empleado= empleado.filter(emp_nom__icontains=texto)
			data = serializers.serialize('json',empleado,
			fields={'emp_nom','emp_ape','emp_direccion','DNI','emp_tel'})
			return HttpResponse(data, content_type='application/json')
		elif seleccion=="5":
			empleado = Empleado.objects.filter(cargo__id=2)
			empleado= empleado.filter(emp_ape__icontains=texto)
			data = serializers.serialize('json',empleado,
			fields={'emp_nom','emp_ape','emp_direccion','DNI','emp_tel'})
			return HttpResponse(data, content_type='application/json')	
		else:
			empleado = Empleado.objects.filter(id=texto)
			#usuario= User.objects.filter(empleado__pk=texto)
			response_data = {'pk':empleado[0].id,'nombre': empleado[0].emp_nom,'apellido':empleado[0].emp_ape,
							'direccion':empleado[0].emp_direccion,'DNI':empleado[0].DNI	,'telefono':empleado[0].emp_tel,	
							'email':empleado[0].email,'sexo':empleado[0].emp_sexo,'fecnac':str(empleado[0].emp_fecnac)
							,'fecIng':str(empleado[0].emp_fecing),'cargo':empleado[0].cargo.id,'user':empleado[0].user.username
							,'userid':empleado[0].user.id}			
			return HttpResponse(json.dumps(response_data), content_type='application/json')
	else :
		print "mal"
		raise Http404


def ModiPersonal(request):	
	if request.method == 'POST':
		instance = Empleado.objects.get(id=request.POST['id'])
		print request.POST['id']
		form = UserFormModi(request.POST or None, instance=instance)		
		#form = UserForm(request.POST)
		response_data = {} 
		if form.is_valid():
			empleado= Empleado.objects.get(id=form.cleaned_data.get('id'))
			empleado.emp_nom = form.cleaned_data.get('emp_nom')	
			empleado.emp_ape = form.cleaned_data.get('emp_ape')
			empleado.emp_fecnac = form.cleaned_data.get('emp_fecnac')
			empleado.emp_direccion = form.cleaned_data.get('emp_direccion')
			empleado.emp_sexo = form.cleaned_data.get('emp_sexo')
			empleado.DNI = form.cleaned_data.get('DNI')
			empleado.emp_tel = form.cleaned_data.get('emp_tel')
			empleado.emp_fecing = form.cleaned_data.get('emp_fecing')	
			empleado.cargo = form.cleaned_data.get('cargo')
			empleado.email = form.cleaned_data.get('email')
			empleado.save()
			response_data['result'] = "Los datos del Personal fueron Actualizados con Exito"				        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errorsEmp': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")

def HomePersonal(req):
	tmpl_vars = {
		#'form': RegistrarPersonalForm(),'form2':RegistrarUserForm
		'form': UserForm()
	}
	return render(req, 'rr_hh/personal.html', tmpl_vars)

def ModiPass(request):	
	if request.method == 'POST':
		instance = User.objects.get(username=request.POST['username'])
		form = UserFormPass(request.POST or None, instance=instance)
		response_data = {}
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			if request.POST['password1'] != request.POST['password2']:
				response_data['errors'] = {"password2": "Los dos campos de contraseña no coinciden"}
				return HttpResponse(json.dumps(response_data),content_type="application/json")
			else :
				if form.is_valid():
					usuario= User.objects.get(username=form.cleaned_data.get('username'))
					usuario.set_password(form.cleaned_data.get('password1'))
					usuario.save()				
					response_data['result'] = "Su contraseña fue Actualizada con Exito"				        
					return HttpResponse(json.dumps(response_data),content_type="application/json")
				else:
					data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
					return HttpResponse(data,content_type="application/json")
		else:
		   response_data['errors'] = {"password": "Su contraseña no es la correcta"}
		   return HttpResponse(json.dumps(response_data),content_type="application/json")		
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")

def HomePass(req):
	tmpl_vars = {		
		'form': UserFormPass()
	}
	return render(req, 'rr_hh/pass.html', tmpl_vars)

def CreateCarga(request):	
	if request.is_ajax():			
		codigo= request.GET['id']
		response_data = {} 	
		for x in request.GET.getlist('servicio[]'):
			serviemp=ServicioEmpleado(empleado_id=codigo, servicio_id=x)
			serviemp.save()			
		response_data['result'] = "El Carga de Servicios fue Almacenada con Exito"
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else :
		print "mal"
		raise Http404

def HomeCarga(req):
	
	tmpl_vars = {		
		'form': RegistrarCargaForm()
	}
	#tmpl_vars['form'].fields['area'].choices=creator_choices
	return render(req, 'rr_hh/Carga.html', tmpl_vars)


def BuscarCarga(request):		
	if request.is_ajax():			
		texto= request.GET['texto']
		if request.GET['seleccion']=='1':
			consulta = ServicioEmpleado.objects.filter(empleado=texto)
			lista=[]
			for carga in consulta:
				d={'pk':carga.id,'servicio': carga.servicio.servi_nom,'estado':carga.estado,'servi_id':carga.servicio.id}

				lista.append(d)
				
			return HttpResponse(json.dumps(lista), content_type='application/json')	
		elif request.GET['seleccion']=='2':
			consulta = ServicioEmpleado.objects.filter(empleado=texto)
			consulta = consulta.filter(estado=True)
			lista=[]
			for carga in consulta:
				d={'pk':carga.id,'servicio': carga.servicio.servi_nom,'estado':carga.estado,'servi_id':carga.servicio.id}
				lista.append(d)
				
			return HttpResponse(json.dumps(lista), content_type='application/json')	

	else :
		print "mal"
		raise Http404

def ModiCarga(request):	
	if request.is_ajax():
		response_data = {} 
		serviemp = ServicioEmpleado.objects.get(id=request.GET['id'])
		if request.GET['estado']=='true':
			serviemp.estado=True
			response_data['result'] = "El servicio quedo habilitado para el especialista selecionado"
		else:
			serviemp.estado=False
			response_data['result'] = "El servicio quedo inhabilitado para el especialista selecionado"
		serviemp.save()			
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")


def HomeHorario(req):
	tmpl_vars = {		
		'form': RegistrarProgramacionForm()
	}	
	return render(req, 'rr_hh/programacion.html', tmpl_vars)


def CreateHorario(request):	
	if request.method == 'POST':
		form = RegistrarProgramacionForm(request.POST)		
		response_data = {} 
		if form.is_valid() :
			bandera=False	
			if form.cleaned_data.get('hor_sal')<=form.cleaned_data.get('hor_ing'):
				response_data['result'] = "La hora de salida debe ser mayor a la hora de ingreso"
			else:
				if (form.cleaned_data.get('turno')== "M") and (form.cleaned_data.get('hor_sal').hour>=13) and (form.cleaned_data.get('hor_sal').minute>0):
					response_data['result'] = "El Turno Mañana solo puede durar hasta la 01:00 PM"
					return HttpResponse(json.dumps(response_data),content_type="application/json")
				elif (form.cleaned_data.get('turno')== "T") and (form.cleaned_data.get('hor_ing').hour<13):
					response_data['result'] = "El Turno Tarde solo puede Iniciar apartir la 01:00 PM"
					return HttpResponse(json.dumps(response_data),content_type="application/json")
				else :
					d= form.cleaned_data.get('hor_fecha')
					delta = dt.timedelta(days=1)			
					h= form.cleaned_data.get('hor_sal').hour - form.cleaned_data.get('hor_ing').hour
					if form.cleaned_data.get('hor_ing').minute > form.cleaned_data.get('hor_sal').minute:
						m= (form.cleaned_data.get('hor_sal').minute+60)-form.cleaned_data.get('hor_ing').minute
						m= m+((h-1)*60)
					else:
						m= form.cleaned_data.get('hor_sal').minute-form.cleaned_data.get('hor_ing').minute
						m= m+(h*60)
					if form.cleaned_data.get('fec_fin'):
						while d<=form.cleaned_data.get('fec_fin'):
							for x in form.cleaned_data.get('serviempledos'):
								if not Programacion.objects.filter(hor_fecha=d,turno=form.cleaned_data.get('turno'),serviempledo_id=x.id):
									serviemp=ServicioEmpleado.objects.get(id=x.id)
									programacion= Programacion(serviempledo_id=x.id)
									programacion.turno= form.cleaned_data.get('turno')
									programacion.hor_fecha= d
									programacion.hor_ing= form.cleaned_data.get('hor_ing')
									programacion.hor_sal= form.cleaned_data.get('hor_sal')
									programacion.cantidadPacientes= m/serviemp.servicio.tiempo_requerido
									programacion.save()	
								else :
									bandera=True
							d += delta
					else:					
						for x in form.cleaned_data.get('serviempledos'):
							if not Programacion.objects.filter(hor_fecha=form.cleaned_data.get('hor_fecha'),turno=form.cleaned_data.get('turno'),serviempledo_id=x.id):
								serviemp=ServicioEmpleado.objects.get(id=x.id)
								programacion= Programacion(serviempledo_id=x.id)
								programacion.turno= form.cleaned_data.get('turno')
								programacion.hor_fecha= form.cleaned_data.get('hor_fecha')
								programacion.hor_ing= form.cleaned_data.get('hor_ing')
								programacion.hor_sal= form.cleaned_data.get('hor_sal')
								programacion.cantidadPacientes= m/serviemp.servicio.tiempo_requerido
								programacion.save()
							else :
								bandera=True
					if bandera:
						response_data['result'] = "El nuevo Horario fue Registrado con Exito, Pero se encontraron fechas con  horarios establecidos, para mas detalle vea el calendario en la gestion de Horario"
					else :
						response_data['result'] = "El nuevo Horario fue Registrado con Exito"	
								
			
			#response_data['postpk'] = paciente.pk	        print "XXSS"
			#paciente.pac_fecnac = form.cleaned_data.get('DNI')	        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			response_data['errorsHor'] = dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])						     
			return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")	


def GestionHorario(req):		
	return render(req, 'rr_hh/GestionProgramacion.html')


def BuscarHorario(request):		
	if request.is_ajax():			
		texto= request.GET['servicio']
		if request.GET['seleccion']=='1':			
			consulta = Programacion.objects.filter(serviempledo_id=texto,hor_fecha__month=datetime.now().month)
			data = serializers.serialize('json',consulta)
			lista=[]
			for carga in consulta:
				if carga.turno=='T':
					d={'id':carga.id,'start': str(carga.hor_fecha)+"T"+str(carga.hor_ing),
					'end': str(carga.hor_fecha)+"T"+str(carga.hor_sal),'title':str(carga.hor_fecha),'description':"Turno Tarde",
		          'className': ["event", "bg-color-red"],'allDay': False,'icon': 'fa-clock-o'}
					lista.append(d)
				else:
					d={'id':carga.id,'start': str(carga.hor_fecha)+"T"+str(carga.hor_ing),
					'end': str(carga.hor_fecha)+"T"+str(carga.hor_sal),'title':str(carga.hor_fecha),
		          'className': ["event", "bg-color-blue"],'allDay': False,'icon': 'fa-clock-o','description':"Turno Mañana"}
					lista.append(d)
				
			return HttpResponse(json.dumps(lista), content_type='application/json')	
		elif request.GET['seleccion']=='2':	
			print request.GET['turno']		
			consulta = Programacion.objects.filter(serviempledo__servicio__id=texto,hor_fecha=request.GET['fecha'],turno=request.GET['turno'])
			lista=[]
			for carga in consulta:
				d={'pk':carga.id,'especialista': carga.serviempledo.empleado.emp_nom+" "+carga.serviempledo.empleado.emp_ape,
				'costo':str(carga.serviempledo.servicio.servi_costo)}
				lista.append(d)
				
			return HttpResponse(json.dumps(lista), content_type='application/json')	
	else :
		print "mal"
		raise Http404

#ID SERVIEMP PARA QUE NO HAYGA OTRO HORARIO DEL MISMO SERVICIO ESE MISMO DIA--LUEGO MIDICAR LA DESCRIPCION PARA QUE DIGA EL SERVICIO-O AREA
def ModiHorario(request):	
	if request.is_ajax():
		response_data = {}
		time= dt.datetime.strptime(request.GET['ingreso'], '%H:%M').time()
		timesalida= dt.datetime.strptime(request.GET['salida'], '%H:%M').time()
		if time.hour>=13:
			turn= "T"
		else:			
			turn= "M"
		if (turn== "M") and (timesalida.hour>=13) and (timesalida.minute>0):
			response_data['result'] = "El Turno Mañana solo puede durar hasta la 01:00 PM"
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:			
			if Programacion.objects.filter(hor_fecha=request.GET['fecha'],turno=turn,serviempledo_id=request.GET['serviemp']).exclude(id=request.GET['id']):
				response_data['result'] = "Ya cuenta con un turno igual para esta fecha"
				return HttpResponse(json.dumps(response_data),content_type="application/json")
			else:
				h= timesalida.hour - time.hour
				if time.minute > timesalida.minute:
					m= (timesalida.minute+60)-time.minute
					m= m+((h-1)*60)
				else:
					m= timesalida.minute-time.minute
					m= m+(h*60)
				programacion = Programacion.objects.get(id=request.GET['id'])
				programacion.turno= turn
				programacion.hor_fecha= request.GET['fecha']
				programacion.hor_ing= time
				programacion.hor_sal= timesalida
				programacion.cantidadPacientes= m/programacion.serviempledo.servicio.tiempo_requerido
				programacion.save()
				response_data['result'] = "El Turno fue modificado con Exito"
				return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")