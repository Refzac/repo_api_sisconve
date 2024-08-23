from .models import Client
from rest_framework import viewsets,permissions
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class= ClientSerializer

    def get_queryset(self):
        queryset = Client.objects.all()
        id= self.request.query_params.get('id')
        name= self.request.query_params.get('name')
        address= self.request.query_params.get('address')
        email= self.request.query_params.get('email')
        telephone= self.request.query_params.get('telephone')


        if id is not None:
            queryset = queryset.filter(id=id)
        if name is not None:
            queryset = queryset.filter(name=name)
        if address is not None:
            queryset = queryset.filter(address=address)
        if email is not None:
            queryset = queryset.filter(email=email)
        if telephone is not None:
            queryset = queryset.filter(telephone=telephone)

        return queryset
