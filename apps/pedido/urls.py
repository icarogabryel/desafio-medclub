from django.urls import path

from .views import PedidoUsuarioListCreateView, PedidoUsuarioDetailView


app_name = 'pedidos'

urlpatterns = [
    path('', PedidoUsuarioListCreateView.as_view(), name='listar'),
    path('<int:pk>/', PedidoUsuarioDetailView.as_view(), name='detalhar'),
]
