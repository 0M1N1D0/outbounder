
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_contacto, name='index'),
]
