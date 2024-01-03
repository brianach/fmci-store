from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_storeitems, name='store'),
    path('<storeitem_id>', views.storeitem_detail, name='storeitem_detail'),
]

