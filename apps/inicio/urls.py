from django.conf.urls import patterns, include, url
from .views import IndexView

urlpatterns = patterns('',
    url(r'^$',IndexView.as_view(),name='inicio'),
    #url(r'^$',IndexView.as_view()),
    url(r'^login/$','django.contrib.auth.views.login' ,
     {'template_name':'inicio/login.html'},name='login'),
    url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login' ,name='logout'),
)
