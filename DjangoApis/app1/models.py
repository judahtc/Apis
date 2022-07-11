from email import message
from email.policy import default
from django.db import models
from tensorboard import program

class usersApi(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    access_role=models.CharField(default='student',max_length=200)

    class Meta:
        db_table='usersApi'


class userData(models.Model):
    id = models.AutoField(primary_key=True)
    email=models.CharField(max_length=200)
    university=models.CharField(max_length=200)
    HighSchool	=models.CharField(max_length=200)
    Subjects=models.CharField(max_length=200)
    Subject1=models.CharField(max_length=200)
    Subject2=models.CharField(max_length=200)
    Subject3=models.CharField(max_length=200)
    Program	=models.CharField(max_length=200)
    Age=models.CharField(max_length=200)
    Gender=models.CharField(max_length=200)
    CareerOption=models.CharField(max_length=200)
    
    class Meta:
        db_table='usersData'

class Programmes(models.Model):
    programme_id = models.AutoField(primary_key=True)
    programme_name=models.CharField(max_length=200)
    url=models.CharField(max_length=200)
   

    class Meta:
        db_table='programmes'

class Universities(models.Model):

    university_name=models.CharField(max_length=200)
    university_url=models.CharField(max_length=200)
   
    programme_id=models.IntegerField(default=0)
    programme_name=models.CharField(max_length=200,default='0')
    class Meta:
        db_table='universities'        


class Chats(models.Model):
    chat_id = models.AutoField(primary_key=True)
    user_id=models.CharField(max_length=200)
    user_name=models.CharField(default=0,max_length=200)
    date= models.DateField()  
    title=models.CharField(default=0,max_length=5000)
    likes=models.IntegerField(default=0)
    messages=models.IntegerField(default=0)

    class Meta:
        db_table='chats'

class Messages(models.Model):
    message_id = models.AutoField(primary_key=True)
    chat_id=models.CharField(max_length=200)
    date = models.DateField()
    message=models.CharField(max_length=5000)
    user_id=models.CharField(max_length=200)
    user_name=models.CharField(default=0,max_length=200)
    access_role=models.CharField(default='student',max_length=200)
    likes=models.IntegerField(default=0)