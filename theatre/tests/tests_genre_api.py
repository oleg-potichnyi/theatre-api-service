from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from theatre.models import Genre, Actor, TheatreHall
from theatre.serializers import GenreSerializer


class GenreViewSetTests(APITestCase):
    def setUp(self):
        self.adminuser = get_user_model().objects.create_user(
            email='admin@example.com',
            password='testpassword',
            is_superuser=True,
            is_staff=True
        )
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpassword'
        )
        content_type = ContentType.objects.get_for_model(Genre)
        permission, created = Permission.objects.get_or_create(
            codename='can_create_genre',
            name='Can Create Genre',
            content_type=content_type
        )
        self.user.user_permissions.add(permission)
        self.adminuser.user_permissions.add(permission)

        self.client.force_authenticate(user=self.user)

    def test_list_genres(self):
        url = "/api/theatre/genres/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Genre.objects.count())

    def test_create_genre(self):
        url = "/api/theatre/genres/"
        data = {"name": "Drama"}
        self.client.force_authenticate(user=self.adminuser)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Genre.objects.get(name="Drama").name, "Drama")

    def test_partial_update_genres(self):
        url = "/api/theatre/genres/1/"
        data = {"name": "Updated Genre Name"}
        self.client.force_authenticate(user=self.adminuser)
        response = self.client.patch(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        genre = Genre.objects.get(pk=1)
        self.assertEqual(genre.name, "Updated Genre Name")


    def test_delete_genres(self):
        self.client.force_authenticate(user=self.adminuser)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Actor.objects.filter(id=self.actor.id).exists())
