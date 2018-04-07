from django.db import models


class Evento(models.Model):
    TIPO_CHOICES = (
        ('B', 'Baixa'),
        ('M', 'Média'),
        ('B', 'Alta'),
    )
    nome = models.CharField(u'Nome', max_length=100)
    # tipo = models.CharField(u'Nome', max_length=100)
    descricao = models.TextField(u'Descrição')
    data_inicial = models.DateField(u'Data Inicial')
    data_final = models.DateField(u'Data Final')

    def __str__(self):
        return self.nome
