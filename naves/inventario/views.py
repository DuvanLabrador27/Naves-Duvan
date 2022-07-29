from django.shortcuts import render, redirect
from  .models import *


# Create your views here.

def inicio(request):
    return render(request, 'paginas/index.html')


def navesNoTripuladas(request):
    navedos=naveNoTripulada.objects.all()
    return render(request, 'paginas/naveNoTripulada.html', {'navesno':navedos})

def navesTripuladas(request):
    navetres=naveTripulada.objects.all()
    return render(request, 'paginas/naveTripulada.html', {'navesitres':navetres})

def NavesLanzaderas(request):
    #Obtener todas las naves (LISTAR)
    nave=naveLanzadera.objects.all()
    return render(request, 'paginas/naveLanzadera.html', {'naves':nave})