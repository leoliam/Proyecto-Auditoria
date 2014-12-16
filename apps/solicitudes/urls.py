from django.conf.urls import patterns, include, url


urlpatterns = patterns('',			
	url(r'^home-solicitud/$', 'apps.solicitudes.views.HomeSolicitud' , name='solicitud'),
	url(r'^buscar-solicitud/$', 'apps.solicitudes.views.BuscarSolicitud' , name='buscarSolitud'),
	url(r'^create-solicitud/$', 'apps.solicitudes.views.CreateSolicitud' , name='createSolicitud'),
	url(r'^gestion-solicitud/$', 'apps.solicitudes.views.GestionSolicitud' , name='gestionSolicitud'),
	url(r'^buscar-Detalesolicitud/$', 'apps.solicitudes.views.BuscarDetalleSolicitud' , name='buscarDetalleSolitud'),
	url(r'^modi-solicitud/$', 'apps.solicitudes.views.ModiSolicitud' , name='modificarSolicitud '),
	url(r'^buscar-ajax/$', 'apps.solicitudes.views.BuscarAjax' , name='buscar'),
	url(r'^create-post/$', 'apps.solicitudes.views.CreatePost' , name='create'),
	url(r'^modi-post/$', 'apps.solicitudes.views.ModiPost' , name='modificar'),	
	url(r'^home/$', 'apps.solicitudes.views.home' , name='home'),
)
