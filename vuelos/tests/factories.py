import factory


class VueloFactory(factory.django.DjangoModelFactory):
    aerolínea = factory.Faker("name")
    fecha = factory.Faker("date")
    hora = factory.Faker("time")
    origen = factory.Faker("name")
    destino = factory.Faker("name")
    capacidad = 10

    class Meta:
        model = "vuelos.Vuelo"
