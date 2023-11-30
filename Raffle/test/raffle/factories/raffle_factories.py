from Sports.models import Raffle
from faker import Faker

faker = Faker()

# Proveedor de datos Pruebas Campeonatos
class RaffleFactory:
    def build_raffle_JSON(self):
        return {
            "title": faker.title,
            "description": faker.text(),
            "participating_number": 20,
            "maximum_participant": 100,
            "ticket_value": 1000,
            "sale_start_date": "2023-10-17",
            "sale_end_date": "2023-10-27",
            "game_date": "2023-11-30",
            "main_prize": "Palco Concierto de Karol G",
            "secondary_prize": "2 entradas concierto Karol G",
            "state": True,
            "winnning_number": 259
        }
    def create_raffle(self):
        return Raffle.objects.create(**self.build_raffle_JSON())
