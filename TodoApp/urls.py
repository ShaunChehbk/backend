from django.urls import path
from . import views

urlpatterns = [
    path('addTodo', views.addTodo),
    path('getTodos', views.getTodos),
]