from django.urls import path
from . import views

urlpatterns = [
    path('getMathNotes', views.getMathNotes),
    path('addMathNote', views.addMathNote)
]