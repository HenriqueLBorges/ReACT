from django.db import models
import datetime

class Atleta(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    idade = models.IntegerField()
    peso = models.DecimalField(max_digits=4, decimal_places=2)
    gênero = models.CharField(max_length=9)
    deh_nascimento = models.DateField()
    deh_cadastro = models.DateField(default = datetime.datetime.now())
