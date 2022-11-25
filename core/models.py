from django.db import models
from django.utils import timezone

from account.models import User


class Perfil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=32)
    bairro = models.CharField(max_length=32)

    def __str__(self):
        return self.nome

class Anuncio(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    tipo_animal = models.CharField(max_length=15)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    def __str__(self):
        return self.titulo