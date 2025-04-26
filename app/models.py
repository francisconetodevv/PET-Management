from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
STATE_CHOICES = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins')
]

class EnderecoCliente(models.Model):
    rua = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=30, null=False, blank=False)
    estado = models.CharField(max_length=2, choices=STATE_CHOICES, null=False, blank=False)

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    endereco = models.ForeignKey(EnderecoCliente, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    profissao = models.CharField(max_length=25, null=False, blank=False)

class Pet(models.Model):
    CATEGORIA_PET_CHOICES = (
        ('Ca', 'Cachorro'),
        ('Ga', 'Gato'),
        ('Co', 'Coelho'),
    )

    COR_PET_CHOICES = (
        ('Pr', 'Preto'),
        ('Br', 'Branco'),
        ('Ci', 'Cinza'),
        ('Ma', 'Marrom'),
    )
    nome = models.CharField(max_length=50, null=False, blank=False)
    nascimento = models.DateField(null=False, blank=False)
    categoria = models.CharField(max_length=2, choices=CATEGORIA_PET_CHOICES, null=False, blank=False)
    cor = models.CharField(max_length=2, choices=COR_PET_CHOICES, null=False, blank=False)
    dono = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False, blank=False)


class ConsultaPet(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=False, blank=False)
    data = models.DateField(null=False, blank=False, auto_now_add=True)
    motivo_consulta = models.CharField(max_length=200, null=False, blank=False)
    peso_atual = models.FloatField(null=False, blank=False)
    medicamento_atual = models.TextField(null=False, blank=True)
    medicamento_prescritos = models.TextField(null=False, blank=True)
    exames = models.TextField(null=False, blank=False)


class Funcionario(AbstractUser):
    CARGO_CHOICES = [
        (1, 'Veterinário'),
        (2, 'Financeiro'),
        (3, 'Atendimento')
    ]

    nome = models.CharField(max_length=50, null=False, blank=False)
    nascimento = models.DateField(null=False, blank=False)
    cargo = models.IntegerField(choices=CARGO_CHOICES, null=False, blank=False)