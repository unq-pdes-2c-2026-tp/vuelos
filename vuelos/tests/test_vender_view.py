import pytest
from django.urls import reverse

from test_utils.views import post
from vuelos.models import VentaVuelo
from vuelos.tests.factories import VueloFactory


@pytest.mark.django_db
def test_post_vender_creates_venta_vuelo():
    vuelo1 = VueloFactory(disponibilidad=1)

    response = post(
        reverse("ventavuelo-list"),
        {
            "vuelo": vuelo1.id,
            "nombre_pasajero": "Juan",
            "email_pasajero": "pepe@mail.com",
        },
    )

    assert response.status_code == 201
    qs = VentaVuelo.objects.filter(
        vuelo=vuelo1, nombre_pasajero="Juan", email_pasajero="pepe@mail.com"
    )
    assert qs.exists()
    assert qs.first().fecha_venta is not None


@pytest.mark.django_db
def test_post_vender_creates_decrements_availability():
    vuelo1 = VueloFactory(disponibilidad=1)

    response = post(
        reverse("ventavuelo-list"),
        {
            "vuelo": vuelo1.id,
            "nombre_pasajero": "Juan",
            "email_pasajero": "pepe@mail.com",
        },
    )

    assert response.status_code == 201
    vuelo1.refresh_from_db()
    assert vuelo1.disponibilidad == 0


@pytest.mark.django_db
def test_post_vender_without_availability_returns_bad_request():
    vuelo1 = VueloFactory(disponibilidad=0)

    response = post(
        reverse("ventavuelo-list"),
        {
            "vuelo": vuelo1.id,
            "nombre_pasajero": "Juan",
            "email_pasajero": "pepe@mail.com",
        },
    )

    assert response.status_code == 400
    assert response.json() == {"non_field_errors": ["El vuelo no tiene disponibilidad"]}
