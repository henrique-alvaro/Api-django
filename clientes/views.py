from rest_framework import viewsets, filters
from .models import Cliente
from .serializers import ClienteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ClientesViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os alunos e alunas """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']
    filterset_fields = ['ativo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


