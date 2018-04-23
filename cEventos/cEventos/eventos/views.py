from django.shortcuts import render

from .forms import EventoForm
from .models import Evento

# Create your views here.


def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})
