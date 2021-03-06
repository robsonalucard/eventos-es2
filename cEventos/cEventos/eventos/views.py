from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from datetime import date
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

from .forms import EventoForm
from .models import Evento, Inscricao


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
            f.organizador = request.user
            if compara_datas(f.data_inicial, f.data_final):
                messages.error(
                    request, 'Data Final deve ser posterior ou igual à Data Inicial.')
                return render(request, 'eventos/novo_evento.html', {'form': form})
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


@login_required
def editar_evento(request, id_evento):
    evento = get_object_or_404(Evento, id=id_evento, organizador=request.user)
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
    if request.user.is_authenticated():
        suas_inscricoes = Inscricao.objects.filter(user=request.user)
        if suas_inscricoes:
            eventos_inscritos = Evento.objects.filter(
                id__in=[e.evento.id for e in suas_inscricoes])
            for e in eventos_inscritos:
                if e.id == evento.id:
                    inscrito = True
                    break
                else:
                    inscrito = False
        else:
            inscrito = False
    else:
        # ADICIONAR LINK EM MESSAGE NO TEMPLATE
        messages.info(
            request, mark_safe('Para se inscrever, faça <a href="../../../accounts/login-usuario/" class="alert-link">Login</a> ou <a href="../../../accounts/novo-usuario/" class="alert-link">Cadastre-se</a>.'))
        inscrito = False
    return render(
        request,
        'eventos/evento_profile.html',
        {
            'evento': evento,
            'inscrito': inscrito,
        }
    )


def busca_evento(request):
    id_busca = request.POST.get('busca', '')
    # Query de busca no banco em varias colunas
    eventos = Evento.objects.filter(Q(titulo__icontains=id_busca) | Q(
        local__icontains=id_busca) | Q(cidade__icontains=id_busca) | Q(descricao__icontains=id_busca))
    return render(request, 'eventos/lista_busca.html', {'eventos': eventos})


@login_required
def inscricao_evento(request, id_evento):
    evento = get_object_or_404(Evento, id=id_evento)
    i = Inscricao(data_inscricao=str(date.today()),
                  evento=evento, user=request.user)
    i.save()
    messages.success(request, 'Inscrição realizada com sucesso!')
    return redirect('eventos:evento_profile', id_evento=id_evento)


@login_required
def cancela_inscricao(request, id_evento):
    #evento = get_object_or_404(Evento, id=id_evento)
    i = get_object_or_404(Inscricao, evento=id_evento, user=request.user)
    i.delete()
    messages.success(request, 'Inscrição cancelada com sucesso!')
    return redirect('eventos:evento_profile', id_evento=id_evento)


def comprovante_inscricao(request, id_evento):
    inscricao = get_object_or_404(
        Inscricao, evento=id_evento, user=request.user)
    evento = get_object_or_404(Evento, id=id_evento)
    user = get_object_or_404(User, id=request.user.id)
    return render(
        request,
        'eventos/comprovante.html',
        {
            'inscricao': inscricao,
            'evento': evento,
            'user': user,
        }
    )


def compara_datas(valor1, valor2):
    if valor1 > valor2:
        return True
    return False
