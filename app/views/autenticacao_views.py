from pyexpat.errors import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def login_usuario(request):

    if request.method == 'POST':
        form_login = AuthenticationForm(data=request.POST)

        if form_login.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            usuario = authenticate(username=username, password=password)

            if usuario is not None:
                login(request, usuario)
                return redirect('listar_clientes')
            else:
                messages.error(request, 'Usuário ou senha inválidos')
                return redirect('login')
    else:
        form_login = AuthenticationForm()

    return render(request, 'autenticacao/login.html', {'form_login': form_login})

@login_required()
def deslogar_usuario(request):
    logout(request)
    return redirect('login')