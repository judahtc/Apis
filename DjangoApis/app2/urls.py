
from django.contrib import admin
from django.urls import path,include
from app2 import views

urlpatterns = [
    path('portal',views.portal,name="home"),
    path('login',views.login,name="login"),
    path('users',views.users,name="users"),
    path('signup',views.signup,name="signup"),
    path('registration',views.registration,name="registration"),
    path('uni/<str:prog>',views.University,name="UNI"),
    path('sidebar',views.sidebar,name="sb"),
    path('menubar',views.menubar,name="mb"),
    path('chats',views.Chats1,name="Chatss"),
    path('messages',views.viewChats,name="Chatss"),
    path('reply/<int:chat_id>',views.Messages1,name="Chatss"),
    path('likes/<int:message_id>',views.likes,name="s"),
    path('simulate',views.simulate,name="sim"),
    path('simulate_form',views.simulate_form,name="simf"),
    path('simulated_recs',views.simulated_recs,name="simulated_recs"),
    path('expect_profile/<str:uname>',views.expect_profile,name="expect_profile"),
    path('logout',views.logout,name="logout"),
]