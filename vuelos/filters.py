from django_filters import rest_framework as filters
from django.db.models import Q
from vuelos.models import Vuelo


class VueloFilterSet(filters.FilterSet):
    search = filters.CharFilter(method="search_func")

    class Meta:
        model = Vuelo
        fields = ()

    def search_func(self, qs, name, value):
        search_or = (
            Q(aerolinea__icontains=value)
            | Q(origen__icontains=value)
            | Q(destino__icontains=value)
        )
        return qs.filter(search_or)
