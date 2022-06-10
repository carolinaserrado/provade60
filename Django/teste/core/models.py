from django.db import models
from .models import Produto

# Create your models here.
class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    estoque = models.IntegerField('Quantidade em estoque')

    def __str__(self):
        return self.nome

