from django.urls import path

from .views import PedidoUsuarioCreateView, PedidoUsuarioListView, PedidoUsuarioDetailView


app_name = 'pedidos'

urlpatterns = [
    path('', PedidoUsuarioListView.as_view(), name='listar'),
    path('novo/', PedidoUsuarioCreateView.as_view(), name='criar'),
    path('<int:pk>/', PedidoUsuarioDetailView.as_view(), name='detalhar'),
]
