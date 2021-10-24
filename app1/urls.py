
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
path('view/<int:id>',views.UsersView.as_view(),name="UsersView"),

path('register',views.Users.as_view(),name="register"),
]