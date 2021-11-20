from django.shortcuts import render
from rest_framework import response
from django.http import HttpResponse, JsonResponse, request #1
from django.views.decorators.csrf import csrf_exempt #2
from rest_framework.parsers import DataAndFiles, JSONParser #3
from rest_framework.response import Response
from app1.models import table1
from app1.serializers import PropertySerializer

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class PropertyView(APIView):
    def get(self,request):
        users=table1.objects.all()
        serializer=PropertySerializer(users,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        serializer=PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Saved")