from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index, name='index'),
    path('formulario_contacto/', views.formulario_contacto, name='formulario_contacto'),
    path('guardar_contacto/', views.guardar_contacto, name='guardar_contacto'),
    path('consulta_servicios/', views.consulta_servicios, name='consulta_servicios'),
    path('buscar_servicio/', views.buscar_servicio, name='buscar_servicio'),
    path('mochilas/', views.mochilas, name='mochilas'),
    path('compra/', views.compra, name='compra'),
    path('contactanos/', views.contactanos, name='contactanos'),
]


