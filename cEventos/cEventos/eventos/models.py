from django.db import models
from django.contrib.auth.models import User


class Evento(models.Model):
    titulo = models.CharField(u'Título do Evento', max_length=250)
    local = models.CharField(u'Local do Evento', max_length=150)
    uf = models.CharField(u'UF', max_length=2)
    cidade = models.CharField(u'Cidade', max_length=50)
    descricao = models.TextField(u'Descrição')
    data_inicial = models.DateField(u'Data Inicial')
    data_final = models.DateField(u'Data Final')
    organizador = models.ForeignKey(User)

    def __str__(self):
        return self.titulo


class Inscricao(models.Model):
    data_inscricao = models.DateField(u'Data de Inscrição')
    presenca = models.BooleanField(default=False)
    evento = models.ForeignKey(Evento)
    user = models.ForeignKey(User)

    def __str__(self):
        return 'Evento: {} / Usuário: {}'.format(self.evento, self.user)
