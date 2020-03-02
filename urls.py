from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('^home/$', views.index, name='index'),
    path('^ads/$', views.ad, name='ad'),
    path('^bookings/<int:game_id>/$', views.booking, name='booking'),
]
