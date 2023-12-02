from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from rest_framework.test import APITestCase

from theatre.models import TheatreHall


class TheatreHallViewSetTests(APITestCase):
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
        content_type = ContentType.objects.get_for_model(TheatreHall)
        permission, created = Permission.objects.get_or_create(
            codename="can_create_theatre_hall",
            name="Can Create TheatreHall",
            content_type=content_type,
        )
        self.user.user_permissions.add(permission)
        self.adminuser.user_permissions.add(permission)

        self.client.force_authenticate(user=self.user)

    def test_list_theatre_halls(self):
        url = "/api/theatre/theatre_halls/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), TheatreHall.objects.count())

    def test_create_theatre_hall(self):
        url = "/api/theatre/theatre_halls/"
        data = {"name": "Blue", "rows": 11, "seats_in_row": 25}
        self.client.force_authenticate(user=self.adminuser)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TheatreHall.objects.get(name="Blue").name, "Blue")
        self.assertEqual(TheatreHall.objects.get(rows=11).rows, 11)
        self.assertEqual(TheatreHall.objects.get(seats_in_row=25).seats_in_row, 25)
