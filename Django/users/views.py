
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import Users
from .serializer import UserSerializer

# Create your views here.
def create (request):
    return HttpResponse("This is a create page")

class UsersCreateList(generics.ListCreateAPIView):
    queryset = Users.objects.all();
    serializer_class =UserSerializer;


