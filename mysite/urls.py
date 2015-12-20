from django.conf.urls import url, include
from django.contrib import admin

from .routers import router

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/(?P<pk>[0-9]+)/', include(router.urls)),
    url(r'', include('orderbox.urls')),
    #User auth urls
    url(r'^accounts/login/$', 'orderbox.views.login'),
    url(r'^accounts/auth/$', 'orderbox.views.auth_view'),
    url(r'^accounts/logout/$', 'orderbox.views.logout'),
    url(r'^accounts/loggedin/$', 'orderbox.views.loggedin'),
    url(r'^accounts/invalid/$', 'orderbox.views.invalid_login'),
]
