from django.shortcuts import render
from .models import Solicitud,DetalleSolicitud
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from apps.logistica.models import Cargo,Area,Servicio
from .forms import RegistrarSolicitud,RegistrarPacienteForm
from django.core import serializers
from django.http import HttpResponse, Http404
import json



def HomeSolicitud(req):
	tmpl_vars = {		
		'form': RegistrarSolicitud()
	}
	return render(req, 'solicitudes/solicitudes.html',tmpl_vars)



def CreateSolicitud(request):	
	if request.method == 'POST':
		form = RegistrarSolicitud(request.POST)
		response_data = {} 
		if form.is_valid():			
			solicitud= Solicitud(paciente_id=request.POST['paciente'])	
			solicitud.usuario = request.user
			solicitud.soli_abono = float(request.POST['abono'])
			solicitud.soli_descuento =float(request.POST['descuento'])			
			if (float(request.POST['abono'])+float(request.POST['descuento']) )< float(request.POST['CTotal']):
				solicitud.soli_estado=False	
			solicitud.save()
			for i in range(len(request.POST.getlist('servicios[]'))):
				detalle= DetalleSolicitud(solicitud_id=solicitud.pk,programacion_id=request.POST.getlist('servicios[]')[i])			
				detalle.pedido_costo=float(request.POST.getlist('costos[]')[i])
				detalle.NumCita=len(DetalleSolicitud.objects.filter(programacion_id=request.POST.getlist('servicios[]')[i]))+1
				detalle.save()
				
			response_data['result'] = "La Solicitud Fue registrada con Exito"
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")	


def GestionSolicitud(req):
	tmpl_vars = {		
		'form': RegistrarSolicitud()
	}
	return render(req, 'solicitudes/GestionSolicitud.html',tmpl_vars)
	

def BuscarSolicitud(request):		
	if request.is_ajax():			
		texto= request.GET['texto']
		seleccion = request.GET['seleccion']
		if seleccion=="0":
			solicitud = Solicitud.objects.filter(paciente__DNI__icontains=texto).order_by('-fec_reg')
			lista=[]
			for carga in solicitud:
				if carga.soli_estado:
					estado="Cancelado"
				else:
					estado="Por Cancelar"
				d={'pk':carga.id,'PacientePk':carga.paciente.id,'paciente': carga.paciente.pac_nombre+" "+carga.paciente.pac_apellido,'fecha':str(carga.fec_reg),'estado':estado,'abono':float(carga.soli_abono),'descuento':float(carga.soli_descuento)}
				lista.append(d)
				
			return HttpResponse(json.dumps(lista), content_type='application/json')		
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


def BuscarDetalleSolicitud(request):		
	if request.is_ajax():
		texto= request.GET['texto']
		seleccion = request.GET['seleccion']
		if seleccion=="1":
			consulta = DetalleSolicitud.objects.filter(solicitud=texto)
			lista=[]
			for carga in consulta:
				if carga.pedido_estado:
					estado="Antendido"
				else:
					estado="Pendiente"				
				d={'pk':carga.id,'costo':float(carga.pedido_costo),'turno':carga.NumCita,'estado':estado,'cita':str(carga.programacion.hor_fecha)+"-Turno "+str(carga.programacion.turno),'especialista':carga.programacion.serviempledo.empleado.emp_nom,'servicio': carga.programacion.serviempledo.servicio.servi_nom}
				lista.append(d)
				
			return HttpResponse(json.dumps(lista), content_type='application/json')			
		elif seleccion=="11":
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


def ModiSolicitud(request):	
	if request.method == 'POST':
		response_data = {}
		if request.POST['opcion']=='1':					
			user = authenticate(username=request.POST['usuario'], password=request.POST['pass'])
			if user is not None:
				detalle= DetalleSolicitud.objects.get(id=request.POST['id'])			
				if not detalle.pedido_estado:
					if request.POST['cantidad']=='1':
						solicitud=Solicitud.objects.get(id=detalle.solicitud_id)
						solicitud.delete()
						response_data['result'] = "1"
					else :
						detalle.delete()
						solicitud=Solicitud.objects.get(id=detalle.solicitud_id)
						solicitud.soli_abono=request.POST['abono']
						#solicitud.soli_descuento=request.POST['descuento']
						#if(request.POST['abono']+request.POST['descuento'])==request.POST['total']:
						solicitud.soli_estado=True
						solicitud.save()
						response_data['result'] = "2"
				else:
					response_data['result'] = "No se puede eliminar esta cita debido a que ya fue atendida"
			else:				
				response_data['result'] = "Usuario o clave Incorrecta"
				#response_data['postpk'] = paciente.pk	        print "XXSS"
				#paciente.pac_fecnac = form.cleaned_data.get('DNI')	        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		elif request.POST['opcion']=='2':
			solicitud=Solicitud.objects.get(id=request.POST['id'])
			solicitud.soli_abono=request.POST['abono']
			solicitud.paciente_id=request.POST['paciente']
			solicitud.soli_descuento=request.POST['descuento']
			solicitud.usuario=request.user
			if float(request.POST['abono'])==float(request.POST['total']):
				solicitud.soli_estado=True
			else:
				solicitud.soli_estado=False
			solicitud.save()
			response_data['result'] = "Modificacion exitosa"
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")	

def BuscarAjax(request):		
	if request.is_ajax():			
		texto= request.GET['texto']
		seleccion = request.GET['seleccion']
		if seleccion=="0":
			paciente = Paciente.objects.filter(DNI__icontains=texto)
			data = serializers.serialize('json',paciente,
			fields={'pac_nombre','pac_apellido','pac_telefono',
			'pac_direccion','DNI','pac_fecnac'})
			return HttpResponse(data, content_type='application/json')
		elif seleccion=="1":
			paciente = Paciente.objects.filter(pac_nombre__icontains=texto)
			data = serializers.serialize('json',paciente,
			fields={'pac_nombre','pac_apellido','pac_telefono',
			'pac_direccion','DNI','pac_fecnac'})
			return HttpResponse(data, content_type='application/json')
		elif seleccion=="2":
			paciente = Paciente.objects.filter(pac_nombre__icontains=texto)
			data = serializers.serialize('json',paciente,
			fields={'pac_nombre','pac_apellido','pac_telefono',
			'pac_direccion','DNI','pac_fecnac'})
			return HttpResponse(data, content_type='application/json')
		else :
			paciente = Paciente.objects.filter(id=texto)
			data = serializers.serialize('json',paciente,
			fields={'pac_nombre','pac_apellido','pac_telefono',
			'pac_direccion','DNI','pac_fecnac','pac_sexo','pac_obs'})
			return HttpResponse(data, content_type='application/json')		
	else :
		print "mal"
		raise Http404

def home(req):
	tmpl_vars = {
		'form': RegistrarPacienteForm()
	}
	return render(req, 'solicitudes/pacienteB.html', tmpl_vars)


def CreatePost(request):	
	if request.method == 'POST':
		form = RegistrarPacienteForm(request.POST)
		response_data = {} 
		if form.is_valid():
			paciente= Paciente()
			paciente.pac_nombre = form.cleaned_data.get('pac_nombre')
			paciente.pac_apellido = form.cleaned_data.get('pac_apellido')
			paciente.DNI = int(form.cleaned_data.get('DNI'))
			paciente.pac_direccion = form.cleaned_data.get('pac_direccion')
			paciente.pac_telefono = form.cleaned_data.get('pac_telefono')
			paciente.pac_sexo = form.cleaned_data.get('pac_sexo')
			paciente.pac_obs = form.cleaned_data.get('pac_obs')
			paciente.pac_fecnac = form.cleaned_data.get('pac_fecnac')
			paciente.save()
			response_data['result'] = "Los datos del Paciente fueron almacenados con Exito"
			#response_data['postpk'] = paciente.pk	        print "XXSS"
			#paciente.pac_fecnac = form.cleaned_data.get('DNI')	        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")



def ModiPost(request):	
	if request.method == 'POST':
		instance = Paciente.objects.get(id=request.POST['id'])
		form = RegistrarPacienteForm(request.POST or None, instance=instance)
		response_data = {} 
		#print request.POST['id']
		if form.is_valid():
			paciente= Paciente.objects.get(id=form.cleaned_data.get('id'))
			paciente.pac_nombre = form.cleaned_data.get('pac_nombre')
			paciente.pac_apellido = form.cleaned_data.get('pac_apellido')
			paciente.pac_fecnac = form.cleaned_data.get('pac_fecnac')
			paciente.DNI = form.cleaned_data.get('DNI')            
			paciente.pac_direccion = form.cleaned_data.get('pac_direccion')
			paciente.pac_telefono = form.cleaned_data.get('pac_telefono')
			paciente.pac_sexo = form.cleaned_data.get('pac_sexo')
			paciente.pac_obs = form.cleaned_data.get('pac_obs')
			paciente.save()	
			response_data['result'] = "Los datos del Paciente fueron Modificados con Exito"
			#response_data['postpk'] = paciente.pk
			#response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')	        
			return HttpResponse(json.dumps(response_data),content_type="application/json")
		else:
			data = json.dumps({'errors': dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])})        
			return HttpResponse(data,content_type="application/json")
	else:
		return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")

