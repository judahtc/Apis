
from django.contrib import admin
from django.urls import path,include
from . import views,views1
from app1.views1 import UsersData
urlpatterns = [
path('view/<int:id>',views.UsersView.as_view(),name="UsersView"),

path('',views.Users.as_view(),name="register"),
path('userdata',views1.UsersData.as_view(),name="userinfo"),
path('login',views.LoginView.as_view(),name="register"),

]