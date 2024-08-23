from .models import Vehicle
from rest_framework import viewsets,permissions
from .serializers import VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    permissions_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        id= self.request.query_params.get('id')
        clientid = self.request.query_params.get('clientid')
        brand = self.request.query_params.get('brand')
        model = self.request.query_params.get('model')
        year = self.request.query_params.get('year')
        matricula = self.request.query_params.get('matricula')
        country = self.request.query_params.get('country')
        color = self.request.query_params.get('color')

        if id is not None:
            queryset = queryset.filter(id=id)

        if clientid is not None:
            queryset = queryset.filter(clientid=clientid)
    
        if brand is not None:
            queryset = queryset.filter(brand=brand)
    
        if model is not None:
            queryset = queryset.filter(model=model)

        if year is not None:
            queryset = queryset.filter(year=year)

        if matricula is not None:
            queryset = queryset.filter(matricula=matricula)

        if country is not None:
            queryset = queryset.filter(country=country)

        if color is not None:
            queryset = queryset.filter(color=color)

        return queryset
    
