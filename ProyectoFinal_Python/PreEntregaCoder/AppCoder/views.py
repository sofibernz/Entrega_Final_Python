from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):

    return render(request, 'AppCoder/inicio.html')

def productos(request):

    return render(request, 'AppCoder/productos.html')

def sobreNosotros(request):

    return render(request, 'AppCoder/Sobre nosotros.html')