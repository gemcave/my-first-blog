from django.shortcuts import render
from rest_framework import generics
from orderbox.serializers import OrderSerializer
from orderbox.models import Order

# Create your views here.
class OrderList(generics.ListCreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer