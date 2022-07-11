from base64 import decode
from datetime import datetime,date
from os import access
from re import sub
from django.http import response
from django.shortcuts import render

from django.shortcuts import render,redirect
from matplotlib.pyplot import title
from matplotlib.style import context
from tensorboard import program
from app1.models import userData,usersApi,Programmes,Universities,Chats,Messages
from datetime import date
from django.db import connection, transaction
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.exceptions import AuthenticationFailed
import requests
import json
from flask import jsonify
import pandas as pd
# Create your views here.

def home(request):
    return render(request,"home.html")




def signup(request):
    if request.method=='POST':
        if request.POST.get('username'):
            request.session['email_session']= request.POST['email']
            user=usersApi()
            user.username=request.POST.get('username')
            user.password=request.POST.get('password')
            user.email=request.POST.get('email')
            user.access_role=request.POST.get('access_role')
            user.save()
            if request.POST.get('access_role')=='student':
                return render(request,"reg.html") 
            else:
                return render(request,"index.html")    
    return render(request,"signup.html")

    
def registration(request):
    if request.method=='POST':
        if request.POST.get('HighSchool'):
            mail=request.session['email_session']
            user=userData()
            user.email=mail
            user.university=request.POST.get('university')
            user.HighSchool	=request.POST.get('HighSchool')
            s1=request.POST.get('Subject_1')
            s2=request.POST.get('Subject_2')
            s3=request.POST.get('Subject_3')
            subs=s1+', '+s2+', '+s3
            user.Subjects=subs
            user.Subject1=request.POST.get('Subject1')
            user.Subject2=request.POST.get('Subject2')
            user.Subject3=request.POST.get('Subject3')
            user.Program='Any'
            user.Age='23'
            user.Gender=request.POST.get('Gender')
            user.CareerOption=request.POST.get('CareerOption')
            user.save()
            return render(request,"index.html")

    return render(request,"reg.html")


def login(request):
   
        return render(request,"index.html")   

def users(request):
    users=usersApi.objects.all()
    context={'users':users}
    return render(request,"juloh.html",context)


def portal(request):
    try:
        if request.method=='POST':
            if usersApi.objects.filter(email=request.POST['email'],password=request.POST['password']).exists():    
                request.session['email']= request.POST['email']
                email=request.session['email']
                all=usersApi.objects.get(email=request.POST['email'])
                if usersApi.objects.filter(access_role='student',email=request.POST['email']):
                    request.session['name']=all.username
                    userd=userData.objects.get(email=email)
                    total=int(userd.Subject1)+int(userd.Subject2)+int(userd.Subject3)
                    co=userd.CareerOption
                    mci=userd.Subjects
                    url="http://127.0.0.1:8000/recommend/"
                    final_url= url+str(mci)+str(co)+str(total)
                    response1 = requests.get(final_url)
                    request.session['response2']=response1.json()
                    nana=request.session['name']
                    nana=nana.upper()
                    return render(request,"sidebar.html",{"data":response1.json,"username":nana})
                else:
                    chats= Chats.objects.all()
                    return render(request,"viewChats.html",{'chats':chats})
            else:
                    context={'data':"invalid username or password"}  
                    return render(request,"index.html",context)  
    except:
        ex="SERVER NOT RESPONDING....."
        context={'ex':ex}
        return render(request,"uni.html",context)
def University(request,prog):
    try:
        progr=Programmes.objects.get(programme_name=prog)
        prog1=progr.programme_name
        uni=Universities.objects.filter(programme_name=prog1)
        
        context={'uni':uni,'prog':prog1}
        return render(request,"uni.html",context)
    except:
        ex="loading....."
        ex1=prog
        context={'ex':ex,'ex1':ex1}
        return render(request,"uni.html",context)

def sidebar(request):
    response3=request.session['response2']
    return render(request,"sidebar.html",{"data":response3})
   

def menubar(request):
     response2 = request.session['response2']
     context={'data':response2}
     return render(request,"menubar.html",context)



def Chats1(request):
    if request.method=='POST':
        if request.POST.get('title'):

            mail=request.session['email']
            all=usersApi.objects.get(email=mail)
            chats=Chats()
            chats.title=request.POST.get('title')
            chats.date=datetime(2013,12,25)
            chats.user_id=all.id
            chats.user_name=all.username
            chats.save()
            print(request.POST.get('title'))
            chats= Chats.objects.all()
            return render(request,"viewChats.html",{'chats':chats})
    return render(request,"login.html")


def viewChats(request):

    chats= Chats.objects.all()
    return render(request,"viewChats.html",{'chats':chats})




def Messages1(request,chat_id):
    
    if request.method=='POST':
        if request.POST.get('message'):
            mail=request.session['email']
            all=usersApi.objects.get(email=mail)
            chats= Chats.objects.get(chat_id=chat_id)
            
            message=Messages()
            message.chat_id=chats.chat_id
            message.date = datetime(2013,12,25)
            message.message=request.POST.get('message')
            message.user_id=all.id
            message.user_name=all.username
            message.access_role=all.access_role
            message.save()
            
            chats= Chats.objects.get(chat_id=chat_id)
    
            messages=Messages.objects.filter(chat_id=chat_id)   

            return render(request,"messages.html",{'qn':chats,'mess':messages}) 

    chats= Chats.objects.get(chat_id=chat_id)
    
    messages=Messages.objects.filter(chat_id=chat_id) 
    request.session['chat_id']=chat_id
    return render(request,"messages.html",{'qn':chats,'mess':messages})

def likes(request,message_id):
    juloh=Messages.objects.get(message_id=message_id)
    mes=juloh
    mes.likes=juloh.likes+1
    mes.save()
    chat_id=request.session['chat_id']
    chats= Chats.objects.get(chat_id=chat_id)
    messages=Messages.objects.filter(chat_id=chat_id)   

    return render(request,"messages.html",{'qn':chats,'mess':messages})

def simulate(request):

    return render(request,"simulate_iframe.html")
def simulate_form(request):

    return render(request,"simulate.html")

def simulated_recs(request):
    if request.method=='POST':
        if request.POST.get('HighSchool'):
          
            s1=request.POST.get('subject_1')
            s2=request.POST.get('subject_2')
            s3=request.POST.get('subject_3')
            subs=s1+', '+s2+', '+s3
            
            Subject1=request.POST.get('grade1')
            Subject2=request.POST.get('grade2')
            Subject3=request.POST.get('grade3')
        
            CareerOption=request.POST.get('CareerOption')
            
            total=int(Subject1)+int(Subject2)+int(Subject3)
            co=CareerOption
            mci=subs
            url="http://127.0.0.1:8000/recommend/"
            final_url= url+str(mci)+str(co)+str(total)
            print(final_url)
                    
            response1 = requests.get(final_url)
            request.session['response2']=response1.json()
            return render(request,"simulate2.html",{"data":response1.json})        
    return render(request,"simulate2.html")


def expect_profile(request,uname):
    user=usersApi.objects.get(username=uname)
    return render(request,"expect_profile.html",{"user":user})


def logout(request):
    
    del request.session['email']
    
    return render(request,"index.html")
