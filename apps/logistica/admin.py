from django.contrib import admin
from .models import *

class CargoAdmin(admin.ModelAdmin):
	list_display=('cargo_nom','cargo_descripcion')

class AreaAdmin(admin.ModelAdmin):
	list_display=('area_nom','area_descripcion')		
	search_fields=('area_nom',)

class ModeloAdmin(admin.ModelAdmin):
	list_display=('Nombre','Marca')		
	search_fields=('Modelo',)

class ServicioAdmin(admin.ModelAdmin):
	list_display=('id','servi_nom','servi_descripcion','area')	
	list_filter=('servi_costo','area')	
	search_fields=('servi_nom',)
	list_editable=('servi_nom','area',)

admin.site.register(Cargo,CargoAdmin)
admin.site.register(Modelo,ModeloAdmin)
admin.site.register(Area,AreaAdmin)
admin.site.register(Servicio,ServicioAdmin)
