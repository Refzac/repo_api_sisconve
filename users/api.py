from .models import User
from rest_framework import viewsets,permissions
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class= UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        id= self.request.query_params.get('id')
        name= self.request.query_params.get('name')
        password= self.request.query_params.get('password')

        if id is not None:
            queryset = queryset.filter(id=id)
        if name is not None:
            queryset = queryset.filter(name=name)
        if password is not None:
            queryset = queryset.filter(password=password)

        return queryset
    
