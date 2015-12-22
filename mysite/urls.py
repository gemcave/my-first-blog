from django.conf.urls import url, include
from django.contrib import admin

from .routers import router

urlpatterns = [
	#Api and main urls
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
    url(r'^accounts/register/$', 'orderbox.views.register_user'),
    url(r'^accounts/register_success/$', 'orderbox.views.register_success'),
    #Token auth
    url(r'^token-auth/$', 'rest_framework.authtoken.views.obtain_auth_token'),
]
