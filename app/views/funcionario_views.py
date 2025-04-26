from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from ..forms.funcionario_forms import FuncionarioForm
from ..entidades import funcionario
from ..services import funcionario_service
from django.contrib.auth.hashers import make_password

@user_passes_test(lambda u: u.cargo == 2)
def listar_funcionarios(request):
    funcionarios = funcionario_service.listar_funcionarios()
    return render(request, 'funcionarios/lista_funcionarios.html', {'funcionarios': funcionarios})

@user_passes_test(lambda u: u.cargo == 2)
def inserir_funcionario(request):
    if request.method == "POST":
        form_funcionario = FuncionarioForm(request.POST)
        if form_funcionario.is_valid():
            nome = form_funcionario.cleaned_data["nome"]
            nascimento = form_funcionario.cleaned_data["nascimento"]
            cargo = form_funcionario.cleaned_data["cargo"]

            usermame = form_funcionario.cleaned_data["username"]
            password = make_password(form_funcionario.cleaned_data["password1"]) # Senha já criptografada

            funcionario_novo = funcionario.Funcionario(nome=nome, nascimento=nascimento, cargo=cargo, username=usermame, 
                                                       password=password)
            funcionario_service.cadastrar_funcionario(funcionario_novo)
            return redirect('listar_funcionarios')
    else:
        form_funcionario = FuncionarioForm()
    return render(request, 'funcionarios/form_funcionario.html', {'form_funcionario': form_funcionario})