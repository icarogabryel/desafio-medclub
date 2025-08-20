from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import Response as DRFResponse

from .serializers import LoginSerializer, RegisterSerializer, UserSerializer


class RegistrarView(generics.CreateAPIView):
    """
    View para registrar novos usuários. Retorna os dados do usuário criado.
    """
    serializer_class = RegisterSerializer


class LogarView(generics.GenericAPIView):
    """
    View para realizar o login de usuários. Retorna um token de autenticação.
    """
    serializer_class = LoginSerializer

    def post(self, request: Request, *args, **kwargs) -> DRFResponse:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.validated_data['usuario']
        token, _ = Token.objects.get_or_create(user=usuario)

        return Response({'token': token.key}, status=status.HTTP_200_OK)


class PerfilView(generics.RetrieveUpdateAPIView):
    """
    View para obter e atualizar o perfil do usuário autenticado. Pega o token
    de autenticação do usuário. Retorna os dados do usuário.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
