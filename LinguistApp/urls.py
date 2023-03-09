from django.urls import path
from . import views

urlpatterns = [
    path('getTenWords', views.get_ten_words),
    path('rateWord', views.rate_word),
    path('getRateHistory', views.get_rate_history)
]