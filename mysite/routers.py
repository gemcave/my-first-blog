from rest_framework import routers

from orderbox.views import OrderViewSet


router = routers.SimpleRouter()
router.register('r^order', OrderViewSet)