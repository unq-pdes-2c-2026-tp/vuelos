import factory


class VueloFactory(factory.django.DjangoModelFactory):
    aerolinea = factory.Faker("name")
    fecha = factory.Faker("date")
    hora = factory.Faker("time")
    origen = factory.Faker("name")
    destino = factory.Faker("name")
    capacidad = 10
    disponibilidad = 1

    class Meta:
        model = "vuelos.Vuelo"
