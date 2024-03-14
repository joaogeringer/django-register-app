
from django.contrib import admin
from django.urls import path
from app_register import views

urlpatterns = [
    # route, view and reference name
    path('', views.home,name='home'),
    # users
    path('users/', views.users, name="users_list")
]
