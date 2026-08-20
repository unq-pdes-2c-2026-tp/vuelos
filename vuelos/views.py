from rest_framework.viewsets import ReadOnlyModelViewSet

from vuelos.models import Vuelo
from vuelos.serializers import VueloSerializer


class VueloViewSet(ReadOnlyModelViewSet):
    queryset = Vuelo.objects.filter(disponibilidad__gt=0)
    serializer_class = VueloSerializer
