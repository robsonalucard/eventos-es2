from django.contrib import admin

from .models import Evento

class EventoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Evento, EventoAdmin)
