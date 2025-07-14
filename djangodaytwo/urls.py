
from django.urls import path

from djangodaytwo import views

urlpatterns = [
    path('home/', views.home),
    path('about/', views.about),
]
