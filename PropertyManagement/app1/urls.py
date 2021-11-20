
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

path('view',views.PropertyView.as_view(),name="Prop"),

]