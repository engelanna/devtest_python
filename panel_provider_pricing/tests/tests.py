from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


def create_user(username, password):
    user = User.objects.create(username=username)
    user.set_password(password)
    user.save()
    return user


class LoginViewTests(TestCase):
    def setUp(self):
        self.user = create_user("Duffy", "Duck")
        self.response = self.client.post(
            reverse("api_login"),
            { "username": self.user.username, "password": self.user.password }
        )

    def test_logging_in(self):
        self.assertEqual(self.response.status_code, HTTP_200_OK)
