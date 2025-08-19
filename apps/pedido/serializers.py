from rest_framework import serializers

from .models import Pedido


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'usuario', 'itens']
        read_only_fields = ['usuario']
