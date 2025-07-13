from django.urls import path
from . import views

urlpatterns = [
    path('parques/', views.listar_parques, name='listar_parques'),
    path('parques/nuevo/', views.crear_parque, name='crear_parque'),
    path('parques/editar/<int:pk>/', views.editar_parque, name='editar_parque'),
    path('guias/', views.listar_guias, name='listar_guias'),
    path('guias/nuevo/', views.crear_guia, name='crear_guia'),
    path('recorridos/', views.listar_recorridos, name='listar_recorridos'),
    path('recorridos/nuevo/', views.crear_recorrido, name='crear_recorrido'),
]
