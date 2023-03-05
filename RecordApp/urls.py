from django.urls import path
from . import views

urlpatterns = [
    path('getRecords', views.getRecords),
    path('addRecord', views.addRecord)
]