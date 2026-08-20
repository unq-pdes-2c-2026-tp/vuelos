import pytest
from django.urls import reverse

from test_utils.views import get
from vuelos.tests.factories import VueloFactory


@pytest.mark.django_db
def test_get_vuelos_list_available_ones():
    vuelo1 = VueloFactory(disponibilidad=1)
    VueloFactory(disponibilidad=0)

    response = get(reverse("vuelo-list"))

    assert response.status_code == 200
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["id"] == vuelo1.id
