from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator

class Cargo(models.Model):
    cargo_nom = models.CharField(max_length=50)
    cargo_descripcion = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.cargo_nom   

class Area(models.Model):
    area_nom = models.CharField(max_length=70)
    area_descripcion = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.area_nom   

class Servicio(models.Model):
    servi_nom = models.CharField(max_length=70)
    servi_descripcion = models.TextField(blank=True)
    servi_costo = models.DecimalField(max_digits=6, decimal_places=2,validators = [MinValueValidator(0.0), MaxValueValidator(3500.0)])
    area = models.ForeignKey(Area)
    tiempo_requerido=models.IntegerField( validators=[MinValueValidator(10), MaxValueValidator(120),RegexValidator(
        regex='^[0-9]*$',
        message='Este Campo debe contener un Valor Positivo')])
    def __unicode__(self):
        return self.servi_nom   


class Modelo(models.Model):
    Nombre= models.CharField(max_length=70)
    Marca= models.CharField(max_length=70)
    Modelo= models.CharField(max_length=70)
    Serie= models.CharField(max_length=70,unique=True)  
    descripcion = models.TextField(blank=True) 
    def __unicode__(self):
        return self.Nombre 


