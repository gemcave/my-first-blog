from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$', views.order_list, name='order_list'),
    url(r'^order/(?P<pk>[0-9]+)/$', views.order_detail, name='order_detail'),
    url(r'^order/new/$', views.new_order, name='new_order'),
    url(r'^order/(?P<pk>[0-9]+)/edit/$', views.order_edit, name='order_edit'),
    url(r'^sign_up/$', views.SignUp.as_view(), name="sign_up"),
    url(r'^login/$', views.LogIn.as_view(), name="log_in"),
]