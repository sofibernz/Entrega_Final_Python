from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Cursos
from AppCoder.forms import ConsultasFormulario
from AppCoder.models import Consultas, Productos


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


def consultasFormulario(request):

    if request.method == 'POST':
       
        miFormulario = ConsultasFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            consultas = Consultas(consulta=informacion['consulta'], nombre=informacion['nombre'], telefono=informacion['telefono'], email=informacion['email'])

            consultas.save()

            return render(request, 'AppCoder/inicio.html')

    else:

        miFormulario= ConsultasFormulario()

    return render(request, 'AppCoder/consultasFormulario.html', {'miFormulario': miFormulario})


def busquedaCurso(request):

    return render(request, 'AppCoder/busquedaCurso.html')


def buscar(request):

    if request.GET["curso"]:
        
        curso = request.GET["curso"]

        cursos = Cursos.objects.filter(curso__icontains=curso)

        return render(request, "AppCoder/resultadoBusqueda.html", {"cursos":cursos, "curso":curso})

    else:

        respuesta = "Ingresar datos."

    return HttpResponse(respuesta)


def leerProductos(request):

    productos = Productos.objects.all()

    dir = {"productos": productos}

    return render(request, "AppCoder/leerProductos.html", dir)