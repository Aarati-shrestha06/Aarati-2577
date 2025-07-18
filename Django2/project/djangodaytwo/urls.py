
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('team/', views.team, name='team'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('career/', views.career, name='career'),
    path('feedback/', views.feedback, name='feedback'),
]

