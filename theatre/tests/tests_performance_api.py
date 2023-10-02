from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.test import APITestCase

from theatre.models import Performance, Play, TheatreHall


class PerformanceViewSetTests(APITestCase):
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
        content_type = ContentType.objects.get_for_model(Performance)
        permission, created = Permission.objects.get_or_create(
            codename="can_create_performance",
            name="Can Create Performance",
            content_type=content_type,
        )
        self.user.user_permissions.add(permission)
        self.adminuser.user_permissions.add(permission)

        self.client.force_authenticate(user=self.user)

    def test_list_performances(self):
        url = "/api/theatre/performances/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Performance.objects.count())

    # def test_create_performance(self):
    #     url = "/api/theatre/performances/"
    #     play_id = 1
    #     theatre_hall_id = 1
    #     play_instance = get_object_or_404(Play, id=play_id)
    #     theatre_hall_instance = get_object_or_404(TheatreHall, id=theatre_hall_id)
    #     data = {
    #         "play": play_instance,
    #         "theatre_hall": theatre_hall_instance,
    #         "show_time": "2023-10-15T15:30:00Z",
    #     }
    #     self.client.force_authenticate(user=self.adminuser)
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertTrue(Performance.objects.filter(
    #         play=play_instance,
    #         theatre_hall=theatre_hall_instance,
    #         show_time="2023-10-15T15:30:00Z").exists()
    #                     )
