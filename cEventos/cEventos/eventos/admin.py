from django.contrib import admin

from .models import Evento, Inscricao


class EventoAdmin(admin.ModelAdmin):
    pass


class InscricaoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Evento, EventoAdmin)
admin.site.register(Inscricao, InscricaoAdmin)
