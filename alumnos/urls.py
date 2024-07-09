#from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('Tienda', views.Tienda, name='Tienda'),
    path('Contacto', views.Contacto, name='Contacto'),
    path('Donacion', views.Donacion, name='Donacion'),
    path('carrito', views.carrito, name='carrito'),
    path('Nosotros', views.Nosotros, name='Nosotros'),

    
]
    
