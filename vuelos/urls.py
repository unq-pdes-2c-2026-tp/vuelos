from rest_framework import routers

from vuelos.views import VueloViewSet, VentaVueloViewSet

router = routers.SimpleRouter()
router.register(r"vuelos", VueloViewSet)
router.register(r"vender", VentaVueloViewSet)

urlpatterns = router.urls
