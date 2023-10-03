from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from rest_framework.test import APITestCase

from theatre.models import Reservation, Play, Performance, TheatreHall


class ReservationViewSetTests(APITestCase):
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
        content_type = ContentType.objects.get_for_model(Reservation)
        permission, created = Permission.objects.get_or_create(
            codename="can_create_reservation",
            name="Can Create Reservation",
            content_type=content_type,
        )
        self.user.user_permissions.add(permission)
        self.adminuser.user_permissions.add(permission)

        self.client.force_authenticate(user=self.user)
        Reservation.objects.create(user=self.user)
        Reservation.objects.create(user=self.user)
        Reservation.objects.create(user=self.adminuser)
        play = Play.objects.create(
            title="Play", description="Description", duration=100
        )
        theatre_hall = TheatreHall.objects.create(name="Name", rows=10, seats_in_row=20)
        show_time = "2023-10-15T15:30:00Z"
        self.performance = Performance.objects.create(
            play_id=play.id,
            theatre_hall_id=theatre_hall.id,
            show_time=show_time,
        )

    def test_create_reservation(self):
        url = "/api/theatre/reservations/"
        data = {
            "tickets": [
                {"row": 1, "seat": 1, "performance": self.performance.id},
                {"row": 2, "seat": 2, "performance": self.performance.id},
            ]
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)
        self.assertIn("tickets", response.data)
        self.assertIn("created_at", response.data)
        created_reservation = Reservation.objects.get(id=response.data["id"])
        self.assertEqual(created_reservation.user, self.user)
        self.assertEqual(created_reservation.tickets.count(), 2)

    def test_list_reservations(self):
        url = "/api/theatre/reservations/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["count"], Reservation.objects.filter(user=self.user).count()
        )
