from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from theatre.models import Genre, Actor, TheatreHall
from theatre.serializers import GenreSerializer


#
# class GenreViewSetTests(APITestCase):
#     def setUp(self):
#         self.adminuser = get_user_model().objects.create_user(
#             email='admin@example.com',
#             password='testpassword',
#             is_superuser=True,
#             is_staff=True
#         )
#         self.user = get_user_model().objects.create_user(
#             email='test@example.com',
#             password='testpassword'
#         )
#         content_type = ContentType.objects.get_for_model(Genre)
#         permission, created = Permission.objects.get_or_create(
#             codename='can_create_genre',
#             name='Can Create Genre',
#             content_type=content_type
#         )
#         self.user.user_permissions.add(permission)
#         self.adminuser.user_permissions.add(permission)
#
#         self.client.force_authenticate(user=self.user)
#
#
#     def test_list_genres(self):
#         url = '/api/theatre/genres/'
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), Genre.objects.count())
#
#     def test_create_genre(self):
#         url = '/api/theatre/genres/'
#         data = {"name": "Drama"}
#         self.client.force_authenticate(user=self.adminuser)
#         response = self.client.post(url, data)
#
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Genre.objects.get(name="Drama").name, "Drama")
#



# class ActorViewSetTests(APITestCase):
#     def test_list_actors(self):
#         url = reverse("theatre:actor-list")
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), Actor.objects.count())
#
#     def test_create_actor(self):
#         url = reverse("theatre:actor-list")
#         data = {"first_name": "John", "last_name": "Doe"}
#         response = self.client.post(url, data)
#
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(
#             Actor.objects.get(first_name="John").first_name,
#             "John"
#         )
#
#     def setUp(self):
#         self.actor = Actor.objects.create(first_name="Test", last_name="Actor")
#         self.url = reverse("theatre:actor-detail", args=[self.actor.id])
#         self.data = {"first_name": "Updated", "last_name": "Model Actor"}
#
#     def test_retrieve_actor(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, GenreSerializer(self.actor).data)
#
#
#     def test_partial_update_genres(self):
#         self.client.force_authenticate(user=self.adminuser)
#         response = self.client.patch(self.url, data=self.data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.actor.refresh_from_db()
#         self.assertEqual(self.actor.first_name, self.data["first_name"])
#         self.assertEqual(self.actor.last_name, self.data["last_name"])
#
#     def test_delete_actor(self):
#         self.client.force_authenticate(user=self.adminuser)
#         response = self.client.delete(self.url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(Actor.objects.filter(id=self.actor.id).exists())


# class TheatreHallViewSetTests(APITestCase):
#     def test_list_theatre_halls(self):
#         url = reverse("theatre:theatrehall-list")
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), TheatreHall.objects.count())
#
#     def test_create_theatre_hall(self):
#         url = reverse("theatre:theatrehall-list")
#         data = {"name": "Main Hall", "rows": 10, "seats_in_row": 20}
#         response = self.client.post(url, data)
#
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(
#             TheatreHall.objects.get(name="Main Hall").name,
#             "Main Hall"
#         )
#
#     def setUp(self):
#         self.theatre_hall = TheatreHall.objects.create(name="Test TheatreHall")
#         self.url = reverse(
#             "theatre:theatre_hall-detail",
#             args=[self.theatre_hall.id]
#         )
#         self.data = {"name": "Updated Model TheatreHall"}
#
#     def test_retrieve_theatre_hall(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.data,
#             GenreSerializer(self.theatre_hall).data
#         )
#
#     def test_update_theatre_hall(self):
#         response = self.client.put(self.url, data=self.data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.theatre_hall.refresh_from_db()
#         self.assertEqual(self.theatre_hall.name, self.data["name"])
#
#     def test_partial_update_theatre_hall(self):
#         response = self.client.put(self.url, data=self.data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.theatre_hall.refresh_from_db()
#         self.assertEqual(self.theatre_hall.first_name, self.data["name"])
#
#     def test_delete_theatre_hall(self):
#         response = self.client.delete(self.url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(
#             TheatreHall.objects.filter(id=self.theatre_hall.id).exists()
#         )
