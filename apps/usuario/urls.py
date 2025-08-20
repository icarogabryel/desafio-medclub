from django.urls import path

from .views import PerfilView


app_name = 'usuario'

urlpatterns = [
    path('perfil/', PerfilView.as_view(), name='perfil'),
]
