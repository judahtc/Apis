
from app1.models import usersApi 
from rest_framework import serializers

class usersApiSerializer(serializers.ModelSerializer):
    class Meta:
        model=usersApi
        fields = ('email', 'password', 'username')