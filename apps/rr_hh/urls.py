from django.conf.urls import patterns, include, url


urlpatterns = patterns('',			
	url(r'^home-personal/$', 'apps.rr_hh.views.HomePersonal' , name='personal'),
	url(r'^buscar-personal/$', 'apps.rr_hh.views.BuscarPersonal' , name='buscarP'),
	url(r'^create-personal/$', 'apps.rr_hh.views.CreatePersonal' , name='createP'),
	url(r'^modi-personal/$', 'apps.rr_hh.views.ModiPersonal' , name='modificarP '),
	url(r'^home-pass/$', 'apps.rr_hh.views.HomePass' , name='Pass'),
	url(r'^modi-pass/$', 'apps.rr_hh.views.ModiPass' , name='modiPass'),
	url(r'^home-carga/$', 'apps.rr_hh.views.HomeCarga' , name='Carga'),
	url(r'^create-carga/$', 'apps.rr_hh.views.CreateCarga' , name='createCarga'),
	url(r'^buscar-carga/$', 'apps.rr_hh.views.BuscarCarga' , name='buscarCarga'),
	url(r'^modi-carga/$', 'apps.rr_hh.views.ModiCarga' , name='modiCarga'),
	url(r'^home-horario/$', 'apps.rr_hh.views.HomeHorario' , name='horario'),
	url(r'^create-horario/$', 'apps.rr_hh.views.CreateHorario' , name='createHorario'),
	url(r'^buscar-horario/$', 'apps.rr_hh.views.BuscarHorario' , name='buscarHorario'),
	url(r'^home-gestionHorario/$', 'apps.rr_hh.views.GestionHorario' , name='GestionHorario'),
	url(r'^modi-horario/$', 'apps.rr_hh.views.ModiHorario' , name='modiHoario'),


)
