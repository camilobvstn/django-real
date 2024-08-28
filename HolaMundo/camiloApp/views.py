from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.

def display(request):
    return HttpResponse("<h1>Hola mundo!</h1>")

def displayDateTime(request):
    dt=datetime.datetime.now()
    s="<b>Fecha y Hora Actual: </b>"+str(dt)
    return HttpResponse(s)

def formulario(request):
    lol="<h1>Formulario</b>"+"<br></>"+"<h3>Usuario</>"+"<br>"+"<input> </>"+"<br></>"+"<h3>Pass</>"+"<br>"+"<input>"+"<br></>"+"<br></>"+"<Button>Enviar</>"
    return HttpResponse(lol)