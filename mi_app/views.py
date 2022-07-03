from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime
from mi_app.models import Curso

# Create your views here.


def saludo(request):

    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"Mi Servicio Tecnico {fecha_hora_ahora}")

def saludar_a(request,nombre):
    return HttpResponse(f"Hola {nombre.capitalize()}")

def saludo_personalizado(request):
    pass

def mostrar_index(request):

    return render(request, "mi_app/index.html", {"mi_titulo":'Bienvenido a Mi Pagina!'})

def listar_cursos(request):
    context={}
    context ["cursos"] = Curso.objects.all()

    return render(request,"mi_app/lista_cursos.html",context)
