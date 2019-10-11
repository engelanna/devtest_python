from faker import Faker

from django.contrib.auth.models import User


class UserFactory():

    @classmethod
    def create(cls, username, password):
        new_user = cls.build(username, password)
        new_user.save()

        return new_user

    @classmethod
    def build(cls, username, password):
        new_user = User(username=username, password=password)

        return new_user
