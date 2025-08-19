from django.urls import path

from .views import LogarView, PerfilView, RegistrarView


app_name = 'usuario'

urlpatterns = [
    path('registrar/', RegistrarView.as_view(), name='registrar'),
    path('logar/', LogarView.as_view(), name='logar'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
]
