from django.db import models


class Evento(models.Model):
    titulo = models.CharField(u'Título do Evento', max_length=250)
    local = models.CharField(u'Local do Evento', max_length=150)
    uf = models.CharField(u'UF', max_length=2)
    cidade = models.CharField(u'Cidade', max_length=50)
    descricao = models.TextField(u'Descrição')
    data_inicial = models.DateField(u'Data Inicial')
    data_final = models.DateField(u'Data Final')

    def __str__(self):
        return self.titulo
