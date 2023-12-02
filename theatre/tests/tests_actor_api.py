from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from rest_framework.test import APITestCase

from theatre.models import Actor


class ActorViewSetTests(APITestCase):
    def setUp(self):
        self.adminuser = get_user_model().objects.create_user(
            email="admin@example.com",
            password="testpassword",
            is_superuser=True,
            is_staff=True,
        )
        self.user = get_user_model().objects.create_user(
            email="test@example.com", password="testpassword"
        )
        content_type = ContentType.objects.get_for_model(Actor)
        permission, created = Permission.objects.get_or_create(
            codename="can_create_actor",
            name="Can Create Actor",
            content_type=content_type,
        )
        self.user.user_permissions.add(permission)
        self.adminuser.user_permissions.add(permission)

        self.client.force_authenticate(user=self.user)

    def test_list_actors(self):
        url = "/api/theatre/actors/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Actor.objects.count())

    def test_create_actor(self):
        url = "/api/theatre/actors/"
        data = {"first_name": "Dmytro", "last_name": "Stupka"}
        self.client.force_authenticate(user=self.adminuser)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Actor.objects.get(first_name="Dmytro").first_name, "Dmytro")
        self.assertEqual(Actor.objects.get(last_name="Stupka").last_name, "Stupka")
