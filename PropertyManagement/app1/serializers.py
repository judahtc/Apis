from app1.models import table1
from rest_framework import serializers

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model=table1
        fields = '__all__'