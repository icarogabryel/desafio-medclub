from django.contrib import admin
from django.urls import include, path

from apps.item.urls import urlpatterns as item_urls
from apps.pedido.urls import urlpatterns as pedido_urls
from apps.usuario.urls import urlpatterns as usuario_urls
from apps.usuario.views import LogarView, RegistrarView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('logar/', LogarView.as_view(), name='logar'),
    path('registrar/', RegistrarView.as_view(), name='registrar'),
    path('usuario/', include(usuario_urls)),
    path('itens/', include(item_urls)),
    path('pedidos/', include(pedido_urls)),
]
