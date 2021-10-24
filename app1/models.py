from django.db import models

class usersApi(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    email=models.CharField(max_length=200)

    class Meta:
        db_table='usersApi'