from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        # user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
            
        return user
		