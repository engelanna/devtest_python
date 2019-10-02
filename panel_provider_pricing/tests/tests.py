from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from .factories import UserFactory


class LoginViewTest(TestCase):
    def setUp(self):
        self.user = UserFactory.create(username="Duffy", password="Duck")
        self.response = self.client.post(
            reverse("api_v1_private_login"),
            { "username": self.user.username, "password": self.user.password }
        )

    def test_logging_in(self):
        self.assertEqual(self.response.status_code, HTTP_200_OK)
