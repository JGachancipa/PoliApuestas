from rest_framework import status
from rest_framework.test import APITestCase

from Sports.test.championship.factories.championship_factories import (
    ChampionshipFactory,
)

# Comando Para Detener Ejecucion
# import pdb; pdb.set_trace()


class ChampionshipTestCase(APITestCase):
    url = "/sports/"

    # Test Consulta Todos Los Campeonatos
    def test_search_all_championships(self):
        response = self.client.get(self.url + "championship/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test Consulta Por Id De Campeonato
    def test_search_championship(self):
        championship = ChampionshipFactory().create_championship()
        response = self.client.get(
            self.url + f"championship/{championship.pk}/", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test Agregar Campeonato
    def test_add_championship(self):
        championship = ChampionshipFactory().build_championship_JSON()
        response = self.client.post(
            self.url + "championship/", championship, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test Actualizar Campeonato
    def test_update_championship(self):
        championship = ChampionshipFactory().create_championship()
        response = self.client.put(
            self.url + f"championship/{championship.pk}/",
            {
                "name": "Test",
                "sport": 1,
                "category": 2,
                "initialDate": "2002-02-02",
                "finalDate": "2022-01-01",
                "description": "Update Test",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data["name"], championship.name)
        self.assertNotEqual(response.data["description"], championship.description)

    # Test Eliminacion Campeonatos
    def test_delete_championship(self):
        championship = ChampionshipFactory().create_championship()
        response = self.client.delete(
            self.url + f"championship/{championship.pk}/", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
