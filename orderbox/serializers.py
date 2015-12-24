from orderbox.models import Order
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
# from oauth2_provider.models import Application


class OrderSerializer(ModelSerializer):
	class Meta:
		model = Order
		#Для того чтобы исключить определенный параметр 
		# exclude = ['TextDest']
class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        write_only_fields = ('password',)
class LogInSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        write_only_fields = ('password',)
        # Application.objects.get(user=obj).client_id