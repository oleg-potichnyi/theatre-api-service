from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from rest_framework.test import APITestCase

from theatre.models import Reservation


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

    def test_list_reservations(self):
        url = "/api/theatre/reservations/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Reservation.objects.filter(user=self.user).count())
