
from app1.models import usersApi ,userData
from rest_framework import serializers

class usersApiSerializer(serializers.ModelSerializer):
    class Meta:
        model=usersApi
        fields = ('email', 'password', 'username')


class userDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=userData
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=userData
        fields = ('email', 'password')             