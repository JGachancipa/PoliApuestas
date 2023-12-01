from rest_framework import status
from rest_framework.test import APITestCase

from Raffle.test.raffle.factories.raffle_factories import (
    RaffleFactory,
)

# Comando Para Detener Ejecucion
# import pdb; pdb.set_trace()


class ChampionshipTestCase(APITestCase):
    url = "/raffle/"

    # Test Consulta Todos Los Campeonatos
    def test_search_all_raffle(self):
        response = self.client.get(self.url + "raffle/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test Consulta Por Id De Campeonato
    def test_search_raffle(self):
        raffle = RaffleFactory().create_raffle()
        response = self.client.get(
            self.url + f"raffle/{raffle.pk}/", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test Agregar Campeonato
    def test_add_raffle(self):
        raffle = RaffleFactory().build_raffle_JSON()
        response = self.client.post(
            self.url + "raffle/", raffle, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test Actualizar Campeonato
    def test_update_raffle(self):
        raffle = RaffleFactory().create_raffle()
        response = self.client.put(
            self.url + f"raffle/{raffle.pk}/",
            {
                "title": "Test",
                "description": "Prueba actualizar",
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
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data["title"], raffle.title)
        self.assertNotEqual(response.data["description"], raffle.description)

    # Test Eliminacion Campeonatos
    def test_delete_raffle(self):
        raffle = RaffleFactory().create_raffle()
        response = self.client.delete(
            self.url + f"raffle/{raffle.pk}/", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
