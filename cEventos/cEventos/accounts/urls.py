from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^troca-senha/$', views.change_password, name='change_password'),
    url(r'^logout-usuario/$', views.user_logout, name='user_logout'),
    url(r'^novo-usuario/$', views.add_user, name='add_user'),
    url(r'^login-usuario/', views.user_login, name='user_login'),
]
