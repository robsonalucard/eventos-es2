from django.shortcuts import render, redirect

from .forms import EventoForm
from .models import Evento

# Create your views here.


def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})


def novo_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eventos:lista_eventos')
        else:
            print(form.errors)
    else:
        form = EventoForm()
    return render(request, 'eventos/novo_evento.html', {'form': form})
