from django.shortcuts import render
from rest_framework import response
from app1.models import usersApi,userData
from app1.serializers import usersApiSerializer,LoginSerializer,userDataSerializer
from rest_framework import serializers, viewsets
from rest_framework.exceptions import AuthenticationFailed
from django.http import HttpResponse, JsonResponse, request #1
from django.views.decorators.csrf import csrf_exempt #2
from rest_framework.parsers import DataAndFiles, JSONParser #3
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
import requests


# Create your views here.((
class LoginView(APIView):
    
    def post(self,request):
        email =request.data['email']
        password =request.data['password']
        
        user=usersApi.objects.filter(email=email).first()
        
    
        if user is None:
            raise AuthenticationFailed('User not found!')

        if user.password!=password :

            raise AuthenticationFailed("incorrect password")
        userd=userData.objects.get(email=email)
        serializer=userDataSerializer(userd)
        mci=serializer.data['Subjects']
        url="http://127.0.0.1:8000/recommend/"
        final_url= url+str(mci)
        response1 = requests.get(final_url)
        

        return Response(response1.json())
        

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
