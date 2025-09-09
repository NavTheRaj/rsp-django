from django.urls import path
from . import views


urlpatterns = [
path('', views.index, name='index'),
path('api/play/', views.play_api, name='play_api'),
]