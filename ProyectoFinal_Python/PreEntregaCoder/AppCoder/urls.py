from django.urls import path
from AppCoder import views

urlpatterns = [
    path('inicio', views.inicio, name="Inicio"),
    path('productos', views.productos, name="Productos"),
    path('sobreNosotros', views.sobreNosotros, name="SobreNosotros"),
    path('clientes', views.clientes, name="Clientes"),
    path('cursos', views.cursos, name="Cursos"),
    path('consultasFormulario', views.consultasFormulario, name="consultasFormulario"),
    path('busquedaCurso', views.busquedaCurso, name="busquedaCurso"),
    path('buscar/', views.buscar),
    path('leerProductos', views.leerProductos, name="LeerProductos"),
]
