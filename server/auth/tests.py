from django.test import TestCase, TransactionTestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth.forms import ValidationError
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
        user = create_user(
            username="test_user",
            password="acomplexpassword342@$#",
            password_confirmation="acomplexpassword342@$#",
        )
        self.assertTrue(User.objects.filter(username="test_user").exists())

    def test_bypass_password_confirmation(self):
        user = create_user(
            username="test_user",
            password="acomplexpassword342@$#",
            bypass_confirmation_password=True,
        )

        self.assertTrue(User.objects.filter(username="test_user").exists())

    def test_duplicate_creation(self):
        original_user = create_user(
            username="test_user",
            password="acomplexpassword342@$#",
            bypass_confirmation_password=True,
        )

        self.assertRaises(
            ValueError,
            create_user,
            username="test_user",
            password="acomplexpassword342@$#",
            bypass_confirmation_password=True,
        )

    def test_non_matching_passwords(self):
        self.assertRaises(ValueError, create_user, username="test_user", password="")


class CreateUserAPITestCase(TransactionTestCase):
    def setUp(self):
        super().setUpClass()
        self.user = User.objects.create_user(
            username="test", password="test", email="example@example.com"
        )

    def test_basic(self):
        authenticated_client = Client()
        authenticated_client.force_login(self.user)
        response = authenticated_client.post(
            "/auth/create/",
            {
                "username": "jess",
                "password": "hello",
                "password_confirmation": "hello",
            },
            content_type="application/json",
        )
