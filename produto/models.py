from django.db import models

# Create your models here.

class Produto(models.Model):
    descricao = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.descricao
