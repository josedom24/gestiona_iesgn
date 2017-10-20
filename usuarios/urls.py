from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.listarUsuarios),
	url(r'^update/(?P<usuario>[0-9a-z.]+)$', views.update),
#	url(r'^alumnos/add$', views.addAlumnos),
#	url(r'^profesores/add$', views.addProfesores),
	url(r'^perfil$', views.perfil),
#	url(r'^alumnos/del$', views.delete),

  ]
