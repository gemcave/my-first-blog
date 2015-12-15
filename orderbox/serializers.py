from orderbox.models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		field = ('id', 'author','textDep','textDest','created_date')

#Модель
  # author = models.ForeignKey('auth.User')
  #   textDep = models.TextField()
  #   textDest = models.TextField()
  #   created_date = models.DateTimeField(
  #   default=timezone.now)