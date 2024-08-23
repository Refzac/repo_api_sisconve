from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id','clientid','brand','model','year','matricula','country','color','create_time','update_time','year','matricula')
        read_only_fields = ('create_time','update_time')
