from django.urls import path
from . import views

# app_name = 'formulario'
urlpatterns = [
	path('', views.index, name='index'),
	path('formulario/', views.formulario, name='formulario'),
	# TODO: cambiar int por str
	path('submit_registro/<str:cedis>/<str:pais>/<str:campania>/<str:num_dist>/', views.submit_registro,
	     name='submit_registro'),
	path(
		'formulario2/<str:pais>/<str:cedis>/<str:campania>/<int:registros_totales>/<int:total_no_exitosos>/<int'
		':total_exitosos>/',
		views.formulario2, name='formulario2'),
]
