from django.test import TestCase, TransactionTestCase
from django.contrib.auth.models import User
from django.forms import ValidationError
from .utils import create_user


class AuthAPITestCase(TransactionTestCase):
    def setUp(self):
        super().setUpClass()
        self.user = User.objects.create_user(
            username="test", password="test", email="example@example.com"
        )
        self.user.password = "test"

    def test_login(self):
        response = self.client.post(
            "/auth/login/",
            {"username": self.user.username, "password": self.user.password},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["token"])
        self.assertTrue(response.json()["expiry"])

    def test_logout(self):
        response = self.client.post(
            "/auth/login/",
            {"username": self.user.username, "password": self.user.password},
        )

        token = response.json()["token"]

        test_response = self.client.post(
            "/auth/logout/",
            content_type="application/json",
            headers={
                "Authorization": "Token " + token,
            },
        )

        self.assertEqual(test_response.status_code, 204)

    def test_logoutall(self):
        response = self.client.post(
            "/auth/login/",
            {"username": self.user.username, "password": self.user.password},
        )
        response1 = self.client.post(
            "/auth/login/",
            {"username": self.user.username, "password": self.user.password},
        )

        token = response.json()["token"]
        token1 = response1.json()["token"]

        test_response = self.client.post(
            "/auth/logoutall/",
            content_type="application/json",
            headers={"Authorization": "Token " + token},
        )

        self.assertEqual(test_response.status_code, 204)


class CreateUserTestCase(TestCase):
    def test_successful_creation(self):
        user = create_user(username="jesudas", password="acomplexpassword342@$#")
        user_in_database = User.objects.get(username="jesudas")
        assert type(user) is User
        assert user == user_in_database

    def test_duplicate_creation(self):
        create_user(username="jesudas", password="acomplexpassword342@$#")

        self.assertRaises(
            ValueError,
            create_user,
            "jesudas",
            "acomplexpassword342@$#",
        )


# class CreateUserAPITestCase(TestCase):
