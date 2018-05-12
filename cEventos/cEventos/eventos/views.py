from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

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
            f = form.save(commit=False)
            if compara_datas(f.data_inicial, f.data_final):
                messages.error(
                    request, 'Data Final deve ser posterior ou igual à Data Inicial.')
                return render(request, 'eventos/novo_evento.html')
            else:
                f.save()
            return redirect('eventos:lista_eventos')
        else:
            messages.error(
                request, form.errors)
            return render(request, 'eventos/novo_evento.html', {'form': form})
    else:
        form = EventoForm()
    return render(request, 'eventos/novo_evento.html', {'form': form})


def editar_evento(request, id_evento):
    evento = get_object_or_404(Evento, id=id_evento)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            f = form.save(commit=False)
            if compara_datas(f.data_inicial, f.data_final):
                messages.error(
                    request, 'Data Final deve ser posterior ou igual à Data Inicial.')
                return render(request, 'eventos/novo_evento.html', {'form': form})
            else:
                f.save()
            return redirect('eventos:lista_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/novo_evento.html', {'form': form})


def compara_datas(valor1, valor2):
    if valor1 > valor2:
        return True
    return False
