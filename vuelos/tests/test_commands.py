import pytest
from django.core.management import call_command

from vuelos.models import Vuelo


@pytest.mark.django_db
def test_crear_vuelos():
    call_command("crear_vuelos")

    vuelos = Vuelo.objects.all()

    assert vuelos.count() == 10

    for vuelo in vuelos:
        assert vuelo.aerolinea
        assert vuelo.fecha
        assert vuelo.hora
        assert vuelo.origen != vuelo.destino
        assert vuelo.capacidad > 0
        assert 0 <= vuelo.disponibilidad <= vuelo.capacidad
