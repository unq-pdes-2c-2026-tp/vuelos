from datetime import date, timedelta
from random import choice, randint

from django.core.management.base import BaseCommand

from vuelos.models import Vuelo


class Command(BaseCommand):
    help = "Genera vuelos de prueba"

    def handle(self, *args, **options):
        today = date.today()
        rutas = [
            ("Mendoza", "Buenos Aires", today, "06:30"),
            ("Buenos Aires", "Mendoza", today + timedelta(days=15), "20:30"),
            ("Buenos Aires", "San Carlos de Bariloche", today, "20:30"),
            (
                "San Carlos de Bariloche",
                "Buenos Aires",
                today + timedelta(days=20),
                "06:30",
            ),
            ("Buenos Aires", "Puerto Iguazú", today, "06:30"),
            ("Puerto Iguazú", "Buenos Aires", today + timedelta(days=15), "20:30"),
        ]

        aerolineas = [
            "Aerolíneas Argentinas",
            "Flybondi",
            "JetSMART",
            "LATAM",
            "GOL",
        ]

        capacidades = [90, 120, 150, 180, 186, 220, 260]

        vuelos = []

        for origen, destino, fecha, hora in rutas:
            capacidad = choice(capacidades)

            vuelos.append(
                Vuelo(
                    aerolinea=choice(aerolineas),
                    fecha=fecha,
                    hora=hora,
                    origen=origen,
                    destino=destino,
                    capacidad=capacidad,
                    disponibilidad=randint(0, capacidad),
                )
            )

        Vuelo.objects.bulk_create(vuelos)

        self.stdout.write(self.style.SUCCESS("Se generaron 10 vuelos correctamente."))
