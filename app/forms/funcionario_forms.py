from django import forms
from django.forms import DateInput
from django.contrib.auth.forms import UserCreationForm

from ..models import Funcionario


class FuncionarioForm(UserCreationForm):
    class Meta:
        model = Funcionario
        fields = UserCreationForm.Meta.fields + ('nome', 'nascimento', 'cargo')
        widgets = {
            'nascimento': DateInput(attrs={'type': 'date'})
        }