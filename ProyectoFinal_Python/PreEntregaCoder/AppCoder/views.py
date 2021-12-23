from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Clientes
from AppCoder.forms import ClientesFormulario


# Create your views here.

def inicio(request):

    return render(request, 'AppCoder/inicio.html')

def productos(request):

    return render(request, 'AppCoder/productos.html')

def sobreNosotros(request):

    return render(request, 'AppCoder/sobreNosotros.html')

def clientes(request):

    return render(request, 'AppCoder/clientes.html')

def cursos(request):

    return render(request, 'AppCoder/cursos.html')

def clientesFormulario(request):

    if request.method == 'POST':
       
        miFormulario = ClientesFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            clientes = Clientes(apellido=informacion['apellido'], nombre=informacion['nombre'], email=informacion['email'])

            clientes.save()

            return render(request, 'AppCoder/inicio.html')

    else:

        miFormulario= ClientesFormulario()

    return render(request, 'AppCoder/clientesFormulario.html', {'miFormulario': miFormulario})

