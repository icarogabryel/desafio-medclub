from django.db import models


class Pedido(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    itens = models.ManyToManyField('item.Item')
