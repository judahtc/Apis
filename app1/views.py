from django.shortcuts import render
from rest_framework import response
from app1.models import usersApi
from app1.serializers import usersApiSerializer
from rest_framework import serializers, viewsets

from django.http import HttpResponse, JsonResponse, request #1
from django.views.decorators.csrf import csrf_exempt #2
from rest_framework.parsers import DataAndFiles, JSONParser #3
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.

class UsersView(APIView):
    def get_object(self, id):
        
        try:
            data1 = usersApi.objects.get(id=id)
            return data1
        except:
            return Response("user does not exist")    

    def get(self, request,id): 
        try:
                users=self.get_object(id)        
                serializer=usersApiSerializer(users)
                
                return Response(serializer.data)
        except:
            
                return Response("user does not exist")

    def delete(self,request,id):
        users=self.get_object(id)
        users.delete()
        
        return Response("deleted")

    def put(self,request,id):
        try:
            users=self.get_object(id)
            serializer = usersApiSerializer(users,data=request.data)
            if serializer.is_valid():
                serializer.save()
                response1=serializer.data
            
                return Response(response1) 
        except:        
            return Response("Not updated")    




class Users(APIView):
    def get(self,request):
        users=usersApi.objects.all()
        serializer=usersApiSerializer(users,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        serializer=usersApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Saved")
    