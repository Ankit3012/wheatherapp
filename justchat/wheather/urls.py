
from django.contrib import admin
from django.urls import path
from wheather import views
urlpatterns = [
    path('', views.index,name='home'),
]
