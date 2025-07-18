from rest_framework import generics
from .serializer import OrderSerializer
from .models import Order
from django.shortcuts import render

# Create your views here.


def home(request):
 return render(request, 'order.html', {'name': 'Aarati'})


class OrderCreateList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'
