from django.db import transaction
from django.db.models import F
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from vuelos.filters import VueloFilterSet
from vuelos.models import Vuelo, VentaVuelo
from vuelos.serializers import VueloSerializer, VentaVueloSerializer


class VueloViewSet(ReadOnlyModelViewSet):
    queryset = Vuelo.objects.filter(disponibilidad__gt=0)
    serializer_class = VueloSerializer
    filterset_class = VueloFilterSet

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class VentaVueloViewSet(CreateModelMixin, GenericViewSet):
    queryset = VentaVuelo.objects.all()
    serializer_class = VentaVueloSerializer

    @transaction.atomic()
    def perform_create(self, serializer):
        super().perform_create(serializer)
        vuelo: Vuelo = serializer.validated_data["vuelo"]
        vuelo.disponibilidad = F("disponibilidad") - 1
        vuelo.save()
