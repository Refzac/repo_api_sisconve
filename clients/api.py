from .models import Client
from rest_framework import viewsets,permissions
from .serializers import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class= ClientSerializer

