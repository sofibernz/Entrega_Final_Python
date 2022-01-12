from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import edit
from AppCoder.models import Cursos
from AppCoder.forms import ConsultasFormulario, UserRegisterForm
from AppCoder.models import Consultas, Productos

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#from django.urls import reverse_lazy

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import login, logout, authenticate



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





class ProductoList(ListView):

    model = Productos
    template_name= "AppCoder/productos_list.html"

class ProductoDetalle(DetailView):

    model = Productos
    template_name= "AppCoder/productos_detalle.html"

class ProductoCreacion(CreateView):

    model = Productos
    success_url = "../productos_list"
    fields = ["nombreProd", "precio"]

class ProductoUpdate(UpdateView):
    model = Productos
    success_url = "../producto/list"
    fields = ["nombreProd", "precio"]

class ProductoDelete(DeleteView):
    model = Productos
    success_url = "../producto/list"
     
    


def login_request(request):

    if request.method == "POST":
       
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
                
                usuario = form.cleaned_data.get('username')
                contra = form.cleaned_data.get('password')

                user = authenticate(username=usuario, password=contra)

                if user is not None:

                    login(request, user)

                    return render(request,"AppCoder/inicio.html", {"mensaje":f"¡Hola, {usuario}!"})

                else:
                    return render(request,"AppCoder/inicio.html", {"mensaje": f"Error, datos incorrectos."})
        else:

            return render(request,"AppCoder/inicio.html", {"mensaje": f"Error, formulario erroneo."})
    
    form = AuthenticationForm()
 
    return render(request,"AppCoder/login.html", {"form":form})



def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            
            form = UserRegisterForm(request.POST)
            
            if form.is_valid():

                  username = form.cleaned_data['username']
                  
                  
                  form.save()
                  
                  return render(request,"AppCoder/inicio.html", {"mensaje":f"El usuario '{username}' ha sido creado correctamente."})


      else:
            #form = UserCreationForm()     
            
              
            form = UserRegisterForm()     

      return render(request,"AppCoder/register.html" ,  {"form":form})

