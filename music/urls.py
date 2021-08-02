from django.contrib import admin
from django.urls import path ,include
from music import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('mymusic/',views.mymusic,name='mymusic'),
    path('lectures/',views.lecture,name='mymusic'),
    path('channel/',views.favchannel,name='channel'),
    path('signin/',views.ourmember,name='signin'),
    path('college/',views.college,name='college'),
    path('pythonlecture/',views.python,name='pythonlecture'),
    path('lectures/gamedev/',views.game,name='gamedev'),
    path('lectures/discord/',views.discord,name='discord')
]
