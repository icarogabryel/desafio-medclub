from rest_framework import generics, permissions
from .models import Pedido
from .serializers import PedidoSerializer


class PedidoUsuarioListCreateView(generics.ListCreateAPIView):
    """View para criar e listar todos os pedidos do usuário autenticado."""
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Pedido.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class PedidoUsuarioDetailView(generics.RetrieveAPIView):
    """View para obter os detalhes de um pedido do usuário autenticado."""
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Pedido.objects.filter(usuario=self.request.user)
