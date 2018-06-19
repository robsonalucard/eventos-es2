from django import forms

from .models import Evento, Inscricao


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'


class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ('presenca',)
