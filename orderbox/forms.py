from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Order

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ('textDep', 'textDest', 'truckType', 'created_date' )
		labels = {
            "textDep": _("Адрес отправления"),
            "textDest": _("Адрес назначения"),
            "truckType": _("Тип грузовика"),
            "created_date": _("Дата и время отправления"),
        }