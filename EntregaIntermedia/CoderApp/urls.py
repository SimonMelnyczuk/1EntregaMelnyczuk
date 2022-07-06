from django.urls import path
from .import views
urlpatterns=[
    path('',views.inicio,name='inicio'),
    path('planta',views.planta,name='planta'),
    path('arbol',views.arbol,name='arbol'),
    path('cactus',views.cactus,name='cactus'),
    path('registrarArbol',views.registrarArbol,name='registrarArbol'),
    path('registrarPlanta',views.registrarPlanta,name='registrarPlanta'),
    path('registrarCactus',views.registrarCactus,name='registrarCactus'),
    path('buscar',views.buscar),
 ]