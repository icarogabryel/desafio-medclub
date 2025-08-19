from rest_framework import generics

from .models import Item
from .serializers import ItemSerializer


class ItemList(generics.ListCreateAPIView):
    """View para listar e criar itens"""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """View para obter, atualizar ou deletar um item"""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
