from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ValidationError

from rest_framework.test import APIClient

from .utils import create_user

User = get_user_model()


class AuthAPITestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            password="test",
            email="example@example.com",
            first_name="Joe",
            last_name="Joe",
        )
        cls.user.password = "test"

    def test_login(self):
        response = self.client.post(
            "/api/auth/login/",
            {"username": self.user.email, "password": self.user.password},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["token"])
        self.assertTrue(response.json()["expiry"])


class CreateUserTestCase(TestCase):
    def test_user_creation(self):
        response = self.client.post(
            "/api/user/create/",
            {
                "email": "jess@gmail.com",
                "first_name": "Jesudas",
                "last_name": "Joseph",
                "password": "123456789123456789",
                "password_confirmation": "123456789123456789",
            },
            content_type="application/json",
        )

        assert response.status_code == 201
        user = User.objects.get(email="jess@gmail.com")
        assert user.first_name == "Jesudas"

    def test_user_creation_validation(self):
        response = self.client.post(
            "/api/user/create/",
            {
                "email": "This is not a valid email",
                "last_name": "Joseph",
                "password": "123123123",
                "password_confirmation": "",
            },
            content_type="application/json",
        )

        assert response.status_code == 400
