from rest_framework.viewsets import ReadOnlyModelViewSet

from vuelos.filters import VueloFilterSet
from vuelos.models import Vuelo
from vuelos.serializers import VueloSerializer


class VueloViewSet(ReadOnlyModelViewSet):
    queryset = Vuelo.objects.filter(disponibilidad__gt=0)
    serializer_class = VueloSerializer
    filterset_class = VueloFilterSet

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
