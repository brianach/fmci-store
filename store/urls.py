from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<store_id>', views.store_detail, name='store_detail'),
]
