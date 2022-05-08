from django.shortcuts import render, HttpResponse

from servicios.models import Servicio

import requests

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout,authenticate
from ProyectoWebApp.forms import UserRegisterForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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


def login_request(request):

    if request.method =="POST":
        form= AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            usuario= form.cleaned_data.get('username')
            contra= form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contra)

            if user is not None:
                login(request,user)

                return render(request,"ProyectoWebApp/home.html", {"mensaje":f"Bienvenido{usuario}"})

            else:

                return render(request,"ProyectoWebApp/home.html", {"mensaje":"Error, datos incorrectos"})

        else:

                return render(request,"ProyectoWebApp/home.html", {"mensaje":"Error, formulario erroneo"})

    form= AuthenticationForm()

    return render(request,"ProyectoWebApp/login.html", {'form':form})


def register (request):

    if request.method == 'POST':

        #form= UserCreationForm(request.POST)
        form= UserRegisterForm(request.POST)

        if form.is_valid():

            username= form.cleaned_data['username']
            form.save()
            return render(request,"ProyectoWebApp/home.html", {"mensaje":"Usuario Creado :)"})

    else:
        #form=UserCreationForm()
        form=UserRegisterForm()
    
    return render(request,"ProyectoWebApp/registro.html", {"form":form})

    