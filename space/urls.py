from django.urls import path
from . import views

urlpatterns = [
    path('', views.spaces, name='space'),
]
