from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render

#Auth
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

from .models import Order
from .serializers import OrderSerializer
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import OrderForm
from django.shortcuts import redirect
from mysite.permissions import IsOwnerOrReadOnly

class OrderMixin(object):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user

class OrderViewSet(OrderMixin, ModelViewSet):
	pass
	# queryset = Order.objects.all()
	# serializer_class = OrderSerializer

def order_list(request):
    orders_posts = Order.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'orderbox/order_list.html', {'posts': orders_posts})

def order_detail(request, pk):
    orders_detail_posts = get_object_or_404(Order, pk=pk)
    return render(request, 'orderbox/order_detail.html', {'post': orders_detail_posts})

def new_order(request):
  if request.method == "POST":
            form = OrderForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
               	post.created_date = timezone.now()
                post.save()
                return redirect('orderbox.views.order_detail', pk=post.pk)
  else:
            form = OrderForm()
  return render(request, 'orderbox/order_edit.html', {'form': form})

def order_edit(request, pk):
        post = get_object_or_404(Order, pk=pk)
        if request.method == "POST":
            form = OrderForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.created_date = timezone.now()
                post.save()
                return redirect('orderbox.views.order_detail', pk=post.pk)
        else:
            form = OrderForm(instance=post)
        return render(request, 'orderbox/order_edit.html', {'form': form})
def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('orderbox/login.html', c)
def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')
def loggedin(request):
	return render_to_response('orderbox/loggedin.html',
							 {'full_name': request.user.username})
def invalid_login(request):
	return render_to_response('orderbox/invalid_login.html')
def logout(request):
	auth.logout(request)
	return render_to_response('orderbox/logout.html')

# Для фильтрации запросов
# queryset = Order.objects.filter(color='white')
# Изменения на 18:
# ModelViewSet
# Полный режим бех удаления:
# class OrderViewSet(mixins.CreateModelMixin,
# 				  mixins.RetrieveModelMixin,
# 				  mixins.UpdateModelMixin,
# 				  mixins.ListModelMixin,
# 				  GenericViewSet):


#New:
# from rest_framework.generics import GenericAPIView
# class OrderView(GenericAPIView):
# 	queryset = Order.objects.all()
# 	serializer_class = OrderSerializer