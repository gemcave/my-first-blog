from orderbox.models import Order
from rest_framework.serializers import ModelSerializer


class OrderSerializer(ModelSerializer):
	class Meta:
		model = Order
		#Для того чтобы исключить определенный параметр 
		# exclude = ['TextDest']