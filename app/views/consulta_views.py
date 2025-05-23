from django.shortcuts import redirect, render
from django.contrib.auth.decorators import user_passes_test, login_required
from django.template.loader import render_to_string
from django.core.mail import send_mail
from PET_Management import settings
from ..forms import consulta_forms
from ..services import pet_service, consulta_service
from ..entidades import consulta


@user_passes_test(lambda u: u.cargo == 1)
def inserir_consulta(request, id):
    if request.method == "POST":
        form_consulta = consulta_forms.ConsultaPetForm(request.POST)
        pet = pet_service.listar_pet_id(id)
        if form_consulta.is_valid():
            motivo_consulta = form_consulta.cleaned_data["motivo_consulta"]
            peso_atual = form_consulta.cleaned_data["peso_atual"]
            medicamento_atual = form_consulta.cleaned_data["medicamento_atual"]
            medicamento_prescritos = form_consulta.cleaned_data["medicamento_prescritos"]
            exames = form_consulta.cleaned_data["exames"]
            consulta_nova = consulta.ConsultaPet(pet=pet, motivo_consulta=motivo_consulta,
                                                 peso_atual=peso_atual, medicamento_atual=medicamento_atual,
                                                 medicamento_prescritos=medicamento_prescritos,
                                                 exames=exames)
            consulta_service.cadastar_consulta(consulta_nova)
            return redirect('listar_pet_id', pet.id)
    else:
        form_consulta = consulta_forms.ConsultaPetForm()
    return render(request, 'consultas/form_consulta.html', {'form_consulta': form_consulta})


@login_required()
def listar_consulta_id(request, id):
    consulta = consulta_service.listar_consulta(id)
    return render(request, 'consultas/lista_consulta.html', {'consulta': consulta})


@login_required()
def enviar_email_consulta(request, id):
    consulta = consulta_service.listar_consulta(id)
    pet_consulta = pet_service.listar_pet_id(consulta.pet.id)
    assunto = "Resumo da consulta do pet " + pet_consulta.nome
    html_conteudo = render_to_string('consultas/consulta_email.html', {'consulta': consulta})
    corpo_email = 'Resumo da consulta'
    email_remetente = settings.EMAIL_HOST_USER
    email_destino = [pet_consulta.dono.email, ]
    send_mail(assunto, corpo_email, email_remetente, email_destino, html_message=html_conteudo)

    return redirect('listar_consulta_id', id)