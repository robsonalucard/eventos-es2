from django import forms

from .models import Evento, Inscricao


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        exclude = ('organizador',)


class PresencaForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ('presenca',)
