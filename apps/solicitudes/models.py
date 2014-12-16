from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from apps.rr_hh.models import Programacion


class Paciente(models.Model):  
    #paciente_id = models.AutoField(primary_key=True)  
    pac_nombre = models.CharField(max_length=100 , validators=[RegexValidator(
        regex='^[a-zA-Z ]*$',
        message='Este Campo no debe contener numeros')])
    pac_apellido = models.CharField(max_length=100 , validators=[RegexValidator(
        regex='^[a-zA-Z ]*$',
        message='Este Campo no debe contener numeros')])
    pac_fecnac = models.DateField(blank=True, null=True, default=datetime.now)
    pac_sexo = models.CharField(max_length=1, blank=True)
    DNI = models.PositiveIntegerField( validators=[RegexValidator(
        regex='^[0-9]*$',
        message='Este Campo debe contener solo numeros')], unique=True)
    pac_direccion = models.CharField(max_length=100, blank=True)
    pac_telefono = models.CharField(max_length=50, blank=True)
    pac_obs = models.TextField(blank=True,null=True)    
    pac_fecreg = models.DateField(default=datetime.now,auto_now_add=True)
    pac_estado = models.BooleanField(default=True)
    def  __unicode__(self):
    	return self.pac_nombre

class Solicitud(models.Model):
    paciente = models.ForeignKey(Paciente)
    usuario = models.CharField(max_length=50,blank=True, null=True)
    fec_reg = models.DateField(default=datetime.now,auto_now_add=True)
    soli_estado = models.BooleanField(default=True)
    soli_abono = models.DecimalField(max_digits=6, decimal_places=2,validators = [MinValueValidator(0.0), MaxValueValidator(3500.0)])
    soli_descuento = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True) 

class DetalleSolicitud(models.Model):
    solicitud = models.ForeignKey(Solicitud)
    programacion = models.ForeignKey(Programacion)
    NumCita=models.IntegerField()    
    pedido_costo = models.DecimalField(max_digits=6, decimal_places=4)
    pedido_estado = models.BooleanField(default=False)       
    triaje = models.BooleanField(default=False)
    
