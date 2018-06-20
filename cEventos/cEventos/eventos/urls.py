from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.lista_eventos, name='lista_eventos'),
    url(r'^novo-evento/', views.novo_evento, name='novo_evento'),
    url(r'^editar-evento/(?P<id_evento>[0-9]+)/$',
        views.editar_evento, name='editar_evento'),
    url(r'^evento/(?P<id_evento>[0-9]+)/$',
        views.evento_profile, name='evento_profile'),
    url(r'^evento_busca/$',
        views.busca_evento, name='busca_evento'),
]
