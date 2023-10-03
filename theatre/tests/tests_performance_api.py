from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
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
        self.play = Play.objects.create(
            title="Play", description="Description", duration=100
        )
        self.theatre_hall = TheatreHall.objects.create(
            name="Name", rows=10, seats_in_row=20
        )

    def test_list_performances(self):
        url = "/api/theatre/performances/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Performance.objects.count())

    def test_create_performance(self):
        url = "/api/theatre/performances/"
        data = {
            "play": self.play.id,
            "theatre_hall": self.theatre_hall.id,
            "show_time": "2023-10-15T15:30:00Z",
        }
        self.client.force_authenticate(user=self.adminuser)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            Performance.objects.filter(
                play=self.play.id,
                theatre_hall=self.theatre_hall,
                show_time="2023-10-15T15:30:00Z",
            ).exists()
        )

    def test_retrieve_performance(self):
        performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.theatre_hall,
            show_time="2023-10-15T15:30:00Z",
        )
        url = reverse("theatre:performance-detail", kwargs={"pk": performance.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], performance.id)
        self.assertEqual(response.data["play"]["id"], self.play.id)
        self.assertEqual(response.data["theatre_hall"]["id"], self.theatre_hall.id)
        self.assertEqual(response.data["show_time"], "2023-10-15T18:30:00+03:00")

    def test_update_performance(self):
        performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.theatre_hall,
            show_time="2023-10-15T15:30:00Z",
        )
        url = reverse("theatre:performance-detail", kwargs={"pk": performance.id})
        updated_data = {
            "play": self.play.id,
            "theatre_hall": self.theatre_hall.id,
            "show_time": "2023-10-16T14:30:00Z",
        }
        self.client.force_authenticate(user=self.adminuser)
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        performance.refresh_from_db()

        self.assertEqual(performance.play.id, self.play.id)
        self.assertEqual(performance.theatre_hall.id, self.theatre_hall.id)

        self.assertEqual(str(performance.show_time), "2023-10-16 14:30:00+00:00")
