from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','email','password','create_time','update_time')
        read_only_fields = ('create_time','update_time')