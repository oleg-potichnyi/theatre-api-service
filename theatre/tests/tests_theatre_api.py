from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from theatre.models import Genre, Actor, TheatreHall
from theatre.serializers import GenreSerializer


class GenreViewSetTests(APITestCase):
    def test_list_genres(self):
        url = reverse("theatre:genre-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Genre.objects.count())

    def test_create_genre(self):
        url = reverse("theatre:genre-list")
        data = {"name": "Drama"}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Genre.objects.get(name="Drama").name, "Drama")

    def setUp(self):
        self.genre = Genre.objects.create(name="Test Genre")
        self.url = reverse("theatre:genre-detail", args=[self.genre.id])
        self.data = {"name": "Updated Model Genre"}

    def test_retrieve_genre(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, GenreSerializer(self.genre).data)

    def test_update_genre(self):
        response = self.client.put(self.url, data=self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.genre.refresh_from_db()
        self.assertEqual(self.genre.name, self.data["name"])

    def test_partial_update_genre(self):
        response = self.client.patch(self.url, data=self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.genre.refresh_from_db()
        self.assertEqual(self.genre.name, self.data["name"])

    def test_delete_genre(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Genre.objects.filter(id=self.genre.id).exists())


class ActorViewSetTests(APITestCase):
    def test_list_actors(self):
        url = reverse("theatre:actor-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Actor.objects.count())

    def test_create_actor(self):
        url = reverse("theatre:actor-list")
        data = {"first_name": "John", "last_name": "Doe"}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Actor.objects.get(first_name="John").first_name,
            "John"
        )

    def setUp(self):
        self.actor = Actor.objects.create(name="Test Actor")
        self.url = reverse("theatre:actor-detail", args=[self.actor.id])
        self.data = {"name": "Updated Model Actor"}

    def test_retrieve_actor(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, GenreSerializer(self.actor).data)

    def test_update_actor(self):
        response = self.client.put(self.url, data=self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.actor.refresh_from_db()
        self.assertEqual(self.actor.first_name, self.data["first_name"])
        self.assertEqual(self.actor.last_name, self.data["last_name"])

    def test_partial_update_actor(self):
        response = self.client.put(self.url, data=self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.actor.refresh_from_db()
        self.assertEqual(self.actor.first_name, self.data["first_name"])
        self.assertEqual(self.actor.last_name, self.data["last_name"])

    def test_delete_actor(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Actor.objects.filter(id=self.actor.id).exists())


class TheatreHallViewSetTests(APITestCase):
    def test_list_theatre_halls(self):
        url = reverse("theatre:theatrehall-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), TheatreHall.objects.count())

    def test_create_theatre_hall(self):
        url = reverse("theatre:theatrehall-list")
        data = {"name": "Main Hall", "rows": 10, "seats_in_row": 20}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            TheatreHall.objects.get(name="Main Hall").name,
            "Main Hall"
        )

    def setUp(self):
        self.theatre_hall = TheatreHall.objects.create(name="Test TheatreHall")
        self.url = reverse(
            "theatre:theatre_hall-detail",
            args=[self.theatre_hall.id]
        )
        self.data = {"name": "Updated Model TheatreHall"}

    def test_retrieve_theatre_hall(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            GenreSerializer(self.theatre_hall).data
        )

    def test_update_theatre_hall(self):
        response = self.client.put(self.url, data=self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.theatre_hall.refresh_from_db()
        self.assertEqual(self.theatre_hall.name, self.data["name"])

    def test_partial_update_theatre_hall(self):
        response = self.client.put(self.url, data=self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.theatre_hall.refresh_from_db()
        self.assertEqual(self.theatre_hall.first_name, self.data["name"])

    def test_delete_theatre_hall(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            TheatreHall.objects.filter(id=self.theatre_hall.id).exists()
        )
