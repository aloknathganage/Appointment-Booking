from django.contrib import admin
from django.urls import path
from django.http import HttpRequest
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index2',views.index2,name='index2'),
    path('appoinment',views.appoinment,name='appoinment'),
    # path('contact',views.contact,name='contact'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

]

