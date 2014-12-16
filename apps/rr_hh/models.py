from django.db import models
from django.contrib.auth.models import User
from apps.logistica.models import Cargo
from apps.logistica.models import Servicio
from django.core.validators import RegexValidator
from datetime import datetime

class Empleado(models.Model):
    emp_nom = models.CharField(max_length=100 , validators=[RegexValidator(
        regex='^[a-zA-Z ]*$',
        message='Este Campo no debe contener numeros')])
    emp_ape = models.CharField(max_length=100 , validators=[RegexValidator(
        regex='^[a-zA-Z ]*$',
        message='Este Campo no debe contener numeros')])
    emp_fecnac = models.DateField(default=datetime.now)    
    emp_direccion = models.CharField(max_length=100)    
    emp_sexo = models.CharField(max_length=1, blank=True)
    DNI = models.PositiveIntegerField( validators=[RegexValidator(
        regex='^[0-9]*$',
        message='Este Campo debe contener solo numeros')], unique=True)    
    emp_tel = models.CharField(max_length=12, blank=True)    
    emp_fecing = models.DateField(default=datetime.now)
    emp_fecreg = models.DateField(default=datetime.now,auto_now_add=True)
    avatar = models.ImageField(upload_to='foto_personal')
    #avatar = models.URLField(blank=True,null=True)
    email= models.EmailField(max_length=50, blank=True)    
    cargo = models.ForeignKey(Cargo)
    user = models.OneToOneField(User, unique=True)
    servi_emp = models.ManyToManyField(Servicio, through='ServicioEmpleado',blank=True,null=True)
    def __unicode__(self):
        return self.emp_nom 

class ServicioEmpleado(models.Model):
    servicio = models.ForeignKey(Servicio)
    empleado = models.ForeignKey(Empleado)
    estado = models.BooleanField(default=True)
    
class Programacion(models.Model):    
    serviempledo= models.ForeignKey(ServicioEmpleado)
    turno = models.CharField(max_length=1, blank=True)    
    hor_ing = models.TimeField(blank=True, null=True)
    hor_sal = models.TimeField(blank=True, null=True)    
    hor_fecha = models.DateField()
    cantidadPacientes = models.IntegerField()

    