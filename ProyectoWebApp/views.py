from django.shortcuts import render, HttpResponse

from servicios.models import Servicio

import requests

# Create your views here.
def home (request):

    return render(request,"ProyectoWebApp/home.html")



def tienda (request):

    return render(request,"ProyectoWebApp/tienda.html")



def contacto (request):

    return render(request,"ProyectoWebApp/contacto.html")

def covid (request):
    response=requests.get('https://api.covid19api.com/country/Argentina/status/confirmed?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z').json()
    return render (request,'ProyectoWebApp/covid.html', {'response':response})