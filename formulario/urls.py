
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario/', views.formulario, name='formulario'),
    path('submit_registro/<str:cedis>/<str:pais>/<str:campania>', views.submit_registro, name='submit_registro'),
    path('formulario2/<str:pais>/<str:cedis>/<str:campania>', views.formulario2, name='formulario2'),
]

