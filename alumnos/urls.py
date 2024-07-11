#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('pacientes/', views.paciente_list, name='paciente_list'),
    path('paciente_add/', views.paciente_add, name='paciente_add'),
    path('paciente_del/<str:pk>', views.paciente_del, name='paciente_del'),
    path('paciente_findEdit/<str:pk>', views.paciente_findEdit, name='paciente_findEdit'),
    path('pacientesUpdate/', views.pacienteUpdate, name='pacienteUpdate'),
    path('salir/', views.salir, name='salir'),
]
