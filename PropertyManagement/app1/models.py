from django.db import models

# Create your models here.
class table1(models.Model):
    propertyID=models.AutoField(primary_key=True)
    propertyName=models.CharField(max_length=250)
    location=models.CharField(max_length=250)
    accomodationType=models.CharField(max_length=250)
    propertyAddress=models.CharField(max_length=250)
    Area=models.CharField(max_length=250)
    propertyAddress=models.CharField(max_length=250)
    date_added=models.CharField(max_length=250)
    
    class Meta:
        db_table='structures'
