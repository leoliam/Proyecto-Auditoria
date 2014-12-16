from django.db import models
from apps.logistica.models import Servicio
# Create your models here.
class Categoria(models.Model):    
    cate_nombre = models.CharField(max_length=100)
    cate_descrip = models.CharField(max_length=100, blank=True)
    servi = models.ForeignKey(Servicio)
    def __unicode__(self):
        return self.cate_nombre

class Item(models.Model):    
    item_nombre = models.CharField(max_length=70)
    item_descripcion = models.TextField(blank=True)
    item_valor_referencial = models.TextField(blank=True)
    cate = models.ForeignKey(Categoria)
    def __unicode__(self):
        return self.item_nombre