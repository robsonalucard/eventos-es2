from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

from .forms import EventoForm
from .models import Evento, Inscricao, User


@login_required
def lista_eventos(request):
    seus_eventos = Evento.objects.filter(organizador=request.user)
    suas_inscricoes = Inscricao.objects.filter(user=request.user)
    eventos_inscritos = Evento.objects.filter(
        id__in=[e.evento.id for e in suas_inscricoes])
    return render(
        request,
        'eventos/lista_eventos.html',
        {
            'seus_eventos': seus_eventos,
            'eventos_inscritos': eventos_inscritos
        }
    )


@login_required
def novo_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            if compara_datas(f.data_inicial, f.data_final):
                messages.error(
                    request, 'Data Final deve ser posterior ou igual à Data Inicial.')
                return render(request, 'eventos/novo_evento.html', {'form': form})
            else:
                f.user = request.user
                f.save()
            return redirect('eventos:lista_eventos')
        else:
            messages.error(
                request, form.errors)
            return render(request, 'eventos/novo_evento.html', {'form': form})
    else:
        form = EventoForm()
    return render(request, 'eventos/novo_evento.html', {'form': form})


@login_required
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


def evento_profile(request, id_evento):
    evento = get_object_or_404(Evento, id=id_evento)
    return render(
        request,
        'eventos/evento_profile.html',
        {
            'evento': evento
        }
    )


def compara_datas(valor1, valor2):
    if valor1 > valor2:
        return True
    return False
