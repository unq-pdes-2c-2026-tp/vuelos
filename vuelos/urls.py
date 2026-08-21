from rest_framework import routers

from vuelos.views import VueloViewSet

router = routers.SimpleRouter()
router.register(r"vuelos", VueloViewSet)

urlpatterns = router.urls
