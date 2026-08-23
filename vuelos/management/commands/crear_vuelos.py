from datetime import date, timedelta
from random import choice, randint

from django.core.management.base import BaseCommand

from vuelos.models import Vuelo


class Command(BaseCommand):
    help = "Genera vuelos de prueba"

    def handle(self, *args, **options):
        rutas = [
            ("Buenos Aires", "Córdoba"),
            ("Buenos Aires", "Mendoza"),
            ("Buenos Aires", "Bariloche"),
            ("Buenos Aires", "Iguazú"),
            ("Buenos Aires", "Salta"),
            ("Buenos Aires", "Ushuaia"),
            ("Buenos Aires", "Santiago de Chile"),
            ("Buenos Aires", "Río de Janeiro"),
            ("Buenos Aires", "Lima"),
            ("Buenos Aires", "Madrid"),
            ("Buenos Aires", "Miami"),
            ("Córdoba", "Buenos Aires"),
            ("Mendoza", "Buenos Aires"),
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

        for _ in range(10):
            origen, destino = choice(rutas)
            capacidad = choice(capacidades)

            vuelos.append(
                Vuelo(
                    aerolinea=choice(aerolineas),
                    fecha=date.today() + timedelta(days=randint(1, 90)),
                    hora=choice(
                        [
                            "06:30",
                            "08:15",
                            "10:45",
                            "13:20",
                            "16:00",
                            "18:30",
                            "21:15",
                        ]
                    ),
                    origen=origen,
                    destino=destino,
                    capacidad=capacidad,
                    disponibilidad=randint(0, capacidad),
                )
            )

        Vuelo.objects.bulk_create(vuelos)

        self.stdout.write(self.style.SUCCESS("Se generaron 10 vuelos correctamente."))
