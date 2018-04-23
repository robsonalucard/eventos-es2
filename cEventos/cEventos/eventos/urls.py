from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^lista-eventos/', views.lista_eventos, name='lista_eventos'),
]
