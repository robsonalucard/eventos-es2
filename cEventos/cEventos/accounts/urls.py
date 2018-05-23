from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^novo-usuario/$', views.add_user, name='add_user'),
    url(r'^login-usuario/', views.user_login, name='user_login'),
]
