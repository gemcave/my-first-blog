from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

def order_list(request):
    return render(request, 'orderbox/order_list.html', {})
class OrderView(GenericAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer




#Для фильтрации запросов
# queryset = Order.objects.filter(color='white')
#Изменения на 18:
# ModelViewSet
# Полный режим бех удаления:
# class OrderViewSet(mixins.CreateModelMixin,
# 				  mixins.RetrieveModelMixin,
# 				  mixins.UpdateModelMixin,
# 				  mixins.ListModelMixin,
# 				  GenericViewSet):