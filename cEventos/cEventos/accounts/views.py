from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, get_user
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserForm, UserFormUpdate


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            u = form.save()
            u.set_password(u.password)
            u.save()
            messages.success(
                request, 'Usuário criado com sucesso. Realize login para acessar sua conta!!')
            return redirect('accounts:user_login')
        else:
            messages.error(
                request, form.errors)
            return render(request, 'accounts/add_user.html', {'form': form})
    else:
        form = UserForm()
    return render(request, 'accounts/add_user.html', {'form': form})


@login_required
def edit_user(request):
    if request.method == 'POST':
        form = UserFormUpdate(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro atualizado.')
            return redirect('accounts:user_profile')
        else:
            messages.error(
                request, form.errors)
            return render(request, 'accounts/add_user.html', {'form': form})
    else:
        form = UserFormUpdate(instance=request.user)
    return render(request, 'accounts/add_user.html', {'form': form})


@login_required
def user_profile(request):
    return render(request, 'accounts/user_profile.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, 'Usuario ou senha invalido.')
    return render(request, 'accounts/user_login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('core')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
        else:
            messages.error(request, 'Não foi possível alterar sua senha!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})
