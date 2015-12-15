from django.shortcuts import render
from rest_framework import generics
from serializers import OrderSerializer
from models import Order

# Create your views here.
class  OrderList(generics.ListCreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	
class ZipDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
		