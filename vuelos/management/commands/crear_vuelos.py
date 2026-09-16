from datetime import date, timedelta
from random import choice, randint

from django.core.management.base import BaseCommand

from vuelos.models import Vuelo


class Command(BaseCommand):
    help = "Genera vuelos de prueba"

    def handle(self, *args, **options):
        rutas = [
            ("Buenos Aires", "Córdoba"),
            ("Córdoba", "Buenos Aires"),
            ("Buenos Aires", "Mendoza"),
            ("Mendoza", "Buenos Aires"),
            ("Buenos Aires", "Bariloche"),
            ("Bariloche", "Buenos Aires"),
            ("Buenos Aires", "Iguazú"),
            ("Iguazú", "Buenos Aires"),
            ("Buenos Aires", "Salta"),
            ("Salta", "Buenos Aires"),
            ("Buenos Aires", "Ushuaia"),
            ("Ushuaia", "Buenos Aires"),
            ("Buenos Aires", "Santiago de Chile"),
            ("Santiago de Chile", "Buenos Aires"),
            ("Buenos Aires", "Río de Janeiro"),
            ("Río de Janeiro", "Buenos Aires"),
            ("Buenos Aires", "Lima"),
            ("Lima", "Buenos Aires"),
            ("Buenos Aires", "Madrid"),
            ("Madrid", "Buenos Aires"),
            ("Buenos Aires", "Miami"),
            ("Miami", "Buenos Aires"),
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
