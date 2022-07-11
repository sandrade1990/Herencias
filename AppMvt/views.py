
from django.http import HttpResponse
from django.shortcuts import render
from AppMvt.models import Familiares
from django.template import Template, Context

# Create your views here.

def Familia(Self):

    miArchivo=open("G:/Mi unidad/Programación/Curso de CODER HOUSE/Proyectos Python/MVTSergioAndrade/MVTSergioAndrade/Plantillas/Template.html")
    Familia=Familiares(nombre='kitty' , Edad= 2, FechaNacimiento = '2020-03-13')
    Familia.save()

    diccionario = {'nombre':Familia.nombre, 'Edad': Familia.Edad, 'FechaNacimiento': Familia.FechaNacimiento}

    plantilla=Template(miArchivo.read())
    miArchivo.close()
    contexto = Context(diccionario)
    documento=plantilla.render(contexto)

    return HttpResponse(documento)

def inicio(request):

    return render(request,"AppMvt/inicio.html")


