from Sports.models import Championship
from faker import Faker

faker = Faker()

# Proveedor de datos Pruebas Campeonatos
class ChampionshipFactory:
    def build_championship_JSON(self):
        return {
            "name": faker.name(),
            "sport": 1,
            "category": 2,
            "initialDate":'2002-02-02',
            "finalDate": '2022-01-01',
            "description": faker.text(),
        }

    def create_championship(self):
        return Championship.objects.create(**self.build_championship_JSON())
