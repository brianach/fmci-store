from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<store_id>', views.store_detail, name='store_detail'),
]
