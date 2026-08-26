from rest_framework import serializers

from vuelos.models import Vuelo, VentaVuelo


class VueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vuelo
        fields = "__all__"


class VentaVueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaVuelo
        fields = "__all__"

    def validate(self, attrs):
        vuelo: Vuelo = attrs.get("vuelo")
        if vuelo.disponibilidad == 0:
            raise serializers.ValidationError("El vuelo no tiene disponibilidad")
        return attrs
