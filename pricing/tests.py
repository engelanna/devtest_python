from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.test import APIRequestFactory
import json


def create_user(username, password):
    return User.objects.create(username=username, password=password)


class LoginViewTests(TestCase):
    def setUp(self):
        self.user = create_user("Duffy", "Duck")
        self.client.login(username=self.user.username, password=self.user.password)
        self.response = self.client.post(
            "api_login",
            { "username": self.user.username, "password": self.user.password },
        )

    def test_logging_in(self):
        self.assertEqual(self.response.status_code, HTTP_200_OK)
