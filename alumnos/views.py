from django.shortcuts import render


# Create your views here.
def index(request):
    context={}
    return render(request, 'alumnos/index.html', context)
def Tienda(request):
    context={}
    return render(request, 'alumnos/Tienda.html', context)
def Contacto(request):
    context={}
    return render(request, 'alumnos/Contacto.html', context)
def Donacion(request):
    context={}
    return render(request, 'alumnos/Donacion.html', context)
def carrito(request):
    context={}
    return render(request, 'alumnos/carrito.html', context)
def Nosotros(request):
    context={}
    return render(request, 'alumnos/Nosotros.html', context)

