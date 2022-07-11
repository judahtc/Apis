from django.shortcuts import render
from rest_framework import response
from app1.models import usersApi,userData
from app1.serializers import usersApiSerializer,userDataSerializer
from rest_framework import serializers, viewsets

from django.http import HttpResponse, JsonResponse, request #1
from django.views.decorators.csrf import csrf_exempt #2
from rest_framework.parsers import DataAndFiles, JSONParser #3
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status


class UsersData(APIView):
    def get(self,request):
        userdata=userData.objects.all()
        serializer=userDataSerializer(userdata,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        serializer=userDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Saved")
    