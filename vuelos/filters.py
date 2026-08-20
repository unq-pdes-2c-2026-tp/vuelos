from django_filters import rest_framework as filters

from vuelos.models import Vuelo


class VueloFilterSet(filters.FilterSet):
    search = filters.CharFilter(method="search_func")

    class Meta:
        model = Vuelo
        fields = ()

    def search_func(self, qs, name, value):
        return qs.filter(aerolinea__icontains=value)
